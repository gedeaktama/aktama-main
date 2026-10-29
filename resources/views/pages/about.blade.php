@extends('layouts.app')

@section('title', 'Tentang Kami | ' . ($settings['company_name'] ?? 'PT Aktama Digital Antika'))
@section('meta_description', 'Profil resmi PT Aktama Digital Antika, visi misi, bidang usaha teknologi terpadu, dan profil kepemimpinan teknis Gede Erik Aktama, S.Pd., M.Pd.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Profil Korporat</span>
            <h1 class="display-6 fw-bold font-display text-dark">Tentang PT Aktama Digital Antika</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Membangun ekosistem teknologi yang adaptif, aman, dan aplikatif untuk mendukung kemajuan pendidikan, pemerintahan, dan dunia usaha.
            </p>
        </div>
    </section>

    <!-- Konten Utama Profil -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <div class="row g-5 align-items-center mb-5">
                <div class="col-lg-6">
                    <span class="badge bg-info bg-opacity-10 text-info fw-bold text-uppercase px-3 py-1 mb-2">Identitas & Legalitas</span>
                    <h2 class="fw-bold font-display text-dark mb-3">Solusi Digital Terpadu Berstandar Industri</h2>
                    <p class="text-muted leading-relaxed mb-3">
                        <strong>PT Aktama Digital Antika</strong> (dikenal dengan brand <strong>{{ $settings['brand_name'] ?? 'Aktama Digital' }}</strong>) adalah badan usaha resmi yang bergerak di bidang penyediaan solusi teknologi informasi, rekayasa perangkat lunak modern, dan pelatihan kecerdasan artifisial (AI) aplikatif.
                    </p>
                    <p class="text-muted leading-relaxed mb-4">
                        Kami lahir dengan komitmen untuk menghadirkan perangkat lunak yang tidak hanya indah secara visual, tetapi juga kokoh secara arsitektural—bebas dari kerentanan keamanan yang sering merugikan bisnis—serta membimbing masyarakat dan instansi untuk menguasai teknologi melalui program pelatihan yang tepat sasaran.
                    </p>

                    <div class="row g-3">
                        <div class="col-sm-6">
                            <div class="p-3 rounded-3 bg-light border">
                                <h6 class="fw-bold text-dark mb-1"><i class="bi bi-shield-check text-success me-1"></i> Legalitas Resmi & Terdaftar</h6>
                                <p class="text-muted small mb-0">NIB: <strong>{{ $settings['nib_number'] ?? '1703250057018' }}</strong> terdaftar resmi dengan izin operasional dan unit LPK.</p>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="p-3 rounded-3 bg-light border">
                                <h6 class="fw-bold text-dark mb-1"><i class="bi bi-mortarboard text-primary me-1"></i> Dipimpin Akademisi</h6>
                                <p class="text-muted small mb-0">Dipandu langsung oleh Dosen Sistem Komputer & Fasilitator Nasional KKA Kemdikdasmen.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-light">
                        <h4 class="fw-bold font-display text-dark mb-3">Visi & Misi Perusahaan</h4>
                        <div class="mb-4">
                            <strong class="text-primary d-block small mb-1 text-uppercase fw-bold">Visi:</strong>
                            <p class="text-dark small leading-relaxed mb-0">
                                Menjadi mitra terpercaya dalam transformasi teknologi informasi dan literasi kecerdasan buatan terdepan yang adaptif, aman, dan berdaya guna bagi kemajuan masyarakat, dunia pendidikan, dan dunia usaha di Indonesia.
                            </p>
                        </div>
                        <div>
                            <strong class="text-primary d-block small mb-1 text-uppercase fw-bold">Misi Utama:</strong>
                            <ul class="text-muted small ps-3 mb-0 space-y-2">
                                <li class="mb-2">Menyelenggarakan pelatihan Kecerdasan Artifisial (AI) dan komputasi aplikatif bagi instansi, sekolah, dan pelaku usaha.</li>
                                <li class="mb-2">Mengembangkan solusi perangkat lunak berbasis web yang aman dari celah malware judi online, cepat, dan teruji.</li>
                                <li class="mb-2">Mendukung digitalisasi momentum keluarga melalui produk undangan online inovatif.</li>
                                <li class="mb-2">Membangun rantai nilai distribusi komoditas kopi riil yang memberdayakan pelaku usaha lokal.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PROFIL PEMILIK FAKTUAL -->
            <div class="p-4 p-md-5 rounded-4 bg-light border mb-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-4 text-center">
                        <div class="bg-white p-3 rounded-4 shadow-sm border d-inline-block">
                            <img src="{{ asset('images/gede-erik-aktama.jpg') }}" alt="{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}" class="img-fluid rounded-3 shadow-sm object-fit-cover mb-2" style="max-height: 260px;">
                            <div>
                                <span class="badge bg-primary px-3 py-1 rounded-pill small mt-1">Direktur Utama & Penanggung Jawab</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-8">
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <h3 class="fw-bold text-dark font-display mb-0">{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</h3>
                        </div>
                        <p class="text-primary fw-semibold mb-3">{{ $settings['owner_title'] ?? 'Dosen Sistem Komputer & Fasilitator Nasional KKA Kemdikdasmen' }}</p>
                        <p class="text-muted leading-relaxed mb-3">
                            {{ $settings['owner_bio'] ?? 'Dosen pada Program Studi Sistem Komputer, Universitas Parna Raya, serta Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen dengan dedikasi tinggi pada literasi teknologi dan rekayasa perangkat lunak modern.' }}
                        </p>
                        <div class="d-flex flex-wrap gap-2 mb-4">
                            <span class="badge bg-white text-dark border p-2"><i class="bi bi-award text-warning me-1"></i> Fasilitator Nasional KKA Kemdikdasmen</span>
                            <span class="badge bg-white text-dark border p-2"><i class="bi bi-building text-info me-1"></i> Dosen Prodi Sistem Komputer Univ. Parna Raya</span>
                            <span class="badge bg-white text-dark border p-2"><i class="bi bi-file-earmark-check text-success me-1"></i> NIB: {{ $settings['nib_number'] ?? '1703250057018' }}</span>
                            <span class="badge bg-white text-dark border p-2"><i class="bi bi-shield-lock text-primary me-1"></i> Software Architect Bebas Malware</span>
                        </div>

                        <!-- Dokumen Izin Usaha -->
                        <div class="p-3 bg-white rounded-3 border d-flex align-items-center justify-content-between flex-wrap gap-3">
                            <div class="d-flex align-items-center gap-3">
                                <img src="{{ asset('images/logo-seal-aktama.png') }}" alt="Cap PT Aktama Digital Antika" style="height: 52px;">
                                <div>
                                    <strong class="text-dark small d-block">Izin Berusaha Berbasis Risiko (NIB)</strong>
                                    <small class="text-muted">Nomor Induk Berusaha: {{ $settings['nib_number'] ?? '1703250057018' }} &bull; LPK Terdaftar</small>
                                </div>
                            </div>
                            <a href="{{ asset('images/nib-document.jpg') }}" target="_blank" class="btn btn-outline-primary btn-sm rounded-pill px-3">
                                <i class="bi bi-eye me-1"></i> Lihat Dokumen NIB
                            </a>
                        </div>

                        <!-- Link ke Website Portofolio & Riset Founder -->
                        <div class="p-3 bg-white rounded-3 border d-flex align-items-center justify-content-between flex-wrap gap-3 mt-3">
                            <div class="d-flex align-items-center gap-3">
                                <div class="rounded-circle bg-primary bg-opacity-10 text-primary p-2 fs-4 d-flex align-items-center justify-content-center" style="width: 52px; height: 52px;">
                                    <i class="bi bi-mortarboard-fill"></i>
                                </div>
                                <div>
                                    <strong class="text-dark small d-block">Website Portofolio Profesional & Riset SINTA</strong>
                                    <small class="text-muted">Jurnal terindeks SINTA 4 & 5, riset algoritma AI, dan rekam jejak akademik founder di profil.aktama.com</small>
                                </div>
                            </div>
                            <a href="{{ $settings['profile_url'] ?? 'https://profil.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm rounded-pill px-4 py-2 fw-semibold">
                                <i class="bi bi-box-arrow-up-right me-1"></i> Buka profil.aktama.com
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5 PILAR BIDANG USAHA -->
            <div class="text-center mb-4">
                <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Struktur Bisnis</span>
                <h3 class="fw-bold font-display text-dark">5 Lini Usaha Terpadu Aktama</h3>
            </div>

            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card card-feature p-4 h-100">
                        <div class="fs-3 text-info mb-2"><i class="bi bi-robot"></i></div>
                        <h5 class="fw-bold text-dark fs-6">Pelatihan Kecerdasan Artifisial (AI)</h5>
                        <p class="text-muted small mb-0">Program bimbingan intensif untuk staf tata usaha, pendidik, dan pemilik bisnis dalam memanfaatkan AI secara produktif.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-feature p-4 h-100">
                        <div class="fs-3 text-primary mb-2"><i class="bi bi-globe"></i></div>
                        <h5 class="fw-bold text-dark fs-6">Jasa Pembuatan Website & Aplikasi</h5>
                        <p class="text-muted small mb-0">Software house penyedia website korporat, portal akademik sekolah, sistem POS kasir, dan aplikasi web custom.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-feature p-4 h-100">
                        <div class="fs-3 text-success mb-2"><i class="bi bi-mortarboard"></i></div>
                        <h5 class="fw-bold text-dark fs-6">Aktama Academy</h5>
                        <p class="text-muted small mb-0">Platform e-learning untuk kursus pemrograman mandiri dengan kurikulum berstandar industri.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card card-feature p-4 h-100">
                        <div class="fs-3 text-danger mb-2"><i class="bi bi-heart"></i></div>
                        <h5 class="fw-bold text-dark fs-6">Undangan Online Digital</h5>
                        <p class="text-muted small mb-0">Layanan pembuatan website undangan pernikahan dan acara keluarga yang elegan, cepat, dan mudah dibagikan via WhatsApp.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card card-feature p-4 h-100">
                        <div class="fs-3 text-warning mb-2"><i class="bi bi-cup-hot"></i></div>
                        <h5 class="fw-bold text-dark fs-6">{{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }}</h5>
                        <p class="text-muted small mb-0">Bisnis distribusi kopi kemasan berkualitas pilihan untuk penikmat retail dan pasokan grosir rutin kafe dan warkop.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

@endsection
