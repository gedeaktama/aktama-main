"""
Modul Naskah Frontmatter dan Postliminaries Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

FRONTMATTER_SMA10 = """# KODING DAN KECERDASAN ARTIFISIAL

## BUKU SISWA KELAS X SMA/SMK (FASE E)

**Penulis:**
Gede Erik Aktama, S.Pd., M.Pd.

**Penerbit:**
PT Aktama Mega Persada
Bekerja sama dengan Tim Pengembang Kurikulum Koding dan Kecerdasan Artifisial

---

# HAK CIPTA DAN KREDIT

**Judul Buku:** Koding dan Kecerdasan Artifisial untuk Siswa SMA/SMK Kelas X (Fase E)
**Penulis Utama:** Gede Erik Aktama, S.Pd., M.Pd.
**Penelaah Ahli:** Tim Pengembang Kurikulum Informatika & KKA Nasional
**Penyelia Penerbitan:** PT Aktama Mega Persada
**Desain Cover & Ilustrasi:** Tim Desain Visual Aktama Studio
**Tata Letak (Layout):** Tim Grafika dan Percetakan Komputasi

**Katalog Terbitan Kemendikdasmen RI:**
Hak cipta dilindungi oleh Undang-Undang Republik Indonesia Nomor 28 Tahun 2014 tentang Hak Cipta. Dilarang memperbanyak atau memindahkan sebagian atau seluruh isi buku ini dalam bentuk apa pun dan dengan cara apa pun, baik secara elektronik maupun mekanik, termasuk memfotokopi, merekam, atau dengan sistem penyimpanan lainnya, tanpa izin tertulis dari penerbit dan penulis, kecuali untuk kepentingan kutipan akademis dan tinjauan literatur ilmiah.

Edisi Pertama: Tahun 2025
Diterbitkan di: Manado, Sulawesi Utara
Ukuran Buku Standar Internasional: Format UNESCO (15,5 cm x 23,0 cm)

---

# PRAKATA

Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan karunia-Nya, sehingga buku ajar *Koding dan Kecerdasan Artifisial (KKA) untuk SMA/SMK Kelas X (Fase E)* ini dapat diselesaikan dengan standar mutu akademik dan pedagogis yang paripurna.

Era Revolusi Industri 4.0 dan transformasi digital abad ke-21 menempatkan kecerdasan artifisial (Artificial Intelligence/AI), komputasi awan, dan pemrosesan data skala besar sebagai lokomotif utama peradaban. Peserta didik pada jenjang Sekolah Menengah Atas (SMA) dan Sekolah Menengah Kejuruan (SMK) Fase E berada pada fase krusial: transisi dari pemahaman logika komputasi prosedural dasar menuju pemikiran abstraksi tingkat lanjut, perancangan arsitektur perangkat lunak, serta penerapan etika digital dan kecerdasan artifisial terapan dalam memecahkan permasalahan nyata di masyarakat dan dunia industri.

Buku ajar ini disusun secara berkesinambungan mengacu pada Kurikulum KKA yang diterbitkan oleh Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) RI. Pendekatan pembelajaran yang digunakan adalah *Deep Learning* (pembelajaran bermakna, kontekstual, dan menantang daya nalar tingkat tinggi/HOTS), didukung metode praktikum langsung berbasis proyek nyata (*Project-Based Learning*). Melalui kehadiran tiga sahabat belajar inspiratif—Arya (siswa SMA peminat sains komputasi dan matematika algoritma), Dinda (siswi peminat analisis data sosial, estetika multimedia, dan etika AI), serta Bagas (siswa SMK rekayasa perangkat lunak dan elektronika cerdas)—peserta didik diajak menjelajahi konsep-konsep inti Fase E:
1. Berpikir komputasional mendalam, perbandingan algoritma pencarian (Linear vs Binary Search), teknik pengurutan data, serta analisis efisiensi waktu asimptotik Big-O Notation.
2. Pemrograman Python terapan berbasis struktur data koleksi (List, Tuple, Set, Dictionary), mekanisme penanganan galat (*exception handling* `try-except`), dan disiplin kode bersih standar PEP 8.
3. Arsitektur basis data relasional, pemodelan ERD notasi Crow's Foot, eksekusi perintah SQL (DDL dan DML), serta integrasi database lokal `sqlite3` dengan bahasa Python.
4. Produksi konten multimedia interaktif berstandar profesional, manajemen resolusi (16:9 vs 9:16), bitrate, kompresi data, prinsip desain antarmuka berpusat pengguna (*User-Centered Design*), dan etika Hak Kekayaan Intelektual (HKI).
5. Pemahaman prinsip dasar Computer Vision melalui manipulasi matriks piksel warna RGB dan operasi konvolusi kernel, spektrogram frekuensi suara, serta peta ekosistem karier masa depan di ranah AI.
6. Rekayasa prompt cerdas (*Prompt Engineering*) tingkat lanjut dengan kerangka kerja ROCCF (*Role, Objective, Context, Constraint, Format*), strategi *Chain-of-Thought*, serta metode *Design Thinking* dalam merancang solusi sistemik kecerdasan artifisial yang etis, aman, dan berdaya guna.

