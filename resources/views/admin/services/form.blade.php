@extends('layouts.admin')

@section('title', $service->exists ? 'Edit Layanan: ' . Str::limit($service->title, 40) : 'Tambah Layanan Jasa Web & Aplikasi')
@section('page_title', $service->exists ? 'Edit Layanan' : 'Tambah Layanan Baru')

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

    <form id="service-form" action="{{ $service->exists ? route('admin.services.update', $service->id) : route('admin.services.store') }}" method="POST" enctype="multipart/form-data">
        @csrf
        @if($service->exists)
            @method('PUT')
        @endif

        <div class="row g-4">
            <!-- ========================================== -->
            <!-- KOLOM KIRI (KONTEN UTAMA LAYANAN) -->
            <!-- ========================================== -->
            <div class="col-lg-8 col-xl-9">

                <!-- 1. JUDUL LAYANAN -->
                <div class="mb-3">
                    <input type="text" name="title" id="service-title" class="form-control post-title-input" placeholder="Masukkan judul paket layanan (contoh: Website Profil Perusahaan & Bisnis)..." required value="{{ old('title', $service->title) }}" autofocus>
                </div>

                <!-- 2. SLUG PERMALINK -->
                <div class="permalink-bar mb-3">
                    <span class="text-muted"><i class="bi bi-link-45deg me-1"></i><strong>Slug:</strong></span>
                    <input type="text" name="slug" id="service-slug" class="form-control form-control-sm font-monospace d-inline-block" style="max-width: 320px;" value="{{ old('slug', $service->slug) }}" placeholder="otomatis-dari-judul">
                    <small class="text-muted ms-auto">Ditampilkan pada katalog jasa website</small>
                </div>

                <!-- 3. ACTION BAR EDITOR (ADD MEDIA) -->
                <div class="d-flex justify-content-between align-items-center bg-white p-2 border border-bottom-0 rounded-top-3">
                    <div class="d-flex align-items-center gap-2">
                        <button type="button" class="btn btn-sm btn-primary rounded-pill px-3 shadow-xs" onclick="openMediaLibraryModal('service-description')">
                            <i class="bi bi-images me-1"></i> Pustaka Media
                        </button>
                        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 shadow-xs" id="btn-add-media-service">
                            <i class="bi bi-cloud-arrow-up me-1"></i> Unggah Cepat
                        </button>
                        <input type="file" id="media-file-input-service" accept="image/*" class="d-none">
                        <span id="media-spinner-service" class="spinner-border spinner-border-sm text-primary d-none" role="status"></span>
                        <span id="media-msg-service" class="small text-muted"></span>
                    </div>

                    <span class="badge bg-light text-muted border py-1 px-2">
                        <i class="bi bi-card-heading me-1"></i> Deskripsi Lengkap Layanan
                    </span>
                </div>

                <!-- 4. WYSIWYG TINYMCE 6 EDITOR -->
                <div class="mb-4">
                    <textarea name="description" id="service-description" class="form-control" rows="14" placeholder="Tuliskan rincian deskripsi, manfaat, dan alur pengerjaan layanan di sini...">{{ old('description', $service->description) }}</textarea>
                </div>

                <!-- 5. RINGKASAN SINGKAT & FITUR UNGGULAN -->
                <div class="row g-3 mb-4">
                    <div class="col-md-6">
                        <div class="wp-metabox h-100">
                            <div class="wp-metabox-header">
                                <span><i class="bi bi-card-text text-secondary me-2"></i> Ringkasan Singkat (Excerpt)</span>
                            </div>
                            <div class="wp-metabox-body">
                                <textarea name="excerpt" class="form-control" rows="4" placeholder="1-2 kalimat ringkasan yang tampil di kartu penawaran beranda...">{{ old('excerpt', $service->excerpt) }}</textarea>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="wp-metabox h-100">
                            <div class="wp-metabox-header">
                                <span><i class="bi bi-check2-square text-success me-2"></i> Fitur-Fitur Unggulan</span>
                                <small class="text-muted fw-normal">1 baris = 1 poin</small>
                            </div>
                            <div class="wp-metabox-body">
                                <textarea name="features_text" class="form-control" rows="4" placeholder="Bebas Malware Judol&#10;Desain Mobile-First Cepat&#10;Integrasi WhatsApp Bisnis&#10;Optimasi Google SEO">{{ old('features_text', is_array($service->features) ? implode("\n", $service->features) : '') }}</textarea>
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
                        @if($service->exists)
                            <span class="badge {{ $service->is_published ? 'bg-success' : 'bg-warning text-dark' }}">
                                {{ $service->is_published ? 'Aktif' : 'Draf' }}
                            </span>
                        @endif
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="form-check form-switch mb-3 p-0 ps-5 d-flex align-items-center">
                            <input class="form-check-input ms-n5 mt-0" type="checkbox" role="switch" id="is_published" name="is_published" value="1" {{ old('is_published', $service->exists ? $service->is_published : true) ? 'checked' : '' }} style="width: 2.25rem; height: 1.25rem;">
                            <label class="form-check-label fw-bold text-dark ms-2" for="is_published">
                                Publikasikan Layanan
                            </label>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Urutan Tampil:</label>
                            <input type="number" name="sort_order" class="form-control form-control-sm" value="{{ old('sort_order', $service->sort_order ?? 0) }}" style="max-width: 100px;">
                        </div>

                        <hr class="my-3">

                        <div class="d-flex justify-content-between align-items-center">
                            @if($service->exists)
                                <button type="button" class="btn btn-link text-danger p-0 text-decoration-none small" onclick="if(confirm('Yakin ingin menghapus layanan ini?')) document.getElementById('delete-service-form').submit();">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            @else
                                <a href="{{ route('admin.services.index') }}" class="btn btn-sm btn-light border">Batal</a>
                            @endif

                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-bold shadow-sm">
                                <i class="bi bi-check2-circle me-1"></i> {{ $service->exists ? 'Perbarui' : 'Simpan Layanan' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- METABOX 2: KATEGORI & HARGA -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-tags text-warning me-2"></i> Kategori & Biaya</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Kategori Layanan *</label>
                            <select name="category" class="form-select form-select-sm" required>
                                <option value="website" {{ old('category', $service->category) === 'website' ? 'selected' : '' }}>Website Profil & Portofolio</option>
                                <option value="aplikasi" {{ old('category', $service->category) === 'aplikasi' ? 'selected' : '' }}>Aplikasi Web & Kasir POS</option>
                                <option value="sistem-informasi" {{ old('category', $service->category) === 'sistem-informasi' ? 'selected' : '' }}>Sistem Informasi Custom</option>
                                <option value="otomasi" {{ old('category', $service->category) === 'otomasi' ? 'selected' : '' }}>Otomasi Kerja & AI</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Harga Mulai (Label)</label>
                            <input type="text" name="price_starting" class="form-control form-control-sm" value="{{ old('price_starting', $service->price_starting) }}" placeholder="Mulai Rp 2.500.000">
                        </div>

                        <div class="mb-2">
                            <label class="text-dark fw-bold d-block mb-1">Ikon Bootstrap</label>
                            <div class="input-group input-group-sm">
                                <span class="input-group-text"><i class="bi {{ $service->icon ?? 'bi-globe' }}"></i></span>
                                <input type="text" name="icon" class="form-control" value="{{ old('icon', $service->icon ?? 'bi-globe') }}" placeholder="bi-globe">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- METABOX 3: GAMBAR UNGGULAN LAYANAN -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-image text-success me-2"></i> Gambar Unggulan / Banner</span>
                    </div>
                    <div class="wp-metabox-body small text-center">
                        <div id="service-image-preview-container" class="{{ $service->image ? '' : 'd-none' }} mb-2">
                            <img id="service-image-preview" src="{{ $service->image ? asset('images/' . $service->image) : '' }}" alt="Thumbnail" class="img-fluid rounded-3 shadow-xs mb-2 w-100 object-fit-cover" style="max-height: 160px;">
                            <div class="d-flex justify-content-center gap-2">
                                <button type="button" class="btn btn-xs btn-outline-secondary py-1 px-2" onclick="document.getElementById('service-image-file').click();">
                                    <i class="bi bi-arrow-repeat"></i> Ganti Gambar
                                </button>
                                <button type="button" class="btn btn-xs btn-outline-danger py-1 px-2" id="btn-remove-service-image">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            </div>
                        </div>

                        <div id="service-image-dropzone" class="featured-dropzone {{ $service->image ? 'd-none' : '' }}" onclick="document.getElementById('service-image-file').click();">
                            <i class="bi bi-cloud-arrow-up display-6 text-muted d-block mb-1"></i>
                            <strong class="text-primary d-block">Tetapkan Gambar Layanan</strong>
                            <small class="text-muted">Klik untuk upload thumbnail</small>
                        </div>

                        <input type="file" name="image_file" id="service-image-file" class="d-none" accept="image/png,image/jpeg,image/webp">
                        <input type="hidden" name="remove_image" id="remove-service-image-input" value="0">
                        <small class="text-muted d-block mt-2" style="font-size: 0.7rem;">Maksimal 5 MB (JPG, PNG, WEBP).</small>
                    </div>
                </div>

            </div>
        </div>
    </form>

    @if($service->exists)
        <form id="delete-service-form" action="{{ route('admin.services.destroy', $service->id) }}" method="POST" class="d-none">
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
        const titleInput = document.getElementById('service-title');
        const slugInput = document.getElementById('service-slug');

        function slugify(text) {
            return text.toString().toLowerCase().trim()
                .replace(/[^\w\s-]/g, '')
                .replace(/[\s_-]+/g, '-')
                .replace(/^-+|-+$/g, '');
        }

        @if(!$service->exists)
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
                selector: '#service-description',
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
        const btnAddMedia = document.getElementById('btn-add-media-service');
        const mediaInput = document.getElementById('media-file-input-service');
        const spinner = document.getElementById('media-spinner-service');
        const msg = document.getElementById('media-msg-service');

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
                        if (isTinyActive && tinymce.get('service-description')) {
                            tinymce.get('service-description').insertContent(imgTag);
                        } else {
                            document.getElementById('service-description').value += '\n' + imgTag + '\n';
                        }
                        msg.innerText = '✅ Disisipkan ke deskripsi!';
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
        const imgInput = document.getElementById('service-image-file');
        const preview = document.getElementById('service-image-preview');
        const previewCont = document.getElementById('service-image-preview-container');
        const dropzone = document.getElementById('service-image-dropzone');
        const btnRemove = document.getElementById('btn-remove-service-image');
        const removeInput = document.getElementById('remove-service-image-input');

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
