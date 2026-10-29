<?php

namespace Tests\Feature;

use App\Models\ActivityLog;
use App\Models\Article;
use App\Models\Category;
use App\Models\Page;
use App\Models\SiteSetting;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AktamaAdvancedWordPressProductivityTest extends TestCase
{
    use RefreshDatabase;

    private User $admin;

    protected function setUp(): void
    {
        parent::setUp();

        $this->admin = User::factory()->create([
            'email' => 'admin@aktama.com',
            'role' => 'admin',
        ]);
    }

    public function test_signature_is_removed_from_homepage_and_about_page(): void
    {
        $responseHome = $this->get('/');
        $responseHome->assertStatus(200);
        $responseHome->assertDontSee('gede-ttd.png');
        $responseHome->assertDontSee('alt="Tanda Tangan Direktur"', false);

        $responseAbout = $this->get('/tentang-kami');
        $responseAbout->assertStatus(200);
        $responseAbout->assertDontSee('gede-ttd.png');
        $responseAbout->assertDontSee('alt="Tanda Tangan Direktur"', false);
    }

    public function test_announcement_bar_can_be_configured_and_renders_on_frontend(): void
    {
        $this->actingAs($this->admin)->post(route('admin.settings.update'), [
            'announcement_enabled' => '1',
            'announcement_badge' => 'DISKON 20%',
            'announcement_text' => 'Pendaftaran Pelatihan AI Batch 2 Telah Dibuka',
            'announcement_link_text' => 'Daftar Sekarang',
            'announcement_link_url' => 'https://wa.me/6285341026331',
            'announcement_bg_color' => '#dc2626',
        ]);

        $response = $this->get('/');
        $response->assertStatus(200);
        $response->assertSee('DISKON 20%');
        $response->assertSee('Pendaftaran Pelatihan AI Batch 2 Telah Dibuka');
        $response->assertSee('Daftar Sekarang');
    }

    public function test_admin_can_duplicate_page_and_quick_edit_page(): void
    {
        $page = Page::create([
            'title' => 'Landing Page Original',
            'slug' => 'landing-page-original',
            'editor_type' => 'builder',
            'template' => 'full-width',
            'content_html' => '<div>Konten visual</div>',
            'is_published' => true,
        ]);

        // 1. Uji Duplikasi
        $responseDuplicate = $this->actingAs($this->admin)->post(route('admin.pages.duplicate', $page->id));
        $responseDuplicate->assertRedirect();

        $duplicatedPage = Page::where('slug', 'landing-page-original-salinan')->first();
        $this->assertNotNull($duplicatedPage);
        $this->assertEquals('Landing Page Original (Salinan)', $duplicatedPage->title);
        $this->assertFalse((bool) $duplicatedPage->is_published);

        // 2. Uji Quick Edit
        $responseQuickEdit = $this->actingAs($this->admin)->put(route('admin.pages.quickUpdate', $duplicatedPage->id), [
            'title' => 'Landing Page Promosi Cepat',
            'slug' => 'landing-page-promosi-cepat',
            'template' => 'blank',
            'sort_order' => 5,
            'is_published' => '1',
        ]);
        $responseQuickEdit->assertSessionHas('success');

        $duplicatedPage->refresh();
        $this->assertEquals('Landing Page Promosi Cepat', $duplicatedPage->title);
        $this->assertEquals('landing-page-promosi-cepat', $duplicatedPage->slug);
        $this->assertEquals('blank', $duplicatedPage->template);
        $this->assertTrue((bool) $duplicatedPage->is_published);
    }

    public function test_admin_can_duplicate_article_and_quick_edit_article(): void
    {
        $category = Category::create(['name' => 'Teknologi AI', 'slug' => 'teknologi-ai']);
        $category2 = Category::create(['name' => 'Rekayasa Web', 'slug' => 'rekayasa-web']);

        $article = Article::create([
            'title' => 'Tutorial AI Modern',
            'slug' => 'tutorial-ai-modern',
            'category_id' => $category->id,
            'summary' => 'Ringkasan tutorial',
            'content' => '<p>Isi tutorial lengkap</p>',
            'status' => 'published',
        ]);

        // 1. Duplikasi Artikel
        $responseDup = $this->actingAs($this->admin)->post(route('admin.articles.duplicate', $article->id));
        $responseDup->assertRedirect();

        $dupArticle = Article::where('slug', 'tutorial-ai-modern-salinan')->first();
        $this->assertNotNull($dupArticle);
        $this->assertEquals('draft', $dupArticle->status);

        // 2. Quick Edit Artikel
        $responseQE = $this->actingAs($this->admin)->put(route('admin.articles.quickUpdate', $dupArticle->id), [
            'title' => 'Tutorial AI Terkini 2026',
            'slug' => 'tutorial-ai-terkini-2026',
            'category_id' => $category2->id,
            'status' => 'published',
        ]);
        $responseQE->assertSessionHas('success');

        $dupArticle->refresh();
        $this->assertEquals('Tutorial AI Terkini 2026', $dupArticle->title);
        $this->assertEquals($category2->id, $dupArticle->category_id);
        $this->assertEquals('published', $dupArticle->status);
    }

    public function test_sitemap_and_rss_feeds_return_valid_xml(): void
    {
        $category = Category::create(['name' => 'Sains Komputer', 'slug' => 'sains-komputer']);
        Article::create([
            'title' => 'Berita Teknologi Terkini',
            'slug' => 'berita-teknologi-terkini',
            'category_id' => $category->id,
            'summary' => 'Ringkasan berita',
            'content' => '<p>Konten berita</p>',
            'status' => 'published',
        ]);

        Page::create([
            'title' => 'Halaman Layanan Khusus',
            'slug' => 'halaman-layanan-khusus',
            'editor_type' => 'standard',
            'is_published' => true,
        ]);

        // Uji Sitemap XML
        $responseSitemap = $this->get('/sitemap.xml');
        $responseSitemap->assertStatus(200);
        $responseSitemap->assertHeader('Content-Type', 'application/xml; charset=utf-8');
        $responseSitemap->assertSee('berita-teknologi-terkini');
        $responseSitemap->assertSee('halaman-layanan-khusus');

        // Uji RSS Feed XML
        $responseRss = $this->get('/rss.xml');
        $responseRss->assertStatus(200);
        $responseRss->assertHeader('Content-Type', 'application/xml; charset=utf-8');
        $responseRss->assertSee('<rss version="2.0"', false);
        $responseRss->assertSee('Berita Teknologi Terkini');
    }

    public function test_activity_log_records_events_and_renders_in_admin(): void
    {
        ActivityLog::record('login', 'User berhasil login', 'User', $this->admin->id);
        ActivityLog::record('create', 'Membuat artikel baru', 'Artikel', 1);

        $response = $this->actingAs($this->admin)->get(route('admin.activityLogs.index'));
        $response->assertStatus(200);
        $response->assertSee('User berhasil login');
        $response->assertSee('Membuat artikel baru');
    }

    public function test_backup_page_and_download_database_stream(): void
    {
        $responsePage = $this->actingAs($this->admin)->get(route('admin.backup.index'));
        $responsePage->assertStatus(200);
        $responsePage->assertSee('Cadangan Database MySQL');
        $responsePage->assertSee('Cadangan Berkas Media & Upload', false);

        $responseDb = $this->actingAs($this->admin)->get(route('admin.backup.database'));
        $responseDb->assertStatus(200);
        $responseDb->assertHeader('Content-Type', 'application/sql');
    }
}
