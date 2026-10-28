<!-- SEKSI DOKUMENTASI KEGIATAN & PELATIHAN RIIL (SOCIAL PROOF LPK) -->
<section class="py-5 bg-light border-bottom position-relative">
    <div class="container py-lg-4">
        <div class="text-center max-w-2xl mx-auto mb-5">
            <span class="badge bg-success bg-opacity-10 text-success fw-bold text-uppercase px-3 py-1 mb-2">
                {{ $sectionConfig->badge ?? 'Dokumentasi Lapangan' }}
            </span>
            <h2 class="display-6 fw-bold font-display text-dark tracking-tight mb-2">
                {{ $sectionConfig->title ?? 'Dokumentasi Kelas Pelatihan & Implementasi Lapangan' }}
            </h2>
            <p class="text-muted small mb-0">
                {{ $sectionConfig->subtitle ?? 'Bukti dedikasi transfer teknologi nyata melalui workshop tatap muka, bimbingan teknis AI di instansi pemerintah, dan serah terima sistem informasi.' }}
            </p>
        </div>

        <div class="row g-4">
            <!-- Galeri 1: Pelatihan Instansi Kepolisian -->
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 border-0 rounded-4 overflow-hidden shadow-sm bg-white hover-lift">
                    <div class="position-relative">
                        <div class="ratio ratio-16x9 bg-dark">
                            <img src="{{ asset('images/articles/article-ai-polres-mitra.jpg') }}" alt="Pelatihan AI Instansi Kepolisian" class="object-fit-cover w-100 h-100" loading="lazy">
                        </div>
                        <span class="position-absolute top-0 end-0 m-3 badge bg-danger text-white shadow-sm" style="z-index: 2;">
                            <i class="bi bi-shield-check me-1"></i> In-House Instansi
                        </span>
                    </div>
                    <div class="p-4">
                        <h5 class="fw-bold text-dark fs-6 mb-2">Pelatihan Generative AI Administrasi di Instansi Kepolisian</h5>
                        <p class="text-muted small mb-3 leading-relaxed">
                            Bimbingan teknis pembuatan draf telaah staf, notula rapat dinas, dan pengolahan spreadsheet naskah dinas bersama perwira dan bintara di Polres Minahasa Tenggara.
                        </p>
                        <span class="text-primary small fw-semibold">
                            <i class="bi bi-geo-alt me-1"></i> Mitra, Sulawesi Utara
                        </span>
                    </div>
                </div>
            </div>

            <!-- Galeri 2: Pelatihan Pendidik & Guru KKA -->
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 border-0 rounded-4 overflow-hidden shadow-sm bg-white hover-lift">
                    <div class="position-relative">
                        <div class="ratio ratio-16x9 bg-dark">
                            <img src="{{ asset('images/articles/article-ai-guru.jpg') }}" alt="Pelatihan Guru KKA" class="object-fit-cover w-100 h-100" loading="lazy">
                        </div>
                        <span class="position-absolute top-0 end-0 m-3 badge bg-primary text-white shadow-sm" style="z-index: 2;">
                            <i class="bi bi-mortarboard me-1"></i> Literasi Nasional
                        </span>
                    </div>
                    <div class="p-4">
                        <h5 class="fw-bold text-dark fs-6 mb-2">Workshop Koding & Kecerdasan Artifisial Guru Sekolah</h5>
                        <p class="text-muted small mb-3 leading-relaxed">
                            Sosialisasi dan pelatihan kurikulum KKA Kemdikdasmen bagi guru sekolah dasar dan menengah untuk mengintegrasikan AI secara aman dan etis di ruang kelas.
                        </p>
                        <span class="text-primary small fw-semibold">
                            <i class="bi bi-award me-1"></i> LPK PT Aktama Digital Antika
                        </span>
                    </div>
                </div>
            </div>

            <!-- Galeri 3: Riset & Rekayasa Software Bebas Malware -->
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 border-0 rounded-4 overflow-hidden shadow-sm bg-white hover-lift">
                    <div class="position-relative">
                        <div class="ratio ratio-16x9 bg-dark">
                            <img src="{{ asset('images/articles/article-web-security.jpg') }}" alt="Rekayasa Keamanan Web" class="object-fit-cover w-100 h-100" loading="lazy">
                        </div>
                        <span class="position-absolute top-0 end-0 m-3 badge bg-success text-white shadow-sm" style="z-index: 2;">
                            <i class="bi bi-code-slash me-1"></i> Rekayasa Sistem
                        </span>
                    </div>
                    <div class="p-4">
                        <h5 class="fw-bold text-dark fs-6 mb-2">Asistensi & Rekayasa Keamanan Web Anti-Malware Judol</h5>
                        <p class="text-muted small mb-3 leading-relaxed">
                            Pendampingan dan audit keamanan website sekolah dan bisnis guna memulihkan serta memproteksi total portal publik dari risiko pembobolan dan peretasan situs judi online.
                        </p>
                        <span class="text-primary small fw-semibold">
                            <i class="bi bi-check2-circle me-1"></i> Arsitektur Laravel Standar Industri
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="text-center mt-4">
            <a href="{{ route('training') }}" class="btn btn-outline-primary rounded-pill px-4 btn-sm fw-semibold">
                <i class="bi bi-journal-text me-1"></i> Lihat Rincian Semua Program Pelatihan LPK
            </a>
        </div>
    </div>
</section>
