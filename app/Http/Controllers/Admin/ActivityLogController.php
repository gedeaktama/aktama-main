<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\ActivityLog;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class ActivityLogController extends Controller
{
    /**
     * Tampilkan riwayat audit log aktivitas admin (ala WP Activity Log)
     */
    public function index(Request $request): View
    {
        $query = ActivityLog::query();

        if ($request->filled('action')) {
            $query->where('action', $request->action);
        }

        if ($request->filled('subject_type')) {
            $query->where('subject_type', $request->subject_type);
        }

        if ($request->filled('q')) {
            $keyword = trim($request->q);
            $query->where(function ($q) use ($keyword) {
                $q->where('description', 'like', "%{$keyword}%")
                  ->orWhere('user_name', 'like', "%{$keyword}%")
                  ->orWhere('ip_address', 'like', "%{$keyword}%");
            });
        }

        $logs = $query->orderByDesc('created_at')->paginate(20)->withQueryString();
        $totalLogs = ActivityLog::count();

        return view('admin.activity_logs.index', compact('logs', 'totalLogs'));
    }

    /**
     * Bersihkan riwayat log
     */
    public function clear(Request $request): RedirectResponse
    {
        ActivityLog::truncate();
        ActivityLog::record('clear_logs', 'Administrator mengosongkan riwayat audit log.');

        return redirect()->route('admin.activityLogs.index')->with('success', 'Riwayat aktivitas berhasil dibersihkan.');
    }
}

