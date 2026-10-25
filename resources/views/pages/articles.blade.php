@extends('layouts.app')

@section('title', ($searchQuery ? 'Pencarian: ' . $searchQuery . ' | ' : '') . 'Artikel & Wawasan Teknologi | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Kumpulan artikel edukatif, panduan kecerdasan artifisial (AI), tips keamanan website bisnis, dan literasi koding komputasi.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Pusat Literasi & Wawasan</span>
            <h1 class="display-6 fw-bold font-display text-dark">Artikel & Wawasan Teknologi Terkini</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-4">
                Wawasan praktis seputar Kecerdasan Artifisial, keamanan website bisnis bebas malware, transformasi komputasi, dan kiat otomasi industri digital.
            </p>

            <!-- Search Bar & Filter Form -->
            <div class="row justify-content-center mb-4">
                <div class="col-md-8 col-lg-6">
                    <form action="{{ route('articles.index') }}" method="GET" class="d-flex gap-2">
                        @if($activeCategory)
                            <input type="hidden" name="kategori" value="{{ $activeCategory }}">
                        @endif
                        <div class="input-group shadow-sm rounded-pill overflow-hidden bg-white p-1 border">
                            <span class="input-group-text bg-white border-0 text-muted ps-3"><i class="bi bi-search"></i></span>
                            <input type="text" name="q" class="form-control border-0 shadow-none px-2" placeholder="Cari topik (contoh: AI, Guru, KKA, Website, Keamanan)..." value="{{ $searchQuery }}">
                            @if($searchQuery)
                                <a href="{{ route('articles.index', $activeCategory ? ['kategori' => $activeCategory] : []) }}" class="btn btn-link text-muted border-0 text-decoration-none" title="Hapus pencarian">
                                    <i class="bi bi-x-circle-fill"></i>
                                </a>
                            @endif
                            <button type="submit" class="btn btn-primary rounded-pill px-4 fw-semibold">
                                Cari
                            </button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Kategori Filter Pills -->
            <div class="d-flex flex-wrap justify-content-center gap-2">
                <a href="{{ route('articles.index', $searchQuery ? ['q' => $searchQuery] : []) }}" class="btn btn-sm rounded-pill px-3 {{ !$activeCategory ? 'btn-primary' : 'btn-white border text-dark' }}">
                    Semua Kategori
                </a>
                @foreach($categories as $category)
                    <a href="{{ route('articles.index', array_filter(['kategori' => $category->slug, 'q' => $searchQuery])) }}" class="btn btn-sm rounded-pill px-3 {{ $activeCategory === $category->slug ? 'btn-primary' : 'btn-white border text-dark' }}">
                        {{ $category->name }} ({{ $category->articles_count }})
                    </a>
                @endforeach
            </div>

            <!-- Filter Status Bar -->
            @if($searchQuery || $activeCategory)
                <div class="mt-3">
                    <span class="badge bg-light text-dark border py-2 px-3 small">
                        <i class="bi bi-funnel-fill text-primary me-1"></i>
                        Filter Aktif:
                        @if($activeCategory)
                            Kategori <strong>"{{ $categories->firstWhere('slug', $activeCategory)?->name ?? $activeCategory }}"</strong>
                        @endif
                        @if($searchQuery)
                            {{ $activeCategory ? '•' : '' }} Kata kunci: <strong>"{{ $searchQuery }}"</strong>
                        @endif
                        ({{ $articles->total() }} artikel ditemukan)
                        <a href="{{ route('articles.index') }}" class="text-danger ms-2 text-decoration-none fw-bold" title="Reset semua filter">
                            <i class="bi bi-x-lg"></i> Reset
                        </a>
                    </span>
                </div>
            @endif
        </div>
    </section>

    <!-- Daftar Artikel -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <div class="row g-4 mb-5">
                @forelse($articles as $art)
                    <div class="col-md-6 col-lg-4">
                        <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between border rounded-4 shadow-sm hover-lift">
                            <div>
                                @if($art->image)
                                    <a href="{{ route('articles.show', $art->slug) }}" class="d-block mb-3 overflow-hidden rounded-3">
                                        <img src="{{ asset('images/' . $art->image) }}" alt="{{ $art->title }}" class="img-fluid w-100 object-fit-cover shadow-xs" style="height: 190px;">
                                    </a>
                                @endif

                                <div class="d-flex justify-content-between align-items-center mb-2">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small">
                                        {{ $art->category?->name ?? 'Wawasan' }}
                                    </span>
                                    <small class="text-muted"><i class="bi bi-clock me-1"></i>{{ max(3, ceil(str_word_count(strip_tags($art->content)) / 180)) }} mnt baca</small>
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
                        <div class="card border rounded-4 p-5 text-center bg-light shadow-xs max-w-xl mx-auto">
                            <i class="bi bi-search text-muted display-4 d-block mb-3 opacity-50"></i>
                            <h5 class="fw-bold text-dark mb-2">Tidak ada artikel yang cocok</h5>
                            <p class="text-muted small mb-4">
                                Kami tidak menemukan artikel dengan kata kunci <strong>"{{ $searchQuery }}"</strong>. Coba periksa ejaan atau telusuri topik lainnya.
                            </p>
                            <div>
                                <a href="{{ route('articles.index') }}" class="btn btn-outline-primary rounded-pill px-4 btn-sm">
                                    <i class="bi bi-arrow-repeat me-1"></i> Tampilkan Seluruh Artikel
                                </a>
                            </div>
                        </div>
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
