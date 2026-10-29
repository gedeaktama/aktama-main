<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        if ($this->app->environment('production')) {
            \Illuminate\Support\Facades\URL::forceScheme('https');
        }

        // Bagikan variabel setting situs secara konsisten ke seluruh template view
        \Illuminate\Support\Facades\View::composer(['layouts.app', 'layouts.admin', 'pages.*', 'partials.*'], function ($view) {
            if (!isset($view->getData()['settings'])) {
                try {
                    $isProd = app()->environment('production');
                    $profileUrl = $isProd ? 'https://profil.aktama.com' : 'http://localhost:8080/portofolio/public';
                    $academyUrl = $isProd ? 'https://academy.aktama.com' : 'http://localhost:8080/aktama/public';
                    $invitationUrl = $isProd ? 'https://undangan.aktama.com' : 'http://localhost:8080/undanganonline/public';
                    $coffeeUrl = $isProd ? 'https://coffee.aktama.com' : 'http://localhost:8080/kopi/public';

                    $settings = [
                        'company_name' => \App\Models\SiteSetting::get('company_name', 'PT Aktama Digital Antika'),
                        'brand_name' => \App\Models\SiteSetting::get('brand_name', 'Aktama Digital'),
                        'tagline' => \App\Models\SiteSetting::get('tagline', 'Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis Digital'),
                        'owner_name' => \App\Models\SiteSetting::get('owner_name', 'Gede Erik Aktama, S.Pd., M.Pd.'),
                        'owner_title' => \App\Models\SiteSetting::get('owner_title', 'Dosen Sistem Komputer & Fasilitator Nasional KKA'),
                        'owner_bio' => \App\Models\SiteSetting::get('owner_bio', 'Dosen Prodi Sistem Komputer Univ. Parna Raya dan Fasilitator Nasional KKA Kemdikdasmen.'),
                        'nib_number' => \App\Models\SiteSetting::get('nib_number', '1703250057018'),
                        'lpk_status' => \App\Models\SiteSetting::get('lpk_status', 'Unit LPK PT Aktama Digital Antika'),
                        'academy_url' => \App\Models\SiteSetting::get('academy_url', $academyUrl),
                        'invitation_url' => \App\Models\SiteSetting::get('invitation_url', $invitationUrl),
                        'coffee_app_url' => \App\Models\SiteSetting::get('coffee_app_url', $coffeeUrl),
                        'profile_url' => \App\Models\SiteSetting::get('profile_url', $profileUrl),
                        'coffee_brand_name' => \App\Models\SiteSetting::get('coffee_brand_name', 'Aktama Coffee'),
                        'coffee_tagline' => \App\Models\SiteSetting::get('coffee_tagline', 'Unit Bisnis Roastery & Distribusi Komoditas Kopi Nusantara'),
                        'whatsapp_number' => \App\Models\SiteSetting::get('whatsapp_number', '6285341026331'),
                        'email' => \App\Models\SiteSetting::get('email', 'gedeerikaktama@gmail.com'),
                        'address' => \App\Models\SiteSetting::get('address', 'Indonesia'),
                        'instagram_url' => \App\Models\SiteSetting::get('instagram_url', 'https://instagram.com/aktama.digital'),
                        'linkedin_url' => \App\Models\SiteSetting::get('linkedin_url', 'https://linkedin.com/in/gedeerikaktama'),
                        'youtube_url' => \App\Models\SiteSetting::get('youtube_url', 'https://youtube.com/@aktama'),
                        'facebook_url' => \App\Models\SiteSetting::get('facebook_url', ''),
                        'logo_path' => \App\Models\SiteSetting::get('logo_path', 'images/logo-aktama.png'),
                        'seal_path' => \App\Models\SiteSetting::get('seal_path', 'images/logo-seal-aktama.png'),
                        'favicon_path' => \App\Models\SiteSetting::get('favicon_path', 'images/logo-aktama.png'),
                        'topbar_text' => \App\Models\SiteSetting::get('topbar_text', 'PT Aktama Digital Antika'),
                        'topbar_highlight' => \App\Models\SiteSetting::get('topbar_highlight', 'NIB: 1703250057018 • LPK Resmi Terdaftar'),
                        'footer_description' => \App\Models\SiteSetting::get('footer_description', 'Perusahaan penyedia solusi teknologi terpadu: Jasa Pembuatan Website & Aplikasi Bebas Malware, Pelatihan Kecerdasan Artifisial (AI) Terapan, serta Ekosistem Produk Digital Mandiri.'),
                        'footer_copyright' => \App\Models\SiteSetting::get('footer_copyright', '© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.'),
                        'header_navigation_menu' => \App\Models\SiteSetting::get('header_navigation_menu', null),
                        'announcement_enabled' => \App\Models\SiteSetting::get('announcement_enabled', '0'),
                        'announcement_text' => \App\Models\SiteSetting::get('announcement_text', '🔥 Promo Spesial: Konsultasi Pembuatan Website & Pelatihan AI Bersertifikat Resmi Terbuka!'),
                        'announcement_badge' => \App\Models\SiteSetting::get('announcement_badge', 'PROMO TERBATAS'),
                        'announcement_link_text' => \App\Models\SiteSetting::get('announcement_link_text', 'Konsultasi Sekarang'),
                        'announcement_link_url' => \App\Models\SiteSetting::get('announcement_link_url', 'https://wa.me/6285341026331'),
                        'announcement_bg_color' => \App\Models\SiteSetting::get('announcement_bg_color', '#4f46e5'),
                    ];
                    $view->with('settings', $settings);
                } catch (\Throwable $e) {
                    // Fail silently during initial migrations or testing
                }
            }
        });
    }
}
