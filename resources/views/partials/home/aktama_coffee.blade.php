<!-- SECTION: BISNIS KOPI (AKTAMA COFFEE) -->
<section id="aktama-coffee" class="py-5 bg-white border-bottom">
    <div class="container py-4">
        <div class="row align-items-end mb-4">
            <div class="col-lg-8">
                <span class="badge bg-warning bg-opacity-25 text-dark fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Lini Usaha Komoditas' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? ($settings['coffee_brand_name'] ?? 'Kopi Distro Premium') }}</h2>
                <p class="text-muted mb-0">
                    {{ $sectionConfig->subtitle ?? ($settings['coffee_tagline'] ?? 'Roastery & Distribusi Biji/Bubuk Kopi Asli Nusantara untuk Retail dan Suplai Kafe') }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <a href="#form-konsultasi" class="btn btn-warning rounded-pill btn-sm px-4 fw-semibold">
                    <i class="bi bi-shop me-1"></i> Kemitraan Grosir / Reseller
                </a>
            </div>
        </div>

        <!-- Roastery Showcase Banner -->
        <div class="row align-items-center mb-5 p-4 rounded-4 text-white shadow-sm g-4" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);">
            <div class="col-lg-7">
                <span class="badge bg-warning text-dark fw-bold mb-2"><i class="bi bi-fire me-1"></i> Standar Roastery Teruji</span>
                <h3 class="fw-bold text-white font-display mb-2">Pasokan Biji Kopi Nusantara Pilihan Petik Merah</h3>
                <p class="text-white-50 small mb-3">
                    Diolah langsung dari sentra perkebunan terpercaya Aceh Gayo, Toraja Sapan, Bajawa Flores, dan Lampung Barat. Cocok untuk kebutuhan seduh manual brew, mesin espresso, maupun basis kopi susu gula aren kafe kekinian.
                </p>
                <div class="d-flex flex-wrap gap-2">
                    <span class="badge bg-white bg-opacity-10 text-white border border-light border-opacity-25"><i class="bi bi-check2 text-warning me-1"></i> Kemasan Valve Aluminium Foil</span>
                    <span class="badge bg-white bg-opacity-10 text-white border border-light border-opacity-25"><i class="bi bi-check2 text-warning me-1"></i> Biji Utuh atau Giling Halus/Medium</span>
                    <span class="badge bg-white bg-opacity-10 text-white border border-light border-opacity-25"><i class="bi bi-check2 text-warning me-1"></i> Suplai Grosir Rutin Mingguan</span>
                </div>
            </div>
            <div class="col-lg-5 text-center">
                <img src="{{ asset('images/coffee/hero-roastery.jpg') }}" alt="Roastery Kopi Aktama" class="img-fluid rounded-3 shadow object-fit-cover w-100" style="max-height: 220px;">
            </div>
        </div>

        <div class="row g-4">
            @forelse($coffeeProducts as $coffee)
                <div class="col-md-6">
                    <div class="card card-feature p-4 h-100 d-flex flex-column justify-content-between">
                        <div>
                            <img src="{{ asset('images/' . ($coffee->image ?? 'coffee/gayo.jpg')) }}" alt="{{ $coffee->name }}" class="rounded-3 mb-3 object-fit-cover w-100 shadow-sm" style="height: 190px;">
                            
                            <div class="d-flex align-items-start justify-content-between mb-2">
                                <div>
                                    <span class="badge bg-dark small mb-1"><i class="bi bi-tag me-1"></i>{{ $coffee->sku }}</span>
                                    <h5 class="fw-bold text-dark mb-0">{{ $coffee->name }}</h5>
                                    <small class="text-muted"><i class="bi bi-geo-alt text-danger me-1"></i>{{ $coffee->origin }} &bull; <i class="bi bi-fire text-warning me-1"></i>{{ $coffee->roast_level }}</small>
                                </div>
                            </div>

                            <p class="text-muted small mb-3 leading-relaxed">{{ $coffee->description }}</p>

                            <div class="border rounded-3 p-3 bg-light mb-3">
                                <h6 class="small fw-bold text-dark mb-2"><i class="bi bi-currency-dollar text-success me-1"></i> Varian & Struktur Harga Resmi:</h6>
                                <div class="table-responsive">
                                    <table class="table table-sm table-borderless small mb-0">
                                        <thead class="text-muted border-bottom">
                                            <tr>
                                                <th>Varian Kemasan</th>
                                                <th>Harga Eceran</th>
                                                <th>Grosir Kafe</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            @foreach($coffee->variants as $variant)
                                                <tr>
                                                    <td class="fw-semibold text-dark">{{ $variant->variant_name }}</td>
                                                    <td class="text-primary fw-bold">Rp {{ number_format($variant->retail_price, 0, ',', '.') }}</td>
                                                    <td class="text-success fw-bold">
                                                        Rp {{ number_format($variant->wholesale_price, 0, ',', '.') }}
                                                        <small class="text-muted fw-normal" style="font-size: 0.7rem;">(Min. {{ $variant->min_wholesale_qty }})</small>
                                                    </td>
                                                </tr>
                                            @endforeach
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>

                        <div class="mt-auto pt-2 border-top d-flex gap-2">
                            <a href="#form-konsultasi" class="btn btn-sm btn-dark rounded-pill w-100">
                                Pesan Eceran / Cicipi Sample
                            </a>
                            <a href="{{ $settings['coffee_app_url'] ?? 'http://localhost:8080/kopi/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-warning rounded-pill px-3" title="Buka Sistem Informasi Kopi">
                                <i class="bi bi-box-arrow-up-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            @empty
                <div class="col-12">
                    <div class="alert alert-light border small text-muted">Katalog kopi sedang diperbarui.</div>
                </div>
            @endforelse
        </div>
    </div>
</section>
