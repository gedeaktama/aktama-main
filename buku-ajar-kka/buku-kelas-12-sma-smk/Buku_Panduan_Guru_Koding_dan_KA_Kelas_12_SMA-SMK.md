# PANDUAN GURU: KODING DAN KECERDASAN ARTIFISIAL

## KELAS XII SMA/SMK (FASE F TINGKAT AKHIR)

**Penulis:**
Gede Erik Aktama, S.Pd., M.Pd.

**Penerbit:**
PT Aktama Mega Persada
Bekerja sama dengan Tim Pengembang Kurikulum Koding dan Kecerdasan Artifisial

---

# BAGIAN I: PANDUAN UMUM PEMBELAJARAN FASE F TINGKAT AKHIR

## 1. Latar Belakang dan Karakteristik Mata Pelajaran KKA Kelas XII

Mata pelajaran Koding dan Kecerdasan Artifisial (KKA) pada jenjang Kelas XII SMA/MA/SMK merupakan tingkat puncak kelulusan (*capstone phase*) dari seluruh struktur kurikulum pendidikan menengah. Di fase ini, peserta didik tidak lagi memelajari konsep komputasi secara terisolasi, melainkan ditantang untuk menyatukan seluruh kompetensi rekayasa perangkat lunak, sistem siber-fisik, penambangan mahadata, dan jaringan saraf tiruan (*Deep Learning*) menjadi satu kesatuan solusi sistemik yang berdampak nyata bagi masyarakat (*Community-Engaged Engineering*).

Fokus kurikulum KKA Kelas XII berpusat pada empat tonggak revolusi industri:
1. **Komputasi Fisik Siber-Fisik (IoT & Edge AI):** Menghubungkan dunia nyata dan komputasi awan menggunakan mikrokontroler (ESP32), protokol telemetri hemat daya (MQTT), serta eksekusi model cerdas berdaya rendah di ujung perangkat (*TinyML*).
2. **Rekayasa Mahadata (Big Data 5V & Data Mining):** Mengelola volume data berskala besar, membedakan arsitektur penyimpanan (SQL vs NoSQL vs Data Lake), serta menerapkan algoritma klastering tak terawasi (*K-Means*) dengan optimasi metode siku (*Elbow Method*).
3. **Pembelajaran Mendalam (Deep Learning CNN & Transfer Learning):** Memahami arsitektur neuron tiruan (ANN), merancang Convolutional Neural Network untuk visi komputer, menerapkan strategi Transfer Learning model industri (MobileNet/ResNet), serta menjunjung tinggi prinsip efisiensi energi (*Green AI*).
4. **Capstone Project & Tata Kelola Global:** Memimpin pengembangan sistem multi-lapisan terintegrasi bermitra dengan UMKM/komunitas lokal, melaksanakan audit etika berbasis standar UNESCO 2021 dan UU PDP No. 27/2022, serta menyusun portofolio digital profesional di GitHub dan pameran inovasi nasional (*Showcase Day*).

## 2. Pendekatan Pembelajaran Mendalam (Deep Learning Pedagogies)

Guru diarahkan untuk menerapkan tiga pilar pedagogis Pembelajaran Mendalam:
- **Mindful Learning (Berkesadaran):** Menuntun peserta didik untuk merefleksikan konsekuensi etis, sosial, dan hukum dari setiap baris kode yang mereka bangun. Mengapa privasi data warga harus dilindungi secara mutlak, mengapa model deteksi penyakit wajib memprioritaskan metrik recall, dan mengapa algoritma tidak boleh mengambil keputusan otonom tanpa pengawasan manusia (*Human-in-the-Loop*).
- **Meaningful Learning (Bermakna):** Mengaitkan setiap praktikum laboratorium dengan konteks riil masyarakat Indonesia, seperti memecahkan masalah hama pertanian hortikultura, efisiensi rute kapal nelayan maritim tradisional, dan mitigasi bencana alam.
- **Joyful Learning (Menggembirakan):** Membangun lingkungan belajar yang suportif melalui dinamika kerja tim Scrum Agile, eksperimen perangkat keras sensor yang menyala dan merespons sentuhan fisik secara otomatis, serta antusiasme menyongsong pameran karya inovasi akbar (*Showcase Day*).

