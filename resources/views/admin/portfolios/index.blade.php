@extends('layouts.admin')

@section('title', 'Kelola Portofolio')
@section('page_title', 'Manajemen Rekam Jejak Portofolio')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola portofolio proyek dan studi kasus implementasi nyata.</p>
        </div>
        <a href="{{ route('admin.portfolios.create') }}" class="btn btn-primary rounded-pill btn-sm px-4">
            <i class="bi bi-plus-lg me-1"></i> Tambah Portofolio Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Judul Proyek</th>
                        <th>Kategori & Klien</th>
                        <th>Teknologi</th>
                        <th>Tahun</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($portfolios as $port)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $port->title }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">/{{ $port->slug }}</span>
                            </td>
                            <td>
                                <span class="badge bg-light text-dark border">{{ $port->category }}</span>
                                <small class="text-muted d-block">{{ $port->client_type }}</small>
                            </td>
                            <td><span class="font-monospace small text-primary">{{ $port->technology }}</span></td>
                            <td>{{ $port->project_year }}</td>
                            <td>
                                @if($port->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Publik</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft</span>
                                @endif
                            </td>
                            <td class="text-end pe-4">
                                <a href="{{ route('admin.portfolios.edit', $port->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Edit
                                </a>
                                <form action="{{ route('admin.portfolios.destroy', $port->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus portofolio ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus portofolio">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">Belum ada portofolio.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
