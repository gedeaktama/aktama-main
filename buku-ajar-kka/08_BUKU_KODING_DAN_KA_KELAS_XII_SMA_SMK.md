# MASTER BLUEPRINT & OUTLINE BUKU TEKS SISWA & PANDUAN GURU
# KODING DAN KECERDASAN ARTIFISIAL UNTUK SMA/MA/SMK KELAS XII
### Kelompok Mata Pelajaran Pilihan — Fase F (Kelas XII SMA/MA/SMK)
**Penulis Utama:** Gede Erik Aktama, M.Kom (Fasilitator Nasional KKA Kemendikdasmen)  
**Pendekatan Pedagogis:** Pembelajaran Mendalam (*Mindful, Meaningful, Joyful Learning*)  
**Standar Mutu:** Permendikbudristek No. 22/2022 & Permendikdasmen No. 13/2025  

---

## I. IDENTITAS & SPESIFIKASI BUKU
* **Judul Buku Siswa:** Koding dan Kecerdasan Artifisial untuk SMA/MA/SMK Kelas XII
* **Judul Buku Guru:** Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SMA/MA/SMK Kelas XII
* **Fase / Jenjang:** Fase F (Tingkat Puncak Kelulusan) — SMA / MA / SMK Kelas 12
* **Alokasi Waktu:** 5 Jam Pelajaran (JP) @ 45 menit per minggu / 160 JP per tahun (1 Buku untuk Semester 1 & 2)
* **Fokus Utama:** Komputasi Fisik IoT Terhubung AI (*Edge AI*), Rekayasa Mahadata (*Big Data 5V & Data Mining*), Jaringan Saraf Tiruan (*Deep Learning CNN & Transfer Learning*), Capstone Project Terpadu Mitra Industri/Masyarakat, serta Tata Kelola Regulasi Global AI (UNESCO).

---

## II. SEMESTER 1: PEMROGRAMAN IOT CERDAS & REKAYASA MAHADATA (80 JP)

### BAB 1: Pemrograman Perangkat Keras Cerdas: Internet of Things (IoT) Terhubung AI (45 JP - 9 Pertemuan @ 5 JP)
* **Elemen CP:** Algoritma Pemrograman (AP) & Berpikir Komputasional (BK)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu merancang arsitektur sistem IoT terhubung mikrokontroler (ESP32/Raspberry Pi) (15 JP).
  2. Murid mampu menerapkan komunikasi data real-time menggunakan protokol IoT (MQTT dan REST HTTP) (15 JP).
  3. Murid mampu mengintegrasikan model AI cerdas langsung pada perangkat fisik (*Edge AI*) (15 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa dunia digital dan dunia fisik kini menyatu menjadi satu ekosistem (*Cyber-Physical System*).
  * *Meaningful:* Mengembangkan alat pemantau kelembapan tanah dan pengairan otomatis untuk petani cabai desa.
  * *Joyful:* Menyaksikan perangkat keras mini di tangan merespons kehadiran orang dan mengambil keputusan otomatis secara mandiri.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **1.1 Arsitektur Internet of Things (IoT) Modern:**
    * 3 Lapisan Arsitektur: Lapisan Sensor Fisik (*Perception Layer*), Lapisan Jaringan Jarak Jauh (*Network Layer*), dan Lapisan Aplikasi Pengguna (*Application Layer*).
    * [PROMPT GAMBAR ILUSTRASI: Diagram arsitektur sistem Smart Agriculture: Sensor kelembapan di ladang terhubung ke papan mikrokontroler ESP32, mengirim sinyal radio nirkabel MQTT ke server cloud, dan membuka katup air irigasi secara otomatis].
  * **1.2 Membaca Data Sensor Fisik & Mengendalikan Aktuator:**
    * Sensor Suhu/Kelembapan (DHT22), Sensor Jarak Ultrasonik (HC-SR04), Sensor Gas (MQ-2), dan Modul Kamera Mini (ESP32-CAM).
    * Mengendalikan motor servo, relay listrik berdaya tinggi, dan layar indikator OLED.
  * **1.3 Protokol Komunikasi Data Ringan IoT: MQTT vs HTTP:**
    * Mengapa HTTP terlalu berat untuk perangkat bertenaga baterai?
    * Arsitektur *Publish-Subscribe* protokol MQTT: Broker (HiveMQ / Mosquitto), Topik Telemetri, dan Klien Pengirim/Penerima.
  * **1.4 Konsep Edge AI (Kecerdasan di Ujung Perangkat):**
    * Menjalankan model klasifikasi ringan langsung di mikrokontroler tanpa bergantung pada internet (*Low Latency, High Privacy, Zero Cloud Cost*).
    * Pemanfaatan platform Edge Impulse / TensorFlow Lite for Microcontrollers.
  * **1.5 LKPD Laboratorium: "Rancang Bangun Sistem Pemantau Lingkungan Sekolah Pintar"**
    * Praktikum merangkai sirkuit sensor pada breadboard, memprogram ESP32 dengan C++/MicroPython, dan mengirim data sensor ke dashboard cloud Adafruit IO / ThingsBoard.
  * **Pojok Karakter & Etika:** Keamanan siber perangkat IoT: Mengganti kredensial bawaan (*default password*), mengenkripsi data telemetri, dan mencegah perangkat disusupi menjadi bagian dari jaringan serangan DDoS (*Kewargaan & Tanggung Jawab Keamanan*).
  * **Rangkuman Bab 1**
* **Paket Soal Evaluasi Bab 1 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Skema Rangkaian & Kode C++):* Menganalisis skema pembagi tegangan sensor analog; menentukan penyebab broker MQTT menolak pesan telemetri; memilih arsitektur Edge AI vs Cloud AI berdasarkan batasan bandwidth desa.
  * *Uraian (5 Soal):* Jelaskan perbedaan mekanisme Publish-Subscribe pada MQTT dibanding Request-Response pada HTTP! Mengapa Edge AI sangat krusial dalam sistem rem darurat mobil listrik?
  * *Tugas Unjuk Kerja Proyek:* Prototipe Alat Cerdas IoT Terhubung Dashboard Cloud.