## 3. Integrasi Profil Pelajar Pancasila

- **Beriman, Bertakwa kepada Tuhan YME, dan Berakhlak Mulia:** Menjunjung integritas ilmiah, menolak memalsukan data hasil evaluasi akurasi, dan berkomitmen menciptakan teknologi yang memuliakan martabat kemanusiaan.
- **Bernalar Kritis:** Mampu mengaudit bias tersembunyi pada dataset publik, mengevaluasi arsitektur sistem komputasi multi-tier, dan menganalisis trade-off antara akurasi model dan efisiensi konsumsi daya komputasi.
- **Kreatif:** Merancang purwarupa sistem siber-fisik inovatif, merangkai antarmuka pengguna yang ramah bagi masyarakat awam, dan menyusun presentasi poster ilmiah berstandar internasional.
- **Bergotong Royong:** Mempraktikkan kolaborasi lintas peran (Lead Architect, IoT Engineer, AI Specialist, UI Designer) dalam manajemen sprint Capstone Project.
- **Mandiri:** Mengelola portofolio profesional di GitHub, memecahkan kendala teknis perangkat keras secara sistematis, dan menunjukkan etos pembelajar sepanjang hayat (*Lifelong Learner*).
- **Berkebinekaan Global:** Menyelaraskan karya inovasi lokal dengan standar tata kelola etika kecerdasan artifisial dunia (UNESCO Recommendation on the Ethics of AI dan EU AI Act).

---

# BAGIAN II: STRATEGI PEMBELAJARAN PER BAB DAN ALOKASI WAKTU

Mata pelajaran KKA Fase F Kelas XII dirancang dengan alokasi total **160 Jam Pelajaran (JP)** dalam satu tahun ajaran (32 minggu efektif @ 5 JP per minggu):

## Matriks Distribusi Alokasi Waktu:
- **Semester 1 (80 JP):**
  - Bab I: Pemrograman Perangkat Keras Cerdas: Internet of Things (IoT) Terhubung AI (45 JP / 9 Pertemuan @ 5 JP)
  - Bab II: Mahadata (Big Data) dan Rekayasa Analisis Skala Besar (35 JP / 7 Pertemuan @ 5 JP)
- **Semester 2 (80 JP):**
  - Bab III: Pengembangan Model AI Lanjut dan Fondasi Deep Learning (35 JP / 7 Pertemuan @ 5 JP)
  - Bab IV: Proyek Akhir Terpadu (Capstone Project): Sistem AI Human-Centered (35 JP / 7 Pertemuan @ 5 JP)
  - Bab V: Diseminasi Karya, Tata Kelola Global, dan Kesiapan Karier Digital (10 JP / 2 Pertemuan @ 5 JP)

### Panduan Teknis Pelaksanaan Tiap Bab bagi Guru:

#### Bab I: Pemrograman Perangkat Keras Cerdas (IoT & Edge AI)
- **Fokus Utama:** Arsitektur 3 lapisan IoT, sirkuit mikrokontroler ESP32, aktuator relay daya tinggi, perbandingan protokol MQTT vs HTTP, dan paradigma Edge AI.
- **Keselamatan Kerja:** Guru wajib memastikan siswa menggunakan sumber daya tegangan rendah (DC 3.3V - 5V) saat merangkai breadboard dan tidak menyentuh terminal kabel listrik AC saat menguji relay.
- **Troubleshooting:** Jika ESP32 gagal mengunggah program, pastikan tombol *BOOT* pada papan ditekan saat proses koneksi serial di Arduino IDE.

#### Bab II: Mahadata (Big Data) & Rekayasa Analisis Skala Besar
- **Fokus Utama:** Karakteristik 5V, basis data NoSQL MongoDB vs PostgreSQL, algoritma klastering K-Means, penentuan k optimal dengan Elbow Method, serta etika data UU PDP No. 27/2022.
- **Tips Guru:** Bimbing siswa menggunakan pustaka Scikit-Learn dan Pandas di Google Colaboratory. Tekankan pentingnya penskalaan fitur (*StandardScaler*) sebelum jarak Euclidean dihitung agar fitur berangka jutaan tidak mendistorsi klaster.

