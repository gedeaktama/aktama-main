<!-- SECTION: FORMULIR KONSULTASI & PERMINTAAN PENAWARAN (LEAD MANAGEMENT) -->
<section id="form-konsultasi" class="py-5 bg-light">
    <div class="container py-4">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card border-0 shadow-sm rounded-4 p-4 p-md-5 bg-white">
                    <div class="text-center mb-4">
                        <span class="badge bg-primary bg-opacity-10 text-primary fw-bold text-uppercase px-3 py-1 mb-2">
                            {{ $sectionConfig->badge ?? 'Konsultasi & Penawaran' }}
                        </span>
                        <h3 class="fw-bold font-display text-dark">{{ $sectionConfig->title ?? 'Mulai Diskusi Kebutuhan Anda Hari Ini' }}</h3>
                        <p class="text-muted small mb-0">
                            {{ $sectionConfig->subtitle ?? 'Isi formulir di bawah ini. Data Anda akan dicatat dan Anda juga dapat langsung melanjutkan percakapan melalui WhatsApp resmi.' }}
                        </p>
                    </div>

                    @if ($errors->any())
                        <div class="alert alert-danger rounded-3 small">
                            <ul class="mb-0 ps-3">
                                @foreach ($errors->all() as $error)
                                    <li>{{ $error }}</li>
                                @endforeach
                            </ul>
                        </div>
                    @endif

                    <form action="{{ route('inquiry.store') }}" method="POST">
                        @csrf

                        <div class="row g-3 mb-3">
                            <div class="col-md-6">
                                <label for="name" class="form-label small fw-bold text-dark">Nama Lengkap *</label>
                                <input type="text" class="form-control rounded-3" id="name" name="name" required value="{{ old('name') }}" placeholder="Contoh: Budi Santoso">
                            </div>
                            <div class="col-md-6">
                                <label for="whatsapp" class="form-label small fw-bold text-dark">Nomor WhatsApp Aktif *</label>
                                <input type="text" class="form-control rounded-3" id="whatsapp" name="whatsapp" required value="{{ old('whatsapp') }}" placeholder="Contoh: 081234567890">
                            </div>
                        </div>

                        <div class="row g-3 mb-3">
                            <div class="col-md-6">
                                <label for="email" class="form-label small fw-bold text-dark">Alamat Email (Opsional)</label>
                                <input type="email" class="form-control rounded-3" id="email" name="email" value="{{ old('email') }}" placeholder="nama@email.com">
                            </div>
                            <div class="col-md-6">
                                <label for="organization" class="form-label small fw-bold text-dark">Instansi / Perusahaan / Usaha</label>
                                <input type="text" class="form-control rounded-3" id="organization" name="organization" value="{{ old('organization') }}" placeholder="Nama instansi/sekolah/kafe">
                            </div>
                        </div>

                        <div class="row g-3 mb-3">
                            <div class="col-md-6">
                                <label for="service_type" class="form-label small fw-bold text-dark">Layanan yang Diminati *</label>
                                <select class="form-select rounded-3" id="service_type" name="service_type" required>
                                    <option value="pelatihan-ai" {{ old('service_type') == 'pelatihan-ai' ? 'selected' : '' }}>Pelatihan Kecerdasan Artifisial (AI)</option>
                                    <option value="jasa-website" {{ old('service_type') == 'jasa-website' ? 'selected' : '' }}>Jasa Pembuatan Website & Aplikasi</option>
                                    <option value="aktama-academy" {{ old('service_type') == 'aktama-academy' ? 'selected' : '' }}>Pendaftaran Kursus Aktama Academy</option>
                                    <option value="aktama-coffee" {{ old('service_type') == 'aktama-coffee' ? 'selected' : '' }}>Kemitraan / Pasokan Kopi (Aktama Coffee)</option>
                                    <option value="undangan-online" {{ old('service_type') == 'undangan-online' ? 'selected' : '' }}>Pemesanan Undangan Online</option>
                                    <option value="konsultasi" {{ old('service_type') == 'konsultasi' ? 'selected' : '' }}>Konsultasi Teknologi Umum</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="budget_range" class="form-label small fw-bold text-dark">Perkiraan Anggaran (Opsional)</label>
                                <select class="form-select rounded-3" id="budget_range" name="budget_range">
                                    <option value="">Pilih Rentang Anggaran...</option>
                                    <option value="< 500rb" {{ old('budget_range') == '< 500rb' ? 'selected' : '' }}>Di bawah Rp 500.000 (Undangan / Eceran Kopi)</option>
                                    <option value="1jt - 3jt" {{ old('budget_range') == '1jt - 3jt' ? 'selected' : '' }}>Rp 1.000.000 - Rp 3.000.000 (Web Sederhana / Pelatihan)</option>
                                    <option value="3jt - 10jt" {{ old('budget_range') == '3jt - 10jt' ? 'selected' : '' }}>Rp 3.000.000 - Rp 10.000.000 (Aplikasi Bisnis / POS)</option>
                                    <option value="> 10jt" {{ old('budget_range') == '> 10jt' ? 'selected' : '' }}>Di atas Rp 10.000.000 (Paket Instansi / Enterprise)</option>
                                </select>
                            </div>
                        </div>

                        <div class="mb-4">
                            <label for="message" class="form-label small fw-bold text-dark">Rincian Kebutuhan atau Pertanyaan *</label>
                            <textarea class="form-control rounded-3" id="message" name="message" rows="4" required placeholder="Jelaskan jenis website, topik pelatihan, perkiraan jumlah peserta, atau kebutuhan pasokan kopi yang Anda rencanakan...">{{ old('message') }}</textarea>
                        </div>

                        <button type="submit" class="btn btn-brand btn-lg w-100 rounded-pill shadow-sm">
                            <i class="bi bi-send-fill me-2"></i> Kirim Permintaan Penawaran
                        </button>

                        <small class="text-muted d-block text-center mt-3" style="font-size: 0.75rem;">
                            <i class="bi bi-lock-fill text-success me-1"></i> Data Anda dijamin kerahasiaannya dan hanya digunakan oleh tim resmi PT Aktama Digital Antika.
                        </small>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>
