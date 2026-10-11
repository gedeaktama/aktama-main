@extends('layouts.app')

@section('title', 'Katalog Pelatihan AI & TI | ' . ($settings['brand_name'] ?? 'Aktama Digital'))
@section('meta_description', 'Program pelatihan Kecerdasan Artifisial (AI) aplikatif untuk instansi dinas, tenaga kependidikan, UMKM, dan koding pemula bersama fasilitator nasional.')

@section('content')

    <!-- Header Banner -->
    <section class="py-5 bg-light border-bottom">
        <div class="container py-3 text-center">
            <span class="badge bg-info bg-opacity-10 text-info fw-bold text-uppercase px-3 py-1 mb-2">Pendidikan & Pelatihan Komputasi</span>
            <h1 class="display-6 fw-bold font-display text-dark">Pelatihan Kecerdasan Artifisial (AI) Terapan</h1>
            <p class="text-muted max-w-2xl mx-auto small mb-0">
                Tingkatkan kompetensi digital dan otomasi kerja nyata bersama instruktur ahli bersertifikasi Fasilitator Nasional KKA Kemdikdasmen.
            </p>
        </div>
    </section>

    <!-- Daftar Program Pelatihan -->
    <section class="py-5 bg-white">
        <div class="container py-3">
            <div class="row g-4 mb-5">
                @forelse($trainingPrograms as $prog)
                    <div class="col-lg-6">
                        <div class="card card-feature p-4 p-md-5 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge bg-primary bg-opacity-10 text-primary small">
                                        {{ ucfirst(str_replace('-', ' ', $prog->category)) }}
                                    </span>
                                    <span class="text-muted small"><i class="bi bi-clock me-1"></i>{{ $prog->duration }}</span>
                                </div>

                                <h3 class="fw-bold text-dark fs-5 mb-2">{{ $prog->title }}</h3>
                                <p class="text-muted small leading-relaxed mb-4">{{ $prog->objectives }}</p>

                                <div class="p-3 rounded-3 bg-light border mb-4">
                                    <strong class="text-dark d-block small mb-1"><i class="bi bi-people text-info me-1"></i> Target Peserta:</strong>
                                    <span class="text-muted small">{{ $prog->target_audience }}</span>
                                </div>

                                @if($prog->syllabus && is_array($prog->syllabus))
                                    <h6 class="fw-bold text-dark small mb-2"><i class="bi bi-journal-check text-success me-1"></i> Silabus & Pokok Bahasan:</h6>
                                    <ul class="list-unstyled small text-muted mb-4 space-y-2">
                                        @foreach($prog->syllabus as $item)
                                            <li class="mb-2 d-flex align-items-start gap-2">
                                                <i class="bi bi-check-circle-fill text-primary small mt-1"></i>
                                                <span>{{ $item }}</span>
                                            </li>
                                        @endforeach
                                    </ul>
                                @endif
                            </div>

                            <div class="border-top pt-3 d-flex flex-wrap justify-content-between align-items-center gap-3">
                                <div>
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Metode Pelaksanaan:</small>
                                    <span class="badge bg-secondary bg-opacity-10 text-dark small text-uppercase">{{ $prog->delivery_format }}</span>
                                </div>
                                <div class="text-end">
                                    <small class="text-muted d-block" style="font-size: 0.75rem;">Biaya Investasi:</small>
                                    <strong class="text-primary">{{ $prog->price_info ?? 'Sesuai Penawaran' }}</strong>
                                </div>
                                <a href="#form-daftar" class="btn btn-brand rounded-pill btn-sm px-4 ms-auto">
                                    Minta Proposal Pelatihan
                                </a>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="col-12">
                        <div class="alert alert-info">Katalog pelatihan sedang diperbarui.</div>
                    </div>
                @endforelse
            </div>

            <!-- FORMULIR PENAWARAN PELATIHAN -->
            <div id="form-daftar" class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-light">
                <div class="text-center max-w-xl mx-auto mb-4">
                    <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">Formulir Minat Pelatihan</span>
                    <h3 class="fw-bold font-display text-dark">Rencanakan Pelatihan untuk Instansi / Kelompok Anda</h3>
                    <p class="text-muted small">
                        Silakan lengkapi formulir singkat di bawah ini. Kami siap menyusun jadwal, materi yang disesuaikan (*custom syllabus*), serta proposal resmi.
                    </p>
                </div>

                <form action="{{ route('inquiry.store') }}" method="POST" class="max-w-2xl mx-auto">
                    @csrf
                    <input type="hidden" name="service_type" value="pelatihan-ai">
                    <input type="hidden" name="source_page" value="Halaman Pelatihan AI">

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nama Kontak / Penanggung Jawab *</label>
                            <input type="text" name="name" class="form-control rounded-3" required placeholder="Contoh: Dra. Sri Wahyuni">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Nomor WhatsApp *</label>
                            <input type="text" name="whatsapp" class="form-control rounded-3" required placeholder="Contoh: 081234567890">
                        </div>
                    </div>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Instansi / Sekolah / Perusahaan</label>
                            <input type="text" name="organization" class="form-control rounded-3" placeholder="Contoh: Dinas Pendidikan / SMKN 1">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-dark">Email Resmi (Opsional)</label>
                            <input type="email" name="email" class="form-control rounded-3" placeholder="email@instansi.go.id">
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-dark">Program Pelatihan yang Diminati & Jumlah Peserta *</label>
                        <textarea name="message" class="form-control rounded-3" rows="3" required placeholder="Jelaskan topik yang dibutuhkan, perkiraan jumlah peserta (misal: 30 guru / 20 staf), serta rencana tanggal pelaksanaan..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-brand btn-lg w-100 rounded-pill shadow-sm">
                        <i class="bi bi-send-fill me-2"></i> Kirim Permintaan Pelatihan
                    </button>
                </form>
            </div>
        </div>
    </section>

@endsection
