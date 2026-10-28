# -*- coding: utf-8 -*-
"""
Naskah Lengkap Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SMP/MTs Kelas VII (Fase D)
Standar: Pusat Perbukuan Kemendikdasmen RI / Deep Learning Approach (Mindful, Meaningful, Joyful)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

from smp7_naskah_frontmatter import DAFTAR_PUSTAKA_RESMI_SMP7

GURU_FRONT_MATTER_SMP7 = """# BUKU PANDUAN GURU
## KODING DAN KECERDASAN ARTIFISIAL UNTUK SMP/MTs KELAS VII
### Mata Pelajaran Pilihan — Fase D (Tingkat Pertama SMP)

**Penulis:**  
Gede Erik Aktama, S.Pd., M.Pd.  
*(Fasilitator Nasional Koding dan Kecerdasan Artifisial Kemendikdasmen RI)*  
*(Dosen Lektor & Ketua Program Studi S1 Sistem Komputer, Universitas Parna Raya)*  

**Penelaah & Konsultan Ahli:**  
Tim Pengembang Kurikulum KKA Direktorat Guru Pendidikan Dasar Kemendikdasmen RI  

**Penerbit:**  
Pusat Perbukuan  
Badan Standar, Kurikulum, dan Asesmen Pendidikan  
Kementerian Pendidikan Dasar dan Menengah Republik Indonesia  
Tahun 2025 / 2026  

---

## IDENTITAS PENERBITAN & HAK CIPTA
Judul Buku: Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SMP/MTs Kelas VII (Fase D)  
Penulis: Gede Erik Aktama, S.Pd., M.Pd.  
Penyunting / Editor Naskah: Tim Fasilitator Dikdasmen Kemendikdasmen  
Tata Letak & Tipografi: Format Standar Buku Ajar UNESCO (15,5 cm x 23,0 cm)  
Desain Sampul & Ilustrasi: Tim Desain Edukatif Digital Aktama  
Penerbit: Pusat Perbukuan Kemendikdasmen RI  
Hak Cipta Dilindungi Undang-Undang: Berdasarkan Permendikdasmen No. 13 Tahun 2025 tentang Kurikulum pada Pendidikan Dasar dan Menengah.  

---

## KATA PENGANTAR KEMENDIKDASMEN
Puji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa atas terselesaikannya **Buku Panduan Guru Koding dan Kecerdasan Artifisial untuk SMP/MTs Kelas VII (Fase D)**. Buku panduan operasional ini disusun untuk menjadi pedoman pedagogis praktis bagi bapak dan ibu guru di seluruh Indonesia dalam mengawal proses transformasi digital peserta didik pada masa awal jenjang Sekolah Menengah Pertama.

Masa awal SMP adalah periode pembentukan nalar kritis dan kedewasaan sosial. Dalam kurikulum KKA Fase D, guru tidak lagi hanya mengajarkan keterampilan teknis menyusun balok kode, melainkan memfasilitasi murid membedah persoalan sosial di sekitarnya menggunakan data empiris, mengomunikasikan gagasan lewat infografis yang beradab, serta membongkar cara kerja dan keterbatasan etis dari sistem kecerdasan artifisial generatif.

Buku Panduan Guru ini memuat skema alur 36 kali pertemuan tahunan (total 72 Jam Pelajaran), panduan diferensiasi pembelajaran berbasis keragaman kesiapan murid, instrumen rubrik penilaian autentik, serta strategi penanaman nilai etika *Human-Centered AI*.

Apresiasi tinggi kami sampaikan kepada Saudara **Gede Erik Aktama, S.Pd., M.Pd.** atas dedikasi dan karyanya dalam menyusun buku panduan yang komprehensif ini. Semoga buku ini menjadi sumber inspirasi yang menyalakan gairah para guru dalam mencetak generasi emas pemikir komputasional yang berakhlak mulia.

Jakarta, 2025  
**Kementerian Pendidikan Dasar dan Menengah Republik Indonesia**

---

## PRAKATA PENULIS
Bapak dan Ibu Guru pejuang pendidikan menengah pertama di seluruh penjuru Nusantara yang saya muliakan,

Salam hangat, salam inovasi, dan salam literasi digital!

Memasuki jenjang SMP (Fase D), kita menyambut anak-anak remaja yang penuh energi, rasa ingin tahu yang meluap, dan interaksi yang semakin intens dengan dunia maya melalui telepon pintar mereka. Tugas kita sebagai pendidik bukanlah menjauhkan mereka dari teknologi, melainkan membimbing mereka agar mampu mengendalikan teknologi dengan kesadaran moral yang kokoh.

