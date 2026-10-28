@extends('layouts.admin')

@section('title', 'Pengaturan Menu Navigasi')
@section('page_title', 'Pengaturan Menu Navigasi (Drag & Drop)')

@section('content')

    <form action="{{ route('admin.menus.update') }}" method="POST" id="menu-form">
        @csrf
        <input type="hidden" name="header_menu" id="header_menu_input" value="">
        <input type="hidden" name="footer_menu" id="footer_menu_input" value="">

        <div class="row g-4">
            <!-- KOLOM KIRI: SUMBER ITEM MENU -->
            <div class="col-lg-4">
                <!-- ACCORDION SUMBER MENU -->
                <div class="card border-0 shadow-sm rounded-4 bg-white mb-3">
                    <div class="card-header bg-white py-3 border-bottom">
                        <h6 class="fw-bold text-dark mb-0"><i class="bi bi-file-earmark-text text-primary me-2"></i> Tambahkan Halaman CMS</h6>
                    </div>
                    <div class="card-body p-3">
                        @if($pages->isNotEmpty())
                            <div class="mb-3" style="max-height: 200px; overflow-y: auto;">
                                @foreach($pages as $p)
                                    <div class="form-check mb-2">
                                        <input class="form-check-input page-checkbox" type="checkbox" value="{{ $p->title }}" data-url="/halaman/{{ $p->slug }}" id="page_{{ $p->id }}">
                                        <label class="form-check-label small text-dark" for="page_{{ $p->id }}">
                                            {{ $p->title }}
                                        </label>
                                    </div>
                                @endforeach
                            </div>
                            <button type="button" class="btn btn-outline-primary btn-sm rounded-pill w-100" id="btn-add-pages">
                                <i class="bi bi-plus-circle me-1"></i> Tambahkan Halaman Terpilih
                            </button>
                        @else
                            <p class="text-muted small mb-0">Belum ada halaman kustom. Anda dapat membuat halaman baru terlebih dahulu.</p>
                        @endif
                    </div>
                </div>

                <!-- TAUTAN KUSTOM -->
                <div class="card border-0 shadow-sm rounded-4 bg-white">
                    <div class="card-header bg-white py-3 border-bottom">
                        <h6 class="fw-bold text-dark mb-0"><i class="bi bi-link-45deg text-primary me-2"></i> Tambahkan Tautan Kustom</h6>
                    </div>
                    <div class="card-body p-3">
                        <div class="mb-2">
                            <label class="form-label small fw-bold text-dark">URL / Tautan Tujuan</label>
                            <input type="text" id="custom-url" class="form-control form-control-sm" placeholder="https:// atau /nama-rute" value="/">
                        </div>
                        <div class="mb-3">
                            <label class="form-label small fw-bold text-dark">Teks Label Menu</label>
                            <input type="text" id="custom-label" class="form-control form-control-sm" placeholder="Contoh: Berita Terkini">
                        </div>
                        <div class="mb-3">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="custom-target">
                                <label class="form-check-label small text-muted" for="custom-target">
                                    Buka di tab baru (target="_blank")
                                </label>
                            </div>
                        </div>
                        <button type="button" class="btn btn-outline-primary btn-sm rounded-pill w-100" id="btn-add-custom">
                            <i class="bi bi-plus-circle me-1"></i> Tambahkan Tautan Kustom
                        </button>
                    </div>
                </div>
            </div>

            <!-- KOLOM KANAN: STRUKTUR MENU DRAG & DROP -->
            <div class="col-lg-8">
                <div class="card border-0 shadow-sm rounded-4 bg-white">
                    <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                        <!-- Nav Tabs -->
                        <ul class="nav nav-pills card-header-pills" id="menuTabs" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active px-3 py-1 rounded-pill small fw-bold" id="header-tab" data-bs-toggle="tab" data-bs-target="#header-tab-pane" type="button" role="tab">
                                    <i class="bi bi-compass me-1"></i> Menu Header (Navbar Utama)
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link px-3 py-1 rounded-pill small fw-bold" id="footer-tab" data-bs-toggle="tab" data-bs-target="#footer-tab-pane" type="button" role="tab">
                                    <i class="bi bi-layout-text-window me-1"></i> Menu Footer (Tautan Bawah)
                                </button>
                            </li>
                        </ul>
                    </div>

                    <div class="card-body p-4">
                        <div class="tab-content" id="menuTabsContent">
                            <!-- TAB HEADER MENU -->
                            <div class="tab-pane fade show active" id="header-tab-pane" role="tabpanel">
                                <p class="text-muted small mb-3">
                                    Tarik dan lepas item di bawah untuk mengubah urutan navbar utama di bagian atas website.
                                </p>

                                <div class="list-group gap-2" id="header-sortable-list">
                                    @foreach($headerMenu as $item)
                                        <div class="list-group-item border rounded-3 p-3 d-flex align-items-center justify-content-between gap-3 menu-item" data-label="{{ $item['label'] }}" data-url="{{ $item['url'] }}" data-target="{{ $item['target'] ?? '_self' }}">
                                            <div class="d-flex align-items-center gap-3 flex-grow-1">
                                                <div class="cursor-grab text-muted drag-handle border rounded-2 px-2 py-1 bg-light small" title="Tarik untuk memindahkan urutan">
                                                    <i class="bi bi-grip-vertical"></i> Geser
                                                </div>
                                                <div class="flex-grow-1">
                                                    <div class="fw-bold text-dark item-label-display">{{ $item['label'] }}</div>
                                                    <small class="text-muted font-monospace item-url-display">{{ $item['url'] }}</small>
                                                    @if(($item['target'] ?? '_self') === '_blank')
                                                        <span class="badge bg-secondary bg-opacity-25 text-dark ms-1 item-target-badge" style="font-size: 0.65rem;">Tab Baru</span>
                                                    @endif
                                                </div>
                                            </div>
                                            <div class="d-flex align-items-center gap-2">
                                                <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 btn-edit-item" title="Edit teks label atau tautan ini">
                                                    <i class="bi bi-pencil-square me-1"></i> Edit
                                                </button>
                                                <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                                                    <i class="bi bi-trash me-1"></i> Hapus
                                                </button>
                                            </div>
                                        </div>
                                    @endforeach
                                </div>
                            </div>

                            <!-- TAB FOOTER MENU -->
                            <div class="tab-pane fade" id="footer-tab-pane" role="tabpanel">
                                <p class="text-muted small mb-3">
                                    Tarik dan lepas item di bawah untuk mengubah urutan tautan layanan pada bagian footer bawah website.
                                </p>

                                <div class="list-group gap-2" id="footer-sortable-list">
                                    @foreach($footerMenu as $item)
                                        <div class="list-group-item border rounded-3 p-3 d-flex align-items-center justify-content-between gap-3 menu-item" data-label="{{ $item['label'] }}" data-url="{{ $item['url'] }}" data-target="{{ $item['target'] ?? '_self' }}">
                                            <div class="d-flex align-items-center gap-3 flex-grow-1">
                                                <div class="cursor-grab text-muted drag-handle border rounded-2 px-2 py-1 bg-light small" title="Tarik untuk memindahkan urutan">
                                                    <i class="bi bi-grip-vertical"></i> Geser
                                                </div>
                                                <div class="flex-grow-1">
                                                    <div class="fw-bold text-dark item-label-display">{{ $item['label'] }}</div>
                                                    <small class="text-muted font-monospace item-url-display">{{ $item['url'] }}</small>
                                                    @if(($item['target'] ?? '_self') === '_blank')
                                                        <span class="badge bg-secondary bg-opacity-25 text-dark ms-1 item-target-badge" style="font-size: 0.65rem;">Tab Baru</span>
                                                    @endif
                                                </div>
                                            </div>
                                            <div class="d-flex align-items-center gap-2">
                                                <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 btn-edit-item" title="Edit teks label atau tautan ini">
                                                    <i class="bi bi-pencil-square me-1"></i> Edit
                                                </button>
                                                <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                                                    <i class="bi bi-trash me-1"></i> Hapus
                                                </button>
                                            </div>
                                        </div>
                                    @endforeach
                                </div>
                            </div>
                        </div>

                        <hr class="my-4">

                        <div class="d-flex justify-content-end">
                            <button type="submit" class="btn btn-brand rounded-pill px-5 shadow-sm">
                                <i class="bi bi-check-circle-fill me-2"></i> Simpan Susunan Menu
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </form>

    <!-- MODAL EDIT ITEM MENU (ALA WORDPRESS NAV-MENUS) -->
    <div class="modal fade" id="modalEditMenu" tabindex="-1" aria-labelledby="modalEditMenuLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border-0 shadow rounded-4">
                <div class="modal-header bg-light border-bottom py-3">
                    <h6 class="modal-title fw-bold text-dark mb-0" id="modalEditMenuLabel">
                        <i class="bi bi-pencil-square text-primary me-2"></i> Edit Item Menu Navigasi
                    </h6>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
                </div>
                <div class="modal-body p-4">
                    <div class="mb-3">
                        <label for="edit_menu_label" class="form-label small fw-bold text-dark">Label Teks Menu *</label>
                        <input type="text" class="form-control" id="edit_menu_label" placeholder="Contoh: Beranda, Layanan Kami, Kontak">
                        <div class="form-text small text-muted">Teks yang akan muncul dan terbaca oleh pengunjung di menu navigasi.</div>
                    </div>
                    <div class="mb-3">
                        <label for="edit_menu_url" class="form-label small fw-bold text-dark">URL / Tautan Tujuan *</label>
                        <input type="text" class="form-control font-monospace" id="edit_menu_url" placeholder="/nama-halaman atau https://...">
                        <div class="form-text small text-muted">Dapat berupa tautan lokal seperti <code>/layanan</code> atau URL lengkap <code>https://...</code></div>
                    </div>
                    <div class="form-check p-3 bg-light rounded-3 mt-3">
                        <input class="form-check-input" type="checkbox" id="edit_menu_target">
                        <label class="form-check-label small text-dark fw-medium" for="edit_menu_target">
                            Buka di tab baru browser (<code>target="_blank"</code>)
                        </label>
                    </div>
                </div>
                <div class="modal-footer bg-light border-top py-3">
                    <button type="button" class="btn btn-outline-secondary rounded-pill px-3 btn-sm" data-bs-dismiss="modal">
                        Batal
                    </button>
                    <button type="button" class="btn btn-primary rounded-pill px-4 btn-sm" id="btn-save-edit-menu">
                        <i class="bi bi-check2-circle me-1"></i> Simpan Perubahan
                    </button>
                </div>
            </div>
        </div>
    </div>

