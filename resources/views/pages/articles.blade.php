@extends('layouts.app')

@section('title', 'Artikel & Wawasan Teknologi | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Kumpulan artikel edukatif, panduan kecerdasan artifisial (AI), tips keamanan website bisnis, dan literasi koding komputasi.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Pusat Literasi & Wawasan</span>
            <h1 class="display-6 fw-bold font-display text-dark">Artikel & Berita Teknologi Terkini</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Wawasan praktis seputar Kecerdasan Artifisial, keamanan website bisnis, dan kiat otomasi operasional digital.
            </p>
        </div>
    </section>

    <!-- Daftar Artikel -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <div class="row g-4 mb-5">
                @forelse($articles as $art)
                    <div class="col-md-6 col-lg-4">
                        <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                @if($art->image)
                                    <a href="{{ route('articles.show', $art->slug) }}" class="d-block mb-3 overflow-hidden rounded-3">
                                        <img src="{{ asset('images/' . $art->image) }}" alt="{{ $art->title }}" class="img-fluid w-100 object-fit-cover shadow-xs" style="height: 180px;">
                                    </a>
                                @endif

                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small">
                                        {{ $art->category?->name ?? 'Umum' }}
                                    </span>
                                    <small class="text-muted">{{ $art->published_at?->format('d M Y') ?? 'Baru' }}</small>
                                </div>

                                <h3 class="fw-bold text-dark fs-6 mb-2">
                                    <a href="{{ route('articles.show', $art->slug) }}" class="text-dark text-decoration-none hover-primary">
                                        {{ $art->title }}
                                    </a>
                                </h3>
                                <p class="text-muted small leading-relaxed mb-4">{{ $art->summary }}</p>
                            </div>

                            <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                                <small class="text-muted" style="font-size: 0.75rem;">
                                    Penulis: <strong class="text-dark">{{ $art->author }}</strong>
                                </small>
                                <a href="{{ route('articles.show', $art->slug) }}" class="btn btn-sm btn-light border rounded-pill">
                                    Baca <i class="bi bi-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-light border text-center small text-muted">Belum ada artikel yang dipublikasikan.</div>
                    </div>
                @endforelse
            </div>

            <!-- Pagination -->
            <div class="d-flex justify-content-center">
                {{ $articles->links('pagination::bootstrap-5') }}
            </div>
        </div>
    </section>

@endsection
