@extends('layouts.admin')

@section('title', $portfolio->exists ? 'Edit Portofolio: ' . Str::limit($portfolio->title, 40) : 'Tambah Portofolio Proyek Baru')
@section('page_title', $portfolio->exists ? 'Edit Portofolio' : 'Tambah Portofolio Baru')

@push('styles')
<style>
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
        font-size: 1.5rem;
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

    <form id="portfolio-form" action="{{ $portfolio->exists ? route('admin.portfolios.update', $portfolio->id) : route('admin.portfolios.store') }}" method="POST" enctype="multipart/form-data">
        @csrf
        @if($portfolio->exists)
            @method('PUT')
        @endif

        <div class="row g-4">
            <!-- ========================================== -->
            <!-- KOLOM KIRI (KONTEN UTAMA PORTOFOLIO) -->
            <!-- ========================================== -->
            <div class="col-lg-8 col-xl-9">

                <!-- 1. JUDUL PROYEK -->
                <div class="mb-3">
                    <input type="text" name="title" id="portfolio-title" class="form-control post-title-input" placeholder="Masukkan judul portofolio proyek (contoh: Sistem Informasi Kelulusan & Pengesahan Dokumen)..." required value="{{ old('title', $portfolio->title) }}" autofocus>
                </div>

                <!-- 2. SLUG PERMALINK -->
                <div class="permalink-bar mb-3">
                    <span class="text-muted"><i class="bi bi-link-45deg me-1"></i><strong>Slug:</strong></span>
                    <input type="text" name="slug" id="portfolio-slug" class="form-control form-control-sm font-monospace d-inline-block" style="max-width: 320px;" value="{{ old('slug', $portfolio->slug) }}" placeholder="otomatis-dari-judul">
                </div>

                <!-- 3. ACTION BAR EDITOR (ADD MEDIA) -->
                <div class="d-flex justify-content-between align-items-center bg-white p-2 border border-bottom-0 rounded-top-3">
                    <div class="d-flex align-items-center gap-2">
                        <button type="button" class="btn btn-sm btn-primary rounded-pill px-3 shadow-xs" onclick="openMediaLibraryModal('portfolio-description')">
                            <i class="bi bi-images me-1"></i> Pustaka Media
                        </button>
                        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 shadow-xs" id="btn-add-media-portfolio">
                            <i class="bi bi-cloud-arrow-up me-1"></i> Unggah Cepat
                        </button>
                        <input type="file" id="media-file-input-portfolio" accept="image/*" class="d-none">
                        <span id="media-spinner-portfolio" class="spinner-border spinner-border-sm text-primary d-none" role="status"></span>
                        <span id="media-msg-portfolio" class="small text-muted"></span>
                    </div>

                    <span class="badge bg-light text-muted border py-1 px-2">
                        <i class="bi bi-briefcase me-1"></i> Deskripsi & Rincian Solusi Teknis
                    </span>
                </div>

                <!-- 4. WYSIWYG TINYMCE 6 EDITOR -->
                <div class="mb-4">
                    <textarea name="description" id="portfolio-description" class="form-control" rows="14" placeholder="Uraikan latar belakang masalah, solusi rekayasa software yang dibangun, arsitektur, dan dampak positif bagi klien...">{{ old('description', $portfolio->description) }}</textarea>
                </div>

                <!-- 5. TEKNOLOGI & URL DEMO -->
                <div class="row g-3 mb-4">
                    <div class="col-md-6">
                        <div class="wp-metabox h-100">
                            <div class="wp-metabox-header">
                                <span><i class="bi bi-cpu text-info me-2"></i> Stack Teknologi *</span>
                            </div>
                            <div class="wp-metabox-body">
                                <input type="text" name="technology" class="form-control" required value="{{ old('technology', $portfolio->technology) }}" placeholder="Contoh: Laravel 12, MySQL, Tailwind CSS, REST API">
                                <small class="text-muted d-block mt-1">Sebutkan bahasa pemrograman & framework yang digunakan.</small>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="wp-metabox h-100">
                            <div class="wp-metabox-header">
                                <span><i class="bi bi-box-arrow-up-right text-primary me-2"></i> URL Proyek / Demo Live</span>
                            </div>
                            <div class="wp-metabox-body">
                                <input type="url" name="project_url" class="form-control" value="{{ old('project_url', $portfolio->project_url) }}" placeholder="https://contoh-klien.aktama.com">
                                <small class="text-muted d-block mt-1">Kosongkan jika sistem bersifat internal / tertutup.</small>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- ========================================== -->
            <!-- KOLOM KANAN (METABOX PUBLIKASI & PARAMETER) -->
            <!-- ========================================== -->
            <div class="col-lg-4 col-xl-3">

                <!-- METABOX 1: PUBLIKASI -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-send-check text-primary me-2"></i> Publikasikan</span>
                        @if($portfolio->exists)
                            <span class="badge {{ $portfolio->is_published ? 'bg-success' : 'bg-warning text-dark' }}">
                                {{ $portfolio->is_published ? 'Publik' : 'Draf' }}
                            </span>
                        @endif
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="form-check form-switch mb-3 p-0 ps-5 d-flex align-items-center">
                            <input class="form-check-input ms-n5 mt-0" type="checkbox" role="switch" id="is_published" name="is_published" value="1" {{ old('is_published', $portfolio->exists ? $portfolio->is_published : true) ? 'checked' : '' }} style="width: 2.25rem; height: 1.25rem;">
                            <label class="form-check-label fw-bold text-dark ms-2" for="is_published">
                                Publikasikan ke Showcase
                            </label>
                        </div>

                        <hr class="my-3">

                        <div class="d-flex justify-content-between align-items-center">
                            @if($portfolio->exists)
                                <button type="button" class="btn btn-link text-danger p-0 text-decoration-none small" onclick="if(confirm('Yakin ingin menghapus portofolio ini?')) document.getElementById('delete-portfolio-form').submit();">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            @else
                                <a href="{{ route('admin.portfolios.index') }}" class="btn btn-sm btn-light border">Batal</a>
                            @endif

                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-bold shadow-sm">
                                <i class="bi bi-check2-circle me-1"></i> {{ $portfolio->exists ? 'Perbarui' : 'Simpan Proyek' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- METABOX 2: KATEGORI & KLIEN -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-card-checklist text-warning me-2"></i> Kategori & Klien</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Kategori Proyek *</label>
                            <select name="category" class="form-select form-select-sm" required>
                                <option value="website" {{ old('category', $portfolio->category) === 'website' ? 'selected' : '' }}>Website Profil / Publik</option>
                                <option value="aplikasi" {{ old('category', $portfolio->category) === 'aplikasi' ? 'selected' : '' }}>Aplikasi Web & POS</option>
                                <option value="sistem-informasi" {{ old('category', $portfolio->category) === 'sistem-informasi' ? 'selected' : '' }}>Sistem Informasi Custom</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Jenis Klien</label>
                            <input type="text" name="client_type" class="form-control form-control-sm" value="{{ old('client_type', $portfolio->client_type) }}" placeholder="Contoh: Lembaga Pendidikan / UMKM">
                        </div>

                        <div class="mb-2">
                            <label class="text-dark fw-bold d-block mb-1">Tahun Pengerjaan</label>
                            <input type="text" name="project_year" class="form-control form-control-sm" value="{{ old('project_year', $portfolio->project_year ?? date('Y')) }}" placeholder="2025" style="max-width: 100px;">
                        </div>
                    </div>
                </div>

                <!-- METABOX 3: GAMBAR / MOCKUP PROYEK -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-image text-success me-2"></i> Screenshot / Mockup Proyek</span>
                    </div>
                    <div class="wp-metabox-body small text-center">
                        <div id="portfolio-image-preview-container" class="{{ $portfolio->image ? '' : 'd-none' }} mb-2">
                            <img id="portfolio-image-preview" src="{{ $portfolio->image ? asset('images/' . $portfolio->image) : '' }}" alt="Thumbnail" class="img-fluid rounded-3 shadow-xs mb-2 w-100 object-fit-cover" style="max-height: 160px;">
                            <div class="d-flex justify-content-center gap-2">
                                <button type="button" class="btn btn-xs btn-outline-secondary py-1 px-2" onclick="document.getElementById('portfolio-image-file').click();">
                                    <i class="bi bi-arrow-repeat"></i> Ganti Gambar
                                </button>
                                <button type="button" class="btn btn-xs btn-outline-danger py-1 px-2" id="btn-remove-portfolio-image">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            </div>
                        </div>

                        <div id="portfolio-image-dropzone" class="featured-dropzone {{ $portfolio->image ? 'd-none' : '' }}" onclick="document.getElementById('portfolio-image-file').click();">
                            <i class="bi bi-cloud-arrow-up display-6 text-muted d-block mb-1"></i>
                            <strong class="text-primary d-block">Tetapkan Mockup Proyek</strong>
                            <small class="text-muted">Klik untuk upload gambar</small>
                        </div>

                        <input type="file" name="image_file" id="portfolio-image-file" class="d-none" accept="image/png,image/jpeg,image/webp">
                        <input type="hidden" name="remove_image" id="remove-portfolio-image-input" value="0">
                        <small class="text-muted d-block mt-2" style="font-size: 0.7rem;">Maksimal 5 MB (JPG, PNG, WEBP).</small>
                    </div>
                </div>

            </div>
        </div>
    </form>

    @if($portfolio->exists)
        <form id="delete-portfolio-form" action="{{ route('admin.portfolios.destroy', $portfolio->id) }}" method="POST" class="d-none">
            @csrf
            @method('DELETE')
        </form>
    @endif

    @include('admin.partials.media-modal')

@endsection

@push('scripts')
<script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.8.3/tinymce.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('portfolio-title');
        const slugInput = document.getElementById('portfolio-slug');

        function slugify(text) {
            return text.toString().toLowerCase().trim()
                .replace(/[^\w\s-]/g, '')
                .replace(/[\s_-]+/g, '-')
                .replace(/^-+|-+$/g, '');
        }

        @if(!$portfolio->exists)
        if (titleInput && slugInput) {
            titleInput.addEventListener('input', function () {
                if (!slugInput.dataset.manual) {
                    slugInput.value = slugify(this.value);
                }
            });
            slugInput.addEventListener('input', function () {
                slugInput.dataset.manual = 'true';
            });
        }
        @endif

        // Inisialisasi TinyMCE 6
        let isTinyActive = false;
        try {
            tinymce.init({
                selector: '#portfolio-description',
                height: 380,
                menubar: 'file edit view insert format tools table',
                plugins: [
                    'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
                    'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                    'insertdatetime', 'media', 'table', 'help', 'wordcount'
                ],
                toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline | ' +
                         'forecolor backcolor | alignleft aligncenter alignright alignjustify | ' +
                         'bullist numlist | link image media table | removeformat code fullscreen',
                content_style: 'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 15px; line-height: 1.7; color: #1e293b; } img { max-width: 100%; height: auto; border-radius: 8px; }',
                images_upload_url: '{{ route('admin.media.upload') }}',
                images_upload_handler: function (blobInfo, progress) {
                    return new Promise((resolve, reject) => {
                        const xhr = new XMLHttpRequest();
                        xhr.open('POST', '{{ route('admin.media.upload') }}');
                        xhr.setRequestHeader('X-CSRF-TOKEN', '{{ csrf_token() }}');
                        xhr.onload = () => {
                            if (xhr.status < 200 || xhr.status >= 300) return reject('Upload gagal: ' + xhr.status);
                            const json = JSON.parse(xhr.responseText);
                            resolve(json.location || json.url);
                        };
                        xhr.onerror = () => reject('Koneksi terputus.');
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
            console.warn('TinyMCE fallback:', e);
        }

        // Add Media Button
        const btnAddMedia = document.getElementById('btn-add-media-portfolio');
        const mediaInput = document.getElementById('media-file-input-portfolio');
        const spinner = document.getElementById('media-spinner-portfolio');
        const msg = document.getElementById('media-msg-portfolio');

        if (btnAddMedia && mediaInput) {
            btnAddMedia.addEventListener('click', () => mediaInput.click());
            mediaInput.addEventListener('change', function () {
                const file = this.files[0];
                if (!file) return;

                spinner.classList.remove('d-none');
                msg.innerText = 'Mengunggah ' + file.name + '...';

                const formData = new FormData();
                formData.append('file', file);

                fetch('{{ route('admin.media.upload') }}', {
                    method: 'POST',
                    headers: { 'X-CSRF-TOKEN': '{{ csrf_token() }}' },
                    body: formData
                })
                .then(res => res.json())
                .then(data => {
                    spinner.classList.add('d-none');
                    if (data.location || data.url) {
                        const imgTag = `<p><img src="${data.location || data.url}" alt="${file.name}" class="img-fluid rounded-3 my-3" /></p>`;
                        if (isTinyActive && tinymce.get('portfolio-description')) {
                            tinymce.get('portfolio-description').insertContent(imgTag);
                        } else {
                            document.getElementById('portfolio-description').value += '\n' + imgTag + '\n';
                        }
                        msg.innerText = '✅ Disisipkan ke rincian!';
                        setTimeout(() => msg.innerText = '', 3000);
                    }
                    mediaInput.value = '';
                })
                .catch(() => {
                    spinner.classList.add('d-none');
                    msg.innerText = '❌ Gagal.';
                    mediaInput.value = '';
                });
            });
        }

        // Featured image
        const imgInput = document.getElementById('portfolio-image-file');
        const preview = document.getElementById('portfolio-image-preview');
        const previewCont = document.getElementById('portfolio-image-preview-container');
        const dropzone = document.getElementById('portfolio-image-dropzone');
        const btnRemove = document.getElementById('btn-remove-portfolio-image');
        const removeInput = document.getElementById('remove-portfolio-image-input');

        if (imgInput) {
            imgInput.addEventListener('change', function () {
                const file = this.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        preview.src = e.target.result;
                        previewCont.classList.remove('d-none');
                        dropzone.classList.add('d-none');
                        removeInput.value = '0';
                    };
                    reader.readAsDataURL(file);
                }
            });
        }

        if (btnRemove) {
            btnRemove.addEventListener('click', function () {
                imgInput.value = '';
                preview.src = '';
                previewCont.classList.add('d-none');
                dropzone.classList.remove('d-none');
                removeInput.value = '1';
            });
        }
    });
</script>
@endpush
