# KODING DAN KECERDASAN ARTIFISIAL

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


# BAB I: PEMROGRAMAN BERORIENTASI OBJEK (OOP) DAN ENGINEERING PROCESS

## APERSEPSI: MENGAPA KODE PROSEDURAL KITA SULIT BERTAHAN?

Di laboratorium rekayasa perangkat lunak sekolah, Arya, Dinda, dan Bagas sedang berkumpul di depan monitor utama. Mereka sedang mengembangkan proyek sistem informasi klinik kesehatan dan akademik sekolah. Namun, seiring bertambahnya fitur, layar kode mereka yang sudah mencapai lebih dari 2.500 baris mulai menunjukkan kekacauan yang serius.

[GAMBAR: assets/bab1_komik_pembuka_sma11.png]

"Aduh, program kita semakin sulit dikendalikan!" keluh Bagas seraya menatap fungsi-fungsi prosedural yang bertumpuk. "Tadi aku baru saja menambahkan fungsi untuk menghitung tunjangan wali kelas, tetapi mendadak variabel global `gaji` tertimpa dan fungsi pembayaran dokter klinik ikut rusak! Semua variabel saling tumpang tindih!"

Dinda mengangguk seraya memeriksa catatan tim. "Bukan hanya itu, Bagas. Kemarin saat Arya mengedit berkas yang sama dan mengirimkannya lewat pesan percakapan, perubahan kode yang kubuat malam sebelumnya terhapus begitu saja karena tertimpa versi terbaru dari Arya. Kita tidak memiliki sistem yang melacak riwayat perubahan secara aman!"

Arya menarik napas lalu tersenyum menenangkan kedua rekannya. "Teman-teman, apa yang kita alami adalah fase pendewasaan seorang pengembang perangkat lunak. Selama ini kita terbiasa menulis kode prosedural linier di mana fungsi dan variabel global tercampur bebas. Pada proyek berskala industri, pendekatan ini tidak lagi memadai. Kita harus beralih ke paradigma **Pemrograman Berorientasi Objek (*Object-Oriented Programming* / OOP)**!"

"Dengan OOP," lanjut Arya, "kita membungkus data dan perilaku ke dalam cetak biru yang disebut **Class**, melindungi data sensitif dengan **Enkapsulasi**, memanfaatkan **Pewarisan** agar kode dapat digunakan kembali (*reusable*), dan menerapkan **Polimorfisme**. Selain itu, agar koding bersama kita tidak pernah saling menimpa lagi, kita wajib menerapkan sistem kendali versi profesional standar dunia: **Git dan platform GitHub**!"

"Luar biasa!" seru Bagas dan Dinda antusias. "Mari kita pelajari arsitektur OOP Python dan disiplin rekayasa perangkat lunak modern!"

---

## A. PARADIGMA PEMROGRAMAN: PROSEDURAL VS BERORIENTASI OBJEK (OOP)

Dalam sejarah ilmu komputer, paradigma pemrograman berkembang seiring dengan melonjaknya kompleksitas sistem perangkat lunak yang dibangun oleh manusia.

[GAMBAR: assets/bab1_diagram_arsitektur_oop_python.png]

### 1. Keterbatasan Paradigma Prosedural

Pada paradigma prosedural, program dipandang sebagai sekumpulan instruksi sekuensial yang mengeksekusi fungsi atau prosedur secara bertahap dari atas ke bawah. Data biasanya disimpan dalam variabel-variabel global atau struktur terpisah, kemudian dikirimkan sebagai argumen ke berbagai fungsi.

**Kelemahan Paradigma Prosedural pada Proyek Besar:**
- **Spaghetti Code & Variabel Global:** Ketika program membesar, variabel global rentan diubah secara tidak sengaja oleh fungsi lain, memicu galat tersembunyi (*side effects*) yang sangat sulit dilacak.
- **Rendahnya Penggunaan Ulang Kode (*Low Reusability*):** Jika kita ingin membuat entitas baru yang mirip (misalnya dari data Siswa ke data Mahasiswa), kita sering kali terpaksa menyalin-tempel (*copy-paste*) kode yang sama berulang-ulang.
- **Sulit Memodelkan Dunia Nyata:** Paradigma prosedural memisahkan antara data (kata benda) dan tindakan (kata kerja), padahal di alam nyata objek selalu memiliki karakteristik fisik (*state*) dan tindakan operasional (*behavior*) yang menyatu.

### 2. Revolusi Berorientasi Objek (OOP)

OOP memandang perangkat lunak sebagai suatu ekosistem interaksi antarentitas mandiri yang disebut **Objek (*Object*)**. Setiap objek merupakan perwujudan konkret dari sebuah cetak biru konseptual yang dinamakan **Kelas (*Class*)**.

- **Class (Cetak Biru / Blueprint):** Definisi abstrak yang menetapkan atribut apa saja yang dimiliki serta metode apa saja yang dapat dilakukan oleh objek tersebut.
- **Object (Wujud Nyata / Instance):** Entitas fisik di dalam memori komputer yang dibuat (*diinstansiasi*) berdasarkan cetak biru Class tertentu, memiliki nilai data atribut yang spesifik.

Sebagai analogi: Class adalah cetak biru gambar teknik arsitektur sebuah rumah modern. Berdasarkan satu cetak biru tersebut, pengembang dapat membangun ratusan rumah fisik nyata (*Objects*) di berbagai kavling tanah dengan warna cat tembok, nomor rumah, dan pemilik yang berbeda-beda.

---

## B. KONSTRUKTOR, ATRIBUT INSTANS, DAN METHOD DALAM PYTHON

Dalam bahasa pemrograman Python, sebuah kelas didefinisikan menggunakan kata kunci `class`. Mari kita bedah anatomi struktur dasarnya:

### 1. Metode Konstruktor `__init__()` dan Parameter `self`

Metode `__init__()` adalah metode khusus yang otomatis dieksekusi pertama kali oleh Python saat sebuah objek baru diciptakan (*diinstansiasi*) ke dalam memori. Metode ini lazim disebut sebagai **Konstruktor (*Constructor*)**, bertugas menginisialisasi atribut-atribut awal objek.

Parameter pertama pada setiap metode di dalam kelas wajib berupa kata kunci `self`. Parameter `self` merepresentasikan referensi eksplisit ke instans objek yang sedang aktif atau sedang memanggil metode tersebut.

```python
# Mendefinisikan Kelas Siswa
class Siswa:
    # Konstruktor penginisialisasi atribut instans
    def __init__(self, nisn, nama, jurusan):
        self.nisn = nisn          # Atribut instans: nomor induk
        self.nama = nama          # Atribut instans: nama lengkap
        self.jurusan = jurusan    # Atribut instans: bidang keahlian
        self.nilai_tugas = []     # Atribut instans: koleksi nilai

    # Metode untuk menambahkan nilai tugas
    def tambah_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.nilai_tugas.append(nilai)
            print(f">> Berhasil menambahkan nilai {nilai} untuk {self.nama}")
        else:
            print("[PERINGATAN] Nilai harus berada dalam rentang 0 hingga 100!")

    # Metode untuk menghitung rata-rata nilai
    def hitung_rata_rata(self):
        if not self.nilai_tugas:
            return 0.0
        return sum(self.nilai_tugas) / len(self.nilai_tugas)

# Menginstansiasi Objek Nyata di Memori
siswa_1 = Siswa("0081234567", "Arya Dinata", "Rekayasa Perangkat Lunak")
siswa_2 = Siswa("0089876543", "Dinda Kirana", "Sains Data & AI")

# Memanggil metode objek
siswa_1.tambah_nilai(88)
siswa_1.tambah_nilai(94)
print(f"Rata-rata {siswa_1.nama} : {siswa_1.hitung_rata_rata():.2f}")
```

---

## C. TIGA PILAR UTAMA OOP: ENKAPSULASI, PEWARISAN, DAN POLIMORFISME

Kekuatan arsitektur OOP ditopang oleh tiga pilar filosofis komputasi:

### 1. Enkapsulasi (Encapsulation) & Data Hiding

Enkapsulasi adalah prinsip membungkus data atribut dan metode operasionalnya ke dalam satu kesatuan terlindung, serta menyembunyikan detail implementasi internal dari akses langsung pihak luar (*Data Hiding*).

Tujuannya adalah menjaga integritas data agar tidak diubah sembarangan oleh kode di luar kelas. Dalam Python, penandaan hak akses privat dilakukan dengan memberikan awalan garis bawah ganda (`__`) pada nama atribut:
- **Atribut Publik (`self.nama`):** Dapat dibaca dan diubah bebas dari luar kelas.
- **Atribut Privat (`self.__saldo`):** Tidak dapat diakses langsung dari luar kelas. Akses hanya diizinkan melalui metode perantara yang aman: **Getter** (mengambil nilai) dan **Setter** (memvalidasi nilai sebelum diubah).

```python
class RekeningSekolah:
    def __init__(self, nomor_rekening, saldo_awal):
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo_awal  # Atribut privat (Encapsulated)

    # Getter: Metode membaca saldo secara aman
    def get_saldo(self):
        return self.__saldo

    # Setter: Metode mengubah saldo dengan validasi ketat
    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"[SETOR] Berhasil menambah Rp{jumlah:,}. Saldo baru: Rp{self.__saldo:,}")
        else:
            print("[GAGAL] Jumlah setoran harus lebih dari nol!")

akun = RekeningSekolah("REK-001", 500000)
# akun.__saldo = 100000000  # Tidak akan memengaruhi atribut privat asli!
akun.setor_tunai(150000)
print(f"Saldo resmi terverifikasi: Rp{akun.get_saldo():,}")
```

### 2. Pewarisan (Inheritance)

Pewarisan adalah mekanisme di mana sebuah kelas baru (**Kelas Turunan / Child Class**) dapat mewarisi seluruh atribut dan metode dari kelas yang sudah ada (**Kelas Induk / Parent Class**).

