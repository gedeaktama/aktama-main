<!-- SECTION: JASA PEMBUATAN WEBSITE & SOLUSI DIGITAL -->
<section id="jasa-website" class="py-5 bg-white border-bottom">
    <div class="container py-4">
        <div class="row align-items-end mb-4">
            <div class="col-lg-8">
                <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Software House' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Jasa Pembuatan Website & Solusi Digital' }}</h2>
                <p class="text-muted mb-0">
                    {{ $sectionConfig->subtitle ?? 'Bangun website dan aplikasi bisnis yang cepat, elegan, dan terbebas dari celah malware script judi online berkat arsitektur modern Laravel.' }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <a href="#form-konsultasi" class="btn btn-outline-dark rounded-pill btn-sm px-3">
                    <i class="bi bi-whatsapp text-success me-1"></i> Konsultasi Kebutuhan Web
                </a>
            </div>
        </div>

        <div class="row g-4">
            @forelse($services as $service)
                <div class="col-md-6 col-lg-3">
                    <div class="card h-100 card-feature p-4 d-flex flex-column justify-content-between">
                        <div>
                            <div class="rounded-3 bg-light text-primary d-inline-flex p-3 mb-3 fs-4">
                                <i class="bi {{ $service->icon }}"></i>
                            </div>
                            <h5 class="fw-bold text-dark fs-6 mb-2">{{ $service->title }}</h5>
                            <p class="text-muted small mb-3 leading-relaxed">{{ $service->excerpt }}</p>

                            @if($service->features && is_array($service->features))
                                <ul class="list-unstyled small text-muted border-top pt-3 mb-3" style="font-size: 0.8rem;">
                                    @foreach($service->features as $feat)
                                        <li class="mb-1 d-flex align-items-start gap-1">
                                            <i class="bi bi-check-circle-fill text-primary small mt-1"></i>
                                            <span>{{ $feat }}</span>
                                        </li>
                                    @endforeach
                                </ul>
                            @endif
                        </div>

                        <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                            <span class="small fw-bold text-dark">{{ $service->price_starting }}</span>
                            <a href="#form-konsultasi" class="btn btn-sm btn-brand rounded-pill px-3">
                                Pesan
                            </a>
                        </div>
                    </div>
                </div>
            @empty
                <div class="col-12">
                    <div class="alert alert-info small">Layanan sedang dimuat.</div>
                </div>
            @endforelse
        </div>
    </div>
</section>
