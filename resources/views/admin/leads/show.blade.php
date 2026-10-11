@extends('layouts.admin')

@section('title', 'Detail Calon Pelanggan - ' . $lead->name)
@section('page_title', 'Rincian Permintaan Calon Pelanggan')

@section('content')

    <div class="row g-4">
        <!-- Rincian Permintaan -->
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 h-100">
                <div class="d-flex justify-content-between align-items-center border-bottom pb-3 mb-3">
                    <div>
                        <span class="badge {{ $lead->status_badge }} text-uppercase mb-1" style="font-size: 0.7rem;">
                            Status: {{ $lead->status }}
                        </span>
                        <h4 class="fw-bold text-dark mb-0">{{ $lead->name }}</h4>
                        <small class="text-muted"><i class="bi bi-clock me-1"></i>Dikirim pada: {{ $lead->created_at->format('d F Y, H:i:s') }}</small>
                    </div>
                    @php
                        $cleanPhone = preg_replace('/[^0-9]/', '', $lead->whatsapp);
                        if (str_starts_with($cleanPhone, '0')) {
                            $cleanPhone = '62' . substr($cleanPhone, 1);
                        }
                        $waUrl = "https://wa.me/{$cleanPhone}?text=" . urlencode("Halo {$lead->name}, terima kasih telah menghubungi PT Aktama Digital Antika terkait penawaran {$lead->service_label}...");
                    @endphp
                    <a href="{{ $waUrl }}" target="_blank" class="btn btn-success rounded-pill px-4 fw-bold">
                        <i class="bi bi-whatsapp me-1"></i> Chat WhatsApp Langsung
                    </a>
                </div>

                <div class="row g-3 mb-4">
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Nomor WhatsApp:</small>
                        <strong class="font-monospace text-dark fs-6">{{ $lead->whatsapp }}</strong>
                    </div>
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Alamat Email:</small>
                        <strong class="text-dark">{{ $lead->email ?? '-' }}</strong>
                    </div>
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Instansi / Perusahaan / Usaha:</small>
                        <strong class="text-dark">{{ $lead->organization ?? '-' }}</strong>
                    </div>
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Layanan yang Diminati:</small>
                        <span class="badge bg-primary bg-opacity-10 text-primary fs-6">{{ $lead->service_label }}</span>
                    </div>
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Estimasi Anggaran:</small>
                        <strong class="text-secondary">{{ $lead->budget_range ?? 'Belum ditentukan' }}</strong>
                    </div>
                    <div class="col-sm-6">
                        <small class="text-muted d-block">Sumber Halaman Form:</small>
                        <span class="text-muted">{{ $lead->source_page ?? 'Website' }}</span>
                    </div>
                </div>

                <div class="border rounded-3 p-3 bg-light mb-3">
                    <strong class="text-dark d-block small mb-2"><i class="bi bi-chat-quote-fill text-primary me-1"></i> Pesan / Rincian Kebutuhan:</strong>
                    <p class="text-dark small leading-relaxed mb-0" style="white-space: pre-line;">{{ $lead->message }}</p>
                </div>
            </div>
        </div>

        <!-- Update Status & Catatan Admin -->
        <div class="col-lg-5">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 h-100">
                <h6 class="fw-bold text-dark border-bottom pb-3 mb-3">
                    <i class="bi bi-pencil-square text-primary me-2"></i> Tindak Lanjut & Catatan Admin
                </h6>

                <form action="{{ route('admin.leads.status', $lead->id) }}" method="POST">
                    @csrf
                    @method('PUT')

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Status Tindak Lanjut</label>
                        <select name="status" class="form-select">
                            <option value="new" {{ $lead->status === 'new' ? 'selected' : '' }}>Baru (Belum Dihubungi)</option>
                            <option value="contacted" {{ $lead->status === 'contacted' ? 'selected' : '' }}>Sudah Dihubungi via WA/Email</option>
                            <option value="qualified" {{ $lead->status === 'qualified' ? 'selected' : '' }}>Tertarik / Tahap Negosiasi Proposal</option>
                            <option value="closed" {{ $lead->status === 'closed' ? 'selected' : '' }}>Deal / Selesai Transaksi</option>
                            <option value="cancelled" {{ $lead->status === 'cancelled' ? 'selected' : '' }}>Batal / Tidak Ada Respons</option>
                        </select>
                    </div>

                    <div class="mb-4">
                        <label class="form-label small fw-bold text-dark">Catatan Internal Admin</label>
                        <textarea name="admin_notes" class="form-control" rows="5" placeholder="Tuliskan catatan progres follow-up, kesepakatan harga, atau jadwal meeting di sini...">{{ $lead->admin_notes }}</textarea>
                        <small class="text-muted" style="font-size: 0.75rem;">Catatan ini hanya terlihat oleh administrator.</small>
                    </div>

                    <button type="submit" class="btn btn-primary rounded-pill w-100 py-2 fw-semibold">
                        <i class="bi bi-check-lg me-1"></i> Simpan Pembaruan Status
                    </button>
                </form>

                <hr class="my-4">

                <form action="{{ route('admin.leads.destroy', $lead->id) }}" method="POST" onsubmit="return confirm('Apakah Anda yakin ingin menghapus data calon pelanggan ini?')">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-outline-danger btn-sm rounded-pill w-100">
                        <i class="bi bi-trash3 me-1"></i> Hapus Data Lead Ini
                    </button>
                </form>
            </div>
        </div>
    </div>

@endsection
