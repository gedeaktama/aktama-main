<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\HomeSection;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class HomeSectionController extends Controller
{
    /**
     * Tampilkan daftar seksi beranda untuk pengaturan tata letak (Drag & Drop)
     */
    public function index(): View
    {
        $sections = HomeSection::orderBy('sort_order')->get();
        return view('admin.sections.index', compact('sections'));
    }

    /**
     * Form edit konten teks & judul seksi beranda
     */
    public function edit(HomeSection $section): View
    {
        return view('admin.sections.edit', compact('section'));
    }

    /**
     * Simpan pembaruan konten seksi beranda
     */
    public function update(Request $request, HomeSection $section): RedirectResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:150',
            'badge' => 'nullable|string|max:100',
            'title' => 'nullable|string|max:255',
            'subtitle' => 'nullable|string|max:1000',
            'is_active' => 'nullable|boolean',
            'content_data' => 'nullable|array',
        ]);

        $updatePayload = [
            'name' => $validated['name'],
            'badge' => $validated['badge'] ?? null,
            'title' => $validated['title'] ?? null,
            'subtitle' => $validated['subtitle'] ?? null,
            'is_active' => $request->has('is_active'),
        ];

        if ($request->has('content_data')) {
            $updatePayload['content_data'] = $request->input('content_data');
        }

        $section->update($updatePayload);

        return redirect()->route('admin.sections.index')->with('success', "Seksi '{$section->name}' berhasil diperbarui!");
    }

    /**
     * AJAX Reorder urutan seksi dengan Drag & Drop (SortableJS)
     */
    public function reorder(Request $request): JsonResponse
    {
        $request->validate([
            'order' => 'required|array',
            'order.*' => 'integer|exists:home_sections,id',
        ]);

        foreach ($request->input('order') as $index => $id) {
            HomeSection::where('id', $id)->update(['sort_order' => $index + 1]);
        }

        return response()->json([
            'success' => true,
            'message' => 'Urutan seksi beranda berhasil diperbarui!',
        ]);
    }

    /**
     * Toggle status aktif/nonaktif seksi
     */
    public function toggle(HomeSection $section): RedirectResponse
    {
        $section->update([
            'is_active' => !$section->is_active,
        ]);

        $status = $section->is_active ? 'diaktifkan' : 'dinonaktifkan';
        return back()->with('success', "Seksi '{$section->name}' berhasil {$status}!");
    }
}
