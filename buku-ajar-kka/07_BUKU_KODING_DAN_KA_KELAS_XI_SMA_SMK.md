# MASTER BLUEPRINT & OUTLINE BUKU TEKS SISWA & PANDUAN GURU
# KODING DAN KECERDASAN ARTIFISIAL UNTUK SMA/MA/SMK KELAS XI
### Kelompok Mata Pelajaran Pilihan — Fase F (Kelas XI SMA/MA/SMK)
**Penulis Utama:** Gede Erik Aktama, M.Kom (Fasilitator Nasional KKA Kemendikdasmen)  
**Pendekatan Pedagogis:** Pembelajaran Mendalam (*Mindful, Meaningful, Joyful Learning*)  
**Standar Mutu:** Permendikbudristek No. 22/2022 & Permendikdasmen No. 13/2025  

---

## I. IDENTITAS & SPESIFIKASI BUKU
* **Judul Buku Siswa:** Koding dan Kecerdasan Artifisial untuk SMA/MA/SMK Kelas XI
* **Judul Buku Guru:** Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SMA/MA/SMK Kelas XI
* **Fase / Jenjang:** Fase F (Kelompok Mata Pelajaran Pilihan) — SMA / MA / SMK Kelas 11
* **Alokasi Waktu:** 5 Jam Pelajaran (JP) @ 45 menit per minggu / 180 JP per tahun (1 Buku untuk Semester 1 & 2)
* **Fokus Utama:** Pemrograman Berorientasi Objek (*OOP Python*), Manajemen Proyek Rekayasa Perangkat Lunak (*SDLC & Git/GitHub*), Integrasi Basis Data via REST API, Pipeline *Machine Learning* Terapan (KNN & Decision Tree), Pemrosesan Bahasa Alami (*NLP*), serta Etika Pengembangan *Human-Centered*.

---

## II. SEMESTER 1: PEMROGRAMAN OOP, REKAYASA PERANGKAT LUNAK, & DATABASE TERINTEGRASI (90 JP)

### BAB 1: Pemrograman Berorientasi Objek (OOP) & Engineering Process (40 JP - 8 Pertemuan @ 5 JP)
* **Elemen CP:** Algoritma Pemrograman (AP) & Berpikir Komputasional (BK)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami dan menerapkan paradigma OOP (Class, Object, Constructor, Method) dalam Python (16 JP).
  2. Murid mampu menerapkan 3 pilar OOP: Encapsulation, Inheritance, dan Polymorphism (14 JP).
  3. Murid mampu menerapkan Software Development Life Cycle (SDLC) dan berkolaborasi menggunakan Git/GitHub (10 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa struktur class memodelkan objek dunia nyata secara elegan dan dapat digunakan kembali (*reusable*).
  * *Meaningful:* Mengembangkan modul sistem manajemen klinik kesehatan atau perpustakaan digital sekolah.
  * *Joyful:* Pengalaman kolaborasi tim programmer mengerjakan repositori kode bersama di GitHub tanpa bentrok (*merge conflict resolution*).
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **1.1 Paradigma OOP vs Prosedural:**
    * Keterbatasan fungsi sekuensial pada proyek perangkat lunak skala besar.
    * Konsep *Class* sebagai cetak biru (*blueprint*) dan *Object* sebagai wujud nyata di memori komputer.
    * [PROMPT GAMBAR ILUSTRASI: Diagram teknis arsitektur: Cetak biru cetakan mobil (Class Mobil) menghasilkan mobil sedan merah, mobil minibus putih, dan mobil truk biru (Objects) dengan atribut warna dan kecepatan berbeda].
  * **1.2 Konstruktor, Atribut, dan Method dalam Python:**
    * Menggunakan method `__init__()`, variabel instans, dan kata kunci `self`.
  * **1.3 Tiga Pilar Utama OOP:**
    * *Encapsulation:* Menyembunyikan data sensitif dengan atribut privat (`__saldo`) dan method *getter/setter*.
    * *Inheritance:* Mewariskan sifat class induk (*Person*) ke class turunan (*Siswa, Guru*).
    * *Polymorphism:* Menimpa method (*method overriding*) agar fungsi `hitung_gaji()` berperilaku sesuai jenis karyawan.
  * **1.4 Engineering Process & SDLC (Agile/Scrum):**
    * Siklus hidup: Analisis Kebutuhan -> Perancangan Arsitektur -> Implementasi Koding -> Pengujian (*Unit Testing*) -> Pemeliharaan.
  * **1.5 Manajemen Versi Kode Menggunakan Git & GitHub:**
    * Praktik perintah terminal: `git init`, `git add`, `git commit`, `git branch`, `git push`, dan membuat *Pull Request*.
  * **1.6 LKPD Laboratorium: "Rancang Bangun Sistem Manajemen Akademik OOP Berbasis Git"**
    * Tugas tim 3 siswa: Membagi class diagram, membagi cabang branch Git, dan menyatukan kode menjadi aplikasi konsol terpadu.
  * **Pojok Karakter & Etika:** Menjaga transparansi repositori kode dan mematuhi etika kontributor open source (*Kolaborasi & Tanggung Jawab Profesional*).
  * **Rangkuman Bab 1**
* **Paket Soal Evaluasi Bab 1 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Diagram UML & Kode):* Menentukan hak akses atribut privat; memprediksi keluaran method overriding pada pewarisan bertingkat; menyelesaikan konflik merge Git.
  * *Uraian (5 Soal):* Rancang Class Diagram UML untuk sistem e-commerce; jelaskan mengapa enkapsulasi mencegah korupsi data dalam sistem perbankan!
  * *Tugas Unjuk Kerja Proyek:* Proyek Aplikasi Konsol OOP Berkelompok Terintegrasi Repositori GitHub.