Buku Panduan Guru ini dirancang dengan pendekatan **Pembelajaran Mendalam (*Deep Learning*)** yang berakar pada tiga dimensi utama:
1. **Berkesadaran (*Mindful Learning*):** Menumbuhkan kebiasaan reflektif pada murid agar tidak menerima informasi di internet secara pasif, melainkan selalu menguji keaslian fakta, mewaspadai bias algoritma, dan menginsafi jejak digital mereka.
2. **Bermakna (*Meaningful Learning*):** Mengaitkan setiap teori komputasi—seperti dekomposisi fishbone, flowchart ISO, dan prompting—dengan pemecahan masalah nyata di lingkungan sekolah dan kepedulian kemanusiaan.
3. **Menggembirakan (*Joyful Learning*):** Menghadirkan dinamika kelas yang hidup melalui permainan peran simulasi unplugged (*Robot Literal*), eksperimen studio grafis cloud, dan perayaan karya kampanye digital bersama.

Buku ini telah memuat pembagian 36 pertemuan yang terinci, petunjuk diferensiasi untuk murid berkebutuhan khusus dan murid berbakat (*gifted*), kunci jawaban soal HOTS, pedoman penilaian autentik, serta panduan pendampingan orang tua.

Semoga buku panduan ini menjadi sahabat setia bagi Bapak dan Ibu Guru dalam memandu tunas-tunas muda Indonesia melangkah percaya diri menjadi pionir peradaban teknologi yang berintegritas luhur. Selamat mendidik dan selamat menginspirasi!

Manado, 2025  
**Gede Erik Aktama, S.Pd., M.Pd.**  
*(Fasilitator Nasional KKA Kemendikdasmen RI)*  
*(Dosen Lektor & Kaprodi Sistem Komputer, Universitas Parna Raya)*

---

## DAFTAR ISI PANDUAN GURU
Bagian 1: Petunjuk Umum Pembelajaran KKA SMP Kelas 7 Fase D
  A. Hakikat Mata Pelajaran KKA dan Profil Kelulusan Fase D
  B. Karakteristik Murid Remaja Awal dan Pendekatan Pembelajaran Mendalam
  C. Capaian Pembelajaran & Alur Tujuan Pembelajaran (ATP) 72 JP
  D. Strategi Pembelajaran Mendalam: Mindful, Meaningful, Joyful
  E. Skema Penilaian Autentik & Portofolio Fase D
  F. Manajemen Laboratorium Komputer dan Pembelajaran Unplugged

Bagian 2: Panduan Khusus Pembelajaran Bab 1 - Bab 4
  Bab I: Berpikir Komputasional & Pengelolaan Data Kehidupan Masyarakat (16 JP)
    A. Gambaran Umum Pembelajaran Bab 1
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Analisis Data Lapangan
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab II: Desain Komunikasi Digital: Slide Presentasi & Infografis Tematik (20 JP)
    A. Gambaran Umum Pembelajaran Bab 2
    B. Skema Alur Pembelajaran 10 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Desain Infografis CRAP
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab III: Menyelami Kecerdasan Artifisial Generatif (GenAI) & Etika Kritis (16 JP)
    A. Gambaran Umum Pembelajaran Bab 3
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Lembar Audit Halusinasi AI
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab IV: Interaksi Efektif dengan AI: Seni Input Bermakna & Prompting Edukatif (20 JP)
    A. Gambaran Umum Pembelajaran Bab 4
    B. Skema Alur Pembelajaran 10 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Capstone Mini Proyek Kampanye Digital
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid

Bagian 3: Panduan Asesmen Sumatif Akhir Tahun & Pelaporan Hasil Belajar
  A. Rubrik Penilaian Portofolio Capstone Mini Proyek
  B. Kunci Jawaban & Pembahasan Evaluasi Sumatif Akhir Tahun
  C. Panduan Konversi Nilai ke Rapor Kurikulum Nasional

Bagian Akhir Buku Guru: Glosarium Pembelajaran, Daftar Pustaka Resmi, & Profil Penulis
"""

GURU_BAGIAN_1_SMP7 = """# BAGIAN 1: PETUNJUK UMUM PEMBELAJARAN KKA SMP KELAS 7 FASE D

### A. Hakikat Mata Pelajaran KKA dan Profil Kelulusan Fase D Kelas VII
Mata pelajaran pilihan Koding dan Kecerdasan Artifisial (KKA) pada jenjang Sekolah Menengah Pertama (Fase D) bertujuan membentuk peserta didik yang tidak hanya cakap mengoperasikan gawai digital, melainkan memiliki disposisi intelektual tingkat tinggi (*High-Order Computational Thinking*), kepekaan terhadap etika data sosial, kecerdasan menyaring luaran AI generatif, serta keterampilan berkolaborasi menciptakan karya komunikasi visual yang bermartabat.

