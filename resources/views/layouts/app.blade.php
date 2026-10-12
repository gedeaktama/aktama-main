<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>@yield('title', 'Aktama Digital | Pelatihan AI, Jasa Website, dan Solusi Digital Terpadu')</title>
    <meta name="description" content="@yield('meta_description', 'PT Aktama Digital Antika — Solusi digital terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website, Aktama Academy, Undangan Online, dan Distribusi Kopi.')">
    <meta name="keywords" content="@yield('meta_keywords', 'pelatihan AI, kursus kecerdasan buatan, jasa website, software house, aktama academy, undangan online, aktama coffee, gede erik aktama')">
    <meta name="author" content="PT Aktama Digital Antika">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{{ url()->current() }}">
    <meta property="og:title" content="@yield('title', 'Aktama Digital | Pelatihan AI & Solusi Teknologi')">
    <meta property="og:description" content="@yield('meta_description', 'Solusi digital terpadu untuk instansi, kampus, bisnis, dan masyarakat.')">
    <meta property="og:image" content="{{ asset($settings['logo_path'] ?? 'images/logo-aktama.png') }}">
    <meta property="og:image:alt" content="{{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="@yield('title', 'Aktama Digital | Pelatihan AI & Solusi Teknologi')">
    <meta name="twitter:description" content="@yield('meta_description', 'Solusi digital terpadu untuk instansi, kampus, bisnis, dan masyarakat.')">
    <meta name="twitter:image" content="{{ asset($settings['logo_path'] ?? 'images/logo-aktama.png') }}">

    <!-- Structured Data (Schema.org JSON-LD) -->
    <script type="application/ld+json">
    {!! json_encode([
      '@context' => 'https://schema.org',
      '@type' => 'Organization',
      'name' => $settings['company_name'] ?? 'PT Aktama Digital Antika',
      'alternateName' => $settings['brand_name'] ?? 'Aktama Digital',
      'url' => url('/'),
      'logo' => asset($settings['logo_path'] ?? 'images/logo-aktama.png'),
      'description' => $settings['footer_description'] ?? 'Solusi teknologi terpadu dan pelatihan AI.',
      'contactPoint' => [
        '@type' => 'ContactPoint',
        'telephone' => '+' . ($settings['whatsapp_number'] ?? '6285341026331'),
        'contactType' => 'customer service',
        'email' => $settings['email'] ?? 'gedeerikaktama@gmail.com',
        'areaServed' => 'ID',
        'availableLanguage' => ['Indonesian'],
      ],
      'founder' => [
        '@type' => 'Person',
        'name' => $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.',
      ],
    ], JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) !!}
    </script>

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="{{ asset($settings['favicon_path'] ?? 'images/logo-aktama.png') }}">

    <!-- Bootstrap Icons (Lokal Vendor & CDN Fallback: Jaminan Ikon 100% Muncul) -->
    <link rel="stylesheet" href="{{ asset('vendor/bootstrap-icons/bootstrap-icons.min.css') }}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <!-- Vite Assets (Bootstrap 5.3 & App SCSS/JS) -->
    @vite(['resources/scss/app.scss', 'resources/js/app.js'])

    @stack('styles')
