# PANDUAN GURU: KODING DAN KECERDASAN ARTIFISIAL

## KELAS XI SMA/SMK (FASE F)

**Penulis:**
Gede Erik Aktama, S.Pd., M.Pd.

**Penerbit:**
PT Aktama Mega Persada
Bekerja sama dengan Tim Pengembang Kurikulum Koding dan Kecerdasan Artifisial

---

# BAGIAN I: PANDUAN UMUM PEMBELAJARAN FASE F KELAS XI

## 1. Latar Belakang dan Karakteristik Mata Pelajaran KKA Fase F

Mata pelajaran Koding dan Kecerdasan Artifisial (KKA) pada Fase F (Kelas XI SMA/MA/SMK) merupakan mata pelajaran kelompok pilihan yang dirancang untuk membekali peserta didik dengan kompetensi rekayasa tingkat menengah-lanjut (*intermediate-to-advanced engineering competencies*). Pada fase ini, peserta didik diarahkan untuk menguasai kompetensi yang memiliki keselarasan langsung (*direct alignment*) dengan kebutuhan industri teknologi informasi global dan riset sains data modern.

Fokus pembelajaran Fase F Kelas XI menitikberatkan pada tiga pilar utama:
1. **Rekayasa Perangkat Lunak Terstruktur:** Transisi dari pemrograman prosedural menuju paradigma Pemrograman Berorientasi Objek (*Object-Oriented Programming* / OOP), disiplin manajemen versi terdistribusi menggunakan Git dan platform kolaborasi GitHub, serta perancangan layanan web mandiri (*RESTful API*).
2. **Sains Data & Pembelajaran Mesin Terapan:** Penguasaan siklus kerja (*pipeline*) Machine Learning, mulai dari pra-pemrosesan data mentah, pencegahan kebocoran data (*data leakage*), pelatihan algoritma klasifikasi (KNN dan Decision Tree), hingga evaluasi objektif berbasis Matriks Konfusi (*Confusion Matrix*).
3. **Komputasi Bahasa Alami & Etika Human-Centered:** Pemahaman tahapan pengolahan teks manusia (NLP), pembobotan TF-IDF, arsitektur revolusioner Transformer, serta penegakan etika sistem cerdas yang adil, transparan (*Explainable AI*), dan taat pada Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022).

## 2. Pendekatan Pembelajaran Mendalam (Deep Learning Pedagogies)

Buku panduan guru ini mengarahkan pendidik untuk mengimplementasikan filosofi pembelajaran mendalam (*Deep Learning Approach*) melalui tiga pilar pengalaman belajar:
- **Mindful Learning (Berkesadaran):** Pendidik memfasilitasi siswa untuk memahami esensi logis dan filosofis dari setiap konstruksi kode yang dirancang. Siswa tidak sekadar menghafal sintaksis pustaka, melainkan menyadari mengapa enkapsulasi mencegah anomali korupsi data perbankan dan mengapa model dengan akurasi 98% bisa menjadi bumerang kegagalan jika nilai recall-nya rendah.
- **Meaningful Learning (Bermakna):** Mengaitkan seluruh penugasan koding dengan pemecahan masalah nyata di lingkungan sekolah, masyarakat lokal, dan dunia industri vokasi (seperti sistem antrean poliklinik, e-commerce kantin sekolah, dan model deteksi dini penyakit tanaman pangan lokal).
- **Joyful Learning (Menggembirakan):** Membangun atmosfer belajar yang kolaboratif dan menantang melalui kehadiran trio sahabat belajar (Arya, Dinda, dan Bagas), sesi *code review* antar-teman di GitHub, simulasi pitching produk startup digital di hadapan kelas, serta festival pameran sains AI sekolah.

## 3. Integrasi Profil Pelajar Pancasila

