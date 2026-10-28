"""
Modul Naskah Bab IV Kelas XII SMA/SMK (Fase F Akhir)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB4_SMA12 = """# BAB IV: PROYEK AKHIR TERPADU (CAPSTONE PROJECT): SISTEM AI HUMAN-CENTERED

## APERSEPSI: MENJAWAB HARAPAN WARGA DENGAN KARYA INOVASI TERPADU

Balai Desa Ranowangko siang itu dipenuhi perwakilan kelompok tani cabai dan pengurus koperasi perikanan lokal. Di bagian depan ruangan, Arya, Dinda, dan Bagas sedang menyiapkan sebuah meja pameran mini yang memuat sebuah kotak perangkat keras pemantau fisik, laptop peladen backend, serta tablet yang menampilkan antarmuka dasbor ramah pengguna. Kepala Desa dan beberapa tokoh masyarakat duduk melingkari meja tersebut dengan pandangan penuh harap.

[GAMBAR: assets/bab4_komik_pembuka_sma12.png]

"Adik-adik siswa SMA/SMK yang terhormat," buka Pak Rondonuwu, Ketua Kelompok Tani setempat. "Selama puluhan tahun, kami para petani sering terlambat mendeteksi serangan hama busuk daun pada tanaman cabai. Ketika daun mulai menguning, obat semprot seringkali sudah tidak mempan dan kami merugi hingga puluhan juta rupiah. Apakah alat canggih yang kalian buat ini benar-benar bisa membantu kami orang desa yang tidak mengerti istilah komputer rumit ini?"

Dinda menyambut pertanyaan tersebut dengan senyum hangat dan sikap takzim. "Bapak dan Ibu sekalian, alat ini kami bangun khusus dengan pendekatan **Kecerdasan Artifisial Berpusat pada Manusia (*Human-Centered AI*)**. Kami tidak menciptakan teknologi untuk menggantikan kearifan Bapak-Ibu sebagai petani, melainkan sebagai asisten pendamping setia di ladang."

Bagas kemudian mengambil sebuah daun cabai yang memiliki bercak penyakit dan mengarahkannya ke depan kamera modul sirkuit IoT buatannya. Hanya dalam tempo 0,8 detik, layar tablet dipegang Pak Rondonuwu berbunyi lembut dan menampilkan tulisan berbahasa Indonesia yang jelas: *Peringatan Dini: Gejala Awal Hawar Daun Terdeteksi (Keyakinan AI 94%). Rekomendasi Tindakan: Pangkas ranting terdampak dan semprotkan fungisida organik dosis ringan.*

Pak Rondonuwu tertegun takjub, sementara para petani lainnya bertepuk tangan riuh. "Luar biasa! Ini sangat mudah dimengerti, bahkan oleh kami yang sudah sepuh!"

Arya menambahkan kepada seluruh hadirin, "Sistem ini merupakan **Proyek Terpadu Multi-Lapisan (*Integrated Capstone Project*)**. Perangkat sensor IoT di ladang mengirimkan data melalui protokol MQTT hemat daya, model Deep Learning di peladen menganalisis foto daun, basis data mencatat riwayat sebaran penyakit di desa, dan antarmukanya dirancang sangat sederhana agar langsung memberi solusi nyata bagi kesejahteraan warga."

"Inilah esensi sejati dari puncak kompetensi koding dan AI tingkat menengah," bisik Dinda bangga kepada Arya dan Bagas. "Ilmu pengetahuan kita bukan sekadar nilai di rapor, melainkan karya nyata yang menyalakan harapan masyarakat luas!"

---

## A. INISIASI PROYEK SOLUTIF BERBASIS MASALAH RIIL MITRA

Proyek Akhir Terpadu (*Capstone Project*) pada Fase F Akhir Kelas XII merupakan kulminasi dari seluruh perjalanan akademis peserta didik. Proyek ini tidak dimulai dari kode pemrograman di depan komputer, melainkan berakar dari interaksi langsung di lapangan untuk memecahkan persoalan mitra nyata (*Community-Engaged Engineering*).

