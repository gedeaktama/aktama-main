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
            <button type="button" class="btn btn-sm btn-outline-info rounded-pill px-3" data-bs-toggle="modal" data-bs-target="#modalHelpBuilder" title="Petunjuk Cara Mendesain">
                <i class="bi bi-question-circle me-1"></i> Cara Pakai
            </button>

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

    <!-- MODAL PANDUAN CARA DESAIN ALA ELEMENTOR -->
    <div class="modal fade" id="modalHelpBuilder" tabindex="-1" aria-labelledby="modalHelpBuilderLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
                <div class="modal-header bg-dark text-white py-3 px-4">
                    <h6 class="modal-title fw-bold mb-0" id="modalHelpBuilderLabel">
                        <i class="bi bi-magic text-warning me-2"></i> Panduan Desain Halaman Visual (Elementor Style)
                    </h6>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Tutup"></button>
                </div>
                <div class="modal-body p-4 bg-white">
                    <div class="row g-3">
                        <div class="col-md-6">
                            <div class="p-3 rounded-3 bg-light border h-100">
                                <h6 class="fw-bold text-dark"><i class="bi bi-arrows-move text-primary me-2"></i> 1. Drag & Drop Blok</h6>
                                <p class="text-muted small mb-0">
                                    Di panel samping kanan, klik tab <strong>Blocks</strong> (ikon kotak 4). Seret dan letakkan blok siap pakai (Hero, Fitur, Testimoni, FAQ) ke kanvas tengah.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 rounded-3 bg-light border h-100">
                                <h6 class="fw-bold text-dark"><i class="bi bi-pencil-square text-success me-2"></i> 2. Edit Teks Langsung</h6>
                                <p class="text-muted small mb-0">
                                    <strong>Klik dua kali (double click)</strong> pada teks apa saja di kanvas untuk langsung mengetik kalimat baru secara visual.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 rounded-3 bg-light border h-100">
                                <h6 class="fw-bold text-dark"><i class="bi bi-gear-fill text-warning me-2"></i> 3. Ubah Link & Gambar</h6>
                                <p class="text-muted small mb-0">
                                    Klik tombol atau gambar, lalu pada panel kanan atas klik ikon <strong>Gerigi (Settings)</strong> untuk mengganti link URL tujuan atau alamat foto.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 rounded-3 bg-light border h-100">
                                <h6 class="fw-bold text-dark"><i class="bi bi-phone text-info me-2"></i> 4. Pratinjau Mobile & Simpan</h6>
                                <p class="text-muted small mb-0">
                                    Ganti mode tampilan ke Tablet/Mobile pada tombol bilah atas. Setelah selesai, klik tombol biru <strong>"Simpan Desain"</strong>.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer bg-light border-top py-3 px-4">
                    <button type="button" class="btn btn-primary rounded-pill px-4 btn-sm" data-bs-dismiss="modal">
                        <i class="bi bi-check-circle me-1"></i> Saya Mengerti, Mulai Mendesain
                    </button>
                </div>
            </div>
        </div>
    </div>

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

            // Buka tab Blok (Blocks) secara otomatis begitu editor selesai dimuat (seperti Elementor)
            editor.on('load', function () {
                const openBlocksBtn = editor.Panels.getButton('views', 'open-blocks');
                if (openBlocksBtn) {
                    openBlocksBtn.set('active', true);
                }
            });

            // 1. TAMBAHKAN BLOK-BLOK BOOTSTRAP 5 SIAP PAKAI (ALA ELEMENTOR)
            const bm = editor.BlockManager;

            // KATEGORI 1: ⭐ TEMPLATE HALAMAN LENGKAP (1-CLICK TEMPLATE)
            bm.add('full-landing-page', {
                label: '<i class="bi bi-star-fill text-warning"></i><span>Landing Page Lengkap</span>',
                category: '⭐ Template Siap Pakai',
                content: `
                    <div class="aktama-landing-template">
                        <!-- Hero Banner -->
                        <section class="py-5 text-center bg-light border-bottom position-relative overflow-hidden">
                            <div class="container py-4">
                                <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-3 fw-semibold">
                                    <i class="bi bi-shield-check me-1"></i> Solusi Rekayasa Digital & Pelatihan AI
                                </span>
                                <h1 class="display-4 fw-extrabold text-dark mb-3 tracking-tight">
                                    Kembangkan Potensi Organisasi Anda Bersama <span class="text-primary">Aktama Digital</span>
                                </h1>
                                <p class="lead text-muted mb-4 mx-auto" style="max-width: 680px;">
                                    Mitra terpercaya penyedia rekayasa perangkat lunak berstandar keamanan tinggi bebas malware dan pelatihan kecerdasan artifisial (AI) terapan berlisensi resmi.
                                </p>
                                <div class="d-flex justify-content-center gap-3 flex-wrap">
                                    <a href="https://wa.me/6285341026331" target="_blank" class="btn btn-primary btn-lg rounded-pill px-4 shadow-sm">
                                        <i class="bi bi-whatsapp me-2"></i> Konsultasi WhatsApp
                                    </a>
                                    <a href="#fitur-unggulan" class="btn btn-outline-dark btn-lg rounded-pill px-4">
                                        Jelajahi Layanan
                                    </a>
                                </div>
                            </div>
                        </section>

                        <!-- 3 Kolom Fitur -->
                        <section id="fitur-unggulan" class="py-5 bg-white">
                            <div class="container py-3">
                                <div class="row g-4 text-center">
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="p-3 bg-primary bg-opacity-10 text-primary rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                                <i class="bi bi-shield-check"></i>
                                            </div>
                                            <h5 class="fw-bold text-dark mb-2">Keamanan Terjamin</h5>
                                            <p class="text-muted small mb-0">Arsitektur steril dari risiko serangan peretasan dan injeksi skrip malware.</p>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="p-3 bg-success bg-opacity-10 text-success rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                                <i class="bi bi-lightning-charge"></i>
                                            </div>
                                            <h5 class="fw-bold text-dark mb-2">Kinerja Cepat & Ringan</h5>
                                            <p class="text-muted small mb-0">Waktu muat instan tanpa ketergantungan plugin berat pihak ketiga.</p>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="p-3 bg-warning bg-opacity-10 text-warning rounded-circle d-inline-flex mx-auto mb-3 fs-3">
                                                <i class="bi bi-award"></i>
                                            </div>
                                            <h5 class="fw-bold text-dark mb-2">Instruktur Bersertifikasi</h5>
                                            <p class="text-muted small mb-0">Dibimbing langsung oleh Fasilitator Nasional dan praktisi berpengalaman.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- 4 Statistik Pencapaian -->
                        <section class="py-5 bg-light border-top border-bottom">
                            <div class="container text-center">
                                <div class="row g-4">
                                    <div class="col-6 col-md-3">
                                        <div class="display-6 fw-bold text-primary mb-1">100+</div>
                                        <div class="text-muted small">Implementasi Sistem</div>
                                    </div>
                                    <div class="col-6 col-md-3">
                                        <div class="display-6 fw-bold text-success mb-1">500+</div>
                                        <div class="text-muted small">Alumni Pelatihan LPK</div>
                                    </div>
                                    <div class="col-6 col-md-3">
                                        <div class="display-6 fw-bold text-warning mb-1">99.8%</div>
                                        <div class="text-muted small">Tingkat Kepuasan Mitra</div>
                                    </div>
                                    <div class="col-6 col-md-3">
                                        <div class="display-6 fw-bold text-info mb-1">24/7</div>
                                        <div class="text-muted small">Pendampingan Teknis</div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Testimoni Klien -->
                        <section class="py-5 bg-white">
                            <div class="container py-3">
                                <div class="text-center mb-5">
                                    <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-2">Testimoni</span>
                                    <h2 class="fw-bold text-dark">Apa Kata Mitra Kami</h2>
                                </div>
                                <div class="row g-4">
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="text-warning mb-3 fs-5">★★★★★</div>
                                            <p class="text-muted small mb-4">"Aplikasi yang dibangun sangat rapi, andal, dan staf kami sangat terbantu dengan sistem pelatihan yang diberikan."</p>
                                            <div class="d-flex align-items-center gap-3 mt-auto">
                                                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                                <div>
                                                    <div class="fw-bold text-dark small">Dewi Lestari</div>
                                                    <div class="text-muted" style="font-size: 0.72rem;">Kepala Bagian IT</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="text-warning mb-3 fs-5">★★★★★</div>
                                            <p class="text-muted small mb-4">"Pelatihan kecerdasan artifisialnya sangat praktis dan langsung dapat diaplikasikan pada pekerjaan sehari-hari."</p>
                                            <div class="d-flex align-items-center gap-3 mt-auto">
                                                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                                <div>
                                                    <div class="fw-bold text-dark small">Budi Pratama</div>
                                                    <div class="text-muted" style="font-size: 0.72rem;">Manajer Operasional</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                            <div class="text-warning mb-3 fs-5">★★★★★</div>
                                            <p class="text-muted small mb-4">"Respon cepat dan komitmen profesional yang luar biasa. Sangat kami rekomendasikan untuk instansi maupun swasta."</p>
                                            <div class="d-flex align-items-center gap-3 mt-auto">
                                                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                                <div>
                                                    <div class="fw-bold text-dark small">Siti Rahma</div>
                                                    <div class="text-muted" style="font-size: 0.72rem;">Direktur Lembaga</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Call to Action Banner WhatsApp -->
                        <section class="py-5 text-white text-center" style="background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);">
                            <div class="container py-4">
                                <h2 class="display-6 fw-bold mb-3">Siap Memulai Transformasi Digital?</h2>
                                <p class="lead text-white-50 mb-4 mx-auto" style="max-width: 600px;">
                                    Diskusikan kebutuhan spesifik Anda bersama praktisi kami dan dapatkan penawaran solusi terbaik.
                                </p>
                                <a href="https://wa.me/6285341026331" target="_blank" class="btn btn-light btn-lg rounded-pill px-5 fw-bold shadow text-dark">
                                    <i class="bi bi-whatsapp text-success me-2"></i> Hubungi WhatsApp Resmi
                                </a>
                            </div>
                        </section>
                    </div>
                `
            });

            // KATEGORI 2: 📐 TATA LETAK & GRID (CONTAINER ALA ELEMENTOR)
            bm.add('grid-1col', {
                label: '<i class="bi bi-square"></i><span>1 Kolom Penuh</span>',
                category: '📐 Tata Letak & Grid',
                content: `
                    <div class="py-4">
                        <div class="container">
                            <div class="p-4 border rounded-3 bg-white shadow-xs">
                                <p class="text-muted mb-0">Isi konten kontainer 1 kolom di sini.</p>
                            </div>
                        </div>
                    </div>
                `
            });

            bm.add('grid-2col', {
                label: '<i class="bi bi-layout-split"></i><span>2 Kolom (50/50)</span>',
                category: '📐 Tata Letak & Grid',
                content: `
                    <div class="py-4">
                        <div class="container">
                            <div class="row g-4">
                                <div class="col-md-6">
                                    <div class="p-4 border rounded-3 bg-white h-100 shadow-xs">
                                        <h5 class="fw-bold text-dark">Kolom Kiri</h5>
                                        <p class="text-muted small mb-0">Tuliskan konten kolom pertama di sini.</p>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="p-4 border rounded-3 bg-white h-100 shadow-xs">
                                        <h5 class="fw-bold text-dark">Kolom Kanan</h5>
                                        <p class="text-muted small mb-0">Tuliskan konten kolom kedua di sini.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            });

            bm.add('grid-3col', {
                label: '<i class="bi bi-columns-gap"></i><span>3 Kolom Rata</span>',
                category: '📐 Tata Letak & Grid',
                content: `
                    <div class="py-4">
                        <div class="container">
                            <div class="row g-4">
                                <div class="col-md-4">
                                    <div class="p-4 border rounded-3 bg-white h-100 shadow-xs">
                                        <h6 class="fw-bold text-dark">Kolom 1</h6>
                                        <p class="text-muted small mb-0">Konten kolom pertama.</p>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="p-4 border rounded-3 bg-white h-100 shadow-xs">
                                        <h6 class="fw-bold text-dark">Kolom 2</h6>
                                        <p class="text-muted small mb-0">Konten kolom kedua.</p>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="p-4 border rounded-3 bg-white h-100 shadow-xs">
                                        <h6 class="fw-bold text-dark">Kolom 3</h6>
                                        <p class="text-muted small mb-0">Konten kolom ketiga.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            });

            bm.add('grid-4col', {
                label: '<i class="bi bi-grid-3x3-gap"></i><span>4 Kolom Rata</span>',
                category: '📐 Tata Letak & Grid',
                content: `
                    <div class="py-4">
                        <div class="container">
                            <div class="row g-3">
                                <div class="col-6 col-md-3">
                                    <div class="p-3 border rounded-3 bg-white text-center h-100 shadow-xs">
                                        <strong class="d-block text-dark small">Kolom 1</strong>
                                        <span class="text-muted" style="font-size: 0.75rem;">Deskripsi singkat</span>
                                    </div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="p-3 border rounded-3 bg-white text-center h-100 shadow-xs">
                                        <strong class="d-block text-dark small">Kolom 2</strong>
                                        <span class="text-muted" style="font-size: 0.75rem;">Deskripsi singkat</span>
                                    </div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="p-3 border rounded-3 bg-white text-center h-100 shadow-xs">
                                        <strong class="d-block text-dark small">Kolom 3</strong>
                                        <span class="text-muted" style="font-size: 0.75rem;">Deskripsi singkat</span>
                                    </div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="p-3 border rounded-3 bg-white text-center h-100 shadow-xs">
                                        <strong class="d-block text-dark small">Kolom 4</strong>
                                        <span class="text-muted" style="font-size: 0.75rem;">Deskripsi singkat</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            });

            // KATEGORI 3: 🚀 SEKSI SIAP PAKAI
            bm.add('hero-section', {
                label: '<i class="bi bi-card-heading"></i><span>Hero Banner</span>',
                category: '🚀 Seksi Siap Pakai',
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
                category: '🚀 Seksi Siap Pakai',
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
                category: '🚀 Seksi Siap Pakai',
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

            bm.add('stats-counter', {
                label: '<i class="bi bi-123"></i><span>Statistik Angka</span>',
                category: '🚀 Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-light border-top border-bottom">
                        <div class="container text-center">
                            <div class="row g-4">
                                <div class="col-6 col-md-3">
                                    <div class="display-6 fw-bold text-primary mb-1">100+</div>
                                    <div class="text-muted small">Proyek Tuntas</div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="display-6 fw-bold text-success mb-1">500+</div>
                                    <div class="text-muted small">Alumni Pelatihan</div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="display-6 fw-bold text-warning mb-1">99.8%</div>
                                    <div class="text-muted small">Kepuasan Klien</div>
                                </div>
                                <div class="col-6 col-md-3">
                                    <div class="display-6 fw-bold text-info mb-1">24/7</div>
                                    <div class="text-muted small">Dukungan Sistem</div>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('testimonials-grid', {
                label: '<i class="bi bi-chat-square-quote"></i><span>Testimoni Klien</span>',
                category: '🚀 Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-white">
                        <div class="container py-3">
                            <div class="text-center mb-5">
                                <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-2">Testimoni</span>
                                <h2 class="fw-bold text-dark">Apa Kata Klien Kami</h2>
                            </div>
                            <div class="row g-4">
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                        <div class="text-warning mb-3 fs-5">★★★★★</div>
                                        <p class="text-muted small mb-4">"Layanan pembuatan sistem informasinya sangat rapi, aman, dan mudah digunakan oleh staf kami."</p>
                                        <div class="d-flex align-items-center gap-3 mt-auto">
                                            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                            <div>
                                                <div class="fw-bold text-dark small">Dewi Lestari</div>
                                                <div class="text-muted" style="font-size: 0.72rem;">Kepala Bagian IT</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                        <div class="text-warning mb-3 fs-5">★★★★★</div>
                                        <p class="text-muted small mb-4">"Materi pelatihan AI-nya sangat aplikatif dan langsung berdampak signifikan bagi efisiensi kerja tim kami."</p>
                                        <div class="d-flex align-items-center gap-3 mt-auto">
                                            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                            <div>
                                                <div class="fw-bold text-dark small">Budi Pratama</div>
                                                <div class="text-muted" style="font-size: 0.72rem;">Manajer Operasional</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="card h-100 p-4 border rounded-4 shadow-sm">
                                        <div class="text-warning mb-3 fs-5">★★★★★</div>
                                        <p class="text-muted small mb-4">"Sangat profesional dan responsif. Garansi bug dan keamanannya benar-benar terbukti nyata."</p>
                                        <div class="d-flex align-items-center gap-3 mt-auto">
                                            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=120&q=80" class="rounded-circle object-fit-cover" style="width: 44px; height: 44px;" alt="Foto">
                                            <div>
                                                <div class="fw-bold text-dark small">Siti Rahma</div>
                                                <div class="text-muted" style="font-size: 0.72rem;">Direktur Lembaga</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('faq-accordion', {
                label: '<i class="bi bi-question-circle"></i><span>FAQ Accordion</span>',
                category: '🚀 Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-light">
                        <div class="container" style="max-width: 800px;">
                            <div class="text-center mb-4">
                                <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-1 rounded-pill mb-2">FAQ</span>
                                <h2 class="fw-bold text-dark">Pertanyaan yang Sering Diajukan</h2>
                            </div>
                            <div class="accordion shadow-sm rounded-4 overflow-hidden" id="faqAccordionExample">
                                <div class="accordion-item border-0 border-bottom">
                                    <h2 class="accordion-header">
                                        <button class="accordion-button fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#faqItemOne">
                                            Berapa lama estimasi pengerjaan website atau sistem?
                                        </button>
                                    </h2>
                                    <div id="faqItemOne" class="accordion-collapse collapse show">
                                        <div class="accordion-body text-muted small">
                                            Waktu pengerjaan rata-rata berkisar antara 7 hingga 21 hari kerja tergantung kompleksitas fitur yang diminta.
                                        </div>
                                    </div>
                                </div>
                                <div class="accordion-item border-0 border-bottom">
                                    <h2 class="accordion-header">
                                        <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#faqItemTwo">
                                            Apakah sistem yang dibuat memiliki garansi bebas bug?
                                        </button>
                                    </h2>
                                    <div id="faqItemTwo" class="accordion-collapse collapse">
                                        <div class="accordion-body text-muted small">
                                            Ya, seluruh layanan kami dilengkapi garansi teknis berkala dan jaminan proteksi keamanan anti-malware.
                                        </div>
                                    </div>
                                </div>
                                <div class="accordion-item border-0">
                                    <h2 class="accordion-header">
                                        <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#faqItemThree">
                                            Bagaimana prosedur konsultasi awal?
                                        </button>
                                    </h2>
                                    <div id="faqItemThree" class="accordion-collapse collapse">
                                        <div class="accordion-body text-muted small">
                                            Anda dapat langsung menghubungi kami melalui WhatsApp atau formulir penawaran untuk penjadwalan diskusi teknis.
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('video-section', {
                label: '<i class="bi bi-play-btn"></i><span>Video YouTube</span>',
                category: '🚀 Seksi Siap Pakai',
                content: `
                    <section class="py-5 bg-white text-center">
                        <div class="container" style="max-width: 850px;">
                            <h3 class="fw-bold text-dark mb-4">Video Profil & Presentasi</h3>
                            <div class="ratio ratio-16x9 rounded-4 overflow-hidden shadow-lg border">
                                <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video" allowfullscreen></iframe>
                            </div>
                        </div>
                    </section>
                `
            });

            bm.add('cta-banner', {
                label: '<i class="bi bi-megaphone"></i><span>Call to Action (CTA)</span>',
                category: '🚀 Seksi Siap Pakai',
                content: `
                    <section class="py-5 text-white" style="background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);">
                        <div class="container py-4 text-center">
                            <h2 class="display-6 fw-bold mb-3">Siap Mengembangkan Ekosistem Bisnis Anda?</h2>
                            <p class="lead text-white-50 mb-4 mx-auto" style="max-width: 600px;">
                                Diskusikan kebutuhan spesifik Anda bersama praktisi kami dan dapatkan penawaran terbaik.
                            </p>
                            <a href="https://wa.me/6285341026331" target="_blank" class="btn btn-light text-primary btn-lg rounded-pill px-5 fw-bold shadow">
                                <i class="bi bi-whatsapp me-2 text-success"></i> Hubungi WhatsApp Resmi
                            </a>
                        </div>
                    </section>
                `
            });

            bm.add('pricing-card', {
                label: '<i class="bi bi-tags"></i><span>Tabel Harga</span>',
                category: '🚀 Seksi Siap Pakai',
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

            // KATEGORI 4: 🧩 ELEMEN DASAR
            bm.add('text-heading', {
                label: '<i class="bi bi-type-h1"></i><span>Heading Teks</span>',
                category: '🧩 Elemen Dasar',
                content: '<h2 class="fw-bold text-dark mb-3">Tuliskan Judul Heading</h2>'
            });

            bm.add('text-paragraph', {
                label: '<i class="bi bi-body-text"></i><span>Paragraf Teks</span>',
                category: '🧩 Elemen Dasar',
                content: '<p class="text-muted leading-relaxed">Tuliskan paragraf teks penjelasan di sini. Anda dapat mengatur tebal, miring, serta tautan langsung dari editor.</p>'
            });

            bm.add('button-element', {
                label: '<i class="bi bi-cursor"></i><span>Tombol Brand</span>',
                category: '🧩 Elemen Dasar',
                content: '<a href="#" class="btn btn-primary rounded-pill px-4 py-2">Klik Di Sini</a>'
            });

            bm.add('button-whatsapp', {
                label: '<i class="bi bi-whatsapp text-success"></i><span>Tombol WhatsApp</span>',
                category: '🧩 Elemen Dasar',
                content: '<a href="https://wa.me/6285341026331" target="_blank" class="btn btn-success rounded-pill px-4 py-2"><i class="bi bi-whatsapp me-2"></i> Chat WhatsApp</a>'
            });

            bm.add('image-element', {
                label: '<i class="bi bi-image"></i><span>Gambar Foto</span>',
                category: '🧩 Elemen Dasar',
                content: '<img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=700&q=80" class="img-fluid rounded-3 shadow-sm" alt="Ilustrasi">'
            });

            bm.add('card-box', {
                label: '<i class="bi bi-square"></i><span>Card Container</span>',
                category: '🧩 Elemen Dasar',
                content: `
                    <div class="card border rounded-4 p-4 shadow-sm bg-white mb-3">
                        <h5 class="fw-bold text-dark">Judul Kotak Konten</h5>
                        <p class="text-muted mb-0">Isi penjelasan singkat di dalam kotak card.</p>
                    </div>
                `
            });

            bm.add('divider-line', {
                label: '<i class="bi bi-hr"></i><span>Garis Pemisah</span>',
                category: '🧩 Elemen Dasar',
                content: '<hr class="my-4 opacity-25">'
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
