<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Service;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class ServiceController extends Controller
{
    public function index(): View
    {
        $services = Service::orderBy('sort_order')->paginate(15);
        return view('admin.services.index', compact('services'));
    }

    public function create(): View
    {
        return view('admin.services.form', ['service' => new Service()]);
    }

    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:150',
            'category' => 'required|string|max:50',
            'excerpt' => 'nullable|string|max:255',
            'description' => 'nullable|string',
            'price_starting' => 'nullable|string|max:100',
            'features_text' => 'nullable|string',
            'icon' => 'nullable|string|max:50',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        Service::create([
            ...$validated,
            'slug' => Str::slug($request->title) . '-' . rand(100, 999),
            'features' => $features,
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.services.index')->with('success', 'Layanan berhasil ditambahkan!');
    }

    public function edit(Service $service): View
    {
        return view('admin.services.form', compact('service'));
    }

    public function update(Request $request, Service $service): RedirectResponse
    {
        $validated = $request->validate([
            'title' => 'required|string|max:150',
            'category' => 'required|string|max:50',
            'excerpt' => 'nullable|string|max:255',
            'description' => 'nullable|string',
            'price_starting' => 'nullable|string|max:100',
            'features_text' => 'nullable|string',
            'icon' => 'nullable|string|max:50',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        $service->update([
            ...$validated,
            'features' => $features,
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.services.index')->with('success', 'Layanan berhasil diperbarui!');
    }

    public function destroy(Service $service): RedirectResponse
    {
        $service->delete();
        return redirect()->route('admin.services.index')->with('success', 'Layanan berhasil dihapus.');
    }
}
