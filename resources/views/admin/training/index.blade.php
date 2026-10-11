@extends('layouts.admin')

@section('title', 'Kelola Pelatihan AI')
@section('page_title', 'Manajemen Program Pelatihan Kecerdasan Artifisial')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola kurikulum dan silabus pelatihan AI untuk instansi, pendidik, dan bisnis.</p>
        </div>
        <a href="{{ route('admin.training.create') }}" class="btn btn-brand rounded-pill btn-sm px-4">
            <i class="bi bi-plus-lg me-1"></i> Tambah Program Pelatihan
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Judul Program</th>
                        <th>Kategori</th>
                        <th>Format & Durasi</th>
                        <th>Biaya / Investasi</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($programs as $prog)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $prog->title }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">Sasaran: {{ $prog->target_audience }}</span>
                            </td>
                            <td><span class="badge bg-light text-dark border">{{ $prog->category }}</span></td>
                            <td>
                                <div><span class="badge bg-secondary bg-opacity-10 text-dark text-uppercase" style="font-size: 0.65rem;">{{ $prog->delivery_format }}</span></div>
                                <small class="text-muted">{{ $prog->duration }}</small>
                            </td>
                            <td><strong class="text-primary">{{ $prog->price_info ?? 'Penawaran' }}</strong></td>
                            <td>
                                @if($prog->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Publik</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft</span>
                                @endif
                            </td>
                            <td class="text-end pe-4">
                                <a href="{{ route('admin.training.edit', $prog->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Edit
                                </a>
                                <form action="{{ route('admin.training.destroy', $prog->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus program pelatihan ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus program pelatihan">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">Belum ada program pelatihan.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