### 1. Tahapan Empati dan Wawancara Pemetaan Masalah (Pain Points)
Metodologi perancangan produk cerdas berpusat pada manusia (*Human-Centered Design*) menuntut tahapan empati yang mendalam:
1. **Identifikasi Mitra Strategis:** Memilih mitra nyata di sekitar lingkungan sekolah, seperti UMKM pengolahan hasil laut, kelompok tani hidroponik, puskesmas pembantu desa, perpustakaan komunitas, atau koperasi sekolah.
2. **Wawancara Kontekstual (*Contextual Inquiry*):** Mendengarkan keluhan langsung pengguna (*Pain Points*), mengamati rutinitas harian mereka, dan mencatat batasan operasional (misal: keterbatasan sinyal internet di sawah, pengguna yang belum terbiasa dengan gawai pintar, atau keterbatasan anggaran listrik).
3. **Penyusunan Pernyataan Masalah (*Problem Statement*):** Merumuskan tantangan spesifik menggunakan kerangka *How Might We (Bagaimana Kita Dapat)*:
   *Contoh:* "Bagaimana kita dapat membantu petani cabai desa mendeteksi penyakit tanaman secara mandiri dan cepat, tanpa bergantung pada koneksi internet berkecepatan tinggi, serta menyajikan instruksi pengobatan dalam bahasa yang mudah dipahami?"

---

## B. REKAYASA SISTEM MULTI-LAPISAN TERPADU

Sistem cerdas kelas industri tidak pernah berdiri sendiri sebagai skrip tunggal. Sistem terintegrasi dibangun atas empat lapisan arsitektur modular yang saling terhubung:

[GAMBAR: assets/bab4_arsitektur_sistem_terintegrasi_capstone.png]

### 1. Lapisan 1: Antarmuka Pengguna (User Interface / Client Tier)
Merupakan kanal interaksi antara pengguna manusia dan sistem perangkat lunak:
- **Aplikasi Web / Seluler:** Antarmuka visual yang dibangun menggunakan teknologi modern (seperti HTML5/Vanilla CSS/JavaScript, Flutter, atau React).
- **Dasbor Pemantauan Real-Time:** Menampilkan grafik telemetri sensor, notifikasi darurat, dan panel intervensi manual pengambil keputusan.
- **Prinsip Human-Centered UI:** Tata letak bersih, tipografi kontras tinggi, tombol aksi yang tegas (*Call to Action*), dan minim jargon teknis rumit.

### 2. Lapisan 2: Peladen Backend dan REST API (Service Tier)
Merupakan pusat lalu lintas data dan logika bisnis aplikasi. Peladen backend (misal menggunakan Python FastAPI atau Flask) menyediakan titik akhir (*endpoints*) layanan:
- Menerima paket data telemetri dari perangkat sensor lapangan via protokol HTTP/MQTT.
- Melakukan verifikasi keamanan token otentikasi (JWT) dan sanitasi data masukan guna mencegah serangan peretasan (seperti *SQL Injection*).
- Menghubungkan antarmuka pengguna dengan mesin kecerdasan artifisial dan basis data penyimpanan.

### 3. Lapisan 3: Mesin Kecerdasan Artifisial (AI / Inference Engine)
Jantung pemrosesan kognitif sistem:
- Menjalankan inferensi model (seperti model klasifikasi Deep Learning CNN atau model klastering K-Means) terhadap data yang dikirimkan oleh backend.
- Menghitung skor keyakinan (*confidence score*) dari prediksi. Jika tingkat keyakinan model berada di bawah ambang batas aman (misal kurang dari 75%), sistem secara otomatis mengaktifkan mekanisme peringatan ketidakpastian.

### 4. Lapisan 4: Penyimpanan Basis Data (Data Tier)
Fondasi persistensi informasi:
- **Basis Data Relasional (PostgreSQL/MySQL):** Mencatat data pengguna terotentikasi, log audit sistem, dan riwayat transaksi resmi.
- **Basis Data Dokumen (MongoDB) / Time-Series Database:** Menampung jutaan titik data telemetri sensor IoT yang mengalir setiap detik secara efisien.

