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
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class HomeController extends Controller
{
    /**
     * Helper untuk mengambil data setting global secara rapi
     */
    private function getSettings(): array
    {
        return [
            'company_name' => SiteSetting::get('company_name', 'PT Aktama Digital Antika'),
            'brand_name' => SiteSetting::get('brand_name', 'Aktama Digital'),
            'tagline' => SiteSetting::get('tagline', 'Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis Digital'),
            'owner_name' => SiteSetting::get('owner_name', 'Gede Erik Aktama, S.Pd., M.Pd.'),
            'owner_title' => SiteSetting::get('owner_title', 'Dosen Sistem Komputer & Fasilitator Nasional KKA'),
            'owner_bio' => SiteSetting::get('owner_bio', 'Dosen Prodi Sistem Komputer Univ. Parna Raya dan Fasilitator Nasional KKA Kemdikdasmen.'),
            'nib_number' => SiteSetting::get('nib_number', '1703250057018'),
            'lpk_status' => SiteSetting::get('lpk_status', 'Unit LPK PT Aktama Digital Antika'),
            'academy_url' => SiteSetting::get('academy_url', 'http://localhost:8080/aktama/public'),
            'invitation_url' => SiteSetting::get('invitation_url', 'http://localhost:8080/undanganonline/public'),
            'coffee_app_url' => SiteSetting::get('coffee_app_url', 'http://localhost:8080/kopi/public'),
            'coffee_brand_name' => SiteSetting::get('coffee_brand_name', 'Aktama Coffee'),
            'coffee_tagline' => SiteSetting::get('coffee_tagline', 'Distribusi Biji & Bubuk Kopi Berkualitas untuk Retail, Kafe, dan Reseller'),
            'whatsapp_number' => SiteSetting::get('whatsapp_number', '6281234567890'),
            'email' => SiteSetting::get('email', 'kontak@aktama.com'),
            'address' => SiteSetting::get('address', 'Indonesia'),
            'logo_path' => SiteSetting::get('logo_path', 'images/logo-aktama.png'),
            'seal_path' => SiteSetting::get('seal_path', 'images/logo-seal-aktama.png'),
            'favicon_path' => SiteSetting::get('favicon_path', 'images/logo-aktama.png'),
            'topbar_text' => SiteSetting::get('topbar_text', 'PT Aktama Digital Antika'),
            'topbar_highlight' => SiteSetting::get('topbar_highlight', 'NIB: 1703250057018 | LPK Resmi Terdaftar'),
            'footer_description' => SiteSetting::get('footer_description', 'Perusahaan penyedia solusi teknologi terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website & Aplikasi Bisnis, Ekosistem Edukasi Digital, Undangan Online, serta Distribusi Komoditas Kopi Riil.'),
            'footer_copyright' => SiteSetting::get('footer_copyright', '© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.'),
            'header_navigation_menu' => SiteSetting::get('header_navigation_menu', null),
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
        $coffeeProducts = CoffeeProduct::with(['variants' => function ($q) {
                $q->where('is_active', true);
            }])
            ->where('is_published', true)
            ->get();
        $invitationPackages = InvitationPackage::where('is_published', true)->orderBy('sort_order')->get();
        $courses = Course::where('is_published', true)->get();
        $portfolios = Portfolio::where('is_published', true)->get();
        $articles = Article::with('category')
            ->where('status', 'published')
            ->orderByDesc('published_at')
            ->take(3)
            ->get();

        return view('home', compact(
            'settings',
            'homeSections',
            'services',
            'trainingPrograms',
            'coffeeProducts',
            'invitationPackages',
            'courses',
            'portfolios',
            'articles'
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

        return view('pages.training', compact('settings', 'trainingPrograms'));
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
     * Landing Page Khusus Bisnis Kopi (Aktama Coffee)
     */
    public function coffee(): View
    {
        $settings = $this->getSettings();
        $coffeeProducts = CoffeeProduct::with(['variants' => function ($q) {
                $q->where('is_active', true);
            }])
            ->where('is_published', true)
            ->get();

        return view('pages.coffee', compact('settings', 'coffeeProducts'));
    }

    /**
     * Halaman Undangan Online
     */
    public function invitations(): View
    {
        $settings = $this->getSettings();
        $packages = InvitationPackage::where('is_published', true)
            ->orderBy('sort_order')
            ->get();

        return view('pages.invitations', compact('settings', 'packages'));
    }

    /**
     * Halaman Portofolio
     */
    public function portfolios(): View
    {
        $settings = $this->getSettings();
        $portfolios = Portfolio::where('is_published', true)->get();

        return view('pages.portfolios', compact('settings', 'portfolios'));
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

        $articles = Article::with('category')
            ->where('status', 'published')
            ->orderByDesc('published_at')
            ->paginate(6);

        return view('pages.articles', compact('settings', 'articles', 'categories'));
    }

    /**
     * Halaman Detail Artikel
     */
    public function articleShow(string $slug): View
    {
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

        $waTargetNumber = SiteSetting::get('whatsapp_number', '6281234567890');
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

        return back()
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

