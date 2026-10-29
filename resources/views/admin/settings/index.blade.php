@extends('layouts.admin')

@section('title', 'Pengaturan Situs & Branding')
@section('page_title', 'Pengaturan Situs, Branding & Tampilan')

@section('content')

    <form action="{{ route('admin.settings.update') }}" method="POST" enctype="multipart/form-data">
        @csrf

        <!-- CARD 1: LOGO, MEDIA BRANDING & CAP RESMI -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4 border-start border-primary border-4">
            <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                <h6 class="fw-bold text-dark mb-0">
                    <i class="bi bi-image text-primary me-2"></i> Ganti Logo, Cap Resmi & Favicon
                </h6>
                <span class="badge bg-primary bg-opacity-10 text-primary small">Media Branding</span>
            </div>
            <div class="card-body p-4">
                <p class="text-muted small mb-4">
                    Unggah file gambar baru (PNG, JPG, SVG, WEBP) untuk mengubah logo navbar, cap legalitas stempel perusahaan, dan favicon tab browser secara langsung tanpa mengedit kode.
                </p>

                <div class="row g-4">
                    <!-- Upload Logo Navbar -->
                    <div class="col-md-4">
                        <div class="border rounded-4 p-3 bg-light h-100 text-center d-flex flex-column justify-content-between">
                            <div>
                                <label class="form-label small fw-bold text-dark d-block">Logo Utama Navbar</label>
                                <div class="bg-white p-3 rounded-3 shadow-xs d-inline-flex align-items-center justify-content-center mb-3" style="min-height: 80px; width: 100%;">
                                    <img src="{{ asset($settings['logo_path']->value ?? 'images/logo-aktama.png') }}" alt="Logo Saat Ini" style="max-height: 48px; max-width: 100%; object-fit: contain;">
                                </div>
                            </div>
                            <div>
                                <input type="file" name="logo_file" class="form-control form-control-sm mb-1" accept="image/png,image/jpeg,image/webp,image/svg+xml">
                                <small class="text-muted d-block" style="font-size: 0.7rem;">Maksimal 2 MB (Disarankan PNG transparan)</small>
                            </div>
                        </div>
                    </div>

                    <!-- Upload Cap Resmi Perusahaan -->
                    <div class="col-md-4">
                        <div class="border rounded-4 p-3 bg-light h-100 text-center d-flex flex-column justify-content-between">
                            <div>
                                <label class="form-label small fw-bold text-dark d-block">Cap / Stempel Resmi Perusahaan</label>
                                <div class="bg-white p-3 rounded-3 shadow-xs d-inline-flex align-items-center justify-content-center mb-3" style="min-height: 80px; width: 100%;">
                                    <img src="{{ asset($settings['seal_path']->value ?? 'images/logo-seal-aktama.png') }}" alt="Cap Resmi Saat Ini" style="max-height: 60px; max-width: 100%; object-fit: contain;">
                                </div>
                            </div>
                            <div>
                                <input type="file" name="seal_file" class="form-control form-control-sm mb-1" accept="image/png,image/jpeg,image/webp,image/svg+xml">
                                <small class="text-muted d-block" style="font-size: 0.7rem;">Maksimal 2 MB (Digunakan pada footer & legalitas)</small>
                            </div>
                        </div>
                    </div>

                    <!-- Upload Favicon Tab Browser -->
                    <div class="col-md-4">
                        <div class="border rounded-4 p-3 bg-light h-100 text-center d-flex flex-column justify-content-between">
                            <div>
                                <label class="form-label small fw-bold text-dark d-block">Favicon Tab Browser</label>
                                <div class="bg-white p-3 rounded-3 shadow-xs d-inline-flex align-items-center justify-content-center mb-3" style="min-height: 80px; width: 100%;">
                                    <img src="{{ asset($settings['favicon_path']->value ?? 'images/logo-aktama.png') }}" alt="Favicon Saat Ini" style="max-height: 36px; max-width: 36px; object-fit: contain;">
                                </div>
                            </div>
                            <div>
                                <input type="file" name="favicon_file" class="form-control form-control-sm mb-1" accept="image/png,image/jpeg,image/x-icon,image/svg+xml">
                                <small class="text-muted d-block" style="font-size: 0.7rem;">Maksimal 1 MB (Ikon kecil tab browser)</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 2: HEADER & INFO DI ATAS MENU (TOPBAR) -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4 border-start border-info border-4">
            <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                <h6 class="fw-bold text-dark mb-0">
                    <i class="bi bi-window-dock text-info me-2"></i> Edit Info di Atas Menu (Topbar Header)
                </h6>
                <span class="badge bg-info bg-opacity-10 text-info small">Header Topbar</span>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Teks Entitas di Topbar</label>
                        <input type="text" name="topbar_text" class="form-control" value="{{ $settings['topbar_text']->value ?? 'PT Aktama Digital Antika' }}" required>
                        <small class="text-muted" style="font-size: 0.75rem;">Muncul di sebelah kiri bar hitam paling atas.</small>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Teks Badge Legalitas / Highlight</label>
                        <input type="text" name="topbar_highlight" class="form-control" value="{{ $settings['topbar_highlight']->value ?? 'NIB: 1703250057018 | LPK Resmi Terdaftar' }}">
                        <small class="text-muted" style="font-size: 0.75rem;">Badge legalitas di bar paling atas.</small>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-whatsapp text-success me-1"></i> Nomor WhatsApp Resmi</label>
                        <input type="text" name="whatsapp_number" class="form-control" value="{{ $settings['whatsapp_number']->value ?? '6281234567890' }}" required>
                        <small class="text-muted" style="font-size: 0.75rem;">Gunakan format kode negara (contoh: 6281234567890).</small>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-envelope text-info me-1"></i> Alamat Email Resmi</label>
                        <input type="email" name="email" class="form-control" value="{{ $settings['email']->value ?? 'kontak@aktama.com' }}" required>
                        <small class="text-muted" style="font-size: 0.75rem;">Ditampilkan pada topbar dan kontak footer.</small>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 3: EDIT FOOTER (DESKRIPSI & HAK CIPTA) -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4 border-start border-secondary border-4">
            <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                <h6 class="fw-bold text-dark mb-0">
                    <i class="bi bi-layout-text-window-reverse text-secondary me-2"></i> Edit Teks & Info Footer
                </h6>
                <span class="badge bg-secondary bg-opacity-10 text-dark small">Footer</span>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Deskripsi Profil Perusahaan di Footer</label>
                        <textarea name="footer_description" class="form-control" rows="3" required>{{ $settings['footer_description']->value ?? 'Perusahaan penyedia solusi teknologi terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website & Aplikasi Bisnis, Ekosistem Edukasi Digital, Undangan Online, serta Distribusi Komoditas Kopi Riil.' }}</textarea>
                        <small class="text-muted" style="font-size: 0.75rem;">Teks pengantar di bawah logo pada kolom pertama footer.</small>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Teks Hak Cipta (Copyright)</label>
                        <input type="text" name="footer_copyright" class="form-control" value="{{ $settings['footer_copyright']->value ?? ('© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.') }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Alamat Domisili Perusahaan</label>
                        <input type="text" name="address" class="form-control" value="{{ $settings['address']->value ?? 'Indonesia' }}">
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 4: IDENTITAS BADAN USAHA & LEGALITAS RESMI -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
            <div class="card-header bg-white py-3 border-bottom">
                <h6 class="fw-bold text-dark mb-0"><i class="bi bi-building text-primary me-2"></i> Identitas Perusahaan & Legalitas Resmi</h6>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Nama Resmi Perusahaan (Badan Usaha)</label>
                        <input type="text" name="company_name" class="form-control" value="{{ $settings['company_name']->value ?? 'PT Aktama Digital Antika' }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Nama Brand Utama</label>
                        <input type="text" name="brand_name" class="form-control" value="{{ $settings['brand_name']->value ?? 'Aktama Digital' }}" required>
                    </div>
                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Slogan / Tagline Perusahaan</label>
                        <input type="text" name="tagline" class="form-control" value="{{ $settings['tagline']->value ?? 'Solusi Teknologi, Pelatihan AI, dan Ekosistem Bisnis Digital' }}">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Nomor Induk Berusaha (NIB Resmi)</label>
                        <input type="text" name="nib_number" class="form-control" value="{{ $settings['nib_number']->value ?? '1703250057018' }}">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Status Unit Pelatihan Kerja (LPK)</label>
                        <input type="text" name="lpk_status" class="form-control" value="{{ $settings['lpk_status']->value ?? 'Lembaga Pelatihan Kerja (LPK) Resmi Terdaftar' }}">
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 5: PROFIL PIMPINAN TEKNIS -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
            <div class="card-header bg-white py-3 border-bottom">
                <h6 class="fw-bold text-dark mb-0"><i class="bi bi-person-badge text-info me-2"></i> Profil Kepemimpinan Teknis</h6>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Nama Lengkap & Gelar Pemilik</label>
                        <input type="text" name="owner_name" class="form-control" value="{{ $settings['owner_name']->value ?? 'Gede Erik Aktama, S.Pd., M.Pd.' }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Jabatan & Kredensial Akademik/Nasional</label>
                        <input type="text" name="owner_title" class="form-control" value="{{ $settings['owner_title']->value ?? 'Dosen Prodi Sistem Komputer Univ. Parna Raya & Fasilitator Nasional KKA Kemdikdasmen' }}" required>
                    </div>
                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Biografi / Profil Singkat</label>
                        <textarea name="owner_bio" class="form-control" rows="3">{{ $settings['owner_bio']->value ?? 'Dosen pada Program Studi Sistem Komputer, Universitas Parna Raya, serta Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen.' }}</textarea>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 6: TAUTAN GATEWAY EKOSISTEM BISNIS -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
            <div class="card-header bg-white py-3 border-bottom">
                <h6 class="fw-bold text-dark mb-0"><i class="bi bi-diagram-3-fill text-success me-2"></i> Tautan Gateway Ekosistem Bisnis</h6>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-mortarboard-fill text-success me-1"></i> URL Aktama Academy</label>
                        <input type="url" name="academy_url" class="form-control" value="{{ $settings['academy_url']->value ?? 'http://localhost:8080/aktama/public' }}" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-heart-fill text-danger me-1"></i> URL Undangan Online</label>
                        <input type="url" name="invitation_url" class="form-control" value="{{ $settings['invitation_url']->value ?? 'http://localhost:8080/undanganonline/public' }}" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-cup-hot-fill text-warning me-1"></i> URL Aplikasi / Order Kopi</label>
                        <input type="text" name="coffee_app_url" class="form-control" value="{{ $settings['coffee_app_url']->value ?? 'http://localhost:8080/kopi/public' }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Nama Brand Kopi</label>
                        <input type="text" name="coffee_brand_name" class="form-control" value="{{ $settings['coffee_brand_name']->value ?? 'Kopi Distro Premium' }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark">Tagline Bisnis Kopi</label>
                        <input type="text" name="coffee_tagline" class="form-control" value="{{ $settings['coffee_tagline']->value ?? 'Roastery & Distribusi Biji/Bubuk Kopi Asli Nusantara untuk Retail dan Suplai Kafe' }}">
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 7: SEO DEFAULT GOOGLE -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
            <div class="card-header bg-white py-3 border-bottom">
                <h6 class="fw-bold text-dark mb-0"><i class="bi bi-search text-secondary me-2"></i> Optimasi SEO Default Mesin Pencari</h6>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Meta Title Default</label>
                        <input type="text" name="meta_default_title" class="form-control" value="{{ $settings['meta_default_title']->value ?? 'PT Aktama Digital Antika | Solusi Teknologi, Pelatihan AI & Ekosistem Bisnis' }}">
                    </div>
                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Meta Description Default</label>
                        <textarea name="meta_default_description" class="form-control" rows="2">{{ $settings['meta_default_description']->value ?? 'PT Aktama Digital Antika (NIB 1703250057018) — Penyedia Pelatihan AI Terapan, Jasa Website & POS Bebas Malware, Undangan Online, dan Distribusi Kopi Nusantara.' }}</textarea>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 8: TAUTAN MEDIA SOSIAL RESMI -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4">
            <div class="card-header bg-white py-3 border-bottom">
                <h6 class="fw-bold text-dark mb-0"><i class="bi bi-share text-primary me-2"></i> Tautan Media Sosial Resmi</h6>
            </div>
            <div class="card-body p-4">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-instagram text-danger me-1"></i> URL Instagram Resmi</label>
                        <input type="url" name="instagram_url" class="form-control" value="{{ $settings['instagram_url']->value ?? 'https://instagram.com/aktama.digital' }}" placeholder="https://instagram.com/aktama.digital">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-linkedin text-info me-1"></i> URL LinkedIn Resmi</label>
                        <input type="url" name="linkedin_url" class="form-control" value="{{ $settings['linkedin_url']->value ?? 'https://linkedin.com/in/gedeerikaktama' }}" placeholder="https://linkedin.com/in/gedeerikaktama">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-youtube text-danger me-1"></i> URL Channel YouTube</label>
                        <input type="url" name="youtube_url" class="form-control" value="{{ $settings['youtube_url']->value ?? 'https://youtube.com/@aktama' }}" placeholder="https://youtube.com/@aktama">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-dark"><i class="bi bi-facebook text-primary me-1"></i> URL Halaman Facebook</label>
                        <input type="url" name="facebook_url" class="form-control" value="{{ $settings['facebook_url']->value ?? '' }}" placeholder="https://facebook.com/...">
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 9: BILAH PENGUMUMAN PROMO (ANNOUNCEMENT TOP BAR ALA OPTINMONSTER) -->
        <div class="card border-0 shadow-sm rounded-4 bg-white mb-4 border-start border-warning border-4">
            <div class="card-header bg-white py-3 border-bottom d-flex justify-content-between align-items-center">
                <h6 class="fw-bold text-dark mb-0">
                    <i class="bi bi-megaphone-fill text-warning me-2"></i> Bilah Pengumuman Promo (Announcement Top Bar)
                </h6>
                <span class="badge bg-warning bg-opacity-25 text-dark small">Marketing & Sales</span>
            </div>
            <div class="card-body p-4">
                <p class="text-muted small mb-4">
                    Bilah promo tipis yang muncul di bagian paling atas halaman publik untuk menarik perhatian pengunjung, mengumumkan promo pelatihan AI, diskon jasa website, atau agenda penting.
                </p>

                <div class="row g-3">
                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark">Status Tampilan Bilah</label>
                        <select name="announcement_enabled" class="form-select">
                            <option value="1" {{ ($settings['announcement_enabled']->value ?? '0') == '1' ? 'selected' : '' }}>Aktif (Tampilkan di Publik)</option>
                            <option value="0" {{ ($settings['announcement_enabled']->value ?? '0') == '0' ? 'selected' : '' }}>Nonaktif (Sembunyikan)</option>
                        </select>
                    </div>

                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark">Teks Label Badge</label>
                        <input type="text" name="announcement_badge" class="form-control" value="{{ $settings['announcement_badge']->value ?? 'PROMO TERBATAS' }}" placeholder="PROMO TERBATAS">
                        <small class="text-muted" style="font-size: 0.72rem;">Label sorotan kecil berlatar putih.</small>
                    </div>

                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark">Warna Latar Bilah (Hex)</label>
                        <div class="input-group">
                            <input type="color" class="form-control form-control-color" id="announcementColorInput" value="{{ $settings['announcement_bg_color']->value ?? '#4f46e5' }}" title="Pilih warna latar" onchange="document.getElementById('announcement_bg_color').value = this.value">
                            <input type="text" name="announcement_bg_color" id="announcement_bg_color" class="form-control" value="{{ $settings['announcement_bg_color']->value ?? '#4f46e5' }}">
                        </div>
                    </div>

                    <div class="col-12">
                        <label class="form-label small fw-bold text-dark">Kalimat Pengumuman / Penawaran Promo</label>
                        <input type="text" name="announcement_text" class="form-control" value="{{ $settings['announcement_text']->value ?? '🔥 Promo Spesial: Konsultasi Pembuatan Website & Pelatihan AI Bersertifikat Resmi Terbuka!' }}" placeholder="Tuliskan kalimat ajakan promo di sini...">
                    </div>

                    <div class="col-md-4">
                        <label class="form-label small fw-bold text-dark">Teks Tombol Aksi</label>
                        <input type="text" name="announcement_link_text" class="form-control" value="{{ $settings['announcement_link_text']->value ?? 'Konsultasi Sekarang' }}" placeholder="Konsultasi Sekarang">
                    </div>

                    <div class="col-md-8">
                        <label class="form-label small fw-bold text-dark">Tautan Tujuan Tombol (URL Web atau WhatsApp)</label>
                        <input type="text" name="announcement_link_url" class="form-control" value="{{ $settings['announcement_link_url']->value ?? 'https://wa.me/6285341026331' }}" placeholder="https://wa.me/... atau /halaman/promo">
                    </div>
                </div>
            </div>
        </div>

        <div class="d-flex justify-content-end mb-5">
            <button type="submit" class="btn btn-brand btn-lg rounded-pill px-5 shadow-sm">
                <i class="bi bi-check-circle-fill me-2"></i> Simpan Seluruh Pengaturan & Media
            </button>
        </div>
    </form>

@endsection