---

## C. PENGUJIAN SISTEM KOMPREHENSIF DAN UJI PENERIMAAN PENGGUNA (UAT)

Sebelum sebuah sistem diterapkan di lingkungan operasional nyata bersama mitra masyarakat, tim pengembang wajib melaksanakan empat tingkatan pengujian mutu perangkat lunak (*Software Quality Assurance*):

### 1. Pengujian Fungsional (Functional Testing)
Menguji setiap modul dan fungsi tombol secara terisolasi untuk memastikan sistem berjalan sesuai spesifikasi kebutuhan:
- Apakah tombol 'Buka Katup Air' mengirimkan sinyal kendali relay listrik yang benar?
- Apakah modul kamera menghasilkan resolusi citra yang sesuai untuk masukan model CNN?

### 2. Pengujian Kinerja dan Uji Beban (Stress / Load Testing)
Menguji ketahanan peladen backend ketika menerima lonjakan data secara serentak:
- Menggunakan perangkat lunak pengujian beban untuk menyimulasikan 500 permintaan baca/tulis data per detik.
- Mengukur metrik waktu tanggap peladen (*Latency / Response Time*) dan penggunaan memori RAM peladen untuk mencegah sistem tumbang (*crash*).

### 3. Uji Akurasi dan Matriks Kebingungan Model AI (Confusion Matrix)
Menguji keandalan model AI menggunakan dataset validasi independen yang belum pernah dilihat model:
- Menghitung metrik **Presisi (*Precision*)**, **Sensitivitas (*Recall*)**, dan **Skor F1 (*F1-Score*)**.
- Memastikan tingkat positif palsu (*False Positive*) dan negatif palsu (*False Negative*) berada dalam batas toleransi keselamatan kerja.

### 4. Uji Penerimaan Pengguna Nyata (User Acceptance Testing / UAT)
Tahap puncak pengujian di mana pengguna akhir nyata (mitra petani, pedagang UMKM, atau tenaga kesehatan) mengoperasikan sistem secara mandiri tanpa bantuan tim teknis sekolah:
- **Lembar Evaluasi UAT:** Memuat kuesioner skala Likert (1 hingga 5) yang mengukur kemudahan pemahaman antarmuka, kecepatan alur kerja, kejelasan instruksi, serta kepuasan menyeluruh pengguna.
- Sistem dinyatakan lulus UAT jika memperoleh persetujuan tertulis (*sign-off*) dari mitra pengguna dengan tingkat kepuasan minimal 85%.

---

## D. AUDIT ETIKA SISTEM CERDAS, KEAMANAN, DAN PENGAWASAN MANUSIA

Sebagai lulusan terdidik yang menjunjung tinggi etika profesi, peserta didik wajib menerapkan audit pertanggungjawaban sistem cerdas (*Ethical AI Audit*):

### 1. Mitigasi Bias Algoritma dan Diskriminasi Data
Memeriksa distribusi dataset latih untuk memastikan tidak terjadi bias demografis, lokasi geografis, maupun gender:
- *Contoh:* Jika sistem AI dilatih menggunakan 95% foto daun cabai dari varietas dataran tinggi di Pulau Jawa, model akan bias dan berkinerja buruk saat diterapkan pada varietas cabai lokal di Sulawesi Utara. Dataset wajib dikurasi ulang secara seimbang.

### 2. Keamanan Siber Perangkat dan Enkripsi Komunikasi
- Seluruh komunikasi data antara perangkat IoT, peladen backend, dan antarmuka web wajib menggunakan enkripsi **TLS/SSL (HTTPS)**.
- Kredensial rahasia (seperti kata sandi basis data dan token API) tidak boleh ditulis secara langsung (*hardcoded*) di dalam kode program publik, melainkan disimpan di dalam berkas variabel lingkungan (`.env`).