* **Bagian Buku Panduan Guru (BG) Bab 1:**
  * Panduan mendampingi setup Git dan akun GitHub di laboratorium komputer sekolah.
  * Kunci jawaban soal pilihan ganda, rubrik review kode, dan penilaian kontribusi commit siswa.

### BAB 2: Rekayasa Basis Data Terintegrasi, Data Encoding, & API (35 JP - 7 Pertemuan @ 5 JP)
* **Elemen CP:** Analisis Data (AD)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami konsep data encoding dalam pertukaran data modern (JSON, XML, UTF-8) (10 JP).
  2. Murid mampu merancang skema database relasional multi-tabel dan query kompleks (JOIN, GROUP BY) (15 JP).
  3. Murid mampu membangun antarmuka REST API dan mengintegrasikan database dengan aplikasi Python (10 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa di era komputasi awan, data ditransmisikan dalam format teks terstruktur antar perangkat.
  * *Meaningful:* Memahami cara kerja aplikasi pemesanan ojek online menghubungkan aplikasi ponsel penumpang dengan database server.
  * *Joyful:* Menguji endpoint API di browser atau Postman dan melihat data JSON rapi muncul seketika.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **2.1 Format Data Encoding & Pertukaran Data:**
    * Mengapa format biner diubah menjadi teks? Mengenal ASCII, UTF-8, dan struktur data JSON (*JavaScript Object Notation*).
    * [PROMPT GAMBAR ILUSTRASI: Diagram transmisi data modern: Objek Python di sisi kiri diubah menjadi teks JSON di tengah (Serialisasi), dikirim melalui kabel fiber optik, dan dibaca kembali oleh aplikasi web di sisi kanan (Deserialisasi)].
  * **2.2 Relasi Multi-Tabel & Query Tingkat Lanjut:**
    * Relasi *One-to-Many* dan *Many-to-Many* menggunakan tabel perantara (*Junction Table*).
    * Perintah `INNER JOIN`, `LEFT JOIN`, dan fungsi agregat (`COUNT`, `AVG`, `HAVING`).
  * **2.3 Konsep Arsitektur REST API:**
    * Protokol HTTP: Endpoint URL, Status Codes (200 OK, 404 Not Found, 500 Server Error), dan Metode HTTP (GET, POST, PUT, DELETE).
  * **2.4 LKPD Plugged: "Membangun Web Service REST API Menggunakan Python Flask/FastAPI"**
    * Praktikum membuat server API mini yang melayani data siswa dan nilai ujian dalam format respons JSON.
  * **2.5 Keamanan Basis Data & Pencegahan Serangan Siber:**
    * Bahaya serangan *SQL Injection* dan teknik pencegahan menggunakan *Parameterized Query*.
    * Pengamanan kata sandi pengguna menggunakan teknik Hashing (*Bcrypt / SHA-256*).
  * **Pojok Karakter & Etika:** Kepatuhan terhadap UU Perlindungan Data Pribadi (UU PDP): Prinsip pembatasan akses data pengguna (*Integritas & Hukum*).
  * **Rangkuman Bab 2**
* **Paket Soal Evaluasi Bab 2 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus JSON & Query JOIN):* Menganalisis skrip query SQL untuk mendeteksi celah kerentanan SQL Injection; memilih metode HTTP yang tepat saat menambahkan data baru.
  * *Uraian (5 Soal):* Jelaskan perbedaan enkripsi dua arah vs hashing satu arah; tuliskan perintah SQL JOIN untuk menampilkan nama siswa beserta nama mata pelajaran yang diikutinya!
  * *Tugas Unjuk Kerja Proyek:* Membangun REST API Basis Data Sekolah Terverifikasi Aman.
