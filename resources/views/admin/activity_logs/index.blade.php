@extends('layouts.admin')

@section('title', 'Log Aktivitas & Audit Trail')
@section('page_title', 'Audit Trail & Log Aktivitas (WP Activity Log Style)')

@section('content')

    <div class="d-flex flex-wrap justify-content-between align-items-center gap-3 mb-3">
        <div>
            <h6 class="text-dark fw-bold mb-1">
                <i class="bi bi-clock-history text-primary me-2"></i> Rekaman Riwayat Aktivitas Administrator
            </h6>
            <small class="text-muted">Total {{ $totalLogs }} rekaman aktivitas tercatat di sistem.</small>
        </div>

        @if($totalLogs > 0)
            <form action="{{ route('admin.activityLogs.clear') }}" method="POST" onsubmit="return confirm('Apakah Anda yakin ingin mengosongkan seluruh riwayat log aktivitas?');">
                @csrf
                <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3 shadow-xs">
                    <i class="bi bi-trash me-1"></i> Kosongkan Riwayat Log
                </button>
            </form>
        @endif
    </div>

    <!-- FILTER BAR -->
    <div class="card border-0 shadow-sm rounded-4 bg-white p-3 mb-4">
        <form action="{{ route('admin.activityLogs.index') }}" method="GET" class="row g-2 align-items-center">
            <div class="col-md-3">
                <select name="action" class="form-select form-select-sm" onchange="this.form.submit()">
                    <option value="">-- Semua Jenis Aksi --</option>
                    <option value="login" {{ request('action') === 'login' ? 'selected' : '' }}>Masuk / Login</option>
                    <option value="create" {{ request('action') === 'create' ? 'selected' : '' }}>Pembuatan Baru (Create)</option>
                    <option value="update" {{ request('action') === 'update' ? 'selected' : '' }}>Pembaruan (Update)</option>
                    <option value="quick_update" {{ request('action') === 'quick_update' ? 'selected' : '' }}>Edit Cepat (Quick Edit)</option>
                    <option value="duplicate" {{ request('action') === 'duplicate' ? 'selected' : '' }}>Duplikasi Konten</option>
                    <option value="delete" {{ request('action') === 'delete' ? 'selected' : '' }}>Penghapusan (Delete)</option>
                </select>
            </div>

            <div class="col-md-3">
                <select name="subject_type" class="form-select form-select-sm" onchange="this.form.submit()">
                    <option value="">-- Semua Modul --</option>
                    <option value="Halaman" {{ request('subject_type') === 'Halaman' ? 'selected' : '' }}>Halaman CMS</option>
                    <option value="Artikel" {{ request('subject_type') === 'Artikel' ? 'selected' : '' }}>Artikel Berita</option>
                    <option value="Menu" {{ request('subject_type') === 'Menu' ? 'selected' : '' }}>Menu Navigasi</option>
                    <option value="Pengaturan" {{ request('subject_type') === 'Pengaturan' ? 'selected' : '' }}>Pengaturan</option>
                    <option value="User" {{ request('subject_type') === 'User' ? 'selected' : '' }}>Pengguna / Akun</option>
                </select>
            </div>

            <div class="col-md-5">
                <div class="input-group input-group-sm">
                    <input type="text" name="q" class="form-control" placeholder="Cari rincian aktivitas, nama admin, atau IP address..." value="{{ request('q') }}">
                    <button class="btn btn-primary" type="submit">
                        <i class="bi bi-search me-1"></i> Cari
                    </button>
                    @if(request()->hasAny(['action', 'subject_type', 'q']))
                        <a href="{{ route('admin.activityLogs.index') }}" class="btn btn-light border" title="Reset Filter">
                            <i class="bi bi-x-circle"></i>
                        </a>
                    @endif
                </div>
            </div>
        </form>
    </div>

    <!-- TABEL LOG AKTIVITAS -->
    <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light border-bottom small text-uppercase text-muted">
                    <tr>
                        <th class="ps-4">Waktu</th>
                        <th>Administrator</th>
                        <th>Aksi</th>
                        <th>Modul</th>
                        <th>Rincian Aktivitas</th>
                        <th class="text-end pe-4">IP Address</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($logs as $log)
                        <tr>
                            <!-- Waktu -->
                            <td class="ps-4 text-nowrap">
                                <div class="fw-bold text-dark">{{ $log->created_at->format('d/m/Y H:i:s') }}</div>
                                <small class="text-muted">{{ $log->created_at->diffForHumans() }}</small>
                            </td>

                            <!-- Administrator -->
                            <td class="text-nowrap">
                                <div class="d-flex align-items-center gap-2">
                                    <div class="bg-primary bg-opacity-10 text-primary rounded-circle d-flex align-items-center justify-content-center fw-bold" style="width: 30px; height: 30px; font-size: 0.75rem;">
                                        {{ strtoupper(substr($log->user_name, 0, 1)) }}
                                    </div>
                                    <span class="fw-semibold text-dark">{{ $log->user_name }}</span>
                                </div>
                            </td>

                            <!-- Aksi Badge -->
                            <td class="text-nowrap">
                                @if($log->action === 'create')
                                    <span class="badge bg-success bg-opacity-10 text-success">
                                        <i class="bi bi-plus-circle me-1"></i> Create
                                    </span>
                                @elseif($log->action === 'update')
                                    <span class="badge bg-primary bg-opacity-10 text-primary">
                                        <i class="bi bi-pencil me-1"></i> Update
                                    </span>
                                @elseif($log->action === 'quick_update')
                                    <span class="badge bg-warning bg-opacity-25 text-dark">
                                        <i class="bi bi-lightning-charge me-1"></i> Quick Edit
                                    </span>
                                @elseif($log->action === 'duplicate')
                                    <span class="badge bg-info bg-opacity-10 text-info">
                                        <i class="bi bi-files me-1"></i> Duplikat
                                    </span>
                                @elseif($log->action === 'delete')
                                    <span class="badge bg-danger bg-opacity-10 text-danger">
                                        <i class="bi bi-trash me-1"></i> Delete
                                    </span>
                                @elseif($log->action === 'login')
                                    <span class="badge bg-dark bg-opacity-10 text-dark">
                                        <i class="bi bi-box-arrow-in-right me-1"></i> Login
                                    </span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">
                                        {{ $log->action }}
                                    </span>
                                @endif
                            </td>

                            <!-- Modul -->
                            <td class="text-nowrap">
                                @if($log->subject_type)
                                    <span class="badge bg-light text-muted border">
                                        {{ $log->subject_type }}
                                    </span>
                                @else
                                    <span class="text-muted opacity-50">-</span>
                                @endif
                            </td>

                            <!-- Deskripsi -->
                            <td>
                                <span class="text-dark">{{ $log->description }}</span>
                            </td>

                            <!-- IP Address -->
                            <td class="text-end pe-4 text-nowrap">
                                <span class="font-monospace text-muted small">{{ $log->ip_address ?? '127.0.0.1' }}</span>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-5 text-muted">
                                <i class="bi bi-journal-x display-6 d-block mb-2 text-secondary opacity-50"></i>
                                Belum ada catatan aktivitas yang sesuai filter.
                            </td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        @if($logs->hasPages())
            <div class="card-footer bg-white py-3 border-top">
                {{ $logs->links() }}
            </div>
        @endif
    </div>

@endsection

