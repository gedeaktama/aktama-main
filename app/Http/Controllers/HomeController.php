<?php

namespace App\Http\Controllers;

use App\Models\Article;
use App\Models\Category;
use App\Models\CoffeeProduct;
use App\Models\Course;
use App\Models\HomeSection;
use App\Models\InvitationPackage;
use App\Models\Lead;
use App\Models\Page;
use App\Models\Portfolio;
use App\Models\Service;
use App\Models\SiteSetting;
use App\Models\TrainingProgram;
use App\Services\InquiryNotificationService;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Schema;
use Illuminate\View\View;

class HomeController extends Controller
{
    /**
     * Helper untuk mengambil data setting global secara rapi
     */
    private function getSettings(): array
    {
        $isProd = app()->environment('production');
        $profileUrl = $isProd ? 'https://profil.aktama.com' : 'http://localhost:8080/portofolio/public';
        $academyUrl = $isProd ? 'https://academy.aktama.com' : 'http://localhost:8080/aktama/public';
        $invitationUrl = $isProd ? 'https://undangan.aktama.com' : 'http://localhost:8080/undanganonline/public';
        $coffeeUrl = $isProd ? 'https://coffee.aktama.com' : 'http://localhost:8080/kopi/public';

        return [
            'company_name' => SiteSetting::get('company_name', 'PT Aktama Digital Antika'),
            'brand_name' => SiteSetting::get('brand_name', 'Aktama Digital'),
            'tagline' => SiteSetting::get('tagline', 'Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis Digital'),
            'owner_name' => SiteSetting::get('owner_name', 'Gede Erik Aktama, S.Pd., M.Pd.'),
            'owner_title' => SiteSetting::get('owner_title', 'Dosen Sistem Komputer & Fasilitator Nasional KKA'),
            'owner_bio' => SiteSetting::get('owner_bio', 'Dosen Prodi Sistem Komputer Univ. Parna Raya dan Fasilitator Nasional KKA Kemdikdasmen.'),
            'nib_number' => SiteSetting::get('nib_number', '1703250057018'),
            'lpk_status' => SiteSetting::get('lpk_status', 'Unit LPK PT Aktama Digital Antika'),
            'academy_url' => SiteSetting::get('academy_url', $academyUrl),
            'invitation_url' => SiteSetting::get('invitation_url', $invitationUrl),
            'coffee_app_url' => SiteSetting::get('coffee_app_url', $coffeeUrl),
            'profile_url' => SiteSetting::get('profile_url', $profileUrl),
            'coffee_brand_name' => SiteSetting::get('coffee_brand_name', 'Aktama Coffee'),
            'coffee_tagline' => SiteSetting::get('coffee_tagline', 'Unit Bisnis Roastery & Distribusi Komoditas Kopi Nusantara'),
            'whatsapp_number' => SiteSetting::get('whatsapp_number', '6285341026331'),
            'email' => SiteSetting::get('email', 'gedeerikaktama@gmail.com'),
            'address' => SiteSetting::get('address', 'Indonesia'),
            'instagram_url' => SiteSetting::get('instagram_url', 'https://instagram.com/aktama.digital'),
            'linkedin_url' => SiteSetting::get('linkedin_url', 'https://linkedin.com/in/gedeerikaktama'),
            'youtube_url' => SiteSetting::get('youtube_url', 'https://youtube.com/@aktama'),
            'facebook_url' => SiteSetting::get('facebook_url', ''),
            'logo_path' => SiteSetting::get('logo_path', 'images/logo-aktama.png'),
            'seal_path' => SiteSetting::get('seal_path', 'images/logo-seal-aktama.png'),
            'favicon_path' => SiteSetting::get('favicon_path', 'images/logo-aktama.png'),
            'topbar_text' => SiteSetting::get('topbar_text', 'PT Aktama Digital Antika'),
            'topbar_highlight' => SiteSetting::get('topbar_highlight', 'NIB: 1703250057018 • LPK Resmi Terdaftar'),
            'footer_description' => SiteSetting::get('footer_description', 'Perusahaan penyedia solusi teknologi terpadu: Jasa Pembuatan Website & Aplikasi Bebas Malware, Pelatihan Kecerdasan Artifisial (AI) Terapan, serta Ekosistem Produk Digital Mandiri.'),
            'footer_copyright' => SiteSetting::get('footer_copyright', '© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.'),
            'header_navigation_menu' => SiteSetting::get('header_navigation_menu', null),
            'announcement_enabled' => SiteSetting::get('announcement_enabled', '0'),
            'announcement_text' => SiteSetting::get('announcement_text', '🔥 Promo Spesial: Konsultasi Pembuatan Website & Pelatihan AI Bersertifikat Resmi Terbuka!'),
            'announcement_badge' => SiteSetting::get('announcement_badge', 'PROMO TERBATAS'),
            'announcement_link_text' => SiteSetting::get('announcement_link_text', 'Konsultasi Sekarang'),
            'announcement_link_url' => SiteSetting::get('announcement_link_url', 'https://wa.me/6285341026331'),
            'announcement_bg_color' => SiteSetting::get('announcement_bg_color', '#4f46e5'),
        ];
    }