* **Bagian Buku Panduan Guru (BG) Bab 2:**
  * Panduan demonstrasi simulasi kerentanan SQL injection dalam lingkungan lokal yang terkontrol.
  * Kunci jawaban soal pilihan ganda dan rubrik pengujian endpoint API.

### BAB 3: Kolaborasi Multimedia Tingkat Lanjut untuk Pendukung Aplikasi (15 JP - 3 Pertemuan @ 5 JP)
* **Elemen CP:** Literasi Digital (LD)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu merancang dan menyusun aset visual antarmuka pengguna (UI Assets) terstandar (8 JP).
  2. Murid mampu menyusun dokumentasi teknis perangkat lunak (*Technical Writing*) dan materi pitching produk (7 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa keindahan kode tidak akan bermanfaat jika pengguna kesulitan memahami antarmuka aplikasi.
  * *Meaningful:* Membuat panduan pengguna (*user manual*) yang ramah bagi orang awam.
  * *Joyful:* Melakukan simulasi pitching produk di hadapan teman sekelas layaknya founder startup digital.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **3.1 Desain Aset Antarmuka Pengguna (UI/UX Assets):**
    * Pemanfaatan grafik vektor SVG, tata letak responsif, dan palet warna kontras aksesibel.
  * **3.2 Penyusunan Dokumentasi Teknis Profesional:**
    * Standar file `README.md` repositori GitHub, panduan instalasi dependensi (`requirements.txt`), dan dokumentasi API.
  * **3.3 Seni Melakukan Pitching & Demo Produk Perangkat Lunak:**
    * Menyusun slide presentasi demo produk yang komunikatif, ringkas, dan fokus pada nilai manfaat bagi pengguna.
  * **3.4 LKPD Praktikum: "Penyusunan Dokumentasi Repositori & Video Demo Aplikasi"**
  * **Pojok Karakter & Etika:** Keterbukaan informasi dan menolak klaim palsu (*no overpromising*) pada produk perangkat lunak (*Komunikasi & Integritas*).
  * **Rangkuman Bab 3**
* **Paket Soal Evaluasi Bab 3 (HOTS):**
  * *Pilihan Ganda (10 Soal):* Memilih komponen dokumentasi teknis yang wajib ada pada repositori open source; menganalisis tata letak UI yang melanggar hierarki visual.
  * *Uraian (5 Soal):* Jelaskan mengapa file `requirements.txt` sangat krusial dalam replikasi proyek perangkat lunak di komputer lain!
  * *Tugas Proyek Mini Akhir Semester 1:* Portofolio Repositori GitHub Terpadu Lengkap dengan Dokumentasi dan Video Demo.
* **Bagian Buku Panduan Guru (BG) Bab 3:**
  * Panduan evaluasi presentasi pitching siswa dengan rubrik komunikasi persuasif.
  * Kunci jawaban soal dan rubrik penilaian dokumentasi teknis.

---

## III. SEMESTER 2: FONDASI MACHINE LEARNING, NLP, & TATA KELOLA HUMAN-CENTERED (90 JP)

### BAB 4: Fondasi Machine Learning: Pipeline, Klasifikasi, & Evaluasi Model (40 JP - 8 Pertemuan @ 5 JP)
* **Elemen CP:** Pemanfaatan dan Pengembangan Kecerdasan Artifisial (PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami taksonomi Machine Learning dan tahapan siklus kerja (*pipeline*) pembelajaran mesin (10 JP).
  2. Murid mampu menerapkan algoritma klasifikasi terawasi (*KNN dan Decision Tree*) menggunakan pustaka Scikit-Learn (18 JP).
  3. Murid mampu mengevaluasi kinerja model secara objektif menggunakan Matriks Konfusi (*Confusion Matrix*) (12 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari bahwa mesin tidak pernah 'berpikir' secara magis, melainkan melakukan optimasi statistik matematika.
  * *Meaningful:* Membangun model prediksi kelayakan beasiswa atau model pendeteksi penyakit diabetes berdasarkan data klinis.
  * *Joyful:* Melihat grafik pohon keputusan (*Decision Tree*) terbentuk dan mengamati bagaimana komputer memisahkan data secara cerdas.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **4.1 Taksonomi Pembelajaran Mesin:**
    * Perbedaan *Rule-Based Programming* (Aturan + Data -> Jawaban) vs *Machine Learning* (Data + Jawaban -> Aturan).
    * *Supervised Learning* (Klasifikasi & Regresi), *Unsupervised Learning* (Klastering), dan *Reinforcement Learning*.
    * [PROMPT GAMBAR ILUSTRASI: Diagram alir alur kerja Machine Learning Pipeline: 1. Dataset mentah -> 2. Pembersihan Data -> 3. Train-Test Split (80:20) -> 4. Pelatihan Algoritma -> 5. Evaluasi Confusion Matrix -> 6. Model Siap Pakai].
  * **4.2 Tahapan Pra-pemrosesan Data (*Data Preprocessing*):**
    * Menangani nilai hilang (*Missing Values*), pengkodean label kategori (*Label Encoding / One-Hot Encoding*), dan penskalaan fitur (*Feature Scaling*).
    * Memisahkan data latih dan data uji (*Train-Test Split*) untuk mencegah kebocoran data (*data leakage*).
  * **4.3 Eksplorasi Algoritma Klasifikasi:**
    * *K-Nearest Neighbors (KNN):* Menghitung jarak terdekat (Euclidean Distance) dan menentukan nilai k optimal.
    * *Decision Tree (Pohon Keputusan):* Konsep Gini Impurity dan Information Gain dalam menentukan akar keputusan (*root node*).
  * **4.4 LKPD Laboratorium: "Melatih Model Klasifikasi dengan Python Scikit-Learn"**
    * Praktikum memuat dataset CSV dengan Pandas, melatih model KNN, dan melakukan prediksi data pasien baru.
  * **4.5 Evaluasi Objektif: Matriks Konfusi (*Confusion Matrix*):**
    * Menghitung dan menganalisis: *Accuracy*, *Precision*, *Recall*, dan *F1-Score*.
    * Mengapa Akurasi tinggi bisa menipu pada dataset kanker yang sangat timpang? (Studi kasus False Negative vs False Positive).
  * **Pojok Karakter & Etika:** Bahaya Overfitting dan Underfitting; menolak penggunaan data latih yang memuat prasangka rasial atau bias gender (*Penalaran Kritis & Kemanusiaan*).
  * **Rangkuman Bab 4**
* **Paket Soal Evaluasi Bab 4 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Matriks Konfusi):* Diberikan tabel Confusion Matrix 2x2, siswa menghitung nilai Recall dan Precision model pendeteksi penipuan kartu kredit; menentukan nilai k terbaik pada KNN.
  * *Uraian (5 Soal):* Jelaskan mengapa data uji (*testing data*) tidak boleh dilihat oleh model saat proses pelatihan! Dalam sistem pendeteksi kebakaran hutan, mana yang lebih berbahaya: False Positive atau False Negative? Jelaskan alasannya!
  * *Tugas Unjuk Kerja Proyek:* Laporan Ilmiah Laboratorium: Pembangunan dan Evaluasi Model Klasifikasi Machine Learning.
* **Bagian Buku Panduan Guru (BG) Bab 4:**
  * Panduan mendampingi praktikum kode Python menggunakan Google Colab di sekolah.
  * Kunci jawaban soal perhitungan matriks konfusi dan rubrik evaluasi model AI siswa.

### BAB 5: Fondasi Pemrosesan Bahasa Alami (Natural Language Processing - NLP) (25 JP - 5 Pertemuan @ 5 JP)
* **Elemen CP:** Pemanfaatan dan Pengembangan Kecerdasan Artifisial (PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu memahami tahapan pra-pemrosesan teks manusia menjadi data komputasi (10 JP).
  2. Murid mampu membangun model analisis sentimen teks sederhana menggunakan teknik Bag of Words dan TF-IDF (10 JP).
  3. Murid mampu memahami konsep dasar arsitektur Transformer yang mendasari Large Language Models (5 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Menyadari kekayaan bahasa manusia yang sarat kearifan lokal, metafora, dan nuansa emosional.
  * *Meaningful:* Membangun sistem pemilah ulasan pelanggan atau sistem deteksi komentar perundungan di media sosial.
  * *Joyful:* Menguji kalimat sarkasme di program buatan sendiri dan melihat apakah model AI mampu mendeteksi sentimennya.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **5.1 Mengapa Komputer Kesulitan Memahami Bahasa Manusia?**
    * Ambiguitas kata, konteks ganda, dialek bahasa daerah, dan bahasa gaul (*slang*).
  * **5.2 Pipeline Pra-pemrosesan Teks (*Text Preprocessing*):**
    * *Case Folding* (menyeragamkan huruf kecil), *Tokenizing* (memecah kalimat jadi kata), *Stopwords Removal* (membuang kata sambung tak bermakna), dan *Stemming* (mengubah kata berimbuhan jadi kata dasar).
    * [PROMPT GAMBAR ILUSTRASI: Diagram alir visual teks: Kalimat 'Siswa-siswa SANGAT menyukai pembelajaran koding!' diolah melalui corong penyaring: diubah huruf kecil -> dipotong per kata -> dibuang kata sambung -> menghasilkan kata dasar bersih ['siswa', 'suka', 'ajar', 'koding']].
  * **5.3 Vektorisasi Teks: Mengubah Kata Menjadi Angka**
    * *Bag of Words (BoW):* Menghitung frekuensi kemunculan kata dalam dokumen.
    * *TF-IDF:* Memberi bobot tinggi pada kata unik yang bernilai informasi dan bobot rendah pada kata pasaran.
  * **5.4 LKPD Laboratorium: "Membangun Model Analisis Sentimen Ulasan Aplikasi Sekolah"**
    * Praktikum melatih model Naive Bayes / Decision Tree untuk mengklasifikasi ulasan positif vs negatif secara otomatis.
  * **5.5 Mengenal Arsitektur Transformer & Mekanisme Perhatian (*Attention Mechanism*):**
    * Konsep dasar bagaimana model ChatGPT memahami keterkaitan antar kata dalam kalimat panjang.
  * **Pojok Karakter & Etika:** Menjaga kebebasan berekspresi: Membedakan kritik konstruktif masyarakat vs ujaran kebencian (*Hate Speech*) (*Keadaban & Tanggung Jawab Sosial*).
  * **Rangkuman Bab 5**
* **Paket Soal Evaluasi Bab 5 (HOTS):**
  * *Pilihan Ganda (10 Soal Berstimulus Vektorisasi Teks):* Menghitung nilai Term Frequency kata tertentu dalam paragraf; menentukan tahapan pra-pemrosesan teks yang tepat untuk menangani kata berimbuhan bahasa Indonesia.
  * *Uraian (5 Soal):* Mengapa kata sambung seperti 'dan', 'di', 'dari' wajib dibuang pada analisis sentimen teks? Jelaskan kelemahan representasi Bag of Words dalam menangani kalimat negatif ganda!
  * *Tugas Unjuk Kerja Proyek:* Membangun Skrip Python Analisis Sentimen Opini Publik Media Daring.
* **Bagian Buku Panduan Guru (BG) Bab 5:**
  * Panduan instalasi library NLP bahasa Indonesia (Sastrawi/NLTK).
  * Kunci jawaban soal pilihan ganda dan rubrik penilaian skrip analisis sentimen.

### BAB 6: Dampak Sosio-Teknologi AI, Ketenagakerjaan, & Etika Pengembang (25 JP - 5 Pertemuan @ 5 JP)
* **Elemen CP:** Literasi dan Etika Kecerdasan Artifisial (LEKA)
* **Tujuan Pembelajaran (TP):**
  1. Murid mampu menganalisis dampak disrupsi AI terhadap ketenagakerjaan dan struktur ekonomi nasional (10 JP).
  2. Murid mampu menerapkan prinsip-prinsip etika pengembang sistem AI berpusat pada manusia (*Human-Centered AI*) (15 JP).
* **Integrasi Pembelajaran Mendalam (PM):**
  * *Mindful:* Merenungkan posisi diri sebagai calon ilmuwan dan pemimpin bangsa di tengah era otomasi global.
  * *Meaningful:* Mengkaji nasib pekerja lokal di sekitar daerah dan merumuskan strategi pemberdayaan teknologi yang adil.
  * *Joyful:* Menyusun deklarasi integritas koding dan memamerkan proyek akhir dalam festival sains kelas.
* **Uraian Sub-Bab & Panduan Ilustrasi:**
  * **6.1 Disrupsi Ketenagakerjaan & Konsep Augmented Intelligence:**
    * Mengapa profesi repetitif terancam otomasi? Pergeseran menuju pekerjaan berbasis empati, analisis mendalam, dan kepemimpinan etis.
    * Kolaborasi manusia + AI: Manusia mengarahkan dan mengevaluasi, AI mengeksekusi komputasi berat.
  * **6.2 Standar Etika Pengembang Sistem Cerdas:**
    * *Transparency & Explainability:* Pengguna berhak mengetahui dasar logika keputusan yang diambil oleh sistem AI (*No Black Box tyranny*).
    * *Privacy & Data Governance:* Kepatuhan ketat terhadap hak pengguna atas datanya sendiri.
    * *Safety & Reliability:* Pengujian ketat agar sistem tahan terhadap manipulasi data jahat (*adversarial attacks*).
  * **6.3 LKPD Proyek Akhir Fase F (Tingkat Pertama): "Pengembangan Prototipe Model AI Solusi Sosial/Kejuruan"**
    * Tugas proyek kelompok 4 siswa: Membangun prototipe model klasifikasi Machine Learning / NLP terintegrasi untuk menyelesaikan masalah nyata di bidang pertanian lokal, layanan kesehatan desa, atau efisiensi energi sekolah.
  * **6.4 Gelar Karya Model Cerdas & Sidang Evaluasi Portofolio Kelas XI**
  * **Pojok Karakter & Etika:** Piagam Integritas Pengembang Muda Indonesia: Berjanji mengabdi demi kemaslahatan rakyat dan menolak menciptakan algoritma yang memecah belah bangsa (*Profil Pelajar Pancasila*).
  * **Rangkuman Bab 6 & Refleksi Pembelajaran Fase F Tingkat Pertama**
* **Paket Soal Evaluasi Akhir Tahun (Sumatif Fase F Kelas 11):**
  * *Pilihan Ganda Terstandar (15 Soal):* Soal komprehensif tahunan (OOP Python, REST API, ML Pipeline, Confusion Matrix, NLP Text Preprocessing, Etika Human-Centered).
  * *Uraian Kasus Terpadu (5 Soal):* Membedah kegagalan sistem AI dalam seleksi tenaga kerja dan merumuskan audit etika perbaikannya.
  * *Rubrik Penilaian Portofolio Akhir:* Standar evaluasi kesiapan kompetensi siswa menuju tingkat akhir (Kelas 12).
* **Bagian Buku Panduan Guru (BG) Bab 6:**
  * Panduan memfasilitasi sidang presentasi model AI siswa dengan panel penguji eksternal/guru mata pelajaran lain.
  * Kunci jawaban lengkap ujian akhir tahun dan rubrik penilaian portofolio model AI.

---

## IV. STRUKTUR BAGIAN AKHIR BUKU (POSTLIMINARIES)
* **Glosarium Istilah Tingkat Menengah Lanjut**
* **Kunci Jawaban Uji Pemahaman Pilihan Ganda Terpilih**
* **Daftar Pustaka Standar Kurikulum Nasional & Jurnal Internasional Acuan**
* **Indeks Istilah Komputasi & AI**
* **Profil Tim Penulis, Reviewer Akademik, Editor, dan Fasilitator TOT**
