@extends('layouts.admin')

@section('title', 'Edit Seksi Beranda: ' . $section->name)
@section('page_title', 'Edit Seksi Beranda: ' . $section->name)

@section('content')

    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <div class="d-flex align-items-center justify-content-between pb-3 mb-3 border-bottom">
                    <div>
                        <h6 class="fw-bold text-dark mb-0"><i class="bi bi-pencil-square text-primary me-2"></i> Pengaturan Konten Seksi</h6>
                        <small class="text-muted">Kunci modul sistem: <code>{{ $section->section_key }}</code></small>
                    </div>
                    <span class="badge {{ $section->is_active ? 'bg-success' : 'bg-secondary' }}">
                        {{ $section->is_active ? 'Status: Aktif' : 'Status: Nonaktif' }}
                    </span>
                </div>

                <form action="{{ route('admin.sections.update', $section->id) }}" method="POST">
                    @csrf
                    @method('PUT')

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Nama Label Seksi (Untuk Tampilan Admin) *</label>
                        <input type="text" name="name" class="form-control" value="{{ old('name', $section->name) }}" required>
                        <small class="text-muted" style="font-size: 0.75rem;">Label internal untuk memudahkan pengorganisasian di panel admin.</small>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Teks Badge / Kategori Seksi</label>
                        <input type="text" name="badge" class="form-control" value="{{ old('badge', $section->badge) }}" placeholder="Contoh: Solusi Teknologi Terpadu, Layanan Software">
                        <small class="text-muted" style="font-size: 0.75rem;">Teks kecil di atas judul utama seksi.</small>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Judul Utama Seksi (Heading / Headline)</label>
                        <input type="text" name="title" class="form-control" value="{{ old('title', $section->title) }}" placeholder="Tuliskan judul besar seksi...">
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Deskripsi / Subtitle Seksi</label>
                        <textarea name="subtitle" class="form-control" rows="3" placeholder="Tuliskan kalimat penjelas di bawah judul...">{{ old('subtitle', $section->subtitle) }}</textarea>
                    </div>

                    <div class="form-check form-switch mb-4 p-3 bg-light rounded-3 d-flex align-items-center gap-3">
                        <input class="form-check-input ms-0 mt-0" type="checkbox" role="switch" id="is_active" name="is_active" value="1" {{ old('is_active', $section->is_active) ? 'checked' : '' }} style="width: 2.5rem; height: 1.25rem;">
                        <label class="form-check-label fw-bold text-dark small mb-0" for="is_active">
                            Tampilkan Seksi ini pada Halaman Beranda Publik
                            <span class="d-block text-muted fw-normal" style="font-size: 0.75rem;">Jika dimatikan, seksi ini akan langsung disembunyikan tanpa menghapus data.</span>
                        </label>
                    </div>

                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-brand rounded-pill px-4">
                            <i class="bi bi-save me-1"></i> Simpan Perubahan
                        </button>
                        <a href="{{ route('admin.sections.index') }}" class="btn btn-light border rounded-pill px-3">
                            Kembali ke Daftar
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>

@endsection