### 3. Mekanisme Pengawasan Manusia (Human-in-the-Loop)
Prinsip paling fundamental dalam etika kecerdasan artifisial adalah: **AI adalah alat pendukung keputusan, bukan pemegang kekuasaan mutlak atas keselamatan manusia**.
- Sistem wajib menyediakan tombol pembatalan darurat (*Emergency Override Button*).
- Jika model AI ragu-ragu (misal skor keyakinan hanya 60%), sistem tidak boleh mengeksekusi tindakan berbahaya secara otomatis (seperti menyemprotkan pestisida kimia pekat), melainkan wajib menampilkan pemberitahuan kepada manusia ahli untuk melakukan inspeksi manual terlebih dahulu.

---

## E. LKPD 4.1: BUKU LOG SPRINT MANAJEMEN CAPSTONE PROJECT TERPADU

Dalam mengerjakan Capstone Project, kalian bekerja dalam tim menggunakan metodologi tangkas **Agile Scrum**. Lengkapi buku log sprint mingguan berikut untuk memantau kemajuan proyek kelompok kalian.

### 1. Identitas Proyek Tim
- **Nama Tim Inovator:** ................................................................
- **Judul Sistem Cerdas:** ................................................................
- **Mitra Sasaran Proyek:** ................................................................
- **Pembagian Peran Anggota:**
  - *Lead System Architect & Frontend UI:* ................................................................
  - *IoT Hardware & Telemetry Engineer:* ................................................................
  - *AI / Machine Learning Engineer:* ................................................................
  - *Backend, Database & Security Specialist:* ................................................................

### 2. Lembar Pelacakan Sprint Mingguan (Sprint Tracker)

```text
================================================================================
LEMBAR PELACAKAN SPRINT CAPSTONE PROJECT FASE F AKHIR
================================================================================
Sprint Ke   : [ 1 / 2 / 3 / 4 ]
Target Fitur: Pengembangan Backend REST API & Integrasi Inferensi Model CNN
Batas Waktu : 2 Minggu

[ DAFTAR TUGAS PEKERJAAN (BACKLOG SPRINT) ]
1. [ SELESAI ] Membuat skrip FastAPI titik akhir POST /predict/leaf-health
2. [ SELESAI ] Mengonversi model MobileNetV2 terlatih ke format biner teroptimasi
3. [ SEDANG BERJALAN ] Menghubungkan pembacaan sensor ESP32 via protokol MQTT ke broker
4. [ BELUM DIMULAI ] Merancang komponen kartu ringkasan diagnosis pada UI antarmuka
5. [ BELUM DIMULAI ] Pengujian beban peladen dengan 200 simulasi panggilan serentak

[ KENDALA TEKNIS YANG DIHADAPI ]
- Tegangan pin GPIO 3,3V pada ESP32 tidak cukup untuk mengaktifkan koil relay 5V.
- Solusi Teknis: Menambahkan modul transistor sakelar driver dan regulator daya terpisah.

[ CATATAN UMPAN BALIK MITRA PENGGUNA ]
- Petani meminta warna tulisan rekomendasi dibuat lebih besar dan tombol semprot diwarnai hijau terang.
================================================================================
```

---

## F. RANGKUMAN MATERI BAB IV

1. **Capstone Project Fase F Akhir** adalah puncak rekayasa sistem terintegrasi yang menyatukan seluruh kompetensi koding, komputasi fisik IoT, analisis mahadata, dan model Deep Learning untuk memecahkan persoalan riil mitra masyarakat melalui pendekatan **Human-Centered AI**.
2. **Arsitektur Sistem Terintegrasi Multi-Lapisan** tersusun atas:
   - *Lapisan Antarmuka Pengguna (UI):* Memberikan visualisasi data yang ramah dan intuitif.
   - *Lapisan Backend REST API:* Menangani logika bisnis, sanitasi data, dan keamanan token otentikasi.
   - *Lapisan Mesin Kecerdasan Artifisial:* Melakukan inferensi prediktif berakurasi tinggi.
   - *Lapisan Basis Data:* Menyimpan data relasional terstruktur dan data telemetri waktu nyata.