    /**
     * Beranda Utama
     */
    public function index(): View
    {
        $settings = $this->getSettings();

        // Opsi A: Seksi Beranda Modular & Dynamic Order
        $homeSections = HomeSection::orderBy('sort_order')->get();

        $services = Service::where('is_published', true)->orderBy('sort_order')->get();
        $trainingPrograms = TrainingProgram::where('is_published', true)->orderBy('sort_order')->get();
        $courses = Course::where('is_published', true)->get();
        $portfolios = Portfolio::where('is_published', true)->get();
        $articles = Article::with('category')
            ->where('status', 'published')
            ->orderByDesc('published_at')
            ->take(3)
            ->get();
        $coffeeProducts = Schema::hasTable('coffee_products')
            ? CoffeeProduct::with('variants')->where('is_published', true)->orderBy('sort_order')->get()
            : collect();
        $invitationPackages = Schema::hasTable('invitation_packages')
            ? InvitationPackage::where('is_published', true)->orderBy('sort_order')->get()
            : collect();

        return view('home', compact(
            'settings',
            'homeSections',
            'services',
            'trainingPrograms',
            'courses',
            'portfolios',
            'articles',
            'coffeeProducts',
            'invitationPackages'
        ));
    }

    /**
     * Halaman Tentang Kami
     */
    public function about(): View
    {
        $settings = $this->getSettings();
        return view('pages.about', compact('settings'));
    }

    /**
     * Halaman Pelatihan AI
     */
    public function training(): View
    {
        $settings = $this->getSettings();
        $trainingPrograms = TrainingProgram::where('is_published', true)
            ->orderBy('sort_order')
            ->get();
        $courses = Course::where('is_published', true)->get();

        return view('pages.training', compact('settings', 'trainingPrograms', 'courses'));
    }

    /**
     * Halaman Jasa Website & Solusi Digital
     */
    public function services(): View
    {
        $settings = $this->getSettings();
        $services = Service::where('is_published', true)
            ->orderBy('sort_order')
            ->get();

        return view('pages.services', compact('settings', 'services'));
    }

    /**
     * Halaman Lini Usaha Komoditas Kopi (Aktama Coffee)
     */
    public function coffee(): View
    {
        $settings = $this->getSettings();
        $coffeeProducts = Schema::hasTable('coffee_products')
            ? CoffeeProduct::with('variants')->where('is_published', true)->orderBy('sort_order')->get()
            : collect();
        return view('pages.coffee', compact('settings', 'coffeeProducts'));
    }

    /**
     * Halaman Platform Undangan Online Digital
     */
    public function invitations(): View
    {
        $settings = $this->getSettings();
        $packages = Schema::hasTable('invitation_packages')
            ? InvitationPackage::where('is_published', true)->orderBy('sort_order')->get()
            : collect();
        $invitationPackages = $packages;
        return view('pages.invitations', compact('settings', 'packages', 'invitationPackages'));
    }

    /**
     * Halaman Portofolio
     */
    public function portfolios(): View
    {
        $settings = $this->getSettings();
        
        $portfolioCategories = Portfolio::where('is_published', true)
            ->whereNotNull('category')
            ->distinct()
            ->pluck('category');

        $query = Portfolio::where('is_published', true);

        if ($cat = request('kategori')) {
            $query->where('category', $cat);
        }

        if ($search = trim((string) request('q'))) {
            $query->where(function ($q) use ($search) {
                $q->where('title', 'like', "%{$search}%")
                  ->orWhere('description', 'like', "%{$search}%")
                  ->orWhere('technologies', 'like', "%{$search}%")
                  ->orWhere('client_type', 'like', "%{$search}%");
            });
        }

        $portfolios = $query->orderBy('sort_order')->get();
        $activeCategory = request('kategori');
        $searchQuery = request('q');

        return view('pages.portfolios', compact('settings', 'portfolios', 'portfolioCategories', 'activeCategory', 'searchQuery'));
    }

