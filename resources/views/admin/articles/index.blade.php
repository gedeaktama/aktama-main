@extends('layouts.admin')

@section('title', 'Semua Postingan & Berita')
@section('page_title', 'Postingan Berita (WordPress Posts Manager)')

@section('content')

    <div class="d-flex flex-wrap justify-content-between align-items-center gap-3 mb-3">
        <!-- TABS STATUS ALA WORDPRESS -->
        <ul class="nav nav-pills small">
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ !request('status') ? 'active bg-primary text-white' : 'text-dark' }}" href="{{ route('admin.articles.index') }}">
                    Semua <span class="badge {{ !request('status') ? 'bg-white text-primary' : 'bg-light text-muted border' }} ms-1">{{ $counts['all'] }}</span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ request('status') === 'published' ? 'active bg-success text-white' : 'text-dark' }}" href="{{ route('admin.articles.index', ['status' => 'published']) }}">
                    Diterbitkan <span class="badge {{ request('status') === 'published' ? 'bg-white text-success' : 'bg-light text-muted border' }} ms-1">{{ $counts['published'] }}</span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ request('status') === 'draft' ? 'active bg-secondary text-white' : 'text-dark' }}" href="{{ route('admin.articles.index', ['status' => 'draft']) }}">
                    Draf <span class="badge {{ request('status') === 'draft' ? 'bg-white text-secondary' : 'bg-light text-muted border' }} ms-1">{{ $counts['draft'] }}</span>
                </a>
            </li>
        </ul>

        <a href="{{ route('admin.articles.create') }}" class="btn btn-primary rounded-pill px-4 shadow-sm">
            <i class="bi bi-pencil-square me-1"></i> Tambah Postingan Baru
        </a>
    </div>

    <!-- FILTER BAR -->
    <div class="card border-0 shadow-sm rounded-4 bg-white p-3 mb-4">
        <form action="{{ route('admin.articles.index') }}" method="GET" class="row g-2 align-items-center">
            @if(request('status'))
                <input type="hidden" name="status" value="{{ request('status') }}">
            @endif

            <div class="col-md-4">
                <select name="category_id" class="form-select form-select-sm" onchange="this.form.submit()">
                    <option value="">Semua Kategori</option>
                    @foreach($categories as $cat)
                        <option value="{{ $cat->id }}" {{ request('category_id') == $cat->id ? 'selected' : '' }}>
                            {{ $cat->name }}
                        </option>
                    @endforeach
                </select>
            </div>

            <div class="col-md-6">
                <div class="input-group input-group-sm">
                    <input type="text" name="q" class="form-control" placeholder="Cari judul atau kata kunci berita..." value="{{ request('q') }}">
                    <button class="btn btn-primary" type="submit">
                        <i class="bi bi-search me-1"></i> Cari
                    </button>
                    @if(request('q') || request('category_id'))
                        <a href="{{ route('admin.articles.index', request('status') ? ['status' => request('status')] : []) }}" class="btn btn-light border" title="Reset Filter">
                            <i class="bi bi-x-circle"></i>
                        </a>
                    @endif
                </div>
            </div>
        </form>
    </div>

    <!-- TABEL POSTINGAN -->
    <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="bg-light text-muted small text-uppercase">
                    <tr>
                        <th class="ps-4" style="width: 70px;">Media</th>
                        <th>Judul Postingan</th>
                        <th>Penulis</th>
                        <th>Kategori</th>
                        <th>Tag</th>
                        <th>Status</th>
                        <th>Tanggal Terbit</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($articles as $art)
                        <tr>
                            <!-- Thumbnail -->
                            <td class="ps-4">
                                @if($art->image)
                                    <img src="{{ asset('images/' . $art->image) }}" alt="Thumbnail" class="rounded-3 shadow-xs object-fit-cover" style="width: 54px; height: 38px;">
                                @else
                                    <div class="bg-light rounded-3 d-flex align-items-center justify-content-center text-muted border" style="width: 54px; height: 38px;">
                                        <i class="bi bi-image" style="font-size: 1rem;"></i>
                                    </div>
                                @endif
                            </td>

                            <!-- Judul & Slug -->
                            <td>
                                <strong class="text-dark d-block mb-1">{{ $art->title }}</strong>
                                <span class="text-muted font-monospace" style="font-size: 0.72rem;">
                                    /artikel/{{ $art->slug }}
                                </span>
                            </td>

                            <!-- Penulis -->
                            <td class="text-muted">{{ $art->author }}</td>

                            <!-- Kategori -->
                            <td>
                                <span class="badge bg-light text-dark border">
                                    {{ $art->category?->name ?? 'Tanpa Kategori' }}
                                </span>
                            </td>

                            <!-- Tag -->
                            <td>
                                @if($art->tags)
                                    <span class="text-muted" style="font-size: 0.75rem;">
                                        {{ Str::limit($art->tags, 25) }}
                                    </span>
                                @else
                                    <span class="text-muted opacity-50">-</span>
                                @endif
                            </td>

                            <!-- Status -->
                            <td>
                                @if($art->status === 'published')
                                    <span class="badge bg-success bg-opacity-10 text-success">
                                        <i class="bi bi-check-circle-fill me-1"></i> Diterbitkan
                                    </span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-muted">
                                        <i class="bi bi-pencil-fill me-1"></i> Draf
                                    </span>
                                @endif
                            </td>

                            <!-- Tanggal -->
                            <td class="text-muted">
                                {{ $art->published_at?->format('d/m/Y H:i') ?? $art->created_at->format('d/m/Y') }}
                            </td>

                            <!-- Aksi -->
                            <td class="text-end pe-4">
                                <div class="d-flex justify-content-end align-items-center gap-1">
                                    @if($art->status === 'published')
                                        <a href="{{ route('articles.show', $art->slug) }}" target="_blank" class="btn btn-sm btn-light border rounded-pill px-2" title="Lihat di Web Publik">
                                            <i class="bi bi-box-arrow-up-right"></i>
                                        </a>
                                    @endif

                                    <!-- Quick Edit Modal Trigger -->
                                    <button type="button" class="btn btn-sm btn-outline-warning text-dark rounded-pill px-2 btn-quick-edit-art" 
                                            title="Edit Cepat (Ganti judul, slug, kategori, status tanpa buka halaman edit)"
                                            data-id="{{ $art->id }}"
                                            data-title="{{ $art->title }}"
                                            data-slug="{{ $art->slug }}"
                                            data-category="{{ $art->category_id }}"
                                            data-status="{{ $art->status }}"
                                            data-url="{{ route('admin.articles.quickUpdate', $art->id) }}">
                                        <i class="bi bi-lightning-charge"></i>
                                    </button>

                                    <!-- 1-Click Duplicate -->
                                    <form action="{{ route('admin.articles.duplicate', $art->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Duplikasi artikel ini?');">
                                        @csrf
                                        <button type="submit" class="btn btn-sm btn-outline-info rounded-pill px-2" title="Duplikasi Artikel 1-Klik">
                                            <i class="bi bi-files"></i>
                                        </button>
                                    </form>

                                    <a href="{{ route('admin.articles.edit', $art->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                        <i class="bi bi-pencil me-1"></i> Edit
                                    </a>

                                    <form action="{{ route('admin.articles.destroy', $art->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Pindahkan artikel ini ke tong sampah?')">
                                        @csrf
                                        @method('DELETE')
                                        <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-2" title="Hapus artikel">
                                            <i class="bi bi-trash"></i>
                                        </button>
                                    </form>
                                </div>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="8" class="text-center py-5 text-muted">
                                <i class="bi bi-newspaper display-6 d-block mb-2 text-secondary opacity-50"></i>
                                Tidak ada postingan berita yang sesuai kriteria pencarian.
                            </td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        @if($articles->hasPages())
            <div class="card-footer bg-white py-3 border-top">
                {{ $articles->links() }}
            </div>
        @endif
    </div>

    <!-- MODAL QUICK EDIT ARTIKEL ALA WORDPRESS -->
    <div class="modal fade" id="modalQuickEditArticle" tabindex="-1" aria-labelledby="modalQuickEditArticleLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <form id="formQuickEditArticle" method="POST">
                    @csrf
                    @method('PUT')
                    <div class="modal-header bg-dark text-white py-3 px-4">
                        <h6 class="modal-title fw-bold mb-0" id="modalQuickEditArticleLabel">
                            <i class="bi bi-lightning-charge text-warning me-2"></i> Edit Cepat Artikel (Quick Edit)
                        </h6>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Tutup"></button>
                    </div>
                    <div class="modal-body p-4 bg-white">
                        <div class="mb-3">
                            <label class="form-label small fw-bold text-dark mb-1">Judul Artikel / Berita</label>
                            <input type="text" name="title" id="qe-art-title" class="form-control form-control-sm" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label small fw-bold text-dark mb-1">URL / Permalink Slug</label>
                            <input type="text" name="slug" id="qe-art-slug" class="form-control form-control-sm font-monospace" required>
                        </div>
                        <div class="row g-2 mb-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-dark mb-1">Kategori</label>
                                <select name="category_id" id="qe-art-category" class="form-select form-select-sm" required>
                                    @foreach($categories as $cat)
                                        <option value="{{ $cat->id }}">{{ $cat->name }}</option>
                                    @endforeach
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-dark mb-1">Status Publikasi</label>
                                <select name="status" id="qe-art-status" class="form-select form-select-sm" required>
                                    <option value="published">Diterbitkan (Publik)</option>
                                    <option value="draft">Draf (Disimpan)</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer bg-light border-top py-2 px-4 d-flex justify-content-between">
                        <button type="button" class="btn btn-sm btn-light border rounded-pill px-3" data-bs-dismiss="modal">Batal</button>
                        <button type="submit" class="btn btn-sm btn-primary rounded-pill px-4 fw-bold shadow-xs">
                            <i class="bi bi-check2-circle me-1"></i> Perbarui Cepat
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

@endsection

@push('scripts')
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const modalEl = document.getElementById('modalQuickEditArticle');
        const formEl = document.getElementById('formQuickEditArticle');
        const titleInput = document.getElementById('qe-art-title');
        const slugInput = document.getElementById('qe-art-slug');
        const catInput = document.getElementById('qe-art-category');
        const statusInput = document.getElementById('qe-art-status');

        document.addEventListener('click', function (e) {
            const btn = e.target.closest('.btn-quick-edit-art');
            if (btn) {
                e.preventDefault();
                formEl.action = btn.getAttribute('data-url');
                titleInput.value = btn.getAttribute('data-title') || '';
                slugInput.value = btn.getAttribute('data-slug') || '';
                catInput.value = btn.getAttribute('data-category') || '';
                statusInput.value = btn.getAttribute('data-status') || 'published';

                const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
                modal.show();
            }
        });
    });
</script>
@endpush