Pada akhir kelas VII Fase D, peserta didik ditargetkan mencapai kompetensi:
1. Mampu mengumpulkan, mengorganisasikan, dan menganalisis data empiris lingkungan masyarakat serta merumuskan algoritma pemecahan masalah dengan diagram tulang ikan (*fishbone*) dan flowchart standar ISO.
2. Mampu merancang media komunikasi digital (slide presentasi dan infografis) dengan menerapkan 4 prinsip desain visual profesional C.R.A.P (*Contrast, Repetition, Alignment, Proximity*) serta taat pada lisensi hak cipta terbuka Creative Commons (TASL).
3. Mampu membongkar arsitektur Model Bahasa Besar (LLM), memahami fenomena halusinasi data dan bias algoritma, serta mendeteksi manipulasi video/audio rekayasa Deepfake.
4. Mampu menyusun instruksi input bermakna (*prompting*) dengan formula 4 pilar (Role, Task, Context, Format) secara aman tanpa membocorkan privasi data pribadi.
5. Mampu menuntaskan Capstone Mini Proyek berupa kampanye sosial digital berbasis kolaborasi manusia dan asisten cerdas AI.

---

### B. Karakteristik Murid Remaja Awal dan Pendekatan Pembelajaran Mendalam
Murid kelas 7 SMP (berusia rata-rata 12-13 tahun) berada pada fase transisi psikososial remaja awal. Karakteristik perkembangannya meliputi:
* Daya abstraksi logis mulai berkembang pesat, mampu memperdebatkan argumen moral dan keadilan sosial.
* Keterikatan tinggi pada interaksi ponsel pintar dan media sosial, rentan terhadap tekanan tren sebaya (*peer pressure*) dan hoaks viral.
* Membutuhkan ruang apresiasi diri yang nyata di mana ide dan opini kritis mereka didengar oleh orang dewasa.

Implementasi **Pembelajaran Mendalam (*Deep Learning*)**:
* **Mindful:** Guru mengajak murid memulai kelas dengan memusatkan kesadaran nalar (*Mindful Inquiry*), mempertanyakan motif di balik sebuah informasi atau gambar digital sebelum mempercayainya.
* **Meaningful:** Topik pembelajaran diangkat langsung dari fenomena keseharian murid (antrean kantin, pencegahan DBD di sekolah, kampanye anti-bullying).
* **Joyful:** Menerapkan simulasi gerak peran (*Role-Play Robot Literal*), tantangan kartu logika, dan pameran mading koridor sekolah yang meriah.

---

### C. Alokasi Waktu dan Struktur Kurikulum Tahunan (72 JP)
Mata pelajaran KKA dialokasikan 2 Jam Pelajaran (JP) @ 40 menit per minggu. Dalam satu tahun ajaran dialokasikan total 36 minggu efektif pembelajaran (72 JP) dengan distribusi materi:
* **Semester 1 (36 JP):**
  * Bab 1: Berpikir Komputasional & Pengelolaan Data Kehidupan Masyarakat (16 JP - 8 Pertemuan)
  * Bab 2: Desain Komunikasi Digital: Slide Presentasi & Infografis Tematik (20 JP - 10 Pertemuan)
* **Semester 2 (36 JP):**
  * Bab 3: Menyelami Kecerdasan Artifisial Generatif (GenAI) & Etika Kritis (16 JP - 8 Pertemuan)
  * Bab 4: Interaksi Efektif dengan AI: Seni Input Bermakna & Prompting Edukatif (20 JP - 10 Pertemuan)

---

### D. Skema Penilaian Autentik & Manajemen Sarana Belajar
Penilaian KKA menitikberatkan pada proses berpikir kritis dan portofolio karya nyata:
1. **Asesmen Formatif Pembelajaran (Bobot 35%):** Partisipasi diskusi kasus, lembar kerja analisis data, lembar audit halusinasi AI, dan refleksi diri.
2. **Asesmen Kinerja Capstone Mini Proyek (Bobot 40%):** Kualitas formulasi prompt 4 pilar, ketepatan verifikasi fakta manusia, estetika infografis CRAP, dan presentasi tim.
3. **Asesmen Sumatif Akhir Tahun (Bobot 25%):** Uji pemahaman terstandar berbasis stimulus kasus kontekstual.

Bagi sekolah dengan keterbatasan perangkat komputer:
* Konsep analisis data, fishbone diagram, flowchart ISO, dan formula prompting dapat diajarkan secara sangat optimal melalui metode **Unplugged** menggunakan kertas plano, sticky notes, dan permainan peran langsung.
"""

GURU_BAGIAN_2_SMP7 = """# BAGIAN 2: PANDUAN KHUSUS PEMBELAJARAN BAB 1 - BAB 4

## BAB I: BERPIKIR KOMPUTASIONAL & PENGELOLAAN DATA KEHIDUPAN MASYARAKAT

### A. Gambaran Umum Pembelajaran Bab 1
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu memahami peran penting pengelolaan data dalam kehidupan masyarakat.
  2. Peserta didik mampu menerapkan dekomposisi masalah dan diagram tulang ikan (*fishbone*) untuk mengurai akar persoalan sosial sekolah.
  3. Peserta didik mampu merancang, memvalidasi, dan menguji instruksi logika algoritma menggunakan standar simbol flowchart ISO dan tabel penelusuran (*trace table*).
* **Profil Pelajar Pancasila:** Bernalar Kritis, Mandiri, dan Berakhlak Mulia (integritas pelaporan data).
* **Media Belajar:** Buku Siswa Bab 1, papan survei dan kuisioner kantin, kertas plano berpetak untuk menggambar flowchart ISO, kalkulator sederhana.

