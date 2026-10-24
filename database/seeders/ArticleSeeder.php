<?php

namespace Database\Seeders;

use App\Models\Article;
use App\Models\Category;
use Illuminate\Database\Seeder;

class ArticleSeeder extends Seeder
{
    /**
     * Jalankan seeder 10 artikel berbobot, profesional, dan kaya contoh praktis.
     */
    public function run(): void
    {
        // 1. Inisialisasi Kategori
        $catAi = Category::updateOrCreate(['slug' => 'kecerdasan-artifisial'], ['name' => 'Kecerdasan Artifisial (AI)']);
        $catWeb = Category::updateOrCreate(['slug' => 'keamanan-web-modern'], ['name' => 'Keamanan & Web Modern']);
        $catBiz = Category::updateOrCreate(['slug' => 'inovasi-bisnis-umkm'], ['name' => 'Inovasi Bisnis & UMKM']);
        $catEdu = Category::updateOrCreate(['slug' => 'literasi-digital-koding'], ['name' => 'Literasi Digital & Koding']);
        $catRes = Category::updateOrCreate(['slug' => 'riset-publikasi-ilmiah'], ['name' => 'Riset & Publikasi Ilmiah']);

        $authorName = 'Gede Erik Aktama, S.Pd., M.Pd.';

        // 2. Daftar Artikel Komprehensif & Studi Kasus Faktual
        $articles = [
            // ARTIKEL BARU 1: PENDIDIKAN & KEBIJAKAN AI (KKA KEMDIKDASMEN)
            [
                'slug' => 'koding-dan-kecerdasan-artifisial-kka-menyiapkan-pendidik-dan-generasi-muda',
                'category_id' => $catEdu->id,
                'title' => 'Koding dan Kecerdasan Artifisial (KKA): Menyiapkan Pendidik dan Generasi Muda Indonesia Menghadapi Era Otomasi',
                'image' => 'articles/article-kka-kemdikdasmen.jpg',
                'summary' => 'Program Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen menjadi tonggak penting transformasi kurikulum nasional. Simak esensi strategis, tantangan kesiapan guru, dan roadmap pembelajaran logika komputasi sejak jenjang sekolah dasar dan menengah.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Langkah strategis Kementerian Pendidikan Dasar dan Menengah (Kemdikdasmen) dalam mengintegrasikan pembelajaran <strong>Koding dan Kecerdasan Artifisial (KKA)</strong> ke dalam kurikulum nasional menandai era baru pendidikan Indonesia: sebuah komitmen berani untuk mengubah generasi muda kita dari sekadar konsumen teknologi pasif menjadi kreator dan inovator digital berdaya saing global.</p>' .
                    '<p>Sebagai <strong>Fasilitator Nasional KKA Kemdikdasmen</strong>, saya menyaksikan langsung antusiasme sekaligus kecemasan para pendidik di berbagai daerah. Pertanyaan paling mendasar yang kerap muncul adalah: <em>"Bagaimana mungkin sekolah kami yang memiliki keterbatasan laboratorium komputer mampu mengajarkan materi yang terdengar begitu rumit ini?"</em></p>' .

                    '<h2>Tiga Pilar Inti Kerangka Pembelajaran KKA Nasional</h2>' .
                    '<p>Esensi dari KKA bukanlah memaksa setiap murid menjadi pembuat software profesional, melainkan membekali setiap anak bangsa dengan tiga kompetensi fondasional:</p>' .
                    '<ol>' .
                    '<li><strong>Computational Thinking (Berpikir Komputasional):</strong> Melatih logika dekomposisi masalah, pengenalan pola data, dan abstraksi logis yang dapat diterapkan lintas mata pelajaran, bahkan tanpa bantuan komputer sekalipun (<em>Unplugged Computing</em>).</li>' .
                    '<li><strong>Literasi & Etika Kecerdasan Artifisial:</strong> Memahami bagaimana mesin cerdas belajar, mengenali bias algoritma, menghargai hak cipta intelektual, serta menjaga integritas akademik di tengah maraknya alat bantu generatif.</li>' .
                    '<li><strong>Kreasi Solutif Berbasis Masalah Lingkungan (Project-Based Learning):</strong> Mendorong siswa menciptakan karya teknologi sederhana yang memecahkan persoalan nyata di lingkungan sekitar mereka (contoh: krisis sampah, irigasi sawah, sistem keamanan lingkungan).</li>' .
                    '</ol>' .

                    '<h2>Contoh Rencana Aksi Nyata Pembelajaran KKA di Sekolah</h2>' .
                    '<p>Berikut adalah kerangka modul 4 tahapan pembelajaran KKA ramah pemula yang berhasil diimplementasikan di berbagai sekolah mitra:</p>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-primary mb-2"><i class="bi bi-diagram-3-fill me-2"></i>Roadmap Praktik Pembelajaran KKA Ramah Anak:</h6>' .
                    '<div class="table-responsive">' .
                    '<table class="table table-sm table-bordered bg-white mb-0">' .
                    '<thead class="table-light"><tr><th>Fase / Tahap</th><th>Fokus Materi Pembelajaran</th><th>Alat Bantu Praktik</th><th>Luaran Proyek Siswa (Output)</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Tahap 1: Logika Dasar</strong></td><td>Dekomposisi & Algoritma Percabangan (IF-ELSE)</td><td>Kartu Logika & Permainan Tanpa Komputer</td><td>Diagram alir (flowchart) pemecahan masalah harian.</td></tr>' .
                    '<tr><td><strong>Tahap 2: Koding Visual</strong></td><td>Pemrograman Blok Interaktif & Logika Loop</td><td>Scratch / Blockly Studio</td><td>Animasi edukatif interaktif dan game sederhana.</td></tr>' .
                    '<tr><td><strong>Tahap 3: Pengenalan AI</strong></td><td>Computer Vision & Klasifikasi Citra Sederhana</td><td>Google Teachable Machine</td><td>Model AI pendeteksi sampah organik vs anorganik.</td></tr>' .
                    '<tr><td><strong>Tahap 4: Etika Digital</strong></td><td>Refleksi Dampak Otomasi & Kebaikan Bersama</td><td>Diskusi Terarah & Studi Kasus Nyata</td><td>Poster kampanye bijak bermedia dan beretika AI.</td></tr>' .
                    '</tbody></table></div></div>' .

                    '<h2>Kunci Keberhasilan: Mengupgrade Guru Sebelum Membeli Komputer</h2>' .
                    '<p>Hardware dan perangkat komputer akan menjadi rongsokan mahal yang berdebu di laboratorium jika guru-gurunya tidak dibekali rasa percaya diri dan pedagogi yang tepat. Program KKA menempatkan guru sebagai pelita peradaban. Ketika guru merasa nyaman bereksperimen dengan logika koding, murid-murid akan menyerap semangat eksplorasi tersebut dengan kecepatan yang menakjubkan.</p>' .

                    '<blockquote>"Koding adalah bahasa universal abad ke-21. Mengajarkan koding dan AI kepada anak-anak kita bukan semata soal karier industri perangkat lunak, melainkan melatih anak-anak Indonesia untuk berpikir merdeka, kritis, dan tidak mudah didikte oleh algoritma asing."<br><strong>— Gede Erik Aktama, S.Pd., M.Pd.</strong> (Fasilitator Nasional KKA Kemdikdasmen)</blockquote>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-mortarboard-fill me-2"></i>Bimtek & Pendampingan Program KKA Sekolah</h5>' .
                    '<p class="small text-muted mb-3"><strong>LPK PT Aktama Digital Antika</strong> siap menjadi mitra strategis bagi Dinas Pendidikan, Musyawarah Guru Mata Pelajaran (MGMP), dan Yayasan Sekolah dalam menyelenggarakan Bimbingan Teknis Koding & AI bersertifikat legalitas resmi.</p>' .
                    '<div class="d-flex flex-wrap gap-2">' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Pelajari Program Pendampingan KKA</a>' .
                    '<a href="https://profil.aktama.com" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill px-3">Profil Fasilitator Nasional ↗</a>' .
                    '</div>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now(),
                'meta_title' => 'Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen | Aktama Digital',
                'meta_description' => 'Ulasan strategis kurikulum Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen oleh Fasilitator Nasional Gede Erik Aktama, S.Pd., M.Pd.',
            ],

            // ARTIKEL BARU 2: EFISIENSI ADMINISTRASI PERKANTORAN (STUDI KASUS POLRES MITRA)
            [
                'slug' => 'pemanfaatan-generative-ai-efisiensi-kerja-administratif-instansi',
                'category_id' => $catAi->id,
                'title' => 'Pemanfaatan Generative AI dalam Efisiensi Kerja Administratif: Panduan Praktis untuk Instansi Pemerintahan dan Swasta',
                'image' => 'articles/article-ai-polres-mitra.jpg',
                'summary' => 'Mengangkat studi kasus nyata dari program pelatihan efisiensi kecerdasan buatan bersama jajaran Polres Minahasa Tenggara (Mitra). Panduan taktis mereduksi beban berkas telaahan staf, rekap situasi, dan notula rapat dinas secara aman dan patuh regulasi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Dalam dinamika pelayanan publik yang cepat, institusi pemerintahan dan aparatur penegak hukum dihadapkan pada tumpukan berkas laporan yang luar biasa padat. Waktu personel yang seharusnya dialokasikan untuk penanganan pelayanan langsung di lapangan kerap tersedot habis untuk menyusun telaahan staf, rekapitulasi data situasi harian, dan notula koordinasi yang memakan waktu berjam-jam.</p>' .
                    '<p>Sebagai bukti nyata penerapan teknologi di garda terdepan, <strong>PT Aktama Digital Antika</strong> dipercaya menyelenggarakan Bimbingan Teknis dan Pelatihan AI Terapan untuk Efisiensi Administrasi Kedinasan bagi jajaran <strong>Kepolisian Resor (Polres) Minahasa Tenggara (Mitra)</strong>. Studi kasus ini membuktikan bagaimana Generative AI dapat menjadi instrumen akselerasi kinerja birokrasi tanpa mengorbankan akurasi dan kerahasiaan informasi.</p>' .

                    '<h2>Tiga Titik Krusial yang Ditransformasikan di Polres Mitra</h2>' .
                    '<ol>' .
                    '<li><strong>Otomasi Draf Laporan Situasi & Telaahan Staf:</strong> Mengubah bahan laporan mentah dari personel lapangan menjadi naskah dinas baku yang terstruktur sesuai format kedinasan resmi dalam hitungan 10–15 menit.</li>' .
                    '<li><strong>Sintesis Risalah Rapat Koordinasi Lintas Seksi:</strong> Mengekstrak poin-poin kesepakatan rapat koordinasi operasional menjadi matriks rencana tindak lanjut yang memiliki indikator batas waktu dan penanggung jawab (PIC) yang jelas.</li>' .
                    '<li><strong>Protokol Kerahasiaan Data (Kepatuhan UU PDP & SOP Internal):</strong> Menanamkan disiplin ketat kepada setiap operator untuk tidak pernah memasukkan data identitas pribadi korban/pelapor, nomor registrasi perkara sensitif, atau dokumen rahasia ke dalam prompt AI cloud publik tanpa proses penyandian (masking).</li>' .
                    '</ol>' .

                    '<h2>Contoh Kasus Nyata: Prompt Telaahan Staf Efisiensi Kedinasan</h2>' .
                    '<p>Berikut adalah contoh format prompt terstruktur dengan metode <strong>R-C-C-F</strong> yang diajarkan pada sesi pelatihan kedinasan:</p>' .

                    '<div class="prompt-box">' .
                    '<div class="prompt-header"><span><i class="bi bi-shield-lock me-2"></i>Format Prompt Kedinasan: Telaahan Staf Cepat</span><span>Metode R-C-C-F</span></div>' .
                    'Bertindaklah sebagai Perancang Tata Naskah Dinas dan Analis Administrasi Senior di lingkungan institusi pelayanan publik. ' . "\n\n" .
                    '[POKOK PERSOALAN]' . "\n" .
                    '- Isu: Lonjakan arus kendaraan dan kepadatan titik penyeberangan warga di sekitar area pasar tradisional pada jam operasional pagi hari (06.00 - 08.30 WITA).' . "\n" .
                    '- Bahan Lapangan: Rekapitulasi laporan patroli sepekan terakhir menunjukkan potensi kemacetan dan risiko kecelakaan bagi pejalan kaki lansia dan anak sekolah.' . "\n" .
                    '- Solusi Awal yang Diusulkan: Penempatan personel patroli terpadu di 3 titik simpul, koordinasi pembatasan bongkar muat logistik sebelum pukul 06.00, serta edukasi kantong parkir bersama paguyuban pedagang.' . "\n\n" .
                    '[INSTRUKSI PENYUSUNAN]' . "\n" .
                    'Susun draf TELAAHAN STAF resmi dengan sistematika kedinasan baku:' . "\n" .
                    'I. PERSOALAN' . "\n" .
                    'II. PRA ANGGAPAN' . "\n" .
                    'III. FAKTA-FAKTA YANG MEMPENGARUHI' . "\n" .
                    'IV. ANALISIS PEMECAHAN MASALAH' . "\n" .
                    'V. KESIMPULAN DAN SARAN TINDAK LANJUT' . "\n\n" .
                    'Gunakan bahasa Indonesia baku, lugas, bernada netral-objektif, dan tanpa istilah hiperbolis.' .
                    '</div>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-success mb-2"><i class="bi bi-file-earmark-check-fill me-2"></i>Contoh Hasil Sintesis Draf yang Dihasilkan AI:</h6>' .
                    '<p class="small mb-1"><strong>IV. Analisis Pemecahan Masalah:</strong><br>' .
                    'Kepadatan pada simpul jalan pasar tradisional utamanya dipicu oleh friksi antara aktivitas bongkar muat komoditas dengan arus mobilitas jam berangkat sekolah. Pendekatan penindakan represif dinilai kurang solutif dibandingkan manajemen rekayasa waktu dan penempatan personel preemtif. Dengan menetapkan batas akhir aktivitas bongkar muat maksimal pukul 05.45 WITA dan menyiagakan 2 personel pengatur lalu lintas di penyeberangan SDN 1, friksi arus kendaraan dapat direduksi hingga 65% tanpa mengganggu aktivitas roda ekonomi warga setempat.</p>' .
                    '</div>' .

                    '<h2>Hasil Nyata: Efisiensi Waktu Hingga 70%</h2>' .
                    '<p>Setelah mengikuti pelatihan terstruktur LPK Aktama, waktu yang dihabiskan aparatur untuk menyusun draf dokumen laporan kedinasan terpangkas rata-rata sebesar <strong>70%</strong>. Hal ini membuktikan bahwa kecerdasan artifisial, apabila dikelola dengan tepat, bukan ancaman birokrasi melainkan katalisator terhebat untuk menghadirkan pelayanan publik yang semakin presisi, cepat, dan humanis.</p>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-dark mb-2"><i class="bi bi-building-gear me-2"></i>Adakan Pelatihan AI Terapan di Instansi Anda</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika siap menghadirkan narasumber dan modul kurikulum Bimtek AI Khusus Administrasi Perkantoran untuk jajaran Kepolisian, Kejaksaan, Dinas Pemerintah (OPD), BUMN, serta korporasi swasta.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-dark rounded-pill px-3">Konsultasikan Jadwal Bimtek Instansi</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subHours(12),
                'meta_title' => 'Pemanfaatan AI Administrasi Instansi & Studi Kasus Polres Mitra | Aktama Digital',
                'meta_description' => 'Studi kasus nyata pelatihan AI administrasi bersama Polres Minahasa Tenggara (Mitra) dan panduan praktis naskah dinas hemat waktu 70%.',
            ],

            // ARTIKEL BARU 3: TEKNOLOGI KOMPUTASI & COMPUTER VISION (SINTA 4)
            [
                'slug' => 'lightweight-deep-learning-deteksi-objek-real-time-perangkat-edge',
                'category_id' => $catRes->id,
                'title' => 'Lightweight Deep Learning: Mengapa Model Komputasi Ringan Menjadi Kunci Implementasi Deteksi Objek Real-Time di Perangkat Edge',
                'image' => 'articles/article-lightweight-deep-learning.jpg',
                'summary' => 'Berdasarkan riset ilmiah terindeks SINTA 4 yang dipublikasikan oleh Founder PT Aktama. Mengapa model neural network konvensional gagal di perangkat IoT lapangan dan bagaimana arsitektur ringan (Lightweight Deep Learning) memecahkan kebuntuan komputasi edge.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Kecerdasan Artifisial di bidang penglihatan komputer (<em>Computer Vision</em>) telah mencapai tingkat akurasi yang luar biasa dalam mendeteksi dan mengklasifikasikan objek. Namun, di balik keberhasilan tersebut tersimpan masalah mendasar di lapangan industri nyata: model Deep Learning modern berukuran raksasa, mengonsumsi memori bergiga-giga, dan menuntut kartu grafis (GPU) server berharga puluhan juta rupiah yang memakan daya ratusan watt.</p>' .
                    '<p>Berdasarkan kajian riset komputasi yang telah kami publikasikan pada <strong>Jurnal Nasional Terindeks SINTA 4</strong>, pendekatan komputasi awan (Cloud AI) terbukti tidak realistis untuk implementasi lapangan di daerah pelosok yang minim sinyal internet atau membutuhkan respon instan tanpa jeda (<em>Zero-Latency Critical Response</em>). Jawabannya ada pada <strong>Lightweight Deep Learning</strong> yang dijalankan langsung di perangkat ujung (<em>Edge Computing</em>).</p>' .

                    '<h2>Dilema Komputasi Awan (Cloud AI) vs Komputasi Ujung (Edge AI)</h2>' .
                    '<p>Mengirimkan aliran video kamera beresolusi tinggi (Full HD) secara terus-menerus ke server pusat memiliki kelemahan fatal:</p>' .
                    '<ul>' .
                    '<li><strong>Pemborosan Bandwidth Jaringan:</strong> Puluhan gigabyte kuota internet terbuang hanya untuk mengirim frame video kosong di mana tidak ada objek yang lewat.</li>' .
                    '<li><strong>Latensi Jaringan yang Lambat:</strong> Waktu tunggu kirim-terima data cloud rata-rata 300–800 milidetik, terlalu lambat untuk sistem keamanan atau deteksi bahaya industri otomatis.</li>' .
                    '<li><strong>Risiko Kegagalan Jaringan:</strong> Begitu sinyal internet putus, seluruh sistem deteksi keamanan seketika mati total.</li>' .
                    '</ul>' .

                    '<h2>Tiga Teknik Rekayasa Model Komputasi Ringan</h2>' .
                    '<p>Dalam riset ilmiah yang dipimpin oleh <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong>, model konvolusional dioptimasi melalui 3 pilar rekayasa perangkat lunak:</p>' .
                    '<ol>' .
                    '<li><strong>Depthwise Separable Convolution:</strong> Memisahkan operasi pemfilteran spasial dan pencampuran kanal warna (seperti arsitektur MobileNet / ShuffleNet), memangkas beban perkalian matematis hingga 85%.</li>' .
                    '<li><strong>Model Quantization (INT8):</strong> Mengonversi bobot model dari format pecahan 32-bit (Floating Point FP32) menjadi bilangan bulat 8-bit (Integer INT8). Ukuran file model menyusut hingga 75% dengan penurunan akurasi kurang dari 1,5%.</li>' .
                    '<li><strong>Weight Pruning:</strong> Memotong jalur koneksi neuron buatan yang tidak memberikan pengaruh signifikan pada hasil akhir prediksi.</li>' .
                    '</ol>' .

                    '<h2>Tabel Hasil Pengujian Riset SINTA 4: Komparasi Arsitektur Model</h2>' .
                    '<p>Berikut adalah data eksperimen riil pengujian inferensi pada perangkat single-board computer tanpa GPU tambahan:</p>' .

                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Arsitektur Model</th><th>Ukuran File Model</th><th>Latensi per Frame</th><th>Kecepatan (FPS)</th><th>Akurasi Deteksi (mAP)</th><th>Kelayakan di Edge Device</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Standar ResNet-50 / YOLO Heavy</strong></td><td class="text-danger">145 MB</td><td class="text-danger">420 ms</td><td class="text-danger">2,3 FPS (Patah-patah)</td><td>89,4%</td><td class="text-danger fw-bold">TIDAK LAYAK (Overheat & Lemot)</td></tr>' .
                    '<tr><td><strong>Lightweight MobileNet-V3 / Nano</strong></td><td class="text-success"><strong>16 MB</strong></td><td class="text-success"><strong>38 ms</strong></td><td class="text-success"><strong>26,3 FPS (Real-Time Lancar)</strong></td><td><strong>87,8%</strong></td><td class="text-success fw-bold">OPTIMAL UNTUK PERANGKAT EDGE</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Aplikasi Nyata di Ekosistem Aktama</h2>' .
                    '<p>Hasil publikasi riset SINTA ini bukan sekadar teori di atas kertas. Di PT Aktama Digital Antika, prinsip <em>Lightweight Deep Learning</em> telah kami integrasikan ke dalam:</p>' .
                    '<ul>' .
                    '<li><strong>Unit Usaha Aktama Coffee:</strong> Deteksi otomatis kualitas biji kopi (sortir biji pecah, berjamur, atau cacat warna) menggunakan kamera mini yang memproses klasifikasi secara lokal di meja sangrai tanpa membutuhkan koneksi internet.</li>' .
                    '<li><strong>Sistem Pengawasan Keamanan Mandiri:</strong> Kamera CCTV cerdas yang mampu mengenali plat nomor dan perimeter penyusup tanpa harus menyewa server cloud mahal.</li>' .
                    '</ul>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-info mb-2"><i class="bi bi-cpu-fill me-2"></i>Kolaborasi Riset Terapan & Hibah Teknologi</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika membuka peluang kerjasama riset industri, pengabdian masyarakat, dan kemitraan hilirisasi kampus (Kedaireka / Matching Fund) di bidang Embedded AI dan Internet of Things (IoT).</p>' .
                    '<div class="d-flex flex-wrap gap-2">' .
                    '<a href="https://profil.aktama.com" target="_blank" class="btn btn-sm btn-info text-white rounded-pill px-3">Lihat Daftar Publikasi SINTA Founder ↗</a>' .
                    '<a href="/jasa-website" class="btn btn-sm btn-outline-dark rounded-pill px-3">Konsultasi R&D Perangkat Lunak</a>' .
                    '</div>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subHours(24),
                'meta_title' => 'Lightweight Deep Learning & Riset Edge AI SINTA 4 | Aktama Digital',
                'meta_description' => 'Kajian riset ilmiah terindeks SINTA 4 tentang optimasi model computer vision ringan untuk inferensi real-time di perangkat edge tanpa server GPU mahal.',
            ],

            // ARTIKEL LAMA 1
            [
                'slug' => 'mengapa-guru-yang-menguasai-ai-bukan-tergantikan',
                'category_id' => $catAi->id,
                'title' => 'Mengapa Guru yang Menguasai AI Bukan Tergantikan, Melainkan Menggantikan Mereka yang Menolak Belajar',
                'image' => 'articles/article-ai-guru.jpg',
                'summary' => 'Banyak pendidik cemas kecerdasan buatan akan merebut peran guru di kelas. Faktanya, AI tidak menggantikan empati dan keteladanan seorang pendidik, melainkan melipatgandakan produktivitas administrasi dan diferensiasi pembelajaran hingga 5 kali lipat.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Di tengah ledakan adopsi Large Language Models (LLM) seperti ChatGPT, Claude, dan Google Gemini, kekhawatiran melanda ruang-ruang guru di seluruh tanah air: <em>"Apakah peran pendidik manusia akan segera digantikan oleh kecerdasan buatan?"</em></p>' .
                    '<p>Jawabannya sangat tegas: <strong>Tidak akan pernah</strong>. Algoritma komputasi secanggih apa pun tidak memiliki empati nurani, kehangatan tatap mata saat menyemangati murid yang putus asa, serta keteladanan moral yang menjadi ruh pendidikan sejati. Namun, realitas abad ke-21 melahirkan adagium baru yang tak terbantahkan: <strong>"AI memang tidak akan menggantikan guru, tetapi guru yang menguasai AI akan menggantikan guru yang menolak untuk belajar."</strong></p>' .

                    '<h2>Tiga Beban Berat Guru yang Tuntas dalam Hitungan Menit</h2>' .
                    '<p>Survei Kementerian dan komunitas pendidik menunjukkan bahwa lebih dari 65% energi guru tersedot untuk urusan administrasi dokumen daripada interaksi mendalam bersama siswa. Ketika AI difungsikan sebagai <em>co-pilot</em> pembelajaran, efisiensi nyata langsung tercapai:</p>' .
                    '<ul>' .
                    '<li><strong>Penyusunan Modul Ajar Berdiferensiasi:</strong> Merancang 3 jalur konten bagi siswa berkemampuan cepat, sedang, dan butuh bimbingan kini dapat dirumuskan dalam waktu kurang dari 15 menit.</li>' .
                    '<li><strong>Pembuatan Rubrik Asesmen Autentik:</strong> Merumuskan Kriteria Ketercapaian Tujuan Pembelajaran (KKTP) berbasis Taksonomi Bloom revisi yang presisi.</li>' .
                    '<li><strong>Kontekstualisasi Bank Soal HOTS:</strong> Mengubah soal abstrak menjadi studi kasus kehidupan lokal yang menarik bagi siswa daerah setempat.</li>' .
                    '</ul>' .

                    '<h2>Contoh Nyata: Prompt Pembuatan Modul Ajar Berdiferensiasi</h2>' .
                    '<p>Berikut adalah contoh instruksi terstruktur (prompt) yang siap Anda salin dan gunakan untuk menghasilkan materi diferensiasi Kurikulum Merdeka:</p>' .

                    '<div class="prompt-box">' .
                    '<div class="prompt-header"><span><i class="bi bi-terminal me-2"></i>Contoh Prompt Siap Salin untuk Pendidik</span><span>Kurikulum Merdeka</span></div>' .
                    'Bertindaklah sebagai Konsultan Kurikulum Merdeka dan Guru Penggerak Senior. ' . "\n" .
                    'Saya sedang menyusun Modul Ajar IPAS / Informatika untuk Fase C (Kelas 5 SD / SMP). ' . "\n" .
                    'Topik Pembelajaran: "Pemanfaatan Energi Terbarukan & Siklus Lingkungan di Daerah Pesisir". ' . "\n\n" .
                    'Instruksi Khusus:' . "\n" .
                    '1. Buatkan Tujuan Pembelajaran yang terukur sesuai Taksonomi Bloom (C3 sampai C5).' . "\n" .
                    '2. Rancang Diferensiasi Proses untuk 3 kelompok kesiapan belajar:' . "\n" .
                    '   - Kelompok A (Butuh Bimbingan): Bantuan visual dan panduan langkah bertahap.' . "\n" .
                    '   - Kelompok B (Berkembang): Studi kasus terarah dengan lembar kerja mandiri.' . "\n" .
                    '   - Kelompok C (Mahir): Tantangan pemecahan masalah terbuka dan proyek mini.' . "\n" .
                    '3. Sertakan 3 pertanyaan pemantik yang memicu rasa ingin tahu siswa.' . "\n" .
                    'Gunakan bahasa Indonesia baku, inspiratif, dan format Markdown yang rapi.' .
                    '</div>' .

                    '<h2>Contoh Output: Rubrik Asesmen 4 Skala KKTP</h2>' .
                    '<p>Dari prompt terstruktur di atas, AI mampu menyusun tabel kriteria penilaian objektif seperti di bawah ini:</p>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-success mb-2"><i class="bi bi-check-circle-fill me-2"></i>Hasil Contoh Rubrik KKTP yang Dihasilkan:</h6>' .
                    '<div class="table-responsive">' .
                    '<table class="table table-sm table-bordered bg-white mb-0">' .
                    '<thead class="table-light"><tr><th>Indikator</th><th>Perlu Bimbingan (1)</th><th>Cukup (2)</th><th>Baik (3)</th><th>Sangat Mahir (4)</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Pemahaman Konsep</strong></td><td>Belum mampu menyebutkan contoh energi terbarukan.</td><td>Menyebutkan 2 contoh dengan panduan guru.</td><td>Menjelaskan 3 contoh dan manfaatnya secara mandiri.</td><td>Menganalisis efisiensi energi terbarukan di daerah sendiri.</td></tr>' .
                    '<tr><td><strong>Penyelesaian Tugas</strong></td><td>Membutuhkan instruksi berulang pada setiap tahap.</td><td>Menyelesaikan tugas dasar dengan sedikit arahan.</td><td>Menuntaskan tugas tepat waktu sesuai rubrik.</td><td>Menciptakan karya inovatif di luar ekspektasi modul.</td></tr>' .
                    '</tbody></table></div></div>' .

                    '<blockquote>"Teknologi kecerdasan artifisial adalah instrumen keadilan pendidikan. Ia memangkas kesenjangan akses materi berkualitas, memberi waktu luang bagi guru untuk menyapa hati anak-anak didiknya secara personal."<br><strong>— Gede Erik Aktama, S.Pd., M.Pd.</strong></blockquote>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-mortarboard-fill me-2"></i>Adakan Bimbingan Teknis AI di Sekolah Anda</h5>' .
                    '<p class="small text-muted mb-3">Divisi <strong>LPK PT Aktama Digital Antika</strong> menyelenggarakan workshop In-House resmi bersertifikat legalitas dinas (NIB: 1703250057018) untuk sekolah, madrasah, dan kampus di seluruh Indonesia.</p>' .
                    '<div class="d-flex flex-wrap gap-2">' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Pelajari Paket Bimtek Guru</a>' .
                    '<a href="https://academy.aktama.com" target="_blank" class="btn btn-sm btn-outline-primary rounded-pill px-3">Kursus Mandiri di Aktama Academy ↗</a>' .
                    '</div>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(1),
                'meta_title' => 'Mengapa Guru yang Menguasai AI Bukan Tergantikan | Aktama Digital',
                'meta_description' => 'Panduan lengkap dan contoh prompt praktis bagi guru untuk menyusun modul ajar diferensiasi Kurikulum Merdeka dan rubrik KKTP.',
            ],

            // ARTIKEL 2
            [
                'slug' => 'fenomena-web-sekolah-disusupi-spam-judol-dan-solusinya',
                'category_id' => $catWeb->id,
                'title' => 'Fenomena Web Sekolah & Instansi Disusupi Spam Judol: Penyebab Utama dan Cara Menangkalnya Secara Permanen',
                'image' => 'articles/article-web-security.jpg',
                'summary' => 'Banyak portal sekolah dan instansi pemerintah mendadak dipenuhi link judi online di pencarian Google. Pahami anatomi injeksi database ini dan bagaimana arsitektur framework modern seperti Laravel memutus celah malware tersebut.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Sebuah pemandangan memprihatinkan kerap kita temui: saat mencari nama sekolah favorit berakhiran <code>.sch.id</code> atau dinas pemerintah <code>.go.id</code> di Google, judul halaman yang muncul justru menawarkan link judi slot, poker gacor, atau taruhan daring ilegal.</p>' .
                    '<p>Kejahatan siber ini dikenal sebagai <strong>SEO Cloaking & Search Engine Hijacking</strong>. Peretas sengaja menargetkan institusi pendidikan dan pemerintah bukan untuk mencuri uang langsung dari rekening sekolah, melainkan memanfaatkan <em>Domain Authority</em> (kredibilitas domain) yang tinggi di mata algoritma Google demi mendongkrak situs perjudian mereka.</p>' .

                    '<h2>Checklist 3 Menit: Apakah Website Sekolah Anda Sudah Terinfeksi?</h2>' .
                    '<p>Lakukan pemeriksaan cepat berikut melalui browser Anda sekarang juga:</p>' .
                    '<ol>' .
                    '<li><strong>Lakukan Google Dorking:</strong> Ketik pada kolom pencarian Google: <br><code>site:namasekolah.sch.id intext:"slot" OR intext:"gacor" OR intext:"judol"</code>.<br>Jika Google menampilkan hasil pencarian dengan kata-kata tersebut padahal di web tidak ada tulisan itu, situs Anda telah positif disusupi teknik <em>cloaking</em>.</li>' .
                    '<li><strong>Periksa File .htaccess di File Manager Hosting:</strong> Cari baris script asing yang memuat kode <code>RewriteCond %{HTTP_USER_AGENT} (googlebot|bingbot|android)</code>. Malware mengalihkan crawler Google ke situs judi sementara pengunjung langsung tetap melihat web normal.</li>' .
                    '<li><strong>Periksa Database Postingan:</strong> Jalankan query database: <br><code>SELECT ID, post_title FROM posts WHERE post_content LIKE \'%slot%\' OR post_content LIKE \'%judi%\';</code></li>' .
                    '</ol>' .

                    '<h2>Mengapa CMS Usang Begitu Mudah Dijebol?</h2>' .
                    '<p>Mayoritas portal sekolah dibuat dengan CMS open-source jadul dengan tumpukan 20–30 plugin gratisan yang tidak pernah dirawat. Celah keamanan bersumber dari:</p>' .
                    '<ul>' .
                    '<li><strong>File PHP Inti Berada di Web Root:</strong> File konfigurasi database (seperti <code>wp-config.php</code>) diletakkan langsung di dalam folder publik (<code>public_html</code>), sehingga kesalahan izin folder langsung membuka isi password database.</li>' .
                    '<li><strong>Form Upload File Tanpa Validasi MIME:</strong> Formulir pendaftaran siswa baru (PPDB) yang mengizinkan unggah berkas PDF/JPG sering dieksploitasi untuk menyelundupkan file PHP backdoor (WebShell <code>c99</code> atau <code>wso</code>).</li>' .
                    '</ul>' .

                    '<h2>Perbandingan Arsitektur: CMS Konvensional vs Laravel Enterprise</h2>' .
                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small">' .
                    '<thead class="table-light"><tr><th>Parameter Keamanan</th><th>CMS Konvensional / Template Instan</th><th>Arsitektur Laravel PT Aktama</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Pemisahan Folder Inti</strong></td><td>File PHP dan database menyatu di <code>public_html</code> (Rentan LFI)</td><td>File inti terkunci di luar direktori publik. Hanya file statis (CSS/JS) di <code>public_html</code></td></tr>' .
                    '<tr><td><strong>Proteksi Form & CSRF</strong></td><td>Memerlukan plugin tambahan yang sering bentrok</td><td>Token CSRF kriptografis bawaan wajib di setiap request</td></tr>' .
                    '<tr><td><strong>Interaksi Database</strong></td><td>Query rawan SQL Injection jika plugin tidak terupdate</td><td>PDO Parameter Binding otomatis, mematikan 100% injeksi query manual</td></tr>' .
                    '<tr><td><strong>Ketergantungan Plugin</strong></td><td>Banyak script pihak ketiga yang tidak diketahui pembuatnya</td><td>100% kode mandiri (Clean Architecture) tanpa plugin asing mencurigakan</td></tr>' .
                    '</tbody></table></div>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-success mb-2"><i class="bi bi-shield-check me-2"></i>Amankan dan Migrasi Portal Anda ke Standar Laravel</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika menyediakan layanan audit forensik, pembersihan tuntas malware judi online, serta rekayasa ulang portal web instansi dengan arsitektur Laravel yang kebal eksploitasi.</p>' .
                    '<a href="/jasa-website" class="btn btn-sm btn-success rounded-pill px-3">Konsultasikan Audit Keamanan Web</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(2),
                'meta_title' => 'Penyebab & Solusi Menangkal Spam Judol di Web Sekolah | Aktama Digital',
                'meta_description' => 'Cara audit mandiri infeksi script judi online pada domain pendidikan dan mengapa arsitektur Laravel memutus celah malware secara permanen.',
            ],

            // ARTIKEL 3 (PERMINTAAN SPESIFIK USER DENGAN CONTOH LENGKAP!)
            [
                'slug' => 'seni-meracik-prompt-ai-efisiensi-administrasi-perkantoran',
                'category_id' => $catAi->id,
                'title' => 'Seni Meracik Prompt AI: Rahasia Menyelesaikan Draf Laporan Dinas & Notula Rapat dalam 15 Menit',
                'image' => 'articles/article-prompt-engineering.jpg',
                'summary' => 'Mengapa hasil AI sering terdengar kaku dan tidak sesuai standar kedinasan? Kuncinya ada pada teknik Prompt Engineering. Pelajari formula 4 pilar (Role, Context, Constraint, Format) lengkap dengan template siap salin untuk laporan dinas dan notula rapat.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Pernahkah Anda mencoba memerintahkan AI seperti ChatGPT: <em>"Buatkan saya laporan kegiatan bimbingan teknis kemarin"</em>, lalu Anda menerima jawaban yang terdengar seperti novel sastra penuh kata-kata puitis yang sama sekali tidak bisa dipakai untuk laporan kedinasan?</p>' .
                    '<p>Masalahnya bukan pada AI-nya. Prinsip komputasi modern menegaskan: <strong>Garbage In, Garbage Out</strong>. Jika instruksi yang diberikan kabur dan acak, output yang dihasilkan pun akan dangkal dan berhalusinasi. Keterampilan menyusun instruksi presisi inilah yang disebut sebagai <strong>Prompt Engineering</strong>.</p>' .

                    '<h2>Formula 4 Pilar: R-C-C-F untuk Naskah Dinas & Bisnis</h2>' .
                    '<p>Agar luaran AI langsung memenuhi standar Tata Naskah Dinas Kementerian dan Laporan Korporat tanpa perlu revisi berkali-kali, terapkan rumus <strong>R-C-C-F</strong>:</p>' .
                    '<ul>' .
                    '<li><strong>Role (Peran):</strong> Beri identitas spesifik pada AI (misal: Analis Kebijakan Ahli Muda, Kepala Bagian Administrasi Umum).</li>' .
                    '<li><strong>Context (Konteks):</strong> Jabarkan latar belakang, peserta, lokasi, dan tujuan kegiatan secara faktual.</li>' .
                    '<li><strong>Constraint (Batasan Aturan):</strong> Larang kata-kata hiperbolis, tetapkan kepatuhan EYD V, dan batasi panjang kalimat.</li>' .
                    '<li><strong>Format (Bentuk Luaran):</strong> Tentukan apakah output berupa matriks tabel, poin hierarki per nomor, atau paragraf formal.</li>' .
                    '</ul>' .

                    '<h2>CONTOH 1: Template Prompt Laporan Pertanggungjawaban (LPJ) Dinas</h2>' .
                    '<p>Berikut adalah template prompt teruji yang dapat langsung Anda salin ke ChatGPT atau Claude untuk menyusun draf laporan dinas resmi:</p>' .

                    '<div class="prompt-box">' .
                    '<div class="prompt-header"><span><i class="bi bi-file-earmark-text me-2"></i>Template Siap Salin: Draf Laporan Kegiatan</span><span>Format R-C-C-F</span></div>' .
                    'Bertindaklah sebagai Perancang Tata Naskah Dinas dan Pejabat Pelaksana Teknis Kegiatan (PPTK) di lingkungan instansi pemerintahan. ' . "\n\n" .
                    '[KONTEKS KEGIATAN]' . "\n" .
                    '- Nama Kegiatan: Bimbingan Teknis Integrasi Kecerdasan Artifisial dalam Pembelajaran Vokasi.' . "\n" .
                    '- Penyelenggara: Dinas Pendidikan berkolaborasi dengan LPK PT Aktama Digital Antika.' . "\n" .
                    '- Waktu & Tempat: 24-25 Oktober 2026, Aula Graha Teknologi.' . "\n" .
                    '- Peserta: 60 Guru Produktif SMK Bidang Teknologi Informasi dan Rekayasa Perangkat Lunak.' . "\n" .
                    '- Narasumber: Gede Erik Aktama, S.Pd., M.Pd. (Fasilitator Nasional KKA Kemdikdasmen).' . "\n" .
                    '- Hasil Evaluasi: 100% peserta berhasil merancang modul ajar digital dan lulus uji kompetensi dasar prompt engineering.' . "\n\n" .
                    '[BATASAN (CONSTRAINT)]' . "\n" .
                    '1. Gunakan Bahasa Indonesia baku sesuai Pedoman Umum Ejaan Bahasa Indonesia (EYD V).' . "\n" .
                    '2. Gaya bahasa harus lugas, formal, objektif, dan bebas dari kata-kata promosi atau hiperbolis seperti "luar biasa", "menakjubkan", atau "spektakuler".' . "\n" .
                    '3. Format draf laporan harus terstruktur dengan sistematika:' . "\n" .
                    '   A. Latar Belakang' . "\n" .
                    '   B. Maksud dan Tujuan' . "\n" .
                    '   C. Realisasi Pelaksanaan Kegiatan' . "\n" .
                    '   D. Hambatan dan Solusi Pemecahan' . "\n" .
                    '   E. Kesimpulan dan Rekomendasi Tindak Lanjut' . "\n\n" .
                    'Susun draf laporan ini secara lengkap dan komprehensif.' .
                    '</div>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-success mb-2"><i class="bi bi-eye-fill me-2"></i>Contoh Potongan Output yang Dihasilkan AI:</h6>' .
                    '<p class="mb-2"><strong>A. Latar Belakang</strong><br>' .
                    'Dalam rangka percepatan transformasi digital pada satuan pendidikan kejuruan serta penyelarasan kompetensi pendidik dengan kebutuhan industri 4.0, penguasaan teknologi Kecerdasan Artifisial (Artificial Intelligence) menjadi kompetensi yang esensial. Pelaksanaan Bimbingan Teknis ini ditujukan guna membekali tenaga pendidik vokasi dengan keterampilan teknis praktis dalam memanfaatkan generative AI secara etis dan bertanggung jawab untuk efisiensi modul ajar serta asesmen berbasis kompetensi.</p>' .
                    '<p class="mb-0"><strong>D. Hambatan dan Solusi Pemecahan</strong><br>' .
                    'Terdapat kendala fluktuasi stabilitas konektivitas internet pada sesi praktik langsung di hari pertama. Penyelenggara segera memitigasi kendala tersebut dengan mengaktifkan dedicated access point cadangan serta menyediakan modul panduan luring (offline workbook) sehingga alur bimbingan tetap berlangsung sesuai jadwal rencana kerja.</p>' .
                    '</div>' .

                    '<h2>CONTOH 2: Template Merangkum Audio Rapat Menjadi Matriks Tindak Lanjut</h2>' .
                    '<p>Seringkali sekretaris rapat kewalahan merangkum rekaman rapat 2 jam yang acak-acakan. Gunakan prompt di bawah ini:</p>' .

                    '<div class="prompt-box">' .
                    '<div class="prompt-header"><span><i class="bi bi-table me-2"></i>Template Siap Salin: Notula & Matriks Tindak Lanjut</span><span>Format Ekstraksi</span></div>' .
                    'Bertindaklah sebagai Notulis Eksekutif Senior. ' . "\n" .
                    'Berikut adalah transkrip rekaman rapat internal koordinasi tim pengembangan aplikasi. ' . "\n" .
                    'Tugas Anda:' . "\n" .
                    '1. Ekstraksi inti keputusan rapat secara objektif.' . "\n" .
                    '2. Abaikan obrolan santai, basa-basi pembuka, atau perdebatan yang tidak menghasilkan mufakat.' . "\n" .
                    '3. Buatkan MATRIKS TINDAK LANJUT dalam format TABEL dengan 5 kolom:' . "\n" .
                    '   | No | Agenda / Isu Pokok | Keputusan / Kesepakatan | Rencana Tindak Lanjut | PIC & Batas Waktu |' . "\n\n" .
                    '[TEMPELKAN TRANSKRIP AUDIO DI SINI]' .
                    '</div>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-success mb-2"><i class="bi bi-table me-2"></i>Contoh Hasil Matriks Tindak Lanjut yang Dihasilkan:</h6>' .
                    '<div class="table-responsive">' .
                    '<table class="table table-sm table-bordered bg-white mb-0">' .
                    '<thead class="table-light"><tr><th>No</th><th>Agenda / Isu Pokok</th><th>Keputusan / Kesepakatan</th><th>Rencana Tindak Lanjut</th><th>PIC & Batas Waktu</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td>1</td><td>Keamanan Portal Web Utama</td><td>Disepakati audit celah malware dan pembaruan framework Laravel 12.</td><td>Deploy patch keamanan dan isolasi file upload PPDB.</td><td>Tim IT Aktama (Deadline: 28 Okt 2026)</td></tr>' .
                    '<tr><td>2</td><td>Sertifikasi Pelatihan AI Batch 4</td><td>Pemberian nomor registrasi unik pada sertifikat fisik & digital.</td><td>Integrasi fitur QR-Code verifikasi di portal aktama.com.</td><td>Koordinator LPK (Deadline: 30 Okt 2026)</td></tr>' .
                    '</tbody></table></div></div>' .

                    '<h2>Peringatan Penting Keamanan Data (Kepatuhan UU PDP)</h2>' .
                    '<p>Saat menggunakan model AI komersial berbasis cloud publik (seperti ChatGPT Free), wajib dipatuhi protokol keselamatan informasi:</p>' .
                    '<ul>' .
                    '<li><strong>Lakukan Masking Data Sensitif:</strong> Ganti nama pegawai, NIK, NIP, nomor rekening dinas, dan nomor telepon dengan placeholder (misal: <code>[Pegawai X]</code>, <code>[Rekening Bendahara A]</code>).</li>' .
                    '<li><strong>Jangan Unggah Dokumen Rahasia Negara:</strong> Jangan mengunggah naskah rahasia atau dokumen perjanjian non-disclosure (NDA) ke server AI publik sebelum melalui proses anonimisasi.</li>' .
                    '</ul>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-laptop me-2"></i>Ingin Menguasai 50+ Template Prompt Kedinasan Lainnya?</h5>' .
                    '<p class="small text-muted mb-3">Ikuti program pelatihan intensif <strong>"AI Terapan untuk Efisiensi Administrasi Perkantoran & Sekolah"</strong> bersama LPK PT Aktama Digital Antika. Lengkap dengan sertifikat resmi ber-NIB.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Daftar Pelatihan Batch Terdekat</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(3),
                'meta_title' => 'Seni Meracik Prompt AI untuk Administrasi Perkantoran | Aktama Digital',
                'meta_description' => 'Panduan lengkap rumus prompt R-C-C-F disertai contoh siap salin untuk menyusun draf laporan dinas dan matriks notula rapat resmi.',
            ],

            // ARTIKEL 4
            [
                'slug' => 'digitalisasi-kasir-dan-stok-menyelamatkan-bisnis-coffee-shop',
                'category_id' => $catBiz->id,
                'title' => 'Stop Catat Manual: Bagaimana Digitalisasi Kasir & Manajemen Stok Menyelamatkan Margin Bisnis Coffee Shop',
                'image' => 'articles/article-coffee-erp.jpg',
                'summary' => 'Ramai pembeli di malam hari belum tentu menghasilkan laba di akhir bulan jika bahan baku bocor dan pencatatan kasir masih manual. Simak strategi integrasi Point of Sale (POS) dan kontrol HPP bahan baku kedai kopi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Setiap akhir pekan, kedai kopi Anda tampak luar biasa sibuk. Antrean pengunjung memenuhi meja bar, suara uap mesin espresso berdesis kencang, dan nota pesanan menumpuk. Namun saat tutup buku di akhir bulan, pemilik kedai kerap terkejut: <em>"Omzet tembus ratusan juta, tapi ke mana perginya saldo kas bersih?"</em></p>' .
                    '<p>Kondisi ini adalah fenomena klasik yang menimpa industri Food & Beverage (F&B) independen: <strong>Kebocoran Finansial Tak Kasat Mata (Silent Margin Bleeding)</strong>. Penyebab utamanya hampir selalu sama: pencatatan nota kasir manual dan ketiadaan sistem kontrol inventori yang terintegrasi secara otomatis.</p>' .

                    '<h2>Contoh Nyata: Simulasi HPP 1 Cup "Iced Brown Sugar Latte"</h2>' .
                    '<p>Untuk memahami di mana uang Anda menguap, mari bedah struktur Harga Pokok Penjualan (HPP) menu terlaris berikut:</p>' .

                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Komponen Bahan Baku</th><th>Standar Dosis (Resep Baku)</th><th>Biaya Satuan Bahan</th><th>HPP per Porsi</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td>Espresso (Biji Kopi House Blend)</td><td>18 gram</td><td>Rp200 / gram (Rp200.000 / kg)</td><td>Rp3.600</td></tr>' .
                    '<tr><td>Susu Fresh Pasteurisasi</td><td>150 ml</td><td>Rp22 / ml (Rp22.000 / liter)</td><td>Rp3.300</td></tr>' .
                    '<tr><td>Gula Aren Cair Organik</td><td>20 ml</td><td>Rp35 / ml (Rp35.000 / liter)</td><td>Rp700</td></tr>' .
                    '<tr><td>Packaging (Cup 16oz, Lid, Straw, Seal)</td><td>1 set lengkap</td><td>Rp900 / set</td><td>Rp900</td></tr>' .
                    '<tr class="table-info fw-bold"><td colspan="3">TOTAL HPP PRODUK PER CUP</td><td>Rp8.500</td></tr>' .
                    '<tr class="table-success fw-bold"><td colspan="3">HARGA JUAL KONSUMEN</td><td>Rp26.000</td></tr>' .
                    '<tr class="table-warning fw-bold"><td colspan="3">GROSS MARGIN (LABA KOTOR)</td><td>Rp17.500 (67,3%)</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Simulasi Kebocoran: Efek Domino "Spill" 3 Gram Biji Kopi</h2>' .
                    '<p>Jika barista Anda tidak menggunakan timbangan digital presisi dan menuang kopi tanpa kontrol sistem POS:</p>' .
                    '<ul>' .
                    '<li>Kelebihan dosis 3 gram kopi per cup x 150 cup sehari = <strong>450 gram kopi terbuang percuma setiap hari</strong>.</li>' .
                    '<li>Dalam 1 bulan (30 hari), Anda kehilangan <strong>13,5 kilogram biji kopi specialty</strong> senilai <strong>Rp2.700.000</strong> hanya dari satu bahan baku!</li>' .
                    '<li>Jika ditambah kebocoran sirup dan susu yang rusak, kerugian tak tercatat bisa mencapai <strong>Rp5.000.000 s/d Rp8.000.000 per bulan</strong>.</li>' .
                    '</ul>' .

                    '<h2>Solusi Modern: Cloud POS dengan Otomasi Bill of Materials (BOM)</h2>' .
                    '<p>Di dalam ekosistem platform <strong>Aktama Coffee Cloud POS</strong>, setiap kali kasir mencetak 1 transaksi pada tablet, sistem backend secara otomatis memotong stok gudang sebesar 18g kopi, 150ml susu, dan 1 set cup. Pada akhir shift, kasir cukup menimbang sisa stok fisik (Stock Opname). Jika terdapat selisih lebih dari batas toleransi 2%, sistem langsung memberi peringatan kepada pemilik.</p>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-dark mb-2"><i class="bi bi-cup-hot-fill me-2"></i>Kelola Bisnis Kopi Anda Bersama Aktama Coffee</h5>' .
                    '<p class="small text-muted mb-3">Unit usaha <strong>Aktama Coffee</strong> menghadirkan pasokan green beans & roast beans specialty nusantara berkualitas prima, terintegrasi dengan aplikasi manajemen kasir dan inventori modern.</p>' .
                    '<a href="/kopi" class="btn btn-sm btn-dark rounded-pill px-3">Jelajahi Ekosistem Aktama Coffee</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(5),
                'meta_title' => 'Digitalisasi Kasir & Manajemen Stok Kedai Kopi | Aktama Digital',
                'meta_description' => 'Simulasi detail HPP, analisis kebocoran bahan baku coffee shop, dan solusi integrasi Point of Sale untuk mengamankan margin bisnis F&B.',
            ],

            // ARTIKEL 5
            [
                'slug' => 'revolusi-undangan-digital-hemat-biaya-mewah-elegan',
                'category_id' => $catBiz->id,
                'title' => 'Revolusi Undangan Digital: Hemat Biaya Cetak Hingga 80% Tanpa Kehilangan Kesan Sakral dan Mewah',
                'image' => 'articles/article-undangan-digital.jpg',
                'summary' => 'Mencetak ratusan fisik kartu undangan tidak hanya menguras anggaran pernikahan, namun sering terbuang sia-sia. Undangan digital berbasis web interaktif menghadirkan pengalaman visual sinematik dengan fitur RSVP dan navigasi presisi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Mempersiapkan hari pernikahan impian seringkali membuat calon mempelai dan keluarga pusing mengatur alokasi anggaran. Salah satu pos pengeluaran yang kerap membebani adalah percetakan ratusan lembar kartu undangan fisik yang setelah acara selesai, nyaris 95% di antaranya berakhir di tempat sampah.</p>' .
                    '<p>Kehadiran <strong>Undangan Pernikahan Digital Berbasis Website Interaktif</strong> mentransformasikan tradisi ini. Bukan sekadar mengirim gambar poster statis di grup obrolan, melainkan sebuah portal multimedia eksklusif dengan nama tamu personal, musik latar sinematik, peta lokasi interaktif, dan konfirmasi kehadiran (RSVP) otomatis.</p>' .

                    '<h2>Tabel Perbandingan Riil: Cetak Kartu Fisik vs Undangan Digital SaaS</h2>' .
                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Parameter Perbandingan</th><th>Undangan Kertas Fisik (500 Lembar)</th><th>Undangan Digital Website (Aktama)</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Estimasi Total Biaya</strong></td><td>Rp3.500.000 s/d Rp6.000.000 (cetak + finishing foil)</td><td><strong>Rp150.000 s/d Rp300.000 (Paket Lengkap)</strong></td></tr>' .
                    '<tr><td><strong>Biaya Pengiriman & Logistik</strong></td><td>Rp500.000 s/d Rp1.000.000 (ongkos kirim / bensin antar)</td><td><strong>Rp0 (Cukup bagikan link via WhatsApp)</strong></td></tr>' .
                    '<tr><td><strong>Batas Jumlah Tamu</strong></td><td>Terbatas sesuai jumlah lembar yang dicetak</td><td><strong>Tanpa Batas (Unlimited Tamu)</strong></td></tr>' .
                    '<tr><td><strong>Akurasi Lokasi Acara</strong></td><td>Denah garis statis sering membingungkan tamu</td><td><strong>Tombol Google Maps Real-Time Navigasi GPS</strong></td></tr>' .
                    '<tr><td><strong>Manajemen Porsi Katering</strong></td><td>Menebak-nebak, risiko makanan berlebih/kurang</td><td><strong>Fitur RSVP Otomatis (Tahu persis siapa yang hadir)</strong></td></tr>' .
                    '<tr><td><strong>Pemberian Tanda Kasih</strong></td><td>Harus hadir langsung ke kotak amplop fisik</td><td><strong>Integrasi Amplop Digital QRIS & Transfer Bank</strong></td></tr>' .
                    '<tr class="table-success fw-bold"><td colspan="2">TOTAL PENGHEMATAN BIAYA</td><td>HEMAT HINGGA RP4.500.000+ (Dapat dialihkan ke katering!)</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Contoh Template Pesan WhatsApp Sebar Undangan yang Elegan & Beradab</h2>' .
                    '<p>Agar pembagian undangan website tidak terkesan seperti pesan siaran (broadcast) yang kaku, gunakan format copywriting santun berikut:</p>' .

                    '<div class="prompt-box">' .
                    '<div class="prompt-header"><span><i class="bi bi-whatsapp me-2"></i>Contoh Template WhatsApp Sebar Undangan</span><span>Adab & Kesantunan</span></div>' .
                    'Bismillahirrohmanirrohim' . "\n" .
                    'Assalamu’alaikum Warahmatullahi Wabarakatuh / Salam Sejahtera,' . "\n\n" .
                    'Kepada Yth.' . "\n" .
                    'Bapak/Ibu/Sahabat: *[Nama Tamu Undangan]*' . "\n" .
                    'di Tempat' . "\n\n" .
                    'Tanpa mengurangi rasa hormat, sehubungan dengan keterbatasan jarak dan waktu untuk bersilaturahmi secara langsung, perkenankan kami mengundang Bapak/Ibu/Sahabat untuk hadir dan memberikan doa restu pada momen sakral pernikahan kami:' . "\n\n" .
                    '🤵 *[Nama Mempelai Pria]*' . "\n" .
                    '&' . "\n" .
                    '👰 *[Nama Mempelai Wanita]*' . "\n\n" .
                    'Informasi detail mengenai rangkaian acara, galeri foto, peta lokasi, serta konfirmasi kehadiran (RSVP) dapat diakses melalui tautan undangan resmi kami berikut ini:' . "\n" .
                    '👉 *https://undangan.aktama.com/to/[slug-nama-tamu]*' . "\n\n" .
                    'Merupakan suatu kehormatan dan kebahagiaan yang mendalam bagi kami apabila Bapak/Ibu/Sahabat berkenan hadir memberikan doa restu.' . "\n\n" .
                    'Atas perhatian dan doa tulusnya, kami haturkan terima kasih yang sebesar-besarnya.' . "\n" .
                    'Wassalamu’alaikum Warahmatullahi Wabarakatuh.' .
                    '</div>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-danger mb-2"><i class="bi bi-heart-fill me-2"></i>Pilih Desain Impian Anda di Undangan Online Aktama</h5>' .
                    '<p class="small text-muted mb-3">Tersedia puluhan tema mewah bernuansa adat nusantara (Jawa, Bali, Minang, Sunda) hingga gaya modern floral minimalis yang ringan dan cepat dibuka di ponsel.</p>' .
                    '<a href="https://undangan.aktama.com" target="_blank" class="btn btn-sm btn-danger rounded-pill px-3">Buka Katalog Undangan Online ↗</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(7),
                'meta_title' => 'Revolusi Undangan Pernikahan Digital Mewah dan Hemat | Aktama Digital',
                'meta_description' => 'Tabel perbandingan biaya cetak vs undangan digital, fitur RSVP otomatis, dan contoh template WhatsApp sebar undangan yang sopan.',
            ],

            // ARTIKEL 6
            [
                'slug' => 'mengapa-berpikir-komputasional-harus-dikenalkan-sejak-dini',
                'category_id' => $catEdu->id,
                'title' => 'Mengapa Berpikir Komputasional dan Koding Harus Dikenalkan Sejak Jenjang Sekolah Menengah?',
                'image' => 'articles/article-coding-education.jpg',
                'summary' => 'Koding bukan sekadar menghafal sintaks bahasa pemrograman, melainkan melatih nalar dekomposisi, pengenalan pola, dan abstraksi logis dalam memecahkan masalah kompleks kehidupan nyata.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Ketika mendengar istilah "pembelajaran koding di sekolah", banyak pendidik dan orang tua masih merasa gentar, membayangkan anak-anak SMP atau SMA dipaksa menghafal barisan teks bahasa C++ atau Python yang membingungkan.</p>' .
                    '<p>Padahal, esensi sejati dari literasi komputasi abad ke-21 bukanlah menghafal titik koma sintaks, melainkan menumbuhkan <strong>Computational Thinking (Berpikir Komputasional)</strong>: sebuah metode pemecahan masalah yang sistematis, terstruktur, dan terukur dalam menghadapi persoalan nyata.</p>' .

                    '<h2>Empat Pilar Logika Komputasional</h2>' .
                    '<ol>' .
                    '<li><strong>Dekomposisi (Decomposition):</strong> Kemampuan memecah masalah besar yang kompleks menjadi serangkaian sub-masalah kecil yang mudah dipecahkan satu demi satu.</li>' .
                    '<li><strong>Pengenalan Pola (Pattern Recognition):</strong> Menemukan kemiripan atau tren dari pengalaman masa lalu untuk merumuskan solusi saat ini lebih cepat.</li>' .
                    '<li><strong>Abstraksi (Abstraction):</strong> Memilah mana variabel yang krusial dan mengabaikan detail yang tidak relevan agar tidak tersesat dalam kebingungan.</li>' .
                    '<li><strong>Perancangan Algoritma (Algorithm Design):</strong> Menyusun urutan langkah-langkah logis yang dapat diulang oleh siapa pun untuk memperoleh hasil yang sama persis.</li>' .
                    '</ol>' .

                    '<h2>Contoh Praktik di Kelas Tanpa Komputer: Simulasi "Robot Logika"</h2>' .
                    '<p>Dalam pelatihan guru yang dibawakan oleh <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong> sebagai Fasilitator Nasional Koding dan Kecerdasan Artifisial (KKA) Kemdikdasmen, diajarkan metode <em>Unplugged Computing</em> (belajar logika komputasi tanpa layar komputer):</p>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-primary mb-2"><i class="bi bi-controller me-2"></i>Aktivitas Kelas: "Instruksi Robot Pembuat Teh Manis"</h6>' .
                    '<p class="small text-muted mb-2">Guru bertindak sebagai Robot yang hanya memahami perintah harfiah (literal). Siswa menulis instruksi di secarik kertas:</p>' .
                    '<ul class="small mb-0">' .
                    '<li><strong>Jika siswa menulis:</strong> <em>"Masukkan gula ke cangkir"</em> $\rightarrow$ Robot memasukkan toples gula utuh bersama wadahnya ke dalam cangkir (karena tidak ada perintah membuka tutup toples dan menyendok).</li>' .
                    '<li><strong>Pelajaran Berharga:</strong> Siswa seketika tersadar bahwa komputer tidak memiliki asumsi akal sehat. Setiap langkah harus dirumuskan secara presisi, urut, dan bebas dari ambiguitas logika.</li>' .
                    '</ul>' .
                    '</div>' .

                    '<p>Siswa yang terlatih berpikir secara komputasional memiliki ketahanan mental (<em>grit</em>) yang jauh lebih tinggi. Ketika mereka menemui kegagalan pada pelajaran matematika, fisika, atau kehidupan sehari-hari, mereka tidak mudah putus asa, melainkan segera melakukan proses <strong>Debugging</strong>: mencari di langkah mana kesalahan logika terjadi dan segera memperbaikinya.</p>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-code-slash me-2"></i>Buka Ekstrakurikuler Koding & AI di Sekolah Anda</h5>' .
                    '<p class="small text-muted mb-3">LPK PT Aktama Digital Antika bermitra dengan sekolah-sekolah di seluruh Nusantara untuk penyusunan silabus kurikulum koding, bimbingan guru pembina, dan sertifikasi kompetensi siswa.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Konsultasikan Kurikulum Koding Sekolah</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(9),
                'meta_title' => 'Mengapa Berpikir Komputasional Harus Dikenalkan Sejak Dini | Aktama Digital',
                'meta_description' => 'Konsep 4 pilar computational thinking, contoh aktivitas belajar logika tanpa komputer, dan manfaat jangka panjang bagi siswa sekolah.',
            ],

            // ARTIKEL 7
            [
                'slug' => 'website-custom-vs-template-murahan-biaya-dan-performa',
                'category_id' => $catWeb->id,
                'title' => 'Memilih Website untuk Bisnis: Mengapa Template Murahan Seringkali Berakhir dengan Biaya yang Jauh Lebih Mahal',
                'image' => 'articles/article-web-architecture.jpg',
                'summary' => 'Tergiur jasa bikin website instan seharga ratusan ribu? Pelajari risiko tersembunyi seperti lambatnya loading, keterbatasan integrasi database, dan celah keamanan yang justru melipatgandakan biaya perawatan di masa depan.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Iklan di platform media sosial begitu gencar menawarkan promosi yang tampak sangat menggoda: <em>"Jasa Bikin Website Perusahaan Hanya Rp300.000, Siap Pakai dalam 2 Jam!"</em>. Bagi pengusaha yang sedang menghemat modal, tawaran ini tentu tampak seperti kesepakatan terbaik.</p>' .
                    '<p>Namun, dalam dunia teknologi rekayasa web berlaku hukum universal yang tak pernah meleset: <strong>"Bila Anda membayar sangat murah di awal, Anda akan membayar berkali-kali lipat lebih mahal untuk menambal kerusakannya di kemudian hari."</strong></p>' .

                    '<h2>Data Audit Teknis Riil: Template Instan vs Rekayasa Custom Laravel</h2>' .
                    '<p>Berikut adalah perbandingan hasil audit Google Core Web Vitals antara template murah berbasis CMS instan dengan sistem kustom Laravel yang dikembangkan oleh PT Aktama Digital Antika:</p>' .

                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Indikator Kinerja Google</th><th>Website Template Murahan</th><th>Website Custom Laravel Aktama</th><th>Dampak terhadap Bisnis</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Skor Kecepatan Mobile (PageSpeed)</strong></td><td class="text-danger fw-bold">28 / 100 (Sangat Buruk)</td><td class="text-success fw-bold">96 / 100 (Optimal)</td><td>Google menurunkan ranking situs yang memiliki skor di bawah 50.</td></tr>' .
                    '<tr><td><strong>Total Waktu Muat (Page Load Time)</strong></td><td class="text-danger">7,8 s/d 11,2 Detik</td><td class="text-success"><strong>0,8 s/d 1,4 Detik</strong></td><td>Riset Google: 53% pengunjung meninggalkan web jika waktu loading > 3 detik.</td></tr>' .
                    '<tr><td><strong>Ukuran File yang Diunduh (Payload)</strong></td><td class="text-danger">5,4 MB (Penuh CSS/JS sampah)</td><td class="text-success"><strong>320 KB (Sangat Ringan)</strong></td><td>Menghemat kuota internet pengunjung dan hemat resource hosting server.</td></tr>' .
                    '<tr><td><strong>Stabilitas Update Jangka Panjang</strong></td><td class="text-danger">Sering rusak saat versi PHP server naik</td><td class="text-success"><strong>Stabil, terdokumentasi, scalable</strong></td><td>Tidak ada biaya tebusan tak terduga untuk merestorasi situs rusak.</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Kalkulasi Kerugian Finansial: Penurunan Konversi 7% per Detik</h2>' .
                    '<p>Riset analitik dari Amazon dan Akamai membuktikan bahwa <strong>setiap keterlambatan 1 detik waktu loading halaman mengakibatkan penurunan konversi penjualan sebesar 7%</strong>. Jika bisnis Anda menargetkan penjualan Rp50.000.000 per bulan melalui website, keterlambatan loading 4 detik akibat template yang lambat berpotensi melenyapkan potensi omzet sebesar <strong>Rp14.000.000 setiap bulannya</strong>!</p>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-success mb-2"><i class="bi bi-laptop me-2"></i>Bangun Aset Digital Perusahaan yang Tahan Lama</h5>' .
                    '<p class="small text-muted mb-3">PT Aktama Digital Antika merancang arsitektur website dan aplikasi bisnis modern berbasis Laravel dengan jaminan performa tinggi, bebas script judol, dan teroptimasi SEO mesin pencari.</p>' .
                    '<a href="/jasa-website" class="btn btn-sm btn-success rounded-pill px-3">Lihat Paket Pembuatan Website Profesional</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(12),
                'meta_title' => 'Website Custom vs Template Murahan untuk Bisnis | Aktama Digital',
                'meta_description' => 'Analisis data benchmark Core Web Vitals, risiko tersembunyi template instan, dan pentingnya arsitektur Laravel kustom untuk investasi bisnis.',
            ],

            // ARTIKEL 8
            [
                'slug' => 'peluang-bisnis-micro-saas-dan-lisensi-source-code',
                'category_id' => $catBiz->id,
                'title' => 'Peluang Bisnis Micro-SaaS dan Lisensi Source Code: Cara Developer Menghasilkan Omzet Berkelanjutan',
                'image' => 'articles/article-digital-products.jpg',
                'summary' => 'Berhenti menukar waktu dengan uang secara linier. Membangun modul perangkat lunak siap pakai, template aplikasi Laravel, dan lisensi produk digital membuka pintu pendapatan pasif skala nasional bagi talenta digital.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Banyak software engineer dan talenta teknologi berbakat terjebak dalam siklus kelelahan jasa pesanan (<em>freelance burnout</em>). Mereka menghabiskan 14 jam sehari di depan monitor untuk menyelesaikan proyek satu klien, namun begitu pekerjaan rampung, pendapatan pun seketika terhenti.</p>' .
                    '<p>Paradigma bisnis perangkat lunak telah bergeser ke arah <strong>Micro-SaaS</strong> dan <strong>Digital Product Licensing</strong>. Alih-alih menjual jam kerja Anda yang terbatas pada 24 jam sehari, buatlah produk perangkat lunak bernilai guna tinggi sekali, lalu jual lisensi hak pakainya kepada ratusan pembeli secara berulang.</p>' .

                    '<h2>Studi Kasus Finansial: Menjual 1 Modul Starter Kit Aplikasi</h2>' .
                    '<p>Mari kita hitung potensi pendapatan nyata dari membangun satu template sistem informasi siap pakai (contoh: Sistem Manajemen Kasir / Starter Kit E-Commerce):</p>' .

                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Paket Lisensi yang Ditawarkan</th><th>Harga per Lisensi</th><th>Volume Penjualan (6 Bulan)</th><th>Total Pendapatan Bersih</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td><strong>Lisensi Standar (Single Domain)</strong><br><span class="text-muted">Untuk pemilik bisnis perorangan atau UMKM</span></td><td>Rp350.000</td><td>120 Lisensi Terjual</td><td>Rp42.000.000</td></tr>' .
                    '<tr><td><strong>Lisensi Developer (Unlimited Domain)</strong><br><span class="text-muted">Untuk agensi IT & freelancer pembuat web klien</span></td><td>Rp1.750.000</td><td>18 Lisensi Terjual</td><td>Rp31.500.000</td></tr>' .
                    '<tr class="table-success fw-bold"><td colspan="3">TOTAL OMZET PENJUALAN PRODUK DIGITAL</td><td>Rp73.500.000</td></tr>' .
                    '<tr class="table-info"><td colspan="3">BIAYA OPERASIONAL SERVER (VPS 6 Bulan)</td><td>Rp900.000</td></tr>' .
                    '<tr class="table-primary fw-bold"><td colspan="3">MARGIN KEUNTUNGAN BERSIH (NET PROFIT)</td><td>Rp72.600.000 (98,7%)</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Tiga Pilar Utama Sukses Toko Produk Digital Mandiri</h2>' .
                    '<ol>' .
                    '<li><strong>Payment Gateway Otomatis Tanpa Konfirmasi Manual:</strong> Integrasi dengan penyedia lokal (seperti Midtrans atau Tripay) memastikan pembeli menerima lisensi dan link download detik itu juga saat transfer QRIS atau Virtual Account berhasil.</li>' .
                    '<li><strong>Sistem Validasi Lisensi Kriptografis:</strong> Menggunakan tanda tangan kunci digital (Digital Signature) untuk melindungi karya dari pembajakan ilegal.</li>' .
                    '<li><strong>Dokumentasi Instalasi yang Sangat Jelas:</strong> Panduan video dan langkah-langkah tertulis yang mudah dipahami memangkas waktu melayani komplain teknis hingga 90%.</li>' .
                    '</ol>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-dark mb-2"><i class="bi bi-box-seam me-2"></i>Dapatkan Script & Modul Aplikasi Berkualitas</h5>' .
                    '<p class="small text-muted mb-3">Jelajahi etalase produk digital, template web Laravel, dan source code teruji yang dikembangkan oleh PT Aktama Digital Antika untuk mempercepat penyelesaian proyek bisnis Anda.</p>' .
                    '<a href="/portofolio" class="btn btn-sm btn-dark rounded-pill px-3">Buka Portofolio Solusi Digital</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(15),
                'meta_title' => 'Peluang Bisnis Micro-SaaS & Lisensi Source Code | Aktama Digital',
                'meta_description' => 'Strategi monetisasi produk digital bagi software engineer, simulasi omzet penjualan lisensi source code, dan otomasi payment gateway.',
            ],

            // ARTIKEL 9
            [
                'slug' => 'nilai-strategis-sertifikat-pelatihan-resmi-lpk-dalam-karier',
                'category_id' => $catEdu->id,
                'title' => 'Nilai Strategis Sertifikat Pelatihan Resmi Berlisensi NIB & LPK dalam Portofolio Karier Profesional',
                'image' => 'articles/article-lpk-certification.jpg',
                'summary' => 'Di tengah banjirnya sertifikat webinar gratis, dokumen kelulusan resmi dari Lembaga Pelatihan Kerja (LPK) berbadan hukum memiliki kekuatan pembuktian hukum dan kompetensi yang diakui instansi pemerintah dan industri.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Di era pasca-pandemi, hampir setiap orang memiliki puluhan lembar sertifikat digital seminar daring gratisan berdurasi 1 atau 2 jam yang menumpuk di folder laptop. Namun saat dokumen tersebut diajukan untuk kenaikan pangkat jabatan fungsional ASN/PPPK, angka kredit guru/dosen, atau rekrutmen perusahaan multinasional, sertifikat tersebut kerap <strong>ditolak atau tidak dinilai</strong>.</p>' .
                    '<p>Tim penilai kepegawaian dan HRD profesional sangat memahami regulasi: sebuah webinar partisipasi tanpa uji kompetensi dan tanpa legalitas izin lembaga pelatihan resmi tidak dapat dijadikan bukti kapabilitas kerja nyata.</p>' .

                    '<h2>Contoh Struktur Transkrip Pelatihan Resmi 32 Jam Pelajaran (JP)</h2>' .
                    '<p>Berikut adalah standar matriks kompetensi yang tertera di lembar belakang sertifikat resmi kelulusan <strong>LPK PT Aktama Digital Antika</strong>:</p>' .

                    '<div class="table-responsive my-3">' .
                    '<table class="table table-bordered small bg-white">' .
                    '<thead class="table-light"><tr><th>Kode Unit Pelatihan</th><th>Materi & Unit Kompetensi</th><th>Jam Teori</th><th>Jam Praktik Mandiri</th><th>Bobot JP</th></tr></thead>' .
                    '<tbody>' .
                    '<tr><td>AKT-AI-01</td><td>Dasar Arsitektur LLM & Etika Privasi Data (UU PDP)</td><td>3 JP</td><td>3 JP</td><td>6 JP</td></tr>' .
                    '<tr><td>AKT-AI-02</td><td>Prompt Engineering Tingkat Lanjut (Metode R-C-C-F)</td><td>4 JP</td><td>6 JP</td><td>10 JP</td></tr>' .
                    '<tr><td>AKT-AI-03</td><td>Otomasi Pembuatan Modul Ajar & Administrasi Dinas</td><td>3 JP</td><td>5 JP</td><td>8 JP</td></tr>' .
                    '<tr><td>AKT-AI-04</td><td>Uji Praktik Proyek Akhir (Evaluasi Portofolio Mandiri)</td><td>2 JP</td><td>6 JP</td><td>8 JP</td></tr>' .
                    '<tr class="table-primary fw-bold"><td colspan="4">TOTAL BOBOT JAM PELAJARAN SERTIFIKAT RESMI</td><td>32 JP</td></tr>' .
                    '</tbody></table></div>' .

                    '<h2>Tiga Indikator Keabsahan Sertifikat yang Diakui Regulator</h2>' .
                    '<ol>' .
                    '<li><strong>Badan Hukum Penyelenggara Resmi (NIB: 1703250057018):</strong> Penyelenggara wajib berbadan hukum Perseroan Terbatas (PT) dengan izin klasifikasi Lembaga Pelatihan Kerja (LPK) yang terdaftar di sistem perizinan berusaha kementerian.</li>' .
                    '<li><strong>QR-Code Verifikasi Keaslian Online:</strong> Setiap sertifikat memiliki tautan unik di mana pihak HRD atau asesor dapat memindai barcode untuk memvalidasi tanggal kelulusan dan nilai peserta langsung dari server Aktama.</li>' .
                    '<li><strong>Tanda Tangan Instruktur Berkompeten:</strong> Ditandatangani langsung oleh instruktur bereputasi akademik resmi (Founder Gede Erik Aktama, S.Pd., M.Pd. - Dosen & Fasilitator Nasional Kemdikdasmen).</li>' .
                    '</ol>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-primary mb-2"><i class="bi bi-award-fill me-2"></i>Dapatkan Sertifikat Kompetensi Berbobot untuk Karier Anda</h5>' .
                    '<p class="small text-muted mb-3">Tingkatkan skor portofolio karier Anda dengan mengikuti program pelatihan resmi LPK Aktama Digital Antika. Pilihan kelas online interaktif dan workshop offline tersedia.</p>' .
                    '<a href="/pelatihan-ai" class="btn btn-sm btn-primary rounded-pill px-3">Lihat Jadwal Pelatihan & Sertifikasi</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(18),
                'meta_title' => 'Nilai Strategis Sertifikat Pelatihan Resmi LPK | Aktama Digital',
                'meta_description' => 'Standar matriks silabus 32 JP pelatihan resmi LPK Aktama, pentingnya legalitas NIB, dan QR Code verifikasi online untuk portofolio karier.',
            ],

            // ARTIKEL 10
            [
                'slug' => 'dari-ruang-riset-ke-industri-integrasi-penelitian-akademik',
                'category_id' => $catRes->id,
                'title' => 'Dari Ruang Riset ke Industri: Mengintegrasikan Penelitian Akademik dengan Solusi Nyata Masyarakat',
                'image' => 'articles/article-academic-research.jpg',
                'summary' => 'Menjembatani jurang pemisah antara paper ilmiah di kampus dan kebutuhan teknologi di lapangan. Bagaimana riset komputasi terindeks SINTA ditransformasikan menjadi produk perangkat lunak bernilai ekonomi.',
                'content' => '<p class="lead fw-medium text-dark mb-4">Sebuah ironi yang sering menjadi perbincangan di dunia pendidikan tinggi tanah air adalah sindrom "Menara Gading" (<em>Ivory Tower</em>): para akademisi menerbitkan ratusan makalah ilmiah bereputasi, namun kajian tersebut hanya berhenti di rak arsip perpustakaan tanpa pernah dirasakan manfaatnya oleh pelaku usaha mikro dan masyarakat di lapangan.</p>' .
                    '<p><strong>PT Aktama Digital Antika</strong> didirikan dengan misi fundamental untuk meruntuhkan sekat pemisah tersebut. Kami meyakini bahwa riset rekayasa sistem komputasi terbaik adalah riset yang mampu menjawab persoalan riil dan mentransformasikannya menjadi solusi teknologi yang berdaya saing komersial.</p>' .

                    '<h2>Studi Kasus: Dari Publikasi SINTA Menuju Ekosistem Aktama Coffee</h2>' .
                    '<p>Sebagai gambaran konkret bagaimana hilirisasi riset diimplementasikan di bawah kepemimpinan <strong>Gede Erik Aktama, S.Pd., M.Pd.</strong> (Dosen & Kaprodi Sistem Komputer Universitas Parna Raya):</p>' .

                    '<div class="output-box">' .
                    '<h6 class="fw-bold text-info mb-2"><i class="bi bi-cpu-fill me-2"></i>Hilirisasi Riset: Smart Farming IoT ke Aplikasi Real-World</h6>' .
                    '<ul class="small mb-0">' .
                    '<li><strong>Tahap 1 (Riset Ilmiah Murni):</strong> Publikasi pada jurnal nasional terakreditasi SINTA 4 & SINTA 5 mengenai kalibrasi sensor suhu, kelembaban udara (DHT22), dan kelembaban tanah kapasitif berbasis mikrokontroler ESP32.</li>' .
                    '<li><strong>Tahap 2 (Uji Laboratorium & Validasi):</strong> Menguji akurasi algoritma pengiriman data telemetri nirkabel pada gudang penyimpanan biji kopi specialty grade guna mencegah jamur pascapanen.</li>' .
                    '<li><strong>Tahap 3 (Implementasi Industri Nyata):</strong> Hasil pengujian diintegrasikan langsung ke dalam dashboard monitoring gudang unit usaha <strong>Aktama Coffee</strong> (<a href="https://coffee.aktama.com" target="_blank">coffee.aktama.com</a>), memastikan kualitas biji kopi pelanggan senantiasa terjaga pada standar internasional.</li>' .
                    '</ul>' .
                    '</div>' .

                    '<h2>Model Kolaborasi Quadruple Helix yang Mandiri</h2>' .
                    '<p>Dengan menyatukan 4 pilar (Akademisi kampus, Pelaku industri bisnis, Komunitas pengguna, dan Kerangka regulasi pemerintah), ekosistem Aktama membuktikan bahwa perusahaan teknologi lokal di Indonesia mampu bertumbuh secara organik, berbasis integritas keilmuan, dan menghadirkan dampak nyata bagi kemandirian ekonomi digital bangsa.</p>' .

                    '<div class="callout-card my-4">' .
                    '<h5 class="fw-bold text-info mb-2"><i class="bi bi-mortarboard me-2"></i>Eksplorasi Profil Akademik & Publikasi SINTA Founder</h5>' .
                    '<p class="small text-muted mb-3">Untuk meninjau rekam jejak riset, publikasi jurnal terakreditasi, dan program pengabdian kepada masyarakat, silakan kunjungi portal portofolio resmi.</p>' .
                    '<a href="https://profil.aktama.com" target="_blank" class="btn btn-sm btn-info text-white rounded-pill px-3">Kunjungi profil.aktama.com ↗</a>' .
                    '</div>',
                'author' => $authorName,
                'status' => 'published',
                'published_at' => now()->subDays(21),
                'meta_title' => 'Dari Riset SINTA ke Industri Teknologi | Aktama Digital',
                'meta_description' => 'Hilirisasi publikasi ilmiah SINTA dan rekayasa mikrokontroler IoT menjadi solusi nyata pada ekosistem PT Aktama Digital Antika.',
            ],
        ];

        // 3. Masukkan ke Database
        foreach ($articles as $artData) {
            Article::updateOrCreate(['slug' => $artData['slug']], $artData);
        }
    }
}
