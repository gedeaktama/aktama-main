@extends('layouts.admin')

@section('title', $service->exists ? 'Edit Layanan' : 'Tambah Layanan Baru')
@section('page_title', $service->exists ? 'Edit Layanan: ' . $service->title : 'Tambah Layanan Baru')

@section('content')

    <div class="card border-0 shadow-sm rounded-4 bg-white p-4 max-w-2xl">
        <form action="{{ $service->exists ? route('admin.services.update', $service->id) : route('admin.services.store') }}" method="POST">
            @csrf
            @if($service->exists)
                @method('PUT')
            @endif

            <div class="row g-3 mb-3">
                <div class="col-md-8">
                    <label class="form-label small fw-bold text-dark">Judul Layanan *</label>
                    <input type="text" name="title" class="form-control" required value="{{ old('title', $service->title) }}" placeholder="Contoh: Website Profil Perusahaan">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Kategori *</label>
                    <select name="category" class="form-select" required>
                        <option value="website" {{ old('category', $service->category) === 'website' ? 'selected' : '' }}>Website</option>
                        <option value="aplikasi" {{ old('category', $service->category) === 'aplikasi' ? 'selected' : '' }}>Aplikasi Web</option>
                        <option value="sistem-informasi" {{ old('category', $service->category) === 'sistem-informasi' ? 'selected' : '' }}>Sistem Informasi</option>
                        <option value="otomasi" {{ old('category', $service->category) === 'otomasi' ? 'selected' : '' }}>Otomasi Kerja</option>
                    </select>
                </div>
            </div>

            <div class="row g-3 mb-3">
                <div class="col-md-6">
                    <label class="form-label small fw-bold text-dark">Estimasi Harga Mulai</label>
                    <input type="text" name="price_starting" class="form-control" value="{{ old('price_starting', $service->price_starting) }}" placeholder="Contoh: Mulai Rp 1.500.000">
                </div>
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-dark">Ikon Bootstrap</label>
                    <input type="text" name="icon" class="form-control" value="{{ old('icon', $service->icon ?? 'bi-globe') }}" placeholder="bi-globe">
                </div>
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-dark">Urutan Tampil</label>
                    <input type="number" name="sort_order" class="form-control" value="{{ old('sort_order', $service->sort_order ?? 0) }}">
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Ringkasan Singkat (Excerpt)</label>
                <input type="text" name="excerpt" class="form-control" value="{{ old('excerpt', $service->excerpt) }}" placeholder="1-2 kalimat pengantar...">
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Deskripsi Lengkap Layanan</label>
                <textarea name="description" class="form-control" rows="4">{{ old('description', $service->description) }}</textarea>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Fitur Unggulan (1 Fitur per Baris)</label>
                <textarea name="features_text" class="form-control" rows="4" placeholder="Desain Responsif&#10;Bebas Malware Judol&#10;Optimasi SEO Dasar">{{ old('features_text', is_array($service->features) ? implode("\n", $service->features) : '') }}</textarea>
            </div>

            <div class="form-check form-switch mb-4">
                <input class="form-check-input" type="checkbox" name="is_published" value="1" id="is_published" {{ old('is_published', $service->is_published ?? true) ? 'checked' : '' }}>
                <label class="form-check-label text-dark fw-bold small" for="is_published">Publikasikan Layanan Ini ke Website</label>
            </div>

            <div class="d-flex gap-2">
                <button type="submit" class="btn btn-brand rounded-pill px-4">
                    <i class="bi bi-save me-1"></i> Simpan Layanan
                </button>
                <a href="{{ route('admin.services.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
            </div>
        </form>
    </div>

@endsection