* **Bagian Buku Panduan Guru (BG) Bab 1:**
  * Panduan keselamatan kerja praktikum elektronika (menghindari korsleting baterai dan keselamatan tegangan listrik).
  * Kunci jawaban soal pilihan ganda, panduan troubleshooting hardware, dan rubrik asesmen sirkuit IoT.

### BAB 2: Mahadata (Big Data) & Rekayasa Analisis Skala Besar (35 JP - 7 Pertemuan @ 5 JP)
* **Elemen CP:** Analisis Data (AD) & Literasi Digital (LD)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami karakteristik 5V Big Data dan ekosistem komputasi awan (*Cloud Computing*) (10 JP).
  2. Murid mampu menerapkan teknik penambangan data (*Data Mining*) dan klastering unsupervised (*K-Means*) (15 JP).
  3. Murid mampu merancang dashboard visualisasi data interaktif untuk pengambilan keputusan strategis (10 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa setiap klik, transaksi belanja, dan lokasi GPS kita menyumbang aliran mahadata dunia.
  * *Meaningful:* Mengolah dataset terbuka bencana alam Indonesia untuk memetakan daerah prioritas bantuan logistik.
  * *Joyful:* Mengelompokkan jutaan data acak menjadi klaster-klaster warna yang mengungkap pola rahasia masyarakat.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **2.1 Karakteristik 5V Mahadata (Big Data):**
    * *Volume* (Ukuran Petabyte), *Velocity* (Aliran real-time), *Variety* (Teks, video, log server), *Veracity* (Akurasi dan noise data), *Value* (Nilai ekonomi dan sosial).
    * [PROMPT GAMBAR ILUSTRASI: Infografis futuristik 5 dimensi menampilkan 5 kubus kristal berlabel Volume, Velocity, Variety, Veracity, dan Value melayang di atas peta kepulauan Indonesia digital yang berpendar cahaya data].
  * **2.2 Arsitektur Pengolahan Big Data:**
    * Perbedaan Basis Data Relasional SQL vs Basis Data NoSQL Berorientasi Dokumen (MongoDB) vs *Data Lake*.
  * **2.3 Penambangan Data & Algoritma Klastering K-Means:**
    * Pembelajaran tak terawasi (*Unsupervised Learning*): Menemukan kelompok alami data tanpa label awal.
    * Menentukan titik pusat klaster (*Centroid*) dan metode *Elbow* untuk memilih jumlah k paling ideal.
  * **2.4 LKPD Laboratorium: "Segmentasi Data Pengguna Menggunakan Python dan K-Means"**
    * Praktikum memuat dataset publik, melakukan penskalaan fitur, menjalankan K-Means, dan memvisualisasikan scatter plot klaster.
  * **2.5 Etika Mahadata & Kedaulatan Data Nasional:**
    * Teknik De-identifikasi dan Anonimisasi data pribadi; hak individu untuk dilupakan (*Right to be Forgotten*) sesuai UU PDP.
    * Isu kedaulatan data (*Data Sovereignty*): Mengapa data penting warga negara harus disimpan di pusat data nasional?
  * **Pojok Karakter & Etika:** Menolak pengawasan massal tanpa izin (*Mass Surveillance*); menjunjung tinggi hak privasi warga negara (*Keadaban & Perlindungan HAM*).
  * **Rangkuman Bab 2**
* **Paket Soal Evaluasi Bab 2 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Grafik Klastering):* Membaca grafik Elbow Method untuk menentukan jumlah klaster k optimal; menganalisis pelanggaran etika saat perusahaan menjual dataset riwayat lokasi pengguna tanpa izin.
  * *Uraian (5 Soal):* Jelaskan perbedaan mendasar antara Klasifikasi (Supervised) dan Klastering (Unsupervised)! Mengapa karakteristik Veracity menjadi tantangan terbesar dalam analisis data media sosial?
  * *Tugas Proyek Mini Akhir Semester 1:* Dashboard Analisis Mahadata Publik Interaktif.
