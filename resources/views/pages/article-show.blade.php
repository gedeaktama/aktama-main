@extends('layouts.app')

@section('title', ($article->meta_title ?: $article->title) . ' | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', $article->meta_description ?: $article->summary)

@section('content')

    <!-- Header Breadcrumb & Judul -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-2 max-w-3xl">
            <nav aria-label="breadcrumb" class="mb-3">
                <ol class="breadcrumb small">
                    <li class="breadcrumb-item"><a href="{{ route('home') }}" class="text-decoration-none">Beranda</a></li>
                    <li class="breadcrumb-item"><a href="{{ route('articles.index') }}" class="text-decoration-none">Artikel</a></li>
                    <li class="breadcrumb-item active text-truncate" aria-current="page" style="max-width: 250px;">{{ $article->title }}</li>
                </ol>
            </nav>

            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                {{ $article->category?->name ?? 'Wawasan Teknologi' }}
            </span>
            <h1 class="display-6 fw-bold font-display text-dark mb-3">{{ $article->title }}</h1>

            <div class="d-flex align-items-center gap-3 small text-muted">
                <span><i class="bi bi-person me-1"></i> {{ $article->author }}</span>
                <span>&bull;</span>
                <span><i class="bi bi-calendar3 me-1"></i> {{ $article->published_at?->format('d F Y') ?? date('d F Y') }}</span>
            </div>
        </div>
    </section>

    <!-- Isi Artikel Lengkap -->
    <section class="py-5 bg-white">
        <div class="container py-2 max-w-3xl">
            @if($article->image)
                <div class="mb-4 text-center">
                    <img src="{{ asset('images/' . $article->image) }}" alt="{{ $article->title }}" class="img-fluid rounded-4 shadow-sm object-fit-cover w-100" style="max-height: 420px;">
                </div>
            @endif

            <div class="article-content fs-6 text-dark leading-relaxed mb-5" style="line-height: 1.8;">
                {!! $article->content !!}
            </div>

            <!-- Share Buttons -->
            <div class="p-4 rounded-4 bg-light border d-flex flex-wrap align-items-center justify-content-between gap-3 mb-5">
                <div>
                    <h6 class="fw-bold text-dark mb-1">Bagikan Artikel Ini:</h6>
                    <small class="text-muted">Bantu rekan atau instansi Anda mendapatkan wawasan ini.</small>
                </div>
                <div class="d-flex gap-2">
                    <a href="https://wa.me/?text={{ urlencode($article->title . ' - ' . url()->current()) }}" target="_blank" rel="noopener noreferrer" class="btn btn-success btn-sm rounded-pill px-3">
                        <i class="bi bi-whatsapp me-1"></i> Bagikan ke WhatsApp
                    </a>
                </div>
            </div>

            <!-- Artikel Terkait -->
            @if($relatedArticles->count() > 0)
                <div class="border-top pt-4">
                    <h5 class="fw-bold font-display text-dark mb-4">Artikel Terkait</h5>
                    <div class="row g-3">
                        @foreach($relatedArticles as $rel)
                            <div class="col-md-4">
                                <div class="card h-100 p-3 rounded-3 border bg-light">
                                    <h6 class="fw-bold text-dark fs-6 mb-2">
                                        <a href="{{ route('articles.show', $rel->slug) }}" class="text-dark text-decoration-none hover-primary">
                                            {{ $rel->title }}
                                        </a>
                                    </h6>
                                    <small class="text-muted mt-auto">{{ $rel->published_at?->format('d M Y') }}</small>
                                </div>
                            </div>
                        @endforeach
                    </div>
                </div>
            @endif
        </div>
    </section>

@endsection
