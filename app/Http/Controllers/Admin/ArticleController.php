<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Article;
use App\Models\Category;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class ArticleController extends Controller
{
    /**
     * Tampilkan daftar seluruh postingan artikel / berita layaknya WordPress Posts Manager
     */
    public function index(Request $request): View
    {
        $query = Article::with('category');

        // Filter Status: All, Published, Draft
        if ($request->filled('status') && in_array($request->status, ['published', 'draft'])) {
            $query->where('status', $request->status);
        }

        // Filter Kategori
        if ($request->filled('category_id')) {
            $query->where('category_id', $request->category_id);
        }

        // Pencarian Kata Kunci
        if ($request->filled('q')) {
            $keyword = trim($request->q);
            $query->where(function ($q) use ($keyword) {
                $q->where('title', 'like', "%{$keyword}%")
                  ->orWhere('summary', 'like', "%{$keyword}%")
                  ->orWhere('tags', 'like', "%{$keyword}%");
            });
        }

        $articles = $query->orderByDesc('created_at')->paginate(15)->withQueryString();

        $categories = Category::all();
        $counts = [
            'all' => Article::count(),
            'published' => Article::where('status', 'published')->count(),
            'draft' => Article::where('status', 'draft')->count(),
        ];

        return view('admin.articles.index', compact('articles', 'categories', 'counts'));
    }

    /**
     * Form buat postingan baru (layaknya WordPress Post)
     */
    public function create(): View
    {
        $categories = Category::all();
        return view('admin.articles.form', ['article' => new Article(), 'categories' => $categories]);
    }

    /**
     * Simpan postingan baru
     */
    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'category_id' => 'nullable|exists:categories,id',
            'new_category' => 'nullable|string|max:100',
            'title' => 'required|string|max:200',
            'slug' => 'nullable|string|max:200|unique:articles,slug',
            'summary' => 'nullable|string|max:500',
            'content' => 'required|string',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'author' => 'required|string|max:100',
            'tags' => 'nullable|string|max:255',
            'status' => 'required|in:draft,published',
            'published_at' => 'nullable|date',
            'meta_title' => 'nullable|string|max:200',
            'meta_description' => 'nullable|string|max:300',
        ]);

        // Cek kategori baru on-the-fly jika diisi
        $categoryId = $validated['category_id'] ?? null;
        if (!empty($request->input('new_category'))) {
            $cat = Category::firstOrCreate(
                ['name' => trim($request->input('new_category'))],
                ['slug' => Str::slug($request->input('new_category'))]
            );
            $categoryId = $cat->id;
        }

        // Upload Gambar Utama / Featured Image
        $imagePath = null;
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/articles');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'post-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'articles/' . $fileName;
        }

        $slug = !empty($validated['slug']) ? Str::slug($validated['slug']) : Str::slug($validated['title']) . '-' . rand(100, 999);

        $publishedAt = null;
        if ($validated['status'] === 'published') {
            $publishedAt = !empty($validated['published_at']) ? $validated['published_at'] : now();
        }

        Article::create([
            'category_id' => $categoryId,
            'title' => $validated['title'],
            'slug' => $slug,
            'summary' => $validated['summary'] ?? null,
            'content' => $validated['content'],
            'image' => $imagePath,
            'author' => $validated['author'],
            'tags' => $validated['tags'] ?? null,
            'status' => $validated['status'],
            'published_at' => $publishedAt,
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
        ]);

        return redirect()->route('admin.articles.index')->with('success', 'Postingan berita/artikel berhasil diterbitkan!');
    }

    /**
     * Form edit artikel
     */
    public function edit(Article $article): View
    {
        $categories = Category::all();
        return view('admin.articles.form', compact('article', 'categories'));
    }

    /**
     * Simpan pembaruan artikel
     */
    public function update(Request $request, Article $article): RedirectResponse
    {
        $validated = $request->validate([
            'category_id' => 'nullable|exists:categories,id',
            'new_category' => 'nullable|string|max:100',
            'title' => 'required|string|max:200',
            'slug' => 'required|string|max:200|unique:articles,slug,' . $article->id,
            'summary' => 'nullable|string|max:500',
            'content' => 'required|string',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'remove_image' => 'nullable|boolean',
            'author' => 'required|string|max:100',
            'tags' => 'nullable|string|max:255',
            'status' => 'required|in:draft,published',
            'published_at' => 'nullable|date',
            'meta_title' => 'nullable|string|max:200',
            'meta_description' => 'nullable|string|max:300',
        ]);

        // Cek kategori baru on-the-fly jika diisi
        $categoryId = $validated['category_id'] ?? null;
        if (!empty($request->input('new_category'))) {
            $cat = Category::firstOrCreate(
                ['name' => trim($request->input('new_category'))],
                ['slug' => Str::slug($request->input('new_category'))]
            );
            $categoryId = $cat->id;
        }

        // Upload Gambar Baru Jika Ada
        $imagePath = $article->image;
        if ($request->boolean('remove_image')) {
            $imagePath = null;
        }
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/articles');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'post-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'articles/' . $fileName;
        }

        $publishedAt = $article->published_at;
        if ($validated['status'] === 'published') {
            $publishedAt = !empty($validated['published_at']) ? $validated['published_at'] : ($article->published_at ?: now());
        }

        $article->update([
            'category_id' => $categoryId,
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'summary' => $validated['summary'] ?? null,
            'content' => $validated['content'],
            'image' => $imagePath,
            'author' => $validated['author'],
            'tags' => $validated['tags'] ?? null,
            'status' => $validated['status'],
            'published_at' => $publishedAt,
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
        ]);

        return redirect()->route('admin.articles.index')->with('success', 'Postingan artikel berhasil diperbarui!');
    }

    /**
     * AJAX endpoint tambah kategori baru secara instan (WordPress style "+ Tambah Kategori Baru")
     */
    public function ajaxStoreCategory(Request $request): \Illuminate\Http\JsonResponse
    {
        $request->validate([
            'name' => 'required|string|max:100',
        ]);

        $name = trim($request->input('name'));
        $slug = Str::slug($name);

        $category = Category::firstOrCreate(
            ['name' => $name],
            ['slug' => $slug]
        );

        return response()->json([
            'success' => true,
            'category' => $category,
            'message' => "Kategori '{$category->name}' berhasil ditambahkan!",
        ]);
    }

    /**
     * 1-Click Duplicate Artikel
     */
    public function duplicate(Article $article): RedirectResponse
    {
        $newTitle = $article->title . ' (Salinan)';
        $baseSlug = Str::slug($article->slug . '-salinan');
        $slug = $baseSlug;
        $counter = 1;
        while (Article::where('slug', $slug)->exists()) {
            $slug = $baseSlug . '-' . $counter++;
        }

        $newArticle = Article::create([
            'title' => $newTitle,
            'slug' => $slug,
            'category_id' => $article->category_id,
            'summary' => $article->summary,
            'content' => $article->content,
            'image' => $article->image,
            'tags' => $article->tags,
            'meta_title' => $article->meta_title ? $article->meta_title . ' (Salinan)' : $newTitle,
            'meta_description' => $article->meta_description,
            'status' => 'draft',
        ]);

        return redirect()->route('admin.articles.edit', $newArticle->id)
            ->with('success', 'Artikel berhasil diduplikasi! Silakan sesuaikan judul dan isi artikel.');
    }

    /**
     * Quick Edit Artikel (WordPress Quick Edit style)
     */
    public function quickUpdate(Request $request, Article $article): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:200',
            'slug' => 'required|string|max:200|unique:articles,slug,' . $article->id,
            'category_id' => 'required|exists:categories,id',
            'status' => 'required|in:published,draft',
        ]);

        $article->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'category_id' => $validated['category_id'],
            'status' => $validated['status'],
        ]);

        return back()->with('success', 'Artikel "' . $article->title . '" berhasil diperbarui dengan Quick Edit!');
    }

    /**
     * Hapus artikel
     */
    public function destroy(Article $article): RedirectResponse
    {
        $article->delete();
        return redirect()->route('admin.articles.index')->with('success', 'Artikel berhasil dihapus.');
    }
}