---

### B. Skema Alur Pembelajaran Bab 1 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 1** (2 JP) | Apersepsi & Data dalam Masyarakat | Memahami peran data dalam kehidupan sosial dan membedakan data kuantitatif vs kualitatif. | Membaca komik antrean kantin; observasi langsung memilah 5 contoh data kuantitatif dan kualitatif di sekolah. | Tanya jawab pemantik lisan |
| **Pertemuan 2** (2 JP) | Siklus Pengelolaan Data 4 Tahap | Memahami tahapan: kumpul, organisasi, analisis, dan pengambilan kebijakan. | Simulasi alur data sensus penduduk sederhana; murid mencatat waktu transaksi belanja di kantin sekolah. | Lembar pencatatan data mentah |
| **Pertemuan 3** (2 JP) | Mengorganisasi Data ke Tabel & Grafik | Mampu menyajikan data ke tabel frekuensi, diagram batang, garis, dan lingkaran. | Mengubah data mentah antrean kantin menjadi diagram batang dan diagram lingkaran di buku berpetak / spreadsheet. | Penilaian grafik visual data |
| **Pertemuan 4** (2 JP) | Dekomposisi & Diagram Tulang Ikan | Mampu melacak akar masalah menggunakan Fishbone Diagram Kaoru Ishikawa. | Diskusi kelompok membedah faktor Manusia, Metode, Mesin/Alat, dan Lingkungan penyebab antrean kantin. | Lembar kerja Fishbone Diagram |
| **Pertemuan 5** (2 JP) | Standar Simbol Flowchart ISO | Mampu memahami dan menggambar simbol Terminator, Input/Output, Proses, dan Decision. | Guru memodelkan flowchart peminjaman buku perpustakaan; murid berlatih menggambar simbol ISO dengan penggaris bentuk. | Latihan pengenalan simbol ISO |
| **Pertemuan 6** (2 JP) | Pengujian Logika dengan Trace Table | Mampu melacak nilai variabel dan mendeteksi bahaya infinite loop pada algoritma. | Simulasi penelusuran variabel saldo kartu kantin langkah demi langkah menggunakan tabel penelusuran manual. | Lembar kerja Trace Table |
| **Pertemuan 7** (2 JP) | Proyek LKPD 1.1: Evakuasi Bencana | Merancang flowchart rute tercepat evakuasi darurat gempa bumi sekolah. | Mengukur jarak koridor dan tangga; merancang bagan alir keputusan evakuasi agar tidak terjadi penumpukan massa. | Rubrik unjuk kerja LKPD 1.1 |
| **Pertemuan 8** (2 JP) | Evaluasi Formatif & Refleksi Bab 1 | Menguji ketuntasan kompetensi Berpikir Komputasional Bab 1. | Mengerjakan Tes Formatif Bab 1 (10 PG & 5 Uraian HOTS); refleksi integritas data dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 1 |

---

### C. Langkah-Langkah Pembelajaran Mendalam (Deep Learning)
1. **Fase Memahami (*Mindful Learning*):** Guru mengarahkan murid menyadari bahwa angka-angka survei mewakili nasib manusia nyata: *"Jika data bantuan gempa bumi salah dicatat, ada balita dan lansia yang terancam kelaparan di posko pengungsian!"*.
2. **Fase Mengaplikasikan (*Meaningful & Joyful Learning*):** Pembelajaran flowchart dilakukan secara interaktif. Guru meminta salah satu murid menjadi *"Mesin Kasir"* yang hanya mengeksekusi kartu perintah jajar genjang dan belah ketupat dari temannya.
3. **Fase Merefleksi (*Ethical Reflection*):** Menekankan larangan keras memanipulasi angka survei (*data falsification*) dalam dunia riset ilmiah.

---

### D. Panduan Diferensiasi (Remedial & Pengayaan)
* **Remedial:** Murid diberikan latihan menata kartu simbol flowchart ISO fisik yang sudah dipotong-potong sebelum diminta menggambarnya sendiri di kertas.
* **Pengayaan:** Tantang murid menambahkan 2 kondisi percabangan bersarang (*nested decision*) pada flowchart sistem evakuasi bencana (misalnya: jika tangga timur roboh tertimpa reruntuhan, rute otomatis dialihkan ke tangga darurat barat).

---

## BAB II: DESAIN KOMUNIKASI DIGITAL: SLIDE PRESENTASI & INFOGRAFIS TEMATIK

