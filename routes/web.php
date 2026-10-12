<?php

use App\Http\Controllers\Admin\ArticleController as AdminArticleController;
use App\Http\Controllers\Admin\AuthController as AdminAuthController;
use App\Http\Controllers\Admin\DashboardController as AdminDashboardController;
use App\Http\Controllers\Admin\HomeSectionController as AdminHomeSectionController;
use App\Http\Controllers\Admin\LeadController as AdminLeadController;
use App\Http\Controllers\Admin\MenuController as AdminMenuController;
use App\Http\Controllers\Admin\PageController as AdminPageController;
use App\Http\Controllers\Admin\PortfolioController as AdminPortfolioController;
use App\Http\Controllers\Admin\ServiceController as AdminServiceController;
use App\Http\Controllers\Admin\SettingController as AdminSettingController;
use App\Http\Controllers\Admin\TrainingProgramController as AdminTrainingController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\SitemapController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| 1. RUTE PUBLIK (PORTAL UTAMA AKTAMA DIGITAL)
|--------------------------------------------------------------------------
*/
Route::controller(HomeController::class)->group(function () {
    Route::get('/', 'index')->name('home');
    Route::get('/tentang-kami', 'about')->name('about');
    Route::get('/pelatihan-ai', 'training')->name('training');
    Route::get('/jasa-website', 'services')->name('services');
    Route::get('/kopi', 'coffee')->name('coffee');
    Route::get('/undangan', 'invitations')->name('invitations');
    Route::get('/portofolio', 'portfolios')->name('portfolios');
    Route::get('/artikel', 'articles')->name('articles.index');
    Route::get('/artikel/{slug}', 'articleShow')->name('articles.show');
    Route::get('/halaman/{slug}', 'customPage')->name('pages.show');
    Route::post('/inquiry', 'storeInquiry')->middleware('throttle:6,1')->name('inquiry.store');
});

// Dynamic XML Sitemap untuk Mesin Pencari
Route::get('/sitemap.xml', [SitemapController::class, 'index'])->name('sitemap');

/*
|--------------------------------------------------------------------------
| 2. RUTE AUTENTIKASI ADMIN
|--------------------------------------------------------------------------
*/
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/login', [AdminAuthController::class, 'showLogin'])->name('login');
    Route::post('/login', [AdminAuthController::class, 'login'])->middleware('throttle:5,1')->name('login.submit');
    Route::post('/logout', [AdminAuthController::class, 'logout'])->middleware('auth')->name('logout');

    /*
    |--------------------------------------------------------------------------
    | 3. CMS DASHBOARD & PENGELOLAAN (PROTECTED BY ADMIN MIDDLEWARE)
    |--------------------------------------------------------------------------
    */
    Route::middleware(['auth', 'admin'])->group(function () {
        Route::get('/dashboard', [AdminDashboardController::class, 'index'])->name('dashboard');
        Route::get('/profile', [AdminAuthController::class, 'showProfile'])->name('profile');
        Route::put('/profile/password', [AdminAuthController::class, 'updatePassword'])->name('profile.password');

        // Pengaturan Situs & Media Branding (Logo, Topbar, Footer)
        Route::get('/settings', [AdminSettingController::class, 'index'])->name('settings.index');
        Route::post('/settings', [AdminSettingController::class, 'update'])->name('settings.update');

        // Opsi A: Seksi Beranda Modular & Drag & Drop Reordering
        Route::get('/sections', [AdminHomeSectionController::class, 'index'])->name('sections.index');
        Route::get('/sections/{section}/edit', [AdminHomeSectionController::class, 'edit'])->name('sections.edit');
        Route::put('/sections/{section}', [AdminHomeSectionController::class, 'update'])->name('sections.update');
        Route::post('/sections/reorder', [AdminHomeSectionController::class, 'reorder'])->name('sections.reorder');
        Route::post('/sections/{section}/toggle', [AdminHomeSectionController::class, 'toggle'])->name('sections.toggle');

        // Opsi B: Halaman Kustom & Visual Drag & Drop Canvas Builder (GrapesJS)
        Route::resource('pages', AdminPageController::class)->except(['show']);
        Route::get('/pages/{page}/builder', [AdminPageController::class, 'builder'])->name('pages.builder');
        Route::post('/pages/{page}/builder', [AdminPageController::class, 'saveBuilder'])->name('pages.saveBuilder');

        // Pengaturan Menu Navigasi Drag & Drop (Header & Footer)
        Route::get('/menus', [AdminMenuController::class, 'index'])->name('menus.index');
        Route::post('/menus', [AdminMenuController::class, 'update'])->name('menus.update');

        // Manajemen Calon Pelanggan (Leads)
        Route::resource('leads', AdminLeadController::class)->only(['index', 'show', 'destroy']);
        Route::put('/leads/{lead}/status', [AdminLeadController::class, 'updateStatus'])->name('leads.status');

        // Manajemen Artikel Blog / Postingan Berita & SEO
        Route::resource('articles', AdminArticleController::class)->except(['show']);

        // Manajemen Layanan Website & Aplikasi
        Route::resource('services', AdminServiceController::class)->except(['show']);

        // Manajemen Pelatihan AI
        Route::resource('training', AdminTrainingController::class)->except(['show']);

        // Manajemen Portofolio
        Route::resource('portfolios', AdminPortfolioController::class)->except(['show']);
    });
});
