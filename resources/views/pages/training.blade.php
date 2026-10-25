@extends('layouts.app')

@section('title', 'Katalog Pelatihan AI & TI | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Program pelatihan Kecerdasan Artifisial (AI) terapan bersertifikat LPK resmi untuk dinas, guru, kampus, serta kursus daring mandiri di Aktama Academy.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom position-relative overflow-hidden">
        <div class="container py-4 text-center position-relative">
            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                <i class="bi bi-award-fill me-1"></i> Lembaga Pelatihan Kerja (LPK) Terdaftar Resmi • NIB: {{ $settings['nib_number'] ?? '1703250057018' }}
            </span>
            <h1 class="display-6 fw-bold font-display text-dark mb-2">Pendidikan, Pelatihan AI Terapan & Sertifikasi Komputasi</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-4">
                Tingkatkan kompetensi digital dan efisiensi kerja nyata bersama instruktur ahli <strong>{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</strong> (Fasilitator Nasional KKA Kemdikdasmen & Dosen Sistem Komputer).
            </p>

            <!-- 3 Pilar Belajar Badges -->
            <div class="d-flex flex-wrap justify-content-center gap-3">
                <a href="#in-house-training" class="btn btn-outline-dark btn-sm rounded-pill px-3 py-2 fw-semibold">
                    <i class="bi bi-building text-info me-1"></i> In-House Training Instansi / Sekolah
                </a>
                <a href="#academy-lms" class="btn btn-outline-success btn-sm rounded-pill px-3 py-2 fw-semibold">
                    <i class="bi bi-mortarboard-fill text-success me-1"></i> Kursus Online di Aktama Academy
                </a>
                <a href="#jadwal-batch" class="btn btn-outline-primary btn-sm rounded-pill px-3 py-2 fw-semibold">
                    <i class="bi bi-calendar-event text-primary me-1"></i> Jadwal Batch Terdekat
                </a>
            </div>
        </div>
    </section>

    <!-- PILAR 1: IN-HOUSE TRAINING INSTANSI & SEKOLAH (B2B / B2G) -->
    <section id="in-house-training" class="py-5 bg-white border-bottom">
        <div class="container py-3">
            <div class="row align-items-end mb-4">
                <div class="col-lg-8">
                    <span class="badge bg-info bg-opacity-10 text-info fw-bold text-uppercase px-3 py-1 mb-2">Program Institusional (B2B / B2G)</span>
                    <h2 class="fw-bold font-display text-dark mb-2">Bimtek & In-House Training untuk Instansi & Sekolah</h2>
                    <p class="text-muted mb-0 small">
                        Dirancang khusus untuk dinas pemerintah (OPD), tenaga pendidik sekolah/madrasah, perguruan tinggi, dan korporat. Dilengkapi Kerangka Acuan Kerja (KAK), faktur pajak, dan sertifikat resmi 32 JP LPK.
                    </p>
                </div>
                <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                    <a href="#form-daftar" class="btn btn-brand rounded-pill btn-sm px-4">
                        <i class="bi bi-file-earmark-pdf me-1"></i> Minta Proposal Resmi
                    </a>
                </div>
            </div>

            <div class="row g-4 mb-5">
                @forelse($trainingPrograms as $prog)
                    <div class="col-lg-6">
                        <div class="card card-feature p-4 p-md-5 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small">
                                        {{ ucfirst(str_replace('-', ' ', $prog->category)) }}
                                    </span>
                                    <span class="text-muted small"><i class="bi bi-clock me-1"></i>{{ $prog->duration }}</span>
                                </div>

                                @if($prog->image)
                                    <img src="{{ asset('images/' . $prog->image) }}" alt="{{ $prog->title }}" class="img-fluid rounded-3 mb-3 w-100 object-fit-cover shadow-xs" style="max-height: 200px;">
                                @endif
                                <h3 class="fw-bold text-dark fs-5 mb-2">{{ $prog->title }}</h3>
                                <div class="text-muted small leading-relaxed mb-4">{!! $prog->objectives !!}</div>

                                <div class="p-3 rounded-3 bg-light border mb-4">
                                    <strong class="text-dark d-block small mb-1"><i class="bi bi-people text-info me-1"></i> Target Peserta:</strong>
                                    <span class="text-muted small">{{ $prog->target_audience }}</span>
                                </div>

                                @if($prog->syllabus && is_array($prog->syllabus))
                                    <h6 class="fw-bold text-dark small mb-2"><i class="bi bi-journal-check text-success me-1"></i> Silabus & Pokok Bahasan:</h6>
                                    <ul class="list-unstyled small text-muted mb-4 space-y-2">
                                        @foreach($prog->syllabus as $item)
                                            <li class="mb-2 d-flex align-items-start gap-2">
                                                <i class="bi bi-check-circle-fill text-primary small mt-1"></i>
                                                <span>{{ $item }}</span>
                                            </li>
                                        @endforeach
                                    </ul>
                                @endif
                            </div>

                            <div class="border-top pt-3 d-flex flex-wrap justify-content-between align-items-center gap-3">
                                <div>
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Metode Pelaksanaan:</small>
                                    <span class="badge bg-secondary bg-opacity-10 text-dark small text-uppercase">{{ $prog->delivery_format }}</span>
                                </div>
                                <div class="text-end">
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Biaya Investasi:</small>
                                    <strong class="text-primary">{{ $prog->price_info ?? 'Sesuai Penawaran' }}</strong>
                                </div>
                                <a href="#form-daftar" class="btn btn-brand rounded-pill btn-sm px-4 ms-auto">
                                    Minta Penawaran
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-info">Katalog pelatihan sedang diperbarui.</div>
                    </div>
                @endforelse
            </div>
        </div>
    </section>

    <!-- PILAR 2: KURSUS DARING MANDIRI DI AKTAMA ACADEMY LMS (B2C RETAIL) -->
    <section id="academy-lms" class="py-5 bg-light border-bottom position-relative">
        <div class="container py-4">
            <!-- Box Promosi Aktama Academy -->
            <div class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-white mb-5" style="border-top: 5px solid #10b981 !important;">
                <div class="row align-items-center g-4">
                    <div class="col-lg-8">
                        <span class="badge bg-success bg-opacity-10 text-success fw-bold text-uppercase px-3 py-1 mb-2">
                            <i class="bi bi-mortarboard-fill me-1"></i> E-Learning Platform • Aktama Academy
                        </span>
                        <h2 class="display-6 fw-bold font-display text-dark mb-2">Ingin Belajar Daring Mandiri Kapan Saja?</h2>
                        <p class="text-secondary small leading-relaxed mb-3">
                            Bagi mahasiswa, pendidik mandiri, atau talenta digital yang ingin belajar secara fleksibel tanpa menunggu jadwal workshop institusi, silakan ikuti kursus terstruktur kami di <strong>Aktama Academy (academy.aktama.com)</strong>.
                        </p>
                        <div class="d-flex flex-wrap gap-3 small text-muted mb-4">
                            <span><i class="bi bi-play-circle-fill text-danger me-1"></i> Video Pembelajaran HD</span>
                            <span><i class="bi bi-card-checklist text-primary me-1"></i> Kuis Evaluasi Interaktif</span>
                            <span><i class="bi bi-credit-card text-success me-1"></i> Checkout Midtrans Instan</span>
                            <span><i class="bi bi-patch-check-fill text-warning me-1"></i> Sertifikat PDF Otomatis</span>
                        </div>
                    </div>
                    <div class="col-lg-4 text-lg-end">
                        <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-success btn-lg rounded-pill px-4 py-3 fw-bold shadow-sm d-inline-flex align-items-center gap-2">
                            <span>Kunjungi Aktama Academy</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>

                <!-- Showcase Kursus Unggulan Aktama Academy -->
                <div class="border-top pt-4 mt-2">
                    <h5 class="fw-bold font-display text-dark mb-3">Katalog Kursus Daring Pilihan di Academy:</h5>
                    <div class="row g-3">
                        <div class="col-md-6 col-lg-3">
                            <div class="p-3 rounded-3 bg-light border h-100 d-flex flex-column justify-content-between">
                                <div>
                                    <span class="badge bg-primary bg-opacity-10 text-primary small mb-2">Web Development</span>
                                    <h6 class="fw-bold text-dark mb-1">Dasar Pemrograman Web Modern</h6>
                                    <small class="text-muted d-block mb-3">HTML5, CSS3, & PHP Native dari nol hingga rilis hosting.</small>
                                </div>
                                <div class="border-top pt-2 d-flex justify-content-between align-items-center">
                                    <strong class="text-success small">Rp 149.000</strong>
                                    <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" class="btn btn-outline-success btn-sm rounded-pill py-1 px-3" style="font-size: 0.75rem;">
                                        Mulai Belajar ↗
                                    </a>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3">
                            <div class="p-3 rounded-3 bg-light border h-100 d-flex flex-column justify-content-between">
                                <div>
                                    <span class="badge bg-info bg-opacity-10 text-info small mb-2">Framework & Database</span>
                                    <h6 class="fw-bold text-dark mb-1">Aplikasi Bisnis & POS dengan Laravel</h6>
                                    <small class="text-muted d-block mb-3">Manajemen stok multi-harga, kasir, invoice, dan otorisasi role.</small>
                                </div>
                                <div class="border-top pt-2 d-flex justify-content-between align-items-center">
                                    <strong class="text-success small">Rp 299.000</strong>
                                    <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" class="btn btn-outline-success btn-sm rounded-pill py-1 px-3" style="font-size: 0.75rem;">
                                        Mulai Belajar ↗
                                    </a>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3">
                            <div class="p-3 rounded-3 bg-light border h-100 d-flex flex-column justify-content-between">
                                <div>
                                    <span class="badge bg-warning bg-opacity-10 text-dark small mb-2">AI Terapan</span>
                                    <h6 class="fw-bold text-dark mb-1">Prompt Engineering Administrasi</h6>
                                    <small class="text-muted d-block mb-3">Otomasi naskah dinas, notula rapat & formula spreadsheet.</small>
                                </div>
                                <div class="border-top pt-2 d-flex justify-content-between align-items-center">
                                    <strong class="text-success small">Rp 199.000</strong>
                                    <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" class="btn btn-outline-success btn-sm rounded-pill py-1 px-3" style="font-size: 0.75rem;">
                                        Mulai Belajar ↗
                                    </a>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3">
                            <div class="p-3 rounded-3 bg-light border h-100 d-flex flex-column justify-content-between">
                                <div>
                                    <span class="badge bg-danger bg-opacity-10 text-danger small mb-2">Edukasi Guru</span>
                                    <h6 class="fw-bold text-dark mb-1">Koding KKA Kemdikdasmen</h6>
                                    <small class="text-muted d-block mb-3">Computational thinking, modul ajar & bank soal penalaran.</small>
                                </div>
                                <div class="border-top pt-2 d-flex justify-content-between align-items-center">
                                    <strong class="text-success small">Rp 249.000</strong>
                                    <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" class="btn btn-outline-success btn-sm rounded-pill py-1 px-3" style="font-size: 0.75rem;">
                                        Mulai Belajar ↗
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PILAR 3: JADWAL BATCH PELATIHAN TERDEKAT -->
            <div id="jadwal-batch" class="mb-5">
                <div class="text-center mb-4">
                    <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Kalender Event Publik</span>
                    <h3 class="fw-bold font-display text-dark">Jadwal Batch Pelatihan Terbuka Terdekat</h3>
                    <p class="text-muted small">Pendaftaran terbuka untuk umum, guru, ASN, dan mahasiswa dengan kuota terbatas.</p>
                </div>

                <div class="row g-4">
                    <div class="col-lg-6">
                        <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <span class="badge bg-danger text-white small px-3 py-1 rounded-pill">Sisa 6 Kursi</span>
                                    <span class="text-muted small"><i class="bi bi-calendar3 me-1"></i> 14 - 15 November 2026</span>
                                </div>
                                <h5 class="fw-bold text-dark mb-2">Masterclass AI Prompt Engineering untuk Guru & Tenaga Administrasi</h5>
                                <p class="text-secondary small leading-relaxed mb-3">
                                    Pelatihan daring interaktif via Zoom (2 hari intensif) menyusun modul ajar, rubrik penilaian, surat dinas, dan pengolahan spreadsheet berbasis AI secara etis dan aman.
                                </p>
                                <ul class="list-unstyled small text-muted mb-3 space-y-1">
                                    <li><i class="bi bi-check2 text-success me-1"></i> Sertifikat 16 JP Lembaga Pelatihan Kerja (LPK) Terdaftar</li>
                                    <li><i class="bi bi-check2 text-success me-1"></i> Modul Panduan & Bank 300+ Prompt Teruji</li>
                                    <li><i class="bi bi-check2 text-success me-1"></i> Rekaman Ulang Video Pembelajaran Selamanya</li>
                                </ul>
                            </div>
                            <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                                <div>
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Investasi:</small>
                                    <strong class="text-primary fs-5">Rp 250.000</strong>
                                </div>
                                <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6285341026331' }}?text={{ urlencode('Halo Admin Aktama, saya ingin mendaftar Kursi Batch Masterclass AI Guru & Administrasi.') }}" target="_blank" rel="noopener" class="btn btn-brand rounded-pill btn-sm px-4">
                                    <i class="bi bi-whatsapp me-1"></i> Amankan Kursi
                                </a>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-6">
                        <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <span class="badge bg-warning text-dark small px-3 py-1 rounded-pill">Sisa 8 Kursi</span>
                                    <span class="text-muted small"><i class="bi bi-calendar3 me-1"></i> 21 - 22 November 2026</span>
                                </div>
                                <h5 class="fw-bold text-dark mb-2">Bootcamp Koding & Kecerdasan Artifisial (KKA) untuk Calon Pemrogram</h5>
                                <p class="text-secondary small leading-relaxed mb-3">
                                    Membangun logika berpikir komputasi, algoritma dasar web, dan otomasi script dengan bimbingan langsung Fasilitator Nasional KKA Kemdikdasmen.
                                </p>
                                <ul class="list-unstyled small text-muted mb-3 space-y-1">
                                    <li><i class="bi bi-check2 text-success me-1"></i> Sertifikat Resmi LPK Terdaftar</li>
                                    <li><i class="bi bi-check2 text-success me-1"></i> Proyek Akhir Berstandar Portofolio Nyata</li>
                                    <li><i class="bi bi-check2 text-success me-1"></i> Mentoring di Grup WhatsApp Eksklusif</li>
                                </ul>
                            </div>
                            <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                                <div>
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Investasi:</small>
                                    <strong class="text-primary fs-5">Rp 450.000</strong>
                                </div>
                                <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6285341026331' }}?text={{ urlencode('Halo Admin Aktama, saya ingin mendaftar Kursi Batch Bootcamp Koding KKA.') }}" target="_blank" rel="noopener" class="btn btn-brand rounded-pill btn-sm px-4">
                                    <i class="bi bi-whatsapp me-1"></i> Amankan Kursi
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PILAR 4: VALIDASI SERTIFIKAT LPK RESMI -->
            <div class="card border-0 shadow-sm rounded-4 p-4 bg-white mb-5">
                <div class="row align-items-center g-3">
                    <div class="col-lg-8">
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <i class="bi bi-patch-check-fill text-success fs-4"></i>
                            <h5 class="fw-bold font-display text-dark mb-0">Verifikasi Keabsahan Sertifikat Pelatihan LPK</h5>
                        </div>
                        <p class="text-muted small mb-0">
                            Seluruh sertifikat yang diterbitkan oleh Lembaga Pelatihan Kerja (LPK) PT Aktama Digital Antika dilengkapi ID Registrasi unik yang dapat divalidasi keasliannya secara daring oleh instansi, sekolah, dan HRD.
                        </p>
                    </div>
                    <div class="col-lg-4 text-lg-end">
                        <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener" class="btn btn-outline-dark rounded-pill px-4 py-2 small fw-semibold">
                            <i class="bi bi-search me-1"></i> Cek Sertifikat di Academy
                        </a>
                    </div>
                </div>
            </div>

            <!-- FORMULIR PENAWARAN & IN-HOUSE TRAINING RESMI -->
            <div id="form-daftar" class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-white">
                <div class="text-center max-w-xl mx-auto mb-4">
                    <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Formulir Pengajuan In-House Training</span>
                    <h3 class="fw-bold font-display text-dark">Rencanakan Pelatihan Resmi untuk Instansi / Kelompok Anda</h3>
                    <p class="text-muted small">
                        Silakan lengkapi formulir di bawah ini. Kami siap menyusun jadwal, materi yang disesuaikan (*custom syllabus*), serta dokumen proposal & KAK resmi.
                    </p>
                </div>

                <form action="{{ route('inquiry.store') }}" method="POST" class="max-w-2xl mx-auto">
                    @csrf
                    <input type="hidden" name="service_type" value="pelatihan-ai">
                    <input type="hidden" name="source_page" value="Halaman Pelatihan AI">

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Kontak / Penanggung Jawab *</label>
                            <input type="text" name="name" class="form-control rounded-3" required placeholder="Contoh: Dra. Sri Wahyuni">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nomor WhatsApp *</label>
                            <input type="text" name="whatsapp" class="form-control rounded-3" required placeholder="Contoh: 081234567890">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Instansi / Sekolah / Perusahaan</label>
                            <input type="text" name="organization" class="form-control rounded-3" placeholder="Contoh: Dinas Pendidikan / SMKN 1">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Email Resmi (Opsional)</label>
                            <input type="email" name="email" class="form-control rounded-3" placeholder="email@instansi.go.id">
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Program Pelatihan yang Diminati & Rencana Pelaksanaan *</label>
                        <textarea name="message" class="form-control rounded-3" rows="3" required placeholder="Jelaskan topik yang dibutuhkan, perkiraan jumlah peserta (misal: 30 guru / 25 ASN), serta rencana tanggal pelaksanaan..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-brand btn-lg w-100 rounded-pill shadow-sm">
                        <i class="bi bi-send-fill me-2"></i> Kirim Permintaan Proposal Pelatihan
                    </button>
                </form>
            </div>
        </div>
    </section>

@endsection
