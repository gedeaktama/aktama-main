@extends('layouts.admin')

@section('title', 'Kelola Jasa Web & Aplikasi')
@section('page_title', 'Manajemen Katalog Jasa Website & Aplikasi')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola katalog layanan pembuatan website, aplikasi kasir, dan software custom.</p>
        </div>
        <a href="{{ route('admin.services.create') }}" class="btn btn-brand rounded-pill btn-sm px-4">
            <i class="bi bi-plus-lg me-1"></i> Tambah Layanan Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Judul Layanan</th>
                        <th>Kategori</th>
                        <th>Estimasi Harga</th>
                        <th>Status Publikasi</th>
                        <th>Urutan</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($services as $srv)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $srv->title }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">/{{ $srv->slug }}</span>
                            </td>
                            <td><span class="badge bg-light text-dark border text-uppercase">{{ $srv->category }}</span></td>
                            <td><strong class="text-primary">{{ $srv->price_starting }}</strong></td>
                            <td>
                                @if($srv->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Aktif / Publik</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft / Nonaktif</span>
                                @endif
                            </td>
                            <td>{{ $srv->sort_order }}</td>
                            <td class="text-end pe-4">
                                <a href="{{ route('admin.services.edit', $srv->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Edit
                                </a>
                                <form action="{{ route('admin.services.destroy', $srv->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus layanan ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus layanan">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">Belum ada layanan.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
