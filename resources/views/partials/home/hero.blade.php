<!-- HERO SECTION -->
<section class="py-5 bg-white border-bottom position-relative overflow-hidden">
    <div class="container py-lg-4">
        <div class="row align-items-center g-5">
            <div class="col-lg-7 text-center text-lg-start">
                <!-- Badge Kredibilitas -->
                <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-light border border-primary border-opacity-25 text-primary small fw-semibold mb-3">
                    <i class="bi bi-shield-check text-primary"></i>
                    <span>{{ $sectionConfig->badge ?? 'PT Aktama Digital Antika • Solusi Teknologi Terpadu' }}</span>
                </div>

                <!-- Headline Utama -->
                <h1 class="display-5 fw-extrabold font-display text-dark tracking-tight mb-3 lh-sm">
                    @if(!empty($sectionConfig?->title))
                        {{ $sectionConfig->title }}
                    @else
                        Kembangkan Bisnis & Kompetensi Digital Bersama <span class="text-gradient">{{ $settings['brand_name'] ?? 'Aktama Digital' }}</span>
                    @endif
                </h1>

                <!-- Ringkasan Nilai Bisnis -->
                <p class="lead text-muted mb-4 fs-6 lh-base">
                    @if(!empty($sectionConfig?->subtitle))
                        {{ $sectionConfig->subtitle }}
                    @else
                        Penyedia layanan <strong>Pelatihan Kecerdasan Artifisial (AI)</strong> terapan untuk instansi & sekolah, <strong>Jasa Pembuatan Website & Aplikasi</strong> bisnis yang aman dari celah malware, ekosistem pembelajaran <strong>Aktama Academy</strong>, serta lini usaha <strong>Undangan Online</strong> dan <strong>{{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }}</strong>.
                    @endif
                </p>

                <!-- CTA Buttons -->
                <div class="d-flex flex-column flex-sm-row gap-3 justify-content-center justify-content-lg-start mb-4">
                    <a href="#form-konsultasi" class="btn btn-brand btn-lg px-4 py-3 rounded-pill shadow-sm">
                        <i class="bi bi-send-fill me-2"></i> Minta Penawaran / Konsultasi
                    </a>
                    <a href="#layanan-utama" class="btn btn-outline-dark btn-lg px-4 py-3 rounded-pill">
                        <i class="bi bi-grid-fill me-2"></i> Jelajahi Layanan
                    </a>
                </div>

                <!-- Ringkasan Profil Singkat Pemilik -->
                <div class="p-3 rounded-3 bg-light border d-flex align-items-center gap-3 text-start">
                    <img src="{{ asset('images/gede-erik-aktama.jpg') }}" alt="{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}" class="rounded-circle object-fit-cover border border-2 border-primary shadow-sm" style="width: 56px; height: 56px;">
                    <div class="small">
                        <div class="text-muted" style="font-size: 0.75rem;">Dipimpin Langsung Oleh:</div>
                        <strong class="text-dark d-block">{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</strong>
                        <span class="text-secondary" style="font-size: 0.8rem;">{{ $settings['owner_title'] ?? 'Dosen Sistem Komputer & Fasilitator Nasional KKA Kemdikdasmen' }}</span>
                    </div>
                </div>
            </div>

            <!-- Ilustrasi / Ringkasan Unit Bisnis Card -->
            <div class="col-lg-5">
                <div class="card border-0 shadow-lg rounded-4 p-4 bg-white position-relative">
                    <div class="d-flex align-items-center justify-content-between border-bottom pb-3 mb-3">
                        <h6 class="fw-bold mb-0 text-dark"><i class="bi bi-layers-fill text-primary me-2"></i> Ekosistem Layanan</h6>
                        <span class="badge bg-success bg-opacity-10 text-success fw-semibold">Operasional Aktif</span>
                    </div>

                    <div class="list-group list-group-flush gap-2">
                        <a href="#jasa-website" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-primary bg-opacity-10 text-primary fs-5"><i class="bi bi-code-slash"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Jasa Rekayasa Website & Software</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Company profile, sekolah/kampus, & POS kasir</div>
                            </div>
                            <span class="badge bg-primary bg-opacity-10 text-primary" style="font-size: 0.65rem;">Layanan</span>
                        </a>

                        <a href="#pelatihan-ai" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-info bg-opacity-10 text-info fs-5"><i class="bi bi-robot"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Pelatihan AI & Koding (LPK)</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Workshop ASN, guru, & instansi berlisensi</div>
                            </div>
                            <span class="badge bg-info bg-opacity-10 text-info" style="font-size: 0.65rem;">Resmi LPK</span>
                        </a>

                        <a href="{{ $settings['invitation_url'] ?? 'https://undanganonline.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-pink bg-opacity-10 text-pink fs-5" style="background: rgba(236,72,153,0.1); color: #ec4899;"><i class="bi bi-heart-fill"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Undangan Online Digital</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Platform undangan pernikahan & adat interaktif</div>
                            </div>
                            <span class="badge bg-pink bg-opacity-10" style="background: rgba(236,72,153,0.1); color: #ec4899; font-size: 0.65rem;">Live SaaS <i class="bi bi-box-arrow-up-right ms-1"></i></span>
                        </a>

                        <a href="{{ $settings['coffee_app_url'] ?? 'https://coffee.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-warning bg-opacity-10 text-warning fs-5"><i class="bi bi-cup-hot-fill"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">{{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }}</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Roastery biji/bubuk kopi & suplai kafe</div>
                            </div>
                            <span class="badge bg-warning bg-opacity-25 text-dark" style="font-size: 0.65rem;">Unit Bisnis <i class="bi bi-box-arrow-up-right ms-1"></i></span>
                        </a>

                        <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-success bg-opacity-10 text-success fs-5"><i class="bi bi-mortarboard-fill"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Aktama Academy (LMS)</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Platform kursus koding & AI daring</div>
                            </div>
                            <span class="badge bg-success bg-opacity-10 text-success" style="font-size: 0.65rem;">Platform <i class="bi bi-box-arrow-up-right ms-1"></i></span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