    /**
     * Halaman Indeks Artikel Blog
     */
    public function articles(): View
    {
        $settings = $this->getSettings();
        $categories = Category::withCount(['articles' => function ($q) {
            $q->where('status', 'published');
        }])->get();

        $query = Article::with('category')
            ->where('status', 'published');

        if ($catSlug = request('kategori')) {
            $query->whereHas('category', function ($q) use ($catSlug) {
                $q->where('slug', $catSlug);
            });
        }

        if ($search = trim((string) request('q'))) {
            $query->where(function ($q) use ($search) {
                $q->where('title', 'like', "%{$search}%")
                  ->orWhere('summary', 'like', "%{$search}%")
                  ->orWhere('content', 'like', "%{$search}%")
                  ->orWhere('tags', 'like', "%{$search}%");
            });
        }

        $articles = $query->orderByDesc('published_at')
            ->paginate(12)
            ->withQueryString();

        $activeCategory = request('kategori');
        $searchQuery = request('q');

        return view('pages.articles', compact('settings', 'articles', 'categories', 'activeCategory', 'searchQuery'));
    }

    /**
     * Halaman Detail Artikel
     */
    public function articleShow(string $slug): View|\Illuminate\Http\RedirectResponse
    {
        // 301 Permanent Redirect untuk URL artikel lama ke artikel baru yang komprehensif
        $legacyRedirects = [
            'mengapa-website-bisnis-harus-aman-dari-celah-malware-judol' => 'fenomena-web-sekolah-disusupi-spam-judol-dan-solusinya',
            'peran-kecerdasan-artifisial-dalam-meningkatkan-produktivitas-kerja-administrasi' => 'pemanfaatan-generative-ai-efisiensi-kerja-administratif-instansi',
        ];

        if (isset($legacyRedirects[$slug])) {
            return redirect()->route('articles.show', $legacyRedirects[$slug], 301);
        }

        $settings = $this->getSettings();
        $article = Article::with('category')
            ->where('slug', $slug)
            ->where('status', 'published')
            ->firstOrFail();

        $relatedArticles = Article::where('id', '!=', $article->id)
            ->where('status', 'published')
            ->where('category_id', $article->category_id)
            ->take(3)
            ->get();

        return view('pages.article-show', compact('settings', 'article', 'relatedArticles'));
    }

    /**
     * Handler Penyimpanan Formulir Calon Pelanggan (Leads)
     */
    public function storeInquiry(Request $request): RedirectResponse
    {
        // 1. Proteksi Anti-Spam (Honeypot): Jika field jebakan ini diisi oleh robot, gagalkan secara senyap
        if ($request->filled('aktama_hp_check')) {
            return redirect()->to(url()->previous() . '#form-konsultasi')
                ->with('success', 'Permintaan konsultasi Anda telah diproses.');
        }

        $validated = $request->validate([
            'name' => 'required|string|max:100',
            'whatsapp' => 'required|string|max:30',
            'email' => 'nullable|email|max:100',
            'organization' => 'nullable|string|max:150',
            'service_type' => 'required|string|max:50',
            'budget_range' => 'nullable|string|max:50',
            'message' => 'required|string|max:2000',
        ]);

        $lead = Lead::create([
            ...$validated,
            'source_page' => $request->input('source_page', 'Website Utama'),
            'status' => 'new',
            'ip_address' => $request->ip(),
        ]);

        InquiryNotificationService::notifyAdminNewInquiry($lead);

        $waTargetNumber = SiteSetting::get('whatsapp_number', '6285341026331');
        $cleanPhone = preg_replace('/[^0-9]/', '', $waTargetNumber);
        if (str_starts_with($cleanPhone, '0')) {
            $cleanPhone = '62' . substr($cleanPhone, 1);
        }

        $waText = "Halo Aktama Digital,\n\n" .
            "Saya *{$lead->name}*" . ($lead->organization ? " dari *{$lead->organization}*" : "") . " ingin berkonsultasi mengenai:\n" .
            "• Layanan: *{$lead->service_label}*\n" .
            "• WhatsApp: {$lead->whatsapp}\n" .
            ($lead->email ? "• Email: {$lead->email}\n" : "") .
            ($lead->budget_range ? "• Anggaran: {$lead->budget_range}\n" : "") .
            "• Rincian Kebutuhan: \"{$lead->message}\"\n\n" .
            "Mohon informasi dan tindak lanjutnya. Terima kasih!";

        $waDirectUrl = "https://wa.me/{$cleanPhone}?text=" . urlencode($waText);

        $previousUrl = url()->previous();
        $targetRedirect = str_contains($previousUrl, '#form-konsultasi')
            ? $previousUrl
            : $previousUrl . '#form-konsultasi';

        return redirect()->to($targetRedirect)
            ->with('success', 'Permintaan konsultasi Anda telah tersimpan dengan aman di sistem kami! Tim kami akan segera menindaklanjuti.')
            ->with('wa_direct_url', $waDirectUrl);
    }

    /**
     * Opsi B: Halaman Kustom Publik (CMS Dynamic Pages)
     */
    public function customPage(string $slug): View
    {
        $settings = $this->getSettings();
        $page = Page::where('slug', $slug)
            ->where('is_published', true)
            ->firstOrFail();

        return view('pages.custom', compact('settings', 'page'));
    }
}

