<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\ActivityLog;
use App\Models\Page;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class PageController extends Controller
{
    /**
     * Tampilkan daftar halaman CMS layaknya WordPress Pages
     */
    public function index(Request $request): View
    {
        $query = Page::query();

        if ($request->filled('status')) {
            if ($request->status === 'published') {
                $query->where('is_published', true);
            } elseif ($request->status === 'draft') {
                $query->where('is_published', false);
            }
        }

        if ($request->filled('q')) {
            $keyword = trim($request->q);
            $query->where(function ($q) use ($keyword) {
                $q->where('title', 'like', "%{$keyword}%")
                  ->orWhere('slug', 'like', "%{$keyword}%");
            });
        }

        $pages = $query->orderBy('sort_order')->orderByDesc('created_at')->paginate(15)->withQueryString();

        $counts = [
            'all' => Page::count(),
            'published' => Page::where('is_published', true)->count(),
            'draft' => Page::where('is_published', false)->count(),
        ];

        return view('admin.pages.index', compact('pages', 'counts'));
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
            'template' => 'nullable|string|in:default,full-width,blank',
            'featured_image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'sort_order' => 'nullable|integer',
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

        // Upload Gambar Unggulan Halaman
        $featuredImage = null;
        if ($request->hasFile('featured_image_file')) {
            $dir = public_path('images/pages');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('featured_image_file');
            $fileName = 'page-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $featuredImage = 'pages/' . $fileName;
        }

        $page = Page::create([
            'title' => $validated['title'],
            'slug' => $slug,
            'editor_type' => $validated['editor_type'],
            'template' => $validated['template'] ?? 'default',
            'featured_image' => $featuredImage,
            'sort_order' => $validated['sort_order'] ?? 0,
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
            'content_html' => $validated['content_html'] ?? ($validated['editor_type'] === 'builder' ? '<div class="py-5 text-center"><h2>' . e($validated['title']) . '</h2><p class="lead text-muted">Selamat datang di halaman baru.</p></div>' : '<p>Tuliskan konten halaman Anda di sini...</p>'),
            'is_published' => $request->has('is_published'),
        ]);

        ActivityLog::record('create', "Membuat halaman baru: '{$page->title}'", 'Halaman', $page->id);

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
            'template' => 'nullable|string|in:default,full-width,blank',
            'featured_image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'remove_featured_image' => 'nullable|boolean',
            'sort_order' => 'nullable|integer',
            'meta_title' => 'nullable|string|max:200',
            'meta_description' => 'nullable|string|max:300',
            'content_html' => 'nullable|string',
            'is_published' => 'nullable|boolean',
        ]);

        $featuredImage = $page->featured_image;
        if ($request->boolean('remove_featured_image')) {
            $featuredImage = null;
        }
        if ($request->hasFile('featured_image_file')) {
            $dir = public_path('images/pages');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('featured_image_file');
            $fileName = 'page-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $featuredImage = 'pages/' . $fileName;
        }

        $page->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'editor_type' => $validated['editor_type'],
            'template' => $validated['template'] ?? 'default',
            'featured_image' => $featuredImage,
            'sort_order' => $validated['sort_order'] ?? 0,
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
            'content_html' => $validated['content_html'] ?? $page->content_html,
            'is_published' => $request->has('is_published'),
        ]);

        ActivityLog::record('update', "Memperbarui rincian halaman: '{$page->title}'", 'Halaman', $page->id);

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

        ActivityLog::record('update', "Menyimpan rancangan visual canvas pada halaman: '{$page->title}'", 'Halaman', $page->id);

        return response()->json([
            'success' => true,
            'message' => 'Desain halaman visual berhasil disimpan!',
        ]);
    }

    /**
     * 1-Click Duplicate Halaman (Yoast Duplicate Post style)
     */
    public function duplicate(Page $page): RedirectResponse
    {
        $newTitle = $page->title . ' (Salinan)';
        $baseSlug = Str::slug($page->slug . '-salinan');
        $slug = $baseSlug;
        $counter = 1;
        while (Page::where('slug', $slug)->exists()) {
            $slug = $baseSlug . '-' . $counter++;
        }

        $newPage = Page::create([
            'title' => $newTitle,
            'slug' => $slug,
            'editor_type' => $page->editor_type,
            'template' => $page->template,
            'content_html' => $page->content_html,
            'content_css' => $page->content_css,
            'content_json' => $page->content_json,
            'featured_image' => $page->featured_image,
            'sort_order' => $page->sort_order + 1,
            'meta_title' => $page->meta_title ? $page->meta_title . ' (Salinan)' : $newTitle,
            'meta_description' => $page->meta_description,
            'is_published' => false, // Default draf untuk keamanan
        ]);

        ActivityLog::record('duplicate', "Menduplikasi halaman: '{$page->title}' menjadi '{$newTitle}'", 'Halaman', $newPage->id);

        if ($newPage->editor_type === 'builder') {
            return redirect()->route('admin.pages.builder', $newPage->id)
                ->with('success', 'Halaman berhasil diduplikasi! Anda sekarang berada di kanvas visual salinan.');
        }

        return redirect()->route('admin.pages.edit', $newPage->id)
            ->with('success', 'Halaman berhasil diduplikasi! Silakan sesuaikan judul dan konten.');
    }

    /**
     * Quick Edit Halaman (WordPress Quick Edit style)
     */
    public function quickUpdate(Request $request, Page $page): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'slug' => 'required|string|max:200|unique:pages,slug,' . $page->id,
            'template' => 'required|string|in:default,full-width,blank',
            'sort_order' => 'nullable|integer',
            'is_published' => 'nullable|boolean',
        ]);

        $page->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'template' => $validated['template'],
            'sort_order' => $validated['sort_order'] ?? 0,
            'is_published' => $request->has('is_published'),
        ]);

        ActivityLog::record('quick_update', "Quick Edit halaman: '{$page->title}'", 'Halaman', $page->id);

        return back()->with('success', 'Halaman "' . $page->title . '" berhasil diperbarui dengan Quick Edit!');
    }

    /**
     * Hapus halaman
     */
    public function destroy(Page $page): RedirectResponse
    {
        $title = $page->title;
        $id = $page->id;
        $page->delete();

        ActivityLog::record('delete', "Menghapus halaman: '{$title}'", 'Halaman', $id);

        return redirect()->route('admin.pages.index')->with('success', 'Halaman berhasil dihapus.');
    }
}
