<?php

namespace Database\Seeders;

use App\Models\Article;
use App\Models\Category;
use App\Models\CoffeeProduct;
use App\Models\CoffeeProductVariant;
use App\Models\Course;
use App\Models\HomeSection;
use App\Models\InvitationPackage;
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
            'coffee_brand_name' => ['Kopi Distro Premium', 'coffee', 'Nama Brand Kopi'],
            'coffee_tagline' => ['Roastery & Distribusi Biji/Bubuk Kopi Asli Nusantara untuk Retail dan Suplai Kafe', 'coffee', 'Tagline Bisnis Kopi'],
            'academy_url' => ['http://localhost:8080/aktama/public', 'gateway', 'URL Gateway Aktama Academy'],
            'invitation_url' => ['http://localhost:8080/undanganonline/public', 'gateway', 'URL Gateway Undangan Online'],
            'coffee_app_url' => ['http://localhost:8080/kopi/public', 'gateway', 'URL Gateway ERP Kopi'],
            'whatsapp_number' => ['6281234567890', 'contact', 'Nomor WhatsApp Resmi Bisnis'],
            'email' => ['kontak@aktama.com', 'contact', 'Email Resmi Perusahaan'],
            'address' => ['Indonesia', 'contact', 'Alamat Domisili Perusahaan'],
            'meta_default_title' => ['PT Aktama Digital Antika | Solusi Teknologi, Pelatihan AI & Ekosistem Bisnis', 'seo', 'Default Meta Title'],
            'meta_default_description' => ['PT Aktama Digital Antika (NIB 1703250057018) — Penyedia Pelatihan AI Terapan, Jasa Website & POS Bebas Malware, Undangan Online, dan Distribusi Kopi Nusantara.', 'seo', 'Default Meta Description'],
            'logo_path' => ['images/logo-aktama.png', 'media', 'Path Logo Utama Navbar'],
            'seal_path' => ['images/logo-seal-aktama.png', 'media', 'Path Cap Resmi Perusahaan'],
            'favicon_path' => ['images/logo-aktama.png', 'media', 'Path Favicon Tab Browser'],
            'topbar_text' => ['PT Aktama Digital Antika', 'header', 'Teks Entitas di Topbar'],
            'topbar_highlight' => ['NIB: 1703250057018 | LPK Resmi Terdaftar', 'header', 'Badge Legalitas di Topbar'],
            'footer_description' => ['Perusahaan penyedia solusi teknologi terpadu: Pelatihan Kecerdasan Artifisial (AI), Jasa Pembuatan Website & Aplikasi Bisnis, Ekosistem Edukasi Digital, Undangan Online, serta Distribusi Komoditas Kopi Riil.', 'footer', 'Deskripsi Perusahaan di Footer'],
            'footer_copyright' => ['© ' . date('Y') . ' PT Aktama Digital Antika. Seluruh hak cipta dilindungi.', 'footer', 'Teks Copyright Footer'],
            'header_navigation_menu' => [json_encode([
                ['label' => 'Beranda', 'url' => '/', 'target' => '_self'],
                ['label' => 'Tentang Kami', 'url' => '/tentang-kami', 'target' => '_self'],
                ['label' => 'Pelatihan AI', 'url' => '/pelatihan-ai', 'target' => '_self'],
                ['label' => 'Jasa Website', 'url' => '/jasa-website', 'target' => '_self'],
                ['label' => 'Kopi', 'url' => '/kopi', 'target' => '_self'],
                ['label' => 'Undangan', 'url' => '/undangan', 'target' => '_self'],
                ['label' => 'Portofolio', 'url' => '/portofolio', 'target' => '_self'],
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
                'excerpt' => 'Membangun kehadiran profesional perusahaan dengan desain elegan, cepat, dan terproteksi dari malware.',
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
                    'Arsitektur Monolit Modern Bersih & Skalabel',
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

        // 5. Katalog Produk Kopi Asli (Sesuai Database Proyek Riil Kopi Distro)
        // A. Arabika Aceh Gayo
        $gayo = CoffeeProduct::updateOrCreate(
            ['slug' => 'kopi-arabika-aceh-gayo'],
            [
                'name' => 'Kopi Arabika Aceh Gayo',
                'sku' => 'SKU-AG-ORIGIN',
                'description' => 'Kopi Arabika dataran tinggi Gayo Aceh dengan karakter keasaman segar yang seimbang, berpadu aroma rempah halus dan sentuhan rasa cokelat karamel khas pegunungan.',
                'origin' => 'Dataran Tinggi Gayo, Aceh Tengah',
                'roast_level' => 'Medium Roast',
                'image' => 'coffee/gayo.jpg',
                'is_published' => true,
            ]
        );

        $gayoVariants = [
            ['name' => 'Arabika Aceh Gayo 100g (Biji/Bubuk)', 'weight' => 100, 'retail' => 40000, 'wholesale' => 35000, 'min' => 10],
            ['name' => 'Arabika Aceh Gayo 250g (Biji/Bubuk)', 'weight' => 250, 'retail' => 90000, 'wholesale' => 78000, 'min' => 5],
            ['name' => 'Arabika Aceh Gayo 500g (Biji/Bubuk)', 'weight' => 500, 'retail' => 170000, 'wholesale' => 148000, 'min' => 5],
            ['name' => 'Arabika Aceh Gayo 1kg Pasokan Kafe', 'weight' => 1000, 'retail' => 310000, 'wholesale' => 275000, 'min' => 3],
        ];
        foreach ($gayoVariants as $v) {
            CoffeeProductVariant::updateOrCreate(
                ['coffee_product_id' => $gayo->id, 'variant_name' => $v['name']],
                ['weight_grams' => $v['weight'], 'retail_price' => $v['retail'], 'wholesale_price' => $v['wholesale'], 'min_wholesale_qty' => $v['min'], 'is_active' => true]
            );
        }

        // B. Arabika Toraja Sapan
        $toraja = CoffeeProduct::updateOrCreate(
            ['slug' => 'kopi-arabika-toraja-sapan'],
            [
                'name' => 'Kopi Arabika Toraja Sapan',
                'sku' => 'SKU-AT-SAPAN',
                'description' => 'Kopi Arabika legendaris khas Toraja Sapan Sulawesi dengan body yang mantap, aftertaste manis yang tahan lama, serta sentuhan herbal rempah khas.',
                'origin' => 'Sapan, Toraja Utara, Sulawesi Selatan',
                'roast_level' => 'Medium to Dark',
                'image' => 'coffee/toraja.jpg',
                'is_published' => true,
            ]
        );

        $torajaVariants = [
            ['name' => 'Arabika Toraja Sapan 250g (Biji/Bubuk)', 'weight' => 250, 'retail' => 95000, 'wholesale' => 82000, 'min' => 5],
            ['name' => 'Arabika Toraja Sapan 500g (Biji/Bubuk)', 'weight' => 500, 'retail' => 180000, 'wholesale' => 155000, 'min' => 5],
            ['name' => 'Arabika Toraja Sapan 1kg Pasokan Kafe', 'weight' => 1000, 'retail' => 330000, 'wholesale' => 290000, 'min' => 3],
        ];
        foreach ($torajaVariants as $v) {
            CoffeeProductVariant::updateOrCreate(
                ['coffee_product_id' => $toraja->id, 'variant_name' => $v['name']],
                ['weight_grams' => $v['weight'], 'retail_price' => $v['retail'], 'wholesale_price' => $v['wholesale'], 'min_wholesale_qty' => $v['min'], 'is_active' => true]
            );
        }

        // C. Arabika Flores Bajawa Honey
        $flores = CoffeeProduct::updateOrCreate(
            ['slug' => 'kopi-arabika-flores-bajawa-honey'],
            [
                'name' => 'Kopi Arabika Flores Bajawa Honey',
                'sku' => 'SKU-FB-HONEY',
                'description' => 'Kopi Arabika proses honey alami dari dataran tinggi Bajawa Flores. Memiliki aroma floral semerbak, rasa manis madu alami yang lembut, dan keasaman bersih.',
                'origin' => 'Bajawa, Ngada, Nusa Tenggara Timur',
                'roast_level' => 'Medium Roast',
                'image' => 'coffee/flores.jpg',
                'is_published' => true,
            ]
        );

        $floresVariants = [
            ['name' => 'Arabika Flores Bajawa 250g', 'weight' => 250, 'retail' => 92000, 'wholesale' => 80000, 'min' => 5],
            ['name' => 'Arabika Flores Bajawa 500g', 'weight' => 500, 'retail' => 175000, 'wholesale' => 150000, 'min' => 5],
            ['name' => 'Arabika Flores Bajawa 1kg Pasokan Kafe', 'weight' => 1000, 'retail' => 320000, 'wholesale' => 280000, 'min' => 3],
        ];
        foreach ($floresVariants as $v) {
            CoffeeProductVariant::updateOrCreate(
                ['coffee_product_id' => $flores->id, 'variant_name' => $v['name']],
                ['weight_grams' => $v['weight'], 'retail_price' => $v['retail'], 'wholesale_price' => $v['wholesale'], 'min_wholesale_qty' => $v['min'], 'is_active' => true]
            );
        }

        // D. Robusta Lampung Gold
        $lampung = CoffeeProduct::updateOrCreate(
            ['slug' => 'kopi-robusta-lampung-gold'],
            [
                'name' => 'Kopi Robusta Lampung Gold',
                'sku' => 'SKU-RL-GOLD',
                'description' => 'Robusta pilihan petani Lampung dengan crema melimpah, kepahitan pekat yang mantap (bold), dan aroma dark chocolate yang sangat cocok untuk kopi susu kekinian.',
                'origin' => 'Lampung Barat, Sumatera',
                'roast_level' => 'Dark Roast',
                'image' => 'coffee/temanggung.jpg',
                'is_published' => true,
            ]
        );

        $lampungVariants = [
            ['name' => 'Robusta Lampung Gold 250g', 'weight' => 250, 'retail' => 48000, 'wholesale' => 38000, 'min' => 5],
            ['name' => 'Robusta Lampung Gold 500g', 'weight' => 500, 'retail' => 88000, 'wholesale' => 72000, 'min' => 5],
            ['name' => 'Robusta Lampung Gold 1kg Pasokan Kafe', 'weight' => 1000, 'retail' => 160000, 'wholesale' => 130000, 'min' => 3],
        ];
        foreach ($lampungVariants as $v) {
            CoffeeProductVariant::updateOrCreate(
                ['coffee_product_id' => $lampung->id, 'variant_name' => $v['name']],
                ['weight_grams' => $v['weight'], 'retail_price' => $v['retail'], 'wholesale_price' => $v['wholesale'], 'min_wholesale_qty' => $v['min'], 'is_active' => true]
            );
        }

        // 6. Paket Undangan Online (Sesuai Proyek Riil Undangan Digital)
        $invitations = [
            [
                'name' => 'Undangan Basic',
                'slug' => 'invitation-basic',
                'image' => 'invitations/wedding-cover.jpg',
                'price' => 249000,
                'discount_price' => 199000,
                'features' => [
                    'Cover Personalisasi Nama Tamu',
                    'Profil Kedua Mempelai',
                    'Detail Rangkaian Acara Lengkap',
                    'Navigasi Peta Google Maps Terintegrasi',
                    'Formulir RSVP / Konfirmasi Kehadiran Tamu',
                    'Masa Aktif 6 Bulan'
                ],
                'demo_url' => 'http://localhost:8080/undanganonline/public/undangan/agung-erik-kunti',
                'is_popular' => false,
                'sort_order' => 1,
            ],
            [
                'name' => 'Undangan Premium',
                'slug' => 'invitation-premium',
                'image' => 'invitations/couple-detail.jpg',
                'price' => 449000,
                'discount_price' => 349000,
                'features' => [
                    'Seluruh Fitur Paket Basic',
                    'Galeri Foto Kenangan (Slider)',
                    'Kisah Perjalanan Cinta (Love Story)',
                    'Dompet Digital / Amplop Online & Rekening',
                    'Ucapan Doa & Buku Tamu Digital',
                    'Countdown Hitung Mundur Hari Acara',
                    'Masa Aktif 1 Tahun'
                ],
                'demo_url' => 'http://localhost:8080/undanganonline/public/undangan/agung-erik-kunti',
                'is_popular' => true,
                'sort_order' => 2,
            ],
            [
                'name' => 'Undangan Exclusive (Flagship)',
                'slug' => 'invitation-exclusive',
                'image' => 'invitations/gallery-1.jpg',
                'price' => 799000,
                'discount_price' => 599000,
                'features' => [
                    'Seluruh Fitur Paket Premium',
                    'Musik Latar Romantis (Audio Player Otomatis)',
                    'Akses Bebas Seluruh Tema Flagship',
                    'Komposisi Visual Lebih Mewah & Halus',
                    'Prioritas Bantuan Input Data dari Tim Desain',
                    'Masa Aktif Selamanya (Lifetime Link)'
                ],
                'demo_url' => 'http://localhost:8080/undanganonline/public/undangan/agung-erik-kunti',
                'is_popular' => false,
                'sort_order' => 3,
            ],
        ];

        foreach ($invitations as $inv) {
            InvitationPackage::updateOrCreate(['slug' => $inv['slug']], $inv);
        }

        // 7. Kursus Pembelajaran (Aktama Academy LMS)
        $courses = [
            [
                'title' => 'Dasar Pemrograman Web Modern (HTML5, CSS3, & PHP)',
                'slug' => 'dasar-pemrograman-web-modern',
                'level' => 'Tingkat Pemula',
                'price' => 149000,
                'summary' => 'Belajar terstruktur dari konsep dasar web hingga berhasil mendeploy website perdana di server hosting.',
                'external_link' => 'http://localhost:8080/aktama/public',
                'is_published' => true,
            ],
            [
                'title' => 'Membangun Aplikasi Bisnis & POS dengan Laravel Framework',
                'slug' => 'membangun-aplikasi-bisnis-dengan-laravel',
                'level' => 'Tingkat Menengah',
                'price' => 299000,
                'summary' => 'Panduan terapan merancang sistem kasir, manajemen stok multi-harga, otorisasi hak akses, dan pelaporan keuangan.',
                'external_link' => 'http://localhost:8080/aktama/public',
                'is_published' => true,
            ],
        ];

        foreach ($courses as $c) {
            Course::updateOrCreate(['slug' => $c['slug']], $c);
        }

        // 8. Portofolio Proyek Terverifikasi
        $portfolios = [
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
                'project_url' => null,
                'description' => 'Aplikasi pencatatan stok barang, transaksi kasir eceran & grosir, cetak surat jalan, dan buku piutang tempo.',
                'is_published' => true,
            ],
            [
                'title' => 'Platform Undangan Pernikahan Digital Mobile-First',
                'slug' => 'platform-undangan-digital',
                'category' => 'website',
                'client_type' => 'Layanan Konsumen Publik',
                'technology' => 'Laravel, MySQL, JavaScript Interaktif',
                'project_year' => '2025',
                'project_url' => null,
                'description' => 'Portal undangan online responsif dengan personalisasi nama tamu, reservasi RSVP, amplop digital, dan integrasi maps.',
                'is_published' => true,
            ],
        ];

        foreach ($portfolios as $p) {
            Portfolio::updateOrCreate(['slug' => $p['slug']], $p);
        }

        // 9. Kategori & Artikel Blog Edukatif
        $catAi = Category::updateOrCreate(['slug' => 'kecerdasan-artifisial'], ['name' => 'Kecerdasan Artifisial (AI)']);
        $catWeb = Category::updateOrCreate(['slug' => 'tips-teknologi-web'], ['name' => 'Teknologi & Web']);

        Article::updateOrCreate(
            ['slug' => 'mengapa-website-bisnis-harus-aman-dari-celah-malware-judol'],
            [
                'category_id' => $catWeb->id,
                'title' => 'Mengapa Website Bisnis Harus Bebas dari Celah Malware & Spam Judi Online',
                'summary' => 'Banyak website perusahaan di Indonesia terkena peretasan script judi online yang merusak peringkat pencarian Google. Pelajari cara mengamankannya.',
                'content' => '<p>Reputasi sebuah bisnis digital sangat ditentukan oleh kehandalan infrastruktur teknologinya. Salah satu kendala yang kerap dihadapi website berbasis CMS usang adalah rentannya injeksi script otomatis judi online. Dengan menggunakan arsitektur modern seperti Laravel, file sistem inti terkunci rapat di luar direktori publik, memastikan data dan nama baik perusahaan Anda senantiasa terlindungi secara profesional.</p>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now(),
                'meta_title' => 'Keamanan Website Bisnis dari Celah Malware Judol | Aktama Digital',
                'meta_description' => 'Strategi mengamankan website perusahaan dari injeksi malware dan spam judi online menggunakan arsitektur modern.',
            ]
        );

        Article::updateOrCreate(
            ['slug' => 'peran-kecerdasan-artifisial-dalam-meningkatkan-produktivitas-kerja-administrasi'],
            [
                'category_id' => $catAi->id,
                'title' => 'Peran Kecerdasan Artifisial dalam Meningkatkan Produktivitas Kerja Administrasi',
                'summary' => 'Bagaimana pemanfaatan Generative AI dapat memangkas waktu kerja rutin penyusunan laporan, notula rapat, dan korespondensi dinas hingga 60%.',
                'content' => '<p>Di era digital saat ini, Kecerdasan Artifisial (AI) bukan lagi sekadar wacana teoritis melainkan instrumen praktis penunjang efisiensi kerja. Mulai dari penyusunan draf surat dinas yang baku, rekapitulasi data survei, hingga sintesis notula rapat yang komprehensif, AI membantu staf perkantoran dan tenaga kependidikan berfokus pada pengambilan keputusan strategis tanpa terbebani tugas manual yang berulang.</p>',
                'author' => 'Gede Erik Aktama, S.Pd., M.Pd.',
                'status' => 'published',
                'published_at' => now(),
                'meta_title' => 'AI untuk Efisiensi Administrasi Perkantoran | Aktama Digital',
                'meta_description' => 'Panduan pemanfaatan AI dalam mengotomasi pekerjaan administrasi perkantoran secara etis dan produktif.',
            ]
        );

        // 10. Opsi A: Seksi Beranda Default (Modular Section Drag & Drop)
        $homeSections = [
            [
                'section_key' => 'hero',
                'name' => 'Hero Banner & Profil Utama',
                'badge' => 'PT Aktama Digital Antika • Solusi Teknologi Terpadu',
                'title' => 'Kembangkan Bisnis & Kompetensi Digital Bersama Aktama Digital',
                'subtitle' => 'Penyedia layanan Pelatihan Kecerdasan Artifisial (AI) terapan untuk instansi & sekolah, Jasa Pembuatan Website & Aplikasi bisnis yang aman dari celah malware, ekosistem pembelajaran Aktama Academy, serta lini usaha Undangan Online dan Aktama Coffee.',
                'sort_order' => 1,
                'is_active' => true,
            ],
            [
                'section_key' => 'pelatihan_ai',
                'name' => 'Pelatihan AI & Koding (LPK Terdaftar)',
                'badge' => 'Pusat Pelatihan AI & Teknologi',
                'title' => 'Program Pelatihan Kecerdasan Artifisial (AI) & Koding Praktis',
                'subtitle' => 'Disusun langsung oleh Fasilitator Nasional KKA Kemdikdasmen berlisensi LPK resmi untuk mendongkrak produktivitas instansi pemerintah, sekolah, dan pelaku usaha.',
                'sort_order' => 2,
                'is_active' => true,
            ],
            [
                'section_key' => 'jasa_website',
                'name' => 'Jasa Pembuatan Website & Aplikasi',
                'badge' => 'Layanan Rekayasa Web & Software',
                'title' => 'Jasa Pembuatan Website & Aplikasi Bisnis Bebas Malware',
                'subtitle' => 'Didesain dengan arsitektur modern berstandar enterprise yang kebal dari risiko injeksi script judi online, cepat, mobile-friendly, dan teroptimasi SEO.',
                'sort_order' => 3,
                'is_active' => true,
            ],
            [
                'section_key' => 'aktama_academy',
                'name' => 'Aktama Academy (Ekosistem LMS)',
                'badge' => 'Platform Pembelajaran Daring',
                'title' => 'Aktama Academy — Belajar Koding & AI Kapan Saja',
                'subtitle' => 'Akses materi kursus terstruktur dari dasar pemrograman hingga pembuatan aplikasi bisnis mandiri bersama komunitas pembelajar aktif.',
                'sort_order' => 4,
                'is_active' => true,
            ],
            [
                'section_key' => 'aktama_coffee',
                'name' => 'Lini Usaha Kopi (Kopi Distro / Aktama Coffee)',
                'badge' => 'Ekosistem Komoditas Riil',
                'title' => 'Katalog Kopi Asli Nusantara — Retail & Pasokan Kafe',
                'subtitle' => 'Biji dan bubuk kopi single origin grade pilihan langsung dari petani mitra di Gayo, Toraja, Flores, dan Lampung untuk penikmat kopi maupun suplai bisnis warkop/kedai.',
                'sort_order' => 5,
                'is_active' => true,
            ],
            [
                'section_key' => 'undangan_online',
                'name' => 'Lini Usaha Undangan Online Digital',
                'badge' => 'Layanan Konsumen Publik',
                'title' => 'Paket Undangan Pernikahan Online Digital Elegan',
                'subtitle' => 'Sebar momen bahagia ke seluruh kerabat dengan desain visual premium, personalisasi nama tamu, reservasi RSVP, amplop digital, dan galeri interaktif.',
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
                'section_key' => 'tentang_kami',
                'name' => 'Profil Pimpinan & Legalitas Perusahaan',
                'badge' => 'Profil Perusahaan & Pimpinan',
                'title' => 'Integritas Legalitas & Kepemimpinan Berbasis Kompetensi Akademik',
                'subtitle' => 'Didirikan dengan landasan kepatuhan hukum yang solid serta dipimpin oleh praktisi sekaligus akademisi yang berkomitmen pada transfer teknologi nyata.',
                'sort_order' => 8,
                'is_active' => true,
            ],
            [
                'section_key' => 'artikel',
                'name' => 'Artikel & Wawasan Teknologi Terbaru',
                'badge' => 'Wawasan & Literasi Digital',
                'title' => 'Wawasan Terkini Seputar AI, Keamanan Web, & Bisnis Digital',
                'subtitle' => 'Artikel edukatif dan panduan praktis untuk membantu Anda memahami perkembangan lanskap teknologi terkini secara bijak.',
                'sort_order' => 9,
                'is_active' => true,
            ],
            [
                'section_key' => 'form_konsultasi',
                'name' => 'Formulir Konsultasi & Permintaan Penawaran',
                'badge' => 'Mulai Kolaborasi',
                'title' => 'Konsultasikan Kebutuhan Teknologi atau Pelatihan Anda',
                'subtitle' => 'Isi formulir ringkas di bawah ini atau hubungi saluran resmi kami. Tim teknis Aktama Digital akan menganalisis kebutuhan Anda dan memberikan solusi terbaik.',
                'sort_order' => 10,
                'is_active' => true,
            ],
        ];

        foreach ($homeSections as $sec) {
            HomeSection::updateOrCreate(['section_key' => $sec['section_key']], $sec);
        }

        // 11. Opsi B: Halaman Kustom Default (CMS Pages)
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
    }
}
