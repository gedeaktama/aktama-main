<!-- MODAL PUSTAKA MEDIA (WORDPRESS MEDIA LIBRARY MODAL) -->
<div class="modal fade" id="modalMediaLibrary" tabindex="-1" aria-labelledby="modalMediaLibraryLabel" aria-hidden="true" style="z-index: 1060;">
    <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable" style="max-width: 92%;">
        <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
            <!-- Modal Header -->
            <div class="modal-header bg-dark text-white py-3 px-4">
                <div class="d-flex align-items-center gap-2">
                    <i class="bi bi-images text-info fs-5"></i>
                    <h5 class="modal-title fw-bold fs-6 mb-0" id="modalMediaLibraryLabel">Pustaka Media & Berkas (WordPress Media Library)</h5>
                </div>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Tutup"></button>
            </div>

            <!-- Modal Sub-Header (Tabs) -->
            <div class="bg-light border-bottom px-4 pt-2">
                <ul class="nav nav-tabs border-bottom-0" id="mediaLibraryTabs" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active fw-semibold text-dark py-2 px-3" id="tab-library-tab" data-bs-toggle="tab" data-bs-target="#tab-library" type="button" role="tab">
                            <i class="bi bi-grid-3x3-gap-fill me-1 text-primary"></i> Pustaka Media
                        </button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link fw-semibold text-secondary py-2 px-3" id="tab-upload-tab" data-bs-toggle="tab" data-bs-target="#tab-upload" type="button" role="tab">
                            <i class="bi bi-cloud-arrow-up-fill me-1 text-success"></i> Unggah Berkas Baru
                        </button>
                    </li>
                </ul>
            </div>

            <!-- Modal Body -->
            <div class="modal-body p-0">
                <div class="tab-content" id="mediaLibraryTabsContent">
                    <!-- TAB 1: PUSTAKA MEDIA (GALLERY) -->
                    <div class="tab-pane fade show active" id="tab-library" role="tabpanel">
                        <!-- Toolbar Filter & Cari -->
                        <div class="p-3 bg-white border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
                            <div class="d-flex align-items-center gap-2 flex-grow-1" style="max-width: 450px;">
                                <div class="input-group input-group-sm">
                                    <span class="input-group-text bg-light border-end-0"><i class="bi bi-search text-muted"></i></span>
                                    <input type="text" id="mediaSearchInput" class="form-control border-start-0" placeholder="Cari nama gambar...">
                                </div>
                                <select id="mediaFolderFilter" class="form-select form-select-sm" style="width: 170px;">
                                    <option value="all">Semua Folder</option>
                                    <option value="uploads">Uploads (Umum)</option>
                                    <option value="articles">Artikel Berita</option>
                                    <option value="services">Jasa Layanan</option>
                                    <option value="training">Pelatihan AI</option>
                                    <option value="portfolios">Portofolio</option>
                                    <option value="pages">Halaman</option>
                                </select>
                            </div>
                            <div class="d-flex align-items-center gap-2">
                                <span class="badge bg-light text-dark border small" id="mediaCountBadge">Memuat berkas...</span>
                                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="loadMediaLibrary()" title="Muat Ulang">
                                    <i class="bi bi-arrow-clockwise"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Main Split Content (Grid & Sidebar) -->
                        <div class="row g-0" style="min-height: 440px; max-height: 520px; overflow-y: hidden;">
                            <!-- Kolom Kiri: Grid Gambar -->
                            <div class="col-lg-8 col-xl-9 p-3 border-end overflow-auto" id="mediaGridContainer" style="max-height: 520px; background-color: #f8fafc;">
                                <div class="row g-2" id="mediaItemsGrid">
                                    <!-- Rendered via JS -->
                                </div>
                                <div id="mediaLoadingState" class="text-center py-5">
                                    <div class="spinner-border text-primary" role="status">
                                        <span class="visually-hidden">Memuat...</span>
                                    </div>
                                    <p class="text-muted small mt-2">Memuat daftar media...</p>
                                </div>
                                <div id="mediaEmptyState" class="text-center py-5 d-none">
                                    <i class="bi bi-image text-muted display-6"></i>
                                    <p class="text-muted small mt-2">Tidak ada media yang ditemukan.</p>
                                </div>
                            </div>

                            <!-- Kolom Kanan: Rincian Lampiran (Attachment Details) -->
                            <div class="col-lg-4 col-xl-3 p-3 bg-white overflow-auto" style="max-height: 520px;">
                                <h6 class="fw-bold text-dark text-uppercase small mb-3 border-bottom pb-2">Rincian Lampiran</h6>
                                
                                <div id="mediaDetailsEmpty" class="text-center py-5 text-muted small">
                                    <i class="bi bi-hand-index-thumb fs-2 text-secondary opacity-50 d-block mb-2"></i>
                                    Klik salah satu gambar pada galeri untuk melihat rincian & menyisipkannya.
                                </div>

                                <div id="mediaDetailsActive" class="d-none">
                                    <div class="rounded-3 border overflow-hidden mb-3 bg-light text-center p-2 shadow-xs" style="max-height: 180px;">
                                        <img id="detailImgPreview" src="" alt="Preview" class="img-fluid rounded" style="max-height: 160px; object-fit: contain;">
                                    </div>
                                    
                                    <div class="small mb-3 space-y-1">
                                        <div class="text-truncate fw-bold text-dark" id="detailFilename" title="">-</div>
                                        <div class="text-muted" style="font-size: 0.78rem;">Folder: <span class="badge bg-secondary bg-opacity-25 text-dark" id="detailFolder">-</span></div>
                                        <div class="text-muted" style="font-size: 0.78rem;">Dimensi: <strong class="text-dark" id="detailDimensions">-</strong></div>
                                        <div class="text-muted" style="font-size: 0.78rem;">Ukuran: <strong class="text-dark" id="detailSize">-</strong></div>
                                        <div class="text-muted" style="font-size: 0.78rem;">Diunggah: <span id="detailDate">-</span></div>
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label small fw-semibold text-muted mb-1">Tautan File (URL)</label>
                                        <div class="input-group input-group-sm">
                                            <input type="text" id="detailFileUrl" class="form-control" readonly>
                                            <button class="btn btn-outline-secondary" type="button" onclick="copyMediaUrl()" title="Salin Tautan">
                                                <i class="bi bi-clipboard"></i>
                                            </button>
                                        </div>
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label small fw-semibold text-muted mb-1">Teks Alternatif (Alt Text)</label>
                                        <input type="text" id="detailAltText" class="form-control form-control-sm" placeholder="Deskripsikan gambar...">
                                    </div>

                                    <div class="d-grid gap-2">
                                        <button type="button" class="btn btn-primary btn-sm rounded-pill py-2 fw-semibold shadow-sm" onclick="insertSelectedMedia()">
                                            <i class="bi bi-check2-circle me-1"></i> Sisipkan ke Postingan
                                        </button>
                                        <button type="button" class="btn btn-outline-danger btn-sm rounded-pill" id="btnDeleteMedia" onclick="deleteSelectedMedia()" style="display: none;">
                                            <i class="bi bi-trash3 me-1"></i> Hapus Permanen
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: UNGGAH BERKAS BARU -->
                    <div class="tab-pane fade p-4" id="tab-upload" role="tabpanel">
                        <div class="border border-2 border-dashed rounded-4 p-5 text-center bg-light" id="mediaDropzone">
                            <i class="bi bi-cloud-arrow-up text-primary display-4 d-block mb-3"></i>
                            <h5 class="fw-bold text-dark mb-1">Tarik & Letakkan berkas gambar di sini</h5>
                            <p class="text-muted small mb-3">Format yang didukung: JPG, JPEG, PNG, WEBP, GIF, SVG (Maks. 5MB per file)</p>
                            
                            <input type="file" id="mediaFileInput" class="d-none" accept="image/*">
                            <button type="button" class="btn btn-primary rounded-pill px-4 py-2 fw-semibold shadow-sm" onclick="document.getElementById('mediaFileInput').click()">
                                <i class="bi bi-folder2-open me-1"></i> Pilih Berkas Komputer
                            </button>

                            <div id="uploadProgressContainer" class="mt-4 mx-auto d-none" style="max-width: 400px;">
                                <div class="progress" style="height: 10px;">
                                    <div id="mediaUploadProgressBar" class="progress-bar progress-bar-striped progress-bar-animated bg-success" role="progressbar" style="width: 0%"></div>
                                </div>
                                <small class="text-muted mt-1 d-block" id="mediaUploadStatus">Mengunggah file ke server...</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="modal-footer bg-light py-2 px-4 d-flex justify-content-between align-items-center">
                <small class="text-muted">PT Aktama Digital Antika • Sistem Media Terpusat</small>
                <button type="button" class="btn btn-secondary btn-sm rounded-pill px-3" data-bs-dismiss="modal">Tutup</button>
            </div>
        </div>
    </div>
