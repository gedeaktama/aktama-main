@extends('layouts.admin')

@section('title', 'Manajemen Halaman')
@section('page_title', 'Manajemen Halaman Kustom (CMS Pages)')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h6 class="text-muted mb-0">Kelola halaman kustom statis & visual canvas layaknya WordPress.</h6>
        </div>
        <a href="{{ route('admin.pages.create') }}" class="btn btn-brand rounded-pill px-4">
            <i class="bi bi-plus-circle me-1"></i> Tambah Halaman Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light border-bottom small text-uppercase text-muted">
                    <tr>
                        <th class="ps-4">Judul Halaman</th>
                        <th>URL / Permalink</th>
                        <th>Tipe Editor</th>
                        <th>Status</th>
                        <th>Dibuat</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($pages as $page)
                        <tr>
                            <td class="ps-4">
                                <div class="fw-bold text-dark">{{ $page->title }}</div>
                                <small class="text-muted">{{ Str::limit($page->meta_title ?: $page->title, 40) }}</small>
                            </td>
                            <td>
                                <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="small font-monospace text-decoration-none text-primary">
                                    /halaman/{{ $page->slug }} <i class="bi bi-box-arrow-up-right ms-1" style="font-size: 0.7rem;"></i>
                                </a>
                            </td>
                            <td>
                                @if($page->editor_type === 'builder')
                                    <span class="badge bg-primary bg-opacity-10 text-primary">
                                        <i class="bi bi-brush me-1"></i> Visual Canvas (Opsi B)
                                    </span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-dark">
                                        <i class="bi bi-file-earmark-text me-1"></i> Standar (HTML/Teks)
                                    </span>
                                @endif
                            </td>
                            <td>
                                @if($page->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">Publik</span>
                                @else
                                    <span class="badge bg-warning bg-opacity-10 text-warning">Draf</span>
                                @endif
                            </td>
                            <td class="small text-muted">
                                {{ $page->created_at?->format('d M Y') ?? '-' }}
                            </td>
                            <td class="text-end pe-4">
                                <div class="d-flex justify-content-end align-items-center gap-1">
                                    @if($page->editor_type === 'builder')
                                        <a href="{{ route('admin.pages.builder', $page->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3" title="Buka Visual Drag & Drop Canvas Builder">
                                            <i class="bi bi-palette-fill me-1"></i> Visual Builder
                                        </a>
                                    @endif

                                    <a href="{{ route('admin.pages.edit', $page->id) }}" class="btn btn-sm btn-outline-secondary rounded-pill px-3" title="Edit Rincian">
                                        <i class="bi bi-pencil me-1"></i> Edit
                                    </a>

                                    <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="btn btn-sm btn-light border rounded-pill px-2" title="Lihat Tampilan">
                                        <i class="bi bi-eye me-1"></i> Lihat
                                    </a>

                                    <form action="{{ route('admin.pages.destroy', $page->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Yakin ingin menghapus halaman ini?');">
                                        @csrf
                                        @method('DELETE')
                                        <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-2" title="Hapus Halaman">
                                            <i class="bi bi-trash me-1"></i> Hapus
                                        </button>
                                    </form>
                                </div>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-5 text-muted">
                                <i class="bi bi-file-earmark-plus display-6 d-block mb-2 text-secondary opacity-50"></i>
                                Belum ada halaman kustom. Klik "Tambah Halaman Baru" untuk mulai membuat halaman.
                            </td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        @if($pages->hasPages())
            <div class="card-footer bg-white py-3 border-top">
                {{ $pages->links() }}
            </div>
        @endif
    </div>

@endsection
