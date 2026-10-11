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
                                                        <span class="badge bg-secondary bg-opacity-25 text-dark ms-1" style="font-size: 0.65rem;">Tab Baru</span>
                                                    @endif
                                                </div>
                                            </div>
                                            <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                                                <i class="bi bi-trash me-1"></i> Hapus
                                            </button>
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
                                                        <span class="badge bg-secondary bg-opacity-25 text-dark ms-1" style="font-size: 0.65rem;">Tab Baru</span>
                                                    @endif
                                                </div>
                                            </div>
                                            <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                                                <i class="bi bi-trash me-1"></i> Hapus
                                            </button>
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

        // Helper Buat Elemen Menu
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
                        ${target === '_blank' ? '<span class="badge bg-secondary bg-opacity-25 text-dark ms-1" style="font-size: 0.65rem;">Tab Baru</span>' : ''}
                    </div>
                </div>
                <button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-3 btn-remove-item" title="Hapus dari menu">
                    <i class="bi bi-trash me-1"></i> Hapus
                </button>
            `;

            div.querySelector('.btn-remove-item').addEventListener('click', function () {
                div.remove();
            });

            return div;
        }

        // Attach event delete untuk item awal
        document.querySelectorAll('.btn-remove-item').forEach(btn => {
            btn.addEventListener('click', function () {
                btn.closest('.menu-item').remove();
            });
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
