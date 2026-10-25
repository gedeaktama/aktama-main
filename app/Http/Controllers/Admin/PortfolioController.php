<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Portfolio;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class PortfolioController extends Controller
{
    public function index(): View
    {
        $portfolios = Portfolio::orderByDesc('project_year')->paginate(15);
        return view('admin.portfolios.index', compact('portfolios'));
    }

    public function create(): View
    {
        return view('admin.portfolios.form', ['portfolio' => new Portfolio()]);
    }

    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:150',
            'slug' => 'nullable|string|max:150|unique:portfolios,slug',
            'category' => 'required|string|max:50',
            'client_type' => 'nullable|string|max:100',
            'technology' => 'required|string|max:150',
            'project_year' => 'nullable|string|max:4',
            'project_url' => 'nullable|url|max:255',
            'description' => 'nullable|string',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'is_published' => 'nullable|boolean',
        ]);

        $imagePath = null;
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/portfolios');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'portfolio-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'portfolios/' . $fileName;
        }

        $slug = !empty($validated['slug']) ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $originalSlug = $slug;
        $counter = 1;
        while (Portfolio::where('slug', $slug)->exists()) {
            $slug = $originalSlug . '-' . $counter++;
        }

        Portfolio::create([
            'title' => $validated['title'],
            'slug' => $slug,
            'category' => $validated['category'],
            'client_type' => $validated['client_type'] ?? null,
            'technology' => $validated['technology'],
            'project_year' => $validated['project_year'] ?? date('Y'),
            'project_url' => $validated['project_url'] ?? null,
            'description' => $validated['description'] ?? null,
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
        ]);

        return redirect()->route('admin.portfolios.index')->with('success', 'Portofolio berhasil ditambahkan!');
    }

    public function edit(Portfolio $portfolio): View
    {
        return view('admin.portfolios.form', compact('portfolio'));
    }

    public function update(Request $request, Portfolio $portfolio): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:150',
            'slug' => 'required|string|max:150|unique:portfolios,slug,' . $portfolio->id,
            'category' => 'required|string|max:50',
            'client_type' => 'nullable|string|max:100',
            'technology' => 'required|string|max:150',
            'project_year' => 'nullable|string|max:4',
            'project_url' => 'nullable|url|max:255',
            'description' => 'nullable|string',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'remove_image' => 'nullable|boolean',
            'is_published' => 'nullable|boolean',
        ]);

        $imagePath = $portfolio->image;
        if ($request->boolean('remove_image')) {
            $imagePath = null;
        }
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/portfolios');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'portfolio-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'portfolios/' . $fileName;
        }

        $portfolio->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'category' => $validated['category'],
            'client_type' => $validated['client_type'] ?? null,
            'technology' => $validated['technology'],
            'project_year' => $validated['project_year'] ?? date('Y'),
            'project_url' => $validated['project_url'] ?? null,
            'description' => $validated['description'] ?? null,
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
        ]);

        return redirect()->route('admin.portfolios.index')->with('success', 'Portofolio berhasil diperbarui!');
    }

    public function destroy(Portfolio $portfolio): RedirectResponse
    {
        $portfolio->delete();
        return redirect()->route('admin.portfolios.index')->with('success', 'Portofolio berhasil dihapus.');
    }
}