</div>

<script>
    // State Media Library
    let mediaLibraryItems = [];
    let selectedMediaItem = null;
    let targetEditorInstanceName = 'editor'; // Default target TinyMCE instance

    function openMediaLibraryModal(editorId = 'editor') {
        targetEditorInstanceName = editorId;
        const modalEl = document.getElementById('modalMediaLibrary');
        const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
        modal.show();

        // Switch to Tab 1
        const tabBtn = document.getElementById('tab-library-tab');
        if (tabBtn) {
            bootstrap.Tab.getOrCreateInstance(tabBtn).show();
        }

        // Load items if not loaded or refresh
        loadMediaLibrary();
    }

    async function loadMediaLibrary() {
        const loadingState = document.getElementById('mediaLoadingState');
        const emptyState = document.getElementById('mediaEmptyState');
        const itemsGrid = document.getElementById('mediaItemsGrid');
        const countBadge = document.getElementById('mediaCountBadge');

        if (loadingState) loadingState.classList.remove('d-none');
        if (emptyState) emptyState.classList.add('d-none');
        if (itemsGrid) itemsGrid.innerHTML = '';

        const search = document.getElementById('mediaSearchInput')?.value || '';
        const folder = document.getElementById('mediaFolderFilter')?.value || 'all';

        try {
            const res = await fetch(`{{ route('admin.media.list') }}?folder=${encodeURIComponent(folder)}&search=${encodeURIComponent(search)}`, {
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            const data = await res.json();
            mediaLibraryItems = data.media || [];

            if (countBadge) {
                countBadge.textContent = `${mediaLibraryItems.length} berkas`;
            }

            if (loadingState) loadingState.classList.add('d-none');

            if (mediaLibraryItems.length === 0) {
                if (emptyState) emptyState.classList.remove('d-none');
                return;
            }

            renderMediaGrid(mediaLibraryItems);
        } catch (err) {
            console.error('Gagal memuat media library:', err);
            if (loadingState) loadingState.classList.add('d-none');
            if (countBadge) countBadge.textContent = 'Gagal memuat';
        }
    }

    function renderMediaGrid(items) {
        const grid = document.getElementById('mediaItemsGrid');
        if (!grid) return;
        grid.innerHTML = '';

        items.forEach((item, index) => {
            const col = document.createElement('div');
            col.className = 'col-6 col-sm-4 col-md-3 col-lg-3 col-xl-2';

            const card = document.createElement('div');
            card.className = 'card h-100 border rounded-3 overflow-hidden position-relative media-thumb-card shadow-xs';
            card.style.cursor = 'pointer';
            card.style.transition = 'all 0.15s ease-in-out';
            card.dataset.index = index;

            if (selectedMediaItem && selectedMediaItem.url === item.url) {
                card.style.borderColor = '#2563eb';
                card.style.boxShadow = '0 0 0 3px rgba(37, 99, 235, 0.35)';
            }

            card.innerHTML = `
                <div class="position-relative">
                    <div class="ratio ratio-1x1 bg-light">
                        <img src="${item.url}" alt="${item.filename}" class="object-fit-cover w-100 h-100" loading="lazy">
                    </div>
                    <span class="position-absolute bottom-0 start-0 m-1 badge bg-dark bg-opacity-75 text-white" style="font-size: 0.65rem; z-index: 2;">
                        ${item.folder}
                    </span>
                </div>
                <div class="p-1 px-2 bg-white text-truncate small" style="font-size: 0.72rem;" title="${item.filename}">
                    ${item.filename}
                </div>
            `;

            card.addEventListener('click', () => {
                selectMediaItem(item);
            });

            col.appendChild(card);
            grid.appendChild(col);
        });
    }

    function selectMediaItem(item) {
        selectedMediaItem = item;

        // Update cards styling
        document.querySelectorAll('.media-thumb-card').forEach(card => {
            card.style.borderColor = '#e2e8f0';
            card.style.boxShadow = 'none';
        });

        const activeCard = Array.from(document.querySelectorAll('.media-thumb-card')).find(c => {
            const idx = c.dataset.index;
            return mediaLibraryItems[idx] && mediaLibraryItems[idx].url === item.url;
        });

        if (activeCard) {
            activeCard.style.borderColor = '#2563eb';
            activeCard.style.boxShadow = '0 0 0 3px rgba(37, 99, 235, 0.35)';
        }

        // Show details sidebar
        document.getElementById('mediaDetailsEmpty')?.classList.add('d-none');
        const detailsActive = document.getElementById('mediaDetailsActive');
        if (detailsActive) detailsActive.classList.remove('d-none');

        document.getElementById('detailImgPreview').src = item.url;
        const filenameEl = document.getElementById('detailFilename');
        filenameEl.textContent = item.filename;
        filenameEl.title = item.filename;
        document.getElementById('detailFolder').textContent = item.folder;
        document.getElementById('detailDimensions').textContent = item.dimensions;
        document.getElementById('detailSize').textContent = item.size;
        document.getElementById('detailDate').textContent = item.date;
        document.getElementById('detailFileUrl').value = item.url;
        
        // Auto-generate Alt Text from filename
        const cleanAlt = item.filename.replace(/^media-/, '').replace(/-\d+-[a-zA-Z0-9]+\.[a-zA-Z]+$/, '').replace(/[-_]/g, ' ');
        document.getElementById('detailAltText').value = cleanAlt;

        // Delete button only for uploads folder
        const btnDelete = document.getElementById('btnDeleteMedia');
        if (btnDelete) {
            btnDelete.style.display = item.folder === 'uploads' ? 'block' : 'none';
        }
    }

    function copyMediaUrl() {
        const input = document.getElementById('detailFileUrl');
        if (!input || !input.value) return;
        input.select();
        navigator.clipboard.writeText(input.value).then(() => {
            alert('Tautan URL gambar berhasil disalin ke clipboard!');
        });
    }

    function insertSelectedMedia() {
        if (!selectedMediaItem) {
            alert('Silakan pilih salah satu gambar terlebih dahulu.');
            return;
        }

        const altText = document.getElementById('detailAltText')?.value || selectedMediaItem.filename;
        const imgHtml = `<p><img src="${selectedMediaItem.url}" alt="${altText}" class="img-fluid rounded my-3" /></p>`;

        // Cek editor TinyMCE aktif
        if (typeof tinymce !== 'undefined' && tinymce.get(targetEditorInstanceName)) {
            tinymce.get(targetEditorInstanceName).insertContent(imgHtml);
        } else if (typeof tinymce !== 'undefined' && tinymce.activeEditor) {
            tinymce.activeEditor.insertContent(imgHtml);
        } else {
            // Fallback textarea biasa
            const textarea = document.getElementById(targetEditorInstanceName);
            if (textarea) {
                textarea.value += "\n" + imgHtml + "\n";
            }
        }

        // Tutup modal
        const modalEl = document.getElementById('modalMediaLibrary');
        const modal = bootstrap.Modal.getInstance(modalEl);
        if (modal) modal.hide();
    }

    async function deleteSelectedMedia() {
        if (!selectedMediaItem || selectedMediaItem.folder !== 'uploads') return;

        if (!confirm(`Apakah Anda yakin ingin menghapus file "${selectedMediaItem.filename}" secara permanen?`)) {
            return;
        }

        try {
            const res = await fetch(`{{ route('admin.media.destroy') }}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    filename: selectedMediaItem.filename,
                    folder: 'uploads'
                })
            });

            const data = await res.json();
            if (data.success) {
                selectedMediaItem = null;
                document.getElementById('mediaDetailsEmpty')?.classList.remove('d-none');
                document.getElementById('mediaDetailsActive')?.classList.add('d-none');
                loadMediaLibrary();
            } else {
                alert(data.message || 'Gagal menghapus file.');
            }
        } catch (err) {
            console.error('Error deleting media:', err);
            alert('Terjadi kesalahan saat menghapus file.');
        }
    }

    // Event listener search & filter
    document.addEventListener('DOMContentLoaded', () => {
        const searchInput = document.getElementById('mediaSearchInput');
        const folderFilter = document.getElementById('mediaFolderFilter');

        let searchDebounce = null;
        if (searchInput) {
            searchInput.addEventListener('input', () => {
                clearTimeout(searchDebounce);
                searchDebounce = setTimeout(() => {
                    loadMediaLibrary();
                }, 350);
            });
        }

        if (folderFilter) {
            folderFilter.addEventListener('change', () => {
                loadMediaLibrary();
            });
        }

        // Setup File Upload in Tab 2
        const fileInput = document.getElementById('mediaFileInput');
        if (fileInput) {
            fileInput.addEventListener('change', handleMediaFileUpload);
        }

        // Setup Drag & Drop
        const dropzone = document.getElementById('mediaDropzone');
        if (dropzone) {
            ['dragenter', 'dragover'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.add('border-primary', 'bg-white');
                }, false);
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.remove('border-primary', 'bg-white');
                }, false);
            });

            dropzone.addEventListener('drop', (e) => {
                const dt = e.dataTransfer;
                const files = dt.files;
                if (files.length > 0) {
                    uploadMediaFile(files[0]);
                }
            }, false);
        }
    });

    function handleMediaFileUpload(e) {
        if (e.target.files && e.target.files.length > 0) {
            uploadMediaFile(e.target.files[0]);
        }
    }

    async function uploadMediaFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Mohon pilih file gambar yang valid.');
            return;
        }

        if (file.size > 5 * 1024 * 1024) {
            alert('Ukuran file maksimal adalah 5MB.');
            return;
        }

        const progressContainer = document.getElementById('uploadProgressContainer');
        const progressBar = document.getElementById('mediaUploadProgressBar');
        const statusText = document.getElementById('mediaUploadStatus');

        if (progressContainer) progressContainer.classList.remove('d-none');
        if (progressBar) progressBar.style.width = '30%';
        if (statusText) statusText.textContent = `Mengunggah ${file.name}...`;

        const formData = new FormData();
        formData.append('file', file);
        formData.append('folder', 'uploads');

        try {
            if (progressBar) progressBar.style.width = '70%';

            const res = await fetch(`{{ route('admin.media.upload') }}`, {
                method: 'POST',
                headers: {
                    'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                    'Accept': 'application/json'
                },
                body: formData
            });

            const data = await res.json();
            if (progressBar) progressBar.style.width = '100%';

            if (res.ok && data.url) {
                if (statusText) statusText.textContent = 'Unggahan selesai!';
                setTimeout(() => {
                    if (progressContainer) progressContainer.classList.add('d-none');
                    if (progressBar) progressBar.style.width = '0%';
                    // Pindah ke Tab 1 dan pilih gambar baru
                    const tabBtn = document.getElementById('tab-library-tab');
                    if (tabBtn) bootstrap.Tab.getOrCreateInstance(tabBtn).show();
                    loadMediaLibrary().then(() => {
                        const newUploaded = mediaLibraryItems.find(m => m.url === data.url);
                        if (newUploaded) selectMediaItem(newUploaded);
                    });
                }, 500);
            } else {
                alert(data.error?.message || 'Gagal mengunggah file.');
                if (progressContainer) progressContainer.classList.add('d-none');
            }
        } catch (err) {
            console.error('Upload error:', err);
            alert('Terjadi kesalahan jaringan saat mengunggah file.');
            if (progressContainer) progressContainer.classList.add('d-none');
        }
    }
</script>
