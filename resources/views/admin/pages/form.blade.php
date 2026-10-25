@extends('layouts.admin')

@section('title', $page->exists ? 'Edit Halaman: ' . Str::limit($page->title, 40) : 'Tambah Halaman Baru (WordPress Style)')
@section('page_title', $page->exists ? 'Edit Halaman: ' . $page->title : 'Tambah Halaman Baru')

@push('styles')
<style>
    /* Styling Editor Halaman Ala WordPress */
    .wp-metabox {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        margin-bottom: 1.25rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        overflow: hidden;
    }
    .wp-metabox-header {
        background: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
        padding: 0.75rem 1rem;
        font-weight: 600;
        font-size: 0.875rem;
        color: #1e293b;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .wp-metabox-body {
        padding: 1rem;
    }
    .page-title-input {
        font-size: 1.6rem;
        font-weight: 700;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        color: #0f172a;
    }
    .page-title-input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
    }
    .permalink-bar {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.4rem 0.75rem;
        font-size: 0.8125rem;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    .editor-mode-card {
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        cursor: pointer;
        transition: all 0.2s;
        background: #ffffff;
    }
    .editor-mode-card:hover {
        border-color: #6366f1;
        background: #f8fafc;
    }
    .editor-mode-card.active {
        border-color: #6366f1;
        background: rgba(99, 102, 241, 0.05);
    }
    /* Google SERP Preview */
    .google-preview-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        font-family: Arial, sans-serif;
    }
    .google-url {
        color: #202124;
        font-size: 0.8125rem;
        line-height: 1.3;
        margin-bottom: 0.15rem;
        word-break: break-all;
    }
    .google-title {
        color: #1a0dab;
        font-size: 1.15rem;
        line-height: 1.3;
        font-weight: 400;
        cursor: pointer;
        margin-bottom: 0.25rem;
    }
    .google-title:hover {
        text-decoration: underline;
    }
    .google-desc {
        color: #4d5156;
        font-size: 0.875rem;
        line-height: 1.4;
    }
    .featured-dropzone {
        border: 2px dashed #cbd5e1;
        border-radius: 8px;
        padding: 1.5rem 1rem;
        text-align: center;
        background: #f8fafc;
        cursor: pointer;
        transition: all 0.2s;
    }
    .featured-dropzone:hover {
        border-color: #6366f1;
        background: #f1f5f9;
    }
</style>
@endpush

