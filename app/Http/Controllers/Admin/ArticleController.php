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
     * Tampilkan daftar seluruh postingan artikel / berita
     */
    public function index(): View
    {
        $articles = Article::with('category')->orderByDesc('created_at')->paginate(15);
        return view('admin.articles.index', compact('articles'));
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
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:2048',
            'author' => 'required|string|max:100',
            'status' => 'required|in:draft,published',
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

        Article::create([
            'category_id' => $categoryId,
            'title' => $validated['title'],
            'slug' => $slug,
            'summary' => $validated['summary'] ?? null,
            'content' => $validated['content'],
            'image' => $imagePath,
            'author' => $validated['author'],
            'status' => $validated['status'],
            'published_at' => $validated['status'] === 'published' ? now() : null,
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
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:2048',
            'author' => 'required|string|max:100',
            'status' => 'required|in:draft,published',
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
        if ($validated['status'] === 'published' && !$publishedAt) {
            $publishedAt = now();
        }

        $article->update([
            'category_id' => $categoryId,
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'summary' => $validated['summary'] ?? null,
            'content' => $validated['content'],
            'image' => $imagePath,
            'author' => $validated['author'],
            'status' => $validated['status'],
            'published_at' => $publishedAt,
            'meta_title' => $validated['meta_title'] ?? $validated['title'],
            'meta_description' => $validated['meta_description'] ?? null,
        ]);

        return redirect()->route('admin.articles.index')->with('success', 'Postingan artikel berhasil diperbarui!');
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
