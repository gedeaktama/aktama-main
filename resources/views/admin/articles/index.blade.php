@extends('layouts.admin')

@section('title', 'Kelola Artikel & SEO')
@section('page_title', 'Manajemen Artikel Blog & SEO Content')

@section('content')

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <p class="text-muted small mb-0">Kelola artikel blog edukasi, wawasan teknologi, dan metadata SEO.</p>
        </div>
        <a href="{{ route('admin.articles.create') }}" class="btn btn-primary rounded-pill btn-sm px-4">
            <i class="bi bi-plus-lg me-1"></i> Tulis Artikel Baru
        </a>
    </div>

    <div class="card border-0 shadow-sm rounded-4 bg-white">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small">
                    <tr>
                        <th class="ps-4">Judul Artikel</th>
                        <th>Kategori</th>
                        <th>Penulis</th>
                        <th>Status</th>
                        <th>Tanggal Publikasi</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($articles as $art)
                        <tr>
                            <td class="ps-4">
                                <strong class="text-dark d-block">{{ $art->title }}</strong>
                                <span class="text-muted" style="font-size: 0.75rem;">/artikel/{{ $art->slug }}</span>
                            </td>
                            <td><span class="badge bg-light text-dark border">{{ $art->category?->name ?? 'Umum' }}</span></td>
                            <td>{{ $art->author }}</td>
                            <td>
                                @if($art->status === 'published')
                                    <span class="badge bg-success bg-opacity-10 text-success">Published</span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">Draft</span>
                                @endif
                            </td>
                            <td class="text-muted">{{ $art->published_at?->format('d/m/Y') ?? '-' }}</td>
                            <td class="text-end pe-4">
                                @if($art->status === 'published')
                                    <a href="{{ route('articles.show', $art->slug) }}" target="_blank" class="btn btn-sm btn-light border rounded-pill px-2" title="Lihat di Web Publik">
                                        <i class="bi bi-box-arrow-up-right"></i>
                                    </a>
                                @endif
                                <a href="{{ route('admin.articles.edit', $art->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                    <i class="bi bi-pencil me-1"></i> Edit
                                </a>
                                <form action="{{ route('admin.articles.destroy', $art->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Hapus artikel ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-3" title="Hapus artikel">
                                        <i class="bi bi-trash me-1"></i> Hapus
                                    </button>
                                </form>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="6" class="text-center py-4 text-muted">Belum ada artikel.</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

@endsection