### A. Gambaran Umum Pembelajaran Bab 2
* **Alokasi Waktu:** 20 Jam Pelajaran (10 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi Digital (LD)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu menganalisis komponen konten digital dan menyusun alur narasi presentasi (Storyline 3 Babak).
  2. Peserta didik mampu menerapkan 4 prinsip desain komunikasi visual C.R.A.P (*Contrast, Repetition, Alignment, Proximity*) pada slide dan infografis.
  3. Peserta didik mampu menerapkan lisensi terbuka Creative Commons dan kaidah penulisan kredit sumber TASL.
* **Profil Pelajar Pancasila:** Kreatif, Bernalar Kritis, dan Berakhlak Mulia (menolak plagiarisme grafis).
* **Media Belajar:** Buku Siswa Bab 2, komputer/tablet dengan akses Canva / Google Slides / Inkscape, contoh slide bermasalah untuk dibedah.

---

### B. Skema Alur Pembelajaran Bab 2 (10 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 9** (2 JP) | Apersepsi Komik & Komponen Konten | Memahami fungsi slide sebagai jangkar visual (Visual Anchor) bukan teks bacaan naskah. | Membaca komik Ayu & Rian; membandingkan slide buruk (koran teks) vs slide modern berprinsip Less is More. | Observasi dialog kritis |
| **Pertemuan 10** (2 JP) | Prinsip Desain 1 & 2: Contrast & Repetition | Mampu menciptakan hierarki visual tegas dan konsistensi palet warna / tipografi. | Eksperimen mengubah kontras warna latar vs teks; menyusun palet 3 warna harmonis untuk tema poster kesehatan. | Latihan palet warna & kontras |
| **Pertemuan 11** (2 JP) | Prinsip Desain 3 & 4: Alignment & Proximity | Mampu menata keteraturan garis sejajar dan pengelompokan elemen logis. | Menata ulang posisi ikon dan teks yang berserakan di layar menggunakan fitur grid dan perataan rata kiri (*left align*). | Latihan perataan dan jarak |
| **Pertemuan 12** (2 JP) | Bedah Redesain Slide Kasus Nyata | Mampu mengidentifikasi pelanggaran CRAP dan membuat sketsa wireframe perbaikan. | Aktivitas Ayo Mencoba: merombak slide teks padat *"Bahaya DBD"* menjadi 3 ikon ringkas modern. | Sketsa wireframe redesain |
| **Pertemuan 13** (2 JP) | Storyline Presentasi: Struktur 3 Babak | Mampu menyusun alur presentasi: Masalah Menggugah, Solusi Data, Call to Action. | Bekerja dalam tim merancang naskah narasi presentasi peduli lingkungan sekolah dengan format 3 babak dramatis. | Draf naskah 3 babak |
| **Pertemuan 14** (2 JP) | Hak Cipta & Lisensi Creative Commons | Memahami perbedaan lisensi CC-BY, CC-SA, CC-NC, CC-ND dan Domain Publik. | Menganalisis makna simbol-simbol lisensi; praktik menelusuri perpustakaan aset grafis legal di internet. | Lembar kuis simbol lisensi CC |
| **Pertemuan 15** (2 JP) | Formula Kredit Atribusi TASL | Mampu menuliskan kredit sumber legal dengan rumus Title, Author, Source, License. | Latihan menuliskan kalimat atribusi resmi pada 3 gambar satwa langka yang diunduh dari Wikimedia Commons. | Rubrik kepatuhan atribusi TASL |
| **Pertemuan 16** (2 JP) | Proyek LKPD 2.1: Desain Infografis Cloud (1) | Memulai perancangan infografis digital isu sosial di aplikasi web desain. | Menyiapkan kanvas ukuran poster portrait, menyusun tata letak header, body 3 poin fakta, dan footer ajakan. | Progres draf kanvas desain |
| **Pertemuan 17** (2 JP) | Proyek LKPD 2.1: Desain Infografis Cloud (2) | Menyempurnakan tipografi, ikon vektor, dan memasang kotak atribusi TASL resmi. | Finishing karya poster digital; peer-review saling memberi masukan keterbacaan teks dan kontras warna antarteman. | Rubrik unjuk kerja LKPD 2.1 |
| **Pertemuan 18** (2 JP) | Evaluasi Formatif & Refleksi Bab 2 | Menguji ketuntasan literasi komunikasi visual dan etika hak cipta digital. | Mengerjakan Tes Formatif Bab 2 (10 PG & 5 Uraian HOTS); pameran galeri digital kelas dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 2 |

---

## BAB III: MENYELAMI KECERDASAN ARTIFISIAL GENERATIF (GENAI) & ETIKA KRITIS

### A. Gambaran Umum Pembelajaran Bab 3
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi dan Etika Kecerdasan Artifisial (LEKA)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu memahami konsep dasar dan mekanisme kerja Model Bahasa Besar (LLM) berbasis prediksi token probabilitas.
  2. Peserta didik mampu mengidentifikasi keterbatasan AI: fenomena halusinasi, bias algoritma, dan data kedaluwarsa.
  3. Peserta didik mampu menganalisis bahaya rekayasa Deepfake dan menerapkan teknik deteksi visual/audio.
* **Profil Pelajar Pancasila:** Bernalar Kritis (skeptis ilmiah terhadap konten digital) dan Berakhlak Mulia (integritas akademik).
* **Media Belajar:** Buku Siswa Bab 3, komputer dengan akses platform LLM edukatif terkurasi, video contoh kasus deepfake untuk analisis.

---

### B. Skema Alur Pembelajaran Bab 3 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 19** (2 JP) | Apersepsi Komik & Konsep GenAI | Memahami lompatan dari AI Klasifikasi ke AI Generatif pencipta konten baru. | Membaca komik Fajar & Rian; demonstrasi eksperimen meminta AI menghasilkan teks dan gambar pemandangan baru. | Tanya jawab pemantik |
| **Pertemuan 20** (2 JP) | Di Balik Dapur LLM: Next Token Prediction | Memahami mekanisme probabilitas statistik kata berikutnya pada model bahasa besar. | Simulasi manusia: guru mengucapkan kalimat pembuka dan murid berlomba menebak kata berikutnya yang paling mungkin secara logika bahasa. | Observasi nalar probabilitas |
| **Pertemuan 21** (2 JP) | Keterbatasan Kritis: Fenomena Halusinasi | Mampu melacak dan membuktikan kesalahan fakta fiktif pada teks keluaran AI. | Eksperimen Ayo Mencoba: menanyakan fakta sejarah pahlawan lokal kepada AI dan membandingkannya dengan ensiklopedia cetak. | Catatan temuan halusinasi teks |
| **Pertemuan 22** (2 JP) | Bias Algoritma & Ketimpangan Representasi | Memahami mengapa data latih internet yang tidak adil memicu bias pada AI. | Eksperimen prompt gambar profesi (dokter vs perawat); diskusi mengapa stereotip gender dan budaya dapat diperkuat oleh algoritma. | Lembar analisis bias visual |
| **Pertemuan 23** (2 JP) | Rekayasa Deepfake & Bahaya Penipuan Siber | Memahami cara kerja manipulasi Face Swap dan Voice Cloning. | Menganalisis studi kasus rekaman suara palsu permintaan transfer uang; membedah modus kejahatan siber berbasis AI. | Studi kasus penipuan digital |
| **Pertemuan 24** (2 JP) | 4 Jurus Detektor Siber Deepfake | Mampu mendeteksi anomali kedipan mata, sinkronisasi bibir, dan artefak blur pada video. | Latihan mengamati video uji perbandingan manusia asli vs rekayasa deepfake; murid mengisi checklist anomali fisik visual. | Lembar audit deteksi deepfake |
| **Pertemuan 25** (2 JP) | Proyek LKPD 3.1: Audit Integritas Teks AI | Menyusun laporan audit keakuratan data AI dan merumuskan protokol verifikasi 3-Cek. | Bekerja dalam kelompok memverifikasi 3 klaim sains/sejarah keluaran AI dengan sumber rujukan resmi perpustakaan. | Rubrik unjuk kerja LKPD 3.1 |
| **Pertemuan 26** (2 JP) | Evaluasi Formatif & Refleksi Bab 3 | Menguji ketuntasan pemahaman literasi dan etika kritis AI Generatif. | Mengerjakan Tes Formatif Bab 3 (10 PG & 5 Uraian HOTS); dialog refleksi kejujuran akademik dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 3 |

---

## BAB IV: INTERAKSI EFEKTIF DENGAN AI: SENI INPUT BERMAKNA & PROMPTING EDUKATIF

### A. Gambaran Umum Pembelajaran Bab 4
* **Alokasi Waktu:** 20 Jam Pelajaran (10 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Pemanfaatan dan Pengembangan Kecerdasan Artifisial (PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu memahami prinsip GIGO dan menerapkan formula Prompting 4 Pilar (Role, Task, Context, Format).
  2. Peserta didik mampu melakukan iterasi penyempurnaan prompt untuk mendukung pembelajaran mandiri.
  3. Peserta didik mampu menjaga kerahasiaan data pribadi saat berinteraksi dengan AI publik.
  4. Peserta didik mampu menyelesaikan Capstone Mini Proyek: Kampanye Digital Sekolah Berbantuan AI & Infografis.
* **Profil Pelajar Pancasila:** Mandiri, Kreatif, Bergotong Royong, dan Bernalar Kritis.
* **Media Belajar:** Buku Siswa Bab 4, laptop praktikum prompting, kertas plano kampanye mading sekolah.

---

### B. Skema Alur Pembelajaran Bab 4 (10 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 27** (2 JP) | Apersepsi Komik & Prinsip GIGO | Memahami bahwa kualitas jawaban AI ditentukan oleh ketajaman input instruksi manusia. | Membaca komik Fajar; eksperimen menguji prompt buruk *"Buatkan ide"* vs prompt spesifik di platform AI sekolah. | Catatan komparasi luaran AI |
| **Pertemuan 28** (2 JP) | Formula Prompt Standar 4 Pilar (R-T-C-F) | Memahami peranan Role, Task, Context, dan Format dalam mengunci ketepatan respons mesin. | Guru membedah formula R-T-C-F; murid menyusun naskah prompt 4 pilar untuk membantu belajar materi tata surya. | Lembar kerja formula R-T-C-F |
| **Pertemuan 29** (2 JP) | Simulasi Unplugged: Robot Literal | Memahami secara fisik mengapa instruksi ambigu berujung pada kegagalan eksekusi. | Permainan peran berpasangan: satu murid menjadi robot literal yang kaku dan satu murid menjadi prompter pemandu minum air. | Observasi keaktifan kelas |
| **Pertemuan 30** (2 JP) | Seni Iterasi Prompt: Dari Buruk ke Sempurna | Mampu melakukan penyempurnaan perintah secara dialogis bertahap (*refinement*). | Praktikum mengubah prompt versi 1 (buruk) -> versi 2 (sedang) -> versi 3 (sempurna) pada kasus ide kegiatan OSIS. | Catatan riwayat iterasi prompt |
| **Pertemuan 31** (2 JP) | Batasan Kerahasiaan Data Saat Prompting | Memahami aturan larangan memasukkan NIK, password, nomor kontak, atau alamat rumah ke AI. | Menganalisis studi kasus kebocoran data privasi; membuat poster mini *"3 Aturan Emas Privasi Digital Siswa"*. | Lembar audit kepatuhan privasi |
| **Pertemuan 32** (2 JP) | Capstone Tahap 1: Riset AI & Verifikasi | Memulai riset ide kampanye anti-bullying / peduli sampah berbantuan prompt 4 pilar. | Kelompok merumuskan prompt terstruktur, memfilter ide AI, dan memverifikasi data fakta dengan buku resmi. | Lembar progres draf kampanye |
| **Pertemuan 33** (2 JP) | Capstone Tahap 2: Desain Infografis CRAP | Memproduksi poster digital kampanye menerapkan prinsip kontras, repetisi, perataan, dan kedekatan. | Mengolah naskah ide terpilih ke dalam layout poster di aplikasi desain; menyematkan kredit atribusi Creative Commons TASL. | Cek estetika poster digital |
| **Pertemuan 34** (2 JP) | Capstone Tahap 3: Publikasi Mading & Pameran | Menempelkan karya di mading koridor sekolah dan melakukan presentasi kelompok di kelas. | Pameran gelar karya mini kelas VII; saling memberikan bintang apresiasi dan umpan balik antar kelompok. | Rubrik unjuk kerja LKPD 4.1 |
| **Pertemuan 35** (2 JP) | Evaluasi Formatif Bab 4 & Refleksi Etika | Menguji pemahaman prompting terstruktur dan filosofi Human-Centered AI. | Mengerjakan Tes Formatif Bab 4 (10 PG & 5 Uraian HOTS); dialog refleksi *"Manusia adalah Pengemudi, AI adalah Kendaraan"*. | Skor Tes Formatif Bab 4 |
| **Pertemuan 36** (2 JP) | Evaluasi Sumatif Akhir Tahun Fase D | Menguji ketuntasan kompetensi menyeluruh Fase D Kelas VII (Semester 1 & 2). | Mengerjakan Evaluasi Sumatif Akhir Tahun (25 Soal PG HOTS & 5 Kasus Terpadu); penyerahan Medali Emas Koder Kelas VII. | Nilai Sumatif Akhir Tahun |
"""

GURU_BAGIAN_3_SMP7 = """# BAGIAN 3: PANDUAN ASESMEN SUMATIF & PELAPORAN HASIL BELAJAR

### A. Rubrik Penilaian Portofolio Capstone Mini Proyek Kelas 7

| Dimensi Penilaian | Kriteria Skor 4 (Sangat Baik) | Kriteria Skor 3 (Baik) | Kriteria Skor 2 (Cukup) | Kriteria Skor 1 (Perlu Bimbingan) |
|:---|:---|:---|:---|:---|
| **1. Formulasi Prompting 4 Pilar (25%)** | Naskah prompt memuat Role, Task, Context, dan Format secara sangat tajam, spesifik, dan menghasilkan luaran AI yang sangat bermutu tinggi. | Memuat 4 pilar, namun batasan konteks atau instruksi format penyajian masih agak umum. | Hanya memuat 2 pilar (misal hanya Task dan Format) tanpa menetapkan Role dan Context. | Prompt ditulis sangat pendek dan asal-asalan tanpa struktur pilar sama sekali. |
| **2. Verifikasi Fakta Manusia (25%)** | Melakukan audit kritis silang fakta dengan sumber rujukan resmi; sukses menyaring seluruh potensi halusinasi AI secara mandiri. | Melakukan verifikasi fakta, namun masih ada 1 klaim kecil fiktif dari AI yang lolos tanpa diperiksa. | Hanya mencocokkan sebagian data tanpa mencantumkan bukti sumber resmi pembanding. | Menelan mentah-mentah seluruh naskah keluaran AI tanpa proses verifikasi fakta sama sekali. |
| **3. Estetika Desain Infografis (30%)** | Menerapkan prinsip C.R.A.P secara sempurna; kontras tajam, palet warna konsisten, ruang kosong lega, dan atribusi TASL lengkap. | Desain rapi dan terbaca jelas, namun penerapan salah satu prinsip (misal perataan garis) masih kurang konsisten. | Desain tampak padat dan sesak oleh teks; kontras warna kurang kuat dan atribusi tidak lengkap. | Desain sangat berantakan, tidak terbaca, dan melanggar hak cipta dengan menjiplak karya orang lain. |
| **4. Kolaborasi & Etika Human-Centered (20%)** | Seluruh anggota berbagi peran aktif; menunjukkan integritas tinggi, kepedulian sosial, dan pemahaman bahwa manusia adalah penanggung jawab akhir. | Pembagian peran berjalan baik; presentasi jelas, meskipun didominasi oleh salah satu anggota tim saja. | Kerja sama tim kurang kompak; pemahaman etika tanggung jawab teknologi masih perlu bimbingan. | Anggota tim saling menyalahkan saat presentasi dan mengabaikan nilai etika kejujuran akademik. |

---

### B. Panduan Pengolahan Nilai Akhir Rapor KKA Fase D Kelas VII
Nilai Akhir Rapor Kurikulum Merdeka / Nasional dihitung menggunakan formula pembobotan proporsional:

**Formula Pembobotan Nilai Akhir:**  
*Nilai Akhir (NA) = [(2 x Rata-rata Formatif) + (2 x Nilai Capstone Mini Proyek) + (1 x Nilai Sumatif Akhir Tahun)] / 5*

**Kategori Ketercapaian Kompetensi Belajar:**
* **85 - 100 (Sangat Mahir):** Murid telah menuntaskan seluruh capaian pembelajaran Fase D Kelas VII dengan sangat unggul, mampu berpikir komputasional kritis, terampil mendesain komunikasi visual beradab, dan bijak berinteraksi dengan AI generatif. Sangat siap melangkah ke Kelas VIII.
* **70 - 84 (Mahir):** Murid telah menguasai konsep pengelolaan data sosial, prinsip desain CRAP, dan teknik prompting terstruktur dengan baik, memerlukan sedikit penguatan pada kasus komparasi fakta kompleks.
* **60 - 69 (Cukup):** Murid memahami konsep dasar, namun masih membutuhkan bimbingan bertahap saat menyusun flowchart ISO atau membedakan bias dan halusinasi AI.
* **< 60 (Perlu Bimbingan Khusus):** Murid memerlukan bimbingan intensif dan remedial konsep berpikir komputasional mendasar.

---

### C. Profil Penulis & Fasilitator ToT Nasional

[[IMAGE: foto_penulis.jpg | Foto Penulis: Gede Erik Aktama, S.Pd., M.Pd.]]

**Gede Erik Aktama, S.Pd., M.Pd.**  
*Fasilitator Nasional Bimbingan Teknis & Training of Trainers (ToT) Koding dan Kecerdasan Artifisial Kemendikdasmen RI*  
*Dosen Lektor & Ketua Program Studi S1 Sistem Komputer, Fakultas Teknik dan Informatika, Universitas Parna Raya (UNIPAR) Manado*

Penulis adalah akademisi dan praktisi pendidikan teknologi informasi yang berdomisili di Kota Manado, Sulawesi Utara. Menyelesaikan pendidikan Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika dan gelar Magister Pendidikan (M.Pd.) pada Program Studi Pendidikan Teknologi dan Kejuruan dari Universitas Pendidikan Ganesha (UNDIKSHA), Singaraja. Saat ini, penulis aktif mengemban jabatan fungsional akademik **Lektor** (SK Mendiktisaintek RI No. 0044/LL16/KP.07/2025) serta menjabat sebagai Ketua Program Studi S1 Sistem Komputer di Universitas Parna Raya Manado.

Sebagai akademisi yang mendedikasikan diri pada transformasi digital pendidikan dasar dan menengah di Indonesia, penulis dipercaya oleh Direktorat Guru Pendidikan Dasar, Direktorat Jenderal Guru dan Tenaga Kependidikan, Kementerian Pendidikan Dasar dan Menengah RI sebagai **Fasilitator Nasional** dalam Bimbingan Teknis dan *Training of Trainers* (ToT) Pembelajaran Koding dan Kecerdasan Artifisial (KKA) untuk jenjang SD, SMP, SMA, dan SMK.

Penulis memiliki kepakaran riset dalam bidang *Computational Thinking in Secondary Education*, *Artificial Intelligence for K-12*, *Educational Robotics*, dan Pengembangan Perangkat Ajar Interaktif berbasis *Deep Learning*.

*Korespondensi & Diskusi Pedagogis Guru:* erikaktama@unipar.ac.id
"""

full_guru_smp7_md = "\n\n".join([
    GURU_FRONT_MATTER_SMP7,
    GURU_BAGIAN_1_SMP7,
    GURU_BAGIAN_2_SMP7,
    GURU_BAGIAN_3_SMP7,
    DAFTAR_PUSTAKA_RESMI_SMP7
])