</head>
<body class="d-flex flex-column min-vh-100">

    <!-- TOPBAR KONTAK & INFO -->
    <div class="bg-dark text-white-50 py-1 border-bottom border-secondary border-opacity-25 small">
        <div class="container d-flex flex-wrap justify-content-between align-items-center">
            <div class="d-flex align-items-center gap-3">
                <span><i class="bi bi-building text-info me-1"></i> {{ $settings['topbar_text'] ?? 'PT Aktama Digital Antika' }}</span>
                <span class="d-none d-md-inline text-secondary">|</span>
                <span class="d-none d-md-inline"><i class="bi bi-patch-check-fill text-success me-1"></i> NIB: {{ $settings['nib_number'] ?? '1703250057018' }}</span>
                <span class="d-none d-lg-inline text-secondary">|</span>
                <span class="d-none d-lg-inline"><i class="bi bi-award-fill text-warning me-1"></i> {{ $settings['lpk_status'] ?? 'LPK Resmi Terdaftar' }}</span>
                @if(!empty($settings['topbar_highlight']))
                    <span class="d-none d-xl-inline text-secondary">|</span>
                    <span class="d-none d-xl-inline badge bg-primary bg-opacity-25 text-info">{{ $settings['topbar_highlight'] }}</span>
                @endif
            </div>
            <div class="d-flex align-items-center gap-3">
                <a href="mailto:{{ $settings['email'] ?? 'kontak@aktama.com' }}" class="text-white-50 text-decoration-none hover-white">
                    <i class="bi bi-envelope text-info me-1"></i> {{ $settings['email'] ?? 'kontak@aktama.com' }}
                </a>
                <span class="text-secondary">|</span>
                <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6281234567890' }}" target="_blank" rel="noopener noreferrer" class="text-white-50 text-decoration-none hover-white">
                    <i class="bi bi-whatsapp text-success me-1"></i> WhatsApp Resmi
                </a>
            </div>
        </div>
    </div>

    <!-- MAIN NAVBAR -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white sticky-top shadow-sm py-2">
        <div class="container">
            <!-- Brand Logo Resmi -->
            <a class="navbar-brand d-flex align-items-center py-1" href="{{ route('home') }}">
                <img src="{{ asset($settings['logo_path'] ?? 'images/logo-aktama.png') }}" alt="{{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}" style="height: 42px; width: auto; object-fit: contain;" class="d-inline-block">
            </a>

            <!-- Mobile Hamburger Toggle -->
            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavbar" aria-controls="mainNavbar" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- Navbar Links Dinamis (Drag & Drop) -->
            <div class="collapse navbar-collapse" id="mainNavbar">
                @php
                    $navItems = !empty($settings['header_navigation_menu']) ? (is_array($settings['header_navigation_menu']) ? $settings['header_navigation_menu'] : json_decode($settings['header_navigation_menu'], true)) : null;
                @endphp

                <ul class="navbar-nav mx-auto mb-2 mb-lg-0 fw-medium">
                    @if(!empty($navItems) && is_array($navItems))
                        @foreach($navItems as $nav)
                            @php
                                $rawUrl = $nav['url'] ?? '/';
                                $targetUrl = str_starts_with($rawUrl, 'http') || str_starts_with($rawUrl, '#') ? $rawUrl : url($rawUrl);
                                $isActive = request()->is(ltrim($rawUrl, '/')) || (request()->path() === '/' && $rawUrl === '/');
                            @endphp
                            <li class="nav-item">
                                <a class="nav-link px-2 {{ $isActive ? 'active text-primary fw-bold' : '' }}" href="{{ $targetUrl }}" target="{{ $nav['target'] ?? '_self' }}">
                                    {{ $nav['label'] }}
                                </a>
                            </li>
                        @endforeach
                    @else
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('home') ? 'active text-primary fw-bold' : '' }}" href="{{ route('home') }}">Beranda</a></li>
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('about') ? 'active text-primary fw-bold' : '' }}" href="{{ route('about') }}">Tentang Kami</a></li>
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('services') ? 'active text-primary fw-bold' : '' }}" href="{{ route('services') }}">Jasa Website</a></li>
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('training') ? 'active text-primary fw-bold' : '' }}" href="{{ route('training') }}">Pelatihan AI</a></li>
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('portfolios') ? 'active text-primary fw-bold' : '' }}" href="{{ route('portfolios') }}">Portofolio</a></li>
                        <li class="nav-item"><a class="nav-link px-2" href="{{ $settings['invitation_url'] ?? 'https://undanganonline.aktama.com' }}" target="_blank" rel="noopener">Undangan Online</a></li>
                        <li class="nav-item"><a class="nav-link px-2" href="{{ $settings['coffee_app_url'] ?? 'https://coffee.aktama.com' }}" target="_blank" rel="noopener">Aktama Coffee</a></li>
                        <li class="nav-item"><a class="nav-link px-2" href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener">Academy</a></li>
                        <li class="nav-item"><a class="nav-link px-2 {{ request()->routeIs('articles.*') ? 'active text-primary fw-bold' : '' }}" href="{{ route('articles.index') }}">Artikel</a></li>
                    @endif
                </ul>

                <!-- Right Action CTA -->
                <div class="d-flex align-items-center gap-2">
                    <a href="#form-konsultasi" class="btn btn-brand btn-sm px-3 py-2 rounded-pill shadow-sm">
                        <i class="bi bi-chat-dots-fill me-1"></i> Minta Penawaran
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- FLASH MESSAGES NOTIFICATION -->
    <div class="container mt-3">
        @if(session('success'))
            <div class="alert alert-success alert-dismissible fade show d-flex align-items-center justify-content-between shadow-sm rounded-3" role="alert">
                <div class="d-flex align-items-center gap-2">
                    <i class="bi bi-check-circle-fill fs-5 text-success"></i>
                    <div>
                        <strong>Berhasil!</strong> {{ session('success') }}
                    </div>
                </div>
                <div class="d-flex align-items-center gap-2">
                    @if(session('wa_direct_url'))
                        <a href="{{ session('wa_direct_url') }}" target="_blank" rel="noopener noreferrer" class="btn btn-success btn-sm rounded-pill px-3">
                            <i class="bi bi-whatsapp me-1"></i> Buka Chat WhatsApp
                        </a>
                    @endif
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            </div>
        @endif

        @if(session('error'))
            <div class="alert alert-danger alert-dismissible fade show d-flex align-items-center gap-2 shadow-sm rounded-3" role="alert">
                <i class="bi bi-exclamation-triangle-fill fs-5 text-danger"></i>
                <div>
                    <strong>Peringatan!</strong> {{ session('error') }}
                </div>
                <button type="button" class="btn-close ms-auto" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif
    </div>

    <!-- MAIN CONTENT INJECTION -->
    <main class="flex-grow-1">
        @yield('content')
    </main>

    <!-- FOOTER -->
    <footer class="bg-brand-dark text-white pt-5 pb-3 mt-5 border-top border-secondary border-opacity-25">
        <div class="container">
            <div class="row g-4 mb-4">
                <!-- Kolom 1: Profil Perusahaan -->
                <div class="col-lg-4 col-md-6">
                    <div class="mb-3">
                        <div class="bg-white px-3 py-2 rounded-3 d-inline-block mb-3 shadow-sm">
                            <img src="{{ asset($settings['logo_path'] ?? 'images/logo-aktama.png') }}" alt="{{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}" style="height: 36px; width: auto; object-fit: contain;">
                        </div>
                        <div class="d-flex align-items-center gap-3">
                            <img src="{{ asset($settings['seal_path'] ?? 'images/logo-seal-aktama.png') }}" alt="Cap Resmi {{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}" style="height: 48px;">
                            <div>
                                <span class="fs-6 fw-bold font-display text-white d-block">{{ $settings['company_name'] ?? 'PT Aktama Digital Antika' }}</span>
                                <small class="text-info fw-semibold" style="font-size: 0.75rem;"><i class="bi bi-patch-check-fill text-success me-1"></i>NIB: {{ $settings['nib_number'] ?? '1703250057018' }} &bull; LPK Resmi</small>
                            </div>
                        </div>
                    </div>
                    <p class="text-white-50 small mb-3 leading-relaxed">
                        {{ $settings['footer_description'] ?? 'Perusahaan penyedia solusi teknologi terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website & Aplikasi Bisnis, Ekosistem Edukasi Digital, Undangan Online, serta Distribusi Komoditas Kopi Riil.' }}
                    </p>
                    <div class="p-3 rounded-3 bg-dark border border-secondary border-opacity-25 small mb-3">
                        <div class="text-info fw-semibold mb-1"><i class="bi bi-person-badge me-1"></i> Kepemimpinan Teknis:</div>
                        <div class="text-white fw-bold">{{ $settings['owner_name'] ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}</div>
                        <div class="text-white-50" style="font-size: 0.8rem;">{{ $settings['owner_title'] ?? 'Dosen Sistem Komputer & Fasilitator Nasional KKA Kemdikdasmen' }}</div>
                    </div>
                </div>

                <!-- Kolom 2: Layanan & Menu Dinamis Footer -->
                @php
                    $footerItems = !empty($settings['footer_navigation_menu']) ? (is_array($settings['footer_navigation_menu']) ? $settings['footer_navigation_menu'] : json_decode($settings['footer_navigation_menu'], true)) : null;
                @endphp
                <div class="col-lg-2 col-md-6">
                    <h6 class="text-uppercase text-info fw-bold small mb-3">Layanan Teknologi</h6>
                    <ul class="list-unstyled small space-y-2">
                        @if(!empty($footerItems) && is_array($footerItems))
                            @foreach($footerItems as $fItem)
                                @php
                                    $rawFUrl = $fItem['url'] ?? '/';
                                    $targetFUrl = str_starts_with($rawFUrl, 'http') || str_starts_with($rawFUrl, '#') ? $rawFUrl : url($rawFUrl);
                                @endphp
                                <li class="mb-2">
                                    <a href="{{ $targetFUrl }}" target="{{ $fItem['target'] ?? '_self' }}" class="text-white-50 text-decoration-none hover-white">
                                        {{ $fItem['label'] }}
                                    </a>
                                </li>
                            @endforeach
                        @else
                            <li class="mb-2"><a href="{{ route('training') }}" class="text-white-50 text-decoration-none hover-white">Pelatihan Kecerdasan AI</a></li>
                            <li class="mb-2"><a href="{{ route('services') }}" class="text-white-50 text-decoration-none hover-white">Website Perusahaan & Sekolah</a></li>
                            <li class="mb-2"><a href="{{ route('services') }}" class="text-white-50 text-decoration-none hover-white">Pengembangan Aplikasi Web</a></li>
                            <li class="mb-2"><a href="{{ route('services') }}" class="text-white-50 text-decoration-none hover-white">Sistem Kasir & POS Bisnis</a></li>
                            <li class="mb-2"><a href="{{ route('portfolios') }}" class="text-white-50 text-decoration-none hover-white">Portofolio Proyek</a></li>
                        @endif
                    </ul>
                </div>

                <!-- Kolom 3: Unit Bisnis & Produk -->
                <div class="col-lg-3 col-md-6">
                    <h6 class="text-uppercase text-info fw-bold small mb-3">Ekosistem Bisnis</h6>
                    <ul class="list-unstyled small space-y-2">
                        <li class="mb-2">
                            <a href="{{ $settings['invitation_url'] ?? 'https://undanganonline.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="text-white-50 text-decoration-none hover-white">
                                <i class="bi bi-heart me-1 text-danger"></i> Undangan Online <i class="bi bi-box-arrow-up-right ms-1 small" style="font-size: 0.7rem;"></i>
                            </a>
                        </li>
                        <li class="mb-2">
                            <a href="{{ $settings['coffee_app_url'] ?? 'https://coffee.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="text-white-50 text-decoration-none hover-white">
                                <i class="bi bi-cup-hot me-1 text-warning"></i> {{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }} <i class="bi bi-box-arrow-up-right ms-1 small" style="font-size: 0.7rem;"></i>
                            </a>
                        </li>
                        <li class="mb-2">
                            <a href="{{ $settings['academy_url'] ?? 'https://academy.aktama.com' }}" target="_blank" rel="noopener noreferrer" class="text-white-50 text-decoration-none hover-white">
                                <i class="bi bi-mortarboard me-1 text-success"></i> Aktama Academy <i class="bi bi-box-arrow-up-right ms-1 small" style="font-size: 0.7rem;"></i>
                            </a>
                        </li>
                    </ul>
                </div>

                <!-- Kolom 4: Kontak & Konsultasi -->
                <div class="col-lg-3 col-md-6">
                    <h6 class="text-uppercase text-info fw-bold small mb-3">Kontak Resmi</h6>
                    <p class="text-white-50 small mb-2">
                        <i class="bi bi-whatsapp text-success me-2"></i> +{{ $settings['whatsapp_number'] ?? '6285341026331' }}
                    </p>
                    <p class="text-white-50 small mb-2">
                        <i class="bi bi-envelope text-info me-2"></i> {{ $settings['email'] ?? 'gedeerikaktama@gmail.com' }}
                    </p>
                    <p class="text-white-50 small mb-3">
                        <i class="bi bi-globe me-2"></i> https://aktama.com
                    </p>
                    <div class="d-flex align-items-center gap-2 mb-3">
                        @if(!empty($settings['instagram_url']))
                            <a href="{{ $settings['instagram_url'] }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary btn-sm rounded-circle p-2 text-white border-secondary border-opacity-50 hover-white" title="Instagram Resmi" style="width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;">
                                <i class="bi bi-instagram text-danger"></i>
                            </a>
                        @endif
                        @if(!empty($settings['linkedin_url']))
                            <a href="{{ $settings['linkedin_url'] }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary btn-sm rounded-circle p-2 text-white border-secondary border-opacity-50 hover-white" title="LinkedIn Resmi" style="width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;">
                                <i class="bi bi-linkedin text-info"></i>
                            </a>
                        @endif
                        @if(!empty($settings['youtube_url']))
                            <a href="{{ $settings['youtube_url'] }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary btn-sm rounded-circle p-2 text-white border-secondary border-opacity-50 hover-white" title="YouTube Channel" style="width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;">
                                <i class="bi bi-youtube text-danger"></i>
                            </a>
                        @endif
                        @if(!empty($settings['facebook_url']))
                            <a href="{{ $settings['facebook_url'] }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary btn-sm rounded-circle p-2 text-white border-secondary border-opacity-50 hover-white" title="Facebook" style="width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;">
                                <i class="bi bi-facebook text-primary"></i>
                            </a>
                        @endif
                    </div>
                    <a href="#form-konsultasi" class="btn btn-outline-info btn-sm rounded-pill w-100">
                        <i class="bi bi-send me-1"></i> Kirim Permintaan Penawaran
                    </a>
                </div>
            </div>

            <!-- Copyright & Subline -->
            <div class="border-top border-secondary border-opacity-25 pt-3 d-flex flex-wrap justify-content-between align-items-center small text-white-50">
                <div>
                    {{ $settings['footer_copyright'] ?? ('© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.') }}
                </div>
                <div class="d-flex align-items-center gap-3">
                    <span class="text-white-50 small"><i class="bi bi-patch-check-fill text-success me-1"></i>NIB: {{ $settings['nib_number'] ?? '1703250057018' }}</span>
                    <a href="{{ route('admin.login') }}" class="text-white-50 text-decoration-none hover-white small py-1 px-2 rounded bg-dark border border-secondary border-opacity-25" title="Login Panel Admin CMS">
                        <i class="bi bi-shield-lock-fill text-info me-1"></i> Login Admin
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <!-- FLOATING WHATSAPP BUTTON (FAB) -->
    <div class="position-fixed bottom-0 end-0 p-3 p-md-4" style="z-index: 1080;">
        <a href="https://wa.me/{{ $settings['whatsapp_number'] ?? '6285341026331' }}?text={{ urlencode('Halo PT Aktama Digital Antika, saya ingin berkonsultasi mengenai solusi teknologi dan pelatihan.') }}" 
           target="_blank" 
           rel="noopener noreferrer" 
           class="btn btn-success d-flex align-items-center gap-2 rounded-pill shadow-lg px-3 py-2 text-white fw-bold text-decoration-none floating-wa-btn" 
           style="background-color: #25D366; border-color: #25D366; transition: transform 0.2s ease, box-shadow 0.2s ease;"
           title="Konsultasi Cepat via WhatsApp">
            <i class="bi bi-whatsapp fs-4"></i>
            <span class="d-none d-sm-inline fw-semibold" style="font-size: 0.9rem;">Chat WhatsApp</span>
        </a>
    </div>

    @stack('scripts')
</body>
</html>
