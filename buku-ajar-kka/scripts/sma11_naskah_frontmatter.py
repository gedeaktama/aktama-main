"""
Modul Naskah Frontmatter dan Postliminaries Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

FRONTMATTER_SMA11 = """# KODING DAN KECERDASAN ARTIFISIAL

## BUKU SISWA KELAS XI SMA/SMK (FASE F)

**Penulis:**
Gede Erik Aktama, S.Pd., M.Pd.

**Penerbit:**
PT Aktama Mega Persada
Bekerja sama dengan Tim Pengembang Kurikulum Koding dan Kecerdasan Artifisial

---

# HAK CIPTA DAN KREDIT

**Judul Buku:** Koding dan Kecerdasan Artifisial untuk Siswa SMA/SMK Kelas XI (Fase F)
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

Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, petunjuk, dan karunia-Nya, sehingga buku ajar *Koding dan Kecerdasan Artifisial (KKA) untuk SMA/SMK Kelas XI (Fase F)* ini dapat dihadirkan sebagai instrumen pembelajaran unggulan berstandar nasional dan internasional.

Memasuki jenjang Fase F pada Kelompok Mata Pelajaran Pilihan, peserta didik diajak melangkah lebih jauh melampaui logika dasar prosedural. Dunia rekayasa perangkat lunak dan sains data modern menuntut kecakapan arsitektur tingkat lanjut: bagaimana mengorganisasikan ribuan baris kode menggunakan paradigma Pemrograman Berorientasi Objek (*Object-Oriented Programming* / OOP), mengelola proyek tim secara kolaboratif melalui *Version Control System* Git dan platform GitHub, serta menghubungkan pangkalan data terdistribusi menggunakan antarmuka layanan web *RESTful API*.

Lebih dari itu, buku ajar ini menyajikan eksplorasi mendalam pada domain mutakhir peradaban: *Machine Learning Terapan* dan *Pemrosesan Bahasa Alami (Natural Language Processing / NLP)*. Peserta didik tidak hanya diajarkan melatih algoritma klasifikasi cerdas seperti K-Nearest Neighbors (KNN) dan Decision Tree, melainkan dilatih berpikir kritis mengevaluasi objektivitas model melalui Matriks Konfusi (*Confusion Matrix*), memahami mekanisme tokenisasi teks bahasa manusia, hingga membedah prinsip dasar arsitektur *Transformer* yang menggerakkan model bahasa cerdas dunia (*Large Language Models*).

Pendekatan pedagogis yang melandasi seluruh buku ini adalah **Pembelajaran Mendalam (Deep Learning Approach)** yang berakar pada kesadaran berpikir (*Mindful*), kebermaknaan kontekstual (*Meaningful*), dan kegembiraan eksplorasi sains (*Joyful*). Ditemani oleh trio sahabat belajar—Arya (sains komputasi & matematika AI), Dinda (analisis data sosial, etika AI & NLP), serta Bagas (rekayasa perangkat lunak, database & integrasi sistem)—siswa dibimbing mempraktikkan kode bersih, membangun empati pada kebutuhan pengguna nyata (*Human-Centered AI*), serta menegakkan integritas etika digital sejalan dengan Profil Pelajar Pancasila dan Undang-Undang Perlindungan Data Pribadi (UU PDP).

Penulis menyampaikan rasa hormat dan terima kasih yang mendalam kepada Kementerian Pendidikan Dasar dan Menengah RI, Universitas Parna Raya (UNIPAR) Manado, para pengembang kurikulum nasional, rekan-rekan pendidik vokasi dan akademik, serta seluruh tim redaksi yang telah berkontribusi mewujudkan mahakarya ini. Semoga buku ajar ini menjadi suluh penerang yang melahirkan barisan insinyur perangkat lunak, ilmuwan data, dan pemimpin teknologi masa depan Indonesia yang tangguh, inovatif, dan berakhlak mulia.

Selamat berkarya dan melahirkan inovasi gemilang bagi bangsa!

Manado,   2025

**Gede Erik Aktama, S.Pd., M.Pd.**
*Penulis & Fasilitator Nasional KKA*

---

# PETUNJUK PENGGUNAAN BUKU

