@extends('layouts.admin')

@section('title', 'Dashboard')
@section('page_title', 'Ringkasan Ekosistem Bisnis Aktama')

@section('content')

    <!-- Statistik Utama Cards -->
    <div class="row g-3 mb-4">
        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <span class="text-muted small fw-bold text-uppercase">Total Leads</span>
                    <span class="p-2 rounded-3 bg-danger bg-opacity-10 text-danger fs-5"><i class="bi bi-people-fill"></i></span>
                </div>
                <h3 class="fw-bold font-display text-dark mb-1">{{ $stats['total_leads'] }}</h3>
                <small class="text-danger fw-semibold"><i class="bi bi-bell-fill me-1"></i>{{ $stats['new_leads'] }} Calon Pelanggan Baru</small>
            </div>
        </div>

        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <span class="text-muted small fw-bold text-uppercase">Jasa Web & Aplikasi</span>
                    <span class="p-2 rounded-3 bg-primary bg-opacity-10 text-primary fs-5"><i class="bi bi-globe"></i></span>
                </div>
                <h3 class="fw-bold font-display text-dark mb-1">{{ $stats['services_count'] }}</h3>
                <small class="text-muted">Katalog Layanan Aktif</small>
            </div>
        </div>

        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <span class="text-muted small fw-bold text-uppercase">Pelatihan AI</span>
                    <span class="p-2 rounded-3 bg-info bg-opacity-10 text-info fs-5"><i class="bi bi-robot"></i></span>
                </div>
                <h3 class="fw-bold font-display text-dark mb-1">{{ $stats['training_count'] }}</h3>
                <small class="text-muted">Silabus Program Mandiri</small>
            </div>
        </div>

        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <span class="text-muted small fw-bold text-uppercase">Produk Kopi</span>
                    <span class="p-2 rounded-3 bg-warning bg-opacity-10 text-warning fs-5"><i class="bi bi-cup-hot-fill"></i></span>
                </div>
                <h3 class="fw-bold font-display text-dark mb-1">{{ $stats['coffee_count'] }}</h3>
                <small class="text-muted">Katalog Robusta & Arabika</small>
            </div>
        </div>
    </div>

    <!-- CMS & Tata Letak Akses Cepat -->
    <div class="row g-3 mb-4">
        <div class="col-md-3 col-sm-6">
            <a href="{{ route('admin.sections.index') }}" class="card border-0 shadow-sm rounded-4 p-3 bg-white text-decoration-none h-100 hover-shadow transition-all border-start border-primary border-4">
                <div class="d-flex align-items-center gap-3">
                    <div class="p-2 bg-primary bg-opacity-10 text-primary rounded-3 fs-4"><i class="bi bi-arrows-move"></i></div>
                    <div>
                        <div class="fw-bold text-dark small">Seksi Beranda</div>
                        <small class="text-muted" style="font-size: 0.75rem;">Drag & Drop {{ $stats['sections_count'] }} Seksi</small>
                    </div>
                </div>
            </a>
        </div>
        <div class="col-md-3 col-sm-6">
            <a href="{{ route('admin.pages.index') }}" class="card border-0 shadow-sm rounded-4 p-3 bg-white text-decoration-none h-100 hover-shadow transition-all border-start border-info border-4">
                <div class="d-flex align-items-center gap-3">
                    <div class="p-2 bg-info bg-opacity-10 text-info rounded-3 fs-4"><i class="bi bi-palette-fill"></i></div>
                    <div>
                        <div class="fw-bold text-dark small">Halaman Visual</div>
                        <small class="text-muted" style="font-size: 0.75rem;">{{ $stats['pages_count'] }} Halaman & Builder</small>
                    </div>
                </div>
            </a>
        </div>
        <div class="col-md-3 col-sm-6">
            <a href="{{ route('admin.menus.index') }}" class="card border-0 shadow-sm rounded-4 p-3 bg-white text-decoration-none h-100 hover-shadow transition-all border-start border-success border-4">
                <div class="d-flex align-items-center gap-3">
                    <div class="p-2 bg-success bg-opacity-10 text-success rounded-3 fs-4"><i class="bi bi-menu-button-wide-fill"></i></div>
                    <div>
                        <div class="fw-bold text-dark small">Menu Navigasi</div>
                        <small class="text-muted" style="font-size: 0.75rem;">Drag & Drop Navbar & Footer</small>
                    </div>
                </div>
            </a>
        </div>
        <div class="col-md-3 col-sm-6">
            <a href="{{ route('admin.settings.index') }}" class="card border-0 shadow-sm rounded-4 p-3 bg-white text-decoration-none h-100 hover-shadow transition-all border-start border-warning border-4">
                <div class="d-flex align-items-center gap-3">
                    <div class="p-2 bg-warning bg-opacity-10 text-warning rounded-3 fs-4"><i class="bi bi-image"></i></div>
                    <div>
                        <div class="fw-bold text-dark small">Ganti Logo & Footer</div>
                        <small class="text-muted" style="font-size: 0.75rem;">Logo, Topbar & Hak Cipta</small>
                    </div>
                </div>
            </a>
        </div>
    </div>

    <!-- Tabel Permintaan Penawaran Terbaru (Leads) -->
    <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
        <div class="card-header bg-white py-3 d-flex align-items-center justify-content-between border-bottom">
            <h6 class="fw-bold text-dark mb-0"><i class="bi bi-inbox-fill text-primary me-2"></i> Calon Pelanggan & Penawaran Masuk Terbaru</h6>
            <a href="{{ route('admin.leads.index') }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                Lihat Seluruh Leads
            </a>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Nama & Instansi</th>
                        <th>Layanan Diminati</th>
                        <th>Kontak WhatsApp</th>
                        <th>Status</th>
                        <th>Tanggal Masuk</th>
                        <th class="text-end pe-4">Aksi Cepat</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($recentLeads as $lead)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $lead->name }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">{{ $lead->organization ?? 'Pribadi / Perorangan' }}</span>
                            </td>
                            <td>
                                <span class="badge bg-light text-dark border">{{ $lead->service_label }}</span>
                            </td>
                            <td>
                                <span class="font-monospace text-dark">{{ $lead->whatsapp }}</span>
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
                                    $quickWaUrl = "https://wa.me/{$cleanPhone}?text=" . urlencode("Halo {$lead->name}, terima kasih telah menghubungi PT Aktama Digital Antika terkait {$lead->service_label}...");
                                @endphp
                                <a href="{{ $quickWaUrl }}" target="_blank" class="btn btn-success btn-sm rounded-pill px-3" title="Hubungi via WhatsApp">
                                    <i class="bi bi-whatsapp me-1"></i> Balas
                                </a>
                                <a href="{{ route('admin.leads.show', $lead->id) }}" class="btn btn-light border btn-sm rounded-pill px-2">
                                    <i class="bi bi-eye"></i>
                                </a>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">
                                <i class="bi bi-inbox fs-3 d-block text-muted mb-2"></i>
                                Belum ada calon pelanggan yang mengisi formulir.
                            </td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