@endsection

@push('scripts')
<script src="https://cdn.jsdelivr.net/npm/sortablejs@1.15.2/Sortable.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const headerList = document.getElementById('header-sortable-list');
        const footerList = document.getElementById('footer-sortable-list');

        // Init SortableJS
        new Sortable(headerList, {
            handle: '.drag-handle',
            animation: 150,
            ghostClass: 'bg-primary-subtle'
        });

        new Sortable(footerList, {
            handle: '.drag-handle',
            animation: 150,
            ghostClass: 'bg-primary-subtle'
        });

        // Modal Edit References
        const editModalEl = document.getElementById('modalEditMenu');
        const editModal = new bootstrap.Modal(editModalEl);
        const editLabelInput = document.getElementById('edit_menu_label');
        const editUrlInput = document.getElementById('edit_menu_url');
        const editTargetInput = document.getElementById('edit_menu_target');
        let currentEditItem = null;

        // Pasang Event Listener (Edit & Remove) pada Elemen Menu
        function attachMenuItemEvents(item) {
            const editBtn = item.querySelector('.btn-edit-item');
            if (editBtn) {
                editBtn.addEventListener('click', function () {
                    currentEditItem = item;
                    editLabelInput.value = item.getAttribute('data-label') || '';
                    editUrlInput.value = item.getAttribute('data-url') || '';
                    editTargetInput.checked = (item.getAttribute('data-target') === '_blank');
                    editModal.show();
                });
            }

            const removeBtn = item.querySelector('.btn-remove-item');
            if (removeBtn) {
                removeBtn.addEventListener('click', function () {
                    item.remove();
                });
            }
        }

        // Simpan Perubahan dari Modal Edit
        document.getElementById('btn-save-edit-menu')?.addEventListener('click', function () {
            if (!currentEditItem) return;

            const newLabel = editLabelInput.value.trim();
            const newUrl = editUrlInput.value.trim();
            const isBlank = editTargetInput.checked;
            const newTarget = isBlank ? '_blank' : '_self';

            if (!newLabel || !newUrl) {
                alert('Silakan isi Label Teks Menu dan URL tujuan terlebih dahulu.');
                return;
            }

            // Update Atribut Data
            currentEditItem.setAttribute('data-label', newLabel);
            currentEditItem.setAttribute('data-url', newUrl);
            currentEditItem.setAttribute('data-target', newTarget);

            // Update Teks Label dan URL Tampilan
            const labelDisplay = currentEditItem.querySelector('.item-label-display');
            const urlDisplay = currentEditItem.querySelector('.item-url-display');
            if (labelDisplay) labelDisplay.textContent = newLabel;
            if (urlDisplay) urlDisplay.textContent = newUrl;

            // Update Badge "Tab Baru"
            let badge = currentEditItem.querySelector('.item-target-badge');
            if (isBlank) {
                if (!badge) {
                    badge = document.createElement('span');
                    badge.className = 'badge bg-secondary bg-opacity-25 text-dark ms-1 item-target-badge';
                    badge.style.fontSize = '0.65rem';
                    badge.textContent = 'Tab Baru';
                    labelDisplay.parentNode.appendChild(badge);
                }
            } else {
                if (badge) {
                    badge.remove();
                }
            }

            editModal.hide();
        });

        // Helper Buat Elemen Menu Baru
        function createMenuItem(label, url, target) {
            const div = document.createElement('div');
            div.className = 'list-group-item border rounded-3 p-3 d-flex align-items-center justify-content-between gap-3 menu-item';
            div.setAttribute('data-label', label);
            div.setAttribute('data-url', url);
            div.setAttribute('data-target', target);

            div.innerHTML = `
                <div class="d-flex align-items-center gap-3 flex-grow-1">
                    <div class="cursor-grab text-muted drag-handle border rounded-2 px-2 py-1 bg-light small" title="Tarik untuk memindahkan urutan">
                        <i class="bi bi-grip-vertical"></i> Geser
                    </div>
                    <div class="flex-grow-1">
                        <div class="fw-bold text-dark item-label-display">${label}</div>
                        <small class="text-muted font-monospace item-url-display">${url}</small>
                        ${target === '_blank' ? '<span class="badge bg-secondary bg-opacity-25 text-dark ms-1 item-target-badge" style="font-size: 0.65rem;">Tab Baru</span>' : ''}
                    </div>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 btn-edit-item" title="Edit teks label atau tautan ini">
                        <i class="bi bi-pencil-square me-1"></i> Edit
                    </button>
                    <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                        <i class="bi bi-trash me-1"></i> Hapus
                    </button>
                </div>
            `;

            attachMenuItemEvents(div);
            return div;
        }

        // Attach event listener untuk seluruh item yang ada saat halaman dimuat
        document.querySelectorAll('.menu-item').forEach(item => {
            attachMenuItemEvents(item);
        });

        // Dapatkan target list aktif (Header atau Footer)
        function getActiveList() {
            const activeTab = document.querySelector('#menuTabs .nav-link.active');
            if (activeTab && activeTab.id === 'footer-tab') {
                return footerList;
            }
            return headerList;
        }

        // Tambah dari checkbox halaman
        document.getElementById('btn-add-pages')?.addEventListener('click', function () {
            const checkedPages = document.querySelectorAll('.page-checkbox:checked');
            const targetList = getActiveList();

            checkedPages.forEach(cb => {
                const label = cb.value;
                const url = cb.getAttribute('data-url');
                const item = createMenuItem(label, url, '_self');
                targetList.appendChild(item);
                cb.checked = false;
            });
        });

        // Tambah dari custom link
        document.getElementById('btn-add-custom')?.addEventListener('click', function () {
            const urlInput = document.getElementById('custom-url');
            const labelInput = document.getElementById('custom-label');
            const targetInput = document.getElementById('custom-target');

            const url = urlInput.value.trim();
            const label = labelInput.value.trim();
            const target = targetInput.checked ? '_blank' : '_self';

            if (!url || !label) {
                alert('Silakan isi URL dan Teks Label terlebih dahulu.');
                return;
            }

            const targetList = getActiveList();
            const item = createMenuItem(label, url, target);
            targetList.appendChild(item);

            urlInput.value = '/';
            labelInput.value = '';
            targetInput.checked = false;
        });

        // Sebelum submit form, serap seluruh item menjadi JSON string
        document.getElementById('menu-form').addEventListener('submit', function (e) {
            const headerItems = [];
            headerList.querySelectorAll('.menu-item').forEach(item => {
                headerItems.push({
                    label: item.getAttribute('data-label'),
                    url: item.getAttribute('data-url'),
                    target: item.getAttribute('data-target') || '_self'
                });
            });

            const footerItems = [];
            footerList.querySelectorAll('.menu-item').forEach(item => {
                footerItems.push({
                    label: item.getAttribute('data-label'),
                    url: item.getAttribute('data-url'),
                    target: item.getAttribute('data-target') || '_self'
                });
            });

            document.getElementById('header_menu_input').value = JSON.stringify(headerItems);
            document.getElementById('footer_menu_input').value = JSON.stringify(footerItems);
        });
    });
</script>
<style>
    .cursor-grab {
        cursor: grab;
    }
    .cursor-grab:active {
        cursor: grabbing;
    }
</style>
@endpush