3. Kualitas sistem wajib diverifikasi melalui empat tingkatan pengujian: **Functional Testing** (keandalan modul individu), **Stress/Load Testing** (ketahanan beban puncak), **Model Validation Matrix** (Presisi, Recall, F1-Score), serta **User Acceptance Testing (UAT)** langsung oleh pengguna akhir di lapangan.
4. Tata kelola sistem bertanggung jawab mengedepankan prinsip **Audit Etika**, mitigasi bias dataset demografis, enkripsi komunikasi data (HTTPS/TLS), serta mekanisme **Human-in-the-Loop** yang menjamin manusia tetap memegang kendali akhir atas seluruh keputusan kritis.

---

## G. UJI KOMPETENSI BAB IV

### Bagian 1: Pilihan Ganda (10 Soal Berbobot HOTS)

1. Dalam tahap inisiasi Capstone Project berbasis pendekatan Human-Centered Design, langkah pertama yang paling fundamental dilakukan oleh tim pengembang sebelum menulis sebaris pun kode program adalah...
A. Membeli peladen superkomputer berharga ratusan juta rupiah.  
B. Melakukan wawancara empati kontekstual bersama mitra pengguna nyata untuk menggali titik masalah (*Pain Points*) yang sesungguhnya mereka hadapi di lapangan.  
C. Menentukan warna logo dan merek dagang perusahaan rintisan.  
D. Mengajukan hak paten internasional di kantor kekayaan intelektual.  
E. Mengunggah repositori kosong ke GitHub.  

2. Perhatikan arsitektur sistem cerdas terintegrasi berikut:
```text
[ Sensor IoT ] --> (Protokol X) --> [ Peladen Backend ] --> [ Mesin Inferensi AI ]
                                              |
                                              v
                                     [ Basis Data Terpusat ]
```
Jika perangkat sensor IoT berupa mikrokontroler bertenaga baterai di pelosok ladang yang memiliki keterbatasan bandwidth, protokol komunikasi telemetri (Protokol X) yang paling hemat daya dan efisien untuk digunakan adalah...
A. HTTP POST Multipart Form-Data  
B. FTP (File Transfer Protocol)  
C. MQTT Publish-Subscribe  
D. SMTP (Simple Mail Transfer Protocol)  
E. Telnet  

3. Pada lapisan Backend REST API, Arya menerapkan mekanisme sanitasi data masukan dan validasi skema payload JSON secara ketat sebelum meneruskannya ke mesin inferensi AI. Praktik rekayasa perangkat lunak ini bertujuan utama untuk...
A. Menghilangkan warna pada gambar citra daun.  
B. Menurunkan kecepatan prosesor peladen agar hemat listrik.  
C. Mencegah kerentanan keamanan siber seperti injeksi data berbahaya (*Injection Attack*) dan memastikan masukan berformat valid.  
D. Mengubah model supervised menjadi unsupervised learning.  
E. Membatasi pengguna aplikasi hanya untuk teman sekelas.  

4. Saat melakukan uji beban (*Stress Testing*) pada peladen backend dengan menyimulasikan 1.000 permintaan identifikasi citra secara serentak per detik, peladen mengalami kegagalan respons (*timeout*) dan penggunaan memori RAM melonjak hingga 99%. Solusi arsitektural yang paling tepat untuk mengatasi kemacetan sistem tersebut adalah...
A. Mengganti semua kabel jaringan LAN di sekolah.  
B. Menerapkan antrean pesan asinkron (*Asynchronous Message Queue*) dan penskalaan peladen backend secara horizontal (*Horizontal Scaling*).  
C. Menghapus seluruh riwayat data transaksi di basis data.  
D. Mengubah bahasa antarmuka aplikasi menjadi bahasa Inggris.  
E. Mematikan sistem pendingin udara di ruang peladen.  

