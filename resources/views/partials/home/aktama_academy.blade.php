<!-- SECTION: AKTAMA ACADEMY (KURSUS ONLINE) -->
<section id="aktama-academy" class="py-5 bg-light border-bottom">
    <div class="container py-4">
        <div class="row align-items-center g-4">
            <div class="col-lg-4">
                <span class="badge bg-success bg-opacity-10 text-success fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'E-Learning Brand' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Aktama Academy' }}</h2>
                <p class="text-muted small leading-relaxed mb-4">
                    {{ $sectionConfig->subtitle ?? 'Platform kursus dan pembelajaran teknologi informasi untuk mengasah keahlian komputasi praktis. Dilengkapi kurikulum terstruktur, modul latihan, dan evaluasi pemahaman.' }}
                </p>
                <a href="{{ $settings['academy_url'] ?? 'http://localhost:8080/aktama/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-success rounded-pill btn-sm px-4">
                    <i class="bi bi-box-arrow-up-right me-1"></i> Kunjungi Portal Academy
                </a>
            </div>

            <div class="col-lg-8">
                <div class="row g-3">
                    @forelse($courses as $course)
                        <div class="col-md-6">
                            <div class="card card-feature p-4 h-100">
                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <span class="badge bg-secondary bg-opacity-10 text-dark small">{{ $course->level }}</span>
                                    <span class="fw-bold text-primary small">Rp {{ number_format($course->price, 0, ',', '.') }}</span>
                                </div>
                                <h5 class="fw-bold text-dark fs-6 mb-2">{{ $course->title }}</h5>
                                <p class="text-muted small mb-3">{{ $course->summary }}</p>
                                <div class="mt-auto">
                                    <a href="{{ $settings['academy_url'] ?? 'http://localhost:8080/aktama/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-success border rounded-pill w-100">
                                        Buka Kursus di Academy <i class="bi bi-box-arrow-up-right ms-1"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    @empty
                        <div class="col-12">
                            <div class="alert alert-light border small text-muted">Kursus sedang dipersiapkan.</div>
                        </div>
                    @endforelse
                </div>
            </div>
        </div>
    </div>
</section>