Proses pembelajaran KKA Fase F menginternalisasikan nilai-nilai Profil Pelajar Pancasila secara autentik:
- **Beriman, Bertakwa kepada Tuhan YME, dan Berakhlak Mulia:** Menjaga kejujuran data, menolak manipulasi data uji untuk menaikkan akurasi semu, menghormati hak cipta lisensi sumber terbuka, dan menolak pembuatan perangkat lunak peretas yang merugikan masyarakat.
- **Bernalar Kritis:** Menganalisis risiko False Negative pada sistem keselamatan, membedah jebakan dataset timpang, dan mengaudit bias diskriminasi pada algoritma AI.
- **Kreatif:** Mengembangkan solusi purwarupa mandiri berbasis pipeline ML/NLP, merancang aset antarmuka SVG yang estetis dan aksesibel, serta menyusun narasi pitching produk yang persuasif.
- **Bergotong Royong:** Berkolaborasi dalam tim rekayasa perangkat lunak, mengelola cabang kerja Git secara disiplin, dan saling mereview kode rekan sejawat secara konstruktif.
- **Mandiri:** Mengelola dependensi berkas `requirements.txt`, melakukan penelusuran dokumentasi teknis pustaka mandiri, dan menyelesaikan galat program secara metodis.
- **Berkebinekaan Global:** Menghargai keragaman bahasa nusantara dalam pemrosesan NLP serta mematuhi standar konsensus rekayasa teknologi internasional (WCAG, IEEE, dan UNESCO).

---

# BAGIAN II: STRATEGI PEMBELAJARAN PER BAB DAN ALOKASI WAKTU

Mata pelajaran KKA Fase F Kelas XI dirancang untuk alokasi total **180 Jam Pelajaran (JP)** dalam satu tahun ajaran (36 minggu efektif @ 5 JP per minggu). Berikut adalah distribusi alokasi waktu dan strategi pelaksanaan tiap bab:

## Matriks Distribusi Alokasi Waktu:
- **Semester 1 (90 JP):**
  - Bab I: Pemrograman Berorientasi Objek (OOP) dan Engineering Process (40 JP / 8 Pertemuan)
  - Bab II: Rekayasa Basis Data Terintegrasi, Data Encoding, dan REST API (35 JP / 7 Pertemuan)
  - Bab III: Kolaborasi Multimedia Tingkat Lanjut untuk Pendukung Aplikasi (15 JP / 3 Pertemuan)
- **Semester 2 (90 JP):**
  - Bab IV: Fondasi Machine Learning: Pipeline, Klasifikasi, dan Evaluasi Model (40 JP / 8 Pertemuan)
  - Bab V: Fondasi Pemrosesan Bahasa Alami (Natural Language Processing - NLP) (25 JP / 5 Pertemuan)
  - Bab VI: Dampak Sosio-Teknologi AI, Ketenagakerjaan, dan Etika Pengembang (25 JP / 5 Pertemuan)

### Panduan Teknis Pelaksanaan Tiap Bab:

#### Bab I: Pemrograman Berorientasi Objek & Engineering Process
- **Fokus Utama:** Paradigma Class & Object, metode `__init__()`, Enkapsulasi (`__atribut`), Pewarisan (`super()`), Polimorfisme (*method overriding*), alur kerja Git/GitHub.
- **Tips Guru:** Bimbing siswa membuat akun GitHub sekolah. Pastikan setiap siswa mempraktikkan pembuatan cabang kerja terpisah (*feature branch*) dan memahami mekanisme penggabungan (*merge*) tanpa konflik.

#### Bab II: Rekayasa Basis Data Terintegrasi, Data Encoding, & API
- **Fokus Utama:** Serialisasi JSON (`dumps` & `loads`), kueri relasional `JOIN` dan `GROUP BY`, protokol HTTP REST API (GET, POST, 200, 201, 404), Parameterized Query, dan Hashing kata sandi (UU PDP).
- **Tips Guru:** Lakukan simulasi demonstrasi bahaya serangan SQL Injection di komputer lokal yang terkontrol. Tunjukkan bagaimana sebuah tanda kutip `' OR '1'='1` dapat membobol sistem login jika kueri tidak diproteksi oleh *Parameterized Query*.

