<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class LeadController extends Controller
{
    public function index(Request $request): View
    {
        $query = Lead::query();

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        if ($request->filled('service_type')) {
            $query->where('service_type', $request->service_type);
        }

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('whatsapp', 'like', "%{$search}%")
                  ->orWhere('organization', 'like', "%{$search}%")
                  ->orWhere('message', 'like', "%{$search}%");
            });
        }

        $leads = $query->orderByDesc('created_at')->paginate(15)->withQueryString();

        return view('admin.leads.index', compact('leads'));
    }

    public function show(Lead $lead): View
    {
        return view('admin.leads.show', compact('lead'));
    }

    public function updateStatus(Request $request, Lead $lead): RedirectResponse
    {
        $validated = $request->validate([
            'status' => 'required|in:new,contacted,qualified,closed,cancelled',
            'admin_notes' => 'nullable|string|max:2000',
        ]);

        $lead->update($validated);

        return back()->with('success', 'Status calon pelanggan berhasil diperbarui!');
    }

    public function destroy(Lead $lead): RedirectResponse
    {
        $lead->delete();
        return redirect()->route('admin.leads.index')
            ->with('success', 'Data calon pelanggan berhasil dihapus.');
    }
}
