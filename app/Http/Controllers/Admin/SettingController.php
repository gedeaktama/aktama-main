<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\SiteSetting;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class SettingController extends Controller
{
    /**
     * Tampilkan Pengaturan Situs Lengkap (CMS Settings)
     */
    public function index(): View
    {
        $settings = SiteSetting::all()->keyBy('key');
        return view('admin.settings.index', compact('settings'));
    }

    /**
     * Simpan Pembaruan Pengaturan Termasuk Upload Logo, Cap & Favicon
     */
    public function update(Request $request): RedirectResponse
    {
        $request->validate([
            'logo_file' => 'nullable|image|mimes:png,jpg,jpeg,svg,webp|max:2048',
            'seal_file' => 'nullable|image|mimes:png,jpg,jpeg,svg,webp|max:2048',
            'favicon_file' => 'nullable|image|mimes:png,jpg,jpeg,svg,ico,webp|max:1024',
        ]);

        $uploadDir = public_path('images/branding');
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        // 1. Upload Logo Utama Navbar
        if ($request->hasFile('logo_file')) {
            $logoFile = $request->file('logo_file');
            $logoName = 'logo-' . time() . '.' . $logoFile->getClientOriginalExtension();
            $logoFile->move($uploadDir, $logoName);
            SiteSetting::updateOrCreate(
                ['key' => 'logo_path'],
                ['value' => 'images/branding/' . $logoName, 'group' => 'media', 'type' => 'image', 'label' => 'Path Logo Utama Navbar']
            );
        }

        // 2. Upload Cap Resmi Perusahaan
        if ($request->hasFile('seal_file')) {
            $sealFile = $request->file('seal_file');
            $sealName = 'seal-' . time() . '.' . $sealFile->getClientOriginalExtension();
            $sealFile->move($uploadDir, $sealName);
            SiteSetting::updateOrCreate(
                ['key' => 'seal_path'],
                ['value' => 'images/branding/' . $sealName, 'group' => 'media', 'type' => 'image', 'label' => 'Path Cap Resmi Perusahaan']
            );
        }

        // 3. Upload Favicon Tab Browser
        if ($request->hasFile('favicon_file')) {
            $favFile = $request->file('favicon_file');
            $favName = 'favicon-' . time() . '.' . $favFile->getClientOriginalExtension();
            $favFile->move($uploadDir, $favName);
            SiteSetting::updateOrCreate(
                ['key' => 'favicon_path'],
                ['value' => 'images/branding/' . $favName, 'group' => 'media', 'type' => 'image', 'label' => 'Path Favicon Tab Browser']
            );
        }

        // 4. Update Seluruh Bidang Teks
        $data = $request->except(['_token', '_method', 'logo_file', 'seal_file', 'favicon_file']);

        foreach ($data as $key => $value) {
            SiteSetting::updateOrCreate(
                ['key' => $key],
                ['value' => $value]
            );
        }

        return back()->with('success', 'Pengaturan situs, logo, header dan footer berhasil diperbarui!');
    }
}
