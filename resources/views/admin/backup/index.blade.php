@extends('layouts.admin')

@section('title', 'Pusat Cadangan Data & Media (Backup)')
@section('page_title', 'Pencadangan Sistem & Berkas (1-Click Backup)')

@section('content')

    <div class="row g-4 mb-4">
        <!-- CARD INFO BANNER -->
        <div class="col-12">
            <div class="card border-0 shadow-sm rounded-4 p-4 text-white" style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%);">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-3">
                    <div class="d-flex align-items-center gap-3">
                        <div class="p-3 bg-primary bg-opacity-25 text-info rounded-circle fs-3 d-flex align-items-center justify-content-center" style="width: 56px; height: 56px;">
                            <i class="bi bi-shield-check"></i>
                        </div>
                        <div>
                            <h5 class="fw-bold mb-1">Pusat Keamanan & Cadangan Data Sistem Aktama</h5>
                            <p class="text-white-50 small mb-0">
                                Unduh salinan database dan file aset media kapan saja dengan 1 klik tanpa perlu membuka cPanel atau phpMyAdmin.
                            </p>
                        </div>
                    </div>
                    <div>
                        <span class="badge bg-success bg-opacity-25 text-success border border-success border-opacity-50 px-3 py-2 rounded-pill">
                            <i class="bi bi-check-circle-fill me-1"></i> Sistem Siap Dicadangkan
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <!-- CADANGAN DATABASE -->
        <div class="col-md-6">
            <div class="card border-0 shadow-sm rounded-4 h-100 bg-white p-4 d-flex flex-column justify-content-between">
                <div>
                    <div class="d-flex align-items-center justify-content-between mb-3">
                        <div class="p-3 bg-primary bg-opacity-10 text-primary rounded-4 fs-3">
                            <i class="bi bi-database-down"></i>
                        </div>
                        <span class="badge bg-light text-muted border">Format: .SQL</span>
                    </div>
                    <h5 class="fw-bold text-dark mb-2">Cadangan Database MySQL</h5>
                    <p class="text-muted small leading-relaxed mb-4">
                        Menyimpan seluruh tabel artikel, halaman landing page, katalog layanan, data kontak calon pelanggan (leads), serta konfigurasi pengaturan situs ke dalam file script SQL standar.
                    </p>

                    <ul class="list-unstyled small text-muted border-top border-bottom py-3 mb-4 space-y-2">
                        <li class="d-flex justify-content-between mb-1">
                            <span>Nama Database:</span>
                            <strong class="text-dark font-monospace">{{ $dbName }}</strong>
                        </li>
                        <li class="d-flex justify-content-between mb-1">
                            <span>Estimasi Ukuran:</span>
                            <strong class="text-primary">{{ $dbSize }}</strong>
                        </li>
                        <li class="d-flex justify-content-between">
                            <span>Metode Dump:</span>
                            <span class="badge bg-success bg-opacity-10 text-success">Native PDO (Aman cPanel)</span>
                        </li>
                    </ul>
                </div>

                <div>
                    <a href="{{ route('admin.backup.database') }}" class="btn btn-primary rounded-pill w-100 py-2 fw-bold shadow-sm d-flex align-items-center justify-content-center gap-2">
                        <i class="bi bi-download"></i>
                        <span>Unduh Cadangan Database (.sql)</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- CADANGAN BERKAS MEDIA -->
        <div class="col-md-6">
            <div class="card border-0 shadow-sm rounded-4 h-100 bg-white p-4 d-flex flex-column justify-content-between">
                <div>
                    <div class="d-flex align-items-center justify-content-between mb-3">
                        <div class="p-3 bg-warning bg-opacity-10 text-warning rounded-4 fs-3">
                            <i class="bi bi-file-earmark-zip-fill"></i>
                        </div>
                        <span class="badge bg-light text-muted border">Format: .ZIP</span>
                    </div>
                    <h5 class="fw-bold text-dark mb-2">Cadangan Berkas Media & Upload</h5>
                    <p class="text-muted small leading-relaxed mb-4">
                        Mengompres seluruh foto artikel, banner layanan, sertifikat, logo stempel, dan gambar unggahan ke dalam 1 file arsip ZIP siap simpan.
                    </p>

                    <ul class="list-unstyled small text-muted border-top border-bottom py-3 mb-4 space-y-2">
                        <li class="d-flex justify-content-between mb-1">
                            <span>Direktori Media:</span>
                            <strong class="text-dark font-monospace">public/images/</strong>
                        </li>
                        <li class="d-flex justify-content-between mb-1">
                            <span>Jumlah File Media:</span>
                            <strong class="text-dark">{{ $mediaCount }} Berkas</strong>
                        </li>
                        <li class="d-flex justify-content-between">
                            <span>Total Ukuran Media:</span>
                            <strong class="text-warning">{{ $mediaSizeMb }}</strong>
                        </li>
                    </ul>
                </div>

                <div>
                    <a href="{{ route('admin.backup.media') }}" class="btn btn-outline-dark rounded-pill w-100 py-2 fw-bold shadow-sm d-flex align-items-center justify-content-center gap-2">
                        <i class="bi bi-file-zip"></i>
                        <span>Unduh Arsip Seluruh Media (.zip)</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- PETUNJUK PEMULIHAN / RESTORE -->
    <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
        <h6 class="fw-bold text-dark mb-3"><i class="bi bi-info-circle text-primary me-2"></i> Petunjuk Pemulihan Data (Restore Guide)</h6>
        <div class="row g-3 small text-muted">
            <div class="col-md-6">
                <div class="p-3 bg-light rounded-3 border">
                    <strong class="text-dark d-block mb-1">Cara Restore Database:</strong>
                    File `.sql` hasil unduhan dapat diimpor langsung melalui menu <strong>phpMyAdmin</strong> di cPanel hosting Niagahoster atau phpMyAdmin XAMPP lokal dengan memilih database tujuan lalu klik tab <strong>Import</strong>.
                </div>
            </div>
            <div class="col-md-6">
                <div class="p-3 bg-light rounded-3 border">
                    <strong class="text-dark d-block mb-1">Cara Restore Media:</strong>
                    Ekstrak file `.zip` hasil unduhan, lalu unggah kembali folder `images/` ke dalam direktori `public_html/images/` di hosting Anda melalui File Manager.
                </div>
            </div>
        </div>
    </div>

@endsection

