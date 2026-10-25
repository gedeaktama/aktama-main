<!-- SEKSI TESTIMONI & ULASAN KLIEN / PESERTA PELATIHAN -->
<section class="py-5 bg-white border-bottom position-relative">
    <div class="container py-lg-4">
        <div class="text-center max-w-2xl mx-auto mb-5">
            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                {{ $sectionConfig->badge ?? 'Kepuasan Stakeholder' }}
            </span>
            <h2 class="display-6 fw-bold font-display text-dark tracking-tight mb-2">
                {{ $sectionConfig->title ?? 'Apa Kata Peserta Pelatihan & Mitra Kami?' }}
            </h2>
            <p class="text-muted small mb-0">
                {{ $sectionConfig->subtitle ?? 'Testimoni nyata dari perwakilan instansi pemerintahan, pendidik sekolah, serta pemilik usaha yang telah bermitra dengan PT Aktama Digital Antika.' }}
            </p>
        </div>

        <div class="row g-4">
            <!-- Testimoni 1: Instansi Kepolisian / Administrasi -->
            <div class="col-md-6 col-lg-3">
                <div class="card h-100 p-4 rounded-4 border bg-light shadow-xs d-flex flex-column justify-content-between hover-lift">
                    <div>
                        <div class="d-flex text-warning mb-3">
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <p class="text-dark small leading-relaxed mb-4" style="font-style: italic;">
                            "Materi prompt engineering yang dibawakan Pak Gede Erik sangat aplikatif. Staf kami kini mampu merapikan draf telaah staf dan notula rapat dinas berlembar-lembar hanya dalam waktu kurang dari 20 menit dengan format baku."
                        </p>
                    </div>
                    <div class="border-top pt-3 d-flex align-items-center gap-3">
                        <div class="rounded-circle bg-danger bg-opacity-10 text-danger p-2 fw-bold d-flex align-items-center justify-content-center" style="width: 42px; height: 42px; min-width: 42px;">
                            <i class="bi bi-shield-lock-fill"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark small">Bagian SDM & Minops</strong>
                            <small class="text-muted" style="font-size: 0.72rem;">Instansi Kepolisian Daerah</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Testimoni 2: Pendidik & Sekolah -->
            <div class="col-md-6 col-lg-3">
                <div class="card h-100 p-4 rounded-4 border bg-light shadow-xs d-flex flex-column justify-content-between hover-lift">
                    <div>
                        <div class="d-flex text-warning mb-3">
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <p class="text-dark small leading-relaxed mb-4" style="font-style: italic;">
                            "Sebagai guru, program Koding & Kecerdasan Artifisial (KKA) dari LPK Aktama benar-benar membuka wawasan kami. Penyampaian materi logika komputasi sangat mudah dipahami bahkan untuk guru non-TIK sekalipun."
                        </p>
                    </div>
                    <div class="border-top pt-3 d-flex align-items-center gap-3">
                        <div class="rounded-circle bg-primary bg-opacity-10 text-primary p-2 fw-bold d-flex align-items-center justify-content-center" style="width: 42px; height: 42px; min-width: 42px;">
                            <i class="bi bi-mortarboard-fill"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark small">Koordinator Kurikulum</strong>
                            <small class="text-muted" style="font-size: 0.72rem;">Sekolah Menengah Kejuruan</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Testimoni 3: Klien Website & Sistem Informasi -->
            <div class="col-md-6 col-lg-3">
                <div class="card h-100 p-4 rounded-4 border bg-light shadow-xs d-flex flex-column justify-content-between hover-lift">
                    <div>
                        <div class="d-flex text-warning mb-3">
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <p class="text-dark small leading-relaxed mb-4" style="font-style: italic;">
                            "Website lembaga kami sebelumnya sering bermasalah dan terkena peringatan Google. Setelah direkayasa ulang dengan arsitektur Laravel oleh tim Aktama Digital, website super cepat dan 100% aman tanpa celah."
                        </p>
                    </div>
                    <div class="border-top pt-3 d-flex align-items-center gap-3">
                        <div class="rounded-circle bg-success bg-opacity-10 text-success p-2 fw-bold d-flex align-items-center justify-content-center" style="width: 42px; height: 42px; min-width: 42px;">
                            <i class="bi bi-globe2"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark small">Pengurus Yayasan Pendidikan</strong>
                            <small class="text-muted" style="font-size: 0.72rem;">Klien Jasa Rekayasa Web</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Testimoni 4: Aplikasi Kasir & POS UMKM -->
            <div class="col-md-6 col-lg-3">
                <div class="card h-100 p-4 rounded-4 border bg-light shadow-xs d-flex flex-column justify-content-between hover-lift">
                    <div>
                        <div class="d-flex text-warning mb-3">
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill me-1"></i>
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <p class="text-dark small leading-relaxed mb-4" style="font-style: italic;">
                            "Aplikasi kasir dan stok multi-satuan sangat membantu operasional toko grosir kami. Selisih stok terpantau harian dan buku piutang pelanggan tidak lagi tercecer secara manual. Sangat direkomendasikan!"
                        </p>
                    </div>
                    <div class="border-top pt-3 d-flex align-items-center gap-3">
                        <div class="rounded-circle bg-warning bg-opacity-10 text-warning p-2 fw-bold d-flex align-items-center justify-content-center" style="width: 42px; height: 42px; min-width: 42px;">
                            <i class="bi bi-receipt-cutoff"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark small">Pemilik Usaha Grosir</strong>
                            <small class="text-muted" style="font-size: 0.72rem;">Sistem POS & Stok Retail</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