#### Bab III: Pengembangan Model AI Lanjut & Deep Learning
- **Fokus Utama:** Konsep ANN, fungsi aktivasi ReLU dan Softmax, lapisan Convolutional & Max Pooling pada CNN, strategi Transfer Learning (MobileNetV2), dan etika Green AI.
- **Tips Guru:** Manfaatkan fasilitas GPU gratis di Google Colab (*Runtime > Change runtime type > T4 GPU*) agar pelatihan model berjalan cepat tanpa membebani fasilitas komputer sekolah.

#### Bab IV: Capstone Project Sistem AI Human-Centered
- **Fokus Utama:** Kemitraan dengan mitra UMKM/masyarakat, integrasi 4 lapisan (UI + REST API + AI Engine + Database), pengujian sistem (Functional, Stress, UAT), dan audit etika pengawasan manusia (*Human-in-the-Loop*).
- **Peran Guru:** Guru bertindak sebagai fasilitator dan penghubung (*liaison*) antara sekolah dan mitra eksternal. Pastikan siswa mematuhi etika saat mewawancarai mitra di lapangan.

#### Bab V: Diseminasi Karya, Tata Kelola Global, & Kesiapan Karier
- **Fokus Utama:** Rekomendasi Etika AI UNESCO 2021, EU AI Act, SE Menkominfo No. 9/2023, standar stan Showcase Day nasional, kurasi portofolio GitHub, dan CV ramah ATS.
- **Tips Guru:** Fasilitasi simulasi sidang tugas akhir dan pameran kelas sebelum pameran akbar sekolah digelar. Undang orang tua siswa dan pelaku industri lokal untuk memberikan evaluasi autentik.

---

# BAGIAN III: RUBRIK PENILAIAN AUTENTIK DAN EVALUASI HASIL BELAJAR

## 1. Rubrik Penilaian Capstone Project Multi-Lapisan (Skala 1 - 4)

1. **Relevansi Solusi & Kemitraan Komunitas (Bobot 20%):**
   - Skor 4: Solusi memecahkan titik masalah (*pain point*) riil mitra nyata dengan bukti lembar wawancara dan persetujuan UAT mitra di atas 85%.
   - Skor 3: Solusi relevan dengan masalah mitra, namun keterlibatan mitra masih bersifat sekunder.
   - Skor 2: Masalah bersifat hipotetis atau simulasi tanpa interaksi dengan mitra pengguna nyata.
   - Skor 1: Solusi tidak jelas dan tidak relevan dengan kebutuhan pengguna mana pun.

2. **Kualitas Rekayasa Sistem Multi-Lapisan (Bobot 30%):**
   - Skor 4: Mengintegrasikan secara harmonis 4 lapisan (UI/Hardware + Backend REST API + Model AI/Edge AI + Basis Data) dengan penanganan galat (*exception handling*) dan sanitasi keamanan yang ketat.
   - Skor 3: Mengintegrasikan 3 lapisan dengan baik, namun integrasi basis data atau keamanan API masih terbatas.
   - Skor 2: Sistem hanya berjalan sebagai skrip tunggal lokal (*monolithic script*) tanpa REST API terstandar.
   - Skor 1: Perangkat keras atau kode program mengalami kegagalan fungsi (*crash*) saat diuji.

3. **Performa Model AI & Efisiensi Hijau / Green AI (Bobot 25%):**
   - Skor 4: Model mencapai metrik Akurasi/Recall di atas 90% pada data uji independen, menggunakan arsitektur ringkas (seperti MobileNet berbasis Transfer Learning), dan waktu inferensi di bawah 100 milidetik.
   - Skor 3: Akurasi model di atas 80%, namun model berukuran terlalu besar atau waktu inferensi lambat.
   - Skor 2: Akurasi model rendah (60-79%) atau mengalami indikasi overfitting parah.
   - Skor 1: Model gagal mengklasifikasikan data masukan.

4. **Kepatuhan Etika, Privasi Data, dan Human-in-the-Loop (Bobot 15%):**
   - Skor 4: Menerapkan enkripsi data, mematuhi prinsip anonimisasi UU PDP No. 27/2022, menyediakan tombol intervensi manual manusia (*override*), dan mendokumentasikan analisis bias dataset.
   - Skor 3: Menerapkan proteksi privasi standar, namun mekanisme pengawasan manusia belum terdokumentasi optimal.
   - Skor 2: Tidak ada mekanisme pengawasan manusia, kunci rahasia API ditulis langsung dalam kode publik.
   - Skor 1: Mengabaikan prinsip privasi data pengguna sama sekali.

