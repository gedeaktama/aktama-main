<!-- SECTION: UNDANGAN DIGITAL ONLINE -->
<section id="undangan-online" class="py-5 bg-light border-bottom">
    <div class="container py-4">
        <div class="row align-items-end mb-4">
            <div class="col-lg-8">
                <span class="badge bg-danger bg-opacity-10 text-danger fw-bold text-uppercase px-3 py-1 mb-2">{{ $sectionConfig->badge ?? 'Event & Pernikahan' }}</span>
                <h2 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Undangan Online Digital' }}</h2>
                <p class="text-muted mb-0">
                    {{ $sectionConfig->subtitle ?? 'Bagikan kabar bahagia pernikahan dan acara keluarga secara praktis, hemat, dan elegan melalui website undangan mobile-first yang dapat disebar langsung via WhatsApp.' }}
                </p>
            </div>
            <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                <a href="{{ $settings['invitation_url'] ?? 'http://localhost:8080/undanganonline/public' }}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-danger rounded-pill btn-sm px-3">
                    <i class="bi bi-box-arrow-up-right me-1"></i> Buka Katalog Tema & Live Demo
                </a>
            </div>
        </div>

        <div class="row g-4">
            @forelse($invitationPackages as $pkg)
                <div class="col-lg-4 col-md-6">
                    <div class="card card-feature p-4 h-100 position-relative d-flex flex-column justify-content-between {{ $pkg->is_popular ? 'border-danger border-2' : '' }}">
                        @if($pkg->is_popular)
                            <span class="badge bg-danger position-absolute top-0 end-0 m-3 px-3 py-2 rounded-pill small">
                                Paling Diminati
                            </span>
                        @endif

                        <div>
                            <img src="{{ asset('images/' . ($pkg->image ?? 'invitations/wedding-cover.jpg')) }}" alt="{{ $pkg->name }}" class="rounded-3 mb-3 object-fit-cover w-100 shadow-sm" style="height: 180px;">

                            <h5 class="fw-bold text-dark mb-1">{{ $pkg->name }}</h5>
                            <div class="d-flex align-items-baseline gap-2 mb-3">
                                <span class="fs-4 fw-bold text-danger">Rp {{ number_format($pkg->discount_price ?? $pkg->price, 0, ',', '.') }}</span>
                                @if($pkg->discount_price)
                                    <span class="text-muted text-decoration-line-through small">Rp {{ number_format($pkg->price, 0, ',', '.') }}</span>
                                @endif
                            </div>

                            @if($pkg->features && is_array($pkg->features))
                                <ul class="list-unstyled small text-muted border-top pt-3 mb-4 space-y-2">
                                    @foreach($pkg->features as $item)
                                        <li class="mb-2 d-flex align-items-center gap-2">
                                            <i class="bi bi-check2-circle text-danger"></i>
                                            <span>{{ $item }}</span>
                                        </li>
                                    @endforeach
                                </ul>
                            @endif
                        </div>

                        <div class="mt-auto d-flex gap-2">
                            <a href="#form-konsultasi" class="btn btn-sm btn-danger rounded-pill w-100">
                                Pesan Paket Ini
                            </a>
                            @if($pkg->demo_url)
                                <a href="{{ $pkg->demo_url }}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-secondary rounded-pill px-3">
                                    Demo
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
    </div>
</section>
