@extends('layouts.admin')

@section('title', 'Kelola Paket Undangan')
@section('page_title', 'Manajemen Paket Undangan Online')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola paket penawaran undangan digital, harga diskon, dan fitur.</p>
        </div>
        <a href="{{ route('admin.invitations.create') }}" class="btn btn-danger rounded-pill btn-sm px-4">
            <i class="bi bi-plus-lg me-1"></i> Tambah Paket Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Nama Paket</th>
                        <th>Harga Normal</th>
                        <th>Harga Promo</th>
                        <th>Status Favorit</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($packages as $pkg)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $pkg->name }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">/{{ $pkg->slug }}</span>
                            </td>
                            <td>Rp {{ number_format($pkg->price, 0, ',', '.') }}</td>
                            <td>
                                @if($pkg->discount_price)
                                    <strong class="text-danger">Rp {{ number_format($pkg->discount_price, 0, ',', '.') }}</strong>
                                @else
                                    <span class="text-muted">-</span>
                                @endif
                            </td>
                            <td>
                                @if($pkg->is_popular)
                                    <span class="badge bg-danger rounded-pill">Favorit Pengantin</span>
                                @else
                                    <span class="text-muted">-</span>
                                @endif
                            </td>
                            <td>
                                @if($pkg->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Publik</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft</span>
                                @endif
                            </td>
                            <td class="text-end pe-4">
                                <a href="{{ route('admin.invitations.edit', $pkg->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Edit
                                </a>
                                <form action="{{ route('admin.invitations.destroy', $pkg->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus paket undangan ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus paket undangan">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">Belum ada paket undangan.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
