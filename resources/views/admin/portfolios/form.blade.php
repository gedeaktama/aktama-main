@extends('layouts.admin')

@section('title', $portfolio->exists ? 'Edit Portofolio' : 'Tambah Portofolio Baru')
@section('page_title', $portfolio->exists ? 'Edit Portofolio: ' . $portfolio->title : 'Tambah Portofolio Baru')

@section('content')

    <div class="card border-0 shadow-sm rounded-4 bg-white p-4 max-w-2xl">
        <form action="{{ $portfolio->exists ? route('admin.portfolios.update', $portfolio->id) : route('admin.portfolios.store') }}" method="POST">
            @csrf
            @if($portfolio->exists)
                @method('PUT')
            @endif

            <div class="row g-3 mb-3">
                <div class="col-md-8">
                    <label class="form-label small fw-bold text-dark">Judul Proyek *</label>
                    <input type="text" name="title" class="form-control" required value="{{ old('title', $portfolio->title) }}" placeholder="Contoh: Sistem Informasi Kelulusan Sekolah">
                </div>
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Kategori *</label>
                    <select name="category" class="form-select" required>
                        <option value="aplikasi" {{ old('category', $portfolio->category) === 'aplikasi' ? 'selected' : '' }}>Aplikasi Web</option>
                        <option value="website" {{ old('category', $portfolio->category) === 'website' ? 'selected' : '' }}>Website Profil</option>
                        <option value="sistem-informasi" {{ old('category', $portfolio->category) === 'sistem-informasi' ? 'selected' : '' }}>Sistem Informasi</option>
                    </select>
                </div>
            </div>

            <div class="row g-3 mb-3">
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-dark">Kategori Klien</label>
                    <input type="text" name="client_type" class="form-control" value="{{ old('client_type', $portfolio->client_type) }}" placeholder="Contoh: Lembaga Pendidikan / UMKM">
                </div>
                <div class="col-md-5">
                    <label class="form-label small fw-bold text-dark">Teknologi yang Digunakan *</label>
                    <input type="text" name="technology" class="form-control" required value="{{ old('technology', $portfolio->technology) }}" placeholder="Contoh: Laravel, MySQL, Bootstrap">
                </div>
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-dark">Tahun Pengerjaan</label>
                    <input type="text" name="project_year" class="form-control" value="{{ old('project_year', $portfolio->project_year ?? date('Y')) }}" placeholder="2025">
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Deskripsi Proyek & Solusi yang Dibangun</label>
                <textarea name="description" class="form-control" rows="4">{{ old('description', $portfolio->description) }}</textarea>
            </div>

            <div class="form-check form-switch mb-4">
                <input class="form-check-input" type="checkbox" name="is_published" value="1" id="is_published" {{ old('is_published', $portfolio->is_published ?? true) ? 'checked' : '' }}>
                <label class="form-check-label text-dark fw-bold small" for="is_published">Publikasikan ke Halaman Portofolio</label>
            </div>

            <div class="d-flex gap-2">
                <button type="submit" class="btn btn-brand rounded-pill px-4">
                    <i class="bi bi-save me-1"></i> Simpan Portofolio
                </button>
                <a href="{{ route('admin.portfolios.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
            </div>
        </form>
    </div>

@endsection
