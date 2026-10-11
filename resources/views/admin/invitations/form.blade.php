@extends('layouts.admin')

@section('title', $package->exists ? 'Edit Paket Undangan' : 'Tambah Paket Baru')
@section('page_title', $package->exists ? 'Edit Paket: ' . $package->name : 'Tambah Paket Baru')

@section('content')

    <div class="card border-0 shadow-sm rounded-4 bg-white p-4 max-w-2xl">
        <form action="{{ $package->exists ? route('admin.invitations.update', $package->id) : route('admin.invitations.store') }}" method="POST">
            @csrf
            @if($package->exists)
                @method('PUT')
            @endif

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Nama Paket Undangan *</label>
                <input type="text" name="name" class="form-control" required value="{{ old('name', $package->name) }}" placeholder="Contoh: Paket Gold (Favorit Pengantin)">
            </div>

            <div class="row g-3 mb-3">
                <div class="col-md-6">
                    <label class="form-label small fw-bold text-dark">Harga Normal (Rp) *</label>
                    <input type="number" name="price" class="form-control" required value="{{ old('price', $package->price ?? 150000) }}">
                </div>
                <div class="col-md-6">
                    <label class="form-label small fw-bold text-dark">Harga Promo / Diskon (Rp)</label>
                    <input type="number" name="discount_price" class="form-control" value="{{ old('discount_price', $package->discount_price) }}" placeholder="Biarkan kosong jika tidak promo">
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">URL Contoh Demo Undangan</label>
                <input type="url" name="demo_url" class="form-control" value="{{ old('demo_url', $package->demo_url) }}" placeholder="http://localhost:8080/undanganonline/public/undangan/...">
            </div>

            <div class="mb-3">
                <label class="form-label small fw-bold text-dark">Fitur Unggulan (1 Fitur per Baris)</label>
                <textarea name="features_text" class="form-control" rows="5" placeholder="Pilihan Seluruh Tema&#10;Personalisasi Tamu&#10;Musik Latar Audio&#10;Amplop Digital">{{ old('features_text', is_array($package->features) ? implode("\n", $package->features) : '') }}</textarea>
            </div>

            <div class="row g-3 mb-4">
                <div class="col-md-6">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" name="is_popular" value="1" id="is_popular" {{ old('is_popular', $package->is_popular) ? 'checked' : '' }}>
                        <label class="form-check-label text-dark fw-bold small" for="is_popular">Tandai sebagai Paket Terpopuler</label>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" name="is_published" value="1" id="is_published" {{ old('is_published', $package->is_published ?? true) ? 'checked' : '' }}>
                        <label class="form-check-label text-dark fw-bold small" for="is_published">Publikasikan Paket Ini</label>
                    </div>
                </div>
            </div>

            <div class="d-flex gap-2">
                <button type="submit" class="btn btn-danger rounded-pill px-4 fw-semibold">
                    <i class="bi bi-save me-1"></i> Simpan Paket
                </button>
                <a href="{{ route('admin.invitations.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
            </div>
        </form>
    </div>

@endsection
