@extends('layouts.app')

@section('title', 'Jasa Pembuatan Website & Aplikasi | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Layanan pembuatan website profesional, company profile, portal sekolah, sistem POS kasir, dan aplikasi web custom dengan arsitektur Laravel aman dari malware.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Software House & Digital Solusi</span>
            <h1 class="display-6 fw-bold font-display text-dark">Jasa Pembuatan Website & Aplikasi Bisnis</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Solusi perangkat lunak berkinerja tinggi, bergaransi keamanan modern, dan bebas dari celah peretasan script judi online.
            </p>
        </div>
    </section>

    <!-- Mengapa Memilih Arsitektur Laravel Kami -->
    <section class="py-4 bg-white border-bottom">
        <div class="container py-2">
            <div class="row g-3 text-center">
                <div class="col-md-3">
                    <div class="p-3 rounded-3 bg-light border">
                        <i class="bi bi-shield-lock-fill text-success fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">100% Bebas Celah Judol</h6>
                        <small class="text-muted">Direktori inti terkunci di luar webroot, kebal dari injeksi spam casino.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 rounded-3 bg-light border">
                        <i class="bi bi-speedometer2 text-primary fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Kecepatan Muat Instan</h6>
                        <small class="text-muted">Desain tanpa plugin berlebih, teroptimasi untuk performa PageSpeed tinggi.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 rounded-3 bg-light border">
                        <i class="bi bi-phone text-info fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Responsif Mobile-First</h6>
                        <small class="text-muted">Tampilan otomatis presisi di smartphone, tablet, maupun laptop.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 rounded-3 bg-light border">
                        <i class="bi bi-sliders text-warning fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">CMS Admin Mandiri</h6>
                        <small class="text-muted">Kelola teks, foto produk, harga, dan artikel dengan mudah tanpa koding.</small>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Katalog Layanan -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <div class="row g-4 mb-5">
                @forelse($services as $srv)
                    <div class="col-lg-6">
                        <div class="card card-feature p-4 p-md-5 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small text-uppercase">
                                        {{ $srv->category }}
                                    </span>
                                    <div class="rounded-3 bg-light p-2 text-primary fs-5">
                                        <i class="bi {{ $srv->icon }}"></i>
                                    </div>
                                </div>

                                @if($srv->image)
                                    <img src="{{ asset('images/' . $srv->image) }}" alt="{{ $srv->title }}" class="img-fluid rounded-3 mb-3 w-100 object-fit-cover shadow-xs" style="max-height: 200px;">
                                @endif
                                <h3 class="fw-bold text-dark fs-5 mb-2">{{ $srv->title }}</h3>
                                <div class="text-muted small leading-relaxed mb-4">{!! $srv->description !!}</div>

                                @if($srv->features && is_array($srv->features))
                                    <div class="p-3 rounded-3 bg-light border mb-4">
                                        <strong class="text-dark d-block small mb-2"><i class="bi bi-check2-all text-success me-1"></i> Ruang Lingkup & Fitur Utama:</strong>
                                        <ul class="list-unstyled small text-muted mb-0 space-y-1">
                                            @foreach($srv->features as $item)
                                                <li class="mb-1 d-flex align-items-center gap-2">
                                                    <i class="bi bi-check-circle-fill text-primary small"></i>
                                                    <span>{{ $item }}</span>
                                                </li>
                                            @endforeach
                                        </ul>
                                    </div>
                                @endif
                            </div>

                            <div class="border-top pt-3 d-flex justify-content-between align-items-center">
                                <div>
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Estimasi Investasi:</small>
                                    <strong class="text-dark">{{ $srv->price_starting }}</strong>
                                </div>
                                <a href="#form-order" class="btn btn-brand rounded-pill btn-sm px-4">
                                    Pesan Layanan Ini
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-info">Layanan sedang dimuat.</div>
                    </div>
                @endforelse
            </div>

            <!-- FORMULIR KONSULTASI WEB -->
            <div id="form-order" class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-light">
                <div class="text-center max-w-xl mx-auto mb-4">
                    <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Konsultasi Kebutuhan</span>
                    <h3 class="fw-bold font-display text-dark">Konsultasikan Website / Aplikasi Impian Anda</h3>
                    <p class="text-muted small">
                        Ceritakan kebutuhan sistem Anda. Kami akan menganalisis alur bisnis dan memberikan rekomendasi solusi paling efisien dan terjangkau.
                    </p>
                </div>

                <form action="{{ route('inquiry.store') }}" method="POST" class="max-w-2xl mx-auto">
                    @csrf
                    <input type="hidden" name="service_type" value="jasa-website">
                    <input type="hidden" name="source_page" value="Halaman Jasa Website">

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Lengkap *</label>
                            <input type="text" name="name" class="form-control rounded-3" required placeholder="Contoh: Rendra Wijaya">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nomor WhatsApp *</label>
                            <input type="text" name="whatsapp" class="form-control rounded-3" required placeholder="Contoh: 081234567890">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Bisnis / Instansi</label>
                            <input type="text" name="organization" class="form-control rounded-3" placeholder="Contoh: CV Maju Bersama / Toko Sembako">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Estimasi Anggaran</label>
                            <select name="budget_range" class="form-select rounded-3">
                                <option value="1jt - 3jt">Rp 1.000.000 - Rp 3.000.000 (Website Profil Standar)</option>
                                <option value="3jt - 10jt">Rp 3.000.000 - Rp 10.000.000 (Sistem Kasir / Sekolah / Bisnis)</option>
                                <option value="> 10jt">Di atas Rp 10.000.000 (Sistem Informasi Enterprise Custom)</option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Fitur dan Kebutuhan yang Diinginkan *</label>
                        <textarea name="message" class="form-control rounded-3" rows="3" required placeholder="Jelaskan kebutuhan website Anda, contoh: butuh web toko dengan nota cetak, web company profile kantor, atau sistem pendaftaran online..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-brand btn-lg w-100 rounded-pill shadow-sm">
                        <i class="bi bi-send-fill me-2"></i> Minta Rencana Biaya & Konsultasi
                    </button>
                </form>
            </div>
        </div>
    </section>

@endsection
