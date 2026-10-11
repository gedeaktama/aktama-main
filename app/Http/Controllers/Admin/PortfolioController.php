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
            'category' => 'required|string|max:50',
            'client_type' => 'nullable|string|max:100',
            'technology' => 'required|string|max:150',
            'project_year' => 'nullable|string|max:4',
            'description' => 'nullable|string',
            'is_published' => 'boolean',
        ]);

        Portfolio::create([
            ...$validated,
            'slug' => Str::slug($request->title) . '-' . rand(100, 999),
            'is_published' => $request->boolean('is_published'),
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
            'category' => 'required|string|max:50',
            'client_type' => 'nullable|string|max:100',
            'technology' => 'required|string|max:150',
            'project_year' => 'nullable|string|max:4',
            'description' => 'nullable|string',
            'is_published' => 'boolean',
        ]);

        $portfolio->update([
            ...$validated,
            'is_published' => $request->boolean('is_published'),
        ]);

        return redirect()->route('admin.portfolios.index')->with('success', 'Portofolio berhasil diperbarui!');
    }

    public function destroy(Portfolio $portfolio): RedirectResponse
    {
        $portfolio->delete();
        return redirect()->route('admin.portfolios.index')->with('success', 'Portofolio berhasil dihapus.');
    }
}
