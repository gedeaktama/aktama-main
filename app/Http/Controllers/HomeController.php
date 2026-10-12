<?php

namespace App\Http\Controllers;

use App\Models\Article;
use App\Models\Category;
use App\Models\Course;
use App\Models\HomeSection;
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
            'academy_url' => SiteSetting::get('academy_url', 'https://academy.aktama.com'),
            'invitation_url' => SiteSetting::get('invitation_url', 'https://undanganonline.aktama.com'),
            'coffee_app_url' => SiteSetting::get('coffee_app_url', 'https://coffee.aktama.com'),
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

        return view('home', compact(
            'settings',
            'homeSections',
            'services',
            'trainingPrograms',
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
     * Gateway Redirect ke Platform Kopi (Aktama Coffee)
     */
    public function coffee(): RedirectResponse
    {
        $url = SiteSetting::get('coffee_app_url', 'https://coffee.aktama.com');
        return redirect()->away($url);
    }

    /**
     * Gateway Redirect ke Platform Undangan Online
     */
    public function invitations(): RedirectResponse
    {
        $url = SiteSetting::get('invitation_url', 'https://undanganonline.aktama.com');
        return redirect()->away($url);
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