5. Perhatikan tabel matriks kebingungan (*Confusion Matrix*) evaluasi model AI pendeteksi penyakit tanaman berikut:
- Sakit Terdeteksi Sakit (True Positive): 92 kasus
- Sehat Terdeteksi Sehat (True Negative): 88 kasus
- Sakit Terdeteksi Sehat (False Negative): 8 kasus
- Sehat Terdeteksi Sakit (False Positive): 12 kasus
Berdasarkan data di atas, berapakah nilai Sensitivitas / Daya Ingat (*Recall*) dari model pendeteksi tersebut?
A. 92,0%  
B. 88,4%  
C. 92,0 / (92 + 8) = 92,0%  
D. 92,0 / (92 + 12) = 88,46%  
E. 88,0%  

6. Dalam kasus deteksi penyakit tanaman menular berisiko gagal panen total di perkebunan warga, jenis kesalahan klasifikasi manakah yang memiliki dampak kerugian finansial paling fatal bagi petani?
A. True Positive (Tanaman sakit terdeteksi sakit).  
B. False Positive (Tanaman sehat dikira sakit, sehingga petani melakukan pemeriksaan ulang).  
C. False Negative (Tanaman terinfeksi ganas lolos terdeteksi sebagai tanaman sehat, sehingga wabah menyebar tak terkendali).  
D. True Negative (Tanaman sehat terdeteksi sehat).  
E. Ambang probabilitas 50%.  

7. Dinda memimpin tahapan User Acceptance Testing (UAT) di balai desa. Salah satu indikator evaluasi keberhasilan UAT yang paling valid adalah...
A. Kode program ditulis lebih dari 10.000 baris.  
B. Pengguna akhir nyata mampu mengoperasikan fitur-fitur utama sistem secara mandiri dengan tingkat keberhasilan tinggi dan menyatakan puas pada lembar penilaian resmi.  
C. Seluruh tampilan aplikasi menggunakan gambar animasi tiga dimensi bergerak.  
D. Biaya pembuatan aplikasi melampaui batas anggaran sekolah.  
E. Aplikasi hanya dapat dijalankan pada komputer milik ketua tim pengembang.  

8. Sebuah sistem kecerdasan artifisial penyortir benih tanaman menunjukkan tingkat akurasi 98% ketika diuji di laboratorium sekolah di Manado, namun akurasinya turun menjadi 52% saat diuji di lahan perkebunan mitra di daerah perbukitan bersuhu dingin. Penyebab utama kegagalan performa lapangan ini ditinjau dari audit data adalah...
A. Terjadi pergeseran distribusi data masukan (*Data Distribution Shift / Dataset Bias*) akibat perbedaan kondisi lingkungan dan pencahayaan yang belum terwakili dalam data latih.  
B. Petani di perbukitan tidak menekan tombol keyboard dengan benar.  
C. Sistem operasi komputer laboratorium lebih canggih dari laptop lapangan.  
D. Model AI mengalami kelebihan memori cache peramban web.  
E. Satelit cuaca memblokir sinyal Wi-Fi perkebunan.  

9. Prinsip **Human-in-the-Loop (Pengawasan Manusia)** dalam tata kelola etika sistem cerdas menegaskan bahwa...
A. Komputer wajib memiliki bentuk fisik menyerupai postur tubuh manusia.  
B. Seluruh kode pemrograman harus diketik oleh minimal sepuluh orang programmer secara bergiliran.  
C. Keputusan akhir yang berdampak signifikan terhadap keselamatan, ekonomi, atau nasib manusia harus tetap berada di bawah kendali dan verifikasi manusia, bukan diserahkan mutlak pada algoritma otonom.  
D. Pengguna tidak diperbolehkan mematikan komputer selama 24 jam penuh.  
E. Model AI harus dilatih menggunakan foto potret manusia saja.  