5. **Dokumentasi Portofolio GitHub & Presentasi Pameran (Bobot 10%):**
   - Skor 4: Repositori GitHub memiliki berkas `README.md` sangat profesional, badge status, diagram arsitektur, panduan instalasi lengkap, lisensi terbuka, serta presentasi pameran memukau dengan live demo interaktif.
   - Skor 3: Repositori lengkap dengan README standar dan poster pameran informatif.
   - Skor 2: Dokumentasi minim, berkas README hanya berisi deskripsi satu paragraf.
   - Skor 1: Tidak memiliki repositori GitHub atau dokumentasi proyek.

---

# BAGIAN IV: KUNCI JAWABAN LENGKAP DAN PEMBAHASAN BUKU SISWA

Guru dapat mengacu pada kunci jawaban resmi yang telah tertera secara mendalam pada setiap akhir bab di Buku Siswa:
- **Bab I:** 10 Soal Pilihan Ganda (Kunci: 1.B, 2.B, 3.B, 4.C, 5.C, 6.B, 7.C, 8.B, 9.B, 10.B) dan 5 Soal Uraian Komputasi Fisik.
- **Bab II:** 10 Soal Pilihan Ganda (Kunci: 1.B, 2.C, 3.B, 4.B, 5.C, 6.B, 7.C, 8.D, 9.B, 10.B) dan 5 Soal Uraian Rekayasa Mahadata.
- **Bab III:** 10 Soal Pilihan Ganda (Kunci: 1.B, 2.C, 3.B, 4.B, 5.B, 6.B, 7.C, 8.C, 9.B, 10.C) dan 5 Soal Uraian Deep Learning.
- **Bab IV:** 10 Soal Pilihan Ganda (Kunci: 1.B, 2.C, 3.C, 4.B, 5.C, 6.C, 7.B, 8.A, 9.C, 10.B) dan 5 Soal Uraian Capstone Project.
- **Bab V:** Evaluasi Akhir Jenjang 20 Soal Pilihan Ganda Komprehensif (Kunci: 1.B, 2.B, 3.C, 4.B, 5.B, 6.B, 7.C, 8.B, 9.B, 10.B, 11.C, 12.B, 13.B, 14.B, 15.A, 16.D, 17.B, 18.D, 19.C, 20.C) dan 5 Soal Uraian Studi Kasus Sistemik Tingkat Tinggi.

---

# BAGIAN V: PROFIL PENULIS

**Gede Erik Aktama, S.Pd., M.Pd.** lahir di Buleleng, Bali. Menyelesaikan pendidikan Sarjana (S1) pada Program Studi Pendidikan Teknik Informatika di Universitas Pendidikan Ganesha (UNDIKSHA) Singaraja, dan melanjutkan pendidikan Magister (S2) pada Program Studi Teknologi Pembelajaran di universitas yang sama dengan predikat kelulusan sangat memuaskan.

Saat ini penulis mengemban amanah akademis sebagai Dosen Lektor (SK Mendiktisaintek RI No. 0044/LL16/KP.07/2025) sekaligus Ketua Program Studi S1 Sistem Komputer di Fakultas Teknologi Informasi, Universitas Parna Raya (UNIPAR) Manado, Sulawesi Utara. Penulis aktif sebagai Fasilitator Nasional Bimbingan Teknis dan Training of Trainers (ToT) Pembelajaran Koding dan Kecerdasan Artifisial (KKA) di bawah naungan Kementerian Pendidikan Dasar dan Menengah Republik Indonesia.

Penulis memiliki kepakaran riset di bidang *Artificial Intelligence in Education*, *Cyber-Physical Systems*, *Deep Learning*, dan *Human-Centered Computing*. Penulis secara konsisten mendedikasikan keahliannya untuk merancang kurikulum dan materi ajar teknologi cerdas yang berpusat pada pembentukan karakter unggul generasi emas Indonesia menuju peradaban dunia yang berkeadilan dan bermartabat.