Buku teks ini disusun dengan arsitektur pedagogi berjenjang yang memadukan teori ilmiah, visualisasi diagramatik 300 DPI, dan praktikum koding berbasis proyek industri. Perhatikan ikon-ikon panduan belajar berikut:

1. **Apersepsi Komik Inspiratif:** Narasi grafis di awal setiap bab yang membedah dilema teknologi riil yang dihadapi para tokoh sahabat belajar.
2. **Bedah Teori & Arsitektur Sistem:** Penjelasan ilmiah mendalam mengenai konsep OOP, aljabar jarak matriks, arsitektur REST API, dan teori pemrosesan bahasa alami.
3. **Eksplorasi Kode Python Terapan:** Implementasi kode program fungsional standar industri dengan ulasan baris demi baris dan tips penanganan galat (*debugging*).
4. **Laboratorium Plugged (LKPD):** Lembar Kerja Peserta Didik berbasis eksperimen terminal, pangkalan data, pustaka Scikit-Learn, dan repositori Git kolaboratif.
5. **Zona Integritas & Etika Pengembang:** Ulasan nilai moral, keamanan siber, kepatuhan hukum UU PDP, serta pencegahan bias diskriminasi pada sistem cerdas.
6. **Rangkuman Bab & Peta Pemikiran:** Ringkasan intisari konsep untuk memperkuat retensi memori komputasi peserta didik.
7. **Uji Kompetensi Mandiri:** 10 Butir Pilihan Ganda berbobot HOTS dan 5 Soal Pemecahan Kasus Sistemik di setiap bab, dilengkapi pembahasan komprehensif.

---

# MENGENAL TOKOH SAHABAT BELAJAR FASE F

Perjalanan eksplorasi koding tingkat lanjut dan kecerdasan artifisial di Kelas XI ini dipandu oleh tiga sahabat pembelajar yang berdedikasi:

[GAMBAR: assets/gambar_tokoh_sahabat_sma11.png]

1. **Arya (Siswa Peminat Sains Komputasi, Algoritma, & Machine Learning):**
Arya sangat menyukai analisis matematis di balik kecerdasan artifisial. Ia terpesona oleh cara model machine learning memisahkan data menggunakan fungsi jarak Euclidean dan pohon keputusan, menguji akurasi model pada Confusion Matrix, dan merancang arsitektur kelas OOP yang modular, elegan, dan hemat memori.

2. **Dinda (Siswi Peminat Pemrosesan Bahasa Alami, Analisis Sosial, & Etika AI):**
Dinda memiliki minat mendalam pada interaksi antara bahasa manusia dan komputasi cerdas (NLP). Ia gemar bereksperimen dengan analisis sentimen opini publik, memahami mekanisme perhatian Transformer, serta gigih mengawal penerapan etika sistem cerdas yang berpusat pada manusia (*Human-Centered AI*) agar bebas dari bias diskriminatif.

3. **Bagas (Siswa SMK Peminat Rekayasa Perangkat Lunak, Database, & API):**
Bagas adalah sosok praktisi rekayasa sistem yang handal. Ia mahir mengelola siklus hidup perangkat lunak (SDLC), mengelola repositori kolaboratif menggunakan Git dan GitHub, merancang antarmuka layanan web RESTful API dengan format pertukaran data JSON, serta mengamankan pangkalan data dari serangan siber SQL Injection.

---

# DAFTAR ISI