10. Mengapa kunci rahasia (*API Secret Key*) dan kata sandi basis data tidak boleh diunggah secara terbuka ke repositori publik GitHub dalam pengembangan Capstone Project?
A. GitHub akan menghapus akun pengguna yang menyimpan kata sandi.  
B. Kunci rahasia publik dapat disalahgunakan oleh pihak asing atau peretas untuk mencuri data, merusak peladen, dan membengkakkan tagihan layanan awan.  
C. Tulisan kata sandi membuat ukuran berkas repositori bertambah 50 Gigabyte.  
D. Bahasa pemrograman Python menolak membaca berkas yang diunggah ke internet.  
E. Guru pembimbing tidak menyukai teks berhuruf kapital.  

---

### Bagian 2: Uraian dan Pemecahan Masalah Sistemik (5 Soal)

1. Gambarkan dan jelaskan keterhubungan hierarkis antara **4 Lapisan Arsitektur Sistem Terintegrasi** (Lapisan UI, Lapisan Peladen REST API, Lapisan AI Inference Engine, dan Lapisan Basis Data) pada rancang bangun Capstone Project kelompok kalian!

2. Jelaskan perbedaan esensial antara **Functional Testing**, **Stress/Load Testing**, dan **User Acceptance Testing (UAT)**! Mengapa sebuah produk perangkat lunak yang telah lulus pengujian fungsional di laboratorium sekolah masih bisa gagal total pada tahap UAT bersama warga masyarakat?

3. Dalam evaluasi model klasifikasi medis atau pertanian, jelaskan mengapa nilai **Sensitivitas / Recall** seringkali dianggap jauh lebih kritis dibanding nilai **Presisi (*Precision*)**! Berikan contoh skenario konkretnya!

4. Uraikan apa yang dimaksud dengan fenomena **Pergeseran Distribusi Data (*Distribution Shift*)** dalam penerapan model AI di dunia nyata, dan jelaskan 2 strategi rekayasa untuk memitigasi kegagalan model akibat fenomena tersebut!

5. Mengapa mekanisme **Tombol Intervensi Manual (*Human Oversight / Manual Override*)** menjadi syarat mutlak dalam perancangan sistem kendali fisik terhubung AI (seperti katup pengairan otomatis atau sakelar pemanas kandang ternak)?

---

### KUNCI JAWABAN DAN PEMBAHASAN LENGKAP BAB IV

#### Kunci Jawaban Pilihan Ganda:
1. **B (Melakukan wawancara empati kontekstual bersama mitra pengguna nyata untuk menggali titik masalah yang sesungguhnya)** — Human-Centered Design menuntut tahap empati mendalam sebelum rekayasa teknis dimulai.
2. **C (MQTT Publish-Subscribe)** — Protokol perpesanan ringan berbasis biner dengan overhead header sangat kecil (2 byte), ideal untuk lingkungan mikrokontroler berdaya baterai dan bandwidth minim.
3. **C (Mencegah kerentanan keamanan siber seperti injeksi data berbahaya dan memastikan masukan berformat valid)** — Sanitasi dan validasi skema masukan adalah benteng pertahanan utama peladen API dari eksploitasi peretasan.
4. **B (Menerapkan antrean pesan asinkron dan penskalaan peladen backend secara horizontal)** — Pola asynchronous queue (misal Redis/RabbitMQ) menampung lonjakan antrean tanpa memblokir thread eksekusi peladen utama.
5. **C (92,0%)** — Rumus Recall = True Positive / (True Positive + False Negative) = 92 / (92 + 8) = 92 / 100 = 0,92 atau 92,0%.
6. **C (False Negative: Tanaman terinfeksi ganas lolos terdeteksi sebagai tanaman sehat)** — Kesalahan negatif palsu menyebabkan penyakit menular tidak diobati dan menyebarkan wabah ke seluruh hamparan kebun.
7. **B (Pengguna akhir nyata mampu mengoperasikan fitur-fitur utama sistem secara mandiri dengan tingkat keberhasilan tinggi dan menyatakan puas)** — UAT adalah validasi penerimaan kontekstual oleh pemangku kepentingan sebenarnya.
8. **A (Terjadi pergeseran distribusi data masukan akibat perbedaan kondisi lingkungan dan pencahayaan yang belum terwakili dalam data latih)** — Ketidakmampuan model menghadapi domain lingkungan baru disebabkan oleh bias distribusi dataset pelatihan.
9. **C (Keputusan akhir yang berdampak signifikan terhadap keselamatan, ekonomi, atau nasib manusia harus tetap berada di bawah kendali dan verifikasi manusia)** — Menjamin agensi dan kedaulatan manusia atas teknologi cerdas.
10. **B (Kunci rahasia publik dapat disalahgunakan oleh pihak asing atau peretas untuk mencuri data, merusak peladen, dan membengkakkan tagihan layanan awan)** — Praktik kredensial bocor pada repositori publik merupakan celah eksploitasi keamanan siber yang sangat rawan.

