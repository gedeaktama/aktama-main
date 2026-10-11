@extends('layouts.admin')

@section('title', 'Manajemen Calon Pelanggan (Leads)')
@section('page_title', 'Daftar Calon Pelanggan & Permintaan Penawaran')

@section('content')

    <!-- Filter & Pencarian -->
    <div class="card border-0 shadow-sm rounded-4 bg-white p-3 mb-4">
        <form action="{{ route('admin.leads.index') }}" method="GET" class="row g-2 align-items-center">
            <div class="col-md-5">
                <div class="input-group">
                    <span class="input-group-text bg-light border-end-0"><i class="bi bi-search text-muted"></i></span>
                    <input type="text" name="search" class="form-control border-start-0" placeholder="Cari nama, WhatsApp, instansi, atau pesan..." value="{{ request('search') }}">
                </div>
            </div>
            <div class="col-md-3">
                <select name="status" class="form-select" onchange="this.form.submit()">
                    <option value="">Semua Status...</option>
                    <option value="new" {{ request('status') === 'new' ? 'selected' : '' }}>Baru (New)</option>
                    <option value="contacted" {{ request('status') === 'contacted' ? 'selected' : '' }}>Sudah Dihubungi</option>
                    <option value="qualified" {{ request('status') === 'qualified' ? 'selected' : '' }}>Tertarik / Negosiasi</option>
                    <option value="closed" {{ request('status') === 'closed' ? 'selected' : '' }}>Selesai / Deal</option>
                    <option value="cancelled" {{ request('status') === 'cancelled' ? 'selected' : '' }}>Batal / Tidak Lanjut</option>
                </select>
            </div>
            <div class="col-md-2">
                <select name="service_type" class="form-select" onchange="this.form.submit()">
                    <option value="">Semua Layanan...</option>
                    <option value="pelatihan-ai" {{ request('service_type') === 'pelatihan-ai' ? 'selected' : '' }}>Pelatihan AI</option>
                    <option value="jasa-website" {{ request('service_type') === 'jasa-website' ? 'selected' : '' }}>Jasa Website</option>
                    <option value="aktama-coffee" {{ request('service_type') === 'aktama-coffee' ? 'selected' : '' }}>Kopi</option>
                    <option value="undangan-online" {{ request('service_type') === 'undangan-online' ? 'selected' : '' }}>Undangan</option>
                </select>
            </div>
            <div class="col-md-2 d-flex gap-2">
                <button type="submit" class="btn btn-primary rounded-3 w-100">Filter</button>
                @if(request()->hasAny(['search', 'status', 'service_type']))
                    <a href="{{ route('admin.leads.index') }}" class="btn btn-light border rounded-3"><i class="bi bi-x-lg"></i></a>
                @endif
            </div>
        </form>
    </div>

    <!-- Tabel Leads -->
    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Nama & Organisasi</th>
                        <th>Layanan</th>
                        <th>Kontak WA & Email</th>
                        <th>Anggaran</th>
                        <th>Status</th>
                        <th>Waktu Masuk</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($leads as $lead)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $lead->name }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">{{ $lead->organization ?? 'Pribadi' }}</span>
                            </td>
                            <td>
                                <span class="badge bg-light text-dark border">{{ $lead->service_label }}</span>
                            </td>
                            <td>
                                <div><i class="bi bi-whatsapp text-success me-1"></i><span class="font-monospace text-dark">{{ $lead->whatsapp }}</span></div>
                                @if($lead->email)
                                    <div class="text-muted" style="font-size: 0.75rem;"><i class="bi bi-envelope me-1"></i>{{ $lead->email }}</div>
                                @endif
                            </td>
                            <td>
                                <span class="text-secondary small">{{ $lead->budget_range ?? '-' }}</span>
                            </td>
                            <td>
                                <span class="badge {{ $lead->status_badge }} text-uppercase" style="font-size: 0.65rem;">
                                    {{ $lead->status }}
                                </span>
                            </td>
                            <td class="text-muted">{{ $lead->created_at->format('d/m/Y H:i') }}</td>
                            <td class="text-end pe-4">
                                @php
                                    $cleanPhone = preg_replace('/[^0-9]/', '', $lead->whatsapp);
                                    if (str_starts_with($cleanPhone, '0')) {
                                        $cleanPhone = '62' . substr($cleanPhone, 1);
                                    }
                                    $quickWaUrl = "https://wa.me/{$cleanPhone}?text=" . urlencode("Halo Bapak/Ibu {$lead->name}, kami dari PT Aktama Digital Antika menindaklanjuti permintaan mengenai {$lead->service_label}...");
                                @endphp
                                <a href="{{ $quickWaUrl }}" target="_blank" class="btn btn-success btn-sm rounded-pill px-3" title="Hubungi via WhatsApp">
                                    <i class="bi bi-whatsapp me-1"></i> Chat WA
                                </a>
                                <a href="{{ route('admin.leads.show', $lead->id) }}" class="btn btn-outline-primary btn-sm rounded-pill px-3">
                                    <i class="bi bi-eye me-1"></i> Detail
                                </a>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="7" class="text-center py-5 text-muted">
                                <i class="bi bi-inbox fs-2 text-muted d-block mb-2"></i>
                                Tidak ada data calon pelanggan yang sesuai dengan pencarian.
                            </td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        @if($leads->hasPages())
            <div class="card-footer bg-white py-3 border-top d-flex justify-content-center">
                {{ $leads->links('pagination::bootstrap-5') }}
            </div>
        @endif
    </div>

@endsection
