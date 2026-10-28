<?php

namespace Tests\Feature;

use App\Models\Article;
use App\Models\Category;
use App\Models\HomeSection;
use App\Models\Page;
use App\Models\SiteSetting;
use App\Models\User;
use Database\Seeders\DatabaseSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Http\UploadedFile;
use Tests\TestCase;

class AktamaCmsWordPressFeaturesTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        $this->seed(DatabaseSeeder::class);
    }

    private function getAdminUser(): User
    {
        return User::where('role', 'admin')->first();
    }

    /**
     * 1. Uji Opsi A: Seksi Beranda Modular & Drag-and-Drop Reorder
     */
    public function test_home_sections_drag_and_drop_reorder(): void
    {
        $admin = $this->getAdminUser();

        $sections = HomeSection::orderBy('sort_order')->get();
        $this->assertGreaterThanOrEqual(8, $sections->count());

        // Balik urutan seksi
        $reversedIds = $sections->pluck('id')->reverse()->values()->all();

        $response = $this->actingAs($admin)->postJson('/admin/sections/reorder', [
            'order' => $reversedIds
        ]);

        $response->assertStatus(200);
        $response->assertJson(['success' => true]);

        // Cek urutan baru di database
        $firstReordered = HomeSection::find($reversedIds[0]);
        $this->assertEquals(1, $firstReordered->sort_order);
    }

    /**
     * 2. Uji Opsi A: Toggle Visibilitas Seksi Beranda
     */
    public function test_home_section_toggle_visibility(): void
    {
        $admin = $this->getAdminUser();
        $section = HomeSection::where('section_key', 'ekosistem_digital')->first();
        $this->assertTrue($section->is_active);

        // Nonaktifkan seksi
        $response = $this->actingAs($admin)->post("/admin/sections/{$section->id}/toggle");
        $response->assertRedirect();

        $section->refresh();
        $this->assertFalse($section->is_active);

        // Kunjungi beranda, seksi ekosistem digital tidak boleh muncul
        $homeResponse = $this->get('/');
        $homeResponse->assertStatus(200);
        $homeResponse->assertDontSee('id="ekosistem-digital"', false);
    }

    /**
     * 3. Uji Opsi B: Tambah Halaman Kustom & Visual Canvas Builder
     */
    public function test_admin_can_create_custom_page_and_visual_builder_saves(): void
    {
        $admin = $this->getAdminUser();

        // Buat halaman baru dengan builder
        $createResponse = $this->actingAs($admin)->post('/admin/pages', [
            'title' => 'Program Magang Mahasiswa',
            'slug' => 'program-magang-mahasiswa',
            'editor_type' => 'builder',
            'meta_title' => 'Program Magang Mahasiswa | Aktama Digital',
            'meta_description' => 'Informasi pendaftaran magang industri.',
            'is_published' => '1',
        ]);

        $page = Page::where('slug', 'program-magang-mahasiswa')->first();
        $this->assertNotNull($page);
        $createResponse->assertRedirect(route('admin.pages.builder', $page->id));

        // Simpan desain visual canvas (HTML & CSS)
        $customHtml = '<div class="magang-hero"><h1>Magang Bersama Aktama Digital</h1><p>Dapatkan pengalaman industri nyata.</p></div>';
        $customCss = '.magang-hero { background: #4f46e5; color: #fff; padding: 2rem; }';

        $builderSaveResponse = $this->actingAs($admin)->postJson("/admin/pages/{$page->id}/builder", [
            'html' => $customHtml,
            'css' => $customCss,
            'components' => json_encode(['mock' => 'component']),
        ]);

        $builderSaveResponse->assertStatus(200);
        $builderSaveResponse->assertJson(['success' => true]);

        $page->refresh();
        $this->assertEquals($customHtml, $page->content_html);
        $this->assertEquals($customCss, $page->content_css);

        // Akses halaman publik /halaman/program-magang-mahasiswa
        $publicResponse = $this->get('/halaman/program-magang-mahasiswa');
        $publicResponse->assertStatus(200);
        $publicResponse->assertSee('Magang Bersama Aktama Digital');
        $publicResponse->assertSee('.magang-hero { background: #4f46e5;', false);
    }

    /**
     * 4. Uji Pengaturan Menu Navigasi Drag & Drop
     */
    public function test_admin_can_save_drag_and_drop_navigation_menus(): void
    {
        $admin = $this->getAdminUser();

        $customHeaderMenu = [
            ['label' => 'Beranda Utama', 'url' => '/', 'target' => '_self'],
            ['label' => 'Program Magang', 'url' => '/halaman/magang', 'target' => '_blank'],
            ['label' => 'Hubungi Kami', 'url' => '#form-konsultasi', 'target' => '_self'],
        ];

        // Pastikan halaman admin menu menampilkan tombol edit dan modal edit
        $menuPageResponse = $this->actingAs($admin)->get('/admin/menus');
        $menuPageResponse->assertStatus(200);
        $menuPageResponse->assertSee('btn-edit-item', false);
        $menuPageResponse->assertSee('modalEditMenu', false);
        $menuPageResponse->assertSee('Edit Item Menu Navigasi');

        $response = $this->actingAs($admin)->post('/admin/menus', [
            'header_menu' => json_encode($customHeaderMenu),
            'footer_menu' => json_encode([['label' => 'Privasi', 'url' => '/halaman/kebijakan-privasi', 'target' => '_self']]),
        ]);

        $response->assertRedirect();

        // Periksa setting tersimpan di database
        $savedMenu = SiteSetting::get('header_navigation_menu');
        $this->assertNotNull($savedMenu);
        $this->assertStringContainsString('Program Magang', $savedMenu);

        // Kunjungi web publik, navbar harus menampilkan menu dinamis
        $homeResponse = $this->get('/');
        $homeResponse->assertStatus(200);
        $homeResponse->assertSee('Program Magang');
        $homeResponse->assertSee('/halaman/magang');
    }

    /**
     * 5. Uji Ganti Logo, Topbar, dan Footer dari Admin
     */
    public function test_admin_can_update_logo_topbar_and_footer(): void
    {
        $admin = $this->getAdminUser();

        $fakeLogo = UploadedFile::fake()->image('custom-logo.png', 200, 50);

        $response = $this->actingAs($admin)->post('/admin/settings', [
            'logo_file' => $fakeLogo,
            'topbar_text' => 'PT Aktama Digital Antika (Holding)',
            'topbar_highlight' => 'LPK Nasional Terakreditasi A',
            'footer_description' => 'Solusi software house terpercaya bebas malware judol.',
            'footer_copyright' => '© 2026 PT Aktama Digital Antika. Custom Footer.',
            'company_name' => 'PT Aktama Digital Antika',
            'brand_name' => 'Aktama Digital',
            'whatsapp_number' => '6281234567890',
            'email' => 'kontak@aktama.com',
        ]);

        $response->assertRedirect();

        // Kunjungi publik dan pastikan info baru tampil
        $homeResponse = $this->get('/');
        $homeResponse->assertStatus(200);
        $homeResponse->assertSee('PT Aktama Digital Antika (Holding)');
        $homeResponse->assertSee('LPK Nasional Terakreditasi A');
        $homeResponse->assertSee('Custom Footer.');
    }

    /**
     * 6. Uji Postingan / Berita Lengkap dengan Kategori dan Gambar
     */
    public function test_admin_can_create_post_with_category_and_publish(): void
    {
        $admin = $this->getAdminUser();

        $fakeImage = UploadedFile::fake()->image('berita-ai.jpg', 600, 400);

        $response = $this->actingAs($admin)->post('/admin/articles', [
            'title' => 'Peluncuran Fitur AI Terkini untuk Pemerintahan',
            'new_category' => 'Inovasi Birokrasi',
            'summary' => 'Ringkasan berita inovasi birokrasi cerdas.',
            'content' => '<p>Pemerintah daerah kini mengadopsi AI untuk pengarsipan cepat.</p>',
            'image_file' => $fakeImage,
            'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
            'status' => 'published',
            'meta_title' => 'Inovasi AI Birokrasi | Berita Aktama',
        ]);

        $response->assertRedirect(route('admin.articles.index'));

        // Cek di database
        $article = Article::where('title', 'Peluncuran Fitur AI Terkini untuk Pemerintahan')->first();
        $this->assertNotNull($article);
        $this->assertEquals('published', $article->status);
        $this->assertNotNull($article->category_id);
        $this->assertEquals('Inovasi Birokrasi', $article->category->name);

        // Kunjungi detail berita publik
        $showResponse = $this->get("/artikel/{$article->slug}");
        $showResponse->assertStatus(200);
        $showResponse->assertSee('Peluncuran Fitur AI Terkini untuk Pemerintahan');
        $showResponse->assertSee('Inovasi Birokrasi');
    }
}