#### Pembahasan Soal Uraian:
1. **4 Lapisan Arsitektur Terintegrasi:**
   - *Lapisan UI (Klien):* Menangani penyajian visual dan menerima input aksi dari pengguna.
   - *Lapisan REST API (Backend):* Gerbang kendali logika, otentikasi, validasi data, dan orkestrasi panggilan.
   - *Lapisan AI Engine:* Menjalankan algoritma pemrosesan citra/klastering dan mengembalikan hasil skor probabilitas ke backend.
   - *Lapisan Basis Data:* Menyimpan data transaksional, profil mitra, dan telemetri perangkat secara persisten dan aman.
2. **Perbedaan Ragam Pengujian dan Alasan Kegagalan UAT:**
   - *Functional Testing:* Menguji kebenaran algoritma dan respon fungsi secara internal teknis.
   - *Stress Testing:* Menguji kapasitas konkurensi peladen di bawah beban lalu lintas ekstrem.
   - *UAT:* Menguji kesesuaian sistem dengan alur kerja, kenyamanan, dan kebutuhan psikologis pengguna akhir.
   - *Penyebab Gagal UAT:* Produk lolos uji teknis tetapi gagal di lapangan jika antarmukanya membingungkan (*poor UX*), tombol tidak terbaca di bawah terik matahari, atau rekomendasi yang dihasilkan tidak realistis diterapkan petani.
3. **Urgensi Recall dibanding Presisi pada Deteksi Wabah:**
   - Recall mengukur seberapa banyak kasus sakit sebenarnya yang berhasil dijaring oleh sistem. Dalam wabah penyakit menular, membiarkan satu tanaman sakit lolos tanpa terdeteksi (False Negative) berakibat kematian seluruh kebun. Sedangkan jika tanaman sehat keliru dikira sakit (False Positive / Presisi rendah), petani hanya perlu memeriksa ulang daun tersebut tanpa risiko kehilangan panen masif.
4. **Distribution Shift dan Mitigasinya:**
   - *Pengertian:* Perubahan karakteristik statistik antara data latih (*training domain*) dan data operasional lapangan (*target domain*), seperti pencahayaan fajar vs siang hari, sudut kamera, atau jenis tanah yang berbeda.
   - *2 Solusi Mitigasi:*
     1. Menerapkan teknik augmentasi data masif (*Data Augmentation*) saat pelatihan (rotasi, variasi kecerahan, penambahan blur dan kontras).
     2. Menerapkan pemantauan berkelanjutan (*Continuous Model Monitoring*) dan melakukan pelatihan ulang (*retraining*) menggunakan data operasional baru dari lapangan.
5. **Urgensi Tombol Intervensi Manual (Manual Override):**
   - Kegagalan mikrokontroler (korsleting, sensor kotor, atau halusinasi model AI) dapat memicu perintah salah yang berbahaya, seperti katup air irigasi membuka terus-menerus hingga membanjiri kebun. Tombol fisik manual atau sakelar darurat memastikan operator manusia dapat memutuskan aliran daya dan mengambil alih kendali secara instan demi keselamatan jiwa dan aset.
"""
