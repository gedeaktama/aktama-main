@extends('layouts.admin')

@section('title', 'Seksi Beranda (Drag & Drop)')
@section('page_title', 'Tata Letak Seksi Beranda (Modular Drag & Drop)')

@section('content')

    <div class="row mb-4">
        <div class="col-12">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
                    <div>
                        <h6 class="fw-bold text-dark mb-1">
                            <i class="bi bi-arrows-move text-primary me-2"></i> Pengaturan Tata Letak Seksi Beranda (Landing Page)
                        </h6>
                        <p class="text-muted small mb-0">
                            Tarik dan lepas (drag & drop) kotak seksi di bawah ini untuk mengubah susunan urutan tampilan beranda secara langsung tanpa menyentuh kode program.
                        </p>
                    </div>
                    <div class="d-flex gap-2">
                        <a href="{{ route('admin.pages.index') }}" class="btn btn-outline-secondary btn-sm rounded-pill px-3">
                            <i class="bi bi-palette-fill me-1"></i> Visual Page Builder (GrapesJS)
                        </a>
                        <a href="{{ route('home') }}" target="_blank" class="btn btn-primary btn-sm rounded-pill px-3">
                            <i class="bi bi-box-arrow-up-right me-1"></i> Lihat Beranda Publik
                        </a>
                    </div>
                </div>

                <div class="row g-3 mt-3 pt-3 border-top">
                    <div class="col-md-4">
                        <div class="p-3 rounded-3 bg-light border h-100">
                            <div class="fw-bold small text-dark mb-1"><i class="bi bi-sliders text-primary me-1"></i> 1. Urutan & Teks Seksi</div>
                            <p class="text-muted small mb-0" style="font-size: 0.78rem;">
                                Geser urutan seksi di bawah, klik <strong>Edit Teks</strong> untuk merubah judul, badge, subtitle, serta tombol CTA Hero.
                            </p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 rounded-3 bg-light border h-100">
                            <div class="fw-bold small text-dark mb-1"><i class="bi bi-database text-success me-1"></i> 2. Konten Dinamis Terpusat</div>
                            <p class="text-muted small mb-0" style="font-size: 0.78rem;">
                                Data layanan, pelatihan AI, portofolio, dan berita pada seksi beranda otomatis terhubung dari menu sidebar kiri.
                            </p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 rounded-3 bg-light border h-100">
                            <div class="fw-bold small text-dark mb-1"><i class="bi bi-magic text-info me-1"></i> 3. Desain Ala Elementor</div>
                            <p class="text-muted small mb-0" style="font-size: 0.78rem;">
                                Ingin landing page bebas kanvas? Buka menu <strong>Halaman & Visual Canvas</strong> untuk mendesain dengan drag & drop visual.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- NOTIFIKASI AJAX TOAST / ALERT -->
    <div id="reorder-alert" class="alert alert-success alert-dismissible fade d-none rounded-3 shadow-xs mb-3" role="alert">
        <i class="bi bi-check-circle-fill me-2"></i> <span id="reorder-message">Urutan berhasil disimpan!</span>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    <!-- DAFTAR SEKSI DRAG & DROP -->
    <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
        <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
            <span class="small fw-bold text-muted text-uppercase">Daftar Seksi Aktif & Nonaktif</span>
            <span class="badge bg-primary bg-opacity-10 text-primary small">
                <i class="bi bi-hand-index-thumb me-1"></i> Drag handle pada sisi kiri untuk menyusun
            </span>
        </div>

        <div class="list-group list-group-flush" id="sortable-sections">
            @foreach($sections as $sec)
                <div class="list-group-item p-3 d-flex align-items-center justify-content-between gap-3 border-bottom transition-all section-item {{ $sec->is_active ? '' : 'bg-light text-muted opacity-75' }}" data-id="{{ $sec->id }}">
                    <!-- Drag Handle & Info -->
                    <div class="d-flex align-items-center gap-3 flex-grow-1">
                        <div class="cursor-grab text-muted p-2 rounded-2 hover-bg-light drag-handle" title="Tarik untuk memindahkan urutan">
                            <i class="bi bi-grip-vertical fs-4"></i>
                        </div>
                        <div class="rounded-circle bg-primary bg-opacity-10 text-primary d-flex align-items-center justify-content-center fw-bold" style="width: 2.25rem; height: 2.25rem; font-size: 0.85rem;">
                            {{ $sec->sort_order }}
                        </div>
                        <div>
                            <div class="d-flex align-items-center gap-2 mb-1">
                                <span class="fw-bold text-dark">{{ $sec->name }}</span>
                                <span class="badge bg-secondary bg-opacity-10 text-dark small font-monospace">{{ $sec->section_key }}</span>
                                @if($sec->badge)
                                    <span class="badge bg-info bg-opacity-10 text-info small">{{ $sec->badge }}</span>
                                @endif
                            </div>
                            <div class="small text-muted text-truncate" style="max-width: 500px;">
                                {{ $sec->title ?: ($sec->subtitle ?: 'Tidak ada teks judul kustom.') }}
                            </div>
                        </div>
                    </div>

                    <!-- Status Toggle & Aksi -->
                    <div class="d-flex align-items-center gap-3">
                        <form action="{{ route('admin.sections.toggle', $sec->id) }}" method="POST" class="d-inline">
                            @csrf
                            @if($sec->is_active)
                                <button type="submit" class="btn btn-sm btn-outline-success rounded-pill px-3" title="Klik untuk menonaktifkan seksi ini">
                                    <i class="bi bi-eye-fill me-1"></i> Tampil di Web
                                </button>
                            @else
                                <button type="submit" class="btn btn-sm btn-outline-secondary rounded-pill px-3" title="Klik untuk mengaktifkan seksi ini">
                                    <i class="bi bi-eye-slash me-1"></i> Disembunyikan
                                </button>
                            @endif
                        </form>

                        <a href="{{ route('admin.sections.edit', $sec->id) }}" class="btn btn-sm btn-brand rounded-pill px-3">
                            <i class="bi bi-pencil-square me-1"></i> Edit Teks
                        </a>
                    </div>
                </div>
            @endforeach
        </div>
    </div>

