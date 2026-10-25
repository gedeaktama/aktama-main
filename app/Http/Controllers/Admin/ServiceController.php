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
            'slug' => 'nullable|string|max:150|unique:services,slug',
            'category' => 'required|string|max:50',
            'excerpt' => 'nullable|string|max:255',
            'description' => 'nullable|string',
            'price_starting' => 'nullable|string|max:100',
            'features_text' => 'nullable|string',
            'icon' => 'nullable|string|max:50',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'is_published' => 'nullable|boolean',
            'sort_order' => 'nullable|integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        $imagePath = null;
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/services');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'service-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'services/' . $fileName;
        }

        $slug = !empty($validated['slug']) ? Str::slug($validated['slug']) : Str::slug($validated['title']);
        $originalSlug = $slug;
        $counter = 1;
        while (Service::where('slug', $slug)->exists()) {
            $slug = $originalSlug . '-' . $counter++;
        }

        Service::create([
            'title' => $validated['title'],
            'slug' => $slug,
            'category' => $validated['category'],
            'excerpt' => $validated['excerpt'] ?? null,
            'description' => $validated['description'] ?? null,
            'price_starting' => $validated['price_starting'] ?? null,
            'features' => $features,
            'icon' => $validated['icon'] ?? 'bi-globe',
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
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
            'slug' => 'required|string|max:150|unique:services,slug,' . $service->id,
            'category' => 'required|string|max:50',
            'excerpt' => 'nullable|string|max:255',
            'description' => 'nullable|string',
            'price_starting' => 'nullable|string|max:100',
            'features_text' => 'nullable|string',
            'icon' => 'nullable|string|max:50',
            'image_file' => 'nullable|image|mimes:png,jpg,jpeg,webp|max:5120',
            'remove_image' => 'nullable|boolean',
            'is_published' => 'nullable|boolean',
            'sort_order' => 'nullable|integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        $imagePath = $service->image;
        if ($request->boolean('remove_image')) {
            $imagePath = null;
        }
        if ($request->hasFile('image_file')) {
            $dir = public_path('images/services');
            if (!file_exists($dir)) {
                mkdir($dir, 0755, true);
            }
            $file = $request->file('image_file');
            $fileName = 'service-' . time() . '.' . $file->getClientOriginalExtension();
            $file->move($dir, $fileName);
            $imagePath = 'services/' . $fileName;
        }

        $service->update([
            'title' => $validated['title'],
            'slug' => Str::slug($validated['slug']),
            'category' => $validated['category'],
            'excerpt' => $validated['excerpt'] ?? null,
            'description' => $validated['description'] ?? null,
            'price_starting' => $validated['price_starting'] ?? null,
            'features' => $features,
            'icon' => $validated['icon'] ?? 'bi-globe',
            'image' => $imagePath,
            'is_published' => $request->has('is_published'),
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
