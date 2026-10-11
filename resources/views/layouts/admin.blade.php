<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>@yield('title', 'Admin Dashboard') | Aktama Digital CMS</title>

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="{{ asset('images/logo-aktama.png') }}">

    <!-- Bootstrap Icons (Lokal Vendor & CDN Fallback: Jaminan Ikon 100% Muncul) -->
    <link rel="stylesheet" href="{{ asset('vendor/bootstrap-icons/bootstrap-icons.min.css') }}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <!-- Vite Assets (Bootstrap 5.3 + Bootstrap Icons) -->
    @vite(['resources/scss/app.scss', 'resources/js/app.js'])

    <style>
        .sidebar {
            min-height: 100vh;
            background-color: #0b0f19;
            width: 260px;
        }
        .sidebar .nav-link {
            color: #94a3b8;
            font-size: 0.875rem;
            padding: 0.65rem 1rem;
            border-radius: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.25rem;
            transition: all 0.15s ease-in-out;
        }
        .sidebar .nav-link:hover, .sidebar .nav-link.active {
            color: #ffffff;
            background-color: rgba(79, 70, 229, 0.2);
        }
        .sidebar .nav-link.active {
            border-left: 3px solid #6366f1;
            font-weight: 600;
        }
        .main-content {
            background-color: #f1f5f9;
            min-height: 100vh;
        }
    </style>
