@extends('layouts.app')

@section('title', ($settings['coffee_brand_name'] ?? 'Aktama Coffee') . ' | Distribusi Kopi Kemasan Retail & Pasokan Grosir')
@section('meta_description', 'Lini usaha komoditas kopi pilihan PT Aktama Digital Antika. Melayani pembelian eceran retail serta suplai grosir rutin untuk kafe, warkop, dan toko kelontong.')

@section('content')

    <!-- Hero Coffee Banner -->
    <section class="py-5 bg-dark text-white border-bottom position-relative" style="background: linear-gradient(rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.95));">
        <div class="container py-4 text-center">
            <span class="badge bg-warning bg-opacity-25 text-warning fw-bold text-uppercase px-3 py-1 mb-2">
                <i class="bi bi-cup-hot-fill me-1"></i> Lini Usaha Komoditas Kopi Riil
            </span>
            <h1 class="display-5 fw-bold font-display text-white mb-2">{{ $settings['coffee_brand_name'] ?? 'Aktama Coffee' }}</h1>
            <p class="text-white-50 max-w-2xl mx-auto fs-6 mb-4">
                {{ $settings['coffee_tagline'] ?? 'Pasokan biji dan bubuk kopi berkualitas langsung dari sentra pengolahan. Menghadirkan aroma otentik untuk penikmat kopi harian dan kemitraan pasokan kafe modern.' }}
            </p>
            <div class="d-flex justify-content-center gap-3">
                <a href="#katalog-kopi" class="btn btn-warning rounded-pill px-4 py-2 fw-semibold">
                    <i class="bi bi-bag-check-fill me-1"></i> Lihat Pilihan Kopi
                </a>
                <a href="#kemitraan-grosir" class="btn btn-outline-light rounded-pill px-4 py-2">
                    <i class="bi bi-shop me-1"></i> Paket Grosir Kafe & Reseller
                </a>
            </div>
        </div>
    </section>

    <!-- Keunggulan Produk Kopi Kami -->
    <section class="py-4 bg-light border-bottom">
        <div class="container py-2">
            <div class="row g-3 text-center">
                <div class="col-md-3">
                    <div class="p-3 bg-white rounded-3 border">
                        <i class="bi bi-patch-check-fill text-warning fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Biji Kopi Petik Merah</h6>
                        <small class="text-muted">Kematangan buah optimal menghasilkan cita rasa bersih & konsisten.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-white rounded-3 border">
                        <i class="bi bi-fire text-danger fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Sangrai Terstandar</h6>
                        <small class="text-muted">Profil sangrai terukur menjaga kekayaan aroma dan keasaman seimbang.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-white rounded-3 border">
                        <i class="bi bi-box-seam text-primary fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Kemasan Segel Higienis</h6>
                        <small class="text-muted">Aluminium foil dengan valve kedap udara menjaga kesegaran lebih lama.</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="p-3 bg-white rounded-3 border">
                        <i class="bi bi-truck text-success fs-3 mb-2 d-block"></i>
                        <h6 class="fw-bold text-dark small mb-1">Suplai B2B Berkala</h6>
                        <small class="text-muted">Kemudahan pasokan mingguan dan bulanan untuk kafe dan warkop.</small>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Katalog Produk Kopi -->
    <section id="katalog-kopi" class="py-5 bg-white">
        <div class="container py-3">
            <div class="text-center max-w-xl mx-auto mb-5">
                <span class="badge bg-warning bg-opacity-25 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Katalog Resmi</span>
                <h2 class="fw-bold font-display text-dark">Pilihan Karakter Kopi Terbaik</h2>
                <p class="text-muted small">Tersedia dalam bentuk biji sangrai utuh maupun bubuk gilingan halus/medium siap seduh.</p>
            </div>

            <div class="row g-4 mb-5">
                @forelse($coffeeProducts as $coffee)
                    <div class="col-lg-6">
                        <div class="card card-feature p-4 p-md-5 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <img src="{{ asset('images/' . ($coffee->image ?? 'coffee/gayo.jpg')) }}" alt="{{ $coffee->name }}" class="rounded-3 mb-3 object-fit-cover w-100 shadow-sm" style="height: 220px;">

                                <div class="d-flex justify-content-between align-items-start mb-3">
                                    <div>
                                        <span class="badge bg-dark small mb-2">{{ $coffee->sku }}</span>
                                        <h3 class="fw-bold text-dark fs-5 mb-1">{{ $coffee->name }}</h3>
                                        <small class="text-muted d-block">
                                            <i class="bi bi-geo-alt text-danger me-1"></i>{{ $coffee->origin }} &bull; 
                                            <i class="bi bi-fire text-warning me-1"></i>{{ $coffee->roast_level }}
                                        </small>
                                    </div>
                                    <div class="rounded-circle bg-warning bg-opacity-10 text-warning p-3 fs-3">
                                        <i class="bi bi-cup-hot"></i>
                                    </div>
                                </div>

                                <p class="text-muted small leading-relaxed mb-4">{{ $coffee->description }}</p>

                                <div class="border rounded-3 p-3 bg-light mb-4">
                                    <h6 class="fw-bold text-dark small mb-2"><i class="bi bi-tag-fill text-warning me-1"></i> Rincian Varian & Struktur Harga:</h6>
                                    <div class="table-responsive">
                                        <table class="table table-sm table-borderless small mb-0">
                                            <thead class="text-muted border-bottom">
                                                <tr>
                                                    <th>Nama Varian</th>
                                                    <th>Berat</th>
                                                    <th>Harga Eceran</th>
                                                    <th>Harga Grosir Kafe</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                @foreach($coffee->variants as $variant)
                                                    <tr>
                                                        <td class="fw-bold text-dark">{{ $variant->variant_name }}</td>
                                                        <td class="text-muted">{{ $variant->weight_grams }}g</td>
                                                        <td class="text-primary fw-bold">Rp {{ number_format($variant->retail_price, 0, ',', '.') }}</td>
                                                        <td class="text-success fw-bold">
                                                            Rp {{ number_format($variant->wholesale_price, 0, ',', '.') }}
                                                            <div class="text-muted fw-normal" style="font-size: 0.7rem;">(Min. {{ $variant->min_wholesale_qty }})</div>
                                                        </td>
                                                    </tr>
                                                @endforeach
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <div class="border-top pt-3 d-flex gap-2">
                                <a href="#kemitraan-grosir" class="btn btn-warning rounded-pill btn-sm w-100 fw-semibold">
                                    Pesan Kopi / Minta Sample
                                </a>
                                <a href="{{ $settings['coffee_app_url'] ?? 'http://localhost:8080/kopi/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-dark rounded-pill btn-sm px-3" title="Buka Sistem Distribusi Kopi">
                                    <i class="bi bi-box-arrow-up-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-light border small text-muted">Katalog kopi sedang disiapkan.</div>
                    </div>
                @endforelse
            </div>

            <!-- FORMULIR KEMITRAAN KOPI -->
            <div id="kemitraan-grosir" class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-light">
                <div class="text-center max-w-xl mx-auto mb-4">
                    <span class="badge bg-warning bg-opacity-25 text-dark fw-bold text-uppercase px-3 py-1 mb-2">Formulir Pemesanan & Kemitraan</span>
                    <h3 class="fw-bold font-display text-dark">Pesan Eceran atau Jadilah Mitra Kafe Kami</h3>
                    <p class="text-muted small">
                        Dapatkan harga pasokan grosir khusus untuk kebutuhan rutin kafe, warkop, kantor, toko kelontong, atau reseller Anda.
                    </p>
                </div>

                <form action="{{ route('inquiry.store') }}" method="POST" class="max-w-2xl mx-auto">
                    @csrf
                    <input type="hidden" name="service_type" value="aktama-coffee">
                    <input type="hidden" name="source_page" value="Landing Page Kopi">

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Pemesan / Pemilik Bisnis *</label>
                            <input type="text" name="name" class="form-control rounded-3" required placeholder="Contoh: Rian Anggoro">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nomor WhatsApp Aktif *</label>
                            <input type="text" name="whatsapp" class="form-control rounded-3" required placeholder="Contoh: 081234567890">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Kafe / Warung / Usaha</label>
                            <input type="text" name="organization" class="form-control rounded-3" placeholder="Contoh: Kopi Titik Temu / Toko Sumber Jaya">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Kategori Pemesanan</label>
                            <select name="budget_range" class="form-select rounded-3">
                                <option value="< 500rb">Pembelian Eceran Pribadi (< Rp 500.000)</option>
                                <option value="1jt - 3jt">Pasokan Mingguan Kafe / Toko (Rp 1.000.000 - Rp 3.000.000)</option>
                                <option value="3jt - 10jt">Distributor / Reseller Besar (> Rp 3.000.000)</option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Varian Kopi yang Diminati & Estimasi Jumlah *</label>
                        <textarea name="message" class="form-control rounded-3" rows="3" required placeholder="Contoh: Mau pesan Robusta 1kg pasokan kafe sebanyak 10 bungkus, mohon info pengiriman..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-warning btn-lg w-100 rounded-pill shadow-sm fw-bold">
                        <i class="bi bi-send-fill me-2"></i> Hubungi untuk Pemesanan Kopi
                    </button>
                </form>
            </div>
        </div>
    </section>

@endsection
