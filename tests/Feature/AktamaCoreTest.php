<?php

namespace Tests\Feature;

use App\Models\Lead;
use App\Models\User;
use Database\Seeders\DatabaseSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;

class AktamaCoreTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        $this->seed(DatabaseSeeder::class);
    }
    /**
     * Uji seluruh halaman publik mengembalikan status 200 OK.
     */
    public function test_public_pages_return_successful_response(): void
    {
        $routes = [
            '/',
            '/tentang-kami',
            '/pelatihan-ai',
            '/jasa-website',
            '/portofolio',
            '/artikel',
            '/sitemap.xml',
        ];

        foreach ($routes as $route) {
            $response = $this->get($route);
            $response->assertStatus(200);
        }

        // Uji rute kopi dan undangan memuat halaman dengan sukses
        $this->get('/kopi')->assertStatus(200);
        $this->get('/undangan')->assertStatus(200);
    }

    /**
     * Uji formulir calon pelanggan memvalidasi dan menyimpan ke database.
     */
    public function test_lead_submission_saves_to_database(): void
    {
        $payload = [
            'name' => 'Dr. H. Hendra Setiawan',
            'whatsapp' => '081298765432',
            'email' => 'hendra@dinas.go.id',
            'organization' => 'Dinas Pendidikan Kota',
            'service_type' => 'pelatihan-ai',
            'budget_range' => '3jt - 10jt',
            'message' => 'Permohonan pelaksanaan pelatihan AI untuk staf administrasi.',
        ];

        $response = $this->post('/inquiry', $payload);

        $response->assertSessionHas('success');
        $this->assertDatabaseHas('leads', [
            'name' => 'Dr. H. Hendra Setiawan',
            'whatsapp' => '081298765432',
            'service_type' => 'pelatihan-ai',
        ]);
    }

    /**
     * Uji proteksi keamanan: Tamu tanpa login ditolak dari dashboard admin.
     */
    public function test_guest_is_redirected_from_admin_dashboard(): void
    {
        $response = $this->get('/admin/dashboard');
        $response->assertRedirect('/admin/login');
    }

    /**
     * Uji otentikasi login admin berhasil dan membuka dashboard.
     */
    public function test_admin_can_authenticate_and_access_dashboard(): void
    {
        $admin = User::firstOrCreate(
            ['email' => 'admin_test@aktama.com'],
            [
                'name' => 'Admin Test',
                'password' => Hash::make('Secret123!'),
                'role' => 'admin',
            ]
        );

        $response = $this->post('/admin/login', [
            'email' => 'admin_test@aktama.com',
            'password' => 'Secret123!',
        ]);

        $response->assertRedirect(route('admin.dashboard'));
        $this->assertAuthenticatedAs($admin);

        // Uji akses langsung dashboard setelah login
        $dashResponse = $this->actingAs($admin)->get('/admin/dashboard');
        $dashResponse->assertStatus(200);
        $dashResponse->assertSee('Ringkasan Ekosistem Bisnis Aktama');
    }

    /**
     * Uji login ditolak jika password salah.
     */
    public function test_invalid_login_credentials_are_rejected(): void
    {
        $response = $this->post('/admin/login', [
            'email' => 'admin_test@aktama.com',
            'password' => 'PasswordSalahTotal',
        ]);

        $response->assertSessionHas('error');
        $this->assertGuest();
    }

    /**
     * Uji validasi formulir inquiry menolak input kosong.
     */
    public function test_lead_submission_validates_required_fields(): void
    {
        $response = $this->post('/inquiry', []);

        $response->assertSessionHasErrors(['name', 'whatsapp', 'service_type', 'message']);
    }

    /**
     * Uji admin dapat memperbarui status lead.
     */
    public function test_admin_can_update_lead_status(): void
    {
        $admin = User::first();
        $lead = Lead::create([
            'name' => 'Calon Klien Pelatihan',
            'whatsapp' => '081234567890',
            'service_type' => 'pelatihan-ai',
            'message' => 'Permintaan in-house training.',
            'status' => 'new',
        ]);

        $response = $this->actingAs($admin)->put(route('admin.leads.status', ['lead' => $lead->id]), [
            'status' => 'contacted',
            'admin_notes' => 'Sudah dikontak via WhatsApp resmi.',
        ]);

        $response->assertRedirect();
        $this->assertDatabaseHas('leads', [
            'id' => $lead->id,
            'status' => 'contacted',
            'admin_notes' => 'Sudah dikontak via WhatsApp resmi.',
        ]);
    }

    /**
     * Uji admin dapat menambahkan layanan baru ke CMS.
     */
    public function test_admin_can_create_service(): void
    {
        $admin = User::first();

        $response = $this->actingAs($admin)->post(route('admin.services.store'), [
            'title' => 'Audit Keamanan & Pembersihan Malware',
            'category' => 'website',
            'icon' => 'bi-shield-check',
            'excerpt' => 'Layanan audit kode dan pembersihan backlink judol pada website.',
            'description' => 'Deskripsi lengkap pembersihan injeksi malware.',
            'price_starting' => 'Mulai Rp 1.500.000',
            'is_published' => 1,
            'sort_order' => 10,
        ]);

        $response->assertRedirect(route('admin.services.index'));
        $this->assertDatabaseHas('services', [
            'title' => 'Audit Keamanan & Pembersihan Malware',
            'category' => 'website',
        ]);
    }

    /**
     * Uji admin dapat memperbarui pengaturan situs (Site Settings).
     */
    public function test_admin_can_update_site_settings(): void
    {
        $admin = User::first();

        $response = $this->actingAs($admin)
            ->from(route('admin.settings.index'))
            ->post(route('admin.settings.update'), [
                'company_name' => 'PT Aktama Digital Antika Corp',
                'brand_name' => 'Aktama Digital Official',
                'coffee_brand_name' => 'Kopi Robusta Aktama',
            ]);

        $response->assertRedirect(route('admin.settings.index'));
        $this->assertDatabaseHas('site_settings', [
            'key' => 'company_name',
            'value' => 'PT Aktama Digital Antika Corp',
        ]);
        $this->assertDatabaseHas('site_settings', [
            'key' => 'coffee_brand_name',
            'value' => 'Kopi Robusta Aktama',
        ]);
    }

    /**
     * Uji halaman artikel dapat membaca artikel berdasarkan slug.
     */
    public function test_article_detail_page_loads_published_article(): void
    {
        $response = $this->get('/artikel/fenomena-web-sekolah-disusupi-spam-judol-dan-solusinya');
        $response->assertStatus(200);
        $response->assertSee('Fenomena Web Sekolah & Instansi Disusupi Spam Judol');
    }

    /**
     * Uji proteksi Honeypot menolak bot spam tanpa menyimpan ke database leads.
     */
    public function test_honeypot_rejects_spam_bot_submission_without_saving_lead(): void
    {
        $response = $this->post(route('inquiry.store'), [
            'aktama_hp_check' => 'http://spam-link-bot.com',
            'name' => 'Spam Bot',
            'whatsapp' => '0899999999',
            'message' => 'Spam content',
            'service_type' => 'jasa-website',
        ]);

        $response->assertRedirect();
        $this->assertDatabaseMissing('leads', [
            'name' => 'Spam Bot',
        ]);
    }

    /**
     * Uji admin dapat membuka halaman profil dan memperbarui kata sandi.
     */
    public function test_admin_can_access_profile_and_change_password(): void
    {
        $admin = User::first();

        $response = $this->actingAs($admin)->get(route('admin.profile'));
        $response->assertStatus(200);
        $response->assertSee('Profil Administrator & Keamanan Akun');

        $updateResponse = $this->actingAs($admin)->put(route('admin.profile.password'), [
            'current_password' => 'AdminAktama2026!',
            'password' => 'PasswordBaruAktama2026!',
            'password_confirmation' => 'PasswordBaruAktama2026!',
        ]);

        $updateResponse->assertSessionHas('success');
        $this->assertTrue(Hash::check('PasswordBaruAktama2026!', $admin->fresh()->password));
    }

    /**
     * Uji floating WhatsApp dan Schema.org JSON-LD termuat di halaman depan.
     */
    public function test_floating_whatsapp_and_schema_rendered_in_homepage(): void
    {
        $response = $this->get('/');
        $response->assertStatus(200);
        $response->assertSee('floating-wa-btn');
        $response->assertSee('6285341026331');
        $response->assertSee('gedeerikaktama@gmail.com');
        $response->assertSee('application/ld+json');
    }

    /**
     * Uji halaman 404 kustom menampilkan identitas Aktama.
     */
    public function test_custom_404_page_renders_with_aktama_branding(): void
    {
        $response = $this->get('/halaman-acak-yang-tidak-ada-12345');
        $response->assertStatus(404);
        $response->assertSee('Halaman Tidak Ditemukan');
        $response->assertSee('Kembali ke Beranda');
    }
}
