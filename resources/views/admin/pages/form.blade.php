@extends('layouts.admin')

@section('title', $page->exists ? 'Edit Halaman' : 'Tambah Halaman Baru')
@section('page_title', $page->exists ? 'Edit Halaman: ' . $page->title : 'Tambah Halaman Baru')

@section('content')

    <div class="row justify-content-center">
        <div class="col-lg-9">
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <form action="{{ $page->exists ? route('admin.pages.update', $page->id) : route('admin.pages.store') }}" method="POST">
                    @csrf
                    @if($page->exists)
                        @method('PUT')
                    @endif

                    <div class="row g-3 mb-3">
                        <div class="col-md-8">
                            <label class="form-label small fw-bold text-dark">Judul Halaman *</label>
                            <input type="text" name="title" id="page-title" class="form-control" required value="{{ old('title', $page->title) }}" placeholder="Contoh: Tentang Aktama, Program Magang, dsb.">
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small fw-bold text-dark">Tipe Editor Konten *</label>
                            <select name="editor_type" id="editor-type" class="form-select" required>
                                <option value="builder" {{ old('editor_type', $page->editor_type ?? 'builder') === 'builder' ? 'selected' : '' }}>
                                    🎨 Visual Drag & Drop Canvas (Opsi B)
                                </option>
                                <option value="standard" {{ old('editor_type', $page->editor_type) === 'standard' ? 'selected' : '' }}>
                                    📝 Editor Teks Standar (HTML/WYSIWYG)
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Slug / URL Permalink</label>
                        <div class="input-group">
                            <span class="input-group-text bg-light text-muted small">/halaman/</span>
                            <input type="text" name="slug" id="page-slug" class="form-control font-monospace" value="{{ old('slug', $page->slug) }}" placeholder="otomatis-dari-judul">
                        </div>
                        <small class="text-muted" style="font-size: 0.75rem;">Biarkan kosong saat membuat baru untuk menghasilkan otomatis dari judul.</small>
                    </div>

                    <!-- KONTEN HTML (Hanya tampil jika editor standar dipilih) -->
                    <div id="standard-content-group" class="mb-3 {{ old('editor_type', $page->editor_type ?? 'builder') === 'builder' ? 'd-none' : '' }}">
                        <label class="form-label small fw-bold text-dark">Isi Konten Halaman (HTML) *</label>
                        <textarea name="content_html" class="form-control font-monospace" rows="12" placeholder="Tuliskan konten atau kode HTML halaman di sini...">{{ old('content_html', $page->content_html) }}</textarea>
                    </div>

                    @if($page->exists && $page->editor_type === 'builder')
                        <div class="alert alert-info rounded-3 p-3 mb-4 d-flex align-items-center justify-content-between">
                            <div class="d-flex align-items-center gap-2">
                                <i class="bi bi-brush fs-4 text-primary"></i>
                                <div>
                                    <strong class="d-block text-dark">Halaman ini menggunakan Visual Drag & Drop Canvas</strong>
                                    <small class="text-muted">Desain tata letak komponen dilakukan secara visual di kanvas builder.</small>
                                </div>
                            </div>
                            <a href="{{ route('admin.pages.builder', $page->id) }}" class="btn btn-primary rounded-pill btn-sm px-3">
                                <i class="bi bi-palette-fill me-1"></i> Buka Visual Canvas Builder
                            </a>
                        </div>
                    @endif

                    <!-- OPTIMASI SEO -->
                    <div class="border rounded-3 p-3 bg-light mb-4">
                        <h6 class="fw-bold text-dark small mb-3"><i class="bi bi-search text-primary me-2"></i> Pengaturan SEO (Google Search)</h6>
                        <div class="row g-3">
                            <div class="col-12">
                                <label class="form-label small text-muted">Meta Title Khusus</label>
                                <input type="text" name="meta_title" class="form-control" value="{{ old('meta_title', $page->meta_title) }}" placeholder="Judul khusus untuk hasil pencarian Google...">
                            </div>
                            <div class="col-12">
                                <label class="form-label small text-muted">Meta Description</label>
                                <textarea name="meta_description" class="form-control" rows="2" placeholder="Deskripsi ringkas halaman di Google...">{{ old('meta_description', $page->meta_description) }}</textarea>
                            </div>
                        </div>
                    </div>

                    <!-- STATUS PUBLISH -->
                    <div class="form-check form-switch mb-4 p-3 bg-light rounded-3 d-flex align-items-center gap-3">
                        <input class="form-check-input ms-0 mt-0" type="checkbox" role="switch" id="is_published" name="is_published" value="1" {{ old('is_published', $page->exists ? $page->is_published : true) ? 'checked' : '' }} style="width: 2.5rem; height: 1.25rem;">
                        <label class="form-check-label fw-bold text-dark small mb-0" for="is_published">
                            Publikasikan Halaman ini ke Publik
                            <span class="d-block text-muted fw-normal" style="font-size: 0.75rem;">Jika dinonaktifkan, halaman hanya tersimpan sebagai draf dan tidak dapat diakses umum.</span>
                        </label>
                    </div>

                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-brand rounded-pill px-4">
                            <i class="bi bi-check-circle me-1"></i> {{ $page->exists ? 'Perbarui Halaman' : 'Simpan Halaman & Lanjutkan' }}
                        </button>
                        <a href="{{ route('admin.pages.index') }}" class="btn btn-light border rounded-pill px-3">Batal</a>
                    </div>
                </form>
            </div>
        </div>
    </div>

@endsection

@push('scripts')
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('page-title');
        const slugInput = document.getElementById('page-slug');
        const editorSelect = document.getElementById('editor-type');
        const standardGroup = document.getElementById('standard-content-group');

        // Toggle standard content group
        if (editorSelect && standardGroup) {
            editorSelect.addEventListener('change', function () {
                if (this.value === 'standard') {
                    standardGroup.classList.remove('d-none');
                } else {
                    standardGroup.classList.add('d-none');
                }
            });
        }

        // Auto slug on create if slug empty
        @if(!$page->exists)
        if (titleInput && slugInput) {
            titleInput.addEventListener('keyup', function () {
                if (!slugInput.dataset.manual) {
                    slugInput.value = this.value
                        .toLowerCase()
                        .trim()
                        .replace(/[^\w\s-]/g, '')
                        .replace(/[\s_-]+/g, '-')
                        .replace(/^-+|-+$/g, '');
                }
            });
            slugInput.addEventListener('input', function () {
                slugInput.dataset.manual = 'true';
            });
        }
        @endif
    });
</script>
@endpush
