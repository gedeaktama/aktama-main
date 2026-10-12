<!-- SECTION: EKOSISTEM BISNIS & PRODUK DIGITAL TERPADU -->
<section id="ekosistem-digital" class="py-5 bg-light position-relative border-bottom overflow-hidden">
    <!-- Subtle Background Glow -->
    <div class="position-absolute top-0 start-50 translate-middle-x w-100 h-100 pointer-events-none" style="background: radial-gradient(circle at 50% 0%, rgba(67, 97, 238, 0.05) 0%, transparent 60%);"></div>

    <div class="container py-lg-4 position-relative">
        <div class="row align-items-end mb-5">
            <div class="col-lg-8">
                <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                    <i class="bi bi-diagram-3-fill me-1"></i> {{ $sectionConfig->badge ?? 'Ekosistem Bisnis Aktama' }}
                </span>
                <h2 class="display-6 fw-bold font-display text-dark tracking-tight mb-2">
                    {{ $sectionConfig->title ?? 'Ekosistem Produk Digital & Unit Bisnis Terpadu' }}
                </h2>
                <p class="text-muted mb-0 lead fs-6">
                    {{ $sectionConfig->subtitle ?? 'Lini inovasi software mandiri, platform edukasi daring, dan unit komoditas riil yang dikembangkan dan dikelola oleh PT Aktama Digital Antika.' }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 px-3 py-2 rounded-pill small">
                    <i class="bi bi-check-circle-fill me-1"></i> Seluruh Platform Aktif & Terintegrasi
                </span>
            </div>
        </div>

        <div class="row g-4">
            <!-- 1. UNDANGAN ONLINE DIGITAL -->
            <div class="col-lg-4 col-md-6">
                <div class="card h-100 border-0 rounded-4 shadow-sm bg-white p-4 d-flex flex-column justify-content-between transition-all hover-translate-up" style="border-top: 4px solid #ec4899 !important;">
                    <div>
                        <div class="d-flex align-items-center justify-content-between mb-3">
                            <div class="p-3 rounded-4 bg-pink bg-opacity-10 text-pink fs-3" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;">
                                <i class="bi bi-heart-fill"></i>
                            </div>
                            <span class="badge bg-pink bg-opacity-10 text-pink fw-semibold px-3 py-1 rounded-pill" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;">
                                Flagship SaaS
                            </span>
                        </div>

                        <h4 class="fw-bold text-dark font-display mb-1">Undangan Online</h4>
                        <p class="text-muted small mb-3">Platform Undangan Pernikahan & Acara Adat Digital</p>

                        <p class="text-secondary small leading-relaxed mb-4">
                            Solusi publikasi momen sakral berbasis web interaktif. Dilengkapi personalisasi nama tamu tanpa batas, buku tamu digital, dan amplop digital kado online.
                        </p>

                        <div class="border-top pt-3 mb-4">
                            <h6 class="text-uppercase small fw-bold text-muted mb-2" style="font-size: 0.7rem; letter-spacing: 0.05em;">Fitur Utama Platform:</h6>
                            <ul class="list-unstyled small text-secondary mb-0 d-flex flex-column gap-2">
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-pink" style="color: #ec4899;"></i>
                                    <span>6 Tema Eksklusif (Adat Bali, Sakinah, Floral)</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-pink" style="color: #ec4899;"></i>
                                    <span>Konfirmasi Kehadiran Tamu (RSVP Realtime)</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-pink" style="color: #ec4899;"></i>
                                    <span>Amplop Digital & Pembayaran QRIS</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-pink" style="color: #ec4899;"></i>
                                    <span>Musik Latar Romantis & Rute Google Maps</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{{ $settings['invitation_url'] ?? 'https://undanganonline.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-danger w-100 rounded-pill py-2 fw-semibold d-flex align-items-center justify-content-center gap-2" style="border-color: #ec4899; color: #ec4899;">
                            <span>Kunjungi Undangan Online</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- 2. AKTAMA COFFEE -->
            <div class="col-lg-4 col-md-6">
                <div class="card h-100 border-0 rounded-4 shadow-sm bg-white p-4 d-flex flex-column justify-content-between transition-all hover-translate-up" style="border-top: 4px solid #f59e0b !important;">
                    <div>
                        <div class="d-flex align-items-center justify-content-between mb-3">
                            <div class="p-3 rounded-4 bg-warning bg-opacity-10 text-warning fs-3">
                                <i class="bi bi-cup-hot-fill"></i>
                            </div>
                            <span class="badge bg-warning bg-opacity-10 text-dark fw-semibold px-3 py-1 rounded-pill">
                                Komoditas Riil
                            </span>
                        </div>

                        <h4 class="fw-bold text-dark font-display mb-1">Aktama Coffee</h4>
                        <p class="text-muted small mb-3">Roastery & Distribusi Kopi Nusantara</p>

                        <p class="text-secondary small leading-relaxed mb-4">
                            Unit bisnis riil pengolahan dan distribusi biji serta bubuk kopi asli Nusantara pilihan petani lokal. Melayani retail online, reseller, dan pasokan rutin kafe.
                        </p>

                        <div class="border-top pt-3 mb-4">
                            <h6 class="text-uppercase small fw-bold text-muted mb-2" style="font-size: 0.7rem; letter-spacing: 0.05em;">Fitur & Kapabilitas:</h6>
                            <ul class="list-unstyled small text-secondary mb-0 d-flex flex-column gap-2">
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-warning"></i>
                                    <span>Single Origin Asli (Gayo, Toraja, Flores, Lampung)</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-warning"></i>
                                    <span>Pembeda Otomatis Harga Eceran vs Grosir Kafe</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-warning"></i>
                                    <span>Sistem Inventaris Stok & Faktur Terpusat</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-warning"></i>
                                    <span>Pemesanan Online Mandiri Khusus Mitra</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{{ $settings['coffee_app_url'] ?? 'https://coffee.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-warning w-100 rounded-pill py-2 fw-semibold text-dark d-flex align-items-center justify-content-center gap-2" style="border-color: #f59e0b;">
                            <span>Kunjungi Aktama Coffee</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- 3. AKTAMA ACADEMY -->
            <div class="col-lg-4 col-md-12">
                <div class="card h-100 border-0 rounded-4 shadow-sm bg-white p-4 d-flex flex-column justify-content-between transition-all hover-translate-up" style="border-top: 4px solid #10b981 !important;">
                    <div>
                        <div class="d-flex align-items-center justify-content-between mb-3">
                            <div class="p-3 rounded-4 bg-success bg-opacity-10 text-success fs-3">
                                <i class="bi bi-mortarboard-fill"></i>
                            </div>
                            <span class="badge bg-success bg-opacity-10 text-success fw-semibold px-3 py-1 rounded-pill">
                                Platform LMS
                            </span>
                        </div>

                        <h4 class="fw-bold text-dark font-display mb-1">Aktama Academy</h4>
                        <p class="text-muted small mb-3">Pusat Pelatihan Koding & Literasi Digital Daring</p>

                        <p class="text-secondary small leading-relaxed mb-4">
                            Ekosistem Learning Management System (LMS) interaktif untuk membimbing siswa, mahasiswa, dan praktisi menguasai keterampilan rekayasa software dan AI secara terarah.
                        </p>

                        <div class="border-top pt-3 mb-4">
                            <h6 class="text-uppercase small fw-bold text-muted mb-2" style="font-size: 0.7rem; letter-spacing: 0.05em;">Kurikulum Unggulan:</h6>
                            <ul class="list-unstyled small text-secondary mb-0 d-flex flex-column gap-2">
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-success"></i>
                                    <span>Dasar Pemrograman Web (HTML, CSS, PHP Native)</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-success"></i>
                                    <span>Framework Laravel & Rekayasa Database MySQL</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-success"></i>
                                    <span>Logika Koding KKA (Kemdikdasmen Standard)</span>
                                </li>
                                <li class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-circle text-success"></i>
                                    <span>Sertifikat Kelulusan Resmi Lembaga Pelatihan Kerja</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div>
                        <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-success w-100 rounded-pill py-2 fw-semibold d-flex align-items-center justify-content-center gap-2">
                            <span>Masuk ke Aktama Academy</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
