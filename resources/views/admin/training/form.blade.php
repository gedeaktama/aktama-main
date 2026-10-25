@extends('layouts.admin')

@section('title', $program->exists ? 'Edit Pelatihan: ' . Str::limit($program->title, 40) : 'Tambah Program Pelatihan AI Baru')
@section('page_title', $program->exists ? 'Edit Pelatihan' : 'Tambah Pelatihan Baru')

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

    <form id="training-form" action="{{ $program->exists ? route('admin.training.update', $program->id) : route('admin.training.store') }}" method="POST" enctype="multipart/form-data">
        @csrf
        @if($program->exists)
            @method('PUT')
        @endif

        <div class="row g-4">
            <!-- ========================================== -->
            <!-- KOLOM KIRI (KONTEN PROGRAM PELATIHAN) -->
            <!-- ========================================== -->
            <div class="col-lg-8 col-xl-9">

                <!-- 1. JUDUL PROGRAM -->
                <div class="mb-3">
                    <input type="text" name="title" id="training-title" class="form-control post-title-input" placeholder="Masukkan judul program pelatihan (contoh: AI untuk Efisiensi Administrasi Perkantoran)..." required value="{{ old('title', $program->title) }}" autofocus>
                </div>

                <!-- 2. TARGET SASARAN PESERTA -->
                <div class="mb-3">
                    <label class="form-label small fw-bold text-dark">Target Sasaran Peserta *</label>
                    <input type="text" name="target_audience" class="form-control" required value="{{ old('target_audience', $program->target_audience) }}" placeholder="Contoh: ASN Instansi Pemerintah, Pejabat Fungsional, Sekretaris, Staf Administrasi">
                </div>

                <!-- 3. ACTION BAR EDITOR (ADD MEDIA) -->
                <div class="d-flex justify-content-between align-items-center bg-white p-2 border border-bottom-0 rounded-top-3">
                    <div class="d-flex align-items-center gap-2">
                        <button type="button" class="btn btn-sm btn-primary rounded-pill px-3 shadow-xs" onclick="openMediaLibraryModal('training-objectives')">
                            <i class="bi bi-images me-1"></i> Pustaka Media
                        </button>
                        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 shadow-xs" id="btn-add-media-training">
                            <i class="bi bi-cloud-arrow-up me-1"></i> Unggah Cepat
                        </button>
                        <input type="file" id="media-file-input-training" accept="image/*" class="d-none">
                        <span id="media-spinner-training" class="spinner-border spinner-border-sm text-primary d-none" role="status"></span>
                        <span id="media-msg-training" class="small text-muted"></span>
                    </div>

                    <span class="badge bg-light text-muted border py-1 px-2">
                        <i class="bi bi-bullseye me-1"></i> Tujuan Pembelajaran & Manfaat
                    </span>
                </div>

                <!-- 4. WYSIWYG TINYMCE 6 EDITOR (TUJUAN PEMBELAJARAN) -->
                <div class="mb-4">
                    <textarea name="objectives" id="training-objectives" class="form-control" rows="12" placeholder="Uraikan tujuan kompetensi, luaran yang dicapai peserta, dan manfaat praktis program ini...">{{ old('objectives', $program->objectives) }}</textarea>
                </div>

                <!-- 5. POKOK BAHASAN & SILABUS -->
                <div class="wp-metabox mb-4">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-journal-check text-primary me-2"></i> Pokok Bahasan & Silabus Materi</span>
                        <small class="text-muted fw-normal">Ketik 1 topik materi per baris</small>
                    </div>
                    <div class="wp-metabox-body">
                        <textarea name="syllabus_text" class="form-control" rows="6" placeholder="Modul 1: Prinsip Kerja LLM & Etika Keamanan Data Rahasia&#10;Modul 2: Formula Prompt Engineering Khusus Dokumen Dinas & Notula Rapat&#10;Modul 3: Otomasi Rumus Spreadsheet Kompleks & Dashboard dengan AI&#10;Modul 4: Praktek Mandiri & Simulasi Output Berstandar Kedinasan">{{ old('syllabus_text', is_array($program->syllabus) ? implode("\n", $program->syllabus) : '') }}</textarea>
                    </div>
                </div>

            </div>

            <!-- ========================================== -->
            <!-- KOLOM KANAN (METABOX PUBLIKASI & RINCIAN) -->
            <!-- ========================================== -->
            <div class="col-lg-4 col-xl-3">

                <!-- METABOX 1: PUBLIKASI -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-send-check text-primary me-2"></i> Publikasikan</span>
                        @if($program->exists)
                            <span class="badge {{ $program->is_published ? 'bg-success' : 'bg-warning text-dark' }}">
                                {{ $program->is_published ? 'Aktif' : 'Draf' }}
                            </span>
                        @endif
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="form-check form-switch mb-3 p-0 ps-5 d-flex align-items-center">
                            <input class="form-check-input ms-n5 mt-0" type="checkbox" role="switch" id="is_published" name="is_published" value="1" {{ old('is_published', $program->exists ? $program->is_published : true) ? 'checked' : '' }} style="width: 2.25rem; height: 1.25rem;">
                            <label class="form-check-label fw-bold text-dark ms-2" for="is_published">
                                Publikasikan Program
                            </label>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Urutan Tampil:</label>
                            <input type="number" name="sort_order" class="form-control form-control-sm" value="{{ old('sort_order', $program->sort_order ?? 0) }}" style="max-width: 100px;">
                        </div>

                        <hr class="my-3">

                        <div class="d-flex justify-content-between align-items-center">
                            @if($program->exists)
                                <button type="button" class="btn btn-link text-danger p-0 text-decoration-none small" onclick="if(confirm('Yakin ingin menghapus program pelatihan ini?')) document.getElementById('delete-training-form').submit();">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            @else
                                <a href="{{ route('admin.training.index') }}" class="btn btn-sm btn-light border">Batal</a>
                            @endif

                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-bold shadow-sm">
                                <i class="bi bi-check2-circle me-1"></i> {{ $program->exists ? 'Perbarui' : 'Simpan Pelatihan' }}
                            </button>
                        </div>
                    </div>
                </div>

                <!-- METABOX 2: KATEGORI & FORMAT -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-mortarboard text-warning me-2"></i> Kategori & Metode</span>
                    </div>
                    <div class="wp-metabox-body small">
                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Kategori Pelatihan *</label>
                            <select name="category" class="form-select form-select-sm" required>
                                <option value="ai-kantor" {{ old('category', $program->category) === 'ai-kantor' ? 'selected' : '' }}>AI Efisiensi Kantor / Instansi</option>
                                <option value="ai-pendidikan" {{ old('category', $program->category) === 'ai-pendidikan' ? 'selected' : '' }}>AI Tenaga Pendidik & Guru</option>
                                <option value="ai-bisnis" {{ old('category', $program->category) === 'ai-bisnis' ? 'selected' : '' }}>AI Bisnis & Pemasaran UMKM</option>
                                <option value="coding" {{ old('category', $program->category) === 'coding' ? 'selected' : '' }}>Koding & Computational Thinking (KKA)</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Format Pelaksanaan *</label>
                            <select name="delivery_format" class="form-select form-select-sm" required>
                                <option value="hybrid" {{ old('delivery_format', $program->delivery_format) === 'hybrid' ? 'selected' : '' }}>Hybrid (Online & Tatap Muka)</option>
                                <option value="online" {{ old('delivery_format', $program->delivery_format) === 'online' ? 'selected' : '' }}>Online (Zoom / Webinar)</option>
                                <option value="offline" {{ old('delivery_format', $program->delivery_format) === 'offline' ? 'selected' : '' }}>Offline (In-House Training)</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="text-dark fw-bold d-block mb-1">Durasi Pelatihan</label>
                            <input type="text" name="duration" class="form-control form-control-sm" value="{{ old('duration', $program->duration) }}" placeholder="Contoh: 16 Jam (2 Hari)">
                        </div>

                        <div class="mb-2">
                            <label class="text-dark fw-bold d-block mb-1">Informasi Biaya / Investasi</label>
                            <input type="text" name="price_info" class="form-control form-control-sm" value="{{ old('price_info', $program->price_info) }}" placeholder="Contoh: Penawaran Instansi / KAK">
                        </div>
                    </div>
                </div>

                <!-- METABOX 3: GAMBAR UNGGULAN PELATIHAN -->
                <div class="wp-metabox">
                    <div class="wp-metabox-header">
                        <span><i class="bi bi-image text-success me-2"></i> Gambar Unggulan (Banner)</span>
                    </div>
                    <div class="wp-metabox-body small text-center">
                        <div id="training-image-preview-container" class="{{ $program->image ? '' : 'd-none' }} mb-2">
                            <img id="training-image-preview" src="{{ $program->image ? asset('images/' . $program->image) : '' }}" alt="Thumbnail" class="img-fluid rounded-3 shadow-xs mb-2 w-100 object-fit-cover" style="max-height: 160px;">
                            <div class="d-flex justify-content-center gap-2">
                                <button type="button" class="btn btn-xs btn-outline-secondary py-1 px-2" onclick="document.getElementById('training-image-file').click();">
                                    <i class="bi bi-arrow-repeat"></i> Ganti Gambar
                                </button>
                                <button type="button" class="btn btn-xs btn-outline-danger py-1 px-2" id="btn-remove-training-image">
                                    <i class="bi bi-trash"></i> Hapus
                                </button>
                            </div>
                        </div>

                        <div id="training-image-dropzone" class="featured-dropzone {{ $program->image ? 'd-none' : '' }}" onclick="document.getElementById('training-image-file').click();">
                            <i class="bi bi-cloud-arrow-up display-6 text-muted d-block mb-1"></i>
                            <strong class="text-primary d-block">Tetapkan Gambar Program</strong>
                            <small class="text-muted">Klik untuk upload thumbnail</small>
                        </div>

                        <input type="file" name="image_file" id="training-image-file" class="d-none" accept="image/png,image/jpeg,image/webp">
                        <input type="hidden" name="remove_image" id="remove-training-image-input" value="0">
                        <small class="text-muted d-block mt-2" style="font-size: 0.7rem;">Maksimal 5 MB (JPG, PNG, WEBP).</small>
                    </div>
                </div>

            </div>
        </div>
    </form>

    @if($program->exists)
        <form id="delete-training-form" action="{{ route('admin.training.destroy', $program->id) }}" method="POST" class="d-none">
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
        // Inisialisasi TinyMCE 6
        let isTinyActive = false;
        try {
            tinymce.init({
                selector: '#training-objectives',
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
        const btnAddMedia = document.getElementById('btn-add-media-training');
        const mediaInput = document.getElementById('media-file-input-training');
        const spinner = document.getElementById('media-spinner-training');
        const msg = document.getElementById('media-msg-training');

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
                        if (isTinyActive && tinymce.get('training-objectives')) {
                            tinymce.get('training-objectives').insertContent(imgTag);
                        } else {
                            document.getElementById('training-objectives').value += '\n' + imgTag + '\n';
                        }
                        msg.innerText = '✅ Disisipkan ke materi!';
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
        const imgInput = document.getElementById('training-image-file');
        const preview = document.getElementById('training-image-preview');
        const previewCont = document.getElementById('training-image-preview-container');
        const dropzone = document.getElementById('training-image-dropzone');
        const btnRemove = document.getElementById('btn-remove-training-image');
        const removeInput = document.getElementById('remove-training-image-input');

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
