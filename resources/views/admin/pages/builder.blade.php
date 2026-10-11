<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>Visual Drag & Drop Canvas: {{ $page->title }} | Aktama Builder</title>

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="{{ asset('images/logo-aktama.png') }}">

    <!-- Bootstrap 5.3 CSS & Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

    <!-- GrapesJS Core CSS -->
    <link rel="stylesheet" href="https://unpkg.com/grapesjs@0.21.10/dist/css/grapes.min.css">

    <style>
        body, html {
            height: 100%;
            margin: 0;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #1e293b;
        }

        #builder-header {
            height: 56px;
            background-color: #0f172a;
            border-bottom: 1px solid #334155;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 1rem;
            color: #ffffff;
            z-index: 1050;
        }

        #gjs {
            height: calc(100vh - 56px);
            border: none;
        }

        /* GrapesJS UI Theme Tweaks */
        .gjs-one-bg {
            background-color: #1e293b;
        }
        .gjs-two-color {
            color: #94a3b8;
        }
        .gjs-three-bg {
            background-color: #334155;
            color: #fff;
        }
        .gjs-four-color, .gjs-four-color-h:hover {
            color: #6366f1;
        }
        .gjs-block {
            border-radius: 6px;
            padding: 10px 8px;
            font-size: 11px;
            font-weight: 500;
            text-align: center;
            border: 1px solid #334155;
            background: #0f172a;
            color: #e2e8f0;
            transition: all 0.15s ease-in-out;
            min-height: 70px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 4px;
        }
        .gjs-block:hover {
            border-color: #6366f1;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25);
            transform: translateY(-2px);
        }
        .gjs-block i {
            font-size: 20px;
            margin-bottom: 2px;
            color: #818cf8;
        }
    </style>
