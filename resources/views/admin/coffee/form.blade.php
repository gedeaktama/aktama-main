@extends('layouts.admin')

@section('title', $product->exists ? 'Edit Produk Kopi' : 'Tambah Produk Kopi Baru')
@section('page_title', $product->exists ? 'Kelola: ' . $product->name : 'Tambah Produk Kopi Baru')

@section('content')

    <div class="row g-4">
        <!-- FORM PRODUK UTAMA -->
        <div class="col-lg-{{ $product->exists ? '7' : '12' }}">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <h6 class="fw-bold text-dark border-bottom pb-3 mb-3">Informasi Utama Produk Kopi</h6>
                <form action="{{ $product->exists ? route('admin.coffee.update', $product->id) : route('admin.coffee.store') }}" method="POST">
                    @csrf
                    @if($product->exists)
                        @method('PUT')
                    @endif

                    <div class="row g-3 mb-3">
                        <div class="col-md-8">
                            <label class="form-label small fw-bold text-dark">Nama Produk Kopi *</label>
                            <input type="text" name="name" class="form-control" required value="{{ old('name', $product->name) }}" placeholder="Contoh: Kopi Robusta Pilihan Aktama">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-dark">SKU / Kode Produk</label>
                            <input type="text" name="sku" class="form-control" value="{{ old('sku', $product->sku) }}" placeholder="CF-ROB-01">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Daerah Asal Perkebunan</label>
                            <input type="text" name="origin" class="form-control" value="{{ old('origin', $product->origin) }}" placeholder="Contoh: Dataran Tinggi Mitra">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Tingkat Sangrai (Roast Level)</label>
                            <input type="text" name="roast_level" class="form-control" value="{{ old('roast_level', $product->roast_level) }}" placeholder="Medium to Dark">
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Deskripsi & Karakter Cita Rasa</label>
                        <textarea name="description" class="form-control" rows="4">{{ old('description', $product->description) }}</textarea>
                    </div>

                    @if(!$product->exists)
                        <div class="row g-3 p-3 bg-light rounded-3 mb-3">
                            <div class="col-12"><strong class="small text-dark">Varian Awal (Kemasan 250g):</strong></div>
                            <div class="col-md-6">
                                <label class="form-label small text-muted">Harga Eceran (Rp)</label>
                                <input type="number" name="default_retail_price" class="form-control" value="35000" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small text-muted">Harga Grosir Kafe (Rp)</label>
                                <input type="number" name="default_wholesale_price" class="form-control" value="28000" required>
                            </div>
                        </div>
                    @endif

                    <div class="form-check form-switch mb-4">
                        <input class="form-check-input" type="checkbox" name="is_published" value="1" id="is_published" {{ old('is_published', $product->is_published ?? true) ? 'checked' : '' }}>
                        <label class="form-check-label text-dark fw-bold small" for="is_published">Tampilkan di Halaman Katalog Kopi</label>
                    </div>

                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-warning text-dark fw-bold rounded-pill px-4">
                            <i class="bi bi-save me-1"></i> Simpan Produk Kopi
                        </button>
                        <a href="{{ route('admin.coffee.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
                    </div>
                </form>
            </div>
        </div>

        <!-- DAFTAR & FORM VARIAN (JIKA PRODUK SUDAH ADA) -->
        @if($product->exists)
            <div class="col-lg-5">
                <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                    <h6 class="fw-bold text-dark border-bottom pb-3 mb-3">
                        <i class="bi bi-tags-fill text-warning me-2"></i> Kelola Varian Ukuran & Harga
                    </h6>

                    <!-- List Varian -->
                    <div class="mb-4">
                        <small class="text-muted fw-bold d-block mb-2">Varian yang Tersedia Saat Ini:</small>
                        <ul class="list-group list-group-flush border rounded-3 mb-0">
                            @forelse($product->variants as $var)
                                <li class="list-group-item d-flex justify-content-between align-items-center small py-2">
                                    <div>
                                        <strong class="text-dark d-block">{{ $var->variant_name }} ({{ $var->weight_grams }}g)</strong>
                                        <span class="text-primary">Eceran: Rp {{ number_format($var->retail_price, 0, ',', '.') }}</span> | 
                                        <span class="text-success fw-bold">Grosir: Rp {{ number_format($var->wholesale_price, 0, ',', '.') }}</span>
                                        <small class="text-muted">(Min. {{ $var->min_wholesale_qty }})</small>
                                    </div>
                                    <form action="{{ route('admin.coffee.variants.destroy', $var->id) }}" method="POST" onsubmit="return confirm('Hapus varian ini?')">
                                        @csrf
                                        @method('DELETE')
                                        <button type="submit" class="btn btn-light text-danger btn-sm border-0 p-1"><i class="bi bi-x-circle fs-6"></i></button>
                                    </form>
                                </li>
                            @empty
                                <li class="list-group-item text-muted text-center py-3">Belum ada varian.</li>
                            @endforelse
                        </ul>
                    </div>

                    <!-- Tambah Varian Baru Form -->
                    <div class="border rounded-3 p-3 bg-light">
                        <strong class="text-dark small d-block mb-2">+ Tambah Varian Ukuran Baru:</strong>
                        <form action="{{ route('admin.coffee.variants.store', $product->id) }}" method="POST">
                            @csrf
                            <div class="mb-2">
                                <input type="text" name="variant_name" class="form-control form-control-sm" placeholder="Contoh: Kemasan 1kg (Grosir)" required>
                            </div>
                            <div class="row g-2 mb-2">
                                <div class="col-6">
                                    <input type="number" name="weight_grams" class="form-control form-control-sm" placeholder="Berat (gram)" value="1000" required>
                                </div>
                                <div class="col-6">
                                    <input type="number" name="min_wholesale_qty" class="form-control form-control-sm" placeholder="Min. Grosir" value="5" required>
                                </div>
                            </div>
                            <div class="row g-2 mb-3">
                                <div class="col-6">
                                    <input type="number" name="retail_price" class="form-control form-control-sm" placeholder="Harga Eceran (Rp)" required>
                                </div>
                                <div class="col-6">
                                    <input type="number" name="wholesale_price" class="form-control form-control-sm" placeholder="Harga Grosir (Rp)" required>
                                </div>
                            </div>
                            <button type="submit" class="btn btn-dark btn-sm rounded-pill w-100">
                                Tambahkan Varian
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        @endif
    </div>

@endsection
