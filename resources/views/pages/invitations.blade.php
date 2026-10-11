@extends('layouts.app')

@section('title', 'Undangan Online Digital Premium | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Layanan undangan digital pernikahan dan event istimewa dengan desain elegan, personalisasi nama tamu tanpa batas, musik latar, RSVP, dan peta lokasi.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-danger bg-opacity-10 text-danger fw-bold text-uppercase px-3 py-1 mb-2">Event & Wedding Tech</span>
            <h1 class="display-6 fw-bold font-display text-dark">Undangan Online Digital Elegan</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Solusi praktis dan berkelas untuk membagikan kabar bahagia momen pernikahan dan acara keluarga ke seluruh tamu undangan melalui smartphone.
            </p>
        </div>
    </section>

    <!-- Fitur Unggulan Undangan -->
    <section class="py-4 bg-white border-bottom">
        <div class="container py-2">
            <div class="row g-3 text-center">
                <div class="col-md-3">
                    <div class="p-3 bg-light rounded-3 border">
                        <i class="bi bi-people-fill text-danger fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Nama Tamu Otomatis</h6>
                        <small class="text-muted">Setiap tautan memuat nama tamu khusus secara personal dan sopan.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-light rounded-3 border">
                        <i class="bi bi-music-note-beamed text-primary fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Musik Latar Romantis</h6>
                        <small class="text-muted">Pilihan lagu latar dengan pemutar audio otomatis yang lembut.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-light rounded-3 border">
                        <i class="bi bi-geo-alt-fill text-success fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Navigasi Google Maps</h6>
                        <small class="text-muted">Petunjuk arah langsung terhubung ke aplikasi peta di HP tamu.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-light rounded-3 border">
                        <i class="bi bi-wallet2 text-warning fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Amplop Digital & RSVP</h6>
                        <small class="text-muted">Konfirmasi kehadiran real-time dan transfer tanda kasih aman.</small>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Paket Harga Undangan -->
    <section class="py-5 bg-white">
        <div class="container py-3">

            <!-- Dedicated Gateway Callout -->
            <div class="card border-0 rounded-4 p-4 p-md-5 mb-5 shadow-sm text-center text-white" style="background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);">
                <div class="max-w-2xl mx-auto">
                    <span class="badge bg-white text-danger fw-bold text-uppercase px-3 py-1 mb-2">Dedicated Wedding SaaS Platform</span>
                    <h2 class="fw-bold font-display text-white mb-2">Platform Khusus Undangan Online Telah Aktif</h2>
                    <p class="text-white-50 small mb-4">
                        Lihat langsung keanggunan 6 tema pernikahan (Balinese Grandeur, Royal Sakinah, Ivory Garden, Covenant Grace, dan lainnya) lengkap dengan alunan musik latar, animasi pembuka amplop, dan formulir RSVP real-time.
                    </p>
                    <div class="d-flex flex-wrap justify-content-center gap-3">
                        <a href="{{ $settings['invitation_url'] ?? 'http://localhost:8080/undanganonline/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-light text-danger fw-bold rounded-pill px-4 shadow">
                            <i class="bi bi-box-arrow-up-right me-1"></i> Buka Katalog Tema & Live Demo
                        </a>
                        <a href="{{ $settings['invitation_url'] ?? 'http://localhost:8080/undanganonline/public' }}/undangan/agung-erik-kunti" target="_blank" rel="noopener noreferrer" class="btn btn-outline-light rounded-pill px-4">
                            <i class="bi bi-eye me-1"></i> Contoh Undangan Nyata (Erik & Kunti)
                        </a>
                    </div>
                </div>
            </div>

            <div class="text-center mb-4">
                <span class="badge bg-danger bg-opacity-10 text-danger fw-bold text-uppercase px-3 py-1 mb-2">Pilihan Paket</span>
                <h3 class="fw-bold font-display text-dark">Daftar Paket Undangan Digital</h3>
                <p class="text-muted small">Pilih paket yang paling sesuai dengan kebutuhan momentum bahagia Anda.</p>
            </div>

            <div class="row g-4 justify-content-center mb-5">
                @forelse($packages as $pkg)
                    <div class="col-lg-4 col-md-6">
                        <div class="card card-feature p-4 p-md-5 h-100 position-relative d-flex flex-column justify-content-between {{ $pkg->is_popular ? 'border-danger border-2' : '' }}">
                            @if($pkg->is_popular)
                                <span class="badge bg-danger position-absolute top-0 end-0 m-3 px-3 py-2 rounded-pill small">
                                    Pilihan Terfavorit
                                </span>
                            @endif

                            <div>
                                <img src="{{ asset('images/' . ($pkg->image ?? 'invitations/wedding-cover.jpg')) }}" alt="{{ $pkg->name }}" class="rounded-3 mb-3 object-fit-cover w-100 shadow-sm" style="height: 190px;">

                                <h3 class="fw-bold text-dark fs-5 mb-1">{{ $pkg->name }}</h3>
                                <div class="d-flex align-items-baseline gap-2 mb-4">
                                    <span class="display-6 fw-bold text-danger">Rp {{ number_format($pkg->discount_price ?? $pkg->price, 0, ',', '.') }}</span>
                                    @if($pkg->discount_price)
                                        <span class="text-muted text-decoration-line-through small">Rp {{ number_format($pkg->price, 0, ',', '.') }}</span>
                                    @endif
                                </div>

                                @if($pkg->features && is_array($pkg->features))
                                    <h6 class="fw-bold text-dark small mb-2"><i class="bi bi-check2-circle text-danger me-1"></i> Keunggulan Paket:</h6>
                                    <ul class="list-unstyled small text-muted border-top pt-3 mb-4 space-y-2">
                                        @foreach($pkg->features as $item)
                                            <li class="mb-2 d-flex align-items-center gap-2">
                                                <i class="bi bi-check-circle-fill text-danger small"></i>
                                                <span>{{ $item }}</span>
                                            </li>
                                        @endforeach
                                    </ul>
                                @endif
                            </div>

                            <div class="mt-auto pt-3 border-top d-flex gap-2">
                                <a href="#form-order-undangan" class="btn btn-danger rounded-pill btn-sm w-100 fw-semibold">
                                    Pesan Paket Ini
                                </a>
                                @if($pkg->demo_url)
                                    <a href="{{ $pkg->demo_url }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-secondary rounded-pill btn-sm px-3">
                                        Lihat Contoh
                                    </a>
                                @endif
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-light border small text-muted">Paket undangan sedang disiapkan.</div>
                    </div>
                @endforelse
            </div>

            <!-- FORMULIR PEMESANAN UNDANGAN -->
            <div id="form-order-undangan" class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-light">
                <div class="text-center max-w-xl mx-auto mb-4">
                    <span class="badge bg-danger bg-opacity-10 text-danger fw-bold text-uppercase px-3 py-1 mb-2">Formulir Pemesanan</span>
                    <h3 class="fw-bold font-display text-dark">Pesan Undangan Digital Acara Anda</h3>
                    <p class="text-muted small">
                        Kirim data awal acara Anda, dan tim kami akan segera menghubungi untuk proses pemilihan tema dan penulisan teks undangan.
                    </p>
                </div>

                <form action="{{ route('inquiry.store') }}" method="POST" class="max-w-2xl mx-auto">
                    @csrf
                    <input type="hidden" name="service_type" value="undangan-online">
                    <input type="hidden" name="source_page" value="Halaman Undangan Online">

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Pemesan / Mempelai *</label>
                            <input type="text" name="name" class="form-control rounded-3" required placeholder="Contoh: Rian & Sari">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nomor WhatsApp Aktif *</label>
                            <input type="text" name="whatsapp" class="form-control rounded-3" required placeholder="Contoh: 081234567890">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Jenis Acara</label>
                            <select name="organization" class="form-select rounded-3">
                                <option value="Pernikahan / Wedding">Pernikahan (Wedding)</option>
                                <option value="Ulang Tahun / Birthday">Ulang Tahun / Syukuran</option>
                                <option value="Wisuda / Graduation">Wisuda / Pelepasan</option>
                                <option value="Acara Formal / Seminar">Acara Formal / Seminar</option>
                            </select>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Pilihan Paket *</label>
                            <select name="budget_range" class="form-select rounded-3">
                                <option value="Undangan Basic (Rp 199.000)">Undangan Basic (Rp 199.000)</option>
                                <option value="Undangan Premium (Rp 349.000)" selected>Undangan Premium (Rp 349.000) - Terfavorit</option>
                                <option value="Undangan Exclusive (Rp 599.000)">Undangan Exclusive (Rp 599.000) - Flagship</option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Rencana Tanggal Acara & Catatan Khusus *</label>
                        <textarea name="message" class="form-control rounded-3" rows="3" required placeholder="Tuliskan perkiraan tanggal acara dan lokasi..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-danger btn-lg w-100 rounded-pill shadow-sm fw-bold">
                        <i class="bi bi-send-fill me-2"></i> Kirim Pemesanan Undangan
                    </button>
                </form>
            </div>
        </div>
    </section>

@endsection
