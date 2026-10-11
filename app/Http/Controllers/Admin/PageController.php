<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Page;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class PageController extends Controller
{
    /**
     * Tampilkan daftar halaman CMS
     */
    public function index(): View
    {
        $pages = Page::orderBy('sort_order')->orderByDesc('created_at')->paginate(15);
        return view('admin.pages.index', compact('pages'));
    }

    /**
     * Form buat halaman baru
     */
    public function create(): View
    {
        return view('admin.pages.form', ['page' => new Page()]);
    }

    /**
     * Simpan halaman baru
     */
    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'slug' => 'nullable|string|max:200|unique:pages,slug',
            'editor_type' => 'required|in:builder,standard',
            'meta_title' => 'nullable|string|max:200',
            'meta_description' => 'nullable|string|max:300',
            'content_html' => 'nullable|string',
            'is_published' => 'nullable|boolean',
        ]);

        $slug = !empty($validated['slug']) ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        // Pastikan slug unik
        $originalSlug = $slug;
        $counter = 1;
        while (Page::where('slug', $slug)->exists()) {
            $slug = $originalSlug . '-' . $counter++;
        }

        $page = Page::create([
            'title' => $validated['title'],
            'slug' => $slug,
            'editor_type' => $validated['editor_type'],
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
            'content_html' => $validated['content_html'] ?? ($validated['editor_type'] === 'builder' ? '<div class="py-5 text-center"><h2>' . e($validated['title']) . '</h2><p class="lead text-muted">Selamat datang di halaman baru.</p></div>' : '<p>Konten halaman...</p>'),
            'is_published' => $request->has('is_published'),
        ]);

        if ($page->editor_type === 'builder') {
            return redirect()->route('admin.pages.builder', $page->id)
                ->with('success', 'Halaman berhasil dibuat! Silakan desain visual dengan Drag & Drop Canvas.');
        }

        return redirect()->route('admin.pages.index')->with('success', 'Halaman baru berhasil disimpan!');
    }

    /**
     * Form edit rincian halaman
     */
    public function edit(Page $page): View
    {
        return view('admin.pages.form', compact('page'));
    }

    /**
     * Simpan pembaruan halaman
     */
    public function update(Request $request, Page $page): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'slug' => 'required|string|max:200|unique:pages,slug,' . $page->id,
            'editor_type' => 'required|in:builder,standard',
            'meta_title' => 'nullable|string|max:200',
            'meta_description' => 'nullable|string|max:300',
            'content_html' => 'nullable|string',
            'is_published' => 'nullable|boolean',
        ]);

        $page->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'editor_type' => $validated['editor_type'],
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
            'content_html' => $validated['content_html'] ?? $page->content_html,
            'is_published' => $request->has('is_published'),
        ]);

        return redirect()->route('admin.pages.index')->with('success', 'Halaman berhasil diperbarui!');
    }

    /**
     * Tampilan Visual Drag & Drop Canvas Builder (Opsi B: GrapesJS)
     */
    public function builder(Page $page): View
    {
        return view('admin.pages.builder', compact('page'));
    }

    /**
     * AJAX endpoint penyimpanan dari Visual Drag & Drop Canvas
     */
    public function saveBuilder(Request $request, Page $page): JsonResponse
    {
        $request->validate([
            'html' => 'required|string',
            'css' => 'nullable|string',
            'components' => 'nullable|string',
        ]);

        $page->update([
            'content_html' => $request->input('html'),
            'content_css' => $request->input('css'),
            'content_json' => $request->input('components'),
        ]);

        return response()->json([
            'success' => true,
            'message' => 'Desain halaman visual berhasil disimpan!',
        ]);
    }

    /**
     * Hapus halaman
     */
    public function destroy(Page $page): RedirectResponse
    {
        $page->delete();
        return redirect()->route('admin.pages.index')->with('success', 'Halaman berhasil dihapus.');
    }
}
