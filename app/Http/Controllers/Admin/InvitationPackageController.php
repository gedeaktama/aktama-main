<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\InvitationPackage;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\View\View;

class InvitationPackageController extends Controller
{
    public function index(): View
    {
        $packages = InvitationPackage::orderBy('sort_order')->paginate(15);
        return view('admin.invitations.index', compact('packages'));
    }

    public function create(): View
    {
        return view('admin.invitations.form', ['package' => new InvitationPackage()]);
    }

    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:150',
            'price' => 'required|numeric|min:0',
            'discount_price' => 'nullable|numeric|min:0',
            'features_text' => 'nullable|string',
            'demo_url' => 'nullable|url',
            'is_popular' => 'boolean',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        InvitationPackage::create([
            ...$validated,
            'slug' => Str::slug($request->name) . '-' . rand(100, 999),
            'features' => $features,
            'is_popular' => $request->boolean('is_popular'),
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.invitations.index')->with('success', 'Paket undangan berhasil ditambahkan!');
    }

    public function edit(InvitationPackage $invitation): View
    {
        return view('admin.invitations.form', ['package' => $invitation]);
    }

    public function update(Request $request, InvitationPackage $invitation): RedirectResponse
    {
        $validated = $request->validate([
            'name' => 'required|string|max:150',
            'price' => 'required|numeric|min:0',
            'discount_price' => 'nullable|numeric|min:0',
            'features_text' => 'nullable|string',
            'demo_url' => 'nullable|url',
            'is_popular' => 'boolean',
            'is_published' => 'boolean',
            'sort_order' => 'integer',
        ]);

        $features = array_filter(array_map('trim', explode("\n", $request->input('features_text', ''))));

        $invitation->update([
            ...$validated,
            'features' => $features,
            'is_popular' => $request->boolean('is_popular'),
            'is_published' => $request->boolean('is_published'),
            'sort_order' => $request->input('sort_order', 0),
        ]);

        return redirect()->route('admin.invitations.index')->with('success', 'Paket undangan berhasil diperbarui!');
    }

    public function destroy(InvitationPackage $invitation): RedirectResponse
    {
        $invitation->delete();
        return redirect()->route('admin.invitations.index')->with('success', 'Paket undangan berhasil dihapus.');
    }
}