Pewarisan mengeliminasi duplikasi kode secara drastis (*Don't Repeat Yourself / DRY*). Python menyediakan fungsi bawaan `super()` yang memungkinkan kelas turunan memanggil konstruktor atau metode kelas induknya secara mulus.

```python
# Kelas Induk (Parent Class)
class AnggotaSekolah:
    def __init__(self, id_anggota, nama, email):
        self.id_anggota = id_anggota
        self.nama = nama
        self.email = email

    def tampilkan_profil(self):
        return f"[{self.id_anggota}] {self.nama} | Surel: {self.email}"

# Kelas Turunan 1: Siswa mewarisi AnggotaSekolah
class SiswaAkademik(AnggotaSekolah):
    def __init__(self, id_anggota, nama, email, kelas):
        super().__init__(id_anggota, nama, email)  # Panggil konstruktor induk
        self.kelas = kelas

# Kelas Turunan 2: Guru mewarisi AnggotaSekolah
class GuruPengajar(AnggotaSekolah):
    def __init__(self, id_anggota, nama, email, mata_pelajaran):
        super().__init__(id_anggota, nama, email)
        self.mata_pelajaran = mata_pelajaran
```

### 3. Polimorfisme (Polymorphism) & Method Overriding

Kata *Polimorfisme* berasal dari bahasa Yunani yang berarti "memiliki banyak bentuk". Dalam rekayasa perangkat lunak, polimorfisme memungkinkan metode dengan nama yang sama pada kelas-kelas yang berbeda mengeksekusi perilaku yang disesuaikan secara dinamis (*Method Overriding*).

```python
class Karyawan:
    def __init__(self, nama, gaji_dasar):
        self.nama = nama
        self.gaji_dasar = gaji_dasar

    def hitung_tunjangan(self):
        return 0  # Perilaku default kelas induk

class ManajerTeknis(Karyawan):
    def hitung_tunjangan(self):
        # Override: Manajer mendapat tunjangan manajerial 30%
        return self.gaji_dasar * 0.30

class StafAdmin(Karyawan):
    def hitung_tunjangan(self):
        # Override: Staf admin mendapat tunjangan operasional tetap
        return 500000

# Pengujian Polimorfisme dalam sebuah perulangan seragam
daftar_karyawan = [
    ManajerTeknis("Arya", 10000000),
    StafAdmin("Bagas", 5000000)
]

for k in daftar_karyawan:
    print(f"Karyawan: {k.nama} | Tunjangan: Rp{k.hitung_tunjangan():,}")
```

---

## D. REKAYASA PERANGKAT LUNAK: SIKLUS SDLC DAN MANAJEMEN VERSI GIT/GITHUB

Menulis kode yang elegan tidak akan bernilai komersial jika tidak dikelola dalam proses rekayasa perangkat lunak (*Software Engineering Process*) yang terstandarisasi.

[GAMBAR: assets/bab1_alur_kerja_git_github_flow.png]

### 1. Siklus Hidup Perangkat Lunak: SDLC (Software Development Life Cycle)

Perangkat lunak industri dikembangkan melalui pendekatan metodologi tangkas (**Agile / Scrum**) yang melibatkan tahapan berulang (*sprint iteratif*):
1. **Analisis Kebutuhan (*Requirements Analysis*):** Menghimpun spesifikasi fitur yang diinginkan pengguna akhir (*User Stories*).
2. **Perancangan Arsitektur (*System & Architecture Design*):** Menyusun diagram kelas UML, diagram basis data ERD, dan antarmuka UI/UX.
3. **Implementasi Koding (*Implementation*):** Menulis kode sumber modular berbasis standar OOP dan konvensi PEP 8.
4. **Pengujian Mandiri & Sistem (*Testing & Quality Assurance*):** Menjalankan pengujian fungsional dan penanganan galat (*Unit Testing*).
5. **Penerapan & Pemeliharaan (*Deployment & Maintenance*):** Merilis sistem ke lingkungan server produksi dan memantau kinerjanya.

### 2. Kolaborasi Tanpa Konflik: Git & GitHub

**Git** adalah sistem kendali versi terdistribusi (*Distributed Version Control System*) yang mencatat setiap jengkal riwayat perubahan kode sumber seperti mesin penjelajah waktu. **GitHub** adalah platform awan global tempat tim pengembang menyimpan repositori bersama, meninjau kode (*Code Review*), dan menyatukan hasil kerja (*Merge*).

**Perintah Terminal Git Esensial yang Wajib Dikuasai:**
- `git init`: Menginisialisasi direktori lokal menjadi repositori Git aktif.
- `git status`: Memeriksa kondisi berkas (apakah ada berkas baru atau yang dimodifikasi).
- `git add .`: Memindahkan seluruh perubahan berkas ke area persiapan (*Staging Area*).
- `git commit -m "Pesan Deskriptif"`: Mengabadikan snapshot versi kode ke riwayat lokal.
- `git branch nama-fitur`: Membuat cabang kerja terpisah agar eksperimen koding tidak merusak kode utama.
- `git switch nama-fitur`: Berpindah ke cabang fitur yang diinginkan.
- `git push origin nama-fitur`: Mengunggah cabang kode lokal ke repositori awan GitHub.
- **Pull Request (PR):** Mekanisme di GitHub di mana pengembang meminta izin kepada ketua tim untuk menggabungkan cabang fiturnya ke cabang utama (`main`) setelah melalui proses penelaahan kode secara teliti.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 1.1

### Rancang Bangun Sistem Manajemen Akademik OOP Berbasis Git

**Tujuan Pembelajaran:**
Peserta didik mampu merancang struktur kelas berorientasi objek yang memadukan konstruktor, enkapsulasi atribut privat, pewarisan kelas, dan polimorfisme, serta mengelola kode tersebut dalam alur kerja cabang (*branching*) sistem kendali versi Git secara kolaboratif.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 dan Git terpasang di terminal.
2. Akun GitHub aktif.
3. Visual Studio Code.

**Instruksi Kerja Praktikum:**
1. Buatlah folder proyek baru bernama `proyek_akademik_oop`.
2. Buka terminal di VS Code, lalu inisialisasi repositori Git lokal:
   ```bash
   git init
   git config user.name "Nama Siswa"
   git config user.email "email.siswa@sekolah.sch.id"
   ```
3. Buat berkas `akademik.py` dan ketikkan implementasi arsitektur OOP terpadu berikut:

```python
# Sistem Manajemen Akademik OOP Terpadu
class CivitasAkademika:
    def __init__(self, id_unik, nama_lengkap):
        self.id_unik = id_unik
        self.nama_lengkap = nama_lengkap
        self.__status_kehadiran = "Alfa"  # Privat: Data terenkapsulasi

    # Getter status
    def get_status(self):
        return self.__status_kehadiran

    # Setter presensi aman
    def set_presensi(self, status):
        status_valid = ["Hadir", "Sakit", "Izin", "Alfa"]
        if status in status_valid:
            self.__status_kehadiran = status
            print(f">> Presensi {self.nama_lengkap} dicatat: {status}")
        else:
            print("[GALAT] Status presensi tidak valid!")

    # Metode polimorfik dasar
    def get_peran(self):
        return "Civitas Sekolah Umum"

class Siswa(CivitasAkademika):
    def __init__(self, id_unik, nama_lengkap, kelas, jurusan):
        super().__init__(id_unik, nama_lengkap)
        self.kelas = kelas
        self.jurusan = jurusan

    # Method Overriding
    def get_peran(self):
        return f"Siswa Jurusan {self.jurusan} (Kelas {self.kelas})"

class Guru(CivitasAkademika):
    def __init__(self, id_unik, nama_lengkap, mata_pelajaran):
        super().__init__(id_unik, nama_lengkap)
        self.mata_pelajaran = mata_pelajaran

    # Method Overriding
    def get_peran(self):
        return f"Guru Pengampu: {self.mata_pelajaran}"

if __name__ == "__main__":
    daftar_warga = [
        Siswa("SIS-101", "Arya Dinata", "XI", "RPL"),
        Siswa("SIS-102", "Dinda Kirana", "XI", "Sains Data"),
        Guru("GUR-001", "Gede Erik Aktama", "Koding dan Kecerdasan Artifisial")
    ]

    print("===== DAFTAR WARGA AKADEMIK SEKOLAH =====")
    for w in daftar_warga:
        w.set_presensi("Hadir")
        print(f"[{w.id_unik}] {w.nama_lengkap} | Peran: {w.get_peran()} | Presensi: {w.get_status()}")
        print("-" * 50)
```

4. Simpan riwayat kerja ke Git:
   ```bash
   git add akademik.py
   git commit -m "feat: inisialisasi arsitektur OOP CivitasAkademika"
   ```
5. Buat cabang baru bernama `fitur-validasi`, tambahkan validasi panjang ID unik minimal 5 karakter, lalu lakukan *commit* dan gabungkan (*merge*) kembali ke cabang `main`!

**Pertanyaan Analisis Laboratorium:**
1. Apa yang terjadi jika kode di luar kelas mencoba mengubah status presensi secara langsung dengan perintah `siswa_1.__status_kehadiran = "Hadir"`? Mengapa enkapsulasi melindunginya?
2. Bagaimana pemanggilan fungsi `super().__init__()` membantu kita menghindari pengetikan ulang kode pada kelas turunan?
3. Mengapa di industri perangkat lunak modern para insinyur dilarang melakukan commit langsung ke cabang `main` dan diwajibkan menggunakan cabang fitur (*feature branch*) serta *Pull Request*?

---

## F. RANGKUMAN MATERI BAB I

1. **Paradigma OOP vs Prosedural:** Pendekatan prosedural rentan kekacauan akibat variabel global yang saling tumpang tindih pada proyek besar. OOP mengorganisasikan perangkat lunak sebagai interaksi objek nyata (*Object*) yang dibangun berdasarkan cetak biru konseptual (*Class*).
2. **Konstruktor dan Instansiasi:** Metode `__init__()` adalah konstruktor penginisialisasi data awal objek di memori, di mana parameter `self` merepresentasikan objek spesifik yang sedang aktif.
3. **Tiga Pilar Inti OOP:**
   - *Enkapsulasi:* Membungkus data dan melindungi variabel privat (`__atribut`) dengan metode perantara *getter* dan *setter*.
   - *Pewarisan (Inheritance):* Menurunkan atribut dan metode dari kelas induk ke kelas turunan melalui fungsi `super()`.
   - *Polimorfisme:* Menimpa metode induk (*method overriding*) agar metode bernama sama mengeksekusi perilaku yang kontekstual pada kelas turunan yang berbeda.
4. **SDLC dan Git/GitHub:** Pengembangan sistem profesional mengadopsi siklus hidup tangkas (Agile/Scrum). Version Control System Git dan platform GitHub memfasilitasi kerja tim yang aman, memungkinkan pelacakan riwayat perubahan kode, percabangan fitur terisolasi (*branching*), serta penelaahan kode sebelum disatukan (*Pull Request*).

---

## G. UJI KOMPETENSI BAB I

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Paradigma pemrograman yang memandang perangkat lunak sebagai sekumpulan entitas mandiri yang menggabungkan karakteristik data fisik dan perilaku operasional ke dalam satu unit disebut...
   A. Pemrograman Fungsional Murni
   B. Pemrograman Prosedural Terstruktur
   C. Pemrograman Berorientasi Objek (OOP)
   D. Pemrograman Logika Deklaratif

2. Dalam sintaksis bahasa Python, metode khusus yang otomatis pertama kali dijalankan ketika sebuah objek baru diinstansiasi ke dalam memori komputer adalah...
   A. `__main__()`
   B. `__init__()`
   C. `__start__()`
   D. `__class__()`

3. Peran utama dari kata kunci `self` pada definisi metode di dalam sebuah kelas Python adalah...
   A. Mengimpor pustaka eksternal secara otomatis
   B. Menghentikan program saat terjadi pembagian dengan angka nol
   C. Mereferensikan instans spesifik dari objek yang sedang memanggil metode tersebut
   D. Menghapus objek dari memori secara permanen

4. Prinsip dalam OOP yang menyembunyikan detail atribut internal objek menggunakan awalan garis bawah ganda (`__`) dan membatasi manipulasi langsung dari luar kelas dinamakan...
   A. Enkapsulasi (*Encapsulation*)
   B. Pewarisan (*Inheritance*)
   C. Polimorfisme (*Polymorphism*)
   D. Abstraksi Sekuensial

5. Perhatikan potongan kode berikut:
   ```python
   class Mobil:
       def klakson(self):
           return "Tin tin!"

   class Truk(Mobil):
       def klakson(self):
           return "Tonton!"
   ```
   Kemampuan kelas `Truk` untuk mengubah implementasi metode `klakson` yang diwarisi dari kelas `Mobil` merupakan penerapan dari pilar...
   A. Enkapsulasi
   B. Kompresi Data
   C. Polimorfisme (*Method Overriding*)
   D. Rekursi

6. Fungsi bawaan Python yang digunakan pada kelas turunan untuk memanggil metode konstruktor atau atribut yang dimiliki oleh kelas induk secara elegan adalah...
   A. `parent()`
   B. `super()`
   C. `master()`
   D. `base()`

7. Tahapan dalam Software Development Life Cycle (SDLC) yang berfokus pada penerjemahan spesifikasi kebutuhan dan diagram UML menjadi baris-baris kode fungsional di lingkungan pengembang dinamakan...
   A. Requirements Analysis
   B. Implementation (Coding)
   C. System Testing
   D. Maintenance

8. Perintah dasar terminal Git yang berfungsi untuk mengabadikan perubahan berkas yang telah berada di area *Staging* menjadi riwayat versi permanen disertai catatan penjelasan adalah...
   A. `git init`
   B. `git add .`
   C. `git commit -m "Pesan"`
   D. `git branch -d`

9. Mengapa dalam alur kolaborasi tim menggunakan Git dan GitHub, para pengembang dilarang melakukan commit langsung ke cabang `main`?
   A. Karena cabang main hanya bisa menampung berkas bertipe gambar
   B. Karena cabang main harus selalu dijaga dalam kondisi stabil, bebas galat, dan siap dirilis ke produksi melalui mekanisme penelaahan kode (*Pull Request*)
   C. Karena server GitHub akan menghapus akun jika ada commit di cabang main
   D. Karena cabang main tidak mendukung bahasa pemrograman Python

10. Perintah Git yang tepat untuk membuat sebuah cabang kerja baru bernama `fitur-pembayaran` sekaligus langsung berpindah ke cabang tersebut adalah...
    A. `git switch -c fitur-pembayaran`
    B. `git delete fitur-pembayaran`
    C. `git merge origin main`
    D. `git push --all`

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara Class dan Object dalam paradigma OOP! Berikan analogi konkret di dunia nyata selain analogi rumah dan cetak biru!
2. Mengapa keberadaan atribut privat (`__atribut`) dan penyediaan metode getter/setter (Enkapsulasi) sangat krusial dalam sistem transaksi perbankan atau kasir toko? Apa bahaya yang timbul jika seluruh atribut dibiarkan bersifat publik?
3. Rancanglah hierarki pewarisan kelas (*Inheritance*) untuk sistem perpustakaan:
   - Kelas Induk: `Buku` (atribut: `isbn`, `judul`, `pengarang`).
   - Kelas Turunan: `EBook` (tambahan atribut: `ukuran_berkas_mb` dan format berkas).
   Tuliskan blok kode Python lengkapnya menggunakan fungsi `super().__init__()`!
4. Jelaskan apa yang dimaksud dengan *Method Overriding* dalam pilar Polimorfisme! Bagaimana teknik ini membantu pengembang membangun sistem perangkat lunak yang fleksibel dan mudah diperluas (*scalable*)?
5. Uraikan alur kerja kolaborasi standar industri (*GitHub Flow*) ketika seorang anggota tim hendak menambahkan fitur baru ke dalam proyek perangkat lunak sekolah, mulai dari pembuatan cabang lokal hingga penggabungan (*merge*) di repositori awan!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB I

**Kunci Pilihan Ganda:**
1. **C** (OOP mengorganisasikan perangkat lunak sebagai objek yang menggabungkan state dan behavior).
2. **B** (Metode `__init__()` adalah konstruktor inisialisasi awal objek di memori).
3. **C** (`self` mereferensikan instans spesifik dari objek yang sedang memanggil metode).
4. **A** (Enkapsulasi membungkus data dan menyembunyikannya dari modifikasi langsung di luar kelas).
5. **C** (Method overriding menimpa metode induk, menerapkan pilar polimorfisme).
6. **B** (Fungsi `super()` merujuk pada pemanggilan konstruktor atau metode kelas induk).
7. **B** (Implementation adalah fase penulisan kode sumber program).
8. **C** (`git commit -m` mencatat snapshot permanen ke riwayat versi repositori lokal).
9. **B** (Cabang main dijaga kestabilannya agar selalu dalam status bebas galat siap produksi).
10. **A** (`git switch -c` membuat dan langsung berpindah ke cabang baru).

**Pembahasan Soal Uraian:**
1. *Class vs Object:*
   - Class adalah konsep cetak biru atau resep generik. Analoginya: cetakan kue aluminium berbentuk bintang.
   - Object adalah benda nyata fisik yang dihasilkan dari cetakan tersebut. Analoginya: kue bolu bintang rasa cokelat atau vanila yang dapat kita cicipi di piring.
2. *Pentingnya Enkapsulasi Saldo Bank:*
   Jika atribut `saldo` bersifat publik, kode di bagian lain sistem (atau skrip peretas) dapat langsung mengetikkan `rekening.saldo = 999999999` tanpa melalui prosedur validasi. Dengan enkapsulasi dan setter (`setor_tunai`), sistem dapat menyaring bahwa penambahan saldo hanya sah jika nilai uang bertipe numerik positif, melewati verifikasi PIN keamanan, dan dicatat dalam riwayat audit bank.
3. *Implementasi Pewarisan Perpustakaan:*
   ```python
   class Buku:
       def __init__(self, isbn, judul, pengarang):
           self.isbn = isbn
           self.judul = judul
           self.pengarang = pengarang

   class EBook(Buku):
       def __init__(self, isbn, judul, pengarang, ukuran_mb, format_file):
           super().__init__(isbn, judul, pengarang)
           self.ukuran_mb = ukuran_mb
           self.format_file = format_file
   ```
4. *Method Overriding dan Skalabilitas:*
   Method overriding adalah teknik di mana kelas turunan mendefinisikan ulang metode yang sudah ada di kelas induk untuk memberikan perilaku spesifik yang sesuai dengan karakteristik kelas turunan. Ini memungkinkan sistem diperluas tanpa mengubah kode yang sudah berjalan (*Open-Closed Principle*). Ketika modul baru ditambahkan (misalnya jenis metode pembayaran baru), pengembang cukup mewarisi kelas induk dan meng-override metode `bayar()`, sementara sistem utama tetap dapat memanggil metode tersebut secara seragam melalui polimorfisme.
5. *Alur Kerja GitHub Flow:*
   (1) Tarik pembaruan terbaru dari cabang utama (`git pull origin main`); (2) Buat cabang fitur baru (`git switch -c fitur-baru`); (3) Tulis kode program dan uji hingga berjalan sempurna; (4) Simpan riwayat perubahan lokal (`git add .` dan `git commit -m "feat: deskripsi"`); (5) Unggah cabang ke GitHub (`git push origin fitur-baru`); (6) Buat *Pull Request (PR)* di antarmuka web GitHub; (7) Anggota tim lain melakukan penelaahan kode (*code review*); (8) Jika disetujui, cabang fitur digabungkan (*merged*) ke cabang `main` dan cabang fitur dihapus.


# BAB II: REKAYASA BASIS DATA TERINTEGRASI, DATA ENCODING, DAN REST API

## APERSEPSI: BAGAIMANA APLIKASI PONSEL MENGAKSES BASIS DATA SERVER?

Di kantin sekolah saat jam istirahat siang, Bagas tampak sedang asyik memamerkan aplikasi ponsel cerdas yang baru dirakitnya menggunakan laptopnya. "Dinda, Arya, coba perhatikan layar ponselku ini! Aku sedang membuat aplikasi pemesanan menu kantin sehat sekolah. Namun ada kendala besar: bagaimana caranya agar data pesanan dari ratusan ponsel siswa ini bisa tersimpan secara terpusat di komputer server koperasi sekolah?"

[GAMBAR: assets/bab2_komik_pembuka_sma11.png]

Arya menyesap minumannya lalu tersenyum. "Apakah kamu berniat mengirimkan berkas fisik database SQLite secara utuh bolak-balik melalui jaringan internet setiap kali seorang siswa memesan sepiring nasi goreng, Bagas?"

Bagas tertawa seraya menggelengkan kepala. "Tentu saja tidak mungkin! Ukuran berkas database bisa puluhan Megabyte, dan jika ratusan ponsel membuka berkas yang sama bersamaan, database pasti akan langsung rusak atau terkunci (*file lock*)!"

Dinda menimpali dengan pandangan cerdas, "Tepat sekali. Di era komputasi awan modern, aplikasi klien tidak pernah terhubung langsung secara fisik ke berkas database di server. Ada jembatan pertukaran data yang sangat ringan, terstandar, dan berkecepatan tinggi: format data teks terstruktur yang disebut **JSON (*JavaScript Object Notation*)**, yang ditransmisikan melalui antarmuka arsitektur web yang disebut **RESTful API (*Application Programming Interface*)**!"

"Dan yang tidak kalah penting," tambah Arya dengan nada tegas, "kita wajib membangun benteng keamanan siber yang kokoh. Kueri data harus menggunakan teknik *Parameterized Query* agar terhindar dari peretasan *SQL Injection*, serta kata sandi akun pengguna wajib diacak menggunakan fungsi *Hashing kriptografi satu arah*. Ini merupakan amanat tegas dari Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022)!"

"Luar biasa!" seru Bagas. "Artinya kita akan belajar menghubungkan ponsel pintar, web service Python, dan pangkalan data server secara aman! Mari kita selami rekayasa data terintegrasi ini!"

---

## A. FORMAT DATA ENCODING DAN PERTUKARAN DATA MODERN: JSON, XML, DAN UTF-8

Dalam ekosistem komputasi terdistribusi, sistem-sistem yang saling berkomunikasi sering kali dibangun di atas bahasa pemrograman dan arsitektur perangkat keras yang berbeda. Aplikasi ponsel dibangun dengan Kotlin atau Flutter, server komputasi AI menggunakan Python, sedangkan basis data menggunakan mesin SQL. Agar informasi dapat dipahami secara seragam tanpa distorsi biner, diperlukan standar **Data Encoding** dan format pertukaran data terbuka.

[GAMBAR: assets/bab2_arsitektur_rest_api_json_pipeline.png]

### 1. Standar Karakter Global: UTF-8

Di masa awal komputasi, sistem menggunakan pengkodean ASCII 7-bit yang hanya mampu menampung 128 karakter abjad Latin dasar. Standardisasi modern beralih ke **UTF-8 (Unicode Transformation Format - 8 bit)**. UTF-8 mampu merepresentasikan lebih dari 1,1 juta karakter dari seluruh aksara bahasa di dunia—termasuk aksara daerah nusantara (seperti Jawa, Bali, Batak), simbol matematika, hingga emoji modern.

### 2. Format Pertukaran Data: XML vs JSON

Pada dekade 1990-an, pertukaran data didominasi oleh format **XML (eXtensible Markup Language)** yang menggunakan tag pembuka dan penutup menyerupai HTML (`<nama>Arya</nama>`). Namun, format XML dinilai terlalu boros karakter (*verbose*) dan menguras kuota internet.

Industri teknologi modern saat ini secara mutlak mengadopsi **JSON (JavaScript Object Notation)** sebagai standar baku pertukaran data web:
- **Sangat Ringkas dan Hemat Pita Lebar:** Menggunakan struktur pasangan Kunci-Nilai (*Key-Value*) yang persis sama dengan Dictionary pada bahasa Python.
- **Mudah Dibaca Manusia (*Human-Readable*):** Formatnya intuitif dan bersih.
- **Dukungan Lintas Bahasa Universal:** Didukung secara bawaan oleh hampir seluruh bahasa pemrograman modern di dunia.

### 3. Proses Serialisasi dan Deserialisasi dalam Python

Python menyediakan modul bawaan `json` untuk melakukan konversi data dua arah:
- **Serialisasi (`json.dumps()`):** Mengubah objek memori Python (seperti Dictionary atau List) menjadi untaian teks string JSON yang siap ditransmisikan melalui kabel jaringan atau disimpan ke berkas.
- **Deserialisasi (`json.loads()`):** Membaca kembali untaian teks string JSON yang diterima dari jaringan menjadi objek struktur data memori Python yang siap dimanipulasi.

```python
import json

# Objek Dictionary data akademik di memori Python
profil_siswa = {
    "nisn": "0081234567",
    "nama": "Arya Dinata",
    "jurusan": "Rekayasa Perangkat Lunak",
    "prestasi": ["Juara 1 LKS Web", "Finalis AI Nasional"],
    "aktif": True
}

# 1. Serialisasi: Objek Python -> Teks JSON String
payload_json = json.dumps(profil_siswa, indent=2)
print("===== TEKS DATA TERKIRIM (SERIALISASI JSON) =====")
print(payload_json)

# 2. Deserialisasi: Teks JSON String -> Objek Python
data_diterima = json.loads(payload_json)
print("
===== DATA DITERIMA & DIPROSES (DESERIALISASI) =====")
print(f"Nama Siswa : {data_diterima['nama']}")
print(f"Prestasi 1 : {data_diterima['prestasi'][0]}")
```

---

## B. RELASI MULTI-TABEL BASIS DATA RELASIONAL DAN KUERI TINGKAT LANJUT

Dalam pangkalan data relasional skala besar, data tidak pernah ditumpuk dalam satu tabel tunggal melainkan dinormalisasi menjadi banyak tabel yang saling terhubung menggunakan relasi kunci utama (*Primary Key*) dan kunci asing (*Foreign Key*).

Untuk menarik wawasan analitis dari banyak tabel secara terpadu, kita menggunakan perintah **SQL JOIN** dan **Fungsi Agregasi**:

### 1. Ragam Operasi SQL JOIN

- **INNER JOIN:** Mengambil baris data yang hanya memiliki pasangan kecocokan (*match*) di kedua tabel yang digabungkan. Jika ada data di Tabel A yang tidak memiliki referensi di Tabel B, data tersebut tidak akan ditampilkan.
- **LEFT JOIN (atau LEFT OUTER JOIN):** Mengambil **seluruh baris** dari tabel sebelah kiri (Tabel A), serta menyertakan kolom yang cocok dari tabel sebelah kanan (Tabel B). Jika tidak ada kecocokan pada Tabel B, kolom dari Tabel B akan diisi dengan nilai kosong (`NULL`).

Perhatikan contoh kueri penggabungan tiga tabel relasional: `siswa`, `kelas`, dan `nilai_ujian`:

```sql
-- Mengambil nama siswa, nama kelas, dan nilai ujian
SELECT 
    s.nama_lengkap, 
    k.nama_kelas, 
    n.mata_pelajaran, 
    n.skor_ujian
FROM siswa s
INNER JOIN kelas k ON s.id_kelas = k.id_kelas
LEFT JOIN nilai_ujian n ON s.nisn = n.nisn
ORDER BY s.nama_lengkap ASC;
```

### 2. Pengelompokan dan Fungsi Agregasi (GROUP BY & HAVING)

Untuk membuat laporan rekapitulasi data, SQL menyediakan fungsi matematis agregat:
- `COUNT()`: Menghitung total banyaknya baris rekaman.
- `AVG()`: Menghitung nilai rata-rata dari kolom numerik.
- `SUM()`: Menjumlahkan total nilai angka.
- `GROUP BY`: Mengelompokkan baris data berdasarkan nilai kategori tertentu.
- `HAVING`: Menyaring hasil agregasi (berbeda dengan `WHERE` yang menyaring baris individual sebelum dikelompokkan).

```sql
-- Menghitung nilai rata-rata ujian per mata pelajaran yang rata-ratanya di atas 80
SELECT 
    mata_pelajaran, 
    COUNT(nisn) AS total_peserta, 
    AVG(skor_ujian) AS nilai_rata_rata
FROM nilai_ujian
GROUP BY mata_pelajaran
HAVING AVG(skor_ujian) >= 80.0
ORDER BY nilai_rata_rata DESC;
```

---

## C. ARSITEKTUR ANTARMUKA LAYANAN WEB: RESTFUL API DAN PROTOKOL HTTP

**REST (Representational State Transfer)** adalah gaya arsitektur antarmuka pemrograman aplikasi web yang memanfaatkan protokol komunikasi standar internet: **HTTP (Hypertext Transfer Protocol)**.

### 1. Metode Operasional HTTP (HTTP Verbs)

Setiap tindakan manipulasi data pada REST API dipetakan secara harmonis ke metode standar HTTP:
- **GET:** Meminta dan membaca data sumber daya dari server (Aksi Aman / *Idempotent*). Contoh: `GET /api/v1/siswa` (mengambil seluruh daftar siswa).
- **POST:** Mengirimkan data baru ke server untuk disimpan ke dalam basis data. Contoh: `POST /api/v1/siswa` dengan membawa muatan bodi JSON data siswa baru.
- **PUT / PATCH:** Memperbarui data yang sudah ada di basis data. Contoh: `PUT /api/v1/siswa/008123` untuk memperbarui alamat siswa.
- **DELETE:** Menghapus data sumber daya dari server. Contoh: `DELETE /api/v1/siswa/008123`.

### 2. Kode Status Tanggapan Standar HTTP (HTTP Status Codes)

Server REST API selalu mengembalikan kode numerik 3 digit yang memberi tahu aplikasi klien mengenai kondisi status pemrosesan permintaan:
- **Kelompok 2xx (Sukses):**
  - `200 OK`: Permintaan berhasil diproses dan data dikembalikan secara normal.
  - `201 Created`: Permintaan berhasil dan sumber daya data baru sukses diciptakan di basis data.
- **Kelompok 4xx (Kesalahan Klien / Client Errors):**
  - `400 Bad Request`: Format data yang dikirim klien tidak valid atau ada kolom wajib yang hilang.
  - `401 Unauthorized`: Klien belum melakukan login atau token autentikasi tidak sah.
  - `404 Not Found`: Alamat endpoint atau data ID yang dicari tidak ditemukan di server.
- **Kelompok 5xx (Kesalahan Server / Server Errors):**
  - `500 Internal Server Error`: Terjadi kegagalan logika atau crash pada kode program server.

---

## D. KEAMANAN BASIS DATA: PARAMETERIZED QUERY DAN HASHING KATA SANDI

Dalam era ancaman siber yang kian canggih, seorang perekayasa perangkat lunak bertanggung jawab penuh melindungi data pengguna dari kebocoran dan peretasan.

### 1. Pencegahan Serangan SQL Injection Melalui Parameterized Query

Serangan **SQL Injection** terjadi ketika masukan teks pengguna yang belum disaring digabungkan secara langsung (*string concatenation*) ke dalam perintah SQL. Peretas dapat menyusupkan karakter kutip dan perintah logika berbahaya (seperti `' OR '1'='1`) untuk membobol sistem tanpa kata sandi atau menghapus seluruh tabel basis data.

**Penangkal Mutlak: Parameterized Query (Prepared Statement)**
Dalam kode Python, jangan pernah menggunakan f-string untuk kueri SQL. Gunakan tanda tanya (`?`) atau parameter aman `%s`:
```python
# KODE BERBAHAYA (Rentan Diretas SQL Injection):
# kursor.execute(f"SELECT * FROM pengguna WHERE username = '{input_user}' AND sandi = '{input_sandi}'")

# KODE AMAN STANDAR INDUSTRI (Parameterized Query):
kursor.execute("SELECT * FROM pengguna WHERE username = ? AND sandi = ?", (input_user, input_sandi))
```
Dengan parameter aman, mesin database mengompilasi cetak biru logika perintah terlebih dahulu. Masukan pengguna diperlakukan murni 100% sebagai teks data mentah dan tidak akan pernah dieksekusi sebagai instruksi bahasa SQL.

### 2. Perlindungan Kata Sandi: Hashing Kriptografi Satu Arah

Menyimpan kata sandi pengguna dalam bentuk teks biasa (*plain text*) di pangkalan data adalah kejahatan arsitektur perangkat lunak yang sangat fatal. Jika server diretas, seluruh kata sandi pengguna akan tersebar bebas.

**Fungsi Hash Satu Arah (*One-Way Cryptographic Hash*):**
Kata sandi wajib diubah menjadi deretan karakter acak terenkripsi yang mustahil dikembalikan ke bentuk aslinya (menggunakan algoritma modern seperti **Bcrypt**, **Argon2**, atau **SHA-256** dipadukan dengan teknik pengacakan garam /*Salt*). Saat pengguna login kembali, sistem hanya membandingkan apakah nilai hash dari kata sandi yang diketik cocok dengan nilai hash yang tersimpan di database.

### 3. Kepatuhan Hukum: UU Perlindungan Data Pribadi (UU PDP No. 27/2022)

Sebagai generasi inovator digital bangsa, kalian wajib memahami bahwa Indonesia telah memberlakukan Undang-Undang Perlindungan Data Pribadi. UU ini mewajibkan setiap pengelola sistem elektronik untuk:
1. Menjaga kerahasiaan data pribadi masyarakat (NIK, data biometrik, rekam medis).
2. Memperoleh persetujuan sah dari pemilik data sebelum memproses informasinya.
3. Menjamin hak penghapusan data (*Right to be Forgotten*) jika pengguna ingin menutup akun.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 2.1

### Membangun Layanan Web RESTful API Mandiri Menggunakan Python

**Tujuan Pembelajaran:**
Peserta didik secara mandiri mampu merancang server web mini menggunakan bahasa Python (memanfaatkan modul bawaan `http.server` atau kerangka kerja mikro), menyajikan endpoint API yang merespons permintaan GET dan POST dalam format data standar JSON, serta mematuhi kaidah kode status HTTP yang benar.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terpasang.
2. Alat penguji API (Browser web, ekstensi cURL terminal, atau aplikasi Postman).

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `server_api_sekolah.py`.
2. Ketikkan kode implementasi server REST API mandiri berikut:

```python
# Server REST API Mandiri Berbasis HTTP Server Python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Database tiruan dalam memori server (Mock In-Memory DB)
DATABASE_SISWA = [
    {"id": 1, "nisn": "008101", "nama": "Arya Dinata", "jurusan": "RPL"},
    {"id": 2, "nisn": "008102", "nama": "Dinda Kirana", "jurusan": "Sains Data"}
]

class RestApiHandler(BaseHTTPRequestHandler):
    # Mengatur header respons standar JSON
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Menangani Permintaan HTTP GET (Membaca Data)
    def do_GET(self):
        if self.path == '/api/v1/siswa':
            self._set_headers(200)
            payload = json.dumps({"status": "sukses", "data": DATABASE_SISWA})
            self.wfile.write(payload.encode('utf-8'))
        else:
            self._set_headers(404)
            pesan_galat = json.dumps({"status": "gagal", "pesan": "Endpoint URL tidak ditemukan!"})
            self.wfile.write(pesan_galat.encode('utf-8'))

    # Menangani Permintaan HTTP POST (Menambah Data Baru)
    def do_POST(self):
        if self.path == '/api/v1/siswa':
            # Membaca panjang bodi permintaan data
            content_length = int(self.headers.get('Content-Length', 0))
            body_data = self.rfile.read(content_length)
            
            try:
                # Deserialisasi bodi JSON masukan
                data_baru = json.loads(body_data.decode('utf-8'))
                
                # Validasi kelengkapan kolom data
                if "nama" not in data_baru or "jurusan" not in data_baru:
                    self._set_headers(400)
                    respons = json.dumps({"status": "gagal", "pesan": "Kolom 'nama' dan 'jurusan' wajib diisi!"})
                    self.wfile.write(respons.encode('utf-8'))
                    return

                # Menambahkan data ke database memori
                data_baru["id"] = len(DATABASE_SISWA) + 1
                DATABASE_SISWA.append(data_baru)

                self._set_headers(201)  # 201 Created
                respons_sukses = json.dumps({"status": "sukses", "pesan": "Siswa berhasil ditambahkan", "data": data_baru})
                self.wfile.write(respons_sukses.encode('utf-8'))

            except json.JSONDecodeError:
                self._set_headers(400)
                respons_galat = json.dumps({"status": "gagal", "pesan": "Format bodi JSON tidak valid!"})
                self.wfile.write(respons_galat.encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(b'{"status": "gagal", "pesan": "Endpoint tidak ditemukan"}')

def jalankan_server_api(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RestApiHandler)
    print(f"===== SERVER REST API BERJALAN PADA PORT http://localhost:{port}/api/v1/siswa =====")
    print("Tekan Ctrl+C untuk menghentikan server secara aman.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("
[INFO] Server dihentikan oleh pengguna.")
        httpd.server_close()

if __name__ == '__main__':
    jalankan_server_api()
```

3. Jalankan skrip di terminal: `python server_api_sekolah.py`.
4. Buka peramban (*web browser*) dan akses URL `http://localhost:8080/api/v1/siswa`. Amati bagaimana peramban menampilkan teks data berformat JSON secara instan!
5. Buka tab terminal kedua, lalu uji pengiriman data baru menggunakan perintah `curl`:
   ```bash
   curl -X POST http://localhost:8080/api/v1/siswa -H "Content-Type: application/json" -d "{"nama": "Bagas Perkasa", "jurusan": "Teknik Komputer"}"
   ```
6. Muat ulang peramban kalian dan buktikan bahwa data Bagas telah sukses bertambah di server!

**Pertanyaan Analisis Laboratorium:**
1. Apa keunggulan mengirimkan data dalam format teks JSON dibandingkan mengirimkan halaman antarmuka HTML utuh dari server ke aplikasi ponsel pintar?
2. Mengapa server wajib mengembalikan status kode HTTP `201 Created` saat data baru sukses disimpan, bukan sekadar kode `200 OK`?
3. Ujilah skenario galat: Kirimkan permintaan POST dengan bodi JSON yang sengaja dirusak sintaksisnya (misalnya tanda kurung kurawal tidak ditutup). Amati apakah server tetap bertahan dan mengirimkan kode tanggapan `400 Bad Request`!

---

## F. RANGKUMAN MATERI BAB II

1. **Standar Pertukaran Data Modern:** Standardisasi karakter global UTF-8 memungkinkan representasi multibahasa internasional. Format JSON telah menjadi standar de facto pertukaran data web modern karena sifatnya yang ringan, hemat kuota data jaringan, dan mudah diproses lintas bahasa pemrograman melalui proses *Serialisasi* (`json.dumps`) dan *Deserialisasi* (`json.loads`).
2. **Kueri Relasional Tingkat Lanjut:** Penggabungan data multi-tabel menggunakan `INNER JOIN` (data yang cocok di kedua tabel) dan `LEFT JOIN` (seluruh data tabel kiri). Rekapitulasi laporan analitis didukung fungsi agregat (`COUNT`, `AVG`, `SUM`), pengelompokan kategori (`GROUP BY`), dan filter pasca-agregasi (`HAVING`).
3. **Arsitektur RESTful API:** Antarmuka layanan web berbasis protokol HTTP tanpa penyimpanan sesi (*stateless*). Menggunakan metode standar `GET` (baca), `POST` (tambah), `PUT` (perbarui), dan `DELETE` (hapus), serta merespons klien menggunakan kode status terstandar (200, 201, 400, 404, 500).
4. **Keamanan Siber & Regulasi:** Penerapan *Parameterized Query* (`?`) wajib ditegakkan untuk memusnahkan kerentanan peretasan *SQL Injection*. Kata sandi akun wajib dienkripsi dengan algoritma hashing satu arah berkriptografi kuat. Inovator sistem wajib tunduk pada mandat perlindungan privasi UU PDP No. 27/2022.

---

## G. UJI KOMPETENSI BAB II

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Format standar pertukaran data modern berbasis teks terbuka yang tersusun atas pasangan Kunci dan Nilai (*Key-Value Pairs*) serta menjadi standar baku komunikasi antarmuka REST API adalah...
   A. Binary EXE
   B. JSON (JavaScript Object Notation)
   C. Spreadsheet XLS
   D. Bitmap Raw

2. Dalam pustaka bawaan Python `json`, fungsi yang digunakan untuk mengubah objek struktur data memori Python (seperti Dictionary) menjadi untaian teks string JSON dinamakan...
   A. `json.loads()`
   B. `json.dumps()`
   C. `json.decode()`
   D. `json.write()`

3. Operasi penggabungan dua tabel pada sintaks SQL yang menampilkan seluruh baris data dari tabel utama sebelah kiri meskipun tidak memiliki data pasangan yang cocok di tabel sebelah kanan adalah...
   A. `INNER JOIN`
   B. `CROSS JOIN`
   C. `LEFT JOIN`
   D. `UNION ALL`

4. Klausa dalam perintah SQL yang berfungsi untuk memfilter atau menyaring hasil perhitungan fungsi agregasi (seperti menyaring nilai rata-rata `AVG()` yang lebih dari 80) adalah...
   A. `WHERE`
   B. `HAVING`
   C. `ORDER BY`
   D. `GROUP BY`

5. Metode protokol komunikasi HTTP yang digunakan oleh aplikasi klien untuk mengirimkan data formulir pendaftaran baru ke server guna disimpan ke dalam pangkalan data adalah...
   A. `GET`
   B. `DELETE`
   C. `POST`
   D. `HEAD`

6. Kode status respons HTTP terstandarisasi yang dikembalikan oleh server web service REST API untuk menginformasikan bahwa data baru telah sukses dibuat dan tersimpan di database adalah...
   A. 200 OK
   B. 201 Created
   C. 404 Not Found
   D. 500 Internal Server Error

7. Kode status tanggapan HTTP yang menandakan bahwa URL endpoint yang diminta klien salah atau sumber daya data yang dicari tidak ditemukan di server adalah...
   A. 400 Bad Request
   B. 401 Unauthorized
   C. 404 Not Found
   D. 503 Service Unavailable

8. Praktik perancangan kode kueri basis data dengan menggunakan tanda parameter pemisah (seperti tanda `?` pada Python SQLite) bertujuan utama untuk memusnahkan ancaman peretasan yang dinamakan...
   A. Distributed Denial of Service (DDoS)
   B. Man-in-the-Middle (MitM)
   C. SQL Injection
   D. Ransomware

9. Mengapa kata sandi pengguna dalam basis data tidak boleh disimpan dalam bentuk teks biasa (*plain text*) dan wajib dienkripsi menggunakan fungsi Hash satu arah (*One-Way Hash*)?
   A. Karena teks biasa menghabiskan memori monitor komputer
   B. Karena fungsi Hash memastikan bahwa meskipun pangkalan data diretas, kata sandi asli pengguna tidak dapat dibaca kembali
   C. Karena teks biasa memperlambat koneksi WiFi sekolah
   D. Karena format hash dapat diubah menjadi gambar bergerak

10. Landasan hukum nasional di Indonesia yang mewajibkan setiap perancang dan pengelola sistem aplikasi untuk menjaga kerahasiaan dan keamanan data pribadi masyarakat adalah...
    A. UU Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)
    B. UU Lalu Lintas dan Angkutan Jalan
    C. UU Perpustakaan Nasional
    D. UU Hak Paten Industri Maritim

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara proses Serialisasi dan Deserialisasi dalam konteks komunikasi data antara aplikasi klien dan server! Mengapa format teks JSON lebih unggul dibandingkan format biner murni untuk komunikasi lintas platform?
2. Diberikan dua tabel relasional:
   - Tabel `siswa` (kolom: `nisn`, `nama_lengkap`, `id_kelas`)
   - Tabel `kelas` (kolom: `id_kelas`, `nama_ruang_kelas`, `wali_kelas`)
   Tuliskan sintaks kueri SQL lengkap menggunakan klausa `INNER JOIN` untuk menampilkan kolom `nama_lengkap`, `nama_ruang_kelas`, dan `wali_kelas` yang diurutkan secara alfabetis berdasarkan nama siswa!
3. Uraikan pemetaan empat metode utama protokol HTTP (GET, POST, PUT, DELETE) terhadap empat operasi dasar manipulasi pangkalan data (*CRUD: Create, Read, Update, Delete*)!
4. Jelaskan secara teknis bagaimana serangan siber *SQL Injection* dapat membobol sistem otentikasi login jika kode program menggunakan penggabungan string (*string concatenation*)! Tunjukkan bentuk potongan kodenya dan perbaikannya menggunakan *Parameterized Query*!
5. Sebutkan dan jelaskan minimal tiga prinsip utama etika dan hukum yang diatur dalam Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022) yang wajib dipatuhi oleh seorang pengembang perangkat lunak aplikasi di Indonesia!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB II

**Kunci Pilihan Ganda:**
1. **B** (JSON adalah standar de facto pertukaran data terbuka berbasis key-value pairs).
2. **B** (`json.dumps()` mengubah objek memori Python menjadi teks string JSON).
3. **C** (`LEFT JOIN` menampilkan seluruh baris tabel kiri dan data cocok dari tabel kanan).
4. **B** (`HAVING` menyaring hasil kelompok dari fungsi agregasi).
5. **C** (`POST` digunakan untuk mengirimkan data baru ke server).
6. **B** (`201 Created` menandakan sumber daya baru berhasil diciptakan di server).
7. **C** (`404 Not Found` menandakan URL endpoint atau ID data tidak ditemukan).
8. **C** (Parameterized query mencegah manipulasi sintaks dari serangan SQL Injection).
9. **B** (Fungsi hash satu arah menjamin kata sandi tidak dapat direkonstruksi jika database bocor).
10. **A** (UU PDP No. 27 Tahun 2022 adalah payung hukum perlindungan data pribadi di Indonesia).

**Pembahasan Soal Uraian:**
1. *Serialisasi vs Deserialisasi & Keunggulan JSON:*
   - Serialisasi adalah konversi struktur data objek di memori lokal menjadi deretan teks terstandar (JSON) agar dapat dikirim melalui protokol jaringan. Deserialisasi adalah proses kebalikannya: membaca teks JSON dari jaringan menjadi objek struktur data memori lokal yang siap dioperasikan.
   - Keunggulan JSON atas biner murni: JSON bersifat teks universal yang independen dari arsitektur prosesor (endianness) dan sistem operasi, sehingga aplikasi yang ditulis dengan bahasa yang sangat berbeda (misalnya Python di server dan Swift di iPhone) dapat saling memahami data tanpa konversi tipe data biner tingkat rendah yang rumit.
2. *Sintaks SQL INNER JOIN:*
   ```sql
   SELECT 
       s.nama_lengkap, 
       k.nama_ruang_kelas, 
       k.wali_kelas
   FROM siswa s
   INNER JOIN kelas k ON s.id_kelas = k.id_kelas
   ORDER BY s.nama_lengkap ASC;
   ```
3. *Pemetaan HTTP ke CRUD:*
   - Create dipetakan ke metode **POST** (membuat data baru di server).
   - Read dipetakan ke metode **GET** (membaca/mengambil data dari server).
   - Update dipetakan ke metode **PUT / PATCH** (memperbarui data yang ada di server).
   - Delete dipetakan ke metode **DELETE** (menghapus data dari server).
4. *Mekanisme SQL Injection & Perbaikannya:*
   - Celah terjadi saat kode ditulis:
     `kueri = "SELECT * FROM users WHERE user='" + input_user + "' AND pass='" + input_pass + "'"`
   - Jika peretas mengisi `input_user` dengan teks: `' OR '1'='1' --`, kueri berubah menjadi:
     `SELECT * FROM users WHERE user='' OR '1'='1' -- AND pass=''`. Tanda `--` mengabaikan pemeriksaan password dan kondisi `'1'='1'` selalu bernilai True, sehingga peretas berhasil login tanpa password.
   - Solusi Parameterized Query:
     `cursor.execute("SELECT * FROM users WHERE user = ? AND pass = ?", (input_user, input_pass))`
   Parameter `?` memisahkan instruksi perintah SQL dari data mentah, sehingga masukan peretas diperlakukan murni sebagai string data biasa dan tidak akan mengubah logika kueri database.
5. *Tiga Prinsip UU PDP bagi Pengembang:*
   (1) Prinsip Pembatasan Tujuan: Data pribadi hanya boleh dikumpulkan sesuai tujuan yang telah disetujui pengguna dan dilarang disalahgunakan untuk keperluan lain; (2) Prinsip Keamanan & Enkripsi: Pengembang wajib menerapkan standar enkripsi dan kontrol akses ketat untuk melindungi data dari kebocoran siber; (3) Prinsip Akuntabilitas & Hak Pemilik Data: Pengguna berhak meminta perbaikan data, penarikan persetujuan, serta penghapusan data pribadinya dari sistem.


# BAB III: KOLABORASI MULTIMEDIA TINGKAT LANJUT UNTUK PENDUKUNG APLIKASI

## APERSEPSI: MENGAPA KARYA APLIKASI HEBAT BISA DIABAIKAN PENGGUNA?

Di laboratorium multimedia dan desain grafis sekolah, Dinda tampak sedang menatap layar presentasi dengan dahi berkerut. Di hadapannya, Arya dan Bagas baru saja selesai memprogram sebuah modul sistem otomasi perpustakaan sekolah yang sangat canggih berbasis algoritma pencarian biner dan REST API. Namun saat mereka mengundang perwakilan pengurus OSIS dan pustakawan sekolah untuk mencoba aplikasi tersebut, suasana canggung pun terjadi.

[GAMBAR: assets/bab3_komik_pembuka_sma11.png]

"Adik-adik, aplikasi kalian ini di mana tombol untuk mencari bukunya ya?" tanya Ibu Pustakawan dengan bingung. "Ikon-ikon di layarnya tampak buram dan pecah saat layarku diperbesar, teks keterangannya berwarna abu-abu redup di atas latar belakang putih sehingga tidak terbaca, dan saat saya mengunduh berkasnya dari repositori, tidak ada petunjuk sama sekali tentang bagaimana cara menjalankannya di komputer lab!"

Bagas menunduk pelan seraya menggaruk tengkuknya. "Aduh, maafkan kami, Bu. Kami terlalu asyik mengoptimalkan kode backend dan kueri SQL di terminal sampai-sampai kami lupa membuat dokumen panduan pengguna dan tidak memperhatikan kualitas aset visual layarnya."

Dinda tersenyum seraya menepuk pundak kedua rekannya. "Inilah pelajaran paling berharga dalam dunia rekayasa teknologi komersial, kawan-kawan. Sebuah perangkat lunak tidak akan pernah dianggap selesai hanya karena kodenya berhasil dieksekusi tanpa galat. Produk perangkat lunak profesional wajib didukung oleh ekosistem multimedia dan komunikasi teknis yang terpadu!"

"Benar sekali," sambung Arya. "Kita membutuhkan aset antarmuka grafis berbasis vektor **SVG (*Scalable Vector Graphics*)** yang tetap tajam sempurna di berbagai ukuran layar monitor, desain warna yang mematuhi standar aksesibilitas internasional **WCAG**, dokumentasi teknis terstandar industri seperti berkas **README.md** dan manajemen dependensi **requirements.txt**, serta keterampilan melakukan **pitching produk** yang persuasif di hadapan publik dan pemangku kepentingan!"

"Tepat!" seru Dinda. "Mari kita pelajari seni mengemas karya rekayasa perangkat lunak menjadi produk digital unggulan yang ramah pengguna, terdokumentasi rapi, dan memukau dunia industri!"

---

## A. PERANCANGAN ASET ANTARMUKA PENGGUNA VEKTOR (SVG) DAN AKSESIBILITAS WCAG

Kualitas pengalaman pengguna (*User Experience* / UX) pada sebuah aplikasi modern sangat ditentukan oleh ketajaman aset grafis dan kemudahan navigasi visual pada berbagai resolusi gawai (*cross-device responsiveness*).

### 1. Keunggulan Format Vektor SVG atas Format Raster Bitmap

Dalam desain antarmuka digital, terdapat dua kelompok format gambar utama:
- **Format Raster / Bitmap (PNG, JPEG, WebP):** Tersusun atas kisi-kisi piksel warna statis. Ketika antarmuka diperbesar pada layar beresolusi tinggi (Retina display atau monitor 4K), gambar raster akan mengalami artefak pecah, buram, dan bergerigi (*pixelated*).
- **Format Vektor SVG (Scalable Vector Graphics):** Tersusun atas rumus-rumus matematika geometris (garis, kurva Bezier, koordinat poligon) yang ditulis dalam sintaks berbasis teks XML terbuka.

**Mengapa SVG Menjadi Standar Baku Desain Antarmuka Modern?**
1. **Ketajaman Tak Terbatas (*Infinite Scalability*):** Aset ikon dan logo SVG dapat diperbesar hingga ukuran baliho raksasa atau diperkecil ke ukuran layar jam tangan pintar (*smartwatch*) tanpa mengalami penurunan kualitas sedikit pun.
2. **Ukuran Berkas Sangat Kecil:** Karena hanya berisi instruksi teks matematika, berkas SVG sering kali hanya berukuran 1 hingga 5 Kilobyte, menghemat kuota internet dan mempercepat waktu pemuatan aplikasi (*loading time*).
3. **Dapat Dimanipulasi dengan Kode (CSS & JavaScript):** Warna, garis tepi (*stroke*), dan animasi ikon SVG dapat diubah secara langsung menggunakan baris kode program secara dinamis tanpa perlu mengekspor ulang gambar.

```xml
<!-- Contoh Sintaks Berkas Vektor SVG: Ikon Centang Sukses -->
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
  <path d="m9 12 2 2 4-4"/>
</svg>
```

### 2. Standar Aksesibilitas Kontras Warna: WCAG (Web Content Accessibility Guidelines)

Sebagai pengembang aplikasi yang inklusif dan humanis, antarmuka perangkat lunak tidak boleh hanya nyaman dilihat oleh mata normal pada kondisi cahaya ideal, melainkan wajib dapat diakses dengan mudah oleh penyandang gangguan penglihatan parsial (*color blindness*) atau pengguna ponsel di bawah terik sinar matahari.

Berdasarkan konsensus resmi konsorsium web dunia **WCAG Level AA**, standar kontras minimum yang wajib dipenuhi adalah:
- **Teks Biasa / Normal:** Rasio kontras kecerahan (*luminance contrast ratio*) antara warna teks dan warna latar belakang minimal **4,5 banding 1 (4.5:1)**.
- **Teks Berukuran Besar / Tebal:** Rasio kontras minimal **3,0 banding 1 (3.0:1)**.
- **Komponen Interaktif & Ikon:** Rasio kontras minimal **3,0 banding 1** terhadap latar sekitarnya.

Contoh Pelanggaran: Menggunakan teks abu-abu terang `#A0AEC0` di atas latar putih `#FFFFFF` hanya menghasilkan rasio kontras ~2,3:1 (GAGAL WCAG). Pengembang wajib menggantinya dengan abu-abu gelap `#4A5568` yang menghasilkan rasio kontras 5,6:1 (LOLOS WCAG).

---

## B. PENYUSUNAN DOKUMENTASI TEKNIS PERANGKAT LUNAK: README.MD DAN DEPENDENSI

Di dunia rekayasa perangkat lunak profesional dan ekosistem sumber terbuka (*open source*), sebuah repositori kode tanpa dokumentasi teknis dianggap tidak layak digunakan oleh industri. Dokumentasi teknis (*Technical Writing*) adalah jembatan komunikasi antara pencipta kode dan pengembang lain yang ingin menguji, memasang, atau berkontribusi pada proyek tersebut.

### 1. Anatomi Berkas Dokumentasi Standar: `README.md`

Berkas `README.md` yang diletakkan pada direktori akar (*root*) repositori GitHub wajib disusun menggunakan format Markdown terstruktur yang mencakup elemen-elemen kunci berikut:

1. **Judul Proyek & Lencana Status (*Badges*):** Nama sistem, versi rilis, dan indikator status kelulusan pengujian kode.
2. **Deskripsi Ringkas & Nilai Manfaat:** Penjelasan 2-3 paragraf mengenai masalah nyata apa yang dipecahkan oleh perangkat lunak tersebut.
3. **Daftar Fitur Utama (*Key Features*):** Poin-poin kemampuan fungsional sistem.
4. **Prasyarat Sistem & Dependensi (*Prerequisites*):** Versi bahasa pemrograman yang dibutuhkan (misal: Python >= 3.10) dan basis data yang kompatibel.
5. **Panduan Instalasi Langkah demi Langkah (*Installation Guide*):** Perintah terminal konkret untuk mengkloning repositori, membuat lingkungan virtual (*virtual environment*), dan menginstal pustaka eksternal.
6. **Petunjuk Penggunaan (*Usage & Examples*):** Contoh perintah untuk menjalankan server atau menggunakan antarmuka API.
7. **Lisensi & Pedoman Kontribusi (*License & Contributing*):** Ketentuan hak cipta (misal lisensi MIT atau Apache 2.0).

### 2. Manajemen Dependensi Proyek: `requirements.txt`

Proyek perangkat lunak Python kelas industri hampir selalu memanfaatkan pustaka eksternal pihak ketiga (seperti Flask, Scikit-Learn, Pandas, atau Requests). Agar proyek tersebut dapat dijalankan dengan lancar di komputer anggota tim lain atau server produksi tanpa kegagalan versi pustaka (*dependency mismatch*), digunakan berkas manifes **`requirements.txt`**.

**Perintah Pengelolaan Dependensi Menggunakan `pip`:**
- Mencatat seluruh pustaka terpasang beserta nomor versinya secara otomatis:
  ```bash
  pip freeze > requirements.txt
  ```
- Menginstal seluruh dependensi secara massal di komputer baru hanya dengan satu baris perintah:
  ```bash
  pip install -r requirements.txt
  ```

Contoh Isi Berkas `requirements.txt`:
```text
Flask==3.0.0
requests==2.31.0
scikit-learn==1.4.0
pandas==2.2.0
```

---

## C. SENI PITCHING DAN DEMONSTRASI PRODUK PERANGKAT LUNAK STARTUP

Keahlian teknis koding tingkat tinggi akan menjadi sia-sia jika seorang inovator muda tidak mampu mengomunikasikan gagasan dan nilai guna produknya kepada calon pengguna, pimpinan lembaga, atau calon investor modal ventura. Seni ini dikenal sebagai **Pitching Produk (*Product Pitching*)**.

### 1. Struktur Rangka Presentasi Pitching 5 Menit (The Pitch Deck Structure)

Presentasi demonstrasi produk yang memikat audiens umumnya mengikuti alur narasi dramatis 6 babak:

1. **The Hook & Problem (Sengatan Masalah Nyata - 1 Menit):**
Membuka presentasi dengan cerita empatik atau data statistik faktual mengenai masalah mendesak yang dihadapi masyarakat. *Contoh: "Setiap hari, 85% siswa antre lebih dari 20 menit hanya untuk meminjam buku paket di perpustakaan sekolah."*
2. **The Solution (Solusi Cerdas Kita - 30 Detik):**
Memperkenalkan produk perangkat lunak sebagai jawaban tuntas atas masalah tersebut dengan proposisi nilai yang unik dan jelas.
3. **Live Product Demo (Unjuk Kerja Nyata - 2 Menit):**
Mendemonstrasikan fitur unggulan aplikasi secara langsung (*live software run*). Tunjukkan alur kerja dari sudut pandang pengguna awam, bukan sekadar menampilkan baris terminal koding.
4. **Under the Hood / Technology Stack (Arsitektur Teknologi - 30 Detik):**
Menjelaskan secara ringkas fondasi keandalan teknis di balik sistem (misalnya: dibangun dengan arsitektur OOP Python modular, RESTful API terenkripsi, dan basis data ternormalisasi).
5. **Impact & Scalability (Dampak Sosial & Prospek Masa Depan - 30 Detik):**
Menguraikan efisiensi waktu atau penghematan biaya yang dirasakan sekolah serta rencana pengembangan fitur cerdas berikutnya.
6. **The Team & Call to Action (Tim Pengembang & Ajakan - 30 Detik):**
Memperkenalkan pembagian peran tim (misal Arya sebagai Backend & AI Engineer, Bagas sebagai Database & DevOps, Dinda sebagai UI/UX & Quality Assurance) dan menutup presentasi dengan ajakan kolaborasi yang hangat.

---

## D. LEMBAR KERJA PESERTA DIDIK (LKPD) 3.1

### Penyusunan Dokumentasi Repositori Teknis dan Video Pitching Produk

**Tujuan Pembelajaran:**
Peserta didik secara berkelompok mampu menyusun dokumen panduan teknis `README.md` berstandar GitHub, menghasilkan berkas manifes dependensi `requirements.txt`, merancang ikon antarmuka SVG berbasis standar kontras WCAG, serta menyajikan video demonstrasi pitching produk berdurasi 3 hingga 5 menit.

**Alat dan Bahan:**
1. Repositori proyek perangkat lunak kelompok yang telah dikembangkan di bab sebelumnya.
2. Kode editor (Visual Studio Code).
3. Perekam layar dan mikrofon untuk video demo pitching.

**Langkah Kerja Proyek:**
1. Bukalah folder proyek perangkat lunak kalian di VS Code.
2. Buatlah berkas baru bernama `README.md` pada direktori utama proyek, lalu susunlah dokumentasi dengan struktur rapi seperti contoh berikut:

```text
# Sistem Cerdas Manajemen Inventaris Sekolah (SCMIS)

[Status Build: Stabil] | [Lisensi: MIT] | [Python: 3.10+]

## Deskripsi Singkat
SCMIS adalah solusi rekayasa perangkat lunak terintegrasi yang dirancang untuk mengotomasi pencatatan, peminjaman, dan audit aset laboratorium komputer sekolah secara real-time melalui antarmuka RESTful API.

## Fitur Utama
- Arsitektur OOP Modular: Menggunakan prinsip enkapsulasi dan pewarisan kelas.
- RESTful API Service: Melayani pertukaran data ringan format JSON.
- Keamanan Siber: Dilengkapi parameterized query penangkal SQL Injection.

## Panduan Instalasi Cepat
1. Kloning repositori ini:
   git clone https://github.com/sekolah/scmis-app.git
   cd scmis-app
2. Pasang dependensi pustaka yang dibutuhkan:
   pip install -r requirements.txt
3. Jalankan peladen aplikasi:
   python server.py

## Tim Pengembang
- Arya Dinata: Arsitek Perangkat Lunak & Logika OOP
- Bagas Perkasa: Perekayasa Basis Data & Integrasi API
- Dinda Kirana: Desainer Antarmuka UI/UX & Dokumentasi Teknis
```

3. Jalankan perintah `pip freeze > requirements.txt` untuk membekukan daftar dependensi pustaka Python proyek kalian.
4. Rekamlah sebuah video presentasi demo produk berdurasi 3 menit yang membagi peran setiap anggota kelompok sesuai panduan struktur pitching!

**Kriteria Penilaian Produk:**
- Kelengkapan struktur berkas `README.md` (30%)
- Validitas berkas dependensi `requirements.txt` (20%)
- Kepatuhan kontras warna antarmuka terhadap standar WCAG (20%)
- Keterampilan komunikasi persuasif dan kejelasan demo video pitching (30%)

---

## E. RANGKUMAN MATERI BAB III

1. **Aset Visual Antarmuka SVG:** Format vektor SVG berbasis teks matematika XML memberikan ketajaman visual tak terbatas pada berbagai resolusi layar tanpa pembengkakan ukuran berkas. Penerapan rasio kontras warna standar internasional WCAG (minimal 4.5:1 untuk teks normal) menjamin aksesibilitas aplikasi bagi seluruh pengguna.
2. **Dokumentasi Teknis Profesional:** Berkas `README.md` adalah dokumen wajib repositori GitHub yang memuat deskripsi produk, prasyarat, panduan instalasi terminal langkah demi langkah, dan informasi lisensi. Berkas manifes `requirements.txt` menjamin reproduksibilitas instalasi pustaka pihak ketiga secara instan dan seragam.
3. **Seni Demonstrasi Pitching Startup:** Keberhasilan diseminasi inovasi perangkat lunak menuntut kemampuan menyampaikan nilai guna produk melalui struktur narasi terpadu: *Hook* masalah riil, solusi cerdas, demonstrasi operasional aplikasi langsung, arsitektur teknologi pendukung, dampak sosial, dan pengenalan tim pengembang.

---

## F. UJI KOMPETENSI BAB III

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Format gambar digital berikut ini yang menggunakan formula matematika geometris berbasis XML sehingga tidak akan pernah pecah atau buram saat diperbesar pada layar resolusi tinggi adalah...
   A. JPEG
   B. PNG
   C. SVG (Scalable Vector Graphics)
   D. GIF

2. Berdasarkan panduan standar aksesibilitas web internasional (WCAG Level AA), berapakah rasio kontras kecerahan minimum yang wajib dipenuhi antara warna teks biasa dan warna latar belakangnya?
   A. 1,5 : 1
   B. 2,0 : 1
   C. 4,5 : 1
   D. 10 : 1

3. Berkas dokumentasi utama yang wajib ada pada direktori akar sebuah repositori proyek perangkat lunak di platform GitHub untuk memandu pengembang lain dinamakan...
   A. `index.html`
   B. `config.ini`
   C. `README.md`
   D. `license.txt`

4. Perintah terminal berbasis manajer paket Python (`pip`) yang digunakan untuk mencatat dan membekukan seluruh nama pustaka eksternal beserta nomor versinya yang aktif ke dalam sebuah berkas manifes teks adalah...
   A. `pip install --upgrade`
   B. `pip freeze > requirements.txt`
   C. `pip list --format=json`
   D. `pip uninstall all`

5. Apabila seorang pengembang baru mengkloning repositori proyek Python di komputer pribadinya, perintah terminal tunggal yang tepat untuk menginstal seluruh pustaka yang tercatat dalam berkas manifes dependensi adalah...
   A. `pip run requirements.txt`
   B. `pip install -r requirements.txt`
   C. `python setup.py install`
   D. `git pull requirements.txt`

6. Di bawah ini yang BUKAN merupakan keunggulan dari format vektor SVG dibandingkan format gambar raster bitmap pada desain antarmuka aplikasi adalah...
   A. Ukuran berkas relatif sangat kecil dan hemat kuota
   B. Warna dan garisnya dapat dimanipulasi secara dinamis menggunakan kode program
   C. Gambar tidak akan buram saat diperbesar di layar Retina monitor 4K
   D. Merekam foto panorama alam nyata dengan detail gradasi warna jutaan daun secara alami

7. Dalam tahapan presentasi pitching produk teknologi berdurasi singkat, bagian pembuka presentasi yang menyajikan data faktual mengejutkan atau cerita empatik untuk menarik fokus perhatian dewan penguji disebut...
   A. The Call to Action
   B. The Technical Architecture
   C. The Hook
   D. The Business Model

8. Manakah pasangan warna teks dan warna latar belakang berikut yang secara jelas MELANGGAR aturan aksesibilitas WCAG karena memiliki rasio kontras yang terlalu rendah dan sulit dibaca?
   A. Teks Hitam pekat di atas latar Putih bersih
   B. Teks Kuning muda cerah di atas latar Putih bersih
   C. Teks Biru gelap pekat di atas latar Abu-abu terang
   D. Teks Putih bersih di atas latar Biru tua malam

9. Praktik etis dalam komunikasi teknis saat mempresentasikan produk perangkat lunak di hadapan audiens umum adalah...
   A. Memberikan janji palsu berlebihan (*overpromising*) mengenai fitur yang sebenarnya belum selesai diprogram
   B. Menjelaskan nilai guna nyata produk dengan jujur, transparan, dan mendemonstrasikan fungsionalitas sistem apa adanya
   C. Mengklaim karya pustaka sumber terbuka milik komunitas dunia sebagai hasil buatan tangan sendiri tanpa atribusi
   D. Menyembunyikan seluruh kelemahan sistem agar mendapatkan nilai sempurna

10. Bagian dalam berkas `README.md` yang memberikan instruksi baris demi baris mengenai cara menyiapkan sistem di komputer baru mulai dari kloning hingga menjalankan aplikasi disebut...
    A. License Terms
    B. Installation Guide
    C. Project Badges
    D. Contribution Guidelines

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara representasi grafis Raster Bitmap dan Vektor SVG dari sudut pandang penyimpanan data matematika! Mengapa para perancang antarmuka antarmuka UI/UX modern memprioritaskan SVG untuk aset ikon dan tombol aplikasi?
2. Analisislah mengapa standar kontras warna WCAG sangat krusial dalam perancangan aplikasi publik (seperti portal layanan sekolah atau aplikasi perbankan)! Apa dampak sosial yang timbul jika perancang antarmuka mengabaikan standar aksesibilitas tersebut?
3. Uraikan secara rinci struktur anatomi sebuah berkas `README.md` yang profesional pada repositori GitHub! Jelaskan fungsi penting dari masing-masing bagian tersebut bagi pengembang lain yang baru bergabung!
4. Jelaskan apa yang dimaksud dengan fenomena *"It works on my machine!"* (aplikasi berjalan lancar di laptop pembuatnya namun gagal berfungsi saat dipasang di komputer orang lain)! Bagaimana keberadaan berkas `requirements.txt` menyelesaikan krisis tersebut?
5. Rancanglah draf naskah presentasi pitching berdurasi 3 menit untuk sebuah aplikasi inovasi sekolah buatan kalian! Susun naskah tersebut ke dalam lima babak narasi: Hook Masalah, Solusi Cerdas, Demonstrasi Fungsional, Landasan Arsitektur Teknologi, dan Ajakan Aksi Penutup!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB III

**Kunci Pilihan Ganda:**
1. **C** (SVG menggunakan rumus matematika geometris XML sehingga skalabel tanpa pecah).
2. **C** (WCAG Level AA menetapkan kontras teks normal minimal 4,5 : 1).
3. **C** (`README.md` adalah berkas dokumentasi utama pada repositori GitHub).
4. **B** (`pip freeze > requirements.txt` membekukan seluruh dependensi ke berkas teks).
5. **B** (`pip install -r requirements.txt` menginstal seluruh dependensi secara massal).
6. **D** (Foto pemandangan alam nyata dengan jutaan gradasi kompleks lebih tepat disimpan dalam format raster foto seperti JPEG, bukan SVG).
7. **C** (The Hook adalah pembuka pemikat perhatian audiens di awal presentasi).
8. **B** (Teks kuning muda di atas latar putih memiliki kontras sangat rendah dan tidak terbaca).
9. **B** (Transparansi dan kejujuran tanpa overpromising adalah integritas komunikasi teknis).
10. **B** (Installation Guide memandu instalasi langkah demi langkah).

**Pembahasan Soal Uraian:**
1. *Raster Bitmap vs Vektor SVG:*
   - Raster Bitmap menyimpan data citra sebagai kisi-kisi warna piksel individual diskret. Jika diperbesar, piksel meregang sehingga gambar menjadi pecah (*pixelated*).
   - Vektor SVG menyimpan citra sebagai serangkaian perintah teks matematika geometris (koordinat titik, lingkaran, kurva). Saat diperbesar, prosesor komputer menghitung ulang rumus matematikanya secara instan sehingga garis tetap tajam sempurna pada resolusi apa pun. Perancang UI memprioritaskan SVG karena tajam di layar gawai apa pun dan ukuran filenya sangat ringan.
2. *Signifikansi Standar Aksesibilitas WCAG:*
   Standar WCAG memastikan produk teknologi bersifat inklusif bagi seluruh warga masyarakat, termasuk penyandang disabilitas penglihatan parsial (*low vision* atau buta warna) serta pengguna yang berada di lingkungan ekstrim (di bawah terik matahari siang). Jika diabaikan, sebagian kelompok masyarakat akan terisolasi secara digital (*digital exclusion*), tidak dapat membaca informasi pengumuman sekolah atau tombol konfirmasi transaksi, yang berpotensi menimbulkan kerugian hak sosial dan finansial.
3. *Anatomi Berkas README.md Profesional:*
   - Judul & Badge: Mengidentifikasi nama proyek dan status kesehatan kode secara visual.
   - Deskripsi Masalah & Solusi: Menjelaskan urgensi produk dan nilai manfaat yang ditawarkan.
   - Fitur Utama: Merangkum kapabilitas sistem dalam poin-poin singkat yang mudah dipindai mata.
   - Prasyarat & Instalasi: Menuliskan instruksi terminal konkret yang dapat disalin-tempel oleh pengembang lain untuk menduplikasi lingkungan kerja.
   - Lisensi & Kontribusi: Menegaskan batasan hukum penggunaan kode serta tata cara mengirimkan kontribusi perbaikan kode sumber.
4. *Penyelesaian Krisis "It works on my machine":*
   Fenomena ini terjadi karena perbedaan versi pustaka pihak ketiga (*library dependency mismatch*) yang terpasang di komputer pengembang versus komputer pengguna lain. Misalnya, fungsi tertentu hanya ada pada pustaka versi 3.0, sementara di komputer lain masih terpasang versi 1.0. Berkas `requirements.txt` menyelesaikan krisis ini dengan mengunci nomor versi eksak setiap dependensi, sehingga perintah `pip install -r requirements.txt` mereplikasi kondisi lingkungan kerja secara 100% identik di komputer mana pun.
5. *Draf Naskah Pitching 3 Menit (Contoh Produk Bank Sampah Digital Sekolah):*
   - Babak 1 (Hook): "Tahukah Anda bahwa kantin sekolah kita menghasilkan 50 kg sampah plastik setiap hari yang 80% di antaranya berakhir di tempat pembuangan akhir tanpa dipilah?"
   - Babak 2 (Solusi): "Kami mempersembahkan *EcoSchool Pay*, aplikasi web service cerdas yang mengubah sampah plastik daur ulang siswa menjadi poin saldo digital belanja koperasi!"
   - Babak 3 (Demo): "Mari kita lihat: Siswa menyetor 5 botol plastik ke loket, petugas memasukkan nomor ID siswa di sistem ini, dan dalam 2 detik, saldo bertambah Rp2.500 yang langsung tercermin di ponsel siswa."
   - Babak 4 (Teknologi): "Sistem ini dibangun dengan arsitektur OOP Python yang tangguh, antarmuka REST API JSON berkecepatan tinggi, serta keamanan parameterized query yang melindungi privasi data siswa sesuai UU PDP."
   - Babak 5 (Ajakan Aksi): "Mari wujudkan sekolah bersih, hijau, dan berdaulat teknologi bersama *EcoSchool Pay*. Terima kasih!"


# BAB IV: FONDASI MACHINE LEARNING: PIPELINE, KLASIFIKASI, DAN EVALUASI MODEL

## APERSEPSI: MENGAPA AKURASI 98% BISA MENIPU KITA?

Di ruang laboratorium kecerdasan artifisial sekolah, Arya tampak bersorak gembira sambil memamerkan hasil grafik di layar monitornya. Di hadapannya, sebuah skrip Python berbasis pustaka Scikit-Learn baru saja selesai mengeksekusi pelatihan model klasifikasi deteksi dini tumor medis.

[GAMBAR: assets/bab4_komik_pembuka_sma11.png]

"Dinda, Bagas, lihat pencapaian ini!" seru Arya dengan penuh kebanggaan. "Model kecerdasan artifisial yang kulatih berhasil meraih skor Akurasi 98,5%! Dari 1.000 data rekam medis pasien uji coba, programku hampir tidak pernah salah memprediksi!"

Dinda mendekat, mengamati struktur sebaran dataset yang digunakan Arya dengan pandangan analitis yang tajam. "Tunggu sebentar, Arya. Mari kita bedah isi dataset yang kamu gunakan. Dari 1.000 data pasien tersebut, berapa banyak pasien yang benar-benar mengidap tumor ganas, dan berapa banyak pasien yang kondisi tubuhnya sehat?"

Arya membuka tabel data mentahnya. "Hmm, di dalam dataset riil ini, pasien yang positif mengidap tumor hanya berjumlah 15 orang, sedangkan 985 pasien lainnya berstatus sehat non-tumor."

Dinda tersenyum prihatin seraya menunjuk baris prediksi model. "Lihat kenyataan pahit ini, kawan. Jika model AI-mu dirancang secara malas untuk selalu menebak bahwa 'Semua Pasien Pasti Sehat', maka secara matematis modelmu otomatis akan langsung memperoleh Akurasi 98,5% (985 dari 1.000 tebakan benar)! Namun apa yang terjadi pada 15 pasien yang sebenarnya mengidap tumor ganas? Modelmu memprediksi mereka sehat, membiarkan penyakit mematikan itu menyebar tanpa penanganan medis!"

Bagas terperangah. "Mengerikan sekali! Pasien yang sakit justru dinyatakan sehat! Itu adalah bencana kegagalan medis yang fatal!"

"Tepat sekali," tegas Dinda. "Pada dataset yang memiliki distribusi kelas sangat timpang (*imbalanced dataset*), parameter Akurasi semu bisa menjadi jebakan mematikan. Dalam rekayasa *Machine Learning* profesional, kita wajib mengevaluasi model secara objektif menggunakan **Matriks Konfusi (*Confusion Matrix*)**, membedah risiko **False Negative**, serta mengukur nilai **Recall**, **Presisi**, dan **F1-Score**!"

Arya tertegun lalu mengangguk penuh rasa hormat. "Kamu benar sekali, Dinda. Ternyata melatih kecerdasan artifisial bukan sekadar mengejar angka akurasi tinggi, melainkan memahami sains matematika evaluasi model. Mari kita bedah tuntas siklus pipeline Machine Learning ini!"

---

## A. TAKSONOMI MACHINE LEARNING: SUPERVISED, UNSUPERVISED, DAN REINFORCEMENT

Untuk memahami kecerdasan artifisial modern, kita harus memahami pergeseran mendasar dari pemrograman konvensional menuju paradigma pembelajaran mesin (*Machine Learning* / ML).

### 1. Paradigma Rule-Based vs Machine Learning

- **Pemrograman Berbasis Aturan Konvensional (*Rule-Based*):**
Manusia merumuskan aturan logika eksplisit (*Rules*) berupa percabangan `if-else` yang kaku, lalu memasukkannya bersama Data masukan ke dalam komputer untuk menghasilkan Jawaban (*Answers*). Kelemahannya: manusia tidak mampu menulis jutaan aturan jika data sangat rumit (seperti mengenali wajah atau mendeteksi sel kanker).
- **Pembelajaran Mesin (*Machine Learning*):**
Membalik paradigma tersebut secara revolusioner. Manusia memasukkan Data dan Jawaban historis ke dalam komputer, lalu algoritma matematika secara mandiri mencari dan memelajari pola aturan (*Rules/Patterns*) tersembunyi di balik data tersebut.

### 2. Tiga Cabang Utama Taksonomi Machine Learning

1. **Supervised Learning (Pembelajaran Terawasi):**
Algoritma dilatih menggunakan dataset yang telah memiliki label kebenaran (*labeled data*). Ibarat seorang murid yang belajar mengerjakan latihan soal disertai kunci jawaban di sampingnya.
Terbagi menjadi dua tugas utama:
- *Klasifikasi:* Memprediksi label kategori diskret (misal: menentukan email Spam vs Bukan Spam, atau memilah tumor Jinak vs Ganas).
- *Regresi:* Memprediksi nilai angka kontinu (misal: memprediksi harga jual rumah berdasarkan luas tanah atau memprediksi suhu udara harian).
2. **Unsupervised Learning (Pembelajaran Tanpa Pengawasan):**
Algoritma diberikan data mentah tanpa label kunci jawaban (*unlabeled data*). Komputer bertugas menemukan struktur alami, kemiripan kelompok, atau pola tersembunyi secara mandiri.
Contoh: Segmentasi pengelompokan pelanggan (*Customer Clustering*) pada aplikasi belanja daring.
3. **Reinforcement Learning (Pembelajaran Berbasis Penguatan):**
Model agen cerdas belajar mengambil keputusan terbaik melalui proses coba-coba (*trial and error*) dalam sebuah lingkungan interaktif, dengan tujuan memaksimalkan penghargaan (*Reward*) dan meminimalkan hukuman (*Penalty*).
Contoh: Agen AI pengemudi mobil otonom atau bot pemain catur profesional (AlphaZero).

---

## B. TAHAPAN PRA-PEMROSESAN DATA DAN PEMBAGIAN DATASET (TRAIN-TEST SPLIT)

Dalam pepatah sains data terkenal: *"Garbage In, Garbage Out"*—jika kita melatih algoritma AI menggunakan data mentah yang kotor, model cerdas apa pun pasti akan menghasilkan prediksi yang kacau dan menyesatkan.

[GAMBAR: assets/bab4_alur_kerja_pipeline_machine_learning.png]

### 1. Siklus Alur Kerja Pipeline Machine Learning

Tahapan rekayasa data standar industri mencakup langkah-langkah berurutan:
1. **Pembersihan Data Nilai Kosong (*Handling Missing Values*):** Mengisi sel data kosong menggunakan nilai rata-rata (*Mean*), nilai tengah (*Median*), atau menghapus baris data jika kerusakannya parah.
2. **Pengkodean Fitur Kategori (*Encoding Categorical Data*):** Komputer hanya memahami angka. Fitur bertipe teks harus dikonversi:
   - *Label Encoding:* Mengubah kategori berjenjang menjadi angka urut (misal: SD=0, SMP=1, SMA=2).
   - *One-Hot Encoding:* Membuat kolom biner baru (0 atau 1) untuk kategori yang setara (misal: Jurusan RPL, Jurusan TKJ, Jurusan DKV) agar model tidak salah mengartikan adanya tingkatan matematis.
3. **Penskalaan Fitur (*Feature Scaling*):** Menyeragamkan rentang skala angka antar-fitur (misal: fitur Umur 15-18 tahun dan fitur Pendapatan Rp2.000.000 - Rp10.000.000) menggunakan metode *Min-Max Normalization* (rentang 0 hingga 1) atau *StandardScaler* (skor-Z). Tanpa penskalaan, fitur dengan angka besar akan mendominasi perhitungan secara tidak adil.

### 2. Pembagian Dataset Latih dan Dataset Uji (Train-Test Split)

Prinsip paling sakral dalam evaluasi pembelajaran mesin adalah **pemisahan data latih dan data uji**. Kita membagi dataset mentah menjadi dua bagian independen:
- **Data Latih (*Training Set* - 80%):** Diberikan kepada algoritma untuk mempelajari pola hubungan antar-fitur dan label.
- **Data Uji (*Testing Set* - 20%):** Disimpan secara rahasia dan **sama sekali tidak boleh dilihat oleh algoritma selama proses pelatihan**. Data uji digunakan murni untuk menguji kemampuan generalisasi model terhadap data baru yang belum pernah dijumpai sebelumnya.

Pelanggaran terhadap prinsip ini disebut **Kebocoran Data (*Data Leakage*)**, yang mengakibatkan model tampak sangat pintar saat diuji di laboratorium (*Overfitting*), namun gagal total saat diterapkan di dunia nyata.

---

## C. EKSPLORASI ALGORITMA KLASIFIKASI: KNN DAN DECISION TREE

Ada dua algoritma klasifikasi terawasi paling fundamental yang wajib dikuasai calon praktisi AI:

### 1. K-Nearest Neighbors (KNN)

Algoritma KNN bekerja berdasarkan prinsip filosofis pepatah kuno: *"Tunjukkan siapa teman-teman terdekatmu, maka aku akan tahu siapa dirimu."* KNN tidak membangun rumus matematika rumit saat pelatihan, melainkan memprediksi label data baru berdasarkan mayoritas label dari sejumlah **k** tetangga terdekatnya.

Jarak geometris antara data baru dan data historis dihitung menggunakan rumus **Jarak Euclidean (*Euclidean Distance*)**:
`Jarak = Akar_Kuadrat( (x2 - x1)^2 + (y2 - y1)^2 + ... + (zn - z1)^2 )`

**Aturan Penentuan Nilai k:**
Gunakan selalu **bilangan ganjil** (misal k = 3, 5, atau 7) untuk menghindari terjadinya kondisi seri (*tie vote*) ketika model menentukan keputusan mayoritas antardua kelas.

### 2. Decision Tree (Pohon Keputusan)

Decision Tree bekerja memodelkan logika pengambilan keputusan menyerupai struktur pohon terbalik: dimulai dari simpul akar (*Root Node*), bercabang melalui pengujian kondisi (*Internal Nodes*), hingga berakhir pada daun kesimpulan (*Leaf Nodes*).

**Bagaimana Algoritma Memilih Fitur Pemisah Terbaik?**
Algoritma mengukur derajat ketidakmurnian (*impurity*) data. Parameter standar yang digunakan adalah **Gini Impurity**:
`Gini = 1 - Jumlah( p_i^2 )`
di mana `p_i` adalah probabilitas kemunculan kelas ke-i pada simpul tersebut. Simpul yang murni sempurna (seluruh anggotanya berasal dari kelas yang sama) memiliki nilai Gini = 0. Fitur yang menghasilkan penurunan nilai Gini paling drastis (*Information Gain* terbesar) akan dipilih sebagai simpul pemecah cabang.

---

## D. EVALUASI OBJEKTIF KINERJA MODEL: MATRIKS KONFUSI (CONFUSION MATRIX)

Bagaimana kita mengukur kinerja model secara adil, ilmiah, dan tidak tertipu oleh akurasi semu? Jawabannya adalah membedah prediksi model ke dalam **Matriks Konfusi (*Confusion Matrix*)**.

[GAMBAR: assets/bab4_diagram_matriks_konfusi_evaluasi.png]

### 1. Anatomi Tabel Kontingensi 2x2

Misalkan kita menguji model pendeteksi Penyakit Kanker (di mana Positif = Terkena Kanker, Negatif = Sehat):
- **True Positive (TP):** Pasien AKTUAL POSITIF, dan model MEMPREDIKSI POSITIF (Tepat & Menyelamatkan Nyawa).
- **True Negative (TN):** Pasien AKTUAL NEGATIF, dan model MEMPREDIKSI NEGATIF (Tepat & Membawa Ketenangan).
- **False Positive (FP / Galat Tipe I):** Pasien AKTUAL NEGATIF, namun model SALAH MEMPREDIKSI POSITIF (Alarm Palsu / Pasien panik namun bisa dikoreksi lewat tes lanjutan).
- **False Negative (FN / Galat Tipe II - SANGAT BERBAHAYA!):** Pasien AKTUAL POSITIF KANKER, namun model SALAH MEMPREDIKSI NEGATIF SEHAT (Pasien pulang tanpa pengobatan hingga penyakitnya terlambat ditangani).

### 2. Empat Pilar Metrik Evaluasi Matematis

1. **Akurasi (Accuracy):**
   `Akurasi = (TP + TN) / (TP + TN + FP + FN)`
   Hanya relevan digunakan jika jumlah kelas positif dan negatif di dalam dataset seimbang (*balanced*).
2. **Presisi (Precision):**
   `Presisi = TP / (TP + FP)`
   Mengukur seberapa akurat tebakan positif model. Sangat krusial pada kasus di mana biaya akibat False Positive sangat mahal (misal: sistem penyaring spam email atau prediksi kelayakan investasi saham).
3. **Recall (Sensitivitas / True Positive Rate):**
   `Recall = TP / (TP + FN)`
   Mengukur kemampuan model menangkap seluruh data yang sebenarnya positif. **Sangat krusial pada kasus di mana False Negative berakibat fatal** (misal: pendeteksi kanker, sistem peringatan dini tsunami, atau deteksi kebakaran pabrik).
4. **F1-Score:**
   `F1-Score = 2 * (Presisi * Recall) / (Presisi + Recall)`
   Rata-rata harmonik penyeimbang antara Presisi dan Recall. Nilai F1-Score yang tinggi menjamin model bekerja andal tanpa mengorbankan salah satu metrik.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 4.1

### Pelatihan dan Evaluasi Model Klasifikasi dengan Python Scikit-Learn

**Tujuan Pembelajaran:**
Peserta didik mampu memuat dataset tabular, membagi data latih dan data uji (80:20), melatih model klasifikasi K-Nearest Neighbors (KNN), mengekstrak matriks konfusi, serta menghitung nilai Akurasi, Presisi, Recall, dan F1-Score menggunakan pustaka Scikit-Learn.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terpasang.
2. Pustaka eksternal terinstal: `pip install scikit-learn pandas numpy`.
3. Editor Visual Studio Code atau Google Colab.

**Instruksi Kerja Praktikum:**
1. Buatlah berkas baru bernama `praktikum_ml_evaluasi.py`.
2. Ketikkan skrip implementasi alur kerja pipeline Machine Learning terpadu berikut:

```python
# Pipeline Machine Learning Terapan & Evaluasi Model
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def jalankan_eksperimen_ai():
    print("===== 1. PEMBUATAN DATASET SIMULASI MEDIS TIMPANG =====")
    # Membuat 1000 data sampel: 95% Sehat (0), 5% Pasien Kritis (1)
    X, y = make_classification(
        n_samples=1000, 
        n_features=5, 
        weights=[0.95, 0.05], 
        random_state=42
    )
    print(f"Total Sampel : {len(y)}")
    print(f"Kelas Sehat (0)  : {np.sum(y == 0)} pasien")
    print(f"Kelas Kritis (1) : {np.sum(y == 1)} pasien (Timpang)")

    # 2. Pembagian Dataset (Train-Test Split 80:20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 3. Penskalaan Fitur (Feature Scaling)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Pelatihan Model K-Nearest Neighbors (k=3)
    model_knn = KNeighborsClassifier(n_neighbors=3)
    model_knn.fit(X_train_scaled, y_train)

    # 5. Pengujian Prediksi pada Data Uji yang Dirahasiakan
    y_pred = model_knn.predict(X_test_scaled)

    # 6. Analisis Matriks Konfusi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    print("
===== 2. MATRIKS KONFUSI (CONFUSION MATRIX) =====")
    print(f"True Negative  (TN) : {tn} (Pasien sehat diprediksi tepat)")
    print(f"False Positive (FP) : {fp} (Alarm palsu)")
    print(f"False Negative (FN) : {fn} (Pasien kritis terlewat / FATAL!)")
    print(f"True Positive  (TP) : {tp} (Pasien kritis terdeteksi tepat)")

    # 7. Perhitungan Metrik Evaluasi Ilmiah
    akurasi = accuracy_score(y_test, y_pred)
    presisi = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (presisi * recall) / (presisi + recall) if (presisi + recall) > 0 else 0

    print("
===== 3. LAPORAN METRIK KINERJA MODEL =====")
    print(f"Akurasi Total : {akurasi * 100:.2f}%")
    print(f"Presisi Model : {presisi * 100:.2f}%")
    print(f"Recall Model  : {recall * 100:.2f}% (Sensitivitas Nyata)")
    print(f"F1-Score      : {f1 * 100:.2f}% (Keseimbangan)")
    print("=" * 45)

if __name__ == "__main__":
    jalankan_eksperimen_ai()
```

3. Jalankan program di terminal dan amatilah perbandingan antara nilai Akurasi Total dengan nilai Recall!
4. Modifikasilah parameter jumlah tetangga `n_neighbors` dari k = 3 menjadi k = 7 dan amati apakah nilai Recall mengalami perubahan!

**Pertanyaan Analisis Laboratorium:**
1. Mengapa fungsi penskalaan `scaler.fit_transform()` hanya diterapkan pada `X_train`, sedangkan untuk `X_test` kita hanya memanggil `scaler.transform()` tanpa pemanggilan fungsi `fit()`? Jelaskan hubungannya dengan bahaya *Data Leakage*!
2. Jika sebuah model AI pendeteksi spam email memiliki nilai Presisi 99% tetapi Recall-nya hanya 40%, apakah dampak yang dirasakan oleh pengguna kotak masuk email tersebut?
3. Uraikan mengapa pada kasus sistem pendeteksi kebocoran gas beracun di pabrik, para insinyur lebih memilih model yang memiliki nilai Recall 99% meskipun nilai Presisinya hanya 75%!

---

## F. RANGKUMAN MATERI BAB IV

1. **Taksonomi Pembelajaran Mesin:** Paradigma Machine Learning membiarkan komputer memelajari pola aturan dari data historis secara mandiri. Terbagi menjadi *Supervised Learning* (berbasis label: klasifikasi dan regresi), *Unsupervised Learning* (tanpa label: klastering), dan *Reinforcement Learning* (pembelajaran agen berbasis reward).
2. **Pipeline dan Pencegahan Data Leakage:** Siklus data mencakup penanganan nilai kosong, pengkodean kategori (Label / One-Hot Encoding), dan penskalaan rentang numerik (*StandardScaler*). Pembagian dataset menjadi data latih (80%) dan data uji rahasia (20%) mutlak diwajibkan untuk menguji generalisasi model bebas bias.
3. **Algoritma Klasifikasi Populer:** K-Nearest Neighbors (KNN) mengklasifikasikan data berdasarkan voting mayoritas k tetangga terdekat dengan jarak Euclidean. Decision Tree membagi simpul data berdasarkan penurunan nilai ketidakmurnian Gini (*Gini Impurity*).
4. **Evaluasi Matriks Konfusi (Confusion Matrix):** Tabel pemetaan True Positive, True Negative, False Positive, dan False Negative. Pada dataset timpang, nilai Akurasi semu sering kali menipu. Evaluasi sistem kritis mengutamakan nilai **Recall** (untuk meminimalkan bahaya fatal False Negative) dan **F1-Score** sebagai tolok ukur keandalan paripurna.

---

## G. UJI KOMPETENSI BAB IV

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Perbedaan mendasar antara paradigma pemrograman konvensional (*Rule-Based*) dan paradigma pembelajaran mesin (*Machine Learning*) adalah...
   A. Pemrograman konvensional tidak membutuhkan komputer
   B. Machine Learning memasukkan Data dan Jawaban ke dalam komputer untuk menghasilkan aturan pola (*Rules*), sedangkan pemrograman konvensional memasukkan Aturan dan Data untuk menghasilkan Jawaban
   C. Machine Learning hanya dapat dijalankan pada ponsel cerdas
   D. Pemrograman konvensional menghasilkan keluaran berupa gambar tiga dimensi

2. Cabang pembelajaran mesin yang melatih model menggunakan kumpulan data yang telah memiliki label jawaban yang benar dinamakan...
   A. Unsupervised Learning
   B. Reinforcement Learning
   C. Supervised Learning
   D. Heuristic Learning

3. Praktik rekayasa data yang memisahkan dataset mentah menjadi data latih (80%) dan data uji rahasia (20%) bertujuan utama untuk...
   A. Menghemat kapasitas penyimpanan harddisk komputer
   B. Menghindari kebocoran data (*Data Leakage*) dan menguji kemampuan generalisasi model terhadap data baru
   C. Mempercepat koneksi internet saat mengunggah kode
   D. Mengubah tipe data teks menjadi gambar vektor

4. Algoritma klasifikasi terawasi yang memprediksi label suatu data baru berdasarkan mayoritas label dari data terdekat di sekitarnya menggunakan rumus jarak Euclidean adalah...
   A. Decision Tree
   B. K-Nearest Neighbors (KNN)
   C. K-Means Clustering
   D. Linear Regression

5. Mengapa dalam menentukan nilai parameter tetangga k pada algoritma KNN sangat disarankan menggunakan bilangan ganjil (seperti k = 3, 5, atau 7)?
   A. Agar komputer tidak mengalami kehabisan memori
   B. Untuk menghindari terjadinya hasil imbang atau seri (*tie vote*) saat proses penentuan kelas mayoritas
   C. Karena bilangan genap tidak dapat dibagi oleh rumus jarak
   D. Agar model secara otomatis berubah menjadi pohon keputusan

6. Ukuran derajat ketidakmurnian data yang digunakan oleh algoritma Decision Tree untuk menentukan simpul pemecah cabang terbaik dinamakan...
   A. Euclidean Metric
   B. Gini Impurity
   C. Cosine Similarity
   D. Manhattan Distance

7. Dalam sebuah Matriks Konfusi pada sistem pendeteksi penyakit medis, kondisi di mana seorang pasien sebenarnya sehat normal namun sistem AI secara keliru memprediksinya sebagai pasien sakit (alarm palsu) dikategorikan sebagai...
   A. True Positive (TP)
   B. True Negative (TN)
   C. False Positive (FP)
   D. False Negative (FN)

8. Kondisi paling berbahaya pada sistem medis pendeteksi penyakit jantung, di mana pasien yang sebenarnya terkena serangan jantung fatal justru diprediksi sehat oleh sistem AI dan dipulangkan tanpa obat, merupakan manifestasi dari...
   A. False Negative (FN)
   B. False Positive (FP)
   C. True Positive (TP)
   D. True Negative (TN)

9. Metrik evaluasi kinerja model klasifikasi yang dihitung dengan membagi jumlah True Positive terhadap total data yang sebenarnya positif (TP / [TP + FN]) dinamakan...
   A. Akurasi
   B. Recall (Sensitivitas)
   C. Presisi
   D. Spesifisitas

10. Metrik evaluasi yang merupakan rata-rata harmonik penyeimbang antara nilai Presisi dan nilai Recall, sangat andal digunakan pada dataset dengan sebaran kelas yang timpang (*imbalanced dataset*), dinamakan...
    A. Mean Squared Error
    B. R-Squared
    C. F1-Score
    D. Z-Score

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan mengapa metrik Akurasi Total (*Accuracy*) dapat menjadi parameter evaluasi yang sangat menyesatkan (*misleading*) ketika diterapkan pada dataset yang memiliki ketimpangan kelas ekstrem (*imbalanced dataset*)! Berikan ilustrasi kasus nyatanya!
2. Uraikan tahapan alur kerja standar (*Machine Learning Pipeline*) mulai dari pengumpulan data mentah hingga model siap diterapkan ke lingkungan produksi (*deployment*)!
3. Diberikan matriks konfusi dari pengujian model pendeteksi transaksi penipuan kartu kredit (*Fraud Detection*) terhadap 1.000 transaksi uji:
   - True Positive (TP) = 40 transaksi penipuan terdeteksi tepat
   - False Positive (FP) = 10 transaksi sah salah dituduh penipuan
   - False Negative (FN) = 5 transaksi penipuan lolos tak terdeteksi
   - True Negative (TN) = 945 transaksi sah diprediksi tepat
   Hitunglah nilai Akurasi, Presisi, Recall, dan F1-Score dari model tersebut secara matematis!
4. Dalam perancangan sistem keselamatan mobil otonom yang bertugas mendeteksi pejalan kaki yang menyeberang jalan, analisislah mana yang membawa dampak risiko kemanusiaan lebih fatal antara *False Positive* atau *False Negative*! Jelaskan konsekuensi operasional dari masing-masing jenis galat tersebut!
5. Jelaskan perbedaan mendasar antara kondisi model yang mengalami *Overfitting* dan *Underfitting*! Bagaimana cara seorang pengembang AI mendeteksi dan mengatasi masalah overfitting saat melatih model Decision Tree?

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB IV

**Kunci Pilihan Ganda:**
1. **B** (Machine Learning memelajari aturan pola dari data dan jawaban historis secara otomatis).
2. **C** (Supervised Learning dilatih menggunakan data berlabel kunci jawaban).
3. **B** (Train-Test Split menguji generalisasi model dan mencegah kebocoran data / data leakage).
4. **B** (KNN mengklasifikasikan data berdasarkan voting tetangga terdekat dengan jarak Euclidean).
5. **B** (Nilai k ganjil mencegah terjadinya seri/tie vote pada klasifikasi biner).
6. **B** (Gini Impurity mengukur ketidakmurnian simpul pemisah pada Decision Tree).
7. **C** (False Positive adalah alarm palsu, aktual negatif namun diprediksi positif).
8. **A** (False Negative adalah kondisi paling berbahaya di mana kasus aktual positif gagal terdeteksi).
9. **B** (Recall mengukur rasio kasus aktual positif yang berhasil ditangkap sistem).
10. **C** (F1-Score adalah rata-rata harmonik penyeimbang antara Presisi dan Recall).

**Pembahasan Soal Uraian:**
1. *Kelemahan Akurasi pada Imbalanced Data:*
   Pada dataset yang timpang (misalnya 990 data transaksi normal dan 10 data penipuan perbankan), sebuah model bodoh yang memprediksi seluruh transaksi berstatus normal tanpa berpikir akan langsung memperoleh akurasi 990/1.000 = 99%. Namun model tersebut memiliki nilai Recall 0% karena gagal mendeteksi satupun penipuan kartu kredit. Akurasi tinggi memberikan rasa aman semu padahal sistem sama sekali tidak berguna secara operasional.
2. *Tahapan Machine Learning Pipeline:*
   (1) Pengumpulan dataset mentah; (2) Pembersihan data (imputasi nilai kosong missing values); (3) Rekayasa fitur (One-Hot Encoding untuk teks kategori, Penskalaan fitur StandardScaler); (4) Pemisahan data latih (80%) dan data uji (20%); (5) Pelatihan algoritma model pada data latih; (6) Evaluasi objektif performa model pada data uji menggunakan Confusion Matrix; (7) Penerapan model (Deployment) melalui antarmuka REST API.
3. *Perhitungan Evaluasi Fraud Detection:*
   - Total Sampel = TP + FP + FN + TN = 40 + 10 + 5 + 945 = 1.000.
   - Akurasi = (TP + TN) / Total = (40 + 945) / 1000 = 985 / 1000 = **98,5% (0,985)**.
   - Presisi = TP / (TP + FP) = 40 / (40 + 10) = 40 / 50 = **80,0% (0,800)**.
   - Recall = TP / (TP + FN) = 40 / (40 + 5) = 40 / 45 = **88,89% (0,889)**.
   - F1-Score = 2 * (Presisi * Recall) / (Presisi + Recall) = 2 * (0,80 * 0,8889) / (0,80 + 0,8889) = 1,4222 / 1,6889 = **84,21% (0,842)**.
4. *False Positive vs False Negative pada Mobil Otonom:*
   - False Positive: Sensor mengira ada pejalan kaki padahal jalanan kosong (misal bayangan daun). Konsekuensinya mobil melakukan pengereman mendadak yang mengagetkan penumpang, namun tidak merenggut korban jiwa.
   - False Negative: Ada pejalan kaki nyata yang menyeberang, namun sistem salah memprediksi bahwa jalanan kosong. Konsekuensinya mobil melaju kencang tanpa mengerem dan menabrak korban hingga tewas. Oleh karena itu, False Negative membawa risiko kemanusiaan yang mutlak jauh lebih fatal dan nilai Recall pendeteksian manusia wajib dioptimalkan mendekati 100%.
5. *Overfitting vs Underfitting:*
   - Underfitting terjadi saat model terlalu sederhana sehingga tidak mampu menangkap pola dasar data baik pada data latih maupun data uji (akurasi rendah di kedua dataset).
   - Overfitting terjadi saat model terlalu kompleks dan menghafal detail derau (*noise*) data latih. Ciri-cirinya: akurasi data latih sangat tinggi (~99%), namun saat diuji pada data uji performanya anjlok drastis (~60%).
   - Cara mengatasi overfitting pada Decision Tree: Menerapkan pemangkasan cabang (*Pruning*), membatasi kedalaman maksimum pohon keputusan (`max_depth`), serta menetapkan batas minimum sampel daun (`min_samples_leaf`).


# BAB V: FONDASI PEMROSESAN BAHASA ALAMI (NATURAL LANGUAGE PROCESSING - NLP)

## APERSEPSI: MENGAPA KOMPUTER KESULITAN MEMAHAMI SARKASME?

Di ruang laboratorium komputer sekolah, Bagas tampak sedang mengerutkan kening di depan layar laptopnya. Ia sedang menguji coba prototipe program analisis sentimen sederhana yang dirancangnya untuk memilah ulasan publik terhadap fasilitas kantin sekolah. Program tersebut bekerja dengan cara mencocokkan kata kunci: jika ada kata "enak" atau "hebat", program otomatis memberi label Positif.

[GAMBAR: assets/bab5_komik_pembuka_sma11.png]

"Dinda, Arya, lihat hasil analisis programku ini!" panggil Bagas seraya menunjuk salah satu baris ulasan di layar. "Seorang siswa menulis ulasan: *'Wah, hebat sekali ya kantin kita, nasi gorengnya dingin dan ada bonus semutnya!'*. Programku dengan bangga memberi label ulasan tersebut sebagai **Sentimen Positif Bintang Lima** hanya karena mendeteksi kata 'hebat'!"

Dinda tertawa kecil seraya menggelengkan kepala. "Tentu saja, Bagas. Program pencocokan kata kuncimu belum memahami konteks dan nuansa emosional bahasa manusia. Kalimat tersebut adalah sarkasme murni yang bermakna kekecewaan mendalam!"

Arya menambahkan, "Bahasa manusia (*Natural Language*) adalah sistem komunikasi paling kompleks di muka bumi. Bahasa sarat dengan metafora, peribahasa, imbuhan kata yang rumit, dan konteks antar-kata yang saling terkait erat. Komputer pada dasarnya adalah mesin hitung kalkulator yang hanya memahami angka biner 0 dan 1, bukan makna rasa di balik kata-kata."

"Lalu, bagaimana para ilmuwan kecerdasan artifisial modern membuat model bahasa besar (*Large Language Models*) seperti ChatGPT atau Gemini mampu diajak berdiskusi secara luwes layaknya manusia?" tanya Bagas penasaran.

Dinda membuka buku catatannya. "Kuncinya ada pada bidang ilmu **Pemrosesan Bahasa Alami (*Natural Language Processing* / NLP)**. Teks mentah manusia harus melalui serangkaian penyaringan pra-pemrosesan: memotong kalimat menjadi kata (*Tokenizing*), membuang kata sambung tak bermakna (*Stopwords*), mencari kata dasar (*Stemming*), lalu mengubah kata menjadi vektor angka bobot informasi (**TF-IDF**). Dan puncaknya, kita akan membedah rahasia arsitektur **Transformer** dengan mekanisme perhatian (*Self-Attention*) yang merevolusi dunia AI modern!"

"Luar biasa!" seru Bagas. "Mari kita pelajari sains komputasi bahasa manusia ini!"

---

## A. KOMPLEKSITAS BAHASA MANUSIA DAN KOMPUTASI LINGUISTIK DIGITAL

Bahasa manusia (*Natural Language*) berkembang secara organik selama ribuan tahun melalui interaksi sosial, budaya, dan emosi. Berbeda dengan bahasa pemrograman komputer (seperti Python atau SQL) yang memiliki aturan tata bahasa yang kaku, deterministik, dan bebas dari ambiguitas, bahasa manusia memiliki karakteristik yang sangat menantang bagi mesin komputasi:

1. **Ambiguitas Semantik (Makna Ganda):**
Sebuah kata yang sama dapat memiliki arti yang sangat berbeda tergantung pada konteks kalimatnya.
*Contoh:* Kata "bisa" dapat bermakna "mampu" (*can*), namun juga dapat bermakna "racun ular" (*venom*). Komputer harus mampu membedakan makna tersebut berdasarkan kata-kata di sekelilingnya.
2. **Kekayaan Imbuhan Bahasa Indonesia (Morfologi Kompleks):**
Bahasa Indonesia memiliki sistem afiksasi (awalan, akhiran, sisipan, dan gabungan) yang sangat kaya. Satu kata dasar "ajar" dapat bertransformasi menjadi *belajar, mengajar, pengajar, pelajaran, terpelajar, diajarkan, mempelajarinya*. Mesin harus mampu mengenali bahwa seluruh kata turunan tersebut memiliki akar makna yang sekeluarga.
3. **Nuansa Emosi, Sarkasme, dan Majas:**
Kalimat manusia sering kali memuat makna tersirat yang berlawanan dengan makna harfiah kata penyusunnya. Ulasan *"Pelayanannya cepat sekali, cuma butuh waktu 3 jam untuk menyajikan segelas air"* menuntut pemahaman ironi yang melampaui perhitungan frekuensi kata biasa.
4. **Bahasa Gaul (Slang), Singkatan, dan Dialek Daerah:**
Di media sosial Indonesia, masyarakat sering menggunakan singkatan informal (misal: *bgt, gpp, mager, kepo*) serta mencampuradukkan bahasa Indonesia dengan kosa kata daerah nusantara.

---

## B. ALUR PRA-PEMROSESAN TEKS (TEXT PREPROCESSING PIPELINE)

Agar teks mentah bahasa manusia dapat diproses oleh algoritma pembelajaran mesin, teks tersebut wajib dibersihkan melalui pipa saluran pra-pemrosesan (*Text Preprocessing Pipeline*) yang terstandarisasi.

[GAMBAR: assets/bab5_diagram_pipeline_nlp_text_processing.png]

Berikut adalah empat tahapan fundamental dalam rekayasa teks digital:

### 1. Case Folding (Penyeragaman Huruf)

Langkah awal untuk menyeragamkan seluruh karakter abjad menjadi huruf kecil (*lowercase*), serta menghapus tanda baca, angka yang tidak relevan, tautan URL, dan karakter khusus.
*Tujuan:* Komputer memperlakukan kata "Koding", "koding", dan "KODING" sebagai satu kata yang identik, bukan tiga entitas yang berbeda.
*Contoh:* `"Siswa-siswa SANGAT Menyukai Koding!"` -> `"siswa-siswa sangat menyukai koding"`

### 2. Tokenizing (Pemotongan Token Kata)

Proses memotong dan memecah untaian teks kalimat panjang menjadi elemen-elemen kata individual yang disebut **Token**.
*Contoh:* `"siswa sangat menyukai koding"` -> `['siswa', 'sangat', 'menyukai', 'koding']`

### 3. Stopwords Removal (Penyaringan Kata Sambung Umum)

Membuang kata-kata fungsional umum yang memiliki frekuensi kemunculan sangat tinggi dalam bahasa sehari-hari namun **tidak membawa bobot informasi unik** terkait topik atau sentimen teks (seperti kata depan dan kata hubung: *dan, di, ke, dari, yang, untuk, pada, ini, itu*).
*Tujuan:* Mengurangi dimensi komputasi secara masif dan memfokuskan model AI hanya pada kata-kata yang bermakna esensial.
*Contoh:* `['buku', 'ini', 'sangat', 'bagus', 'dan', 'menarik']` -> `['buku', 'bagus', 'menarik']` (kata *ini, sangat, dan* dibuang).

### 4. Stemming Bahasa Indonesia (Pencarian Kata Dasar)

Proses morfologis untuk memotong seluruh imbuhan (prefiks, sufiks, konfiks) dari suatu kata berimbuhan guna mengembalikannya ke bentuk **Kata Dasar (*Root Word*)**.
Dalam ekosistem Python di Indonesia, proses ini dieksekusi menggunakan pustaka sumber terbuka populer bernama **Sastrawi** yang mengadopsi algoritma morfologi Nazief-Adriani:
*Contoh:*
- *"mempelajari"* -> `"ajar"`
- *"pengembangan"* -> `"kembang"`
- *"diterapkannya"* -> `"terap"`

---

## C. VEKTORISASI TEKS: MENGUBAH KATA MENJADI ANGKA

Setelah teks dibersihkan menjadi daftar kata dasar, komputer tetap belum dapat memprosesnya karena algoritma Machine Learning hanya mampu melakukan operasi aljabar pada angka numerik. Tahap berikutnya adalah **Vektorisasi Teks (*Text Vectorization*)**.

### 1. Pendekatan Kantung Kata (Bag of Words / BoW)

Metode BoW menyusun sebuah kamus kosakata (*vocabulary*) dari seluruh kata unik yang muncul di seluruh dokumen, lalu memetakan setiap kalimat menjadi vektor frekuensi kemunculan kata.
*Kelemahan BoW:* Mengabaikan urutan tata bahasa dan memberikan nilai bobot yang sama tingginya pada kata-kata umum yang sering berulang di semua dokumen, padahal kata tersebut kurang informatif.

### 2. Algoritma Pembobotan TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF adalah standar emas dalam sains penelusuran informasi (*Information Retrieval*) dan NLP klasik. Algoritma ini memberikan bobot nilai tinggi pada kata yang **sering muncul di dokumen tertentu**, namun **jarang muncul di dokumen-dokumen lainnya** (menandakan kata tersebut adalah kata kunci unik pembeda topik).

Rumus Matematis TF-IDF:
1. **Term Frequency (TF):** Frekuensi kemunculan kata $t$ di dalam dokumen spesifik $d$.
   `TF(t, d) = Jumlah kemunculan kata t dalam dokumen d / Total kata dalam dokumen d`
2. **Inverse Document Frequency (IDF):** Ukuran seberapa langka kata $t$ di seluruh koleksi total $N$ dokumen.
   `IDF(t) = log( Total seluruh dokumen N / Jumlah dokumen yang memuat kata t )`
3. **Bobot Akhir TF-IDF:**
   `TF-IDF(t, d) = TF(t, d) * IDF(t)`

Jika sebuah kata (misal: "sekolah") muncul di hampir setiap dokumen, nilai IDF-nya akan mendekati nol, sehingga bobot akhirnya menjadi sangat rendah. Sebaliknya, kata langka dan spesifik (misal: "konvolusi" atau "algoritma") akan memperoleh bobot nilai yang sangat tinggi.

---

## D. PENGANTAR ARSITEKTUR TRANSFORMER DAN MEKANISME PERHATIAN (SELF-ATTENTION)

Dalam sejarah pembelajaran mendalam untuk teks, model generasi lama seperti Recurrent Neural Networks (RNN) dan LSTM memiliki keterbatasan fatal: model membaca kata satu demi satu secara sekuensial dari kiri ke kanan. Ketika memproses paragraf yang sangat panjang, model RNN menderita fenomena "lupa ingatan" (*catastrophic forgetting*) di mana konteks kata di awal paragraf telah pudar saat model mencapai akhir paragraf.

### 1. Terobosan Bersejarah: "Attention Is All You Need" (2017)

Pada tahun 2017, tim peneliti Google mempublikasikan makalah ilmiah legendaris berjudul *"Attention Is All You Need"*. Makalah ini memperkenalkan arsitektur baru bernama **Transformer**, yang membuang mekanisme perulangan sekuensial dan menggantinya dengan pemrosesan paralel penuh yang ditenagai oleh **Mekanisme Perhatian Diri Sendiri (*Self-Attention Mechanism*)**.

### 2. Cara Kerja Mekanisme Self-Attention

Mekanisme Attention memungkinkan model komputasi untuk menimbang dan menghitung derajat keterkaitan semantik antara setiap kata dengan seluruh kata lainnya dalam kalimat secara simultan.

Perhatikan kalimat kompleks berikut:
*"Kucing itu tidak mau menyeberang jalan raya karena **ia** terlalu lelah."*
Bagi manusia, akal budi kita langsung memahami bahwa kata ganti **"ia"** merujuk pada **kucing**, bukan pada jalan raya.
Bagi komputer konvensional, penentuan rujukan ini sangat membingungkan. Namun dengan mekanisme Self-Attention, model Transformer menghitung matriks probabilitas hubungan bobot kata. Model memberikan skor perhatian (*attention score*) yang sangat tinggi antara token kata `"ia"` dan kata `"kucing"`, sehingga makna semantik utuh kalimat dapat dipahami secara akurat tanpa distorsi.

Arsitektur Transformer inilah yang menjadi fondasi tunggal yang menggerakkan seluruh revolusi model bahasa cerdas dunia (*Generative Pre-trained Transformer* / GPT, Gemini, LLaMA, dan Claude).

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 5.1

### Membangun Model Analisis Sentimen Ulasan Berbasis Teks Menggunakan Python

**Tujuan Pembelajaran:**
Peserta didik mampu menerapkan tahapan pra-pemrosesan teks sederhana, mentransformasikan ulasan kalimat menjadi representasi numerik menggunakan pembobotan TF-IDF, serta melatih model klasifikasi Naive Bayes / Decision Tree untuk memprediksi sentimen ulasan positif dan negatif secara otomatis.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terpasang.
2. Pustaka Scikit-Learn terinstal (`pip install scikit-learn`).

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `praktikum_sentimen_nlp.py`.
2. Ketikkan dan pelajari kode implementasi analisis sentimen teks berikut:

```python
# Klasifikasi Analisis Sentimen Ulasan dengan TF-IDF & Naive Bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def jalankan_analisis_sentimen():
    print("===== 1. MENYIAPKAN DATASET TEKS PELATIHAN =====")
    # Sampel dataset opini ulasan kantin sekolah
    data_ulasan = [
        "Makanan kantin hari ini sangat enak lezat dan bersih sekali",
        "Pelayanan ramah tempat duduk nyaman makanannya sedap",
        "Menu ayam bakar gurih sekali porsinya mengenyangkan puas",
        "Rasa makanan nikmat higienis dan harga sangat terjangkau",
        "Makanannya dingin hambar tidak enak pelayanannya lambat",
        "Sangat kecewa porsi sedikit harga mahal dan tempat kotor",
        "Jus buahnya basi berbau masam bikin sakit perut parah",
        "Pelayan kantin judes tidak sopan makanan dingin mengecewakan"
    ]
    # Label: 1 = Positif, 0 = Negatif
    label_sentimen = [1, 1, 1, 1, 0, 0, 0, 0]

    # 2. Membangun Pipeline NLP: TfidfVectorizer + Klasifier Naive Bayes
    # Pipeline mengotomasi proses vektorisasi dan inferensi model
    model_nlp = make_pipeline(
        TfidfVectorizer(lowercase=True, stop_words=None),
        MultinomialNB()
    )

    # 3. Melatih Model
    model_nlp.fit(data_ulasan, label_sentimen)
    print("[SUKSES] Model NLP berhasil dilatih menggunakan vektor TF-IDF!")

    # 4. Pengujian dengan Kalimat Opini Baru yang Belum Pernah Dilihat
    kalimat_uji = [
        "Tempatnya sangat bersih dan ayam gorengnya lezat mantap",
        "Kecewa sekali makanannya dingin dan sangat mahal",
        "Pelayanannya ramah makanannya sangat memuaskan",
        "Harganya mahal rasanya hambar bikin kapok"
    ]

    print("
===== 2. PENGUJIAN PREDIKSI SENTIMEN REAL-TIME =====")
    prediksi = model_nlp.predict(kalimat_uji)
    probabilitas = model_nlp.predict_proba(kalimat_uji)

    for i, teks in enumerate(kalimat_uji):
        kategori = "POSITIF (+)" if prediksi[i] == 1 else "NEGATIF (-)"
        skor_keyakinan = probabilitas[i][prediksi[i]] * 100
        print(f"Kalimat : "{teks}"")
        print(f"Hasil   : {kategori} (Tingkat Keyakinan: {skor_keyakinan:.2f}%)")
        print("-" * 65)

if __name__ == "__main__":
    jalankan_analisis_sentimen()
```

3. Eksekusi program di terminal dan amatilah bagaimana model mampu mengenali sentimen positif dan negatif pada kalimat-kalimat baru secara akurat!
4. Masukkan kalimat uji coba kalian sendiri yang memuat kata-kata unik, lalu amati tingkat keyakinan probabilitas yang dihasilkan oleh model!

**Pertanyaan Analisis Laboratorium:**
1. Mengapa teknik pembobotan TF-IDF jauh lebih akurat digunakan pada pengolahan teks dibandingkan hanya menghitung panjang karakter kalimat?
2. Apa yang terjadi jika sebuah model NLP yang dilatih menggunakan bahasa Indonesia baku diuji dengan kalimat yang dipenuhi bahasa gaul singkatan (*slang*)? Langkah pra-pemrosesan tambahan apa yang wajib ditambahkan pada pipeline?
3. Uraikan mengapa pemahaman konteks antar-kata melalui mekanisme perhatian (*Attention*) menjadi kunci utama yang membedakan model bahasa modern (LLM) dari sistem klasifikasi teks berbasis kata kunci sederhana!

---

## F. RANGKUMAN MATERI BAB V

1. **Kompleksitas Komputasi Bahasa:** Bahasa alami manusia sarat dengan ambiguitas semantik, afiksasi morfologis bertingkat, nuansa emosi sarkasme, dan dialek sosial yang menuntut pemrosesan komputasi melampaui pencocokan kata kunci linier.
2. **Tahapan Pra-Pemrosesan Teks:** Rangkaian pembersihan data teks yang mencakup *Case Folding* (penyeragaman huruf kecil), *Tokenizing* (pemotongan kata), *Stopwords Removal* (pembuangan kata sambung umum), dan *Stemming* (reduksi imbuhan ke bentuk kata dasar menggunakan algoritma Nazief-Adriani / Sastrawi).
3. **Vektorisasi TF-IDF:** Mentransformasikan kata menjadi bobot numerik berdasarkan frekuensi kemunculan kata dalam dokumen lokal (*Term Frequency*) dikalikan kelangkaan kata tersebut di seluruh koleksi dokumen (*Inverse Document Frequency*), menonjolkan kata kunci informatif.
4. **Revolusi Arsitektur Transformer:** Membuang keterbatasan model sekuensial lama (RNN/LSTM) dan menggantinya dengan mekanisme *Self-Attention* paralel yang menghitung bobot keterkaitan antarkata dalam kalimat secara komprehensif, menjadi landasan teknologi di balik lahirnya model bahasa besar dunia (LLM).

---

## G. UJI KOMPETENSI BAB V

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Cabang ilmu kecerdasan artifisial yang berfokus pada kemampuan komputer untuk memahami, menginterpretasikan, memanipulasi, dan menghasilkan bahasa alami manusia dinamakan...
   A. Computer Vision
   B. Natural Language Processing (NLP)
   C. Internet of Things
   D. Cryptographic Hashing

2. Tahapan pra-pemrosesan teks yang bertujuan menyeragamkan seluruh karakter abjad di dalam dokumen menjadi huruf kecil (*lowercase*) untuk menghindari duplikasi kata disebut...
   A. Tokenizing
   B. Case Folding
   C. Stemming
   D. Lemmatization

3. Proses memecah satu paragraf atau kalimat panjang menjadi potongan-potongan kata individual yang berdiri sendiri di dalam struktur daftar dinamakan...
   A. Tokenizing
   B. Normalisasi
   C. Penskalaan Fitur
   D. Serialisasi

4. Kata-kata umum seperti "dan", "di", "ke", "dari", "yang", dan "adalah" yang sering dibuang dalam pemrosesan teks karena tidak membawa bobot informasi unik dikenal dengan istilah...
   A. Rare words
   B. Stopwords
   C. Keywords
   D. Root words

5. Proses morfologis dalam bahasa Indonesia untuk menghilangkan seluruh imbuhan (awalan, sisipan, dan akhiran) guna mengembalikan kata ke bentuk aslinya dinamakan...
   A. Stemming
   B. Tokenizing
   C. Vectorizing
   D. Parsing

6. Algoritma pembobotan teks yang memberikan skor tinggi pada kata yang sering muncul dalam dokumen tertentu tetapi jarang muncul di seluruh dokumen lain dalam suatu korpus koleksi adalah...
   A. One-Hot Encoding
   B. Bag of Words
   C. TF-IDF (Term Frequency - Inverse Document Frequency)
   D. Label Encoder

7. Apabila sebuah kata muncul di hampir seluruh dokumen di dalam pangkalan data perpustakaan digital, maka nilai *Inverse Document Frequency* (IDF) dari kata tersebut akan...
   A. Mendekati angka tak hingga
   B. Bernilai negatif
   C. Mendekati angka nol sehingga bobot informasinya menjadi sangat rendah
   D. Berubah menjadi karakter gambar

8. Makalah ilmiah legendaris terbitan Google Research pada tahun 2017 yang memperkenalkan arsitektur Transformer dan mekanisme perhatian (*Attention Mechanism*) berjudul...
   A. Deep Learning in Practice
   B. Attention Is All You Need
   C. The Master Algorithm
   D. Computer Machinery and Intelligence

9. Komponen utama dalam arsitektur Transformer yang memungkinkan model menimbang derajat keterkaitan semantik antara suatu kata ganti (misal kata "ia") dengan subjek aslinya di dalam kalimat panjang secara simultan adalah...
   A. Convolutional Kernel
   B. Self-Attention Mechanism
   C. Pooling Layer
   D. Sigmoid Activation

10. Mengapa model klasifikasi teks berbasis kamus kata kunci sederhana (*keyword matching*) sering kali salah dalam menganalisis kalimat yang memuat majas sarkasme atau sindiran halus?
    A. Karena kamus kata kunci mengonsumsi daya listrik terlalu besar
    B. Karena kamus kata kunci hanya mencocokkan kata positif secara harfiah tanpa mempertimbangkan konteks relasi antarkata di sekelilingnya
    C. Karena kata sarkasme selalu ditulis menggunakan bahasa asing
    D. Karena model kamus tidak dapat membaca huruf vokal

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan mengapa bahasa alami manusia (*Natural Language*) jauh lebih sulit dipahami oleh sistem komputasi dibandingkan bahasa pemrograman komputer formal (seperti Python atau SQL)! Uraikan minimal tiga faktor penyebabnya!
2. Diberikan kalimat mentah dari sebuah ulasan media sosial:
   `"Siswa-siswa SANGAT MENGAPRESIASI pembelajaran koding di sekolah ini!"`
   Tuliskan perubahan bentuk kalimat tersebut secara bertahap melalui empat fase pra-pemrosesan teks: Case Folding, Tokenizing, Stopwords Removal, dan Stemming Bahasa Indonesia!
3. Jelaskan prinsip kerja matematis dari pembobotan TF-IDF! Mengapa kata "komputasi" pada artikel jurnal sains komputer akan memperoleh bobot TF-IDF yang jauh lebih tinggi daripada kata "adalah"?
4. Uraikan keterbatasan mendasar dari arsitektur model sekuensial lama seperti Recurrent Neural Networks (RNN) saat memproses teks panjang, dan jelaskan bagaimana arsitektur Transformer menyelesaikan kelemahan tersebut melalui mekanisme pemrosesan paralel dan *Self-Attention*!
5. Rancanglah sebuah alur kerja sistem deteksi ujaran kebencian (*Hate Speech Detection*) otomatis untuk mengawal kolom komentar portal berita daring sekolah! Sebutkan tahapan pipeline yang harus dilalui serta pertimbangan etika dalam membedakan antara kritik konstruktif dan ujaran kebencian!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB V

**Kunci Pilihan Ganda:**
1. **B** (NLP berfokus pada komputasi pemrosesan bahasa manusia).
2. **B** (Case Folding menyeragamkan seluruh karakter abjad menjadi huruf kecil).
3. **A** (Tokenizing memecah kalimat menjadi token kata individual).
4. **B** (Stopwords adalah kata fungsional umum yang disaring dan dibuang).
5. **A** (Stemming memotong imbuhan untuk mengembalikan kata ke bentuk dasar).
6. **C** (TF-IDF menimbang frekuensi kemunculan terhadap kelangkaan dokumen).
7. **C** (Kata pasaran yang muncul di semua dokumen memiliki IDF mendekati nol).
8. **B** ("Attention Is All You Need" adalah judul makalah revolusioner Vaswani et al., 2017).
9. **B** (Self-Attention mechanism menghitung bobot keterkaitan semantik antarkata).
10. **B** (Keyword matching gagal menangkap sarkasme karena mengabaikan konteks semantik kalimat).

**Pembahasan Soal Uraian:**
1. *Tantangan Komputasi Bahasa Manusia:*
   - Ambiguitas Kontekstual: Satu kata memiliki banyak arti yang bergantung pada kata sekitarnya (polisemi).
   - Morfologi Fleksibel: Sistem imbuhan yang kompleks (afiksasi) mengubah struktur dan fungsi gramatikal kata secara dinamis.
   - Bahasa Kiasan & Sarkasme: Makna sesungguhnya sering kali bertolak belakang dengan makna harfiah kata penyusunnya. Sebaliknya, bahasa pemrograman dirancang formal, memiliki tata bahasa kaku (*context-free grammar*), dan bebas dari ambiguitas tafsir.
2. *Tahapan Preprocessing Kalimat:*
   - Kalimat Asli: `"Siswa-siswa SANGAT MENGAPRESIASI pembelajaran koding di sekolah ini!"`
   - Case Folding: `"siswa-siswa sangat mengapresiasi pembelajaran koding di sekolah ini"` (huruf kecil dan tanda seru dibuang).
   - Tokenizing: `['siswa-siswa', 'sangat', 'mengapresiasi', 'pembelajaran', 'koding', 'di', 'sekolah', 'ini']`.
   - Stopwords Removal: `['siswa-siswa', 'mengapresiasi', 'pembelajaran', 'koding', 'sekolah']` (kata *sangat, di, ini* dibuang).
   - Stemming: `['siswa', 'apresiasi', 'ajar', 'koding', 'sekolah']` (kata dikembalikan ke akar kata dasar).
3. *Prinsip Matematis TF-IDF:*
   - TF mengukur frekuensi kemunculan lokal: seberapa sering kata tersebut muncul dalam satu artikel spesifik.
   - IDF mengukur kelangkaan global: logaritma dari total dokumen dibagi jumlah dokumen yang memuat kata tersebut.
   - Kata "adalah" muncul di hampir 100% dokumen, sehingga nilai N/DF mendekati 1 dan log(1) = 0. Akibatnya bobot TF-IDF kata "adalah" menjadi 0 (tidak berharga). Sebaliknya kata "komputasi" hanya muncul di beberapa dokumen khusus, sehingga nilai IDF-nya tinggi dan bobot akhirnya sangat besar, menjadikannya pembeda topik yang kuat.
4. *Kelemahan RNN vs Terobosan Transformer:*
   - RNN membaca kata secara sekuensial satu per satu dari kiri ke kanan. Informasi kata awal dialirkan melalui status tersembunyi (*hidden state*) yang semakin lama semakin memudar (*vanishing gradient*), sehingga model melupakan konteks awal pada kalimat panjang. Selain itu, proses sekuensial tidak dapat diparalelkan di kartu grafis (GPU).
   - Transformer memproses seluruh kata dalam kalimat secara paralel sekaligus. Mekanisme Self-Attention menghitung matriks korelasi langsung antara setiap pasangan kata tanpa peduli seberapa jauh jarak posisinya di dalam teks, melipatgandakan kecepatan pelatihan dan mempertahankan pemahaman konteks panjang secara sempurna.
5. *Alur Deteksi Ujaran Kebencian & Etika:*
   - Pipeline: Pengumpulan data komentar -> Pra-pemrosesan teks (Pembersihan slang & normalisasi singkatan) -> Vektorisasi TF-IDF / Word Embedding -> Model Klasifikasi berbasis probabilitas -> Penandaan otomatis.
   - Pertimbangan Etika: Sistem harus dilatih secara cermat agar mampu membedakan antara ekspresi kritik konstruktif (misal: *"Kebijakan ini kurang tepat dan perlu diperbaiki sistemnya"*) dengan ujaran kebencian yang menyerang martabat SARA individu. Komentar yang terdeteksi tidak boleh langsung dihapus permanen oleh AI (*No Black Box tyranny*), melainkan dialirkan ke moderator manusia (*Human-in-the-Loop*) untuk menjamin kebebasan berpendapat yang sehat.


# BAB VI: DAMPAK SOSIO-TEKNOLOGI AI, KETENAGAKERJAAN, DAN ETIKA PENGEMBANG

## APERSEPSI: APAKAH KECERDASAN ARTIFISIAL AKAN MENGGANTIKAN KITA?

Di teras laboratorium komputer saat senja mulai temaram, Arya, Dinda, dan Bagas sedang duduk melingkar sambil menikmati secangkir teh hangat setelah menuntaskan rangkaian proyek koding mereka selama satu tahun penuh di Fase F. Di hadapan mereka, tablet pintar menampilkan tajuk berita utama sebuah surat kabar nasional: *"Otomasi Industri dan Gelombang Kecerdasan Artifisial: Ancaman Pengangguran Massal ataukah Fajar Baru Peradaban Kerja Manusia?"*.

[GAMBAR: assets/bab6_komik_pembuka_sma11.png]

"Membaca berita ini membuatku sedikit cemas," ujar Bagas dengan nada pelan. "Sebagai siswa SMK jurusan teknik, aku melihat banyak pekerjaan perakitan kabel, penginputan data inventaris, bahkan pemilahan barang di gudang logistik kini mulai digantikan oleh lengan robot cerdas dan algoritma Computer Vision. Apakah di masa depan keahlian kita sebagai manusia akan menjadi usang dan tidak dibutuhkan lagi di dunia kerja?"

Arya menatap layar laptopnya lalu menoleh ke arah Bagas. "Sejarah membuktikan bahwa setiap kali revolusi teknologi meletus—mulai dari penemuan mesin uap pada abad ke-18 hingga kehadiran komputer pribadi pada abad ke-20—pekerjaan yang sifatnya repetitif, mekanis, dan dapat diprediksi memang akan terdisrupsi secara drastis. Namun di saat yang sama, revolusi tersebut selalu melahirkan jutaan jenis profesi baru dengan nilai ekonomi yang jauh lebih tinggi!"

Dinda tersenyum bijak seraya menyandarkan tabletnya. "Tepat sekali, kawan. Kunci utamanya terletak pada cara pandang kita terhadap kecerdasan artifisial. AI bukanlah pengganti manusia (*Replacement*), melainkan penguat kecerdasan manusia (**Augmented Intelligence**)! Perangkat AI dirancang untuk membebaskan manusia dari beban rutinitas yang menjemukan, sehingga manusia dapat berfokus pada hal-hal yang menjadi esensi kemanusiaan: kreativitas imajinatif, kepemimpinan berempati, kepekaan etika moral, dan pemecahan masalah kritis."

"Dan tugas terberat kita sebagai generasi pengembang muda," lanjut Dinda dengan tatapan mantap, "adalah memastikan bahwa teknologi AI dikembangkan dengan berlandaskan filosofi **Human-Centered AI**—kecerdasan buatan yang berpusat pada manusia, transparan, adil tanpa bias diskriminatif, dan setia mengabdi demi kemaslahatan seluruh rakyat Indonesia!"

"Benar sekali!" seru Arya dan Bagas kompak. "Mari kita pelajari tata kelola sosio-teknologi, transparansi algoritma Explainable AI, dan mempertegas komitmen etika kita sebagai perekayasa masa depan bangsa!"

---

## A. DISRUPSI KETENAGAKERJAAN DAN KONSEP AUGMENTED INTELLIGENCE

Laju transformasi kecerdasan artifisial yang eksponensial telah mengubah peta ketenagakerjaan global dan struktur ekonomi peradaban modern.

### 1. Spektrum Disrupsi: Pekerjaan Repetitif vs Pekerjaan Bernalar Tinggi

Berdasarkan laporan kajian ekonomi ketenagakerjaan dunia (World Economic Forum), dampak otomasi cerdas membelah jenis profesi menjadi dua kategori:
- **Profesi yang Terdisrupsi Tinggi (*High Vulnerability*):** Pekerjaan yang melibatkan tugas-tugas administratif rutin, pemrosesan data manual berulang, pencatatan pembukuan sederhana, dan pekerjaan fisik mekanis di lingkungan terprediksi.
- **Profesi yang Berkembang Pesat (*High Growth*):** Profesi yang menuntut integrasi keterampilan tingkat tinggi (*High-Order Skills*):
  1. *Kecakapan Rekayasa Sistem:* Insinyur pembelajaran mesin, arsitek data terintegrasi, perekayasa keamanan siber (*Cybersecurity Specialist*), dan perawat sistem IoT.
  2. *Kecerdasan Emosional & Empati:* Konselor psikologi, perawat medis holistik, pendidik adaptif, dan mediator sosial.
  3. *Kreativitas Strategis:* Desainer antarmuka pengalaman pengguna (UI/UX), perancang inovasi sosial, dan analis kebijakan etika teknologi.

### 2. Dari Penggantian (*Replacement*) Menuju Penguatan (*Augmented Intelligence*)

Paradigma usang memandang AI sebagai ancaman yang menyingkirkan manusia dari tempat kerja. Sebaliknya, paradigma modern mempromosikan **Augmented Intelligence (Kecerdasan yang Dikuatkan)**: kemitraan sinergis antara akal budi manusia dan daya komputasi mesin.

**Formula Kolaborasi Manusia + Kecerdasan Artifisial:**
- **Peran Kecerdasan Artifisial:** Memproses mahadata (*Big Data*) jutaan baris dalam hitungan detik, mendeteksi korelasi pola statistik tersembunyi, melakukan perhitungan matematika matriks tanpa lelah, dan mengotomasi kalkulasi teknis 24 jam sehari.
- **Peran Manusia (Insinyur & Pengguna):** Memberikan arah visi strategis, merumuskan masalah berakar empati (*Design Thinking*), menyaring pertimbangan etika moral, memvalidasi kebenaran faktual (*fact-checking*), dan mengambil keputusan akhir yang bertanggung jawab secara hukum.

---

## B. STANDAR ETIKA SISTEM CERDAS BERPUSAT MANUSIA (HUMAN-CENTERED AI)

Teknologi cerdas tidak pernah bebas nilai. Algoritma pembelajaran mesin belajar dari data masa lalu yang dikumpulkan dari masyarakat, di mana data tersebut mungkin memuat prasangka rasial, ketimpangan gender, atau stereotip sosial. Jika tidak diaudit secara ketat, AI akan mengamplifikasi ketidakadilan sosial tersebut secara otomatis dalam skala raksasa.

Mengacu pada rekomendasi resmi badan dunia **UNESCO (2021)** dan standar etika rekayasa **IEEE**, terdapat empat pilar etika **Human-Centered AI**:

1. **Keadilan dan Non-Diskriminasi (*Fairness & Equity*):**
Sistem AI wajib memperlakukan seluruh individu dan kelompok masyarakat secara adil dan setara. Algoritma seleksi beasiswa atau perekrutan tenaga kerja dilarang keras mendiskriminasi pelamar berdasarkan latar belakang suku, agama, ras, gender, atau disabilitas fisik.
2. **Keberlanjutan Lingkungan (*Environmental Sustainability*):**
Pelatihan model kecerdasan artifisial raksasa mengonsumsi energi listrik dan air pendingin peladen yang sangat besar (*Carbon Footprint*). Pengembang bertanggung jawab merancang algoritma yang hemat energi (*Green AI*) dan memanfaatkan teknologi cerdas untuk pelestarian alam serta efisiensi energi terbarukan.
3. **Akuntabilitas dan Tanggung Jawab Hukum (*Accountability*):**
AI adalah alat buatan, bukan subjek hukum yang berkesadaran. Jika sebuah sistem mobil otonom menabrak pejalan kaki atau sebuah model medis salah mendiagnosis penyakit, tanggung jawab hukum dan moral tidak dapat dilimpahkan kepada algoritma, melainkan melekat secara mutlak pada perusahaan pengembang, insinyur perancang, dan operator sistem manusia.
4. **Privasi dan Kedaulatan Data (*Data Governance*):**
Menghormati kerahasiaan informasi warga negara sejalan dengan Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022). Pengguna memiliki kedaulatan mutlak untuk mengetahui data apa yang dikumpulkan, bagaimana data tersebut diproses, dan berhak menarik izin sewaktu-waktu.

---

## C. TRANSPARANSI ALGORITMA (EXPLAINABLE AI) DAN MITIGASI MANIPULASI SISTEM

Salah satu kritik terbesar terhadap model pembelajaran mendalam (*Deep Learning*) modern adalah sifatnya yang menyerupai **Kotak Hitam (*Black Box*)**—sistem mampu memberikan prediksi yang sangat akurat, namun para ilmuwan sendiri tidak dapat menjelaskan secara runtut mengapa dan bagaimana angka keputusan tersebut dihasilkan.

### 1. Bahaya "Tirani Kotak Hitam" (*Black Box Tyranny*)

Bayangkan jika seorang warga miskin mengajukan permohonan bantuan sosial atau seorang pasien ditolak klaim asuransi kesehatannya oleh sebuah sistem AI, dan ketika ditanya alasannya, petugas hanya menjawab: *"Komputer menyatakan demikian, kami tidak tahu alasannya karena modelnya adalah kotak hitam."*

Kondisi ini melanggar hak asasi martabat manusia. Dalam domain kritis (hukum, perbankan, kepolisian, dan kesehatan), model AI wajib mematuhi standar **Explainable AI (XAI / Kecerdasan Artifisial yang Dapat Dijelaskan)**:
- Sistem wajib menyediakan penjelasan logis dan transparan mengenai faktor-faktor apa saja yang memengaruhi keputusannya.
- Pengguna berhak meminta peninjauan ulang oleh manusia (*Human-in-the-Loop* / Hak Banding) jika keputusan sistem dirasa merugikan hak hidupnya.

### 2. Ancaman Serangan Manipulasi Data: Serangan Bermusuhan (*Adversarial Attacks*)

Sistem kecerdasan artifisial memiliki kerentanan keamanan yang unik. Model Computer Vision pada mobil otonom dapat dikelabui secara fatal melalui **Serangan Bermusuhan (*Adversarial Attack*)**:
- Peretas menempelkan stiker kecil yang tampak biasa bagi mata manusia pada rambu lalu lintas "STOP".
- Namun bagi algoritma penglihatan komputer, stiker tersebut memanipulasi nilai gradien matriks piksel sedemikian rupa sehingga model AI 99% yakin bahwa rambu "STOP" tersebut adalah rambu batas kecepatan "80 km/jam"! Mobil otonom melaju kencang tanpa berhenti dan menabrak persimpangan.

Oleh karena itu, seorang insinyur AI profesional wajib melakukan pengujian ketahanan (*Adversarial Robustness Testing*) dan penguatan pertahanan data secara berkala sebelum merilis model ke ruang publik.

---

## D. LEMBAR KERJA PESERTA DIDIK (LKPD) 6.1

### Capstone Project: Prototipe Solusi Sosial Berbasis Machine Learning dan NLP

**Tujuan Pembelajaran:**
Peserta didik secara berkelompok (3-4 orang) mampu merancang sebuah prototipe solusi sistemik terintegrasi yang memadukan pipeline Machine Learning atau NLP dengan antarmuka basis data/API untuk memecahkan permasalahan nyata di lingkungan masyarakat lokal, serta menyusun laporan audit etika dan transparansi algoritma.

**Pilihan Tema Proyek Berkelanjutan:**
1. **Pertanian Cerdas Lokal:** Model klasifikasi penyakit tanaman pangan lokal (padi/jagung) berbasis citra atau teks gejala klinis.
2. **Kesehatan Komunitas:** Sistem pemilah mandiri kelayakan gizi dan deteksi risiko stunting balita posyandu desa.
3. **Pemberdayaan UMKM:** Model analisis sentimen ulasan produk lokal dan asisten rekomendasi harga wajar pasar tradisional.

**Tahapan Pelaksanaan Proyek:**
1. **Analisis Kebutuhan & Empati:** Wawancarai calon pengguna lokal untuk merumuskan masalah nyata.
2. **Pengumpulan & Pembersihan Data:** Kumpulkan dataset etis berlisensi terbuka dan lakukan pra-pemrosesan data bebas kebocoran.
3. **Pelatihan & Evaluasi Model:** Latih algoritma klasifikasi (KNN/Decision Tree/Naive Bayes) dan evaluasi menggunakan Matriks Konfusi (fokus pada Recall dan F1-Score).
4. **Integrasi Perangkat Lunak:** Hubungkan model dengan antarmuka layanan (REST API sederhana atau aplikasi konsol).
5. **Audit Etika & Transparansi (Explainability):** Susun lembar pernyataan etika proyek:
   - Apakah dataset memuat bias etnis/gender? Bagaimana tim kalian memitigasinya?
   - Bagaimana cara sistem menjelaskan alasan prediksinya kepada pengguna awam?
   - Apa protokol keselamatan tim jika model mengalami False Negative?

---

## E. RANGKUMAN MATERI BAB VI

1. **Disrupsi Ketenagakerjaan & Augmented Intelligence:** Otomasi kecerdasan artifisial menggeser pekerjaan klerikal repetitif menuju profesi bernalar kritis dan berkecerdasan emosional. Paradigma masa depan memosisikan AI sebagai penguat daya komputasi (*Augmented Intelligence*), di mana manusia memegang kemudi arah strategis, empati, dan kendali etika.
2. **Prinsip Human-Centered AI:** Pengembangan sistem cerdas wajib tunduk pada empat pilar UNESCO: keadilan non-diskriminasi, kelestarian lingkungan hidup (*Green AI*), akuntabilitas hukum mutlak pada pembuat sistem manusia, dan kepatuhan hukum privasi data (UU PDP No. 27/2022).
3. **Transparansi & Ketahanan Sistem:** Menghindari bahaya tirani "Kotak Hitam" melalui penerapan kaidah *Explainable AI (XAI)* yang memberikan alasan rasional atas setiap keputusan sistem, serta memperkuat ketahanan algoritma terhadap ancaman manipulasi siber (*Adversarial Attacks*).
4. **Integritas Insan Inovator Muda:** Kedaulatan teknologi Indonesia bertumpu pada generasi perekayasa perangkat lunak dan ilmuwan data yang tidak hanya cerdas merangkai algoritma, melainkan berkarakter teguh menjunjung tinggi martabat kemanusiaan dan nilai-nilai luhur Pancasila.

---

## F. EVALUASI AKHIR TAHUN FASE F (KELAS XI)

### I. Pilihan Ganda Komprehensif (Bab I - VI)
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Pilar dalam paradigma pemrograman berorientasi objek yang memungkinkan metode bernama sama pada kelas-kelas turunan yang berbeda memiliki perilaku operasional yang berbeda (*method overriding*) disebut...
   A. Enkapsulasi
   B. Abstraksi
   C. Polimorfisme
   D. Kompresi

2. Perintah terminal Git yang digunakan untuk menggabungkan cabang fitur (*feature branch*) yang telah selesai diuji kembali ke cabang utama (`main`) adalah...
   A. `git init`
   B. `git merge`
   C. `git status`
   D. `git drop`

3. Format pertukaran data modern berbasis teks terbuka yang tersusun atas pasangan Kunci dan Nilai (*Key-Value Pairs*) serta ringan ditransmisikan melalui jaringan internet adalah...
   A. XML
   B. CSV
   C. JSON
   D. Biner Raw

4. Manakah pasangan metode protokol HTTP dan kode status respons yang paling tepat ketika sebuah aplikasi klien sukses menambahkan data siswa baru ke dalam basis data server?
   A. Metode GET dengan kode status 404 Not Found
   B. Metode POST dengan kode status 201 Created
   C. Metode DELETE dengan kode status 500 Server Error
   D. Metode PUT dengan kode status 401 Unauthorized

5. Teknik penulisan kueri basis data SQL yang memisahkan struktur perintah dari parameter data mentah menggunakan tanda pemisah (`?`) guna menangkal serangan siber SQL Injection dinamakan...
   A. String Concatenation
   B. Parameterized Query (Prepared Statement)
   C. Cross-Site Scripting
   D. Hash Collision

6. Format gambar grafis digital yang tersusun atas formula matematika geometris berbasis XML sehingga kualitasnya tidak akan pernah buram atau pecah saat diperbesar pada layar monitor resolusi tinggi adalah...
   A. JPEG
   B. SVG (Scalable Vector Graphics)
   C. PNG Raster
   D. BMP

7. Berkas manifes teks dalam ekosistem Python yang mencatat daftar seluruh pustaka pihak ketiga beserta nomor versinya secara pasti untuk menjamin kemudahan instalasi di komputer lain adalah...
   A. `README.md`
   B. `requirements.txt`
   C. `license.mit`
   D. `setup.bat`

8. Praktik rekayasa pembelajaran mesin yang memisahkan dataset secara ketat menjadi Data Latih (80%) dan Data Uji (20%) bertujuan untuk mencegah terjadinya fenomena...
   A. Database Deadlock
   B. Kebocoran Data (*Data Leakage*)
   C. Stack Overflow
   D. Null Pointer Exception

9. Diberikan hasil evaluasi model klasifikasi kanker: dari 100 pasien yang sebenarnya sakit kanker, sistem AI berhasil mendeteksi 92 pasien secara tepat (TP), sedangkan 8 pasien sakit lainnya lolos terabaikan sebagai orang sehat (FN). Berapakah nilai Recall (Sensitivitas) dari model tersebut?
   A. 8,0%
   B. 92,0%
   C. 50,0%
   D. 100,0%

10. Metrik evaluasi kinerja model klasifikasi pembelajaran mesin yang merupakan rata-rata harmonik penyeimbang antara nilai Presisi dan nilai Recall adalah...
    A. Akurasi
    B. F1-Score
    C. Root Mean Square
    D. Silhouette Score

11. Tahapan pra-pemrosesan teks dalam Natural Language Processing (NLP) yang bertugas memotong imbuhan awalan dan akhiran dari suatu kata untuk mengembalikannya ke bentuk kata dasar aslinya dinamakan...
    A. Case Folding
    B. Tokenizing
    C. Stemming
    D. Stopwords Removal

12. Algoritma pembobotan teks yang memberikan bobot tinggi pada kata unik yang bernilai informasi spesifik dalam satu dokumen dan memberi bobot rendah pada kata pasaran yang sering muncul di semua dokumen adalah...
    A. TF-IDF (Term Frequency - Inverse Document Frequency)
    B. Bag of Words
    C. One-Hot Vector
    D. Binary Index

13. Komponen kunci dalam arsitektur jaringan saraf Transformer yang memungkinkan model bahasa besar (seperti GPT atau Gemini) menghitung derajat keterkaitan semantik antarkata dalam kalimat panjang secara simultan adalah...
    A. Convolution Filter
    B. Self-Attention Mechanism
    C. Max Pooling
    D. Recurrent Feedback Loop

14. Paradigma masa depan peradaban yang memosisikan kecerdasan artifisial bukan sebagai pengganti manusia melainkan sebagai mitra penguat daya komputasi akal budi manusia dinamakan...
    A. Replacement Paradigm
    B. Augmented Intelligence
    C. Technocracy Rule
    D. Autonomous Singularity

15. Pendekatan dalam pengembangan kecerdasan artifisial yang menuntut agar setiap keputusan yang dihasilkan oleh algoritma dapat dipahami, dilacak, dan dipertanggungjawabkan secara logis kepada manusia (*anti-kotak hitam*) dikenal sebagai...
    A. Black Box Computing
    B. Brute Force AI
    C. Explainable AI (XAI)
    D. Heuristic Guessing

---

### II. Uraian Pemecahan Kasus Sistemik Berbobot HOTS
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, mendalam, dan tepat!

1. **Arsitektur Perangkat Lunak Berorientasi Objek & API:**
Sebuah rumah sakit daerah ingin membangun sistem antrean poliklinik cerdas.
a. Rancanglah struktur kelas OOP: Kelas Induk `Pasien` (atribut: `id_pasien`, `nama_lengkap`, dan atribut privat `__rekam_medis`) serta Kelas Turunan `PasienPrioritas` (tambahan atribut: `kategori_kebutuhan_khusus`). Tuliskan kode Python lengkapnya disertai metode getter untuk rekam medis!
b. Jika data antrean tersebut ingin dikirimkan ke aplikasi layar monitor TV di ruang tunggu melalui layanan REST API, rancanglah contoh muatan data (*payload*) berformat JSON yang aman dan efisien!

2. **Keamanan Siber Basis Data & Regulasi Privasi:**
Sebuah aplikasi bimbingan belajar sekolah mencatat riwayat nilai dan nomor induk kependudukan (NIK) siswa.
a. Jelaskan bagaimana serangan siber *SQL Injection* dapat membocorkan seluruh data NIK tersebut jika kueri ditulis menggunakan penggabungan teks langsung!
b. Berikan contoh potongan sintaks *Parameterized Query* dalam bahasa Python untuk menangkal serangan tersebut!
c. Analisislah kewajiban hukum pengembang aplikasi tersebut berdasarkan Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022) jika terjadi insiden kebocoran data!

3. **Analisis Matematis Evaluasi Model Machine Learning:**
Sebuah model AI pendeteksi dini kebakaran hutan (*Forest Fire Early Warning*) diuji menggunakan 500 citra satelit independen:
- True Positive (TP) = 45 titik api kebakaran terdeteksi tepat
- False Positive (FP) = 15 citra awan panas salah dituduh kebakaran
- False Negative (FN) = 5 titik api kebakaran lolos tak terdeteksi
- True Negative (TN) = 435 kawasan hutan normal diprediksi tepat
a. Hitunglah nilai Akurasi, Presisi, Recall, dan F1-Score model tersebut!
b. Dalam konteks mitigasi bencana kebakaran hutan, analisislah mengapa nilai Recall (90%) jauh lebih penting untuk terus ditingkatkan mendekati 100% dibandingkan nilai Presisi (75%)!

4. **Pipeline Natural Language Processing (NLP):**
Diberikan sebuah kalimat opini mentah dari masyarakat:
`"Fasilitas laboratorium komputer ini SANGAT MEMBANTU kami dalam mempelajari koding!"`
a. Uraikan transformasi bentuk kalimat tersebut melalui tahapan Case Folding, Tokenizing, Stopwords Removal, dan Stemming Bahasa Indonesia!
b. Jelaskan secara matematis mengapa pembobotan TF-IDF memberikan skor yang jauh lebih besar pada kata "koding" daripada kata "dalam" pada dokumen teknologi tersebut!

5. **Etika Rekayasa Sistem Cerdas & Disrupsi Sosial:**
Sebuah perusahaan transportasi logistik berencana mengganti seluruh pengemudi truk antar-kota dengan armada truk otonom berbasis AI guna memangkas biaya operasional sebesar 40%.
a. Analisislah dilema sosio-ekonomi dan dampak ketenagakerjaan dari kebijakan tersebut terhadap kesejahteraan para pekerja lokal!
b. Bagaimana konsep *Augmented Intelligence* menawarkan jalan tengah yang lebih manusiawi (*Human-Centered*) dibandingkan penggantian total secara sepihak?
c. Jika suatu saat truk otonom tersebut mengalami kecelakaan di jalan raya akibat gangguan sensor cuaca ekstrem, menurut prinsip etika AI internasional, pihak manakah yang wajib memikul tanggung jawab hukum dan moral? Jelaskan alasannya!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS EVALUASI AKHIR TAHUN

**Kunci Pilihan Ganda Komprehensif:**
1. **C** (Polimorfisme memungkinkan method overriding pada kelas turunan).
2. **B** (`git merge` menggabungkan cabang fitur ke cabang utama).
3. **C** (JSON adalah standar format pertukaran data terbuka berbasis teks key-value).
4. **B** (Metode POST dengan status 201 Created menandakan keberhasilan penambahan sumber daya baru).
5. **B** (Parameterized Query memisahkan perintah SQL dari data mentah).
6. **B** (SVG menggunakan rumus matematika vektor berbasis XML sehingga tidak pernah buram).
7. **B** (`requirements.txt` mencatat daftar dependensi pustaka Python).
8. **B** (Train-Test Split mencegah kebocoran data / data leakage).
9. **B** (Recall = TP / [TP + FN] = 92 / [92 + 8] = 92 / 100 = 92,0%).
10. **B** (F1-Score adalah rata-rata harmonik penyeimbang Presisi dan Recall).
11. **C** (Stemming mengembalikan kata berimbuhan ke kata dasar).
12. **A** (TF-IDF menimbang frekuensi lokal terhadap kelangkaan global dokumen).
13. **B** (Self-Attention mechanism menghitung bobot keterkaitan antarkata kalimat panjang).
14. **B** (Augmented Intelligence memosisikan AI sebagai penguat daya komputasi akal budi manusia).
15. **C** (Explainable AI / XAI menolak tirani kotak hitam dan menuntut transparansi logis).

**Pembahasan Soal Uraian Kasus Sistemik:**
1. *Rancangan Kelas Pasien & Payload JSON:*
   a. Kode Python OOP:
   ```python
   class Pasien:
       def __init__(self, id_pasien, nama_lengkap, rekam_medis):
           self.id_pasien = id_pasien
           self.nama_lengkap = nama_lengkap
           self.__rekam_medis = rekam_medis  # Atribut Privat

       def get_rekam_medis(self):
           return self.__rekam_medis

   class PasienPrioritas(Pasien):
       def __init__(self, id_pasien, nama_lengkap, rekam_medis, kebutuhan_khusus):
           super().__init__(id_pasien, nama_lengkap, rekam_medis)
           self.kebutuhan_khusus = kebutuhan_khusus
   ```
   b. Payload JSON Layar TV (Efisien & Menjaga Privasi tanpa mengekspos rekam medis rahasia):
   ```json
   {
     "status": "sukses",
     "nomor_antrean": "A-015",
     "nama": "Arya Dinata",
     "poliklinik": "Poli Umum",
     "prioritas": false
   }
   ```
2. *Keamanan Siber & UU PDP:*
   a. Jika menggunakan konkatenasi string: `SELECT * FROM siswa WHERE nisn = '` + input + `'`, peretas dapat menginput `' OR '1'='1`, mengekspos seluruh pangkalan data NIK secara telanjang ke publik.
   b. Parameterized Query:
   `cursor.execute("SELECT * FROM siswa WHERE nisn = ?", (input_nisn,))`
   c. Tanggung jawab hukum UU PDP: (1) Kewajiban memberitahukan insiden kebocoran secara tertulis kepada pemilik data dan lembaga pengawas paling lambat 3 x 24 jam; (2) Mengambil langkah pemulihan dan penutupan celah keamanan; (3) Sanksi administratif berupa denda ganti rugi finansial hingga pembekuan izin operasional sistem jika terbukti lalai tidak mengenkripsi data sensitif warga negara.
3. *Perhitungan Evaluasi Kebakaran Hutan:*
   a. Total = 45 + 15 + 5 + 435 = 500 sampel.
   - Akurasi = (45 + 435) / 500 = 480 / 500 = **96,0% (0,96)**.
   - Presisi = 45 / (45 + 15) = 45 / 60 = **75,0% (0,75)**.
   - Recall = 45 / (45 + 5) = 45 / 50 = **90,0% (0,90)**.
   - F1-Score = 2 * (0,75 * 0,90) / (0,75 + 0,90) = 1,35 / 1,65 = **81,82% (0,818)**.
   b. Urgensi Recall: False Positive (alarm palsu awan panas) hanya mengakibatkan petugas patroli memeriksa lokasi yang ternyata aman. Namun False Negative (ada kebakaran hutan tetapi model menyatakan aman) mengakibatkan api berkobar hebat membakar ribuan hektar hutan lindung, merenggut nyawa flora-fauna, dan memicu bencana kabut asap lintas negara. Oleh karena itu, metrik Recall wajib diprioritaskan mendekati 100%.
4. *Transformasi Teks NLP & TF-IDF:*
   a. Kalimat: `"Fasilitas laboratorium komputer ini SANGAT MEMBANTU kami dalam mempelajari koding!"`
   - Case Folding: `"fasilitas laboratorium komputer ini sangat membantu kami dalam mempelajari koding"`
   - Tokenizing: `['fasilitas', 'laboratorium', 'komputer', 'ini', 'sangat', 'membantu', 'kami', 'dalam', 'mempelajari', 'koding']`
   - Stopwords: `['fasilitas', 'laboratorium', 'komputer', 'membantu', 'mempelajari', 'koding']` (*ini, sangat, kami, dalam* dibuang).
   - Stemming: `['fasilitas', 'laboratorium', 'komputer', 'bantu', 'ajar', 'koding']`
   b. Bobot TF-IDF: Kata "dalam" adalah kata sambung pasaran yang muncul di hampir 100% dokumen sehingga nilai IDF-nya = log(1) = 0 (bobot akhir nol). Kata "koding" adalah kata khusus bidang komputasi yang frekuensi lokalnya tinggi di dokumen tersebut namun langka di dokumen umum lainnya, menghasilkan nilai IDF tinggi dan bobot nilai signifikan.
5. *Etika Human-Centered & Tanggung Jawab Hukum:*
   a. Dilema Sosial: Pemutusan hubungan kerja massal pengemudi truk memicu gejolak sosial, hilangnya mata pencaharian ribuan keluarga kelas pekerja, dan memperlebar jurang ketimpangan ekonomi daerah.
   b. Solusi Augmented Intelligence: Truk tidak beroperasi 100% tanpa pengemudi. Truk dilengkapi fitur otonom asisten (*autopilot*) untuk jalur lurus bebas hambatan guna mencegah kelelahan sopir, sementara manuver rumit di jalan kota dan pengelolaan kargo tetap dikendalikan oleh pengemudi manusia yang telah ditingkatkan kompetensi teknologinya (*reskilling*) dengan gaji yang lebih layak dan jam kerja yang manusiawi.
   c. Tanggung Jawab Hukum: Tanggung jawab hukum melekat secara proporsional pada entitas manusia dan korporasi: (1) Produsen perangkat lunak AI bertanggung jawab jika ditemukan cacat logika pada algoritma deteksi sensor; (2) Perusahaan logistik bertanggung jawab jika lalai melakukan pemeliharaan armada truk; (3) Operator armada manusia yang mengawasi operasional jarak jauh jika gagal mengambil alih kemudi darurat. AI adalah alat mekanik dan tidak dapat dimintai pertanggungjawaban hukum di pengadilan.


# GLOSARIUM ISTILAH TINGKAT LANJUT FASE F

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