@section('content')

    <form id="page-form" action="{{ $page->exists ? route('admin.pages.update', $page->id) : route('admin.pages.store') }}" method="POST" enctype="multipart/form-data">
        @csrf
        @if($page->exists)
            @method('PUT')
        @endif

        <div class="row g-4">
            <!-- ========================================== -->
            <!-- KOLOM KIRI (KONTEN UTAMA & BUILDER) -->
            <!-- ========================================== -->
            <div class="col-lg-8 col-xl-9">

                <!-- 1. JUDUL HALAMAN -->
                <div class="mb-3">
                    <input type="text" name="title" id="page-title" class="form-control page-title-input" placeholder="Tambahkan judul halaman (contoh: Profil Perusahaan, Kebijakan Privasi, Tim Kami)..." required value="{{ old('title', $page->title) }}" autofocus>
                </div>

                <!-- 2. PERMALINK SLUG -->
                <div class="permalink-bar mb-3">
                    <span class="text-muted"><i class="bi bi-link-45deg me-1"></i><strong>Permalink:</strong> {{ url('/halaman') }}/</span>
                    <span id="slug-display" class="fw-semibold text-primary font-monospace">{{ old('slug', $page->slug ?: 'nama-halaman') }}</span>
                    <button type="button" id="btn-edit-slug" class="btn btn-xs btn-outline-secondary py-0 px-2 rounded" style="font-size: 0.75rem;">Edit</button>
                    
                    <div id="slug-edit-box" class="d-none d-flex align-items-center gap-1 mt-1 w-100">
                        <input type="text" name="slug" id="slug-input" class="form-control form-control-sm font-monospace" value="{{ old('slug', $page->slug) }}" style="max-width: 320px;">
                        <button type="button" id="btn-save-slug" class="btn btn-sm btn-primary py-0 px-2">OK</button>
                        <button type="button" id="btn-cancel-slug" class="btn btn-sm btn-light border py-0 px-2">Batal</button>
                    </div>

                    @if($page->exists && $page->is_published)
                        <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="btn btn-xs btn-light border ms-auto py-0 px-2 rounded" style="font-size: 0.75rem;">
                            <i class="bi bi-box-arrow-up-right me-1"></i> Buka Halaman Publik
                        </a>
                    @endif
                </div>

                <!-- 3. PILIHAN MODE EDITOR (WP DUAL MODE: WYSIWYG vs VISUAL BUILDER) -->
                <div class="card border rounded-3 p-3 bg-light mb-3">
                    <label class="form-label small fw-bold text-dark mb-2">
                        <i class="bi bi-sliders text-primary me-1"></i> Pilih Metode Pembuatan Halaman:
                    </label>
                    <div class="row g-2">
                        <div class="col-md-6">
                            <label class="editor-mode-card d-block {{ old('editor_type', $page->editor_type ?? 'standard') === 'standard' ? 'active' : '' }}" id="label-mode-standard">
                                <div class="form-check m-0">
                                    <input class="form-check-input" type="radio" name="editor_type" id="mode-standard" value="standard" {{ old('editor_type', $page->editor_type ?? 'standard') === 'standard' ? 'checked' : '' }}>
                                    <span class="form-check-label fw-bold text-dark ms-1">
                                        📝 Editor Standar (WYSIWYG Teks & Media)
                                    </span>
                                </div>
                                <small class="text-muted d-block mt-1 ps-4" style="font-size: 0.75rem;">
                                    Mirip WordPress Classic Editor. Mudah diformat teks, gambar, tabel, dan tautan. Sangat pas untuk dokumen, visi misi, & regulasi.
                                </small>
                            </label>
                        </div>
                        <div class="col-md-6">
                            <label class="editor-mode-card d-block {{ old('editor_type', $page->editor_type) === 'builder' ? 'active' : '' }}" id="label-mode-builder">
                                <div class="form-check m-0">
                                    <input class="form-check-input" type="radio" name="editor_type" id="mode-builder" value="builder" {{ old('editor_type', $page->editor_type) === 'builder' ? 'checked' : '' }}>
                                    <span class="form-check-label fw-bold text-primary ms-1">
                                        🎨 Visual Drag & Drop Canvas (Elementor Style)
                                    </span>
                                </div>
                                <small class="text-muted d-block mt-1 ps-4" style="font-size: 0.75rem;">
                                    GrapesJS Visual Canvas. Rancang tata letak bebas seperti banner hero, kolom fitur, grid harga, dan tombol CTA interaktif.
                                </small>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- 4A. EDITOR STANDAR WYSIWYG (TINYMCE 6 ALA WP) -->
                <div id="standard-editor-wrapper" class="{{ old('editor_type', $page->editor_type ?? 'standard') === 'builder' ? 'd-none' : '' }}">
                    <!-- Action Bar "Tambah Media" -->
                    <div class="d-flex justify-content-between align-items-center bg-white p-2 border border-bottom-0 rounded-top-3">
                        <div class="d-flex align-items-center gap-2">
                            <button type="button" class="btn btn-sm btn-primary rounded-pill px-3 shadow-xs" onclick="openMediaLibraryModal('page-content-html')">
                                <i class="bi bi-images me-1"></i> Pustaka Media
                            </button>
                            <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 shadow-xs" id="btn-add-media-page">
                                <i class="bi bi-cloud-arrow-up me-1"></i> Unggah Cepat
                            </button>
                            <input type="file" id="media-file-input-page" accept="image/*" class="d-none">
                            <span id="media-spinner-page" class="spinner-border spinner-border-sm text-primary d-none" role="status"></span>
                            <span id="media-msg-page" class="small text-muted"></span>
                        </div>
                        <span class="badge bg-light text-muted border py-1 px-2">
                            <i class="bi bi-file-earmark-richtext me-1"></i> Editor Konten Halaman
                        </span>
                    </div>

                    <div class="mb-4">
                        <textarea name="content_html" id="page-content-html" class="form-control" rows="18" placeholder="Tuliskan isi halaman lengkap di sini...">{{ old('content_html', $page->content_html) }}</textarea>
                    </div>
                </div>

                <!-- 4B. BUILDER CANVAS PROMPT (JIKA MODE BUILDER AKTIF) -->
                <div id="builder-editor-wrapper" class="{{ old('editor_type', $page->editor_type) === 'builder' ? '' : 'd-none' }} mb-4">
                    <div class="card border-primary border-opacity-50 rounded-4 p-4 text-center bg-primary bg-opacity-10">
                        <div class="p-3 bg-white text-primary rounded-circle d-inline-flex mx-auto mb-3 shadow-sm fs-2">
                            <i class="bi bi-palette-fill"></i>
                        </div>
                        <h5 class="fw-bold text-dark mb-2">Halaman Dirancang dengan Visual Canvas Builder</h5>
                        <p class="text-muted small mx-auto mb-4" style="max-width: 580px;">
                            Anda dapat menyusun komponen seperti Hero Banner, 3 Kolom Fitur, Tabel Harga, dan Call to Action cukup dengan drag and drop di kanvas visual.
                        </p>
                        @if($page->exists)
                            <div>
                                <a href="{{ route('admin.pages.builder', $page->id) }}" class="btn btn-primary rounded-pill px-5 py-2 shadow-sm fw-bold">
                                    <i class="bi bi-brush me-2"></i> Buka Visual Drag & Drop Canvas Builder
                                </a>
                            </div>
                        @else
                            <div class="text-muted small">
                                <em>Simpan halaman terlebih dahulu, lalu sistem akan langsung mengarahkan Anda ke Kanvas Desain Visual.</em>
                            </div>
                        @endif
                    </div>
                </div>

                <!-- 5. METABOX SEO SEARCH ENGINE -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-google text-primary me-2"></i> Pengaturan SEO & Cuplikan Google (SERP Preview)</span>
                        <span class="badge bg-success bg-opacity-10 text-success">SEO Ready</span>
                    </div>
                    <div class="wp-metabox-body">
                        <!-- SERP Simulator Card -->
                        <div class="google-preview-card mb-3">
                            <div class="google-url">
                                {{ url('/halaman') }}/<span id="serp-slug-preview">{{ $page->slug ?: 'nama-halaman' }}</span>
                            </div>
                            <div class="google-title" id="serp-title-preview">
                                {{ $page->meta_title ?: ($page->title ?: 'Judul Halaman | PT Aktama Digital Antika') }}
                            </div>
                            <div class="google-desc" id="serp-desc-preview">
                                {{ $page->meta_description ?: 'Kunjungi halaman resmi PT Aktama Digital Antika untuk melihat informasi layanan dan detail penawaran lengkap...' }}
                            </div>
                        </div>

                        <!-- SEO Inputs -->
                        <div class="row g-3">
                            <div class="col-12">
                                <div class="d-flex justify-content-between">
                                    <label class="form-label small fw-bold text-dark mb-1">Judul SEO (Meta Title)</label>
                                    <small class="text-muted"><span id="meta-title-length">0</span> / 60 karakter</small>
                                </div>
                                <input type="text" name="meta_title" id="meta-title" class="form-control form-control-sm" placeholder="Biarkan kosong untuk otomatis memakai judul halaman" value="{{ old('meta_title', $page->meta_title) }}">
                                <div class="progress mt-1" style="height: 4px;">
                                    <div class="progress-bar bg-success" id="title-progress" role="progressbar" style="width: 0%"></div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="d-flex justify-content-between">
                                    <label class="form-label small fw-bold text-dark mb-1">Deskripsi Meta (Meta Description)</label>
                                    <small class="text-muted"><span id="meta-desc-length">0</span> / 160 karakter</small>
                                </div>
                                <textarea name="meta_description" id="meta-description" class="form-control form-control-sm" rows="2" placeholder="Deskripsi ringkas yang muncul saat halaman terindeks di mesin pencari...">{{ old('meta_description', $page->meta_description) }}</textarea>
                                <div class="progress mt-1" style="height: 4px;">
                                    <div class="progress-bar bg-success" id="desc-progress" role="progressbar" style="width: 0%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- ========================================== -->
            <!-- KOLOM KANAN (METABOX PUBLIKASI & ATRIBUT) -->
            <!-- ========================================== -->
            <div class="col-lg-4 col-xl-3">

                <!-- METABOX 1: PUBLIKASIKAN (PUBLISH BOX) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-send-check text-primary me-2"></i> Publikasikan</span>
                        @if($page->exists)
                            <span class="badge {{ $page->is_published ? 'bg-success' : 'bg-warning text-dark' }}">
                                {{ $page->is_published ? 'Publik' : 'Draf' }}
                            </span>
                        @endif
                    </div>
                    <div class="wp-metabox-body small">
                        <!-- Switch Status -->
                        <div class="form-check form-switch mb-3 p-0 ps-5 d-flex align-items-center">
                            <input class="form-check-input ms-n5 mt-0" type="checkbox" role="switch" id="is_published" name="is_published" value="1" {{ old('is_published', $page->exists ? $page->is_published : true) ? 'checked' : '' }} style="width: 2.25rem; height: 1.25rem;">
                            <label class="form-check-label fw-bold text-dark ms-2" for="is_published">
                                Publikasikan ke Publik
                            </label>
                        </div>
                        <p class="text-muted" style="font-size: 0.75rem;">
                            Jika dinonaktifkan, halaman disimpan sebagai draf dan hanya bisa dilihat oleh administrator.
                        </p>

                        <hr class="my-3">

                        <!-- Action Buttons -->
                        <div class="d-flex justify-content-between align-items-center">
                            @if($page->exists)
                                <button type="button" class="btn btn-link text-danger p-0 text-decoration-none small" onclick="if(confirm('Yakin ingin menghapus halaman ini?')) document.getElementById('delete-page-form').submit();">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            @else
                                <a href="{{ route('admin.pages.index') }}" class="btn btn-sm btn-light border">Batal</a>
                            @endif

                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-bold shadow-sm">
                                <i class="bi bi-check2-circle me-1"></i> {{ $page->exists ? 'Perbarui' : 'Simpan Halaman' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- METABOX 2: ATRIBUT HALAMAN (PAGE ATTRIBUTES / TEMPLATE) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-layout-text-window-reverse text-info me-2"></i> Atribut Halaman</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <!-- Pilihan Template -->
                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Tata Letak (Template):</label>
                            <select name="template" class="form-select form-select-sm">
                                <option value="default" {{ old('template', $page->template ?? 'default') === 'default' ? 'selected' : '' }}>
                                    Default (Container Standar)
                                </option>
                                <option value="full-width" {{ old('template', $page->template) === 'full-width' ? 'selected' : '' }}>
                                    Full Width (Layar Penuh / Canvas)
                                </option>
                                <option value="blank" {{ old('template', $page->template) === 'blank' ? 'selected' : '' }}>
                                    Blank Canvas (Tanpa Banner Header)
                                </option>
                            </select>
                            <small class="text-muted d-block mt-1" style="font-size: 0.7rem;">Pilih Full Width jika ingin elemen konten membentang lebar penuh layar.</small>
                        </div>

                        <!-- Urutan (Order) -->
                        <div class="mb-2">
                            <label class="text-dark fw-bold d-block mb-1">Urutan Menu (Order):</label>
                            <input type="number" name="sort_order" class="form-control form-control-sm" value="{{ old('sort_order', $page->sort_order ?? 0) }}" style="max-width: 100px;">
                            <small class="text-muted d-block mt-1" style="font-size: 0.7rem;">Angka lebih kecil tampil lebih dulu.</small>
                        </div>
                    </div>
                </div>

                <!-- METABOX 3: GAMBAR UNGGULAN HALAMAN (FEATURED IMAGE) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-image text-success me-2"></i> Gambar Unggulan Halaman</span>
                    </div>
                    <div class="wp-metabox-body small text-center">
                        <div id="featured-image-preview-container" class="{{ $page->featured_image ? '' : 'd-none' }} mb-2">
                            <img id="featured-image-preview" src="{{ $page->featured_image ? asset('images/' . $page->featured_image) : '' }}" alt="Featured Image" class="img-fluid rounded-3 shadow-xs mb-2 w-100 object-fit-cover" style="max-height: 160px;">
                            <div class="d-flex justify-content-center gap-2">
                                <button type="button" class="btn btn-xs btn-outline-secondary py-1 px-2" onclick="document.getElementById('featured-image-file').click();">
                                    <i class="bi bi-arrow-repeat"></i> Ganti Gambar
                                </button>
                                <button type="button" class="btn btn-xs btn-outline-danger py-1 px-2" id="btn-remove-featured">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            </div>
                        </div>

                        <div id="featured-image-dropzone" class="featured-dropzone {{ $page->featured_image ? 'd-none' : '' }}" onclick="document.getElementById('featured-image-file').click();">
                            <i class="bi bi-cloud-arrow-up display-6 text-muted d-block mb-1"></i>
                            <strong class="text-primary d-block">Tetapkan Gambar Halaman</strong>
                            <small class="text-muted">Untuk thumbnail kartu & share WhatsApp</small>
                        </div>

                        <input type="file" name="featured_image_file" id="featured-image-file" class="d-none" accept="image/png,image/jpeg,image/webp">
                        <input type="hidden" name="remove_featured_image" id="remove-featured-image-input" value="0">
                        <small class="text-muted d-block mt-2" style="font-size: 0.7rem;">Maksimal 5 MB (JPG, PNG, WEBP).</small>
                    </div>
                </div>

            </div>
        </div>
    </form>

    @if($page->exists)
        <form id="delete-page-form" action="{{ route('admin.pages.destroy', $page->id) }}" method="POST" class="d-none">
            @csrf
            @method('DELETE')
        </form>
    @endif

    @include('admin.partials.media-modal')

@endsection

@push('scripts')
<!-- TinyMCE 6 Core via CDNJS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.8.3/tinymce.min.js"></script>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('page-title');
        const slugDisplay = document.getElementById('slug-display');
        const slugInput = document.getElementById('slug-input');
        const slugEditBox = document.getElementById('slug-edit-box');
        const btnEditSlug = document.getElementById('btn-edit-slug');
        const btnSaveSlug = document.getElementById('btn-save-slug');
        const btnCancelSlug = document.getElementById('btn-cancel-slug');

        function slugify(text) {
            return text.toString().toLowerCase().trim()
                .replace(/[^\w\s-]/g, '')
                .replace(/[\s_-]+/g, '-')
                .replace(/^-+|-+$/g, '');
        }

        let isSlugManuallyEdited = {{ $page->exists ? 'true' : 'false' }};

        if (titleInput) {
            titleInput.addEventListener('input', function () {
                if (!isSlugManuallyEdited) {
                    const generated = slugify(this.value);
                    slugDisplay.innerText = generated || 'nama-halaman';
                    slugInput.value = generated;
                    updateSerpPreview();
                }
            });
        }

        if (btnEditSlug) {
            btnEditSlug.addEventListener('click', function () {
                slugEditBox.classList.remove('d-none');
                btnEditSlug.classList.add('d-none');
                slugInput.focus();
            });
        }

        if (btnSaveSlug) {
            btnSaveSlug.addEventListener('click', function () {
                const clean = slugify(slugInput.value);
                slugInput.value = clean;
                slugDisplay.innerText = clean || 'nama-halaman';
                slugEditBox.classList.add('d-none');
                btnEditSlug.classList.remove('d-none');
                isSlugManuallyEdited = true;
                updateSerpPreview();
            });
        }

        if (btnCancelSlug) {
            btnCancelSlug.addEventListener('click', function () {
                slugEditBox.classList.add('d-none');
                btnEditSlug.classList.remove('d-none');
            });
        }

        // TOGGLE MODE EDITOR (STANDARD vs BUILDER)
        const modeStandard = document.getElementById('mode-standard');
        const modeBuilder = document.getElementById('mode-builder');
        const standardWrapper = document.getElementById('standard-editor-wrapper');
        const builderWrapper = document.getElementById('builder-editor-wrapper');
        const labelModeStandard = document.getElementById('label-mode-standard');
        const labelModeBuilder = document.getElementById('label-mode-builder');

        function toggleEditorMode() {
            if (modeBuilder.checked) {
                standardWrapper.classList.add('d-none');
                builderWrapper.classList.remove('d-none');
                labelModeBuilder.classList.add('active');
                labelModeStandard.classList.remove('active');
            } else {
                standardWrapper.classList.remove('d-none');
                builderWrapper.classList.add('d-none');
                labelModeStandard.classList.add('active');
                labelModeBuilder.classList.remove('active');
            }
        }

        if (modeStandard && modeBuilder) {
            modeStandard.addEventListener('change', toggleEditorMode);
            modeBuilder.addEventListener('change', toggleEditorMode);
        }

        // INISIALISASI TINYMCE UNTUK HALAMAN
        let isTinyActive = false;
        try {
            tinymce.init({
                selector: '#page-content-html',
                height: 520,
                menubar: 'file edit view insert format tools table',
                plugins: [
                    'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
                    'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                    'insertdatetime', 'media', 'table', 'help', 'wordcount'
                ],
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | ' +
                         'forecolor backcolor | alignleft aligncenter alignright alignjustify | ' +
                         'bullist numlist outdent indent | link image media table blockquote code | ' +
                         'removeformat fullscreen preview',
                content_style: 'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 15px; line-height: 1.7; color: #1e293b; } img { max-width: 100%; height: auto; border-radius: 8px; }',
                images_upload_url: '{{ route('admin.media.upload') }}',
                images_upload_handler: function (blobInfo, progress) {
                    return new Promise((resolve, reject) => {
                        const xhr = new XMLHttpRequest();
                        xhr.open('POST', '{{ route('admin.media.upload') }}');
                        xhr.setRequestHeader('X-CSRF-TOKEN', '{{ csrf_token() }}');

                        xhr.upload.onprogress = (e) => {
                            progress(e.loaded / e.total * 100);
                        };

                        xhr.onload = () => {
                            if (xhr.status < 200 || xhr.status >= 300) {
                                reject('Gagal mengunggah gambar: ' + xhr.status);
                                return;
                            }
                            const json = JSON.parse(xhr.responseText);
                            resolve(json.location || json.url);
                        };

                        xhr.onerror = () => reject('Koneksi terputus saat mengunggah.');
                        const formData = new FormData();
                        formData.append('file', blobInfo.blob(), blobInfo.filename());
                        xhr.send(formData);
                    });
                },
                setup: function (editor) {
                    isTinyActive = true;
                    editor.on('input change keyup', function () {
                        editor.save();
                    });
                }
            });
        } catch (e) {
            console.warn('TinyMCE CDN fallback:', e);
        }

        // TOMBOL "TAMBAH MEDIA" UNTUK HALAMAN
        const btnAddMediaPage = document.getElementById('btn-add-media-page');
        const mediaFileInputPage = document.getElementById('media-file-input-page');
        const mediaSpinnerPage = document.getElementById('media-spinner-page');
        const mediaMsgPage = document.getElementById('media-msg-page');

        if (btnAddMediaPage && mediaFileInputPage) {
            btnAddMediaPage.addEventListener('click', function () {
                mediaFileInputPage.click();
            });

            mediaFileInputPage.addEventListener('change', function () {
                const file = this.files[0];
                if (!file) return;

                mediaSpinnerPage.classList.remove('d-none');
                mediaMsgPage.innerText = 'Mengunggah ' + file.name + '...';

                const formData = new FormData();
                formData.append('file', file);

                fetch('{{ route('admin.media.upload') }}', {
                    method: 'POST',
                    headers: { 'X-CSRF-TOKEN': '{{ csrf_token() }}' },
                    body: formData
                })
                .then(res => res.json())
                .then(data => {
                    mediaSpinnerPage.classList.add('d-none');
                    if (data.location || data.url) {
                        const imgUrl = data.location || data.url;
                        const imgTag = `<p><img src="${imgUrl}" alt="${file.name}" class="img-fluid rounded-3 my-3" /></p>`;
                        if (isTinyActive && tinymce.get('page-content-html')) {
                            tinymce.get('page-content-html').insertContent(imgTag);
                        } else {
                            document.getElementById('page-content-html').value += '\n' + imgTag + '\n';
                        }
                        mediaMsgPage.innerText = '✅ Disisipkan ke halaman!';
                        setTimeout(() => mediaMsgPage.innerText = '', 3000);
                    }
                    mediaFileInputPage.value = '';
                })
                .catch(() => {
                    mediaSpinnerPage.classList.add('d-none');
                    mediaMsgPage.innerText = '❌ Gagal.';
                    mediaFileInputPage.value = '';
                });
            });
        }

        // FEATURED IMAGE PREVIEW & REMOVE
        const featuredInput = document.getElementById('featured-image-file');
        const featuredPreview = document.getElementById('featured-image-preview');
        const featuredPreviewContainer = document.getElementById('featured-image-preview-container');
        const featuredDropzone = document.getElementById('featured-image-dropzone');
        const btnRemoveFeatured = document.getElementById('btn-remove-featured');
        const removeFeaturedImageInput = document.getElementById('remove-featured-image-input');

        if (featuredInput) {
            featuredInput.addEventListener('change', function () {
                const file = this.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        featuredPreview.src = e.target.result;
                        featuredPreviewContainer.classList.remove('d-none');
                        featuredDropzone.classList.add('d-none');
                        removeFeaturedImageInput.value = '0';
                    };
                    reader.readAsDataURL(file);
                }
            });
        }

        if (btnRemoveFeatured) {
            btnRemoveFeatured.addEventListener('click', function () {
                featuredInput.value = '';
                featuredPreview.src = '';
                featuredPreviewContainer.classList.add('d-none');
                featuredDropzone.classList.remove('d-none');
                removeFeaturedImageInput.value = '1';
            });
        }

        // SEO SERP PREVIEW REALTIME
        const metaTitleInput = document.getElementById('meta-title');
        const metaDescInput = document.getElementById('meta-description');
        const serpTitlePreview = document.getElementById('serp-title-preview');
        const serpDescPreview = document.getElementById('serp-desc-preview');
        const serpSlugPreview = document.getElementById('serp-slug-preview');
        const metaTitleLength = document.getElementById('meta-title-length');
        const metaDescLength = document.getElementById('meta-desc-length');
        const titleProgress = document.getElementById('title-progress');
        const descProgress = document.getElementById('desc-progress');

        function updateSerpPreview() {
            const currentTitle = metaTitleInput.value.trim() || titleInput.value.trim() || 'Judul Halaman';
            const currentDesc = metaDescInput.value.trim() || 'Kunjungi halaman resmi PT Aktama Digital Antika untuk melihat informasi layanan dan detail penawaran lengkap...';
            const currentSlug = slugInput.value.trim() || slugify(titleInput.value) || 'nama-halaman';

            serpTitlePreview.innerText = currentTitle + ' | PT Aktama Digital Antika';
            serpDescPreview.innerText = currentDesc;
            serpSlugPreview.innerText = currentSlug;

            const tLen = metaTitleInput.value.length;
            metaTitleLength.innerText = tLen;
            const tPercent = Math.min(100, Math.round((tLen / 60) * 100));
            titleProgress.style.width = tPercent + '%';
            titleProgress.className = 'progress-bar ' + (tLen > 60 ? 'bg-danger' : (tLen >= 40 ? 'bg-success' : 'bg-warning'));

            const dLen = metaDescInput.value.length;
            metaDescLength.innerText = dLen;
            const dPercent = Math.min(100, Math.round((dLen / 160) * 100));
            descProgress.style.width = dPercent + '%';
            descProgress.className = 'progress-bar ' + (dLen > 160 ? 'bg-danger' : (dLen >= 100 ? 'bg-success' : 'bg-warning'));
        }

        if (metaTitleInput) metaTitleInput.addEventListener('input', updateSerpPreview);
        if (metaDescInput) metaDescInput.addEventListener('input', updateSerpPreview);

        updateSerpPreview();
    });
</script>
@endpush
