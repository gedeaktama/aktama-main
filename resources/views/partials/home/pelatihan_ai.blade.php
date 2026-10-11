<!-- SECTION: PELATIHAN KECERDASAN ARTIFISIAL (AI) -->
<section id="pelatihan-ai" class="py-5 bg-light border-bottom">
    <div class="container py-4">
        <div class="row align-items-end mb-4">
            <div class="col-lg-8">
                <span class="badge bg-info bg-opacity-10 text-info fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Pendidikan & Pelatihan' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Program Pelatihan Kecerdasan Artifisial (AI)' }}</h2>
                <p class="text-muted mb-0">
                    {{ $sectionConfig->subtitle ?? 'Membantu instansi pemerintah, institusi pendidikan, perusahaan, dan UMKM memanfaatkan teknologi AI untuk otomasi tugas administratif dan peningkatan produktivitas kerja nyata.' }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <a href="#form-konsultasi" class="btn btn-outline-primary rounded-pill btn-sm px-3">
                    <i class="bi bi-file-earmark-text me-1"></i> Permintaan Proposal Pelatihan
                </a>
            </div>
        </div>

        <div class="row g-4">
            @forelse($trainingPrograms as $program)
                <div class="col-md-6 col-lg-3">
                    <div class="card h-100 card-feature p-4 d-flex flex-column justify-content-between">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="badge bg-primary bg-opacity-10 text-primary small">
                                    {{ ucfirst(str_replace('-', ' ', $program->category)) }}
                                </span>
                                <span class="text-muted small"><i class="bi bi-clock me-1"></i>{{ $program->duration }}</span>
                            </div>

                            <h5 class="fw-bold text-dark fs-6 mb-2">{{ $program->title }}</h5>
                            <p class="text-muted small mb-3 leading-relaxed">{{ Str::limit($program->objectives, 100) }}</p>

                            <div class="border-top pt-2 mb-3">
                                <small class="text-muted d-block fw-semibold mb-1">Target Peserta:</small>
                                <small class="text-secondary">{{ $program->target_audience }}</small>
                            </div>

                            @if($program->syllabus && is_array($program->syllabus))
                                <div class="border-top pt-2 mb-3">
                                    <small class="text-muted d-block fw-semibold mb-1">Materi Inti:</small>
                                    <ul class="list-unstyled small text-muted mb-0" style="font-size: 0.75rem;">
                                        @foreach(array_slice($program->syllabus, 0, 2) as $syl)
                                            <li class="mb-1"><i class="bi bi-check2 text-success me-1"></i>{{ $syl }}</li>
                                        @endforeach
                                    </ul>
                                </div>
                            @endif
                        </div>

                        <div class="border-top pt-3 mt-2 d-flex justify-content-between align-items-center">
                            <span class="small fw-bold text-primary">{{ $program->price_info ?? 'Sesuai Penawaran' }}</span>
                            <a href="#form-konsultasi" class="btn btn-sm btn-light border rounded-pill">
                                Daftar <i class="bi bi-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            @empty
                <div class="col-12">
                    <div class="alert alert-info small">Katalog program pelatihan sedang dalam pembaruan berkala melalui admin.</div>
                </div>
            @endforelse
        </div>
    </div>
</section>
