<?php

namespace Database\Seeders;

use App\Models\Article;
use App\Models\Category;
use App\Models\Course;
use App\Models\HomeSection;
use App\Models\Page;
use App\Models\Portfolio;
use App\Models\Service;
use App\Models\SiteSetting;
use App\Models\TrainingProgram;
use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database with factual, high-quality initial data.
     */
    public function run(): void
    {
        // 1. Akun Admin Utama
        User::updateOrCreate(
            ['email' => 'admin@aktama.com'],
            [
                'name' => 'Administrator Aktama',
                'password' => Hash::make('AdminAktama2026!'),
                'role' => 'admin',
            ]
        );

        $isProd = app()->environment('production');
        $academyUrl = $isProd ? 'https://academy.aktama.com' : 'http://localhost:8080/aktama/public';
        $invitationUrl = $isProd ? 'https://undangan.aktama.com' : 'http://localhost:8080/undanganonline/public';
        $coffeeUrl = $isProd ? 'https://coffee.aktama.com' : 'http://localhost:8080/kopi/public';
        $profileUrl = $isProd ? 'https://profil.aktama.com' : 'http://localhost:8080/portofolio/public';

        // 2. Pengaturan Situs (Site Settings) Faktual & Terverifikasi
        $settings = [
            'company_name' => ['PT Aktama Digital Antika', 'general', 'Nama Resmi Badan Usaha'],
            'brand_name' => ['Aktama Digital', 'general', 'Nama Brand Komersial'],
            'tagline' => ['Solusi Teknologi Terpadu, Pelatihan AI, dan Ekosistem Bisnis Digital', 'general', 'Slogan Perusahaan'],
            'nib_number' => ['1703250057018', 'general', 'Nomor Induk Berusaha (NIB)'],
            'lpk_status' => ['Lembaga Pelatihan Kerja (LPK) Resmi Terdaftar', 'general', 'Status Legalitas Pelatihan'],
            'owner_name' => ['Gede Erik Aktama, S.Pd., M.Pd.', 'owner', 'Direktur Utama / Pemilik'],
            'owner_title' => ['Dosen Prodi Sistem Komputer Univ. Parna Raya & Fasilitator Nasional KKA Kemdikdasmen', 'owner', 'Jabatan & Kredensial Akademik'],
            'owner_bio' => ['Dosen pada Program Studi Sistem Komputer, Universitas Parna Raya, serta Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen. Berfokus pada rekayasa perangkat lunak modern, keamanan web bebas malware, dan literasi teknologi tepat guna.', 'owner', 'Biografi Singkat Direktur'],
            'coffee_brand_name' => ['Aktama Coffee', 'coffee', 'Nama Brand Kopi'],
            'coffee_tagline' => ['Unit Bisnis Roastery & Distribusi Komoditas Kopi Nusantara', 'coffee', 'Tagline Bisnis Kopi'],
            'academy_url' => [$academyUrl, 'gateway', 'URL Gateway Aktama Academy'],
            'invitation_url' => [$invitationUrl, 'gateway', 'URL Gateway Undangan Online'],
            'coffee_app_url' => [$coffeeUrl, 'gateway', 'URL Gateway ERP Kopi'],
            'profile_url' => [$profileUrl, 'gateway', 'URL Website Portofolio & Riset Founder'],
            'whatsapp_number' => ['6285341026331', 'contact', 'Nomor WhatsApp Resmi Bisnis'],
            'email' => ['gedeerikaktama@gmail.com', 'contact', 'Email Resmi Perusahaan'],
            'address' => ['Indonesia', 'contact', 'Alamat Domisili Perusahaan'],
            'instagram_url' => ['https://instagram.com/aktama.digital', 'social', 'URL Instagram Resmi'],
            'linkedin_url' => ['https://linkedin.com/in/gedeerikaktama', 'social', 'URL LinkedIn Resmi'],
            'youtube_url' => ['https://youtube.com/@aktama', 'social', 'URL Channel YouTube'],
            'facebook_url' => ['', 'social', 'URL Halaman Facebook'],
            'meta_default_title' => ['PT Aktama Digital Antika | Solusi Rekayasa Software, Pelatihan AI & Ekosistem Digital', 'seo', 'Default Meta Title'],
            'meta_default_description' => ['PT Aktama Digital Antika (NIB 1703250057018) — Penyedia Jasa Pembuatan Website & Software Bebas Malware, Pelatihan AI Terapan Berlisensi LPK, serta Ekosistem Undangan Online dan Aktama Coffee.', 'seo', 'Default Meta Description'],
            'logo_path' => ['images/logo-aktama.png', 'media', 'Path Logo Utama Navbar'],
            'seal_path' => ['images/logo-seal-aktama.png', 'media', 'Path Cap Resmi Perusahaan'],
            'favicon_path' => ['images/logo-aktama.png', 'media', 'Path Favicon Tab Browser'],
            'topbar_text' => ['PT Aktama Digital Antika', 'header', 'Teks Entitas di Topbar'],
            'topbar_highlight' => ['NIB: 1703250057018 • LPK Resmi Terdaftar', 'header', 'Badge Legalitas di Topbar'],
            'footer_description' => ['Perusahaan penyedia solusi teknologi terpadu: Jasa Rekayasa Website & Aplikasi Bisnis Bebas Malware, Pelatihan Kecerdasan Artifisial (AI) Terapan berlisensi LPK Resmi, serta pengembang ekosistem digital mandiri.', 'footer', 'Deskripsi Perusahaan di Footer'],
            'footer_copyright' => ['© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.', 'footer', 'Teks Copyright Footer'],
            'header_navigation_menu' => [json_encode([
                ['label' => 'Beranda', 'url' => '/', 'target' => '_self'],
                ['label' => 'Tentang Kami', 'url' => '/tentang-kami', 'target' => '_self'],
                ['label' => 'Jasa Website', 'url' => '/jasa-website', 'target' => '_self'],
                ['label' => 'Pelatihan AI', 'url' => '/pelatihan-ai', 'target' => '_self'],
                ['label' => 'Portofolio Proyek', 'url' => '/portofolio', 'target' => '_self'],
                ['label' => 'Profil & Riset Founder', 'url' => $profileUrl, 'target' => '_blank'],
                ['label' => 'Aktama Academy', 'url' => $academyUrl, 'target' => '_blank'],
                ['label' => 'Undangan Online', 'url' => $invitationUrl, 'target' => '_blank'],
                ['label' => 'Aktama Coffee', 'url' => $coffeeUrl, 'target' => '_blank'],
                ['label' => 'Artikel', 'url' => '/artikel', 'target' => '_self'],
            ]), 'menus', 'Menu Navigasi Header'],
        ];

        foreach ($settings as $key => [$value, $group, $label]) {
            SiteSetting::updateOrCreate(
                ['key' => $key],
                ['value' => $value, 'group' => $group, 'type' => 'text', 'label' => $label]
            );
        }

        // 3. Jasa Pembuatan Website & Solusi Digital (Riset Harga Pasar Indonesia Faktual)
        $services = [
            [
                'title' => 'Website Profil Perusahaan & Bisnis (Company Profile)',
                'slug' => 'website-profil-perusahaan',
                'category' => 'website',
                'excerpt' => 'Membangun kehadiran profesional perusahaan dengan desain elegan, cepat, dan terproteksi dari celah malware.',
                'description' => 'Layanan pembuatan website profil perusahaan modern untuk merepresentasikan kredibilitas bisnis kepada klien, investor, dan mitra usaha. Dilengkapi arsitektur kode bersih, mobile-responsive, optimasi SEO on-page, formulir terhubung WhatsApp, dan panel CMS admin mandiri.',
                'price_starting' => 'Mulai Rp 2.500.000',
                'features' => [
                    '3 - 6 Halaman Utama Profesional',
                    'Bebas Celah Injeksi Script Malware & Judol',
                    'Desain Mobile-First Responsif & Cepat',
                    'Integrasi WhatsApp & Formulir Penawaran',
                    'Optimasi Google Search & SEO On-Page Dasar'
                ],
                'icon' => 'bi-briefcase',
                'is_featured' => true,
                'sort_order' => 1,
            ],
            [
                'title' => 'Website Sekolah, Kampus & Lembaga Pendidikan',
                'slug' => 'website-lembaga-pendidikan',
                'category' => 'website',
                'excerpt' => 'Portal resmi institusi pendidikan untuk publikasi berita, profil pendidik, galeri, dan PPDB online.',
                'description' => 'Website terstruktur rapi untuk sekolah, madrasah, pesantren, dan perguruan tinggi. Memudahkan pengumuman kalender akademik, direktori guru/dosen, unduhan dokumen resmi, serta formulir pendaftaran peserta didik baru (PPDB).',
                'price_starting' => 'Mulai Rp 4.500.000',
                'features' => [
                    'Portal Pengumuman & Berita Berkala',
                    'Sistem Informasi Profil Pendidik & Prestasi',
                    'Modul Formulir Pendaftaran Online (PPDB)',
                    'Keamanan Data Tingkat Tinggi & Bebas Spam',
                    'Pelatihan Pengelolaan untuk Staf Operator'
                ],
                'icon' => 'bi-mortarboard',
                'is_featured' => true,
                'sort_order' => 2,
            ],
            [
                'title' => 'Aplikasi Kasir & Stok (POS Grosir/Retail)',
                'slug' => 'aplikasi-kasir-dan-stok',
                'category' => 'aplikasi',
                'excerpt' => 'Sistem pencatatan transaksi kasir, inventaris multi-satuan, cetak struk thermal, dan buku piutang tempo.',
                'description' => 'Aplikasi web operasional internal untuk toko retail, distributor, minimarket, atau kedai kopi. Mendukung pembedaan level harga eceran vs grosir, cetak surat jalan / faktur, kontrol stok real-time, dan pemantauan laba rugi berkala.',
                'price_starting' => 'Mulai Rp 5.000.000',
                'features' => [
                    'Pembeda Otomatis Harga Eceran & Grosir',
                    'Cetak Nota Kasir & Surat Jalan Pengiriman',
                    'Pencatatan Buku Piutang & Jatuh Tempo Pelanggan',
                    'Multi-User (Hak Akses Admin, Kasir, & Gudang)',
                    'Dapat Diakses Melalui Laptop, Tablet, & Smartphone'
                ],
                'icon' => 'bi-receipt',
                'is_featured' => true,
                'sort_order' => 3,
            ],
            [
                'title' => 'Pengembangan Sistem Informasi & Web Custom',
                'slug' => 'pengembangan-aplikasi-web-custom',
                'category' => 'aplikasi',
                'excerpt' => 'Solusi sistem informasi berbasis web yang dirancang 100% mengikuti SOP dan alur kerja spesifik organisasi.',
                'description' => 'Pengembangan perangkat lunak kustom menggunakan arsitektur Laravel dan database MySQL yang tangguh. Cocok untuk portal kepegawaian, sistem penilaian akademik, otomasi operasional bisnis, atau integrasi API pihak ketiga.',
                'price_starting' => 'Mulai Rp 12.500.000 (Sesuai KAK)',
                'features' => [
                    'Arsitektur Monolit Modern Bersih & Skalalabel',
                    'Otorisasi Peran Berjenjang & Log Audit Aktivitas',
                    'Integrasi REST API & Payment Gateway (Midtrans/dll)',
                    'Garansi Pemeliharaan Bug & Pendampingan Pasca-Rilis'
                ],
                'icon' => 'bi-cpu',
                'is_featured' => false,
                'sort_order' => 4,
            ],
        ];

        foreach ($services as $srv) {
            Service::updateOrCreate(['slug' => $srv['slug']], $srv);
        }

        // 4. Katalog Pelatihan AI & TI (Fasilitator Nasional KKA & LPK Terdaftar)
        $trainingPrograms = [
            [
                'title' => 'Pemanfaatan AI untuk Efisiensi Administrasi Perkantoran',
                'slug' => 'ai-untuk-efisiensi-administrasi-perkantoran',
                'category' => 'ai-kantor',
                'target_audience' => 'Staf Administrasi, Sekretaris, Pejabat Fungsional, dan ASN Instansi Pemerintah',
                'objectives' => 'Meningkatkan kecepatan dan ketepatan penyusunan surat dinas baku, telaah staf, notula rapat komprehensif, dan pengolahan data spreadsheet menggunakan generative AI secara etis dan aman.',
                'syllabus' => [
                    'Prinsip Kerja LLM & Etika Keamanan Data Rahasia Instansi',
                    'Prompt Engineering Terstruktur untuk Dokumen Dinas & Notula',
                    'Analisis Data & Pembuatan Formula Spreadsheet Kompleks dengan AI',
                    'Studi Kasus Efisiensi Kerja Rutin Kantor Tanpa Celah Kebocoran Data'
                ],
                'delivery_format' => 'hybrid',
                'duration' => '1 - 2 Hari Intensif (Workshop)',
                'price_info' => 'Penawaran Instansi / KAK Resmi',
                'is_featured' => true,
                'sort_order' => 1,
            ],
            [
                'title' => 'AI untuk Tenaga Pendidik & Perancangan Modul Ajar Interaktif',
                'slug' => 'ai-untuk-tenaga-pendidik',
                'category' => 'ai-pendidikan',
                'target_audience' => 'Guru, Dosen, Instruktur Vokasi, dan Tim Pengembang Kurikulum',
                'objectives' => 'Mendampingi tenaga pendidik merancang Rencana Pembelajaran, modul ajar berdiferensiasi, kisi-kisi soal penalaran tingkat tinggi (HOTS), dan presentasi multimedia secara efektif.',
                'syllabus' => [
                    'Integrasi AI dalam Kurikulum Merdeka & Pembelajaran Berpusat pada Siswa',
                    'Perumusan Modul Ajar dan Lembar Kerja Peserta Didik (LKPD)',
                    'Penyusunan Bank Soal HOTS & Rubrik Penilaian Otomatis',
                    'Etika Penggunaan AI bagi Guru dan Peserta Didik di Lingkungan Sekolah'
                ],
                'delivery_format' => 'hybrid',
                'duration' => '16 Jam Pelatihan (Sertifikat LPK)',
                'price_info' => 'In-House Training Sekolah / Kampus',
                'is_featured' => true,
                'sort_order' => 2,
            ],
            [
                'title' => 'Pemanfaatan AI untuk Produktivitas Bisnis & Pemasaran UMKM',
                'slug' => 'ai-untuk-produktivitas-bisnis-umkm',
                'category' => 'ai-bisnis',
                'target_audience' => 'Pelaku UMKM, Wirausahawan, Tim Pemasaran, dan Content Creator',
                'objectives' => 'Membekali pelaku usaha dengan kapabilitas membuat materi promosi, riset kompetitor, penulisan copywriting persuasif, dan otomasi balasan chat pelanggan WhatsApp.',
                'syllabus' => [
                    'Riset Audiens Target & Ideasi Konten Produk Unik',
                    'Formula Copywriting Iklan & Penulisan Penawaran Menjual',
                    'Kreasi Visual Produk & Banner Media Sosial dengan Alat Bantu AI',
                    'Menyusun Standard Operating Procedure (SOP) Balasan Chat Cepat'
                ],
                'delivery_format' => 'online',
                'duration' => '2 Sesi Intensif (8 Jam)',
                'price_info' => 'Rp 250.000 / Peserta (Kelas Publik)',
                'is_featured' => false,
                'sort_order' => 3,
            ],
            [
                'title' => 'Dasar Pemikiran Komputasi & Logika Koding (KKA) untuk Pemula',
                'slug' => 'dasar-pemikiran-komputasi-dan-koding',
                'category' => 'coding',
                'target_audience' => 'Pelajar, Mahasiswa, Calon Programmer, dan Guru Pembina IT',
                'objectives' => 'Membangun logika computational thinking, algoritma terstruktur, dekomposisi masalah kompleks, dan fondasi pengkodean web modern.',
                'syllabus' => [
                    'Dekomposisi, Pengenalan Pola, dan Abstraksi Masalah Komputasi',
                    'Struktur Logika Algoritma: Sekuensial, Percabangan, dan Perulangan',
                    'Implementasi Sintaks Dasar Pemrograman Berbasis Masalah Riil',
                    'Penyusunan Proyek Akhir Berstandar Portofolio Teknis'
                ],
                'delivery_format' => 'hybrid',
                'duration' => '3 Minggu (6 Sesi Terjadwal)',
                'price_info' => 'Rp 450.000 / Peserta',
                'is_featured' => true,
                'sort_order' => 4,
            ],
        ];

        foreach ($trainingPrograms as $prog) {
            TrainingProgram::updateOrCreate(['slug' => $prog['slug']], $prog);
        }

        // 5. Kursus Pembelajaran (Aktama Academy LMS)
        $courses = [
            [
                'title' => 'Dasar Pemrograman Web Modern (HTML5, CSS3, & PHP)',
                'slug' => 'dasar-pemrograman-web-modern',
                'level' => 'Tingkat Pemula',
                'price' => 149000,
                'summary' => 'Belajar terstruktur dari konsep dasar web hingga berhasil mendeploy website perdana di server hosting.',
                'external_link' => $academyUrl,
                'is_published' => true,
            ],
            [
                'title' => 'Membangun Aplikasi Bisnis & POS dengan Laravel Framework',
                'slug' => 'membangun-aplikasi-bisnis-dengan-laravel',
                'level' => 'Tingkat Menengah',
                'price' => 299000,
                'summary' => 'Panduan terapan merancang sistem kasir, manajemen stok multi-harga, otorisasi hak akses, dan pelaporan keuangan.',
                'external_link' => $academyUrl,
                'is_published' => true,
            ],
            [
                'title' => 'Prompt Engineering & Otomasi AI untuk Administrasi Perkantoran',
                'slug' => 'prompt-engineering-ai-administrasi',
                'level' => 'Tingkat Pemula - Menengah',
                'price' => 199000,
                'summary' => 'Otomasi penyusunan naskah dinas baku, ringkasan notula rapat eksekutif, dan formula spreadsheet kompleks dengan Generative AI.',
                'external_link' => $academyUrl,
                'is_published' => true,
            ],
            [
                'title' => 'Computational Thinking & Logika Koding (KKA) untuk Tenaga Pendidik',
                'slug' => 'koding-kka-tenaga-pendidik',
                'level' => 'Tingkat Pemula',
                'price' => 249000,
                'summary' => 'Panduan perancangan modul ajar Koding dan Kecerdasan Artifisial (KKA) Kurikulum Merdeka beserta bank soal penalaran.',
                'external_link' => $academyUrl,
                'is_published' => true,
            ],
        ];

        foreach ($courses as $c) {
            Course::updateOrCreate(['slug' => $c['slug']], $c);
        }

        // 6. Portofolio Proyek Terverifikasi
        $portfolios = [
            [
                'title' => 'Website Portofolio Profesional & Publikasi Riset SINTA Founder',
                'slug' => 'website-portofolio-riset-founder',
                'category' => 'website',
                'client_type' => 'Akademisi & Personal Branding',
                'technology' => 'Laravel 12, Filament 5, Tailwind CSS, MySQL',
                'project_year' => '2026',
                'project_url' => $profileUrl,
                'description' => 'Portal resmi publikasi jurnal terakreditasi SINTA 4 & 5, riset computer vision deteksi manusia, dan rekam jejak akademik Ketua Prodi Sistem Komputer UNIPAR.',
                'is_published' => true,
            ],
            [
                'title' => 'Sistem Informasi Kelulusan & Pengesahan Dokumen Sekolah',
                'slug' => 'sistem-informasi-kelulusan-sekolah',
                'category' => 'aplikasi',
                'client_type' => 'Lembaga Pendidikan Menengah',
                'technology' => 'Laravel 11, MySQL, Bootstrap 5',
                'project_year' => '2024',
                'project_url' => null,
                'description' => 'Sistem publikasi surat keterangan kelulusan dengan verifikasi QR code dan pencarian instan berbasis NISN.',
                'is_published' => true,
            ],
            [
                'title' => 'Sistem POS Kasir & Inventaris Multi-Toko (Kopi Distro)',
                'slug' => 'sistem-pos-kasir-inventaris',
                'category' => 'aplikasi',
                'client_type' => 'Bisnis Retail & Grosir Roastery',
                'technology' => 'Laravel 12, MySQL, Bootstrap 5.3',
                'project_year' => '2025',
                'project_url' => $coffeeUrl,
                'description' => 'Aplikasi pencatatan stok barang, transaksi kasir eceran & grosir, cetak surat jalan, dan buku piutang tempo.',
                'is_published' => true,
            ],
            [
                'title' => 'Platform Undangan Pernikahan Digital Mobile-First',
                'slug' => 'platform-undangan-digital',
                'category' => 'website',
                'client_type' => 'Layanan Konsumen Publik',
                'technology' => 'Laravel 12, MySQL, JavaScript Interaktif',
                'project_year' => '2025',
                'project_url' => $invitationUrl,
                'description' => 'Portal undangan online responsif dengan personalisasi nama tamu, reservasi RSVP, amplop digital, dan integrasi maps.',
                'is_published' => true,
            ],
        ];

        foreach ($portfolios as $p) {
            Portfolio::updateOrCreate(['slug' => $p['slug']], $p);
        }

        // 7. Kategori & 10 Artikel Blog Strategis & Edukatif
        $this->call(ArticleSeeder::class);

        // 8. Seksi Beranda Default (Clean Modular Sections)
        // Bersihkan seksi lama yang tidak lagi dipakai
        HomeSection::whereIn('section_key', ['aktama_academy', 'aktama_coffee', 'undangan_online'])->delete();

        $homeSections = [
            [
                'section_key' => 'hero',
                'name' => 'Hero Banner & Profil Utama',
                'badge' => 'PT Aktama Digital Antika • NIB: 1703250057018',
                'title' => 'Solusi Rekayasa Perangkat Lunak, Pelatihan AI Terapan, dan Ekosistem Bisnis Digital',
                'subtitle' => 'Perusahaan teknologi berbadan hukum resmi penyedia jasa pembuatan website & aplikasi bisnis bebas malware, Lembaga Pelatihan Kerja (LPK) AI & Koding berlisensi, serta pengembang ekosistem digital mandiri.',
                'sort_order' => 1,
                'is_active' => true,
            ],
            [
                'section_key' => 'mitra_klien',
                'name' => 'Mitra Kerjasama & Social Proof',
                'badge' => 'Jejak Rekam Kepercayaan',
                'title' => 'Dipercaya Lintas Sektor Instansi & Bisnis',
                'subtitle' => 'Membangun sinergi berdampak nyata bersama kepolisian, institusi pendidikan, sekolah, dan pelaku usaha.',
                'sort_order' => 2,
                'is_active' => true,
            ],
            [
                'section_key' => 'jasa_website',
                'name' => 'Jasa Pembuatan Website & Aplikasi',
                'badge' => 'Software House & Rekayasa Web',
                'title' => 'Jasa Pembuatan Website & Sistem Informasi Bebas Celah Malware',
                'subtitle' => 'Didesain dengan arsitektur modern berstandar enterprise yang kebal dari risiko injeksi script judi online, cepat, mobile-friendly, dan teroptimasi SEO.',
                'sort_order' => 3,
                'is_active' => true,
            ],
            [
                'section_key' => 'pelatihan_ai',
                'name' => 'Pelatihan AI & Koding (LPK Terdaftar)',
                'badge' => 'Pusat Pelatihan AI & Teknologi',
                'title' => 'Program Pelatihan Kecerdasan Artifisial (AI) & Koding Praktis',
                'subtitle' => 'Disusun langsung oleh Fasilitator Nasional KKA Kemdikdasmen berlisensi LPK resmi untuk mendongkrak produktivitas instansi pemerintah, sekolah, dan pelaku usaha.',
                'sort_order' => 4,
                'is_active' => true,
            ],
            [
                'section_key' => 'dokumentasi_kegiatan',
                'name' => 'Dokumentasi Kelas & Pelatihan Lapangan',
                'badge' => 'Social Proof LPK',
                'title' => 'Dokumentasi Kelas Pelatihan & Implementasi Lapangan',
                'subtitle' => 'Bukti dedikasi transfer teknologi nyata melalui workshop tatap muka, bimbingan teknis AI di instansi pemerintah, dan serah terima sistem informasi.',
                'sort_order' => 5,
                'is_active' => true,
            ],
            [
                'section_key' => 'ekosistem_digital',
                'name' => 'Ekosistem Produk & Layanan Terpadu',
                'badge' => 'Ekosistem Bisnis Aktama',
                'title' => 'Ekosistem Produk Digital & Unit Bisnis Terpadu',
                'subtitle' => 'Jelajahi lini produk perangkat lunak unggulan, platform pembelajaran daring, dan unit komoditas riil yang dikembangkan dan dikelola oleh PT Aktama Digital Antika.',
                'sort_order' => 6,
                'is_active' => true,
            ],
            [
                'section_key' => 'portofolio',
                'name' => 'Portofolio Proyek Terverifikasi',
                'badge' => 'Bukti Kinerja Nyata',
                'title' => 'Portofolio Implementasi Sistem & Rekayasa Digital',
                'subtitle' => 'Jejak karya sistem informasi, aplikasi kasir operasional, dan portal web yang telah sukses diimplementasikan dan digunakan secara riil.',
                'sort_order' => 7,
                'is_active' => true,
            ],
            [
                'section_key' => 'testimoni',
                'name' => 'Ulasan & Testimoni Mitra',
                'badge' => 'Kepuasan Stakeholder',
                'title' => 'Apa Kata Peserta Pelatihan & Mitra Kami?',
                'subtitle' => 'Testimoni nyata dari perwakilan instansi kepolisian, pendidik sekolah, serta pemilik usaha retail.',
                'sort_order' => 8,
                'is_active' => true,
            ],
            [
                'section_key' => 'tentang_kami',
                'name' => 'Profil Pimpinan & Legalitas Perusahaan',
                'badge' => 'Integritas & Kepemimpinan',
                'title' => 'Integritas Legalitas & Kepemimpinan Berbasis Kompetensi Akademik',
                'subtitle' => 'Didirikan dengan landasan kepatuhan hukum yang solid serta dipimpin oleh praktisi sekaligus akademisi yang berkomitmen pada transfer teknologi nyata.',
                'sort_order' => 9,
                'is_active' => true,
            ],
            [
                'section_key' => 'artikel',
                'name' => 'Artikel & Wawasan Teknologi',
                'badge' => 'Wawasan & Literasi Digital',
                'title' => 'Wawasan Terkini Seputar AI, Keamanan Web, & Bisnis Digital',
                'subtitle' => 'Artikel edukatif dan panduan praktis untuk membantu Anda memahami perkembangan lanskap teknologi terkini secara bijak.',
                'sort_order' => 10,
                'is_active' => true,
            ],
            [
                'section_key' => 'faq',
                'name' => 'FAQ (Pertanyaan yang Sering Diajukan)',
                'badge' => 'Transparansi Layanan',
                'title' => 'Pertanyaan yang Sering Diajukan (FAQ)',
                'subtitle' => 'Jawaban transparan seputar legalitas pelatihan LPK, garansi keamanan rekayasa website, serta prosedur kolaborasi resmi bersama PT Aktama Digital Antika.',
                'sort_order' => 11,
                'is_active' => true,
            ],
            [
                'section_key' => 'form_konsultasi',
                'name' => 'Formulir Konsultasi & Permintaan Penawaran',
                'badge' => 'Mulai Kolaborasi',
                'title' => 'Konsultasikan Kebutuhan Teknologi atau Pelatihan Anda',
                'subtitle' => 'Isi formulir ringkas di bawah ini atau hubungi saluran resmi kami. Tim teknis Aktama Digital siap menganalisis kebutuhan Anda dan memberikan solusi terbaik.',
                'sort_order' => 12,
                'is_active' => true,
            ],
        ];

        foreach ($homeSections as $sec) {
            HomeSection::updateOrCreate(['section_key' => $sec['section_key']], $sec);
        }

        // 9. Halaman Kustom Default (CMS Pages) - Standar Kepatuhan UU PDP No. 27/2022
        Page::updateOrCreate(
            ['slug' => 'kebijakan-privasi'],
            [
                'title' => 'Kebijakan Privasi (Privacy Policy)',
                'editor_type' => 'standard',
                'content_html' => '<div class="py-2">
                    <p class="lead text-muted">Kebijakan Privasi ini menjelaskan bagaimana <strong>PT Aktama Digital Antika</strong> (NIB: <code>1703250057018</code>) mengumpulkan, mengelola, memproses, dan melindungi data pribadi Anda sesuai dengan <strong>Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)</strong>.</p>
                    
                    <h3 class="fw-bold text-dark mt-4 mb-2">1. Prinsip Pengumpulan Informasi</h3>
                    <p>Kami hanya mengumpulkan data pribadi yang diserahkan secara sukarela oleh pengguna saat:</p>
                    <ul>
                        <li>Mengisi formulir konsultasi, permohonan penawaran harga (inquiry), atau pemesanan jasa rekayasa perangkat lunak.</li>
                        <li>Melakukan pendaftaran program pelatihan kerja (LPK), webinar, atau workshop.</li>
                        <li>Menghubungi layanan pelanggan kami melalui saluran resmi WhatsApp atau email.</li>
                    </ul>
                    <p>Data yang dihimpun mencakup: nama lengkap, alamat email, nomor telepon/WhatsApp, nama instansi/organisasi, serta rincian pesan kebutuhan.</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">2. Tujuan Pemrosesan Data Pribadi</h3>
                    <p>Informasi pribadi Anda diproses secara sah untuk tujuan:</p>
                    <ul>
                        <li>Menyusun dokumen penawaran teknis, Kerangka Acuan Kerja (KAK), dan perjanjian kerjasama resmi.</li>
                        <li>Penerbitan sertifikat pelatihan kerja berlisensi LPK resmi yang dilengkapi nomor identifikasi unik.</li>
                        <li>Komunikasi koordinasi pelaksanaan proyek dan layanan purna jual (maintenance support).</li>
                        <li>Memenuhi kewajiban pelaporan administratif sesuai peraturan perundang-undangan yang berlaku di Indonesia.</li>
                    </ul>

                    <h3 class="fw-bold text-dark mt-4 mb-2">3. Jaminan Keamanan & Kerahasiaan Data</h3>
                    <p>PT Aktama Digital Antika menerapkan standar keamanan teknologi informasi yang ketat. Kami <strong>tidak pernah menjual, menyewakan, atau memperdagangkan</strong> data pribadi Anda kepada pihak ketiga manapun untuk kepentingan komersial.</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">4. Hak Subjek Data Pribadi</h3>
                    <p>Sesuai UU PDP, Anda memiliki hak untuk meminta akses, pembaharuan, koreksi kesalahan, atau penghapusan data pribadi Anda dari sistem kami dengan mengajukan permohonan resmi ke email: <code>gedeerikaktama@gmail.com</code>.</p>
                </div>',
                'meta_title' => 'Kebijakan Privasi | PT Aktama Digital Antika',
                'meta_description' => 'Kebijakan privasi resmi PT Aktama Digital Antika sesuai UU Pelindungan Data Pribadi (UU PDP No. 27/2022).',
                'is_published' => true,
                'sort_order' => 1,
            ]
        );

        Page::updateOrCreate(
            ['slug' => 'syarat-ketentuan'],
            [
                'title' => 'Syarat & Ketentuan Layanan (Terms of Service)',
                'editor_type' => 'standard',
                'content_html' => '<div class="py-2">
                    <p class="lead text-muted">Selamat datang di portal resmi <strong>PT Aktama Digital Antika</strong>. Dengan mengakses situs ini dan menggunakan layanan rekayasa perangkat lunak serta program pelatihan kami, Anda menyetujui ketentuan-ketentuan di bawah ini:</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">1. Ruang Lingkup Layanan & Perjanjian Kerja</h3>
                    <p>Penyediaan jasa pembuatan website, pengembangan sistem informasi, dan pelatihan AI diatur berdasarkan Surat Perjanjian Kerja (SPK), Surat Perintah Kerja, atau Kerangka Acuan Kerja (KAK) resmi yang ditandatangani kedua belah pihak.</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">2. Standar Integritas & Jaminan Bebas Malware</h3>
                    <p>PT Aktama Digital Antika berkomitmen menyerahkan perangkat lunak yang dibangun di atas fondasi teknologi yang kokoh, terbebas dari script tersembunyi berbahaya, celah injeksi situs judi online, maupun backdoor yang dapat merugikan reputasi klien.</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">3. Sertifikat Pelatihan & Kode Etik LPK</h3>
                    <p>Sertifikat yang diterbitkan oleh Lembaga Pelatihan Kerja (LPK) PT Aktama Digital Antika diberikan kepada peserta yang telah memenuhi seluruh syarat kehadiran dan penugasan evaluasi materi. Penyalahgunaan sertifikat untuk tindakan melanggar hukum di luar tanggung jawab PT Aktama Digital Antika.</p>

                    <h3 class="fw-bold text-dark mt-4 mb-2">4. Hak Kekayaan Intelektual</h3>
                    <p>Seluruh materi publikasi, logo, modul pelatihan, dan konten artikel di situs web ini dilindungi hak cipta. Pengutipan materi artikel untuk kepentingan akademik atau edukasi diperkenankan dengan mencantumkan sumber rujukan jelas ke <code>https://aktama.com</code>.</p>
                </div>',
                'meta_title' => 'Syarat & Ketentuan Layanan | PT Aktama Digital Antika',
                'meta_description' => 'Syarat dan ketentuan layanan resmi PT Aktama Digital Antika.',
                'is_published' => true,
                'sort_order' => 2,
            ]
        );

        // 10. Sanitasi Data Uji Coba (Memastikan Database Produksi Bersih)
        // Bersihkan data lead atau formulir dummy jika pernah diisi selama masa uji coba lokal
        if (\Illuminate\Support\Facades\Schema::hasTable('leads')) {
            \App\Models\Lead::where('name', 'like', '%test%')
                ->orWhere('name', 'like', '%coba%')
                ->orWhere('name', 'like', '%dummy%')
                ->orWhere('whatsapp', 'like', '%123456%')
                ->orWhere('email', 'like', '%example.com%')
                ->delete();
        }
    }
}
