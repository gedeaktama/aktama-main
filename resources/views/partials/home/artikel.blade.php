<!-- SECTION: ARTIKEL & BLOG TERBARU -->
<section id="artikel" class="py-5 bg-white border-bottom">
    <div class="container py-4">
        <div class="row align-items-end mb-4">
            <div class="col-lg-8">
                <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Wawasan & Literasi' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Artikel & Berita Teknologi Terbaru' }}</h2>
                <p class="text-muted mb-0">
                    {{ $sectionConfig->subtitle ?? 'Artikel edukatif dan wawasan perkembangan teknologi terkini.' }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <a href="{{ route('articles.index') }}" class="btn btn-outline-dark rounded-pill btn-sm px-3">
                    <i class="bi bi-journal-text me-1"></i> Buka Semua Artikel
                </a>
            </div>
        </div>

        <div class="row g-4">
            @forelse($articles as $art)
                <div class="col-md-6 col-lg-4">
                    <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between border rounded-4 shadow-sm hover-lift">
                        <div>
                            @if($art->image)
                                <a href="{{ route('articles.show', $art->slug) }}" class="d-block mb-3 overflow-hidden rounded-3">
                                    <img src="{{ asset('images/' . $art->image) }}" alt="{{ $art->title }}" class="img-fluid w-100 object-fit-cover shadow-xs" style="height: 180px;">
                                </a>
                            @endif

                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <span class="badge bg-primary bg-opacity-10 text-primary small">{{ $art->category?->name ?? 'Wawasan' }}</span>
                                <small class="text-muted"><i class="bi bi-clock me-1"></i>{{ max(3, ceil(str_word_count(strip_tags($art->content)) / 180)) }} mnt</small>
                            </div>

                            <h5 class="fw-bold text-dark fs-6 mb-2">
                                <a href="{{ route('articles.show', $art->slug) }}" class="text-dark text-decoration-none hover-primary">
                                    {{ $art->title }}
                                </a>
                            </h5>
                            <p class="text-muted small mb-3 leading-relaxed">{{ Str::limit($art->summary, 120) }}</p>
                        </div>

                        <div class="mt-auto d-flex justify-content-between align-items-center border-top pt-3 small text-muted">
                            <span style="font-size: 0.75rem;">Oleh: <strong class="text-dark">{{ $art->author }}</strong></span>
                            <a href="{{ route('articles.show', $art->slug) }}" class="btn btn-sm btn-light border rounded-pill px-3">
                                Baca <i class="bi bi-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            @empty
                <div class="col-12">
                    <div class="alert alert-light border small text-muted text-center">Belum ada artikel dipublikasikan.</div>
                </div>
            @endforelse
        </div>
    </div>
</section>
