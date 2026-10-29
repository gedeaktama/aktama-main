<!-- SECTION: TENTANG KAMI & PROFIL PEMILIK -->
<section id="tentang-kami" class="py-5 bg-light border-bottom">
    <div class="container py-4">
        <div class="row align-items-center g-5">
            <!-- Kolom Foto Direktur & Kredensial -->
            <div class="col-lg-5">
                <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white text-center p-4">
                    <div class="position-relative d-inline-block mx-auto mb-3">
                        <img src="{{ asset('images/gede-erik-aktama.jpg') }}" alt="{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}" class="img-fluid rounded-4 shadow object-fit-cover" style="max-height: 340px; width: auto;">
                        <span class="position-absolute bottom-0 start-50 translate-middle-x badge bg-primary px-3 py-2 rounded-pill shadow-sm small text-white" style="margin-bottom: -10px;">
                            <i class="bi bi-patch-check-fill me-1"></i> Penanggung Jawab Teknis
                        </span>
                    </div>

                    <div class="mt-3">
                        <h4 class="fw-bold font-display text-dark mb-1">{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</h4>
                        <p class="text-primary fw-semibold small mb-2">{{ $settings['owner_title'] ?? 'Dosen Sistem Komputer & Fasilitator Nasional KKA Kemdikdasmen' }}</p>
                    </div>

                    <div class="d-flex justify-content-center gap-2 flex-wrap border-top pt-3 small">
                        <span class="badge bg-light text-dark border"><i class="bi bi-mortarboard text-primary me-1"></i> Akademisi Komputer</span>
                        <span class="badge bg-light text-dark border"><i class="bi bi-award text-warning me-1"></i> Fasilitator KKA</span>
                        <span class="badge bg-light text-dark border"><i class="bi bi-shield-check text-success me-1"></i> Software Architect</span>
                    </div>

                    <div class="mt-3">
                        <a href="{{ $settings['profile_url'] ?? 'https://profil.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm rounded-pill w-100 py-2 fw-semibold d-flex align-items-center justify-content-center gap-2">
                            <i class="bi bi-mortarboard-fill"></i>
                            <span>Buka Portofolio & Riset SINTA</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Kolom Legalitas Perusahaan & Visi -->
            <div class="col-lg-7">
                <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Legalitas & Kepemimpinan' }}</span>
                <h2 class="fw-bold font-display text-dark mb-3">{{ $sectionConfig->title ?? 'Komitmen Kualitas & Integritas Teknis' }}</h2>
                
                <p class="text-muted leading-relaxed mb-4">
                    {{ $sectionConfig->subtitle ?? ($settings['owner_bio'] ?? 'Dosen pada Program Studi Sistem Komputer, Universitas Parna Raya, serta Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen. Menjamin bahwa seluruh layanan perangkat lunak, sistem informasi, dan kurikulum pelatihan dikembangkan secara profesional dan dapat dipertanggungjawabkan.') }}
                </p>

                <!-- Card Dokumen Legalitas NIB & LPK -->
                <div class="p-4 rounded-4 bg-white border shadow-sm mb-4">
                    <div class="row align-items-center g-3">
                        <div class="col-md-3 text-center">
                            <img src="{{ asset($settings['seal_path'] ?? 'images/logo-seal-aktama.png') }}" alt="Cap Resmi PT Aktama Digital Antika" style="max-height: 85px;" class="img-fluid mb-2">
                            <span class="badge bg-success bg-opacity-10 text-success small d-block">Badan Usaha Resmi</span>
                        </div>
                        <div class="col-md-6 border-start border-md-start">
                            <h5 class="fw-bold text-dark font-display mb-1">{{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}</h5>
                            <div class="text-primary fw-bold small mb-1"><i class="bi bi-file-earmark-check me-1"></i>NIB: {{ $settings['nib_number'] ?? '1703250057018' }}</div>
                            <div class="text-secondary small mb-2"><i class="bi bi-building-check me-1"></i>Unit: {{ $settings['lpk_status'] ?? 'Lembaga Pelatihan Kerja (LPK) Resmi' }}</div>
                            <p class="text-muted small mb-0" style="font-size: 0.8rem;">Terdaftar resmi pada sistem perizinan berusaha Republik Indonesia untuk jasa perangkat lunak dan pendidikan vokasi.</p>
                        </div>
                        <div class="col-md-3 text-center">
                            <a href="{{ asset('images/nib-document.jpg') }}" target="_blank" class="d-inline-block position-relative border rounded-3 overflow-hidden shadow-sm hover-shadow" title="Klik untuk memperbesar dokumen izin">
                                <img src="{{ asset('images/nib-document.jpg') }}" alt="Dokumen NIB Resmi" style="height: 95px; width: 75px; object-fit: cover;">
                                <span class="position-absolute bottom-0 start-0 end-0 bg-dark bg-opacity-75 text-white small" style="font-size: 0.65rem;">Periksa NIB</span>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="row g-3">
                    <div class="col-sm-6">
                        <div class="p-3 rounded-3 bg-white border h-100">
                            <div class="text-primary fw-bold mb-1"><i class="bi bi-shield-lock-fill me-1"></i> Bebas Injeksi Judol</div>
                            <small class="text-muted">Arsitektur Laravel terproteksi penuh dari celah injeksi script malware judi online yang kerap merusak reputasi CMS lama.</small>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="p-3 rounded-3 bg-white border h-100">
                            <div class="text-primary fw-bold mb-1"><i class="bi bi-headset me-1"></i> Pendampingan Nyata</div>
                            <small class="text-muted">Konsultasi langsung dengan tim pengembang dan akademisi teknologi, bukan calo atau perantara pihak ketiga.</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