* **Bagian Buku Panduan Guru (BG) Bab 2:**
  * Panduan penyediaan dataset terbuka yang aman dan bebas dari informasi pribadi rahasia.
  * Kunci jawaban soal pilihan ganda dan rubrik penilaian dashboard analitik data.

---

## III. SEMESTER 2: DEEP LEARNING, CAPSTONE PROJECT, & DISKUSI GLOBAL GOVERNANCE (80 JP)

### BAB 3: Pengembangan Model AI Lanjut & Fondasi Deep Learning (35 JP - 7 Pertemuan @ 5 JP)
* **Elemen CP:** Pemanfaatan dan Pengembangan Kecerdasan Artifisial (PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami arsitektur Jaringan Saraf Tiruan (*Artificial Neural Network - ANN*) dan fungsi aktivasi (10 JP).
  2. Murid mampu menerapkan arsitektur Convolutional Neural Network (CNN) untuk pengenalan citra kompleks (15 JP).
  3. Murid mampu memanfaatkan teknik Transfer Learning dan mengintegrasikan Cloud AI API ke dalam aplikasi (10 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa jaringan saraf tiruan terinspirasi dari arsitektur neuron otak biologis manusia.
  * *Meaningful:* Membangun sistem pendeteksi penyakit mata katarak atau sistem deteksi penyakit padi daun otomatis.
  * *Joyful:* Mengamati visualisasi lapisan filter konvolusi yang mengekstrak fitur garis, sudut, hingga bentuk utuh secara ajaib.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **3.1 Dari Machine Learning Konvensional Menuju Deep Learning:**
    * Keterbatasan ekstraksi fitur manual pada data citra resolusi tinggi.
    * Konsep dasar Perceptron: Bobot (*Weights*), Bias, Jumlah Tertimbang, dan Fungsi Aktivasi (*ReLU, Sigmoid, Softmax*).
    * [PROMPT GAMBAR ILUSTRASI: Diagram arsitektur Jaringan Saraf Tiruan (ANN) berlapis: Input Layer (lingkaran biru) terhubung jaring-jaring benang cahaya ke Hidden Layers (lingkaran kuning), dan berakhir di Output Layer (lingkaran hijau) yang memprediksi jenis penyakit tanaman].
  * **3.2 Arsitektur Convolutional Neural Network (CNN):**
    * Tiga Lapisan Utama: *Convolutional Layer* (ekstraksi fitur), *Pooling Layer* (reduksi ukuran matriks), dan *Fully Connected Layer* (klasifikasi akhir).
  * **3.3 Transfer Learning: Menghemat Waktu dan Daya Komputasi:**
    * Memanfaatkan model terlatih raksasa industri (*MobileNet, ResNet*) dan melakukan penyesuaian akhir (*fine-tuning*) pada dataset lokal terbatas.
  * **3.4 LKPD Laboratorium: "Melatih Model Deteksi Citra Menggunakan Transfer Learning Python"**
    * Praktikum menggunakan TensorFlow/Keras untuk melatih model klasifikasi sampah plastik daur ulang dengan akurasi di atas 90%.
  * **3.5 Mengintegrasikan Cloud AI API ke dalam Aplikasi Nyata:**
    * Memanggil API pengenal teks (OCR), Vision API, atau Generative AI API menggunakan skrip Python untuk memperkaya fungsionalitas software.
  * **Pojok Karakter & Etika:** Jejak Karbon Komputasi AI (*Green AI*): Memilih arsitektur model yang efisien energi demi menjaga kelestarian lingkungan bumi (*Keberlanjutan Lingkungan & Moralitas*).
  * **Rangkuman Bab 3**
* **Paket Soal Evaluasi Bab 3 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Arsitektur CNN):* Menghitung dimensi matriks keluaran setelah operasi Max Pooling 2x2; menganalisis peran fungsi aktivasi ReLU dalam mengatasi masalah vanishing gradient.
  * *Uraian (5 Soal):* Jelaskan mengapa teknik Transfer Learning jauh lebih realistis diterapkan oleh pengembang pemula dibanding melatih model CNN dari awal (*from scratch*)! Apa kelemahan model deep learning jika dihadapkan pada fenomena black box?
  * *Tugas Unjuk Kerja Proyek:* Laporan Pelatihan Model Deep Learning Pengenal Citra dan Pengujian Cloud API.
* **Bagian Buku Panduan Guru (BG) Bab 3:**
  * Panduan memanfaatkan GPU gratis di Google Colab agar pelatihan model berjalan cepat tanpa membebani komputer sekolah.
  * Kunci jawaban soal pilihan ganda dan rubrik penilaian akurasi model deep learning.

### BAB 4: Proyek Akhir Terpadu (Capstone Project Fase F): Sistem AI Terintegrasi Human-Centered (35 JP - 7 Pertemuan @ 5 JP)
* **Elemen CP:** Seluruh Elemen Capaian Pembelajaran Fase F (BK, LD, AP, AD, LEKA, PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu merumuskan persoalan nyata mitra industri/komunitas dan merancang arsitektur sistem terintegrasi (10 JP).
  2. Murid mampu mengembangkan produk nyata lengkap (Hardware IoT / UI Aplikasi + REST API Database + Model AI Cerdas) (15 JP).
  3. Murid mampu melakukan audit etika sistem, pengujian beban, dan uji penerimaan pengguna nyata (UAT) (10 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Melakukan refleksi atas seluruh kompetensi koding dan AI yang telah dikuasai selama 3 tahun di sekolah menengah.
  * *Meaningful:* Mempersembahkan karya inovasi nyata yang dipakai langsung oleh UMKM, puskesmas desa, atau komunitas sekitar.
  * *Joyful:* Merasakan kepuasan luar biasa sebagai pencipta teknologi (*tech creator*) yang karyanya memberikan solusi nyata bagi sesama.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **4.1 Inisiasi Proyek Solutif Berbasis Masalah Mitra Nyata:**
    * Wawancara mendalam bersama mitra UMKM atau pimpinan komunitas lokal untuk memetakan titik masalah (*Pain Points*).
    * [PROMPT GAMBAR ILUSTRASI: Empat siswa SMA/SMK tingkat akhir mengenakan seragam sekolah rapi sedang mempresentasikan prototipe kotak pintar IoT berlayar digital kepada seorang bapak petani dan ibu pelaku UMKM di ruang pertemuan balai desa].
  * **4.2 Rekayasa Sistem Terintegrasi Multi-Lapisan:**
    * Lapisan 1: Antarmuka Pengguna (Web/Mobile App).
    * Lapisan 2: Backend REST API Server.
    * Lapisan 3: Model AI Cerdas (Machine Learning / Deep Learning / IoT).
    * Lapisan 4: Penyimpanan Basis Data Relasional / Cloud.
  * **4.3 Pengujian Komprehensif Produk:**
    * *Functional Testing*, Uji Akurasi Model AI, Pengujian Beban (*Stress Testing*), dan *User Acceptance Testing (UAT)* bersama mitra.
  * **4.4 Audit Etika, Keamanan Data, dan Mekanisme Human Oversight:**
    * Memastikan sistem tidak diskriminatif, data pengguna terenkripsi, dan ada tombol intervensi manusia saat sistem ragu mengambil keputusan.
  * **4.5 LKPD Proyek Akhir: "Buku Log Sprint Capstone Project Mingguan"**
  * **Pojok Karakter & Etika:** Menjaga integritas profesional: Tidak memalsukan data hasil pengujian akurasi; komitmen dedikasi untuk kemajuan bangsa (*Profil Pelajar Pancasila*).
  * **Rangkuman Bab 4**
* **Paket Soal Evaluasi Bab 4 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Kasus Proyek):* Menentukan prioritas penanganan bug berdasarkan matriks keparahan; menganalisis lembar hasil UAT dari pengguna nyata.
  * *Uraian (5 Soal):* Rancang diagram arsitektur sistem terintegrasi untuk produk Capstone kelompokmu; jelaskan 3 langkah mitigasi jika model AI mengalami penurunan akurasi saat diuji di lapangan!
  * *Penilaian Kinerja Capstone Project:* Rubrik Komprehensif Produk, Laporan Teknis, dan Uji Penerimaan Mitra.
* **Bagian Buku Panduan Guru (BG) Bab 4:**
  * Panduan mendampingi kerja sama sekolah dengan mitra eksternal (UMKM/industri/pemerintah desa).
  * Format penilaian sidang tugas akhir proyek siswa.

### BAB 5: Diseminasi Karya, Tata Kelola Global, & Kesiapan Karier Digital (10 JP - 2 Pertemuan @ 5 JP)
* **Elemen CP:** Literasi dan Etika Kecerdasan Artifisial (LEKA) & Literasi Digital (LD)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami standar tata kelola global etika AI (UNESCO & Regulasi Nasional) (5 JP).
  2. Murid mampu menyusun portofolio profesional dan mempresentasikan karya di pameran inovasi nasional (5 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari peran strategis diri sebagai generasi emas Indonesia yang siap bersaing di panggung inovasi dunia.
  * *Meaningful:* Menyusun repositori GitHub dan profil profesional untuk melangkah ke perguruan tinggi atau dunia kerja.
  * *Joyful:* Merayakan kelulusan pendidikan menengah dalam festival teknologi akbar bersama keluarga dan guru.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **5.1 Tata Kelola Global & Kedaulatan AI Indonesia:**
    * Rekomendasi Etika AI UNESCO (*UNESCO Recommendation on the Ethics of AI*), EU AI Act, dan Pedoman Etika AI Nasional Kemkomdigi/Kemendikdasmen.
  * **5.2 Pameran Akbar Inovasi Pelajar (National Coding & AI Showcase Day):**
    * Standar stan pameran profesional: Demo live produk, poster ilmiah, lembar umpan balik, dan kartu nama digital.
  * **5.3 Menata Portofolio Digital Profesional:**
    * Menyusun repositori kode terkurasi di GitHub, membuat laman portofolio web pribadi, dan menyusun Curriculum Vitae (CV) digital.
  * **Pojok Karakter & Etika:** Menjadi manusia pembelajar sepanjang hayat (*Lifelong Learner*) yang menggunakan ilmu teknologi untuk menegakkan keadilan dan kemakmuran nusantara (*Integritas & Cinta Tanah Air*).
  * **Rangkuman Bab 5 & Refleksi Akhir Kelulusan Fase F**
* **Paket Soal Evaluasi Akhir Jenjang SMA/SMK (Kelulusan Fase F Terstandar):**
  * *Pilihan Ganda Terstandar (20 Soal):* Ujian komprehensif menguji seluruh elemen CP Fase F (OOP, API, ML, IoT, Deep Learning, Etika AI).
  * *Uraian Desain Solusi Tingkat Tinggi (5 Soal):* Menganalisis studi kasus disrupsi teknologi skala industri.
  * *Rubrik Kelulusan Akhir Fase F:* Standar sertifikasi kompetensi Koding dan Kecerdasan Artifisial tingkat pendidikan menengah.
* **Bagian Buku Panduan Guru (BG) Bab 5:**
  * Panduan evaluasi sidang kelulusan mata pelajaran pilihan Koding dan Kecerdasan Artifisial.
  * Kunci jawaban komprehensif dan rubrik penilaian portofolio karier digital siswa.

---

## IV. STRUKTUR BAGIAN AKHIR BUKU (POSTLIMINARIES)
* **Glosarium Istilah Lengkap Tingkat Lanjut (Fase F Akhir)**
* **Kunci Jawaban Uji Pemahaman Pilihan Ganda Terpilih**
* **Daftar Pustaka Resmi Kemendikdasmen, Standar UNESCO, & Literatur Sains Internasional**
* **Indeks Istilah Komprehensif**
* **Biodata Lengkap Tim Penulis, Reviewer Industri, Editor Bahasa, dan Fasilitator TOT**
