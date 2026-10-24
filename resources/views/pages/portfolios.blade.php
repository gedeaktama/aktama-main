@extends('layouts.app')

@section('title', 'Portofolio Proyek Terverifikasi | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Daftar rekam jejak implementasi proyek sistem informasi, website profil, dan aplikasi bisnis yang telah dibangun oleh PT Aktama Digital Antika.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-secondary bg-opacity-10 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Rekam Jejak Implementasi</span>
            <h1 class="display-6 fw-bold font-display text-dark">Portofolio & Studi Kasus Terverifikasi</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Bukti nyata kapabilitas rekayasa perangkat lunak yang andal, cepat, dan menjawab tantangan bisnis secara terukur.
            </p>
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
                        <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small text-uppercase">
                                        {{ $port->category }}
                                    </span>
                                    <span class="text-muted small fw-bold">{{ $port->project_year }}</span>
                                </div>

                                <h4 class="fw-bold text-dark fs-6 mb-2">{{ $port->title }}</h4>
                                <small class="text-muted d-block mb-3">
                                    <i class="bi bi-building me-1"></i> Kategori Klien: <strong class="text-dark">{{ $port->client_type }}</strong>
                                </small>

                                <p class="text-muted small leading-relaxed mb-4">{{ $port->description }}</p>
                            </div>

                            <div class="border-top pt-3 mt-auto">
                                <small class="text-muted d-block mb-1" style="font-size: 0.75rem;">Teknologi Utama:</small>
                                <span class="badge bg-light text-dark border font-monospace small mb-3">{{ $port->technology }}</span>

                                <a href="{{ route('home') }}#form-konsultasi" class="btn btn-outline-primary btn-sm rounded-pill w-100">
                                    Buat Proyek Serupa
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-light border small text-muted">Portofolio sedang dirapikan.</div>
                    </div>
                @endforelse
            </div>

            <!-- Konsultasi CTA Box -->
            <div class="p-4 p-md-5 rounded-4 bg-light border text-center max-w-2xl mx-auto">
                <h4 class="fw-bold font-display text-dark mb-2">Ingin Membangun Solusi Khusus untuk Organisasi Anda?</h4>
                <p class="text-muted small mb-4">
                    Diskusikan ide dan alur kerja sistem Anda dengan tim teknis kami secara langsung tanpa biaya konsultasi awal.
                </p>
                <a href="{{ route('home') }}#form-konsultasi" class="btn btn-brand btn-lg rounded-pill px-4 shadow-sm">
                    <i class="bi bi-chat-dots-fill me-2"></i> Mulai Konsultasi Proyek
                </a>
            </div>
        </div>
    </section>

@endsection