</head>
<body class="bg-light">

    <div class="d-flex">
        <!-- SIDEBAR -->
        <aside class="sidebar text-white d-flex flex-column p-3 shrink-0 position-sticky top-0" style="height: 100vh; overflow-y: auto;">
            <!-- Brand -->
            <a href="{{ route('admin.dashboard') }}" class="d-flex align-items-center mb-4 text-decoration-none px-2">
                <img src="{{ asset('images/logo-aktama.png') }}" alt="Aktama CMS" class="img-fluid bg-white p-2 rounded-3 shadow-sm" style="max-height: 42px; width: auto; object-fit: contain;">
            </a>

            <!-- Menu Navigation -->
            <ul class="nav nav-pills flex-column mb-auto">
                <li class="nav-item">
                    <a href="{{ route('admin.dashboard') }}" class="nav-link {{ request()->routeIs('admin.dashboard') ? 'active' : '' }}">
                        <i class="bi bi-speedometer2"></i> Dashboard
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.leads.index') }}" class="nav-link {{ request()->routeIs('admin.leads.*') ? 'active' : '' }}">
                        <i class="bi bi-people-fill"></i> Calon Pelanggan (Leads)
                    </a>
                </li>

                <div class="text-white-50 text-uppercase small fw-bold px-3 mt-3 mb-1" style="font-size: 0.65rem;">CMS & Desain Tata Letak</div>

                <li class="nav-item">
                    <a href="{{ route('admin.sections.index') }}" class="nav-link {{ request()->routeIs('admin.sections.*') ? 'active' : '' }}">
                        <i class="bi bi-arrows-move"></i> Seksi Beranda (Drag & Drop)
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.pages.index') }}" class="nav-link {{ request()->routeIs('admin.pages.*') ? 'active' : '' }}">
                        <i class="bi bi-palette-fill"></i> Halaman & Visual Canvas
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.menus.index') }}" class="nav-link {{ request()->routeIs('admin.menus.*') ? 'active' : '' }}">
                        <i class="bi bi-menu-button-wide-fill"></i> Menu Navigasi (Drag & Drop)
                    </a>
                </li>

                <div class="text-white-50 text-uppercase small fw-bold px-3 mt-3 mb-1" style="font-size: 0.65rem;">Konten & Layanan</div>

                <li class="nav-item">
                    <a href="{{ route('admin.articles.index') }}" class="nav-link {{ request()->routeIs('admin.articles.*') ? 'active' : '' }}">
                        <i class="bi bi-journal-richtext"></i> Postingan / Berita
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.services.index') }}" class="nav-link {{ request()->routeIs('admin.services.*') ? 'active' : '' }}">
                        <i class="bi bi-globe"></i> Jasa Web & Aplikasi
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.training.index') }}" class="nav-link {{ request()->routeIs('admin.training.*') ? 'active' : '' }}">
                        <i class="bi bi-robot"></i> Pelatihan AI
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.coffee.index') }}" class="nav-link {{ request()->routeIs('admin.coffee.*') ? 'active' : '' }}">
                        <i class="bi bi-cup-hot-fill"></i> Produk Kopi & Varian
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.invitations.index') }}" class="nav-link {{ request()->routeIs('admin.invitations.*') ? 'active' : '' }}">
                        <i class="bi bi-heart-fill"></i> Paket Undangan
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{{ route('admin.portfolios.index') }}" class="nav-link {{ request()->routeIs('admin.portfolios.*') ? 'active' : '' }}">
                        <i class="bi bi-briefcase-fill"></i> Portofolio
                    </a>
                </li>

                <div class="text-white-50 text-uppercase small fw-bold px-3 mt-3 mb-1" style="font-size: 0.65rem;">Pengaturan & Branding</div>

                <li class="nav-item">
                    <a href="{{ route('admin.settings.index') }}" class="nav-link {{ request()->routeIs('admin.settings.*') ? 'active' : '' }}">
                        <i class="bi bi-gear-fill"></i> Pengaturan, Logo & Footer
                    </a>
                </li>
            </ul>

            <hr class="border-secondary border-opacity-25 my-3">

            <!-- Bottom Actions -->
            <div class="d-flex flex-column gap-2">
                <a href="{{ route('home') }}" target="_blank" class="btn btn-outline-light btn-sm rounded-pill w-100 text-start px-3">
                    <i class="bi bi-box-arrow-up-right me-2"></i> Buka Web Publik
                </a>
                <form action="{{ route('admin.logout') }}" method="POST">
                    @csrf
                    <button type="submit" class="btn btn-danger btn-sm rounded-pill w-100 text-start px-3">
                        <i class="bi bi-box-arrow-right me-2"></i> Keluar (Logout)
                    </button>
                </form>
            </div>
        </aside>

        <!-- MAIN VIEW WRAPPER -->
        <div class="flex-grow-1 main-content d-flex flex-column">
            <!-- Topbar Admin -->
            <header class="bg-white border-bottom py-3 px-4 d-flex justify-content-between align-items-center sticky-top shadow-xs">
                <div>
                    <h5 class="fw-bold mb-0 text-dark">@yield('page_title', 'Dashboard')</h5>
                </div>
                <div class="d-flex align-items-center gap-3">
                    <div class="text-end d-none d-sm-block">
                        <div class="small fw-bold text-dark">{{ auth()->user()->name }}</div>
                        <div class="text-muted" style="font-size: 0.75rem;">Administrator Aktama</div>
                    </div>
                    <div class="rounded-circle bg-primary bg-opacity-10 text-primary p-2 d-flex align-items-center justify-content-center fw-bold" style="width: 2.25rem; height: 2.25rem;">
                        {{ substr(auth()->user()->name, 0, 1) }}
                    </div>
                </div>
            </header>

            <!-- Container Content -->
            <div class="p-4 flex-grow-1">
                @if(session('success'))
                    <div class="alert alert-success alert-dismissible fade show rounded-3 shadow-xs d-flex align-items-center gap-2 mb-4" role="alert">
                        <i class="bi bi-check-circle-fill text-success fs-5"></i>
                        <div>{{ session('success') }}</div>
                        <button type="button" class="btn-close ms-auto" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                @endif

                @if(session('error'))
                    <div class="alert alert-danger alert-dismissible fade show rounded-3 shadow-xs d-flex align-items-center gap-2 mb-4" role="alert">
                        <i class="bi bi-exclamation-triangle-fill text-danger fs-5"></i>
                        <div>{{ session('error') }}</div>
                        <button type="button" class="btn-close ms-auto" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                @endif

                @yield('content')
            </div>

            <!-- Footer Admin -->
            <footer class="bg-white border-top py-3 px-4 text-muted small text-center">
                &copy; {{ date('Y') }} PT Aktama Digital Antika. Laravel 12 Admin Panel.
            </footer>
        </div>
    </div>

    @stack('scripts')
</body>
</html>