Penulis menyampaikan apresiasi dan penghargaan yang setinggi-tingginya kepada Kemendikdasmen RI, Universitas Parna Raya (UNIPAR) Manado, para fasilitator nasional, pendidik informatika se-Indonesia, serta segenap tim redaksi yang telah berkontribusi mencurahkan dedikasi terbaik bagi terwujudnya buku ini. Semoga karya ini mampu menjadi jembatan akselerasi lahirnya generasi talenta emas Indonesia yang cakap digital, kreatif, inovatif, berintegritas moral, dan siap memimpin peradaban teknologi dunia.

Selamat belajar, bereksperimen, dan berinovasi!

Manado,   2025

**Gede Erik Aktama, S.Pd., M.Pd.**
*Penulis & Fasilitator Nasional KKA*

---

# PETUNJUK PENGGUNAAN BUKU

Buku ajar ini dirancang dengan tata letak visual modern, pedagogi bertahap, dan dilengkapi berbagai ikon panduan aktivitas belajar untuk memastikan pengalaman belajar yang menyenangkan, mendalam, dan terstruktur:

1. **Apersepsi & Komik Inspiratif:** Kisah ilustratif di setiap awal bab yang mengaitkan fenomena teknologi nyata dengan dilema komputasi yang dihadapi siswa.
2. **Uraian Konsep Matematis & Teknis:** Pembahasan konsep ilmiah secara runut, mendalam, dan gamblang, disertai diagram visual beresolusi tinggi 300 DPI.
3. **Eksplorasi Kode Python Terapan:** Blok kode program Python fungsional yang disertai ulasan baris demi baris, studi kasus kesalahan umum, dan petunjuk debugging.
4. **Laboratorium Komputasi Mandiri & Kelompok (LKPD):** Lembar Kerja Peserta Didik berbasis proyek nyata untuk mengasah keterampilan kolaboratif, logika kritis, dan kreasi rekayasa perangkat lunak.
5. **Zona Karakter & Integritas Digital:** Refleksi nilai-nilai moral, privasi data, kejujuran akademik, dan mitigasi bias dalam penerapan teknologi AI.
6. **Rangkuman Bab & Peta Konsep:** Intisari materi komprehensif untuk memudahkan pengulangan materi (*retrieval practice*).
7. **Uji Kompetensi Komprehensif:** 10 Soal Pilihan Ganda berbobot HOTS (*Higher Order Thinking Skills*) dan 5 Soal Uraian Pemecahan Kasus Nyata di setiap akhir bab, disertai kunci jawaban dan pembahasan analitis.

---

# MENGENAL TOKOH SAHABAT BELAJAR FASE E

Dalam perjalanan mempelajari Koding dan Kecerdasan Artifisial di Kelas X SMA/SMK ini, kalian akan didampingi oleh tiga sahabat muda yang penuh semangat inovasi:

[GAMBAR: assets/gambar_tokoh_sahabat_sma10.png]

1. **Arya (Siswa SMA Peminat Sains Komputasi & Matematika):**
Arya adalah sosok yang sangat gemar membedah struktur logika di balik program komputer. Ia terpesona oleh cara algoritma bekerja menghemat waktu eksekusi jutaan data, menganalisis kurva efisiensi Big-O, dan merancang kode Python yang bersih, terstruktur, serta berkinerja tinggi. Arya selalu menantang dirinya untuk mencari solusi komputasi yang paling optimal.

2. **Dinda (Siswi Peminat Analisis Sosial, Multimedia, & Etika AI):**
Dinda memiliki kepekaan rasa yang tinggi terhadap interaksi antara manusia dan teknologi. Ia menyukai visualisasi data, desain multimedia interaktif yang ramah pengguna (UI/UX), serta sangat peduli terhadap aspek sosial teknologi. Dinda selalu mengingatkan pentingnya etika, kejujuran data, perlindungan hak cipta, serta pencegahan bias diskriminatif dalam sistem kecerdasan artifisial.

