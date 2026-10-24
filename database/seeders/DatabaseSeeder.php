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
        $catAi = Category::updateOrCreate(['slug' => 'kecerdasan-artifisial'], ['name' => 'Kecerdasan Artifisial (AI)']);
        $catWeb = Category::updateOrCreate(['slug' => 'keamanan-web-modern'], ['name' => 'Keamanan & Web Modern']);
        $catBiz = Category::updateOrCreate(['slug' => 'inovasi-bisnis-umkm'], ['name' => 'Inovasi Bisnis & UMKM']);
        $catEdu = Category::updateOrCreate(['slug' => 'literasi-digital-koding'], ['name' => 'Literasi Digital & Koding']);
        $catRes = Category::updateOrCreate(['slug' => 'riset-publikasi-ilmiah'], ['name' => 'Riset & Publikasi Ilmiah']);

        $articles = [
            [
                'slug' => 'mengapa-guru-yang-menguasai-ai-bukan-tergantikan',
                'category_id' => $catAi->id,
                'title' => 'Mengapa Guru yang Menguasai AI Bukan Tergantikan, Melainkan Menggantikan Mereka yang Menolak Belajar',
                'image' => 'articles/article-ai-guru.jpg',
                'summary' => 'Banyak pendidik cemas kecerdasan buatan akan merebut peran guru di kelas. Faktanya, AI tidak menggantikan empati dan keteladanan seorang pendidik, melainkan melipatgandakan produktivitas administrasi dan diferensiasi pembelajaran hingga 5 kali lipat.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Di tengah pesatnya perkembangan model bahasa cerdas seperti ChatGPT, Claude, dan Gemini, muncul kegelisahan di kalangan pendidik: <em>"Apakah profesi guru akan segera usang dan digantikan oleh algoritma?"</em></p>' .
                    '<p>Jawabannya tegas: <strong>Tidak</strong>. Kecerdasan artifisial tidak memiliki jiwa, empati, dan kepekaan nurani untuk memotivasi anak didik yang sedang terpuruk atau menanamkan integritas moral. Namun, pepatah baru di era transformasi digital ini telah terbukti nyata: <strong>"AI tidak akan menggantikan guru, tetapi guru yang menguasai AI akan menggantikan guru yang menolak untuk belajar."</strong></p>' .
                    '<h2>Tiga Beban Berat Guru yang Tuntas dalam Hitungan Menit</h2>' .
                    '<p>Survei internal pendidik menunjukkan bahwa lebih dari 60% waktu kerja seorang guru tersedot untuk tugas-tugas administratif rutin. Ketika AI diintegrasikan secara etis dan tepat sasaran, efisiensi spektakuler langsung dirasakan:</p>' .
                    '<ul>' .
                    '<li><strong>Penyusunan Modul Ajar Berdiferensiasi:</strong> Merancang materi yang disesuaikan untuk siswa dengan kecepatan belajar berbeda (kinestetik, visual, auditori) biasanya memakan waktu berhari-hari. Bersama AI, draf awal diferensiasi konten selesai dalam 15 menit.</li>' .
                    '<li><strong>Pembuatan Rubrik Asesmen Autentik:</strong> Merumuskan indikator capaian pembelajaran berbasis taksonomi Bloom revisi yang selaras dengan Kurikulum Merdeka.</li>' .
                    '<li><strong>Bank Soal Kontekstual & Studi Kasus:</strong> Mengubah konsep teoritis yang rumit menjadi analogi kehidupan sehari-hari yang dekat dengan peserta didik daerah setempat.</li>' .
                    '</ul>' .
                    '<blockquote>"Kecerdasan Artifisial adalah co-pilot terbaik bagi guru. Ia mengambil alih kerja mekanis yang melelahkan, sehingga guru dapat kembali ke hakikat mulia profesinya: mendidik manusia dengan cinta dan keteladanan."<br><strong>— Gede Erik Aktama, S.Pd., M.Pd.</strong></blockquote>' .
                    '<h2>Yang Tidak Akan Pernah Dimiliki Algoritma AI</h2>' .
                    '<p>Algoritma dapat merangkum ratusan buku dalam 3 detik, tetapi ia tidak bisa melihat mata seorang murid yang kehilangan kepercayaan diri. Guru adalah inspirator, jangkar emosional, dan model karakter. AI membebaskan guru dari tumpukan berkas administratif agar guru memiliki energi lebih untuk mendengarkan, membimbing, dan menyalakan api rasa ingin tahu siswa di ruang kelas.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-mortarboard-fill me-2"></i>Tingkatkan Kompetensi AI Sekolah Anda</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika melalui divisi <strong>LPK Aktama</strong> dan platform <strong>Aktama Academy</strong> menyediakan Bimbingan Teknis (Bimtek) In-House AI khusus guru, dosen, dan yayasan pendidikan dengan sertifikasi resmi terdaftar pemerintah.</p>' .
                    '<div class="d-flex flex-wrap gap-2">' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Konsultasi Bimtek In-House</a>' .
                    '<a href="https://academy.aktama.com" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill px-3">Akses Aktama Academy ↗</a>' .
                    '</div>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(1),
                'meta_title' => 'Mengapa Guru yang Menguasai AI Bukan Tergantikan | Aktama Digital',
                'meta_description' => 'Bagaimana guru memanfaatkan kecerdasan artifisial untuk memangkas beban administrasi dan meningkatkan mutu pembelajaran Kurikulum Merdeka.',
            ],
            [
                'slug' => 'fenomena-web-sekolah-disusupi-spam-judol-dan-solusinya',
                'category_id' => $catWeb->id,
                'title' => 'Fenomena Web Sekolah & Instansi Disusupi Spam Judol: Penyebab Utama dan Cara Menangkalnya Secara Permanen',
                'image' => 'articles/article-web-security.jpg',
                'summary' => 'Banyak portal sekolah dan instansi pemerintah mendadak dipenuhi link judi online di pencarian Google. Pahami anatomi injeksi database ini dan bagaimana arsitektur framework modern seperti Laravel memutus celah malware tersebut.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Pernahkah Anda mengetik nama sekolah, universitas, atau dinas pemerintah di mesin pencari Google, namun hasil teratas yang muncul justru memuat judul dan tautan ke situs slot atau judi online?</p>' .
                    '<p>Fenomena <em>SEO Hijacking</em> atau injeksi backlink judi online pada domain berakhiran <code>.sch.id</code>, <code>.ac.id</code>, dan <code>.go.id</code> telah menjadi krisis siber nasional di Indonesia. Pelaku peretasan sengaja mengincar domain pemerintah dan pendidikan karena memiliki skor otoritas domain (Domain Authority) yang tinggi di mata mesin pencari.</p>' .
                    '<h2>Bagaimana Celah Ini Terbuka?</h2>' .
                    '<p>Mayoritas website sekolah atau instansi dibangun menggunakan Content Management System (CMS) berbasis template instan dengan puluhan plugin pihak ketiga yang tidak pernah diperbarui. Celah kerentanan biasanya bersumber dari:</p>' .
                    '<ol>' .
                    '<li><strong>File Upload yang Tidak Tervalidasi:</strong> Penyerang berhasil mengunggah file PHP backdoor terselubung (Web Shell) melalui formulir kontak atau plugin galeri usang.</li>' .
                    '<li><strong>Database Insecure Direct Object References:</strong> Penyerang menyisipkan ribuan link judol ke dalam tabel postingan database secara diam-diam (seringkali disembunyikan menggunakan CSS <code>display: none</code>).</li>' .
                    '<li><strong>Shared Hosting Tanpa Isolasi Folder Inti:</strong> File konfigurasi database (<code>wp-config.php</code>) diletakkan di root web yang dapat dibaca saat ada eksploit Local File Inclusion (LFI).</li>' .
                    '</ol>' .
                    '<h2>Mengapa Arsitektur Laravel Menjadi Benteng Terbaik?</h2>' .
                    '<p>Di PT Aktama Digital Antika, seluruh sistem web instansi dibangun di atas kerangka kerja modern <strong>Laravel</strong> dengan filosofi <em>Security by Design</em>:</p>' .
                    '<ul>' .
                    '<li><strong>Pemisahan Total Direktori Inti:</strong> Seluruh file logika sistem, konfigurasi environment (<code>.env</code>), dan migrasi database diletakkan di luar direktori <code>public_html</code>. Peretas yang mengakses web browser tidak akan pernah bisa mengeksekusi file inti.</li>' .
                    '<li><strong>Proteksi CSRF & SQL Injection Bawaan:</strong> Setiap interaksi formulir diproteksi token kriptografis otomatis dan PDO Parameter Binding, menutup 99% celah injeksi query manual.</li>' .
                    '<li><strong>Anti-Bloatware Tanpa Plugin Pihak Ketiga:</strong> Modul galeri, berita, dan PPDB dibuat khusus (custom code) yang bersih, ringan, dan terpelihara.</li>' .
                    '</ul>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-success mb-2"><i class="bi bi-shield-check me-2"></i>Audit & Amankan Portal Instansi Anda</h5>' .
                    '<p class="small text-muted mb-3">Jangan tunggu nama baik sekolah atau instansi Anda tercoreng di Google. Tim rekayasa perangkat lunak PT Aktama Digital Antika siap melakukan audit forensik serta migrasi portal ke arsitektur aman anti-malware.</p>' .
                    '<a href="/jasa-website" class="btn btn-sm btn-success rounded-pill px-3">Lihat Solusi Jasa Website & Keamanan</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(2),
                'meta_title' => 'Solusi Menangkal Spam Judol di Web Sekolah & Instansi | Aktama Digital',
                'meta_description' => 'Strategi mengamankan website instansi dan sekolah dari deface serta injeksi malware spam judi online menggunakan arsitektur Laravel.',
            ],
            [
                'slug' => 'seni-meracik-prompt-ai-efisiensi-administrasi-perkantoran',
                'category_id' => $catAi->id,
                'title' => 'Seni Meracik Prompt AI: Rahasia Menyelesaikan Draf Laporan Dinas & Notula Rapat dalam 15 Menit',
                'image' => 'articles/article-prompt-engineering.jpg',
                'summary' => 'Mengapa hasil AI sering terdengar kaku dan tidak sesuai standar kedinasan? Kuncinya ada pada teknik Prompt Engineering. Pelajari formula 4 pilar (Role, Context, Constraint, Format) untuk memangkas waktu kerja administrasi hingga 70%.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Banyak staf kantor dan pegawai dinas mencoba menggunakan ChatGPT untuk membuat surat dinas, namun berakhir kecewa: <em>"Bahasanya terlalu puitis, tidak baku, dan tidak sesuai tata naskah dinas."</em></p>' .
                    '<p>Kelemahan tersebut sebenarnya bukan terletak pada model AI, melainkan pada kualitas perintah yang diinputkan. AI adalah cerminan dari instruksi yang diterimanya (<em>Garbage In, Garbage Out</em>). Inilah mengapa <strong>Prompt Engineering</strong> kini menjadi keterampilan kerja paling dicari di perkantoran modern.</p>' .
                    '<h2>Formula 4 Pilar: Standar Emas Prompt Kedinasan</h2>' .
                    '<p>Untuk menghasilkan draf administratif yang langsung siap pakai tanpa perlu revisi berulang, gunakan kerangka kerja <strong>R-C-C-F</strong>:</p>' .
                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small">' .
                    '<thead class="table-light"><tr><th style="width: 25%;">Pilar</th><th>Penjelasan</th><th>Contoh Instruksi Nyata</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>1. Role (Peran)</strong></td><td>Tetapkan identitas kepakaran AI secara spesifik.</td><td><em>"Bertindaklah sebagai Arsiparis Senior dan Pakar Tata Naskah Dinas Kementerian Pendidikan..."</em></td></tr>' .
                    '<tr><td><strong>2. Context (Konteks)</strong></td><td>Jelaskan latar belakang kegiatan dan audiens target.</td><td><em>"Kami baru saja menyelenggarakan rapat koordinasi implementasi kurikulum vokasi bersama 12 kepala sekolah mitra..."</em></td></tr>' .
                    '<tr><td><strong>3. Constraint (Batasan)</strong></td><td>Tetapkan aturan tegas yang dilarang dan wajib dipatuhi.</td><td><em>"Gunakan bahasa Indonesia baku sesuai EYD V. Jangan gunakan kata-kata berlebihan seperti \'luar biasa\' atau \'fenomenal\'. Maksimal 300 kata."</em></td></tr>' .
                    '<tr><td><strong>4. Format (Bentuk)</strong></td><td>Tentukan struktur luaran yang diinginkan.</td><td><em>"Sajikan dalam bentuk tabel matriks 4 kolom: Nomor, Pokok Bahasan, Kesepakatan/Tindak Lanjut, dan Penanggung Jawab (PIC)."</em></td></tr>' .
                    '</tbody></table></div>' .
                    '<h2>Prinsip Keamanan Informasi & Etika</h2>' .
                    '<p>Hal terpenting yang selalu ditekankan dalam pelatihan LPK Aktama adalah kepatuhan privasi data (UU PDP). Jangan pernah memasukkan NIK pegawai, nomor rekening kas dinas, atau kata sandi sistem ke dalam prompt publik. Gunakan data anonim atau inisial saat menyusun kerangka dokumen.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-lightning-charge-fill me-2"></i>Ikuti Pelatihan Praktik AI Perkantoran</h5>' .
                    '<p class="small text-muted mb-3">Kuasai 50+ pustaka template prompt kedinasan, otomasi spreadsheet cerdas, dan pembuatan slide presentasi kilat melalui program resmi LPK Aktama.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Daftar Pelatihan AI Terapan</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(3),
                'meta_title' => 'Seni Meracik Prompt AI untuk Administrasi Perkantoran | Aktama Digital',
                'meta_description' => 'Panduan prompt engineering 4 pilar untuk mengotomasi penyusunan laporan dinas dan notula rapat secara profesional dan cepat.',
            ],
            [
                'slug' => 'digitalisasi-kasir-dan-stok-menyelamatkan-bisnis-coffee-shop',
                'category_id' => $catBiz->id,
                'title' => 'Stop Catat Manual: Bagaimana Digitalisasi Kasir & Manajemen Stok Menyelamatkan Margin Bisnis Coffee Shop',
                'image' => 'articles/article-coffee-erp.jpg',
                'summary' => 'Ramai pembeli di malam hari belum tentu menghasilkan laba di akhir bulan jika bahan baku bocor dan pencatatan kasir masih manual. Simak strategi integrasi Point of Sale (POS) dan kontrol HPP bahan baku kedai kopi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Kedai kopi Anda selalu penuh meja tiap malam, antrean kasir mengular, dan suara mesin grinder berderu tanpa henti. Namun saat tiba waktu tutup buku akhir bulan, Anda terkejut: <em>"Ke mana perginya semua uang kas?"</em></p>' .
                    '<p>Ini adalah penyakit umum yang menjerat 70% pengusaha coffee shop pemula. Ilusi omzet harian yang terlihat besar sering kali menutupi kebocoran finansial di belakang layar akibat tidak adanya pengawasan inventori bahan baku secara real-time.</p>' .
                    '<h2>Tiga Titik Kebocoran Finansial Terbesar di Kedai Kopi</h2>' .
                    '<ul>' .
                    '<li><strong>Spill Bahan Baku (Biji Kopi & Susu Fresh):</strong> Tanpa kalibrasi dosis gramasi yang dicatat sistem, barista bisa membuang ratusan gram bubuk kopi per shift tanpa disadari.</li>' .
                    '<li><strong>Selisih Kas Manual:</strong> Pembayaran tunai yang tercecer atau struk transaksi yang lupa dimasukkan ke buku besar kasir.</li>' .
                    '<li><strong>Deadstock Sirup & Topping:</strong> Membeli bahan baku musiman dalam jumlah besar yang akhirnya kedaluwarsa sebelum terjual habis.</li>' .
                    '</ul>' .
                    '<h2>Solusi: Otomasi Bill of Materials (BOM)</h2>' .
                    '<p>Dengan sistem kasir cerdas yang terintegrasi ke modul inventori gudang (seperti platform <strong>Aktama Coffee Cloud ERP</strong>), setiap kali kasir menekan tombol <em>"1 Iced Caramel Macchiato"</em>, sistem secara otomatis memotong stok di database:</p>' .
                    '<ul>' .
                    '<li>18 gram Espresso Beans</li>' .
                    '<li>120 ml Fresh Milk</li>' .
                    '<li>20 ml Vanilla Syrup</li>' .
                    '<li>15 ml Caramel Drizzle</li>' .
                    '<li>1 Cup 16oz + Straw + Lid</li>' .
                    '</ul>' .
                    '<p>Di akhir hari kerja, pemilik bisnis cukup mencocokkan stok fisik di meja bar dengan laporan pengurangan otomatis sistem. Jika terjadi selisih mencurigakan, titik kebocoran langsung terlacak seketika.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-dark mb-2"><i class="bi bi-cup-hot-fill me-2"></i>Tingkatkan Efisiensi Bisnis Kopi Anda</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika mengembangkan ekosistem <strong>Aktama Coffee</strong> yang memadukan pasokan biji kopi specialty grade dengan platform manajemen operasional kedai kopi terintegrasi.</p>' .
                    '<a href="/kopi" class="btn btn-sm btn-dark rounded-pill px-3">Pelajari Solusi Aktama Coffee</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(5),
                'meta_title' => 'Digitalisasi Kasir & Manajemen Stok Kedai Kopi | Aktama Digital',
                'meta_description' => 'Strategi menghentikan kebocoran bahan baku dan mengoptimalkan margin laba coffee shop melalui sistem POS dan inventory modern.',
            ],
            [
                'slug' => 'revolusi-undangan-digital-hemat-biaya-mewah-elegan',
                'category_id' => $catBiz->id,
                'title' => 'Revolusi Undangan Digital: Hemat Biaya Cetak Hingga 80% Tanpa Kehilangan Kesan Sakral dan Mewah',
                'image' => 'articles/article-undangan-digital.jpg',
                'summary' => 'Mencetak ratusan fisik kartu undangan tidak hanya menguras anggaran pernikahan, namun sering terbuang sia-sia. Undangan digital berbasis web interaktif menghadirkan pengalaman visual sinematik dengan fitur RSVP dan navigasi presisi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Biaya percetakan undangan fisik untuk 500 orang tamu rata-rata menghabiskan Rp3.500.000 hingga Rp7.000.000. Mirisnya, setelah acara selesai, hampir 95% dari kartu kertas tersebut berakhir di tempat sampah.</p>' .
                    '<p>Kini, pasangan calon mempelai modern dan vendor Wedding Organizer (WO) beralih ke <strong>Undangan Pernikahan Digital Berbasis Website</strong>. Bukan sekadar gambar JPG atau video biasa, melainkan portal web interaktif yang dapat dibuka mulus di semua jenis smartphone tanpa perlu mengunduh aplikasi tambahan.</p>' .
                    '<h2>Fitur Unggulan yang Mustahil Dimiliki Undangan Kertas</h2>' .
                    '<ul>' .
                    '<li><strong>Personalisasi Nama Tamu Tanpa Batas:</strong> Kirim undangan dengan sapaan khusus (<em>"Kepada Yth. Bapak Bambang & Keluarga"</em>) hanya dengan membagikan tautan unik melalui WhatsApp.</li>' .
                    '<li><strong>Integrasi Google Maps Real-Time:</strong> Tamu undangan tidak akan tersesat karena tombol navigasi langsung membuka rute GPS ke gedung atau lokasi acara.</li>' .
                    '<li><strong>Konfirmasi Kehadiran (RSVP) Otomatis:</strong> Calon pengantin dapat mengetahui pasti berapa jumlah porsi katering yang harus dipesan, mencegah pemborosan makanan.</li>' .
                    '<li><strong>Amplop Digital & QRIS Terintegrasi:</strong> Memfasilitasi tamu yang berhalangan hadir agar tetap bisa mengirimkan hadiah dan doa restu secara langsung ke rekening mempelai.</li>' .
                    '<li><strong>Galeri Sinematik & Musik Latar:</strong> Menghadirkan video pre-wedding dan alunan lagu romantis pilihan kedua mempelai.</li>' .
                    '</ul>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-danger mb-2"><i class="bi bi-heart-fill me-2"></i>Jelajahi Koleksi Tema Undangan Online Aktama</h5>' .
                    '<p class="small text-muted mb-3">Platform <strong>undangan.aktama.com</strong> hadir dengan puluhan tema adat tradisional nusantara, gaya modern floral minimalis, dan teknologi loading ultra cepat.</p>' .
                    '<a href="https://undangan.aktama.com" target="_blank" class="btn btn-sm btn-danger rounded-pill px-3">Lihat Katalog & Demo ↗</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(7),
                'meta_title' => 'Revolusi Undangan Digital Mewah dan Hemat | Aktama Digital',
                'meta_description' => 'Solusi undangan pernikahan website interaktif dengan RSVP otomatis, amplop digital, dan Google Maps presisi hemat biaya cetak.',
            ],
            [
                'slug' => 'mengapa-berpikir-komputasional-harus-dikenalkan-sejak-dini',
                'category_id' => $catEdu->id,
                'title' => 'Mengapa Berpikir Komputasional dan Koding Harus Dikenalkan Sejak Jenjang Sekolah Menengah?',
                'image' => 'articles/article-coding-education.jpg',
                'summary' => 'Koding bukan sekadar menghafal sintaks bahasa pemrograman, melainkan melatih nalar dekomposisi, pengenalan pola, dan abstraksi logis dalam memecahkan masalah kompleks kehidupan nyata.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Ketika mendengar kata "koding", sebagian besar orang tua dan guru masih membayangkan barisan teks rumit berwarna hijau berlatar hitam yang hanya dipahami oleh insinyur perangkat lunak lulusan universitas.</p>' .
                    '<p>Paradigma ini sudah kuno. Dalam literasi pendidikan abad ke-21, pembelajaran koding dan <strong>Computational Thinking (Berpikir Komputasional)</strong> diposisikan setara dengan kemampuan membaca dan berhitung dasar. Tujuannya bukan semata mencetak semua siswa menjadi programmer, melainkan membekali mereka dengan kerangka berpikir sistematis.</p>' .
                    '<h2>Empat Fondasi Berpikir Komputasional</h2>' .
                    '<ol>' .
                    '<li><strong>Dekomposisi:</strong> Kemampuan memecah masalah besar yang menakutkan menjadi sub-bagian kecil yang terkelola dengan mudah.</li>' .
                    '<li><strong>Pengenalan Pola (Pattern Recognition):</strong> Menemukan kemiripan atau tren dari masalah masa lalu untuk mempercepat solusi saat ini.</li>' .
                    '<li><strong>Abstraksi:</strong> Memilah informasi penting dan mengabaikan detail yang tidak relevan agar fokus pada inti persoalan.</li>' .
                    '<li><strong>Perancangan Algoritma:</strong> Menyusun langkah-langkah terurut dan logis untuk menyelesaikan tugas secara konsisten.</li>' .
                    '</ol>' .
                    '<h2>Pengalaman Fasilitasi Nasional KKA Kemdikdasmen</h2>' .
                    '<p>Sebagai Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen, <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong> menyaksikan langsung bagaimana siswa yang terbiasa memecahkan teka-teki logika pemrograman memiliki daya tahan mental (grit) dan kreativitas yang jauh lebih tinggi ketika menghadapi pelajaran eksakta lainnya.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-code-slash me-2"></i>Buka Kelas Koding & AI di Sekolah Anda</h5>' .
                    '<p class="small text-muted mb-3">LPK Aktama siap bermitra dengan SMP, SMA, dan SMK di seluruh Indonesia untuk penyusunan silabus ekstrakurikuler koding, pelatihan guru pendamping, dan sertifikasi siswa.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Pelajari Program Kemitraan Sekolah</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(9),
                'meta_title' => 'Mengapa Berpikir Komputasional Harus Dikenalkan Sejak Dini | Aktama Digital',
                'meta_description' => 'Membangun logika terstruktur dan daya cipta generasi muda melalui pengenalan computational thinking dan pemrograman sejak jenjang sekolah.',
            ],
            [
                'slug' => 'website-custom-vs-template-murahan-biaya-dan-performa',
                'category_id' => $catWeb->id,
                'title' => 'Memilih Website untuk Bisnis: Mengapa Template Murahan Seringkali Berakhir dengan Biaya yang Jauh Lebih Mahal',
                'image' => 'articles/article-web-architecture.jpg',
                'summary' => 'Tergiur jasa bikin website instan seharga ratusan ribu? Pelajari risiko tersembunyi seperti lambatnya loading, keterbatasan integrasi database, dan celah keamanan yang justru melipatgandakan biaya perawatan di masa depan.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Iklan di media sosial kerap menawarkan janji menggiurkan: <em>"Jasa Bikin Website Perusahaan Hanya Rp300.000, Jadi dalam 2 Jam!"</em>. Bagi pemilik bisnis yang ingin berhemat, tawaran ini tentu terdengar sangat manis.</p>' .
                    '<p>Namun, apa yang sebenarnya terjadi 3 hingga 6 bulan kemudian? Ratusan klien yang akhirnya datang ke PT Aktama menceritakan pengalaman pahit yang seragam: website sering <em>down</em>, form kontak tidak pernah mengirim notifikasi, tampilan di handphone berantakan, dan ketika ingin menambah fitur pembayaran, pengembang lamanya menghilang tanpa kabar.</p>' .
                    '<h2>Biaya Tak Terlihat dari Website Template Murahan</h2>' .
                    '<ul>' .
                    '<li><strong>Kecepatan Halaman yang Sangat Buruk (PageSpeed Drop):</strong> Template murah biasanya memuat puluhan skrip JavaScript dan CSS yang tidak terpakai (bloated code), membuat waktu tunggu loading mencapai 8–12 detik. Calon pelanggan keburu menutup tab sebelum halaman sempat terbuka.</li>' .
                    '<li><strong>Hukuman Ranking Google:</strong> Algoritma Google Core Web Vitals memprioritaskan situs yang ringan dan cepat. Website yang lambat otomatis terlempar ke halaman 4 ke bawah.</li>' .
                    '<li><strong>Kerentanan Terhadap Peretasan:</strong> Plugin bajakan (nulled) yang diselipkan pembuat web murah sering kali membawa script tersembunyi yang sewaktu-waktu menginjeksi malware.</li>' .
                    '<li><strong>Ketiadaan Hak Milik Kode (Vendor Lock-in):</strong> Anda tidak diberikan akses penuh ke database dan source code, sehingga jika ingin pindah server, Anda dipaksa membayar biaya tebusan mahal.</li>' .
                    '</ul>' .
                    '<h2>Mengapa Website Custom Laravel Adalah Investasi Jangka Panjang?</h2>' .
                    '<p>Website yang dibangun khusus dengan framework modern memiliki kode yang 100% bersih, hanya memuat apa yang dibutuhkan bisnis Anda, serta siap diskalakan hingga jutaan pengunjung tanpa perlu dibongkar dari nol.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-success mb-2"><i class="bi bi-laptop me-2"></i>Konsultasikan Kebutuhan Web Bisnis Anda</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika merancang arsitektur website dan aplikasi bisnis berkinerja tinggi, bergaransi bebas injeksi judol, dan dirancang khusus untuk mendongkrak penjualan Anda.</p>' .
                    '<a href="/jasa-website" class="btn btn-sm btn-success rounded-pill px-3">Lihat Paket Jasa Website Profesional</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(12),
                'meta_title' => 'Website Custom vs Template Murahan untuk Bisnis | Aktama Digital',
                'meta_description' => 'Perbandingan mendalam risiko template web instan murah vs keunggulan arsitektur custom Laravel untuk aset digital jangka panjang perusahaan.',
            ],
            [
                'slug' => 'peluang-bisnis-micro-saas-dan-lisensi-source-code',
                'category_id' => $catBiz->id,
                'title' => 'Peluang Bisnis Micro-SaaS dan Lisensi Source Code: Cara Developer Menghasilkan Omzet Berkelanjutan',
                'image' => 'articles/article-digital-products.jpg',
                'summary' => 'Berhenti menukar waktu dengan uang secara linier. Membangun modul perangkat lunak siap pakai, template aplikasi Laravel, dan lisensi produk digital membuka pintu pendapatan pasif skala nasional bagi talenta digital.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Banyak programmer dan pengembang web berbakat terjebak dalam siklus kelelahan freelance (<em>freelance burnout</em>). Mereka mengerjakan proyek klien siang dan malam, namun ketika proyek selesai, penghasilan pun seketika berhenti.</p>' .
                    '<p>Model bisnis perangkat lunak telah berevolusi. Alih-alih mengerjakan satu proyek pesanan untuk satu klien, pengembang kini beralih membangun <strong>Micro-SaaS</strong> dan menjual <strong>Lisensi Source Code Digital</strong> yang dapat dibeli oleh ratusan pengguna berulang kali tanpa batas fisik logistik.</p>' .
                    '<h2>Mengapa Produk Digital Sangat Menjanjikan di Indonesia?</h2>' .
                    '<ol>' .
                    '<li><strong>Margin Keuntungan Hampir 100%:</strong> Biaya replikasi sebuah file ZIP atau kode aplikasi adalah Rp0. Begitu sistem selesai dibangun, setiap penjualan berikutnya adalah keuntungan murni.</li>' .
                    '<li><strong>Otomasi Transaksi Tanpa Intervensi Manual:</strong> Integrasi dengan payment gateway lokal memungkinkan pembeli melakukan transfer bank atau QRIS, dan sistem otomatis menerbitkan lisensi serta link download secara instan 24 jam sehari.</li>' .
                    '<li><strong>Kebutuhan UMKM & Agensi yang Sangat Tinggi:</strong> Banyak agensi kecil membutuhkan starter kit siap pakai (misal: sistem e-commerce, sistem kasir, aplikasi PPDB sekolah) untuk mempercepat waktu delivery proyek mereka.</li>' .
                    '</ol>' .
                    '<h2>Pilar Utama Membangun Toko Produk Digital yang Sukses</h2>' .
                    '<p>Kunci sukses menjual aset digital adalah perlindungan hak cipta (kode lisensi unik), dokumentasi instalasi yang sangat jelas, dan ketersediaan pembaruan (update) berkala. Hal inilah yang terus dikembangkan oleh ekosistem digital Aktama.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-dark mb-2"><i class="bi bi-box-seam me-2"></i>Eksplorasi Ekosistem Digital Assets</h5>' .
                    '<p class="small text-muted mb-3">Temukan berbagai source code pilihan, modul Laravel enterprise, dan produk digital berlisensi resmi yang dirancang oleh tim developer PT Aktama Digital Antika.</p>' .
                    '<a href="/portofolio" class="btn btn-sm btn-dark rounded-pill px-3">Lihat Portofolio Produk & Solusi</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(15),
                'meta_title' => 'Peluang Bisnis Micro-SaaS dan Lisensi Source Code | Aktama Digital',
                'meta_description' => 'Strategi monetisasi produk digital, lisensi source code web aplikasi, dan micro-SaaS bagi developer dan pelaku usaha teknologi di Indonesia.',
            ],
            [
                'slug' => 'nilai-strategis-sertifikat-pelatihan-resmi-lpk-dalam-karier',
                'category_id' => $catEdu->id,
                'title' => 'Nilai Strategis Sertifikat Pelatihan Resmi Berlisensi NIB & LPK dalam Portofolio Karier Profesional',
                'image' => 'articles/article-lpk-certification.jpg',
                'summary' => 'Di tengah banjirnya sertifikat webinar gratis, dokumen kelulusan resmi dari Lembaga Pelatihan Kerja (LPK) berbadan hukum memiliki kekuatan pembuktian hukum dan kompetensi yang diakui instansi pemerintah dan industri.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Berapa banyak sertifikat pelatihan PDF yang saat ini tersimpan di memori laptop Anda? Di era pasca-pandemi, jutaan orang memiliki puluhan sertifikat seminar daring gratisan berdurasi 1–2 jam.</p>' .
                    '<p>Namun saat dokumen tersebut diajukan untuk kenaikan pangkat pegawai negeri (PNS/PPPK), usulan angka kredit jabatan fungsional guru/dosen, atau seleksi lamaran kerja di korporasi multinasional, sertifikat tersebut kerap <strong>ditolak atau tidak dihitung</strong>. Mengapa?</p>' .
                    '<h2>Beda Mendasar: Sertifikat Webinar vs Sertifikat Kompetensi LPK</h2>' .
                    '<p>Tim penilai instansi dan praktisi HRD sangat cermat dalam membedakan sertifikat partisipasi biasa dengan sertifikat pelatihan kerja resmi:</p>' .
                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small">' .
                    '<thead class="table-light"><tr><th>Indikator</th><th>Sertifikat Seminar Biasa</th><th>Sertifikat LPK Resmi (PT Aktama Digital)</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Legalitas Penyelenggara</strong></td><td>Komunitas / Panitia Lepas tanpa izin resmi</td><td>Lembaga Pelatihan Kerja (LPK) Berbadan Hukum PT & NIB: 1703250057018</td></tr>' .
                    '<tr><td><strong>Struktur Jam Pelajaran (JP)</strong></td><td>Tidak tercantum / Hanya 2 jam</td><td>Memuat matriks materi dengan bobot jam pelatihan standar (32 JP, 64 JP, dst.)</td></tr>' .
                    '<tr><td><strong>Uji Kompetensi & Portofolio</strong></td><td>Cukup isi form presensi tanpa tugas</td><td>Wajib menyelesaikan tugas proyek nyata yang dievaluasi instruktur berkompeten</td></tr>' .
                    '<tr><td><strong>Verifikasi Keaslian</strong></td><td>File gambar tanpa pengaman</td><td>Dilengkapi Nomor Registrasi Unik & QR Code verifikasi online anti-pemalsuan</td></tr>' .
                    '</tbody></table></div>' .
                    '<h2>Menjadikan Sertifikat Sebagai Pembeda Karier Anda</h2>' .
                    '<p>Investasi waktu dalam program bimbingan teknis terstruktur bukan hanya memberi Anda wawasan praktis terkini, melainkan juga perlindungan administratif atas pengakuan keahlian Anda di hadapan hukum dan regulator ketenagakerjaan.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-award-fill me-2"></i>Raih Sertifikasi Kompetensi Resmi</h5>' .
                    '<p class="small text-muted mb-3">Tingkatkan kualifikasi portofolio Anda bersama LPK PT Aktama Digital Antika. Jadwal kelas terbuka untuk individu dan rombongan instansi.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Lihat Jadwal Batch Terdekat</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(18),
                'meta_title' => 'Nilai Strategis Sertifikat LPK Resmi untuk Karier | Aktama Digital',
                'meta_description' => 'Mengapa sertifikat pelatihan kerja resmi berizin LPK dan NIB memiliki bobot hukum tinggi untuk angka kredit pegawai dan seleksi karier industri.',
            ],
            [
                'slug' => 'dari-ruang-riset-ke-industri-integrasi-penelitian-akademik',
                'category_id' => $catRes->id,
                'title' => 'Dari Ruang Riset ke Industri: Mengintegrasikan Penelitian Akademik dengan Solusi Nyata Masyarakat',
                'image' => 'articles/article-academic-research.jpg',
                'summary' => 'Menjembatani jurang pemisah antara paper ilmiah di kampus dan kebutuhan teknologi di lapangan. Bagaimana riset komputasi terindeks SINTA ditransformasikan menjadi produk perangkat lunak bernilai ekonomi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Salah satu kritik terbesar terhadap dunia pendidikan tinggi di negara berkembang adalah fenomena "Menara Gading" (<em>Ivory Tower</em>): para akademisi getol mempublikasikan ratusan makalah ilmiah, namun hasil penelitian tersebut hanya berakhir di arsip perpustakaan tanpa pernah dirasakan manfaatnya oleh pelaku usaha dan masyarakat luas.</p>' .
                    '<p>PT Aktama Digital Antika lahir dari cita-cita luhur untuk meruntuhkan tembok pemisah tersebut. Kami meyakini bahwa riset komputasi dan kecerdasan buatan terbaik adalah riset yang mampu memecahkan persoalan riil di tengah masyarakat.</p>' .
                    '<h2>Model Kolaborasi Quadruple Helix</h2>' .
                    '<p>Untuk menciptakan inovasi yang berkelanjutan, riset terapan harus melibatkan 4 pilar secara simultan:</p>' .
                    '<ol>' .
                    '<li><strong>Akademisi (Kampus):</strong> Menyediakan metodologi ilmiah yang ketat, kajian literatur mendalam, dan eksperimen algoritma teruji.</li>' .
                    '<li><strong>Industri (Perusahaan):</strong> Menguji skalabilitas teknologi, efisiensi komputasi, dan kelayakan model bisnis (feasibility).</li>' .
                    '<li><strong>Pemerintah (Regulator):</strong> Menyelaraskan inovasi dengan arah kebijakan nasional dan perlindungan hak cipta (HAKI).</li>' .
                    '<li><strong>Masyarakat & UMKM:</strong> Menjadi pengguna akhir (end-user) yang memberikan umpan balik langsung atas kegunaan produk.</li>' .
                    '</ol>' .
                    '<h2>Rekam Jejak Publikasi Terindeks SINTA</h2>' .
                    '<p>Pendiri PT Aktama Digital Antika, <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong> (Kaprodi Sistem Komputer Universitas Parna Raya), secara konsisten mempublikasikan karya ilmiah di jurnal nasional terakreditasi <strong>SINTA 4 dan SINTA 5</strong> dalam bidang sistem tertanam (IoT), pemrosesan data, dan media pembelajaran komputasional. Setiap baris kode yang dikembangkan di Aktama dilandasi oleh kajian teoritis yang kokoh dan dapat dipertanggungjawabkan secara akademik.</p>' .
                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-info mb-2"><i class="bi bi-journal-bookmark-fill me-2"></i>Jelajahi Profil Peneliti & Publikasi SINTA</h5>' .
                    '<p class="small text-muted mb-3">Ingin melihat daftar lengkap jurnal ilmiah, rekam jejak pengajaran, dan kolaborasi riset? Kunjungi portal akademik resmi Founder.</p>' .
                    '<a href="https://profil.aktama.com" target="_blank" class="btn btn-sm btn-info text-white rounded-pill px-3">Buka profil.aktama.com ↗</a>' .
                    '</div>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now()->subDays(21),
                'meta_title' => 'Integrasi Riset SINTA dan Industri Teknologi | Aktama Digital',
                'meta_description' => 'Bagaimana PT Aktama Digital mentransformasikan riset komputasi dan publikasi ilmiah SINTA menjadi aplikasi nyata berdaya saing tinggi.',
            ],
        ];

        foreach ($articles as $artData) {
            Article::updateOrCreate(['slug' => $artData['slug']], $artData);
        }

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
                'section_key' => 'jasa_website',
                'name' => 'Jasa Pembuatan Website & Aplikasi',
                'badge' => 'Software House & Rekayasa Web',
                'title' => 'Jasa Pembuatan Website & Sistem Informasi Bebas Celah Malware',
                'subtitle' => 'Didesain dengan arsitektur modern berstandar enterprise yang kebal dari risiko injeksi script judi online, cepat, mobile-friendly, dan teroptimasi SEO.',
                'sort_order' => 2,
                'is_active' => true,
            ],
            [
                'section_key' => 'pelatihan_ai',
                'name' => 'Pelatihan AI & Koding (LPK Terdaftar)',
                'badge' => 'Pusat Pelatihan AI & Teknologi',
                'title' => 'Program Pelatihan Kecerdasan Artifisial (AI) & Koding Praktis',
                'subtitle' => 'Disusun langsung oleh Fasilitator Nasional KKA Kemdikdasmen berlisensi LPK resmi untuk mendongkrak produktivitas instansi pemerintah, sekolah, dan pelaku usaha.',
                'sort_order' => 3,
                'is_active' => true,
            ],
            [
                'section_key' => 'ekosistem_digital',
                'name' => 'Ekosistem Produk & Layanan Terpadu',
                'badge' => 'Ekosistem Bisnis Aktama',
                'title' => 'Ekosistem Produk Digital & Unit Bisnis Terpadu',
                'subtitle' => 'Jelajahi lini produk perangkat lunak unggulan, platform pembelajaran daring, dan unit komoditas riil yang dikembangkan dan dikelola oleh PT Aktama Digital Antika.',
                'sort_order' => 4,
                'is_active' => true,
            ],
            [
                'section_key' => 'portofolio',
                'name' => 'Portofolio Proyek Terverifikasi',
                'badge' => 'Bukti Kinerja Nyata',
                'title' => 'Portofolio Implementasi Sistem & Rekayasa Digital',
                'subtitle' => 'Jejak karya sistem informasi, aplikasi kasir operasional, dan portal web yang telah sukses diimplementasikan dan digunakan secara riil.',
                'sort_order' => 5,
                'is_active' => true,
            ],
            [
                'section_key' => 'tentang_kami',
                'name' => 'Profil Pimpinan & Legalitas Perusahaan',
                'badge' => 'Integritas & Kepemimpinan',
                'title' => 'Integritas Legalitas & Kepemimpinan Berbasis Kompetensi Akademik',
                'subtitle' => 'Didirikan dengan landasan kepatuhan hukum yang solid serta dipimpin oleh praktisi sekaligus akademisi yang berkomitmen pada transfer teknologi nyata.',
                'sort_order' => 6,
                'is_active' => true,
            ],
            [
                'section_key' => 'artikel',
                'name' => 'Artikel & Wawasan Teknologi',
                'badge' => 'Wawasan & Literasi Digital',
                'title' => 'Wawasan Terkini Seputar AI, Keamanan Web, & Bisnis Digital',
                'subtitle' => 'Artikel edukatif dan panduan praktis untuk membantu Anda memahami perkembangan lanskap teknologi terkini secara bijak.',
                'sort_order' => 7,
                'is_active' => true,
            ],
            [
                'section_key' => 'form_konsultasi',
                'name' => 'Formulir Konsultasi & Permintaan Penawaran',
                'badge' => 'Mulai Kolaborasi',
                'title' => 'Konsultasikan Kebutuhan Teknologi atau Pelatihan Anda',
                'subtitle' => 'Isi formulir ringkas di bawah ini atau hubungi saluran resmi kami. Tim teknis Aktama Digital siap menganalisis kebutuhan Anda dan memberikan solusi terbaik.',
                'sort_order' => 8,
                'is_active' => true,
            ],
        ];

        foreach ($homeSections as $sec) {
            HomeSection::updateOrCreate(['section_key' => $sec['section_key']], $sec);
        }

        // 9. Halaman Kustom Default (CMS Pages)
        Page::updateOrCreate(
            ['slug' => 'kebijakan-privasi'],
            [
                'title' => 'Kebijakan Privasi',
                'editor_type' => 'standard',
                'content_html' => '<div class="py-4"><h3>Kebijakan Privasi PT Aktama Digital Antika</h3><p>PT Aktama Digital Antika berkomitmen untuk melindungi dan menghormati hak privasi setiap pengguna, klien, dan peserta pelatihan kami.</p><h4>1. Pengumpulan Informasi</h4><p>Kami hanya mengumpulkan informasi yang Anda berikan secara sukarela melalui formulir konsultasi, pendaftaran pelatihan, atau pemesanan layanan, seperti nama, nomor kontak, dan alamat email.</p><h4>2. Penggunaan Informasi</h4><p>Informasi yang terkumpul digunakan semata-mata untuk memproses permintaan penawaran, mengoordinasikan pelaksanaan pelatihan, serta memberikan layanan purna jual terbaik tanpa membagikannya kepada pihak ketiga tanpa izin Anda.</p></div>',
                'meta_title' => 'Kebijakan Privasi | PT Aktama Digital Antika',
                'meta_description' => 'Kebijakan privasi resmi PT Aktama Digital Antika mengenai perlindungan data pengguna dan klien.',
                'is_published' => true,
                'sort_order' => 1,
            ]
        );

        Page::updateOrCreate(
            ['slug' => 'syarat-ketentuan'],
            [
                'title' => 'Syarat & Ketentuan Layanan',
                'editor_type' => 'standard',
                'content_html' => '<div class="py-4"><h3>Syarat & Ketentuan Layanan PT Aktama Digital Antika</h3><p>Dengan menggunakan layanan dan platform PT Aktama Digital Antika, Anda menyetujui ketentuan-ketentuan berikut:</p><h4>1. Ruang Lingkup Layanan</h4><p>Seluruh jasa rekayasa perangkat lunak, pelatihan AI, serta produk yang kami sediakan disesuaikan dengan Surat Perjanjian Kerja (SPK) atau Kerangka Acuan Kerja (KAK) yang disepakati.</p><h4>2. Hak Kekayaan Intelektual</h4><p>Kode sumber aplikasi yang diserahterimakan menjadi milik klien sesuai klausul kontrak, dengan jaminan bahwa infrastruktur yang kami bangun bebas dari celah injeksi kode berbahaya.</p></div>',
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
