@extends('layouts.admin')

@section('title', 'Kelola Produk Kopi')
@section('page_title', 'Manajemen Katalog Kopi & Varian Harga')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola produk kopi (Robusta/Arabika) beserta varian ukuran kemasan, harga eceran, dan harga grosir kafe.</p>
        </div>
        <a href="{{ route('admin.coffee.create') }}" class="btn btn-warning text-dark rounded-pill btn-sm px-4 fw-bold">
            <i class="bi bi-plus-lg me-1"></i> Tambah Produk Kopi Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Nama Produk & SKU</th>
                        <th>Asal & Sangrai</th>
                        <th>Varian Ukuran & Harga</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($products as $p)
                        <tr>
                            <td class="ps-4">
                                <span class="badge bg-dark small mb-1">{{ $p->sku }}</span>
                                <strong class="text-dark d-block">{{ $p->name }}</strong>
                            </td>
                            <td>
                                <div><small class="text-muted"><i class="bi bi-geo-alt me-1"></i>{{ $p->origin }}</small></div>
                                <div><small class="text-muted"><i class="bi bi-fire me-1"></i>{{ $p->roast_level }}</small></div>
                            </td>
                            <td>
                                <ul class="list-unstyled mb-0" style="font-size: 0.75rem;">
                                    @foreach($p->variants as $v)
                                        <li class="mb-1">
                                            <strong>{{ $v->variant_name }}</strong>: 
                                            Eceran Rp {{ number_format($v->retail_price, 0, ',', '.') }} | 
                                            <span class="text-success fw-bold">Grosir Rp {{ number_format($v->wholesale_price, 0, ',', '.') }}</span> (Min. {{ $v->min_wholesale_qty }})
                                        </li>
                                    @endforeach
                                </ul>
                            </td>
                            <td>
                                @if($p->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Publik</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft</span>
                                @endif
                            </td>
                            <td class="text-end pe-4">
                                <a href="{{ route('admin.coffee.edit', $p->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Kelola Varian
                                </a>
                                <form action="{{ route('admin.coffee.destroy', $p->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus produk kopi ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus produk kopi">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="5" class="text-center py-4 text-muted">Belum ada produk kopi.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
