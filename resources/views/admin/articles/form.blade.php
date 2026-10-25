@extends('layouts.admin')

@section('title', $article->exists ? 'Edit Postingan: ' . Str::limit($article->title, 40) : 'Tambah Postingan Baru (WordPress Style)')
@section('page_title', $article->exists ? 'Edit Postingan' : 'Tambah Postingan / Berita Baru')

@push('styles')
<style>
    /* Styling Editor Ala WordPress */
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
    .post-title-input {
        font-size: 1.6rem;
        font-weight: 700;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        color: #0f172a;
    }
    .post-title-input:focus {
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
    .category-checklist {
        max-height: 180px;
        overflow-y: auto;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        background: #fafafa;
    }
    .tag-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        background: #e0e7ff;
        color: #3730a3;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.2rem 0.5rem;
        border-radius: 9999px;
        margin: 0.2rem;
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
    .google-url span {
        color: #5f6368;
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

    <form id="post-form" action="{{ $article->exists ? route('admin.articles.update', $article->id) : route('admin.articles.store') }}" method="POST" enctype="multipart/form-data">
        @csrf
        @if($article->exists)
            @method('PUT')
        @endif

        <div class="row g-4">
            <!-- ========================================== -->
            <!-- KOLOM KIRI (KONTEN UTAMA & SEO) -->
            <!-- ========================================== -->
            <div class="col-lg-8 col-xl-9">

                <!-- 1. JUDUL POSTINGAN -->
                <div class="mb-3">
                    <input type="text" name="title" id="post-title" class="form-control post-title-input" placeholder="Tambahkan judul postingan atau berita di sini..." required value="{{ old('title', $article->title) }}" autofocus>
                </div>

                <!-- 2. PERMALINK SLUG (WP STYLE) -->
                <div class="permalink-bar mb-3">
                    <span class="text-muted"><i class="bi bi-link-45deg me-1"></i><strong>Permalink:</strong> {{ url('/artikel') }}/</span>
                    <span id="slug-display" class="fw-semibold text-primary font-monospace">{{ old('slug', $article->slug ?: 'judul-postingan') }}</span>
                    <button type="button" id="btn-edit-slug" class="btn btn-xs btn-outline-secondary py-0 px-2 rounded" style="font-size: 0.75rem;">Edit</button>
                    
                    <div id="slug-edit-box" class="d-none d-flex align-items-center gap-1 mt-1 w-100">
                        <input type="text" name="slug" id="slug-input" class="form-control form-control-sm font-monospace" value="{{ old('slug', $article->slug) }}" style="max-width: 320px;">
                        <button type="button" id="btn-save-slug" class="btn btn-sm btn-primary py-0 px-2">OK</button>
                        <button type="button" id="btn-cancel-slug" class="btn btn-sm btn-light border py-0 px-2">Batal</button>
                    </div>

                    @if($article->exists && $article->status === 'published')
                        <a href="{{ route('articles.show', $article->slug) }}" target="_blank" class="btn btn-xs btn-light border ms-auto py-0 px-2 rounded" style="font-size: 0.75rem;">
                            <i class="bi bi-box-arrow-up-right me-1"></i> Lihat Postingan
                        </a>
                    @endif
                </div>

                <!-- 3. ACTION BAR EDITOR (ADD MEDIA & WORD COUNT) -->
                <div class="d-flex justify-content-between align-items-center bg-white p-2 border border-bottom-0 rounded-top-3">
                    <div class="d-flex align-items-center gap-2">
                        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 shadow-xs" id="btn-add-media">
                            <i class="bi bi-camera me-1"></i> Tambah Media (Upload Gambar ke Konten)
                        </button>
                        <input type="file" id="media-file-input" accept="image/*" class="d-none">
                        <span id="media-uploading-spinner" class="spinner-border spinner-border-sm text-primary d-none" role="status"></span>
                        <span id="media-upload-msg" class="small text-muted"></span>
                    </div>

                    <div class="d-flex align-items-center gap-2">
                        <span class="badge bg-light text-muted border py-1 px-2" id="stats-counter">
                            <i class="bi bi-file-text me-1"></i> <span id="word-count">0</span> kata &bull; ~<span id="read-time">1</span> mnt baca
                        </span>
                        <div class="btn-group btn-group-sm" role="group">
                            <button type="button" class="btn btn-outline-secondary active" id="btn-mode-visual">Visual</button>
                            <button type="button" class="btn btn-outline-secondary" id="btn-mode-html">Teks / HTML</button>
                        </div>
                    </div>
                </div>

                <!-- 4. WYSIWYG EDITOR TEXTAREA -->
                <div class="mb-4">
                    <textarea name="content" id="post-content" class="form-control" rows="18" placeholder="Mulai tuliskan isi berita lengkap di sini...">{{ old('content', $article->content) }}</textarea>
                </div>

                <!-- 5. METABOX EXCERPT (RINGKASAN SINGKAT) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-card-text text-secondary me-2"></i> Ringkasan Singkat (Excerpt)</span>
                        <small class="text-muted fw-normal">Opsional (Muncul di kartu daftar berita)</small>
                    </div>
                    <div class="wp-metabox-body">
                        <textarea name="summary" id="post-summary" class="form-control" rows="2" placeholder="Tuliskan 1-2 kalimat ringkasan artikel untuk memikat pembaca...">{{ old('summary', $article->summary) }}</textarea>
                    </div>
                </div>

                <!-- 6. METABOX YOAST / RANK MATH SEO PREVIEW -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-google text-primary me-2"></i> Optimasi SEO & Cuplikan Google (RankMath / Yoast Style)</span>
                        <span class="badge bg-success bg-opacity-10 text-success" id="seo-score-badge">Optimal</span>
                    </div>
                    <div class="wp-metabox-body">
                        <p class="small text-muted mb-3">Lihat bagaimana postingan berita ini akan tampil di hasil pencarian Google:</p>
                        
                        <!-- SERP Simulator Card -->
                        <div class="google-preview-card mb-3">
                            <div class="google-url">
                                {{ url('/artikel') }}/<span id="serp-slug-preview">{{ $article->slug ?: 'judul-postingan' }}</span>
                            </div>
                            <div class="google-title" id="serp-title-preview">
                                {{ $article->meta_title ?: ($article->title ?: 'Judul Postingan Berita | PT Aktama Digital Antika') }}
                            </div>
                            <div class="google-desc" id="serp-desc-preview">
                                {{ $article->meta_description ?: ($article->summary ?: 'Klik untuk membaca ulasan lengkap mengenai inovasi teknologi, kecerdasan artifisial, dan transformasi digital...') }}
                            </div>
                        </div>

                        <!-- SEO Inputs -->
                        <div class="row g-3">
                            <div class="col-12">
                                <div class="d-flex justify-content-between">
                                    <label class="form-label small fw-bold text-dark mb-1">Judul SEO (Meta Title)</label>
                                    <small class="text-muted"><span id="meta-title-length">0</span> / 60 karakter</small>
                                </div>
                                <input type="text" name="meta_title" id="meta-title" class="form-control form-control-sm" placeholder="Biarkan kosong untuk otomatis memakai judul utama" value="{{ old('meta_title', $article->meta_title) }}">
                                <div class="progress mt-1" style="height: 4px;">
                                    <div class="progress-bar bg-success" id="title-progress" role="progressbar" style="width: 0%"></div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="d-flex justify-content-between">
                                    <label class="form-label small fw-bold text-dark mb-1">Deskripsi Meta (Meta Description)</label>
                                    <small class="text-muted"><span id="meta-desc-length">0</span> / 160 karakter</small>
                                </div>
                                <textarea name="meta_description" id="meta-description" class="form-control form-control-sm" rows="2" placeholder="Tuliskan deskripsi ringkas 1-2 kalimat yang menarik untuk hasil pencarian Google...">{{ old('meta_description', $article->meta_description) }}</textarea>
                                <div class="progress mt-1" style="height: 4px;">
                                    <div class="progress-bar bg-success" id="desc-progress" role="progressbar" style="width: 0%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- ========================================== -->
            <!-- KOLOM KANAN (METABOX PUBLIKASI, KATEGORI, MEDIA) -->
            <!-- ========================================== -->
            <div class="col-lg-4 col-xl-3">

                <!-- METABOX 1: TERBITKAN (PUBLISH BOX) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-send-check text-primary me-2"></i> Terbitkan</span>
                        @if($article->exists)
                            <span class="badge {{ $article->status === 'published' ? 'bg-success' : 'bg-secondary' }}">
                                {{ ucfirst($article->status) }}
                            </span>
                        @endif
                    </div>
                    <div class="wp-metabox-body small">
                        <!-- Status -->
                        <div class="mb-3">
                            <label class="text-muted fw-bold d-block mb-1">Status:</label>
                            <select name="status" id="post-status" class="form-select form-select-sm">
                                <option value="published" {{ old('status', $article->status ?? 'published') === 'published' ? 'selected' : '' }}>
                                    ✅ Diterbitkan (Published)
                                </option>
                                <option value="draft" {{ old('status', $article->status) === 'draft' ? 'selected' : '' }}>
                                    📝 Simpan sebagai Draf (Draft)
                                </option>
                            </select>
                        </div>

                        <!-- Tanggal Publikasi -->
                        <div class="mb-3">
                            <label class="text-muted fw-bold d-block mb-1">Tanggal Publikasi:</label>
                            <input type="datetime-local" name="published_at" class="form-control form-control-sm" value="{{ old('published_at', $article->published_at ? $article->published_at->format('Y-m-d\TH:i') : now()->format('Y-m-d\TH:i')) }}">
                            <small class="text-muted" style="font-size: 0.7rem;">Dapat diatur ke tanggal masa lampau atau jadwal.</small>
                        </div>

                        @if($article->exists && $article->views_count)
                            <div class="mb-3 text-muted">
                                <i class="bi bi-eye me-1"></i> Dibaca: <strong>{{ number_format($article->views_count) }} kali</strong>
                            </div>
                        @endif

                        <hr class="my-3">

                        <!-- Action Buttons -->
                        <div class="d-flex justify-content-between align-items-center">
                            @if($article->exists)
                                <button type="button" class="btn btn-link text-danger p-0 text-decoration-none small" onclick="if(confirm('Yakin ingin menghapus postingan ini?')) document.getElementById('delete-form').submit();">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            @else
                                <a href="{{ route('admin.articles.index') }}" class="btn btn-sm btn-light border">Batal</a>
                            @endif

                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-bold shadow-sm" id="btn-submit-post">
                                <i class="bi bi-cloud-arrow-up me-1"></i> {{ $article->exists ? 'Perbarui' : 'Terbitkan' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- METABOX 2: KATEGORI (CATEGORIES CHECKLIST + AJAX ADD) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-folder2-open text-warning me-2"></i> Kategori Berita</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="category-checklist mb-3" id="category-container">
                            @foreach($categories as $cat)
                                <div class="form-check mb-1">
                                    <input class="form-check-input" type="radio" name="category_id" id="cat-{{ $cat->id }}" value="{{ $cat->id }}" {{ old('category_id', $article->category_id) == $cat->id ? 'checked' : '' }}>
                                    <label class="form-check-label" for="cat-{{ $cat->id }}">
                                        {{ $cat->name }}
                                    </label>
                                </div>
                            @endforeach
                        </div>

                        <!-- Accordion Tambah Kategori Baru -->
                        <div class="border-top pt-2">
                            <a href="#collapseNewCat" data-bs-toggle="collapse" class="text-decoration-none fw-semibold small d-inline-flex align-items-center gap-1 text-primary">
                                <i class="bi bi-plus-circle"></i> + Tambah Kategori Baru
                            </a>
                            <div class="collapse mt-2" id="collapseNewCat">
                                <div class="input-group input-group-sm mb-1">
                                    <input type="text" id="new-category-name" class="form-control" placeholder="Nama kategori baru...">
                                    <button class="btn btn-outline-primary" type="button" id="btn-ajax-add-cat">Tambah</button>
                                </div>
                                <span id="cat-feedback" class="text-success small d-none" style="font-size: 0.7rem;"></span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- METABOX 3: GAMBAR UNGGULAN (FEATURED IMAGE) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-image text-success me-2"></i> Gambar Unggulan (Thumbnail)</span>
                    </div>
                    <div class="wp-metabox-body small text-center">
                        <div id="featured-image-preview-container" class="{{ $article->image ? '' : 'd-none' }} mb-2">
                            <img id="featured-image-preview" src="{{ $article->image ? asset('images/' . $article->image) : '' }}" alt="Featured Image" class="img-fluid rounded-3 shadow-xs mb-2 w-100 object-fit-cover" style="max-height: 180px;">
                            <div class="d-flex justify-content-center gap-2">
                                <button type="button" class="btn btn-xs btn-outline-secondary py-1 px-2" onclick="document.getElementById('featured-image-file').click();">
                                    <i class="bi bi-arrow-repeat"></i> Ganti Gambar
                                </button>
                                <button type="button" class="btn btn-xs btn-outline-danger py-1 px-2" id="btn-remove-featured">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            </div>
                        </div>

                        <div id="featured-image-dropzone" class="featured-dropzone {{ $article->image ? 'd-none' : '' }}" onclick="document.getElementById('featured-image-file').click();">
                            <i class="bi bi-cloud-arrow-up display-6 text-muted d-block mb-1"></i>
                            <strong class="text-primary d-block">Tetapkan Gambar Unggulan</strong>
                            <small class="text-muted">Klik untuk memilih file gambar dari komputer Anda</small>
                        </div>

                        <input type="file" name="image_file" id="featured-image-file" class="d-none" accept="image/png,image/jpeg,image/webp">
                        <input type="hidden" name="remove_image" id="remove-image-input" value="0">
                        <small class="text-muted d-block mt-2" style="font-size: 0.7rem;">Rekomendasi rasio 16:9 (1200x675 px). Maks 5MB.</small>
                    </div>
                </div>

                <!-- METABOX 4: TAG & KATA KUNCI (TAGS) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-tags text-info me-2"></i> Tag / Kata Kunci</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <input type="text" name="tags" id="tags-input" class="form-control form-control-sm mb-2" placeholder="Pisahkan dengan koma (AI, KKA, Riset...)" value="{{ old('tags', $article->tags) }}">
                        <div id="tags-chips-container" class="d-flex flex-wrap"></div>
                        <small class="text-muted d-block mt-1" style="font-size: 0.7rem;">Ketik kata kunci lalu beri tanda koma.</small>
                    </div>
                </div>

                <!-- METABOX 5: PENULIS (AUTHOR) -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-person-circle text-secondary me-2"></i> Penulis (Author)</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <input type="text" name="author" class="form-control form-control-sm" required value="{{ old('author', $article->author ?? 'Gede Erik Aktama, S.Pd., M.Pd.') }}">
                    </div>
                </div>

            </div>
        </div>
    </form>

    @if($article->exists)
        <form id="delete-form" action="{{ route('admin.articles.destroy', $article->id) }}" method="POST" class="d-none">
            @csrf
            @method('DELETE')
        </form>
    @endif

@endsection

@push('scripts')
<!-- TinyMCE 6 Core via CDNJS (Open Source & No API Key Needed) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.8.3/tinymce.min.js"></script>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('post-title');
        const slugDisplay = document.getElementById('slug-display');
        const slugInput = document.getElementById('slug-input');
        const slugEditBox = document.getElementById('slug-edit-box');
        const btnEditSlug = document.getElementById('btn-edit-slug');
        const btnSaveSlug = document.getElementById('btn-save-slug');
        const btnCancelSlug = document.getElementById('btn-cancel-slug');

        // 1. OTOMATIS GENERATE SLUG DARI JUDUL (WP STYLE)
        function slugify(text) {
            return text.toString().toLowerCase().trim()
                .replace(/[^\w\s-]/g, '')
                .replace(/[\s_-]+/g, '-')
                .replace(/^-+|-+$/g, '');
        }

        let isSlugManuallyEdited = {{ $article->exists ? 'true' : 'false' }};

        if (titleInput) {
            titleInput.addEventListener('input', function () {
                if (!isSlugManuallyEdited) {
                    const generated = slugify(this.value);
                    slugDisplay.innerText = generated || 'judul-postingan';
                    slugInput.value = generated;
                    updateSerpPreview();
                }
            });
        }

        // Edit Slug Inline
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
                slugDisplay.innerText = clean || 'judul-postingan';
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

        // 2. INISIALISASI TINYMCE 6 (WYSIWYG ALA WORDPRESS CLASSIC EDITOR)
        let isTinyActive = false;
        try {
            tinymce.init({
                selector: '#post-content',
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
                        xhr.withCredentials = false;
                        xhr.open('POST', '{{ route('admin.media.upload') }}');
                        xhr.setRequestHeader('X-CSRF-TOKEN', '{{ csrf_token() }}');

                        xhr.upload.onprogress = (e) => {
                            progress(e.loaded / e.total * 100);
                        };

                        xhr.onload = () => {
                            if (xhr.status === 403) {
                                reject({ message: 'HTTP Error: ' + xhr.status, remove: true });
                                return;
                            }
                            if (xhr.status < 200 || xhr.status >= 300) {
                                reject('Gagal mengunggah gambar: ' + xhr.status);
                                return;
                            }
                            const json = JSON.parse(xhr.responseText);
                            if (!json || typeof json.location != 'string') {
                                reject('Respons server tidak valid: ' + xhr.responseText);
                                return;
                            }
                            resolve(json.location);
                        };

                        xhr.onerror = () => {
                            reject('Koneksi terputus saat mengunggah gambar.');
                        };

                        const formData = new FormData();
                        formData.append('file', blobInfo.blob(), blobInfo.filename());
                        xhr.send(formData);
                    });
                },
                setup: function (editor) {
                    isTinyActive = true;
                    editor.on('input change keyup', function () {
                        editor.save();
                        updateStats();
                    });
                }
            });
        } catch (e) {
            console.warn('TinyMCE CDN fallback:', e);
        }

        // 3. STATISTIK KATA & WAKTU BACA
        function updateStats() {
            let contentText = '';
            if (isTinyActive && tinymce.get('post-content')) {
                contentText = tinymce.get('post-content').getContent({ format: 'text' });
            } else {
                contentText = document.getElementById('post-content').value;
            }
            const words = contentText.trim().split(/\s+/).filter(w => w.length > 0).length;
            const minutes = Math.ceil(words / 200) || 1;
            document.getElementById('word-count').innerText = words;
            document.getElementById('read-time').innerText = minutes;
        }

        // 4. TOGGLE MODE VISUAL / HTML
        const btnVisual = document.getElementById('btn-mode-visual');
        const btnHtml = document.getElementById('btn-mode-html');
        btnVisual.addEventListener('click', function () {
            btnVisual.classList.add('active');
            btnHtml.classList.remove('active');
            if (tinymce.get('post-content')) {
                tinymce.get('post-content').show();
            }
        });
        btnHtml.addEventListener('click', function () {
            btnHtml.classList.add('active');
            btnVisual.classList.remove('active');
            if (tinymce.get('post-content')) {
                tinymce.get('post-content').hide();
            }
        });

        // 5. TOMBOL "TAMBAH MEDIA" (ADD MEDIA UPLOAD)
        const btnAddMedia = document.getElementById('btn-add-media');
        const mediaFileInput = document.getElementById('media-file-input');
        const mediaSpinner = document.getElementById('media-uploading-spinner');
        const mediaMsg = document.getElementById('media-upload-msg');

        if (btnAddMedia && mediaFileInput) {
            btnAddMedia.addEventListener('click', function () {
                mediaFileInput.click();
            });

            mediaFileInput.addEventListener('change', function () {
                const file = this.files[0];
                if (!file) return;

                mediaSpinner.classList.remove('d-none');
                mediaMsg.innerText = 'Mengunggah ' + file.name + '...';

                const formData = new FormData();
                formData.append('file', file);

                fetch('{{ route('admin.media.upload') }}', {
                    method: 'POST',
                    headers: {
                        'X-CSRF-TOKEN': '{{ csrf_token() }}'
                    },
                    body: formData
                })
                .then(res => res.json())
                .then(data => {
                    mediaSpinner.classList.add('d-none');
                    if (data.location || data.url) {
                        const imgUrl = data.location || data.url;
                        const imgTag = `<p><img src="${imgUrl}" alt="${file.name}" class="img-fluid rounded-3 my-3" /></p>`;
                        
                        if (isTinyActive && tinymce.get('post-content')) {
                            tinymce.get('post-content').insertContent(imgTag);
                        } else {
                            const textarea = document.getElementById('post-content');
                            textarea.value += '\n' + imgTag + '\n';
                        }
                        mediaMsg.innerText = '✅ Berhasil disisipkan ke konten!';
                        setTimeout(() => mediaMsg.innerText = '', 3500);
                    } else {
                        mediaMsg.innerText = '❌ Gagal upload media.';
                    }
                    mediaFileInput.value = '';
                })
                .catch(err => {
                    console.error(err);
                    mediaSpinner.classList.add('d-none');
                    mediaMsg.innerText = '❌ Kesalahan jaringan.';
                    mediaFileInput.value = '';
                });
            });
        }

        // 6. METABOX FEATURED IMAGE PREVIEW & REMOVE
        const featuredInput = document.getElementById('featured-image-file');
        const featuredPreview = document.getElementById('featured-image-preview');
        const featuredPreviewContainer = document.getElementById('featured-image-preview-container');
        const featuredDropzone = document.getElementById('featured-image-dropzone');
        const btnRemoveFeatured = document.getElementById('btn-remove-featured');
        const removeImageInput = document.getElementById('remove-image-input');

        if (featuredInput) {
            featuredInput.addEventListener('change', function () {
                const file = this.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        featuredPreview.src = e.target.result;
                        featuredPreviewContainer.classList.remove('d-none');
                        featuredDropzone.classList.add('d-none');
                        removeImageInput.value = '0';
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
                removeImageInput.value = '1';
            });
        }

        // 7. AJAX TAMBAH KATEGORI BARU LANGSUNG
        const btnAjaxAddCat = document.getElementById('btn-ajax-add-cat');
        const newCatNameInput = document.getElementById('new-category-name');
        const catFeedback = document.getElementById('cat-feedback');
        const catContainer = document.getElementById('category-container');

        if (btnAjaxAddCat && newCatNameInput) {
            btnAjaxAddCat.addEventListener('click', function () {
                const catName = newCatNameInput.value.trim();
                if (!catName) return;

                btnAjaxAddCat.disabled = true;
                btnAjaxAddCat.innerText = '...';

                fetch('{{ route('admin.categories.ajaxStore') }}', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': '{{ csrf_token() }}'
                    },
                    body: JSON.stringify({ name: catName })
                })
                .then(res => res.json())
                .then(data => {
                    btnAjaxAddCat.disabled = false;
                    btnAjaxAddCat.innerText = 'Tambah';

                    if (data.success && data.category) {
                        const newCat = data.category;
                        const catHtml = `
                            <div class="form-check mb-1">
                                <input class="form-check-input" type="radio" name="category_id" id="cat-${newCat.id}" value="${newCat.id}" checked>
                                <label class="form-check-label fw-bold text-primary" for="cat-${newCat.id}">
                                    ${newCat.name} (Baru)
                                </label>
                            </div>
                        `;
                        catContainer.insertAdjacentHTML('afterbegin', catHtml);
                        newCatNameInput.value = '';
                        catFeedback.innerText = data.message;
                        catFeedback.classList.remove('d-none');
                        setTimeout(() => catFeedback.classList.add('d-none'), 3000);
                    }
                })
                .catch(err => {
                    console.error(err);
                    btnAjaxAddCat.disabled = false;
                    btnAjaxAddCat.innerText = 'Tambah';
                    alert('Gagal menambah kategori baru.');
                });
            });
        }

        // 8. REALTIME SEO SERP PREVIEW (YOAST / RANKMATH SIMULATOR)
        const metaTitleInput = document.getElementById('meta-title');
        const metaDescInput = document.getElementById('meta-description');
        const postSummaryInput = document.getElementById('post-summary');
        const serpTitlePreview = document.getElementById('serp-title-preview');
        const serpDescPreview = document.getElementById('serp-desc-preview');
        const serpSlugPreview = document.getElementById('serp-slug-preview');
        const metaTitleLength = document.getElementById('meta-title-length');
        const metaDescLength = document.getElementById('meta-desc-length');
        const titleProgress = document.getElementById('title-progress');
        const descProgress = document.getElementById('desc-progress');

        function updateSerpPreview() {
            const currentTitle = metaTitleInput.value.trim() || titleInput.value.trim() || 'Judul Postingan Berita';
            const currentDesc = metaDescInput.value.trim() || (postSummaryInput ? postSummaryInput.value.trim() : '') || 'Klik untuk membaca ulasan lengkap mengenai inovasi teknologi, kecerdasan artifisial, dan transformasi digital...';
            const currentSlug = slugInput.value.trim() || slugify(titleInput.value) || 'judul-postingan';

            serpTitlePreview.innerText = currentTitle + ' | PT Aktama Digital Antika';
            serpDescPreview.innerText = currentDesc;
            serpSlugPreview.innerText = currentSlug;

            // Meters
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
        if (postSummaryInput) postSummaryInput.addEventListener('input', updateSerpPreview);

        // 9. TAGS CHIP RENDERER
        const tagsInput = document.getElementById('tags-input');
        const tagsChipsContainer = document.getElementById('tags-chips-container');

        function renderTagChips() {
            tagsChipsContainer.innerHTML = '';
            const raw = tagsInput.value.split(',');
            raw.forEach(t => {
                const clean = t.trim();
                if (clean) {
                    const badge = document.createElement('span');
                    badge.className = 'tag-badge';
                    badge.innerHTML = `<i class="bi bi-tag-fill me-1"></i>${clean}`;
                    tagsChipsContainer.appendChild(badge);
                }
            });
        }

        if (tagsInput) {
            tagsInput.addEventListener('input', renderTagChips);
            renderTagChips();
        }

        // Initial setup
        updateSerpPreview();
        updateStats();
    });
</script>
@endpush