3. **Bagas (Siswa SMK Peminat Rekayasa Perangkat Lunak & Sistem Cerdas):**
Bagas adalah siswa yang sangat menyukai penerapan teknologi langsung di ranah perangkat keras dan industri terapan. Ia gemar bereksperimen dengan basis data SQL, pengolahan matriks citra piksel (Computer Vision), pengenalan suara sensorik, serta perakitan prototipe berbasis Internet of Things (IoT). Bagas percaya bahwa teknologi cerdas harus mampu memecahkan masalah nyata di lingkungan sekolah dan dunia kerja.

---

# DAFTAR ISI

- Prakata
- Petunjuk Penggunaan Buku
- Mengenal Tokoh Sahabat Belajar Fase E
- Capaian Pembelajaran Fase E (KKA Kelas X)
- BAB I: Berpikir Komputasional dan Kompleksitas Algoritma
  - A. Konsep Pencarian Data: Linear Search vs Binary Search
  - B. Algoritma Pengurutan: Bubble Sort, Selection Sort, dan Insertion Sort
  - C. Analisis Kompleksitas Waktu Asimptotik (Big-O Notation)
  - D. LKPD 1.1: Komparasi Efisiensi Algoritma Pengurutan Berbasis Waktu Eksekusi
  - E. Rangkuman Materi Bab I
  - F. Uji Kompetensi Bab I (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB II: Pemrograman Python Terapan dan Struktur Data Koleksi
  - A. Struktur Data Koleksi Python: List, Tuple, Set, dan Dictionary
  - B. Mekanisme Penanganan Galat (Exception Handling) try-except-else-finally
  - C. Konvensi Penulisan Standar PEP 8 dan Teknik Debugging Mandiri
  - D. LKPD 2.1: Rancang Bangun Sistem Kasir Toko Retail Bebas Crash
  - E. Rangkuman Materi Bab II
  - F. Uji Kompetensi Bab II (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB III: Basis Data Relasional dan Perintah SQL
  - A. Fondasi Basis Data Relasional: Entitas, Atribut, Primary Key, dan Foreign Key
  - B. Perancangan Model Data: Entity Relationship Diagram (ERD) Notasi Crow's Foot
  - C. Sintaks Dasar SQL: Data Definition Language (DDL) dan Data Manipulation Language (DML)
  - D. Integrasi Database Relasional Python Menggunakan Modul Lokal sqlite3
  - E. LKPD 3.1: Proyek Sistem Inventarisasi Fasilitas Laboratorium Komputer Sekolah
  - F. Rangkuman Materi Bab III
  - G. Uji Kompetensi Bab III (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB IV: Produksi Konten Multimedia Interaktif dan Desain Antarmuka
  - A. Anatomi Multimedia Digital: Aspek Rasio (16:9 vs 9:16), Resolusi, dan Bitrate
  - B. Prinsip Kompresi Data: Lossless vs Lossy Audio-Visual
  - C. Prinsip Perancangan Desain Antarmuka Berpusat Pengguna (User-Centered Design)
  - D. Etika Digital, Hak Kekayaan Intelektual (HKI), dan Diseminasi Informasi Bertanggung Jawab
  - E. LKPD 4.1: Kampanye Publik Digital Sosialisasi Literasi AI untuk Komunitas Sekolah
  - F. Rangkuman Materi Bab IV
  - G. Uji Kompetensi Bab IV (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB V: Pengenalan Citra Digital (Computer Vision) dan Pola Audio AI
  - A. Representasi Citra Digital: Matriks Piksel Warna Merah, Hijau, dan Biru (RGB)
  - B. Operasi Konvolusi Dasar: Filter Kernel 3x3 untuk Deteksi Tepi (Edge Detection)
  - C. Representasi Suara Digital: Dari Gelombang Akustik ke Spektrogram Frekuensi
  - D. Peta Peluang Karier dan Lanskap Keahlian di Bidang Kecerdasan Artifisial
  - E. LKPD 5.1: Eksperimen Deteksi Pola Citra Piksel dan Spektrogram Suara Mandiri
  - F. Rangkuman Materi Bab V
  - G. Uji Kompetensi Bab V (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB VI: Rekayasa Prompt Tingkat Lanjut dan Perancangan Solusi Sistem AI
  - A. Kerangka Kerja Rekayasa Prompt Cerdas ROCCF (Role, Objective, Context, Constraint, Format)
  - B. Teknik Rekayasa Penalaran: Few-Shot Prompting dan Chain-of-Thought (CoT)
  - C. Perancangan Prototipe Sistem Berbasis AI Menggunakan Metode Design Thinking
  - D. Mitigasi Risiko Halusinasi AI, Keamanan Data Pribadi, dan Tanggung Jawab Moral Inovator
  - E. LKPD 6.1: Capstone Project Merancang Solusi Otomasi Berkelanjutan Sekolah Ramah Lingkungan
  - F. Rangkuman Materi Bab VI
  - G. Evaluasi Akhir Tahun Fase E (15 Soal PG, 5 Soal Pemecahan Kasus Sistemik, Kunci Jawaban)
- Glosarium Istilah Fase E
- Indeks Istilah
- Daftar Pustaka Resmi
- Profil Penulis

---

# CAPAIAN PEMBELAJARAN FASE E (KELAS X SMA/SMK)

Pada akhir Fase E, peserta didik memiliki pemahaman mendalam dan kecakapan komputasional terapan yang mencakup domain:
1. **Berpikir Komputasional (BK):** Mampu mengabstraksikan masalah kompleks, membandingkan efisiensi algoritma pencarian dan pengurutan data secara matematis, serta menganalisis kompleksitas waktu asimptotik Big-O untuk menentukan solusi paling efisien pada sistem komputasi berdaya tampung besar.
2. **Pemrograman & Struktur Data (PL):** Mahir menulis kode program fungsional terstruktur dalam bahasa Python, mengelola struktur data koleksi majemuk (List, Tuple, Set, Dictionary), menerapkan arsitektur penanganan kesalahan (*exception handling*) untuk mencegah program macet (*crash*), dan mematuhi konvensi tata kelola kode bersih standar industri (PEP 8).
3. **Sistem Informasi & Basis Data (SIBD):** Mampu merancang diagram hubungan antar-entitas (ERD) notasi Crow's Foot dengan relasi kunci (Primary Key & Foreign Key), mengeksekusi operasi basis data relasional standar (DDL dan DML), serta menghubungkan aplikasi perangkat lunak dengan basis data lokal relasional.
4. **Multimedia Interaktif & Desain UI/UX (MI):** Memahami karakteristik teknis media digital (resolusi, rasio aspek, bitrate, kompresi), menerapkan prinsip desain antarmuka berorientasi pengguna, serta memiliki kesadaran hukum dan etika terkait Hak Kekayaan Intelektual (HKI).
5. **Kecerdasan Artifisial & Pembelajaran Mesin Terapan (AI):** Memahami prinsip matematis pembentukan citra visual sebagai matriks angka piksel, cara kerja filter kernel konvolusi pada Computer Vision, representasi frekuensi suara pada spektrogram, serta mengenali prospek karier transformatif di era AI.
6. **Rekayasa Prompt & Solusi Sistemik AI (RP-SAI):** Terampil memformulasikan perintah multi-kondisi berstruktur ROCCF, memandu model penalaran kompleks menggunakan teknik *Chain-of-Thought*, serta mengintegrasikan metodologi *Design Thinking* untuk menciptakan solusi sistem cerdas yang berdampak positif bagi peradaban masyarakat.
"""

POSTLIMINARIES_SMA10 = """# GLOSARIUM ISTILAH FASE E

- **Aspek Rasio (Aspect Ratio):** Perbandingan proporsional antara lebar dan tinggi suatu tampilan media digital (misalnya 16:9 untuk format horizontal bioskop/laptop dan 9:16 untuk format vertikal smartphone).
- **Big-O Notation:** Notasi matematika formal yang digunakan dalam ilmu komputer untuk mendeskripsikan batas atas perilaku asimptotik dan efisiensi waktu eksekusi atau konsumsi memori suatu algoritma terhadap pertumbuhan ukuran masukan (n).
- **Binary Search:** Algoritma pencarian efisien berordo O(log n) yang bekerja pada sekumpulan data terurut dengan cara membagi rentang pencarian menjadi dua bagian secara berulang hingga elemen sasaran ditemukan.
- **Bitrate:** Jumlah bit data yang diproses atau ditransmisikan dalam satuan waktu tertentu (biasanya bit per detik atau bps), menentukan kualitas dan ukuran file video atau audio.
- **Chain-of-Thought (CoT):** Teknik rekayasa prompt yang memandu model bahasa cerdas (Large Language Model) untuk menguraikan tahapan penalaran logis secara bertahap sebelum memberikan kesimpulan akhir, meningkatkan akurasi pemecahan masalah rumit.
- **Computer Vision:** Cabang ilmu kecerdasan artifisial yang memungkinkan komputer mengekstrak makna, menganalisis, dan memahami informasi visual tingkat tinggi dari gambar digital atau video.
- **Design Thinking:** Metodologi perancangan solusi inovatif yang berpusat pada empati terhadap kebutuhan manusia, melalui tahapan Empathize, Define, Ideate, Prototype, dan Test.
- **Dictionary:** Struktur data koleksi bawaan Python yang menyimpan elemen data berpasangan dalam format kunci dan nilai (*key-value pairs*), memungkinkan pencarian data instan berordo O(1).
- **Entity Relationship Diagram (ERD):** Diagram visual standar rekayasa perangkat lunak yang menggambarkan struktur basis data, entitas data, atribut, dan hubungan antarentitas menggunakan notasi Crow's Foot.
- **Exception Handling:** Mekanisme arsitektur pemrograman untuk menangkap, mengisolasi, dan merespons kesalahan atau anomali saat program dieksekusi (runtime error) sehingga aplikasi tidak mengalami penghentian paksa (*crash*).
- **Foreign Key:** Atribut atau kolom dalam sebuah tabel basis data relasional yang merujuk pada Primary Key tabel lain untuk membentuk hubungan relasi integritas referensial antarentitas.
- **Konvolusi (Convolution):** Operasi matematika pada pengolahan citra digital yang mengalikan matriks nilai piksel tetangga dengan matriks filter berukuran kecil (kernel) untuk menghasilkan fitur baru seperti deteksi tepi, penajaman, atau pengaburan gambar.
- **Linear Search:** Algoritma pencarian sekuensial paling sederhana yang memeriksa setiap elemen data satu per satu dari awal hingga akhir dengan kompleksitas waktu berordo O(n).
- **Lossless Compression:** Metode kompresi berkas digital yang mengecilkan ukuran data tanpa menghilangkan satu bit pun informasi asli, memungkinkan rekonstruksi berkas yang sempurna persis seperti aslinya.
- **Lossy Compression:** Metode kompresi berkas digital yang mengorbankan sebagian detail data yang kurang disadari oleh indra manusia untuk mencapai ukuran berkas yang jauh lebih kecil dan efisien untuk transmisi jaringan.
- **PEP 8 (Python Enhancement Proposal 8):** Panduan gaya resmi yang menetapkan konvensi standar penulisan kode sumber bahasa Python agar bersih, rapi, seragam, dan mudah dipelihara secara kolaboratif.
- **Primary Key:** Atribut unik dalam sebuah tabel basis data yang berfungsi sebagai pengidentifikasi tunggal dan pasti untuk membedakan setiap baris data tanpa kemungkinan duplikasi.
- **ROCCF Framework:** Kerangka kerja sistematis dalam rekayasa prompt tingkat lanjut yang mencakup penentuan Peran (*Role*), Tujuan (*Objective*), Konteks (*Context*), Batasan (*Constraint*), dan Format Keluaran (*Format*).
- **Spektrogram (Spectrogram):** Representasi visual dua dimensi yang memetakan spektrum frekuensi sinyal suara terhadap perubahan waktu, di mana intensitas warna menunjukkan kekuatan amplitudo gelombang suara.
- **SQL (Structured Query Language):** Bahasa pemrograman domain-khusus standar internasional yang digunakan untuk mengelola, mendefinisikan, dan memanipulasi data dalam sistem manajemen basis data relasional (RDBMS).

---

# INDEKS ISTILAH

- **A**
  - Algoritma Pengurutan, 12, 16, 21
  - Aspek Rasio, 84, 86, 91
  - Atribut Basis Data, 55, 58
- **B**
  - Big-O Notation, 13, 23, 25
  - Binary Search, 14, 15, 17
  - Bitrate, 87, 88
  - Bubble Sort, 18, 19
- **C**
  - Chain-of-Thought, 128, 130
  - Computer Vision, 103, 105, 108
  - Crow's Foot Notasi, 59, 61
- **D**
  - Data Manipulation Language (DML), 64, 66
  - Data Definition Language (DDL), 63, 65
  - Design Thinking, 132, 135
  - Dictionary Python, 37, 40
- **E**
  - Entity Relationship Diagram (ERD), 58, 60
  - Exception Handling, 42, 44
- **F**
  - Few-Shot Prompting, 126, 127
  - Foreign Key, 56, 57
- **I**
  - Insertion Sort, 20, 22
- **K**
  - Kernel Konvolusi, 106, 107
  - Kompleksitas Asimptotik, 24, 26
- **L**
  - Linear Search, 13, 15
  - List Python, 35, 36
  - Lossless vs Lossy, 89, 90
- **M**
  - Matriks RGB, 104, 105
- **P**
  - PEP 8, 46, 47
  - Primary Key, 55, 56
- **R**
  - ROCCF Framework, 124, 125
- **S**
  - Selection Sort, 19, 20
  - Spektrogram Suara, 109, 111
  - sqlite3 Python, 67, 69
- **T**
  - Try-Except, 43, 45
  - Tuple Python, 36, 37
- **U**
  - User-Centered Design, 92, 94

---

# DAFTAR PUSTAKA RESMI

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). Cambridge, MA: The MIT Press.
2. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Boston: Addison-Wesley Professional.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. Cambridge, MA: The MIT Press.
4. IEEE Computer Society. (2023). *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide V4.0)*. Los Alamitos, CA: IEEE Computer Society Press.
5. Kementerian Pendidikan Dasar dan Menengah RI. (2025). *Panduan Pembelajaran dan Asesmen Kurikulum Koding dan Kecerdasan Artifisial Jenjang SMA/SMK (Fase E)*. Jakarta: Pusat Kurikulum dan Pembelajaran, Kemendikdasmen RI.
6. McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter* (3rd ed.). Sebastopol, CA: O'Reilly Media.
7. Norman, D. (2013). *The Design of Everyday Things* (Revised and Expanded ed.). New York: Basic Books.
8. Python Software Foundation. (2024). *PEP 8 – Style Guide for Python Code*. Diakses dari https://peps.python.org/pep-0008/
9. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Hoboken, NJ: Pearson Education.
10. Szeliski, R. (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Cham, Switzerland: Springer Nature.
11. Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database System Concepts* (7th ed.). New York: McGraw-Hill Education.
12. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. Paris: United Nations Educational, Scientific and Cultural Organization.

---

# PROFIL PENULIS

[GAMBAR: assets/foto_penulis.jpg]

**Gede Erik Aktama, S.Pd., M.Pd.** adalah seorang akademisi, peneliti, dan praktisi pendidikan di bidang sains komputer dan kecerdasan artifisial berkebangsaan Indonesia. Beliau menyelesaikan pendidikan Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika di Universitas Pendidikan Ganesha (UNDIKSHA) Singaraja, Bali, dan menuntaskan gelar Magister Pendidikan (M.Pd.) dengan fokus konsentrasi pada penelitian teknologi pembelajaran dan rekayasa media digital interaktif.

Saat ini, beliau mengemban amanah sebagai dosen tetap dengan jabatan fungsional akademik **Lektor** (berdasarkan Keputusan Menteri Pendidikan Tinggi, Sains, dan Teknologi Republik Indonesia Nomor: 0044/LL16/KP.07/2025) sekaligus menjabat sebagai **Ketua Program Studi S1 Sistem Komputer** di Fakultas Sains dan Teknologi, Universitas Parna Raya (UNIPAR) Manado, Sulawesi Utara.

Di tingkat nasional, Gede Erik Aktama aktif berperan sebagai **Fasilitator Nasional Bimbingan Teknis dan Training of Trainers (ToT) Kurikulum Koding dan Kecerdasan Artifisial (KKA)** yang diselenggarakan oleh Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) Republik Indonesia. Dalam kiprahnya, beliau telah melatih ribuan guru informatika dan praktisi komputasi di berbagai pelosok nusantara guna mempersiapkan fondasi talenta digital Indonesia menuju era kedaulatan sains dan teknologi masa depan.

Bidang riset dan kepakaran beliau berfokus pada arsitektur pembelajaran mendalam (*Deep Learning*), rekayasa sistem berbasis kecerdasan artifisial, etika sistem cerdas, dan pengembangan kurikulum vokasi berbasis komputasi modern. Beliau dapat dihubungi melalui surel akademik di: *erik.aktama@parnaraya.ac.id*.
"""
