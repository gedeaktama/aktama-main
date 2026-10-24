@extends('layouts.app')

@section('title', ($article->meta_title ?: $article->title) . ' | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', $article->meta_description ?: $article->summary)

@section('content')

    <style>
        .article-content h2 {
            font-size: 1.55rem;
            font-weight: 700;
            color: #0f172a;
            margin-top: 2.25rem;
            margin-bottom: 1.1rem;
            border-left: 4px solid #4f46e5;
            padding-left: 0.85rem;
            line-height: 1.35;
        }
        .article-content h3 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1e293b;
            margin-top: 1.75rem;
            margin-bottom: 0.85rem;
        }
        .article-content p {
            margin-bottom: 1.35rem;
            color: #334155;
            font-size: 1.05rem;
            line-height: 1.85;
        }
        .article-content ul, .article-content ol {
            margin-bottom: 1.6rem;
            padding-left: 1.6rem;
            color: #334155;
            font-size: 1.02rem;
            line-height: 1.8;
        }
        .article-content li {
            margin-bottom: 0.6rem;
        }
        .article-content blockquote {
            border-left: 4px solid #6366f1;
            background: #f8fafc;
            padding: 1.25rem 1.5rem;
            border-radius: 0 0.75rem 0.75rem 0;
            font-style: italic;
            color: #475569;
            margin: 2rem 0;
            line-height: 1.75;
        }
        .article-content .callout-card {
            background: linear-gradient(135deg, #f0fdf4 0%, #eff6ff 100%);
            border: 1px solid #bfdbfe;
            border-radius: 1rem;
            padding: 1.5rem 1.75rem;
            margin: 2.25rem 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .article-content code {
            color: #4338ca;
            background-color: #eef2ff;
            padding: 0.2rem 0.45rem;
            border-radius: 0.35rem;
            font-size: 0.9em;
        }
        .article-content table {
            margin: 1.5rem 0;
        }
    </style>

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

            <div class="d-flex flex-wrap align-items-center gap-3 small text-muted">
                <span><i class="bi bi-person me-1"></i> {{ $article->author }}</span>
                <span>&bull;</span>
                <span><i class="bi bi-calendar3 me-1"></i> {{ $article->published_at?->format('d F Y') ?? date('d F Y') }}</span>
                <span>&bull;</span>
                <span><i class="bi bi-clock me-1"></i> {{ max(3, ceil(str_word_count(strip_tags($article->content)) / 180)) }} menit baca</span>
            </div>
        </div>
    </section>

    <!-- Isi Artikel Lengkap -->
    <section class="py-5 bg-white">
        <div class="container py-2 max-w-3xl">
            @if($article->image)
                <div class="mb-4 text-center">
                    <img src="{{ asset('images/' . $article->image) }}" alt="{{ $article->title }}" class="img-fluid rounded-4 shadow-sm object-fit-cover w-100" style="max-height: 440px;">
                </div>
            @endif

            <div class="article-content fs-6 text-dark leading-relaxed mb-5">
                {!! $article->content !!}
            </div>

            <!-- Author Bio Card (Membangun Otoritas Pakar) -->
            <div class="card border rounded-4 p-4 mb-5 bg-light bg-opacity-50 shadow-xs">
                <div class="d-flex flex-column flex-sm-row align-items-sm-center gap-3">
                    <img src="{{ asset('images/gede-erik-aktama.jpg') }}" alt="{{ $article->author }}" class="rounded-circle object-fit-cover shadow-xs border" style="width: 72px; height: 72px; min-width: 72px;">
                    <div>
                        <div class="d-flex align-items-center gap-2 mb-1">
                            <h6 class="fw-bold text-dark mb-0">{{ $article->author }}</h6>
                            <span class="badge bg-success bg-opacity-10 text-success small" style="font-size: 0.7rem;">Verified Author</span>
                        </div>
                        <p class="text-muted small mb-2">
                            Founder PT Aktama Digital Antika • Dosen & Kaprodi Sistem Komputer Univ. Parna Raya • Fasilitator Nasional KKA Kemdikdasmen.
                        </p>
                        <a href="https://profil.aktama.com" target="_blank" rel="noopener noreferrer" class="small text-primary text-decoration-none fw-semibold">
                            Lihat Profil Akademik & Publikasi SINTA <i class="bi bi-arrow-up-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Share Buttons -->
            <div class="p-4 rounded-4 bg-light border d-flex flex-wrap align-items-center justify-content-between gap-3 mb-5">
                <div>
                    <h6 class="fw-bold text-dark mb-1">Bagikan Artikel Ini:</h6>
                    <small class="text-muted">Bantu rekan atau instansi Anda mendapatkan wawasan strategis ini.</small>
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
                    <h5 class="fw-bold font-display text-dark mb-4">Artikel Terkait dalam Topik Serupa</h5>
                    <div class="row g-3">
                        @foreach($relatedArticles as $rel)
                            <div class="col-md-4">
                                <div class="card h-100 p-3 rounded-4 border bg-light shadow-xs hover-lift">
                                    @if($rel->image)
                                        <img src="{{ asset('images/' . $rel->image) }}" alt="{{ $rel->title }}" class="img-fluid rounded-3 mb-2 object-fit-cover w-100" style="height: 100px;">
                                    @endif
                                    <h6 class="fw-bold text-dark fs-6 mb-2">
                                        <a href="{{ route('articles.show', $rel->slug) }}" class="text-dark text-decoration-none hover-primary">
                                            {{ $rel->title }}
                                        </a>
                                    </h6>
                                    <small class="text-muted mt-auto" style="font-size: 0.75rem;">{{ $rel->published_at?->format('d M Y') }}</small>
                                </div>
                            </div>
                        @endforeach
                    </div>
                </div>
            @endif
        </div>
    </section>

@endsection
