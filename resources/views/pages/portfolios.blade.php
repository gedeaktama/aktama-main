@extends('layouts.app')

@section('title', ($searchQuery ? 'Pencarian: ' . $searchQuery . ' | ' : '') . 'Portofolio Proyek Terverifikasi | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Daftar rekam jejak implementasi proyek sistem informasi, website profil, dan aplikasi bisnis yang telah dibangun oleh PT Aktama Digital Antika.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Rekam Jejak Implementasi</span>
            <h1 class="display-6 fw-bold font-display text-dark">Portofolio & Studi Kasus Terverifikasi</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-4">
                Bukti nyata kapabilitas rekayasa perangkat lunak yang andal, bebas dari risiko celah malware, cepat, dan menjawab tantangan bisnis secara terukur.
            </p>

            <!-- Search Bar Portofolio -->
            <div class="row justify-content-center mb-4">
                <div class="col-md-8 col-lg-6">
                    <form action="{{ route('portfolios') }}" method="GET" class="d-flex gap-2">
                        @if($activeCategory)
                            <input type="hidden" name="kategori" value="{{ $activeCategory }}">
                        @endif
                        <div class="input-group shadow-sm rounded-pill overflow-hidden bg-white p-1 border">
                            <span class="input-group-text bg-white border-0 text-muted ps-3"><i class="bi bi-search"></i></span>
                            <input type="text" name="q" class="form-control border-0 shadow-none px-2" placeholder="Cari portofolio, teknologi (Laravel, Python), atau klien..." value="{{ $searchQuery }}">
                            @if($searchQuery)
                                <a href="{{ route('portfolios', $activeCategory ? ['kategori' => $activeCategory] : []) }}" class="btn btn-link text-muted border-0 text-decoration-none" title="Hapus pencarian">
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
                <a href="{{ route('portfolios', $searchQuery ? ['q' => $searchQuery] : []) }}" class="btn btn-sm rounded-pill px-3 {{ !$activeCategory ? 'btn-primary' : 'btn-white border text-dark' }}">
                    Semua Kategori
                </a>
                @foreach($portfolioCategories as $pCat)
                    <a href="{{ route('portfolios', array_filter(['kategori' => $pCat, 'q' => $searchQuery])) }}" class="btn btn-sm rounded-pill px-3 {{ $activeCategory === $pCat ? 'btn-primary' : 'btn-white border text-dark' }}">
                        {{ ucfirst($pCat) }}
                    </a>
                @endforeach
            </div>

            <!-- Filter Status Bar -->
            @if($searchQuery || $activeCategory)
                <div class="mt-3">
                    <span class="badge bg-light text-dark border py-2 px-3 small">
                        <i class="bi bi-funnel-fill text-primary me-1"></i>
                        Filter:
                        @if($activeCategory)
                            Kategori <strong>"{{ ucfirst($activeCategory) }}"</strong>
                        @endif
                        @if($searchQuery)
                            {{ $activeCategory ? '•' : '' }} Kata kunci: <strong>"{{ $searchQuery }}"</strong>
                        @endif
                        ({{ count($portfolios) }} proyek ditemukan)
                        <a href="{{ route('portfolios') }}" class="text-danger ms-2 text-decoration-none fw-bold">
                            <i class="bi bi-x-lg"></i> Reset
                        </a>
                    </span>
                </div>
            @endif
        </div>
    </section>

    <!-- Daftar Portofolio -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <!-- BANNER WEBSITE PORTOFOLIO FOUNDER -->
            <div class="card border-0 shadow-sm rounded-4 p-4 mb-5" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(37, 99, 235, 0.03) 100%); border-left: 5px solid #3b82f6 !important;">
                <div class="row align-items-center g-3">
                    <div class="col-lg-8">
                        <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                            <i class="bi bi-person-workspace me-1"></i> Personal Branding & Publikasi Riset
                        </span>
                        <h4 class="fw-bold font-display text-dark mb-1">Website Portofolio Profesional & Publikasi Ilmiah SINTA</h4>
                        <p class="text-secondary small mb-0 leading-relaxed">
                            Mencari publikasi jurnal ilmiah terakreditasi SINTA 4 & 5, rekam jejak riset AI / Computer Vision, dan dokumentasi Pengabdian Kepada Masyarakat (PKM) dari <strong>{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</strong>? Kunjungi portal akademik resmi beliau.
                        </p>
                    </div>
                    <div class="col-lg-4 text-lg-end">
                        <a href="{{ $settings['profile_url'] ?? 'https://profil.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="btn btn-primary rounded-pill px-4 py-2 fw-semibold shadow-sm d-inline-flex align-items-center gap-2">
                            <span>Buka profil.aktama.com</span>
                            <i class="bi bi-box-arrow-up-right small"></i>
                        </a>
                    </div>
                </div>
            </div>

            <div class="row g-4 mb-5">
                @forelse($portfolios as $port)
                    <div class="col-md-6 col-lg-4">
                        <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between border rounded-4 shadow-sm hover-lift">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small text-uppercase">
                                        {{ $port->category }}
                                    </span>
                                    <span class="text-muted small fw-bold">{{ $port->project_year }}</span>
                                </div>

                                @if($port->image)
                                    <div class="rounded-3 overflow-hidden mb-3 bg-light border shadow-xs" style="max-height: 190px;">
                                        <img src="{{ asset('images/' . $port->image) }}" alt="{{ $port->title }}" class="img-fluid w-100 object-fit-cover" style="height: 190px;">
                                    </div>
                                @endif

                                <h4 class="fw-bold text-dark fs-6 mb-2">{{ $port->title }}</h4>
                                <small class="text-muted d-block mb-3">
                                    <i class="bi bi-building me-1"></i> Kategori Klien: <strong class="text-dark">{{ $port->client_type }}</strong>
                                </small>

                                <div class="text-muted small leading-relaxed mb-4">
                                    {!! $port->description !!}
                                </div>
                            </div>

                            <div>
                                @if(!empty($port->technologies) && is_array($port->technologies))
                                    <div class="d-flex flex-wrap gap-1 mb-3">
                                        @foreach($port->technologies as $tech)
                                            <span class="badge bg-light text-secondary border font-monospace" style="font-size: 0.7rem;">{{ $tech }}</span>
                                        @endforeach
                                    </div>
                                @endif

                                <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                                    <span class="text-success small fw-semibold">
                                        <i class="bi bi-shield-check me-1"></i> Terverifikasi
                                    </span>
                                    @if($port->project_url)
                                        <a href="{{ $port->project_url }}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-primary rounded-pill px-3">
                                            Kunjungi Proyek <i class="bi bi-arrow-up-right ms-1"></i>
                                        </a>
                                    @else
                                        <a href="#form-konsultasi" class="btn btn-sm btn-light border rounded-pill px-3">
                                            Konsultasi Serupa
                                        </a>
                                    @endif
                                </div>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="card border rounded-4 p-5 text-center bg-light shadow-xs max-w-xl mx-auto">
                            <i class="bi bi-briefcase text-muted display-4 d-block mb-3 opacity-50"></i>
                            <h5 class="fw-bold text-dark mb-2">Tidak ada proyek yang sesuai filter</h5>
                            <p class="text-muted small mb-4">
                                Tidak ditemukan portofolio untuk kriteria pencarian ini.
                            </p>
                            <div>
                                <a href="{{ route('portfolios') }}" class="btn btn-outline-primary rounded-pill px-4 btn-sm">
                                    <i class="bi bi-arrow-repeat me-1"></i> Lihat Semua Portofolio
                                </a>
                            </div>
                        </div>
                    </div>
                @endforelse
            </div>
        </div>
    </section>

@endsection
