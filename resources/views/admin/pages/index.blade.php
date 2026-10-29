@extends('layouts.admin')

@section('title', 'Semua Halaman CMS')
@section('page_title', 'Halaman Kustom (WordPress Pages Manager)')

@section('content')

    <div class="d-flex flex-wrap justify-content-between align-items-center gap-3 mb-3">
        <!-- TABS STATUS ALA WORDPRESS -->
        <ul class="nav nav-pills small">
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ !request('status') ? 'active bg-primary text-white' : 'text-dark' }}" href="{{ route('admin.pages.index') }}">
                    Semua <span class="badge {{ !request('status') ? 'bg-white text-primary' : 'bg-light text-muted border' }} ms-1">{{ $counts['all'] }}</span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ request('status') === 'published' ? 'active bg-success text-white' : 'text-dark' }}" href="{{ route('admin.pages.index', ['status' => 'published']) }}">
                    Publik <span class="badge {{ request('status') === 'published' ? 'bg-white text-success' : 'bg-light text-muted border' }} ms-1">{{ $counts['published'] }}</span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link py-1 px-3 rounded-pill {{ request('status') === 'draft' ? 'active bg-warning text-dark' : 'text-dark' }}" href="{{ route('admin.pages.index', ['status' => 'draft']) }}">
                    Draf <span class="badge {{ request('status') === 'draft' ? 'bg-dark text-white' : 'bg-light text-muted border' }} ms-1">{{ $counts['draft'] }}</span>
                </a>
            </li>
        </ul>

        <a href="{{ route('admin.pages.create') }}" class="btn btn-primary rounded-pill px-4 shadow-sm">
            <i class="bi bi-file-earmark-plus me-1"></i> Tambah Halaman Baru
        </a>
    </div>

    <!-- BANNER PANDUAN ELEMENTOR / VISUAL BUILDER -->
    <div class="card border-0 shadow-sm rounded-4 p-3 mb-4 text-white" style="background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);">
        <div class="d-flex flex-wrap align-items-center justify-content-between gap-3">
            <div class="d-flex align-items-center gap-3">
                <div class="p-3 bg-white text-primary rounded-circle shadow-sm fs-4 d-none d-sm-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">
                    <i class="bi bi-brush"></i>
                </div>
                <div>
                    <h6 class="fw-bold mb-1">
                        <i class="bi bi-palette-fill me-1"></i> Desain Landing Page Visual Seperti Elementor WordPress
                    </h6>
                    <p class="mb-0 small text-white-50">
                        Ingin membuat landing page kustom yang dinamis? Klik <strong>"Tambah Halaman Baru"</strong>, pilih opsi <strong>"Visual Drag & Drop Canvas (Elementor Style)"</strong>, lalu susun Hero Banner, Grid Kolom, Testimoni, FAQ Accordion, hingga tombol WhatsApp secara visual.
                    </p>
                </div>
            </div>
            <div>
                <a href="{{ route('admin.pages.create') }}" class="btn btn-light text-primary btn-sm rounded-pill px-3 fw-bold shadow-sm text-nowrap">
                    <i class="bi bi-plus-circle me-1"></i> Buat Halaman Visual
                </a>
            </div>
        </div>
    </div>

    <!-- SEARCH BAR -->
    <div class="card border-0 shadow-sm rounded-4 bg-white p-3 mb-4">
        <form action="{{ route('admin.pages.index') }}" method="GET" class="row g-2 align-items-center">
            @if(request('status'))
                <input type="hidden" name="status" value="{{ request('status') }}">
            @endif

            <div class="col-md-6">
                <div class="input-group input-group-sm">
                    <input type="text" name="q" class="form-control" placeholder="Cari judul halaman atau URL slug..." value="{{ request('q') }}">
                    <button class="btn btn-primary" type="submit">
                        <i class="bi bi-search me-1"></i> Cari Halaman
                    </button>
                    @if(request('q'))
                        <a href="{{ route('admin.pages.index', request('status') ? ['status' => request('status')] : []) }}" class="btn btn-light border" title="Reset Filter">
                            <i class="bi bi-x-circle"></i>
                        </a>
                    @endif
                </div>
            </div>
        </form>
    </div>

    <!-- TABEL HALAMAN -->
    <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light border-bottom small text-uppercase text-muted">
                    <tr>
                        <th class="ps-4">Judul Halaman</th>
                        <th>URL / Permalink</th>
                        <th>Metode Editor</th>
                        <th>Template Layout</th>
                        <th>Urutan</th>
                        <th>Status</th>
                        <th>Dibuat</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody class="small">
                    @forelse($pages as $page)
                        <tr>
                            <!-- Judul -->
                            <td class="ps-4">
                                <div class="fw-bold text-dark mb-0">{{ $page->title }}</div>
                                <small class="text-muted">{{ Str::limit($page->meta_title ?: $page->title, 40) }}</small>
                            </td>

                            <!-- Permalink -->
                            <td>
                                <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="font-monospace text-decoration-none text-primary" style="font-size: 0.78rem;">
                                    /halaman/{{ $page->slug }} <i class="bi bi-box-arrow-up-right ms-1" style="font-size: 0.65rem;"></i>
                                </a>
                            </td>

                            <!-- Metode Editor -->
                            <td>
                                @if($page->editor_type === 'builder')
                                    <span class="badge bg-primary bg-opacity-10 text-primary">
                                        <i class="bi bi-brush me-1"></i> Visual Canvas
                                    </span>
                                @else
                                    <span class="badge bg-secondary bg-opacity-10 text-dark">
                                        <i class="bi bi-file-earmark-richtext me-1"></i> Standar (WYSIWYG)
                                    </span>
                                @endif
                            </td>

                            <!-- Template -->
                            <td>
                                @if($page->template === 'full-width')
                                    <span class="badge bg-info bg-opacity-10 text-info">Full Width</span>
                                @elseif($page->template === 'blank')
                                    <span class="badge bg-dark bg-opacity-10 text-dark">Blank Canvas</span>
                                @else
                                    <span class="badge bg-light text-muted border">Default</span>
                                @endif
                            </td>

                            <!-- Urutan -->
                            <td class="text-muted">#{{ $page->sort_order }}</td>

                            <!-- Status -->
                            <td>
                                @if($page->is_published)
                                    <span class="badge bg-success bg-opacity-10 text-success">
                                        <i class="bi bi-check-circle-fill me-1"></i> Publik
                                    </span>
                                @else
                                    <span class="badge bg-warning bg-opacity-10 text-dark">
                                        <i class="bi bi-pencil-fill me-1"></i> Draf
                                    </span>
                                @endif
                            </td>

                            <!-- Tanggal -->
                            <td class="text-muted">
                                {{ $page->created_at?->format('d/m/Y') ?? '-' }}
                            </td>

                            <!-- Aksi -->
                            <td class="text-end pe-4">
                                <div class="d-flex justify-content-end align-items-center gap-1">
                                    @if($page->editor_type === 'builder')
                                        <a href="{{ route('admin.pages.builder', $page->id) }}" class="btn btn-sm btn-outline-primary rounded-pill px-3" title="Buka Visual Drag & Drop Canvas Builder">
                                            <i class="bi bi-palette-fill me-1"></i> Visual Builder
                                        </a>
                                    @endif

                                    <!-- Quick Edit Modal Trigger -->
                                    <button type="button" class="btn btn-sm btn-outline-warning text-dark rounded-pill px-2 btn-quick-edit-page" 
                                            title="Edit Cepat (Ganti judul, slug, status tanpa buka halaman edit)"
                                            data-id="{{ $page->id }}"
                                            data-title="{{ $page->title }}"
                                            data-slug="{{ $page->slug }}"
                                            data-template="{{ $page->template }}"
                                            data-order="{{ $page->sort_order }}"
                                            data-published="{{ $page->is_published ? '1' : '0' }}"
                                            data-url="{{ route('admin.pages.quickUpdate', $page->id) }}">
                                        <i class="bi bi-lightning-charge"></i>
                                    </button>

                                    <!-- 1-Click Duplicate -->
                                    <form action="{{ route('admin.pages.duplicate', $page->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Duplikasi halaman ini?');">
                                        @csrf
                                        <button type="submit" class="btn btn-sm btn-outline-info rounded-pill px-2" title="Duplikasi Halaman 1-Klik">
                                            <i class="bi bi-files"></i>
                                        </button>
                                    </form>

                                    <a href="{{ route('admin.pages.edit', $page->id) }}" class="btn btn-sm btn-outline-secondary rounded-pill px-3" title="Edit Rincian Lengkap">
                                        <i class="bi bi-pencil me-1"></i> Edit
                                    </a>

                                    @if($page->is_published)
                                        <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="btn btn-sm btn-light border rounded-pill px-2" title="Lihat Tampilan">
                                            <i class="bi bi-eye"></i>
                                        </a>
                                    @endif

                                    <form action="{{ route('admin.pages.destroy', $page->id) }}" method="POST" class="d-inline" onsubmit="return confirm('Yakin ingin menghapus halaman ini?');">
                                        @csrf
                                        @method('DELETE')
                                        <button type="submit" class="btn btn-sm btn-outline-danger rounded-pill px-2" title="Hapus Halaman">
                                            <i class="bi bi-trash"></i>
                                        </button>
                                    </form>
                                </div>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td colspan="8" class="text-center py-5 text-muted">
                                <i class="bi bi-file-earmark-plus display-6 d-block mb-2 text-secondary opacity-50"></i>
                                Belum ada halaman yang sesuai. Klik "Tambah Halaman Baru" untuk mulai membuat halaman.
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

    <!-- MODAL QUICK EDIT HALAMAN ALA WORDPRESS -->
    <div class="modal fade" id="modalQuickEditPage" tabindex="-1" aria-labelledby="modalQuickEditPageLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <form id="formQuickEditPage" method="POST">
                    @csrf
                    @method('PUT')
                    <div class="modal-header bg-dark text-white py-3 px-4">
                        <h6 class="modal-title fw-bold mb-0" id="modalQuickEditPageLabel">
                            <i class="bi bi-lightning-charge text-warning me-2"></i> Edit Cepat Halaman (Quick Edit)
                        </h6>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Tutup"></button>
                    </div>
                    <div class="modal-body p-4 bg-white">
                        <div class="mb-3">
                            <label class="form-label small fw-bold text-dark mb-1">Judul Halaman</label>
                            <input type="text" name="title" id="qe-page-title" class="form-control form-control-sm" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label small fw-bold text-dark mb-1">URL / Permalink Slug</label>
                            <input type="text" name="slug" id="qe-page-slug" class="form-control form-control-sm font-monospace" required>
                        </div>
                        <div class="row g-2 mb-3">
                            <div class="col-md-7">
                                <label class="form-label small fw-bold text-dark mb-1">Tata Letak (Template)</label>
                                <select name="template" id="qe-page-template" class="form-select form-select-sm">
                                    <option value="default">Default (Container)</option>
                                    <option value="full-width">Full Width (Canvas)</option>
                                    <option value="blank">Blank Canvas (Murni)</option>
                                </select>
                            </div>
                            <div class="col-md-5">
                                <label class="form-label small fw-bold text-dark mb-1">Urutan Menu</label>
                                <input type="number" name="sort_order" id="qe-page-order" class="form-control form-control-sm" value="0">
                            </div>
                        </div>
                        <div class="form-check form-switch p-0 ps-5 mt-3">
                            <input class="form-check-input ms-n5" type="checkbox" role="switch" name="is_published" id="qe-page-published" value="1" style="width: 2rem; height: 1.15rem;">
                            <label class="form-check-label fw-bold text-dark ms-2 small" for="qe-page-published">
                                Publikasikan Halaman
                            </label>
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
        const modalEl = document.getElementById('modalQuickEditPage');
        const formEl = document.getElementById('formQuickEditPage');
        const titleInput = document.getElementById('qe-page-title');
        const slugInput = document.getElementById('qe-page-slug');
        const templateInput = document.getElementById('qe-page-template');
        const orderInput = document.getElementById('qe-page-order');
        const publishedInput = document.getElementById('qe-page-published');

        document.addEventListener('click', function (e) {
            const btn = e.target.closest('.btn-quick-edit-page');
            if (btn) {
                e.preventDefault();
                formEl.action = btn.getAttribute('data-url');
                titleInput.value = btn.getAttribute('data-title') || '';
                slugInput.value = btn.getAttribute('data-slug') || '';
                templateInput.value = btn.getAttribute('data-template') || 'default';
                orderInput.value = btn.getAttribute('data-order') || 0;
                publishedInput.checked = btn.getAttribute('data-published') === '1';

                const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
                modal.show();
            }
        });
    });
</script>
@endpush
