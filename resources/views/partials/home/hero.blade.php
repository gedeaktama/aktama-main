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
                        <a href="#pelatihan-ai" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-info bg-opacity-10 text-info fs-5"><i class="bi bi-robot"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Pelatihan AI & Komputer</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Untuk instansi, kantor, guru, & bisnis</div>
                            </div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="#jasa-website" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-primary bg-opacity-10 text-primary fs-5"><i class="bi bi-globe"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Jasa Website & Aplikasi Bisnis</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Company profile, sekolah, & POS kasir</div>
                            </div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="#aktama-coffee" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-warning bg-opacity-10 text-warning fs-5"><i class="bi bi-cup-hot"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">{{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }}</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Pasokan kopi kemasan retail & grosir kafe</div>
                            </div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="#undangan-online" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3">
                            <div class="p-2 rounded-3 bg-danger bg-opacity-10 text-danger fs-5"><i class="bi bi-heart"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-dark small">Undangan Online Digital</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Template elegan pernikahan & acara</div>
                            </div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="{{ $settings['academy_url'] ?? 'http://localhost:8080/aktama/public' }}" target="_blank" rel="noopener noreferrer" class="list-group-item list-group-item-action border rounded-3 p-3 d-flex align-items-center gap-3 bg-success bg-opacity-10">
                            <div class="p-2 rounded-3 bg-success text-white fs-5"><i class="bi bi-mortarboard-fill"></i></div>
                            <div class="flex-grow-1">
                                <div class="fw-bold text-success small">Aktama Academy (LMS)</div>
                                <div class="text-muted" style="font-size: 0.75rem;">Platform kursus & sertifikasi online</div>
                            </div>
                            <i class="bi bi-box-arrow-up-right text-success small"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