@endsection

@push('scripts')
<script src="https://cdn.jsdelivr.net/npm/sortablejs@1.15.2/Sortable.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const list = document.getElementById('sortable-sections');
        if (!list) return;

        new Sortable(list, {
            handle: '.drag-handle',
            animation: 180,
            ghostClass: 'bg-primary-subtle',
            chosenClass: 'shadow-md',
            onEnd: function () {
                const items = list.querySelectorAll('.section-item');
                const order = Array.from(items).map(item => item.getAttribute('data-id'));

                fetch("{{ route('admin.sections.reorder') }}", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                    },
                    body: JSON.stringify({ order: order })
                })
                .then(response => response.json())
                .then(data => {
                    const alertBox = document.getElementById('reorder-alert');
                    const msgSpan = document.getElementById('reorder-message');
                    if (alertBox && msgSpan) {
                        msgSpan.innerText = data.message || 'Urutan seksi berhasil diperbarui!';
                        alertBox.classList.remove('d-none');
                        alertBox.classList.add('show');
                        setTimeout(() => {
                            alertBox.classList.remove('show');
                            alertBox.classList.add('d-none');
                        }, 4000);
                    }
                })
                .catch(err => {
                    console.error('Reorder error:', err);
                    alert('Gagal menyimpan urutan seksi. Silakan coba kembali.');
                });
            }
        });
    });
</script>
<style>
    .cursor-grab {
        cursor: grab;
    }
    .cursor-grab:active {
        cursor: grabbing;
    }
    .hover-bg-light:hover {
        background-color: rgba(0, 0, 0, 0.05);
    }
</style>
@endpush