- Prakata
- Petunjuk Penggunaan Buku
- Mengenal Tokoh Sahabat Belajar Fase F
- Capaian Pembelajaran Fase F (KKA Kelas XI)
- BAB I: Pemrograman Berorientasi Objek (OOP) dan Engineering Process
  - A. Paradigma Pemrograman: Prosedural vs Berorientasi Objek (OOP)
  - B. Konstruktor, Atribut Instans, dan Method dalam Python
  - C. Tiga Pilar Inti OOP: Enkapsulasi, Pewarisan, dan Polimorfisme
  - D. Rekayasa Perangkat Lunak: Siklus SDLC Agile dan Manajemen Versi Git/GitHub
  - E. LKPD 1.1: Rancang Bangun Sistem Manajemen Akademik OOP Terintegrasi Git
  - F. Rangkuman Materi Bab I
  - G. Uji Kompetensi Bab I (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB II: Rekayasa Basis Data Terintegrasi, Data Encoding, dan REST API
  - A. Format Data Encoding dan Pertukaran Data Modern: JSON, XML, dan UTF-8
  - B. Relasi Multi-Tabel Basis Data Relasional dan Kueri Tingkat Lanjut (JOIN)
  - C. Arsitektur Antarmuka Layanan Web: RESTful API dan Protokol HTTP
  - D. Keamanan Basis Data: Parameterized Query dan Hashing Kata Sandi
  - E. LKPD 2.1: Membangun Layanan REST API Mandiri Menggunakan Python
  - F. Rangkuman Materi Bab II
  - G. Uji Kompetensi Bab II (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB III: Kolaborasi Multimedia Tingkat Lanjut untuk Pendukung Aplikasi
  - A. Perancangan Aset Antarmuka Pengguna Vektor (SVG) dan Aksesibilitas WCAG
  - B. Penyusunan Dokumentasi Teknis Perangkat Lunak: README.md dan Dependensi
  - C. Seni Pitching dan Demonstrasi Produk Perangkat Lunak Startup
  - D. LKPD 3.1: Proyek Penyusunan Dokumentasi Repositori dan Presentasi Produk
  - E. Rangkuman Materi Bab III
  - F. Uji Kompetensi Bab III (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB IV: Fondasi Machine Learning: Pipeline, Klasifikasi, dan Evaluasi Model
  - A. Taksonomi Machine Learning: Supervised, Unsupervised, dan Reinforcement
  - B. Tahapan Pra-Pemrosesan Data dan Pembagian Dataset (Train-Test Split)
  - C. Algoritma Klasifikasi Populer: K-Nearest Neighbors (KNN) dan Decision Tree
  - D. Evaluasi Objektif Kinerja Model: Matriks Konfusi (Confusion Matrix)
  - E. LKPD 4.1: Pelatihan dan Evaluasi Model Klasifikasi dengan Scikit-Learn
  - F. Rangkuman Materi Bab IV
  - G. Uji Kompetensi Bab IV (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB V: Fondasi Pemrosesan Bahasa Alami (Natural Language Processing - NLP)
  - A. Kompleksitas Bahasa Manusia dan Komputasi Linguistik Digital
  - B. Alur Pra-Pemrosesan Teks: Case Folding, Tokenizing, Stopwords, dan Stemming
  - C. Vektorisasi Teks: Pendekatan Bag of Words dan Pembobotan TF-IDF
  - D. Pengantar Arsitektur Transformer dan Mekanisme Perhatian (Attention)
  - E. LKPD 5.1: Membangun Model Analisis Sentimen Ulasan Publik Berbasis Teks
  - F. Rangkuman Materi Bab V
  - G. Uji Kompetensi Bab V (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB VI: Dampak Sosio-Teknologi AI, Ketenagakerjaan, dan Etika Pengembang
  - A. Disrupsi Ketenagakerjaan dan Konsep Augmented Intelligence
  - B. Standar Etika Sistem Cerdas Berpusat Manusia (Human-Centered AI)
  - C. Transparansi Algoritma (Explainable AI) dan Mitigasi Manipulasi Sistem
  - D. LKPD 6.1: Proyek Akhir Solusi Sosial Cerdas Berbasis Machine Learning/NLP
  - E. Rangkuman Materi Bab VI
  - F. Evaluasi Akhir Tahun Fase F Kelas XI (15 Soal PG, 5 Soal Uraian Kasus Sistemik, Kunci Jawaban)
- Glosarium Istilah Tingkat Lanjut Fase F
- Indeks Istilah
- Daftar Pustaka Resmi
- Profil Penulis

---

# CAPAIAN PEMBELAJARAN FASE F (KELAS XI SMA/SMK)

Pada akhir Fase F (Kelas XI), peserta didik menguasai kompetensi tingkat lanjut yang mencakup domain:
1. **Algoritma dan Pemrograman (AP):** Mampu merancang perangkat lunak modular berbasis paradigma Pemrograman Berorientasi Objek (OOP) dengan menerapkan enkapsulasi, pewarisan, dan polimorfisme, serta mengelola kolaborasi pengembangan kode sumber tim menggunakan Version Control System Git dan GitHub secara profesional.
2. **Analisis Data dan Rekayasa Sistem (AD-RS):** Memahami arsitektur serialisasi data JSON, merancang skema relasi basis data multi-tabel dengan kueri relasional JOIN yang optimal, membangun antarmuka web service RESTful API, serta menerapkan proteksi keamanan siber terhadap SQL Injection dan manajemen hashing kata sandi.
3. **Produksi Media Digital & Komunikasi Teknis (PMD):** Mampu merancang aset visual antarmuka pengguna berbasis vektor SVG yang mematuhi standar aksesibilitas WCAG, menyusun dokumentasi teknis kode sumber (Technical Writing), dan mempresentasikan demonstrasi produk perangkat lunak secara persuasif.
4. **Pemanfaatan dan Pengembangan Kecerdasan Artifisial (PPKA):** Menguasai siklus kerja (*pipeline*) Machine Learning terapan, menerapkan teknik pra-pemrosesan data numerik dan kategorikal, melatih model klasifikasi terawasi (KNN dan Decision Tree), serta mengevaluasi performa model secara kritis menggunakan Matriks Konfusi (Akurasi, Presisi, Recall, F1-Score).
5. **Pemrosesan Bahasa Alami (NLP):** Mampu mengolah teks bahasa manusia mentah melalui tahapan case folding, tokenizing, stopwords filtering, dan stemming bahasa Indonesia, mentransformasikan kata menjadi bobot numerik TF-IDF, serta memahami prinsip dasar arsitektur Transformer pada model bahasa besar.
6. **Literasi dan Etika Kecerdasan Artifisial (LEKA):** Mampu menganalisis dampak sosio-ekonomi otomasi cerdas terhadap lanskap ketenagakerjaan, merancang sistem cerdas berpusat manusia (*Human-Centered AI*), menegakkan transparansi algoritma (*Explainable AI*), serta mematuhi hukum perlindungan data pribadi nasional (UU PDP No. 27/2022).
"""

POSTLIMINARIES_SMA11 = """# GLOSARIUM ISTILAH TINGKAT LANJUT FASE F

- **Accuracy (Akurasi):** Rasio total prediksi benar (positif dan negatif) terhadap keseluruhan jumlah sampel data uji yang dievaluasi pada model pembelajaran mesin.
- **Attention Mechanism (Mekanisme Perhatian):** Komponen arsitektur jaringan saraf Transformer yang memungkinkan model menimbang derajat kepentingan hubungan semantik antar-kata dalam sebuah kalimat panjang secara dinamis.
- **Bag of Words (BoW):** Metode representasi teks sederhana yang memodelkan dokumen sebagai kantung berisi kumpulan kata tanpa memedulikan urutan tata bahasa, melainkan menghitung frekuensi kemunculannya.
- **Case Folding:** Tahap pra-pemrosesan teks yang menyeragamkan seluruh karakter abjad menjadi huruf kecil (lowercase) untuk menghindari duplikasi kata akibat perbedaan kapitalisasi.
- **Class:** Cetak biru (*blueprint*) atau definisi abstrak dalam paradigma pemrograman berorientasi objek yang memuat sekumpulan atribut dan metode untuk menciptakan objek nyata.
- **Confusion Matrix (Matriks Konfusi):** Tabel kontingensi dua dimensi berukuran 2x2 (atau NxN) yang memetakan jumlah prediksi model terhadap nilai aktual sebenarnya (True Positive, True Negative, False Positive, False Negative).
- **Decision Tree (Pohon Keputusan):** Algoritma pembelajaran mesin terawasi non-parametrik yang membagi data menjadi simpul-simpul cabang keputusan menyerupai pohon terbalik berdasarkan ukuran kemurnian data (Gini Impurity atau Entropy).
- **Encapsulation (Enkapsulasi):** Pilar OOP yang membungkus data atribut dan metode dalam satu unit tunggal kelas, serta membatasi akses langsung dari luar menggunakan modifikator akses privat untuk mencegah korupsi data.
- **Endpoint API:** Alamat URL spesifik pada server jaringan tempat klien dapat mengirimkan permintaan HTTP untuk mengakses atau memanipulasi sumber daya data tertentu.
- **Explainable AI (XAI):** Rangkaian metode dan teknik dalam sistem kecerdasan artifisial yang memungkinkan keputusan yang dihasilkan oleh model cerdas dapat dipahami, dilacak, dan dipertanggungjawabkan secara logis oleh manusia.
- **F1-Score:** Rata-rata harmonik antara Presisi dan Recall, memberikan ukuran performa model yang seimbang dan andal terutama pada kasus distribusi data kelas yang timpang (*imbalanced dataset*).
- **Git:** Perangkat lunak sistem kendali versi terdistribusi (*Distributed Version Control System*) untuk melacak riwayat perubahan berkas kode sumber dan memfasilitasi kolaborasi pengembang.
- **Inheritance (Pewarisan):** Pilar OOP yang memungkinkan sebuah kelas turunan (*child class*) mewarisi atribut dan metode dari kelas induk (*parent class*) sehingga meningkatkan penggunaan ulang kode (*code reusability*).
- **JSON (JavaScript Object Notation):** Format standar pertukaran data berbasis teks terbuka yang ringan, terstruktur, dan mudah dibaca baik oleh manusia maupun mesin komputasi.
- **K-Nearest Neighbors (KNN):** Algoritma klasifikasi berbasis instans yang memprediksi label kelas suatu data baru berdasarkan mayoritas label dari sejumlah k tetangga terdekatnya menggunakan perhitungan jarak Euclidean.
- **Polymorphism (Polimorfisme):** Pilar OOP yang memungkinkan sebuah antarmuka metode yang sama memiliki perilaku atau implementasi yang berbeda pada berbagai kelas turunan yang berbeda (*method overriding*).
- **Precision (Presisi):** Rasio ketepatan prediksi positif, dihitung dengan membagi jumlah True Positive terhadap total data yang diprediksi positif (True Positive + False Positive).
- **Recall (Sensitivitas):** Rasio keberhasilan model dalam menangkap seluruh kejadian aktual positif, dihitung dengan membagi True Positive terhadap total data yang sebenarnya positif (True Positive + False Negative).
- **RESTful API:** Gaya arsitektur antarmuka pemrograman aplikasi berbasis protokol komunikasi HTTP yang memanfaatkan metode standar GET, POST, PUT, dan DELETE tanpa menyimpan status sesi (*stateless*).
- **Stemming:** Proses morfologis dalam NLP yang memotong imbuhan (awalan, sisipan, akhiran) dari suatu kata untuk mengembalikannya ke bentuk kata dasar (*root word*).
- **Stopwords Removal:** Tahapan pembersihan teks yang membuang kata-kata fungsional umum (seperti kata hubung dan kata depan) yang memiliki frekuensi tinggi namun tidak memiliki nilai bobot informasi spesifik.
- **TF-IDF (Term Frequency - Inverse Document Frequency):** Algoritma pembobotan statistik numerik yang mencerminkan seberapa penting sebuah kata dalam dokumen tertentu di dalam kumpulan koleksi teks.
- **Transformer:** Arsitektur jaringan saraf pembelajaran mendalam berbasis mekanisme *self-attention* yang revolusioner, menjadi fondasi utama model-model bahasa besar modern (LLM).

---

# INDEKS ISTILAH

- **A**
  - Accuracy, 128, 131, 135
  - Agile Scrum, 42, 43
  - Attention Mechanism, 180, 181
  - Augmented Intelligence, 202, 204
- **B**
  - Bag of Words, 176, 177
  - Bcrypt Hashing, 81, 82
- **C**
  - Case Folding, 172, 173
  - Class dan Object, 34, 36, 38
  - Confusion Matrix, 128, 146, 147
- **D**
  - Decision Tree, 143, 145
  - Deserialisasi, 70, 71
- **E**
  - Encapsulation, 39, 40
  - Explainable AI (XAI), 206, 207
- **F**
  - F1-Score, 147, 148
  - False Negative, 148, 149
  - False Positive, 148, 149
- **G**
  - Gini Impurity, 143, 144
  - Git dan GitHub, 44, 45, 47
- **H**
  - Human-Centered AI, 196, 205
- **I**
  - Inheritance, 40, 41
- **J**
  - JSON Encoding, 69, 70
  - Junction Table, 73, 74
- **K**
  - K-Nearest Neighbors (KNN), 142, 143
- **N**
  - Natural Language Processing (NLP), 169, 171
- **P**
  - Parameterized Query, 80, 81
  - Polymorphism, 41, 42
  - Precision, 147, 148
- **R**
  - Recall, 147, 148
  - RESTful API, 75, 76, 78
- **S**
  - Scikit-Learn, 127, 144
  - Stemming Sastrawi, 173, 174
  - Stopwords, 173, 174
- **T**
  - TF-IDF, 177, 178
  - Tokenizing, 172, 173
  - Train-Test Split, 139, 140
  - Transformer, 180, 181

---

# DAFTAR PUSTAKA RESMI

1. Booch, G., Maksimchuk, R. A., Engle, M. W., Young, B. J., Conallen, J., & Houston, K. A. (2007). *Object-Oriented Analysis and Design with Applications* (3rd ed.). Boston: Addison-Wesley.
2. Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). New York: Apress.
3. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems* (3rd ed.). Sebastopol, CA: O'Reilly Media.
4. Jurafsky, D., & Martin, J. H. (2024). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition* (3rd ed. draft). Stanford, CA: Stanford University Press.
5. Kementerian Pendidikan Dasar dan Menengah RI. (2025). *Panduan Pembelajaran dan Asesmen Kurikulum Koding dan Kecerdasan Artifisial Jenjang SMA/SMK (Fase F)*. Jakarta: Pusat Kurikulum dan Pembelajaran, Kemendikdasmen RI.
6. Lutz, M. (2013). *Learning Python: Powerful Object-Oriented Programming* (5th ed.). Sebastopol, CA: O'Reilly Media.
7. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
8. Republik Indonesia. (2022). *Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*. Lembaran Negara Republik Indonesia Tahun 2022 Nomor 196. Jakarta: Sekretariat Negara.
9. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Hoboken, NJ: Pearson Education.
10. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 5998-6008.

---

# PROFIL PENULIS

[GAMBAR: assets/foto_penulis.jpg]

**Gede Erik Aktama, S.Pd., M.Pd.** adalah akademisi, inovator teknologi pembelajaran, dan peneliti sains komputer Indonesia. Beliau menamatkan studi Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika di Universitas Pendidikan Ganesha (UNDIKSHA) Singaraja, Bali, serta meraih gelar Magister Pendidikan (M.Pd.) dengan keahlian khusus pada rekayasa media pembelajaran digital interaktif dan sistem komputasi adaptif.

Saat ini, beliau menjabat sebagai **Ketua Program Studi S1 Sistem Komputer** di Fakultas Sains dan Teknologi, Universitas Parna Raya (UNIPAR) Manado, Sulawesi Utara, dengan jabatan akademik fungsional **Lektor** berdasarkan Keputusan Menteri Pendidikan Tinggi, Sains, dan Teknologi RI Nomor: 0044/LL16/KP.07/2025.

Dalam kancah pendidikan nasional, beliau dipercaya sebagai **Fasilitator Nasional Bimbingan Teknis dan Training of Trainers (ToT) Kurikulum Koding dan Kecerdasan Artifisial (KKA)** oleh Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) Republik Indonesia. Melalui dedikasinya, beliau giat memberikan pelatihan dan penguatan kompetensi sains data, pemrograman berorientasi objek, machine learning, dan etika AI kepada ribuan guru dan instruktur teknologi di seluruh wilayah Indonesia guna mewujudkan kedaulatan talenta digital bangsa.

Fokus penelitian dan publikasi ilmiah beliau meliputi arsitektur pembelajaran mesin (*Deep Learning*), integrasi layanan mikro data berbasis REST API, pemrosesan bahasa alami berbahasa daerah nusantara, serta penerapan tata kelola kecerdasan artifisial yang berpusat pada nilai-nilai kemanusiaan (*Human-Centered AI*). Beliau dapat dihubungi melalui korespondensi resmi di: *erik.aktama@parnaraya.ac.id*.
"""
