<!-- SECTION: PORTOFOLIO TERVERIFIKASI -->
<section id="portofolio" class="py-5 bg-white border-bottom">
    <div class="container py-4">
        <div class="text-center max-w-2xl mx-auto mb-5">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Rekam Jejak Proyek' }}</span>
            <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Portofolio & Studi Kasus Terverifikasi' }}</h2>
            <p class="text-muted small">
                {{ $sectionConfig->subtitle ?? 'Implementasi nyata yang telah dibangun dengan standar performa dan kehandalan teruji.' }}
            </p>
        </div>

        <div class="row g-4">
            @forelse($portfolios as $port)
                <div class="col-md-4">
                    <div class="card card-feature p-4 h-100">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge bg-light text-muted small">{{ $port->client_type }}</span>
                            <span class="text-muted small fw-semibold">{{ $port->project_year }}</span>
                        </div>
                        @if($port->image)
                            <img src="{{ asset('images/' . $port->image) }}" alt="{{ $port->title }}" class="img-fluid rounded-3 mb-2 w-100 object-fit-cover shadow-xs" style="max-height: 140px;">
                        @endif
                        <h5 class="fw-bold text-dark fs-6 mb-2">{{ $port->title }}</h5>
                        <p class="text-muted small mb-3">{{ Str::limit(strip_tags($port->description), 140) }}</p>
                        <div class="mt-auto border-top pt-2">
                            <small class="text-muted d-block" style="font-size: 0.75rem;">Stack Teknologi:</small>
                            <span class="badge bg-primary bg-opacity-10 text-primary small font-monospace">{{ $port->technology }}</span>
                        </div>
                    </div>
                </div>
            @empty
                <div class="col-12">
                    <div class="alert alert-light border small text-muted">Portofolio sedang dirapikan.</div>
                </div>
            @endforelse
        </div>
    </div>
</section>
