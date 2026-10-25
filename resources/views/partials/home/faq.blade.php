<!-- SEKSI FAQ (PERTANYAAN YANG SERING DIAJUKAN) -->
<section class="py-5 bg-white border-bottom position-relative" id="faq-seksi">
    <div class="container py-lg-4">
        <div class="text-center max-w-2xl mx-auto mb-5">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">
                {{ $sectionConfig->badge ?? 'Informasi & Kejelasan Layanan' }}
            </span>
            <h2 class="display-6 fw-bold font-display text-dark tracking-tight mb-2">
                {{ $sectionConfig->title ?? 'Pertanyaan yang Sering Diajukan (FAQ)' }}
            </h2>
            <p class="text-muted small mb-0">
                {{ $sectionConfig->subtitle ?? 'Jawaban transparan seputar legalitas pelatihan LPK, garansi keamanan rekayasa website, serta prosedur kolaborasi resmi bersama PT Aktama Digital Antika.' }}
            </p>
        </div>

        <div class="row justify-content-center">
            <div class="col-lg-9">
                <div class="accordion accordion-flush rounded-4 border overflow-hidden shadow-xs" id="accordionFaqAktama">
                    
                    <!-- FAQ 1: Legalitas LPK & Sertifikat -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button fw-bold text-dark py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                <i class="bi bi-patch-check-fill text-success me-2 fs-5"></i>
                                Apakah sertifikat pelatihan dari Aktama Digital resmi dan berpayung hukum?
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionFaqAktama">
                            <div class="accordion-body text-secondary small leading-relaxed pt-0 pb-4">
                                <strong>Ya, sepenuhnya resmi.</strong> Pelatihan diselenggarakan oleh unit Lembaga Pelatihan Kerja (LPK) <strong>PT Aktama Digital Antika</strong> yang terdaftar secara sah dengan Nomor Induk Berusaha (NIB) <strong>1703250057018</strong>. Setiap peserta yang lulus evaluasi kompetensi berhak memperoleh sertifikat fisik maupun digital ber-barcode verifikasi resmi yang diakui untuk portofolio kedinasan, SKP ASN, maupun pengembangan karir profesional.
                            </div>
                        </div>
                    </div>

                    <!-- FAQ 2: Keamanan dari Hacker & Judol -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingTwo">
                            <button class="accordion-button collapsed fw-bold text-dark py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                <i class="bi bi-shield-lock-fill text-primary me-2 fs-5"></i>
                                Mengapa website buatan Aktama Digital dijamin kebal dari celah peretasan situs judi online (judol)?
                            </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionFaqAktama">
                            <div class="accordion-body text-secondary small leading-relaxed pt-0 pb-4">
                                Lebih dari 90% peretasan judi online menimpa website WordPress akibat celah keamanan ribuan plugin pihak ketiga. PT Aktama Digital Antika membangun perangkat lunak menggunakan <strong>arsitektur framework Laravel modern</strong> yang murni bebas dari plugin usang. Seluruh query database terlindungi dari SQL Injection (*PDO Prepared Statements*), formulir dilengkapi enkripsi token CSRF, proteksi brute-force login aktif, dan folder media diproteksi dengan konfigurasi server ketat yang menolak eksekusi file script PHP berbahaya.
                            </div>
                        </div>
                    </div>

                    <!-- FAQ 3: Pelatihan Luar Daerah & In-House -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingThree">
                            <button class="accordion-button collapsed fw-bold text-dark py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                <i class="bi bi-geo-alt-fill text-danger me-2 fs-5"></i>
                                Apakah Aktama melayani pelatihan in-house tatap muka untuk instansi di luar kota?
                            </button>
                        </h2>
                        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionFaqAktama">
                            <div class="accordion-body text-secondary small leading-relaxed pt-0 pb-4">
                                <strong>Tentu saja.</strong> Kami melayani pelatihan tatap muka langsung (*onsite in-house training*) di lokasi instansi pemohon di seluruh Indonesia, maupun pelatihan daring interaktif (*webinar intensive*). Tim narasumber dan instruktur dipimpin langsung oleh <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong> (Fasilitator Nasional KKA Kemdikdasmen). Silabus materi dapat disesuaikan secara khusus sesuai kebutuhan dinas atau organisasi Anda.
                            </div>
                        </div>
                    </div>

                    <!-- FAQ 4: Waktu Pengerjaan & Alur Pemesanan -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingFour">
                            <button class="accordion-button collapsed fw-bold text-dark py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                                <i class="bi bi-clock-history text-info me-2 fs-5"></i>
                                Berapa lama estimasi pembuatan website atau sistem informasi kustom?
                            </button>
                        </h2>
                        <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#accordionFaqAktama">
                            <div class="accordion-body text-secondary small leading-relaxed pt-0 pb-4">
                                Untuk website profil instansi/sekolah standar membutuhkan waktu <strong>7 hingga 14 hari kerja</strong>. Sedangkan untuk sistem informasi kustom atau aplikasi kasir berskala menengah membutuhkan waktu <strong>3 hingga 6 minggu</strong>, mencakup tahap analisis kebutuhan (KAK), perancangan database, coding, uji keamanan (penetration test awal), dan pelatihan operator.
                            </div>
                        </div>
                    </div>

                    <!-- FAQ 5: Garansi & Maintenance Pasca Rilis -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingFive">
                            <button class="accordion-button collapsed fw-bold text-dark py-3" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
                                <i class="bi bi-tools text-warning me-2 fs-5"></i>
                                Bagaimana dengan pemeliharaan (maintenance) dan garansi pasca peluncuran?
                            </button>
                        </h2>
                        <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive" data-bs-parent="#accordionFaqAktama">
                            <div class="accordion-body text-secondary small leading-relaxed pt-0 pb-4">
                                Seluruh proyek rekayasa perangkat lunak kami dilindungi <strong>Garansi Bebas Bug (Free Bug Fix)</strong> selama minimal 3 hingga 6 bulan pasca serah terima. Kami juga menyediakan paket pemeliharaan berkala yang mencakup pemantauan keamanan server, pencadangan database rutin (cloud backup), serta konsultasi teknis darurat via WhatsApp.
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <div class="text-center mt-5">
            <p class="text-muted small mb-2">Punya pertanyaan spesifik mengenai kebutuhan organisasi Anda?</p>
            <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6285341026331' }}?text={{ urlencode('Halo PT Aktama Digital Antika, saya ingin berkonsultasi mengenai pertanyaan layanan.') }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-success rounded-pill px-4 btn-sm fw-semibold">
                <i class="bi bi-whatsapp me-1"></i> Tanyakan Langsung via WhatsApp
            </a>
        </div>
    </div>
</section>