#### Bab III: Kolaborasi Multimedia Tingkat Lanjut untuk Pendukung Aplikasi
- **Fokus Utama:** Aset vektor SVG berbasis XML matematika, standar kontras aksesibilitas WCAG (minimal 4.5:1), penyusunan `README.md` dan `requirements.txt`, serta teknik pitching produk startup.
- **Tips Guru:** Fasilitasi simulasi sidang pitching produk 5 menit. Ajak siswa bertindak sebagai founder startup teknologi yang mempresentasikan karya solutif di hadapan panel investor/dewan guru.

#### Bab IV: Fondasi Machine Learning: Pipeline, Klasifikasi, & Evaluasi Model
- **Fokus Utama:** Pipeline ML Scikit-Learn, Train-Test Split (80:20), algoritma KNN dan Decision Tree, analisis Confusion Matrix (TP, TN, FP, FN), serta metrik Recall vs Presisi.
- **Tips Guru:** Gunakan analogi kasus medis tumor atau deteksi kebakaran hutan. Tekankan mengapa Akurasi bisa sangat menipu pada dataset timpang (*imbalanced data*) dan mengapa meminimalkan False Negative adalah parameter hidup-mati.

#### Bab V: Fondasi Pemrosesan Bahasa Alami (NLP)
- **Fokus Utama:** Alur pra-pemrosesan teks (Case Folding, Tokenizing, Stopwords, Stemming Sastrawi), pembobotan TF-IDF, serta konsep revolusioner arsitektur Transformer dan mekanisme Self-Attention.
- **Tips Guru:** Dampingi siswa dalam menguji teks ulasan berbahasa Indonesia. Tunjukkan bagaimana sebuah kata unik memperoleh skor TF-IDF tinggi, sementara kata sambung pasaran memperoleh skor mendekati nol.

#### Bab VI: Dampak Sosio-Teknologi AI, Ketenagakerjaan, & Etika Pengembang
- **Fokus Utama:** Disrupsi otomasi industri, konsep Augmented Intelligence, standar Human-Centered AI UNESCO, transparansi algoritma Explainable AI (XAI), dan mitigasi Adversarial Attacks.
- **Tips Guru:** Bimbing tim siswa menuntaskan Capstone Project akhir tahun. Selenggarakan festival gelar karya teknologi sekolah untuk memamerkan model cerdas buatan siswa kepada seluruh warga sekolah dan orang tua.

---

# BAGIAN III: RUBRIK ASESMEN DAN EVALUASI PEMBELAJARAN

## 1. Rubrik Penilaian Kinerja Koding OOP & Git Kolaboratif

| Aspek Penilaian | Skor 4 (Sangat Mahir) | Skor 3 (Mahir) | Skor 2 (Cukup) | Skor 1 (Perlu Bimbingan) |
| :--- | :--- | :--- | :--- | :--- |
| **Arsitektur OOP** | Menerapkan enkapsulasi privat, pewarisan bertingkat via `super()`, dan polimorfisme overriding secara tepat dan modular. | Menerapkan class dan pewarisan dasar, namun enkapsulasi belum konsisten. | Menggunakan class sederhana namun masih tercampur variabel global prosedural. | Gagal menerapkan konsep class dan struktur OOP. |
| **Disiplin Git/GitHub** | Melakukan commit terstruktur, menggunakan feature branch, dan membuat Pull Request rapi tanpa merge conflict. | Melakukan commit dan push mandiri, namun jarang menggunakan cabang terpisah. | Riwayat commit tidak teratur dan pesan commit tidak deskriptif. | Tidak mampu mengoperasikan perintah dasar Git di terminal. |
| **Keamanan Sistem** | Menerapkan parameterized query dan hashing kata sandi secara sempurna sesuai UU PDP. | Menerapkan parameterized query dasar pada sebagian besar kueri SQL. | Kueri SQL masih menggunakan konkatenasi string rawan injeksi. | Tidak ada mekanisme keamanan basis data sama sekali. |

## 2. Rubrik Evaluasi Model Machine Learning & NLP

