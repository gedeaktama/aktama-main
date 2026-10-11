<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Page;
use App\Models\SiteSetting;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class MenuController extends Controller
{
    /**
     * Tampilkan Pengaturan Menu Drag & Drop
     */
    public function index(): View
    {
        $pages = Page::where('is_published', true)->orderBy('title')->get();

        $headerMenuRaw = SiteSetting::get('header_navigation_menu', null);
        $headerMenu = $headerMenuRaw ? json_decode($headerMenuRaw, true) : [
            ['label' => 'Beranda', 'url' => '/', 'target' => '_self'],
            ['label' => 'Tentang Kami', 'url' => '/tentang-kami', 'target' => '_self'],
            ['label' => 'Pelatihan AI', 'url' => '/pelatihan-ai', 'target' => '_self'],
            ['label' => 'Jasa Website', 'url' => '/jasa-website', 'target' => '_self'],
            ['label' => 'Kopi', 'url' => '/kopi', 'target' => '_self'],
            ['label' => 'Undangan', 'url' => '/undangan', 'target' => '_self'],
            ['label' => 'Portofolio', 'url' => '/portofolio', 'target' => '_self'],
            ['label' => 'Artikel', 'url' => '/artikel', 'target' => '_self'],
        ];

        $footerMenuRaw = SiteSetting::get('footer_navigation_menu', null);
        $footerMenu = $footerMenuRaw ? json_decode($footerMenuRaw, true) : [
            ['label' => 'Pelatihan Kecerdasan AI', 'url' => '/pelatihan-ai', 'target' => '_self'],
            ['label' => 'Website Perusahaan & Sekolah', 'url' => '/jasa-website', 'target' => '_self'],
            ['label' => 'Pengembangan Aplikasi Web', 'url' => '/jasa-website', 'target' => '_self'],
            ['label' => 'Sistem Kasir & POS Bisnis', 'url' => '/jasa-website', 'target' => '_self'],
            ['label' => 'Portofolio Proyek', 'url' => '/portofolio', 'target' => '_self'],
        ];

        return view('admin.menus.index', compact('pages', 'headerMenu', 'footerMenu'));
    }

    /**
     * Simpan susunan menu navigasi header & footer
     */
    public function update(Request $request): RedirectResponse
    {
        $headerMenu = $request->input('header_menu', '[]');
        $footerMenu = $request->input('footer_menu', '[]');

        SiteSetting::updateOrCreate(
            ['key' => 'header_navigation_menu'],
            [
                'value' => is_string($headerMenu) ? $headerMenu : json_encode($headerMenu),
                'group' => 'menus',
                'type' => 'text',
                'label' => 'Menu Navigasi Header'
            ]
        );

        SiteSetting::updateOrCreate(
            ['key' => 'footer_navigation_menu'],
            [
                'value' => is_string($footerMenu) ? $footerMenu : json_encode($footerMenu),
                'group' => 'menus',
                'type' => 'text',
                'label' => 'Menu Tautan Footer'
            ]
        );

        return back()->with('success', 'Susunan menu navigasi berhasil disimpan!');
    }
}