</head>
<body>

    <!-- TOP BUILDER NAVBAR -->
    <header id="builder-header">
        <div class="d-flex align-items-center gap-3">
            <a href="{{ route('admin.pages.index') }}" class="btn btn-sm btn-outline-secondary text-white rounded-pill px-3" title="Kembali ke Panel Admin">
                <i class="bi bi-arrow-left me-1"></i> Kembali
            </a>
            <div class="vr bg-secondary opacity-50 d-none d-sm-block"></div>
            <div>
                <strong class="text-white d-block text-truncate" style="max-width: 280px;">{{ $page->title }}</strong>
                <small class="text-secondary" style="font-size: 0.7rem;">
                    <i class="bi bi-brush text-primary me-1"></i> Opsi B: Visual Canvas
                </small>
            </div>
        </div>

        <!-- DEVICE PREVIEW SWITCHER -->
        <div class="btn-group btn-group-sm bg-dark p-1 rounded-pill border border-secondary border-opacity-50" role="group">
            <button type="button" class="btn btn-sm text-white px-3 rounded-pill active" id="btn-desktop" title="Tampilan Desktop">
                <i class="bi bi-display"></i> Desktop
            </button>
            <button type="button" class="btn btn-sm text-white-50 px-3 rounded-pill" id="btn-tablet" title="Tampilan Tablet">
                <i class="bi bi-tablet"></i> Tablet
            </button>
            <button type="button" class="btn btn-sm text-white-50 px-3 rounded-pill" id="btn-mobile" title="Tampilan Smartphone">
                <i class="bi bi-phone"></i> Mobile
            </button>
        </div>

        <!-- ACTION BUTTONS -->
        <div class="d-flex align-items-center gap-2">
            <a href="{{ route('pages.show', $page->slug) }}" target="_blank" class="btn btn-sm btn-outline-light rounded-pill px-3" title="Lihat Hasil di Tab Baru">
                <i class="bi bi-box-arrow-up-right me-1"></i> Lihat Publik
            </a>

            <button type="button" class="btn btn-sm btn-primary rounded-pill px-4 shadow-sm" id="btn-save-builder">
                <span id="save-spinner" class="spinner-border spinner-border-sm me-1 d-none" role="status" aria-hidden="true"></span>
                <i class="bi bi-check2-circle me-1" id="save-icon"></i> <span id="save-label">Simpan Desain</span>
            </button>
        </div>
    </header>

    <!-- GRAPESJS CONTAINER -->
    <div id="gjs"></div>

    <!-- TOAST NOTIFIKASI -->
    <div class="toast-container position-fixed bottom-0 end-0 p-3" style="z-index: 9999;">
        <div id="saveToast" class="toast align-items-center text-bg-success border-0 shadow-lg" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="bi bi-check-circle-fill me-2 fs-6"></i> <span id="toast-message">Perubahan visual berhasil disimpan ke database!</span>
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <!-- GrapesJS Core JS -->
    <script src="https://unpkg.com/grapesjs@0.21.10/dist/grapes.min.js"></script>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // Inisialisasi GrapesJS
            const editor = grapesjs.init({
                container: '#gjs',
                fromElement: false,
                height: 'calc(100vh - 56px)',
                width: 'auto',
                storageManager: false, // Disimpan manual via AJAX
                canvas: {
                    styles: [
                        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
                        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
                        'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap'
                    ],
                    scripts: [
                        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'
                    ]
                },
                deviceManager: {
                    devices: [
                        { name: 'Desktop', width: '' },
                        { name: 'Tablet', width: '768px', widthMedia: '992px' },
                        { name: 'Mobile', width: '375px', widthMedia: '480px' }
                    ]
                },
                blockManager: {
                    appendTo: '', // Default panel
                }
            });

            // 1. TAMBAHKAN BLOK-BLOK BOOTSTRAP 5 SIAP PAKAI
            const bm = editor.BlockManager;

            // Kategori: Seksi & Tata Letak
            bm.add('hero-section', {
                label: '<i class="bi bi-card-heading"></i><span>Hero Banner</span>',
                category: 'Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-light text-center border-bottom">
                        <div class="container py-4">
                            <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-3">Layanan Unggulan</span>
                            <h1 class="display-5 fw-bold text-dark mb-3">Judul Utama Halaman Kustom</h1>
                            <p class="lead text-muted mb-4 mx-auto" style="max-width: 650px;">
                                Tuliskan kalimat pengantar yang menarik dan informatif untuk menjelaskan layanan atau informasi penting Anda.
                            </p>
                            <div class="d-flex justify-content-center gap-3">
                                <a href="#mulai" class="btn btn-primary rounded-pill px-4 py-2">Mulai Sekarang</a>
                                <a href="#pelajari" class="btn btn-outline-secondary rounded-pill px-4 py-2">Pelajari Lebih Lanjut</a>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('features-3col', {
                label: '<i class="bi bi-columns-gap"></i><span>3 Kolom Fitur</span>',
                category: 'Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-white">
                        <div class="container">
                            <div class="row g-4">
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm text-center">
                                        <div class="p-3 bg-primary bg-opacity-10 text-primary rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                            <i class="bi bi-shield-check"></i>
                                        </div>
                                        <h5 class="fw-bold text-dark mb-2">Keamanan Terjamin</h5>
                                        <p class="text-muted small mb-0">Proteksi data tingkat tinggi yang menjaga kerahasiaan informasi bisnis Anda.</p>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm text-center">
                                        <div class="p-3 bg-success bg-opacity-10 text-success rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                            <i class="bi bi-lightning-charge"></i>
                                        </div>
                                        <h5 class="fw-bold text-dark mb-2">Kinerja Super Cepat</h5>
                                        <p class="text-muted small mb-0">Arsitektur bersih dan teroptimasi menghasilkan waktu muat yang instan.</p>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm text-center">
                                        <div class="p-3 bg-warning bg-opacity-10 text-warning rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                            <i class="bi bi-award"></i>
                                        </div>
                                        <h5 class="fw-bold text-dark mb-2">Standar Kualitas</h5>
                                        <p class="text-muted small mb-0">Didukung instruktur dan praktisi berpengalaman bersertifikasi resmi.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('media-text', {
                label: '<i class="bi bi-layout-sidebar"></i><span>Media & Teks (2 Kolom)</span>',
                category: 'Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-light">
                        <div class="container">
                            <div class="row align-items-center g-5">
                                <div class="col-lg-6">
                                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80" alt="Kolaborasi Tim" class="img-fluid rounded-4 shadow">
                                </div>
                                <div class="col-lg-6">
                                    <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-2">Tentang Kami</span>
                                    <h2 class="fw-bold text-dark mb-3">Membangun Solusi dengan Komitmen Nyata</h2>
                                    <p class="text-muted mb-4 leading-relaxed">
                                        Kami menghadirkan sinergi antara rekayasa perangkat lunak modern dan transfer ilmu pengetahuan untuk mendongkrak performa digital organisasi Anda.
                                    </p>
                                    <ul class="list-unstyled space-y-2 mb-4">
                                        <li class="mb-2"><i class="bi bi-check-circle-fill text-primary me-2"></i> Implementasi sesuai kebutuhan nyata</li>
                                        <li class="mb-2"><i class="bi bi-check-circle-fill text-primary me-2"></i> Pendampingan teknis berkelanjutan</li>
                                        <li class="mb-2"><i class="bi bi-check-circle-fill text-primary me-2"></i> Legalitas badan usaha resmi & terpercaya</li>
                                    </ul>
                                    <a href="#hubungi" class="btn btn-primary rounded-pill px-4">Hubungi Kami</a>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('cta-banner', {
                label: '<i class="bi bi-megaphone"></i><span>Call to Action (CTA)</span>',
                category: 'Seksi Siap Pakai',
                content: `
                    <section class="py-5 text-white" style="background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);">
                        <div class="container py-4 text-center">
                            <h2 class="display-6 fw-bold mb-3">Siap Mengembangkan Ekosistem Bisnis Anda?</h2>
                            <p class="lead text-white-50 mb-4 mx-auto" style="max-width: 600px;">
                                Diskusikan kebutuhan spesifik Anda bersama praktisi kami dan dapatkan penawaran terbaik.
                            </p>
                            <a href="https://wa.me/6281234567890" target="_blank" class="btn btn-light text-primary btn-lg rounded-pill px-5 fw-bold shadow">
                                <i class="bi bi-whatsapp me-2 text-success"></i> Hubungi WhatsApp Resmi
                            </a>
                        </div>
                    </section>
                `
            });

            bm.add('pricing-card', {
                label: '<i class="bi bi-tags"></i><span>Tabel Harga</span>',
                category: 'Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-white">
                        <div class="container">
                            <div class="row justify-content-center">
                                <div class="col-md-6 col-lg-4">
                                    <div class="card p-4 border rounded-4 shadow-sm text-center">
                                        <h5 class="fw-bold text-dark mb-1">Paket Standar</h5>
                                        <p class="text-muted small mb-3">Pilihan tepat untuk kebutuhan awal</p>
                                        <div class="fs-2 fw-bold text-primary mb-3">Rp 1.500.000</div>
                                        <ul class="list-unstyled small text-muted text-start border-top pt-3 mb-4">
                                            <li class="mb-2"><i class="bi bi-check2 text-success me-2"></i> Domain & Server Hosting</li>
                                            <li class="mb-2"><i class="bi bi-check2 text-success me-2"></i> 3 - 5 Halaman Konten</li>
                                            <li class="mb-2"><i class="bi bi-check2 text-success me-2"></i> Integrasi WhatsApp Bisnis</li>
                                            <li class="mb-2"><i class="bi bi-check2 text-success me-2"></i> Bantuan Input Data</li>
                                        </ul>
                                        <a href="#pilih" class="btn btn-primary rounded-pill w-100">Pilih Paket Ini</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            // Kategori: Elemen Dasar
            bm.add('text-heading', {
                label: '<i class="bi bi-type-h1"></i><span>Heading Teks</span>',
                category: 'Elemen Dasar',
                content: '<h2 class="fw-bold text-dark mb-3">Tuliskan Judul Heading</h2>'
            });

            bm.add('text-paragraph', {
                label: '<i class="bi bi-body-text"></i><span>Paragraf Teks</span>',
                category: 'Elemen Dasar',
                content: '<p class="text-muted leading-relaxed">Tuliskan paragraf teks penjelasan di sini. Anda dapat mengatur tebal, miring, serta tautan langsung dari editor.</p>'
            });

            bm.add('button-element', {
                label: '<i class="bi bi-cursor"></i><span>Tombol Aksi</span>',
                category: 'Elemen Dasar',
                content: '<a href="#" class="btn btn-primary rounded-pill px-4 py-2">Klik Di Sini</a>'
            });

            bm.add('image-element', {
                label: '<i class="bi bi-image"></i><span>Gambar Foto</span>',
                category: 'Elemen Dasar',
                content: '<img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=700&q=80" class="img-fluid rounded-3 shadow-sm" alt="Ilustrasi">'
            });

            bm.add('card-box', {
                label: '<i class="bi bi-square"></i><span>Card Container</span>',
                category: 'Elemen Dasar',
                content: `
                    <div class="card border rounded-4 p-4 shadow-sm bg-white mb-3">
                        <h5 class="fw-bold text-dark">Judul Kotak Konten</h5>
                        <p class="text-muted mb-0">Isi penjelasan singkat di dalam kotak card.</p>
                    </div>
                `
            });

            // 2. MUAT KONTEN TERSIMPAN DARI DATABASE
            @if(!empty($page->content_json))
                try {
                    const savedComponents = {!! json_encode($page->content_json) !!};
                    if (savedComponents) {
                        editor.setComponents(JSON.parse(savedComponents));
                    }
                } catch (e) {
                    console.warn('Fallback parsing JSON components:', e);
                    editor.setComponents({!! json_encode($page->content_html) !!});
                }
            @elseif(!empty($page->content_html))
                editor.setComponents({!! json_encode($page->content_html) !!});
            @else
                editor.setComponents(`
                    <div class="py-5 text-center">
                        <h2 class="fw-bold font-display text-dark">{{ $page->title }}</h2>
                        <p class="lead text-muted">Seret dan letakkan blok komponen dari panel samping kanan untuk mulai merancang halaman ini.</p>
                    </div>
                `);
            @endif

            @if(!empty($page->content_css))
                editor.setStyle({!! json_encode($page->content_css) !!});
            @endif

            // 3. PENGATUR SWITCH DEVICE
            const btnDesktop = document.getElementById('btn-desktop');
            const btnTablet = document.getElementById('btn-tablet');
            const btnMobile = document.getElementById('btn-mobile');

            function setActiveDevice(btn, deviceName) {
                [btnDesktop, btnTablet, btnMobile].forEach(b => {
                    b.classList.remove('active', 'text-white');
                    b.classList.add('text-white-50');
                });
                btn.classList.add('active', 'text-white');
                btn.classList.remove('text-white-50');
                editor.setDevice(deviceName);
            }

            btnDesktop.addEventListener('click', () => setActiveDevice(btnDesktop, 'Desktop'));
            btnTablet.addEventListener('click', () => setActiveDevice(btnTablet, 'Tablet'));
            btnMobile.addEventListener('click', () => setActiveDevice(btnMobile, 'Mobile'));

            // 4. AJAX PENYIMPANAN
            const btnSave = document.getElementById('btn-save-builder');
            const saveSpinner = document.getElementById('save-spinner');
            const saveIcon = document.getElementById('save-icon');
            const saveLabel = document.getElementById('save-label');
            const toastEl = document.getElementById('saveToast');
            const toastMsg = document.getElementById('toast-message');
            const toast = new bootstrap.Toast(toastEl);

            btnSave.addEventListener('click', function () {
                // UI Loading
                saveSpinner.classList.remove('d-none');
                saveIcon.classList.add('d-none');
                saveLabel.innerText = 'Menyimpan...';
                btnSave.disabled = true;

                const htmlContent = editor.getHtml();
                const cssContent = editor.getCss();
                const jsonComponents = JSON.stringify(editor.getComponents());

                fetch("{{ route('admin.pages.saveBuilder', $page->id) }}", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                    },
                    body: JSON.stringify({
                        html: htmlContent,
                        css: cssContent,
                        components: jsonComponents
                    })
                })
                .then(res => res.json())
                .then(data => {
                    saveSpinner.classList.add('d-none');
                    saveIcon.classList.remove('d-none');
                    saveLabel.innerText = 'Simpan Desain';
                    btnSave.disabled = false;

                    toastMsg.innerText = data.message || 'Desain halaman visual berhasil disimpan!';
                    toast.show();
                })
                .catch(err => {
                    console.error('Save error:', err);
                    saveSpinner.classList.add('d-none');
                    saveIcon.classList.remove('d-none');
                    saveLabel.innerText = 'Simpan Desain';
                    btnSave.disabled = false;
                    alert('Gagal menyimpan desain halaman. Silakan periksa koneksi Anda.');
                });
            });
        });
    </script>
</body>
</html>