- **Tahap Pembersihan & Preprocessing Data (Bobot 25%):** Ketepatan penanganan missing values, encoding teks/kategori, dan pencegahan data leakage pada train-test split.
- **Pelatihan & Optimasi Algoritma (Bobot 25%):** Pemilihan model yang tepat (KNN/Decision Tree/Naive Bayes) dan penyesuaian parameter (*hyperparameter tuning*).
- **Analisis Kritis Confusion Matrix (Bobot 30%):** Kemampuan membedah rasio TP, TN, FP, FN, serta perhitungan objektif nilai Recall, Presisi, dan F1-Score.
- **Audit Etika & Transparansi Explainable AI (Bobot 20%):** Ketiadaan bias diskriminasi dalam dataset dan kejelasan penjelasan logika keputusan model kepada manusia.

---

# BAGIAN IV: KUNCI JAWABAN LENGKAP DAN PEMBAHASAN PEDAGOGIS

Guru dapat merujuk pada kunci jawaban dan pembahasan analitis yang telah disusun secara lengkap di bagian akhir setiap bab pada Buku Siswa:
- **Bab I:** Kunci 10 Pilihan Ganda (1.C, 2.B, 3.C, 4.A, 5.C, 6.B, 7.B, 8.C, 9.B, 10.A) serta pembahasan 5 soal uraian.
- **Bab II:** Kunci 10 Pilihan Ganda (1.B, 2.B, 3.C, 4.B, 5.C, 6.B, 7.C, 8.C, 9.B, 10.A) serta pembahasan 5 soal uraian.
- **Bab III:** Kunci 10 Pilihan Ganda (1.C, 2.C, 3.C, 4.B, 5.B, 6.D, 7.C, 8.B, 9.B, 10.B) serta pembahasan 5 soal uraian.
- **Bab IV:** Kunci 10 Pilihan Ganda (1.B, 2.C, 3.B, 4.B, 5.B, 6.B, 7.C, 8.A, 9.B, 10.C) serta pembahasan 5 soal uraian.
- **Bab V:** Kunci 10 Pilihan Ganda (1.B, 2.B, 3.A, 4.B, 5.A, 6.C, 7.C, 8.B, 9.B, 10.B) serta pembahasan 5 soal uraian.
- **Bab VI / Evaluasi Akhir:** Kunci 15 Pilihan Ganda (1.C, 2.B, 3.C, 4.B, 5.B, 6.B, 7.B, 8.B, 9.B, 10.B, 11.C, 12.A, 13.B, 14.B, 15.C) serta pembahasan 5 soal studi kasus sistemik berbobot HOTS.

---

# BAGIAN V: PROFIL PENULIS BUKU PANDUAN GURU

[GAMBAR: assets/foto_penulis.jpg]

**Gede Erik Aktama, S.Pd., M.Pd.** adalah akademisi, inovator teknologi pembelajaran, dan peneliti sains komputer Indonesia. Beliau menamatkan studi Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika di Universitas Pendidikan Ganesha (UNDIKSHA) Singaraja, Bali, serta meraih gelar Magister Pendidikan (M.Pd.) dengan keahlian khusus pada rekayasa media pembelajaran digital interaktif dan sistem komputasi adaptif.

Saat ini beliau menjabat sebagai **Ketua Program Studi S1 Sistem Komputer** di Fakultas Sains dan Teknologi, Universitas Parna Raya (UNIPAR) Manado, Sulawesi Utara, dengan jabatan akademik fungsional **Lektor** berdasarkan Keputusan Menteri Pendidikan Tinggi, Sains, dan Teknologi RI Nomor: 0044/LL16/KP.07/2025.

Sebagai **Fasilitator Nasional Bimtek & Training of Trainers (ToT) Kurikulum KKA Kemendikdasmen RI**, beliau aktif membimbing pendidik di seluruh penjuru tanah air dalam mengimplementasikan pembelajaran koding tingkat lanjut, arsitektur basis data terintegrasi, machine learning, pemrosesan bahasa alami, dan etika kecerdasan artifisial yang bermakna, kontekstual, dan berintegritas tinggi demi melahirkan talenta emas Indonesia berdaulat digital.
