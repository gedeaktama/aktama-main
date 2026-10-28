# -*- coding: utf-8 -*-
"""
Naskah Lengkap Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SD/MI Kelas VI (Fase C)
Standar: Pusat Perbukuan Kemendikdasmen RI / Deep Learning Approach (Mindful, Meaningful, Joyful)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

from sd6_naskah_frontmatter import DAFTAR_PUSTAKA_RESMI_SD6

GURU_FRONT_MATTER_SD6 = """# BUKU PANDUAN GURU
## KODING DAN KECERDASAN ARTIFISIAL UNTUK SD/MI KELAS VI
### Mata Pelajaran Pilihan — Fase C (Tingkat Akhir SD)

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
Judul Buku: Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SD/MI Kelas VI (Fase C)  
Penulis: Gede Erik Aktama, S.Pd., M.Pd.  
Penyunting / Editor Naskah: Tim Fasilitator Dikdasmen Kemendikdasmen  
Tata Letak & Tipografi: Format Standar Buku Ajar UNESCO (15,5 cm x 23,0 cm)  
Desain Sampul & Ilustrasi: Tim Desain Edukatif Digital Aktama  
Penerbit: Pusat Perbukuan Kemendikdasmen RI  
Hak Cipta Dilindungi Undang-Undang: Berdasarkan Permendikdasmen No. 13 Tahun 2025 tentang Kurikulum pada Pendidikan Dasar dan Menengah.  

---

## KATA PENGANTAR KEMENDIKDASMEN
Puji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa atas terbitnya **Buku Panduan Guru Koding dan Kecerdasan Artifisial untuk SD/MI Kelas VI (Fase C)**. Buku panduan operasional ini dihadirkan untuk mendampingi bapak/ibu guru di seluruh Indonesia dalam mengimplementasikan pembelajaran KKA secara bermakna, kontekstual, dan menggembirakan.

Kelas VI adalah fase penuntasan (*capstone phase*) jenjang Sekolah Dasar. Pada fase ini, murid tidak lagi hanya mempelajari konsep secara terpisah-pisah, melainkan mengintegrasikannya dalam sebuah karya inovasi kolaboratif nyata (*Capstone Project*) yang solutif bagi lingkungan sekolah dan masyarakat sekitar.

Buku Panduan Guru ini menyajikan skema rinci 32 kali pertemuan tahunan (total 64 Jam Pelajaran), panduan diferensiasi pembelajaran, strategi asesmen autentik, rubrik evaluasi unjuk kerja, serta petunjuk penyelenggaraan Gelar Karya (*Showcase Day*).

Apresiasi setinggi-tingginya kami sampaikan kepada Saudara **Gede Erik Aktama, S.Pd., M.Pd.** atas kontribusi keilmuan dan dedikasinya dalam menyusun panduan pedagogis yang aplikatif ini. Semoga buku ini menjadi kompas pemandu yang menyalakan semangat para guru dalam mendidik tunas-tunas muda inovator bangsa.

Jakarta, 2025  
**Kementerian Pendidikan Dasar dan Menengah Republik Indonesia**

---

## PRAKATA PENULIS
Bapak dan Ibu Guru pejuang pendidikan dasar di seluruh penjuru Tanah Air yang saya banggakan,

Salam hangat dan salam inovasi!

Mengajar murid kelas 6 Sekolah Dasar dalam mata pelajaran Koding dan Kecerdasan Artifisial merupakan sebuah kehormatan sekaligus peluang emas yang sangat berharga. Murid-murid kelas 6 berada pada masa transisi kognitif yang sangat dinamis: daya nalar logis mereka mulai matang, rasa ingin tahu mereka tinggi, dan mereka memiliki kerinduan besar untuk diakui melalui karya-karya nyata yang dapat dibanggakan kepada orang tua dan teman sebayanya.

Buku Panduan Guru ini dirancang dengan pendekatan **Pembelajaran Mendalam (*Deep Learning*)** yang bertumpu pada tiga pilar:
1. **Berkesadaran (*Mindful Learning*):** Mengajak murid menyadari mengapa mereka belajar logika, bagaimana teknologi memengaruhi perasaan sesama, serta menumbuhkan kebiasaan reflektif dan etika keadaban digital.
2. **Bermakna (*Meaningful Learning*):** Menghubungkan setiap konsep komputasi (percabangan, loop, variabel, sensor, dan AI) dengan persoalan nyata di sekolah dan kearifan lokal Nusantara, bukan sekadar hafalan rumus sintaksis.
3. **Menggembirakan (*Joyful Learning*):** Menciptakan suasana belajar yang riang tanpa rasa takut salah, di mana kesalahan kode (*bug*) diposisikan sebagai sahabat terbaik yang melatih kegigihan mental para murid.

Buku ini telah memuat skema 8 pertemuan untuk setiap bab secara terperinci, strategi penanganan kelas inklusi, panduan diferensiasi untuk anak yang membutuhkan bimbingan khusus maupun anak berbakat (*gifted*), instrumen asesmen formatif dan sumatif terstandar, serta tata laksana Gelar Karya Pameran Kelulusan Fase C.

Semoga buku panduan ini mampu meringankan langkah Bapak dan Ibu Guru dalam memandu murid-murid tercinta menjadi pribadi yang cerdas, kreatif, berakhlak mulia, dan siap melangkah tegak ke jenjang SMP. Selamat mendidik dan selamat menginspirasi tunas peradaban bangsa!

Manado, 2025  
**Gede Erik Aktama, S.Pd., M.Pd.**  
*(Fasilitator Nasional KKA Kemendikdasmen RI)*  
*(Dosen Lektor & Kaprodi Sistem Komputer, Universitas Parna Raya)*

---

## DAFTAR ISI PANDUAN GURU
Bagian 1: Petunjuk Umum Pembelajaran KKA SD Kelas 6 Fase C
  A. Hakikat Mata Pelajaran KKA dan Profil Kelulusan Fase C
  B. Karakteristik Murid Kelas 6 SD dan Pendekatan Pembelajaran Mendalam
  C. Capaian Pembelajaran & Alur Tujuan Pembelajaran (ATP) 64 JP
  D. Strategi Pembelajaran Mendalam: Mindful, Meaningful, Joyful
  E. Skema Penilaian Autentik & Portofolio Fase C
  F. Manajemen Laboratorium Komputer dan Pembelajaran Unplugged

Bagian 2: Panduan Khusus Pembelajaran Bab 1 - Bab 4
  Bab I: Logika Bersyarat, Perulangan, & Pembuatan Game Kuis Edukasi (16 JP)
    A. Gambaran Umum Pembelajaran Bab 1
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Kinerja Game Scratch
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab II: Memproduksi & Membagikan Konten Digital Berkeadaban (16 JP)
    A. Gambaran Umum Pembelajaran Bab 2
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Komik Strip Atribusi
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab III: Menjelajahi Sensor dan Otomasi Perangkat Cerdas (16 JP)
    A. Gambaran Umum Pembelajaran Bab 3
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Poster Inovasi Sekolah Cerdas
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid
  Bab IV: Kolaborasi Proyek Terpadu (Capstone Project Fase C) (16 JP)
    A. Gambaran Umum Pembelajaran Bab 4
    B. Skema Alur Pembelajaran 8 Pertemuan @ 2 JP
    C. Langkah-Langkah Pembelajaran Mendalam
    D. Panduan Diferensiasi (Remedial & Pengayaan)
    E. Panduan Asesmen & Rubrik Gelar Karya (Showcase Day)
    F. Kunci Jawaban Buku Siswa & Catatan Pedagogis
    G. Panduan Interaksi dengan Orang Tua Murid

Bagian 3: Panduan Asesmen Sumatif Kelulusan Fase C & Pelaporan Hasil Belajar
  A. Rubrik Penilaian Komprehensif Capstone Project
  B. Kunci Jawaban & Pembahasan Evaluasi Sumatif Akhir Tahun
  C. Panduan Konversi Nilai ke Rapor Kurikulum Nasional

Bagian Akhir Buku Guru: Glosarium, Daftar Pustaka Resmi, & Profil Penulis
"""

GURU_BAGIAN_1_SD6 = """# BAGIAN 1: PETUNJUK UMUM PEMBELAJARAN KKA KELAS 6 FASE C

### A. Hakikat Mata Pelajaran KKA dan Profil Kelulusan Fase C
Mata pelajaran pilihan Koding dan Kecerdasan Artifisial (KKA) pada Fase C (Kelas V dan VI SD/MI) dirancang bukan untuk mencetak programmer profesional instan, melainkan untuk membangun disposisi bernalar kritis (*computational thinker*), keadaban dalam berkomunikasi digital (*digital citizenship*), pemahaman dasar cara kerja teknologi cerdas (*AI literacy*), serta kebiasaan memecahkan masalah kompleks secara terstruktur dan mandiri.

Pada akhir Fase C, murid diharapkan memiliki profil kelulusan:
1. Mampu merancang algoritma sekuensial dan percabangan berkondisi (*If-Then-Else*) serta perulangan (*Loops*) pada lingkungan koding visual blok.
2. Mampu membuat dan mengelola variabel untuk mencatat dinamika data (skor, timer, status).
3. Mampu memproduksi karya multimedia digital yang menghormati hak cipta, memahami lisensi Creative Commons, dan menjauhi perilaku perundungan siber (*cyberbullying*).
4. Mampu memahami cara kerja sensor sebagai indera buatan komputer serta mengidentifikasi pemanfaatan AI ramah disabilitas (*AI for Inclusivity*).
5. Mampu berkolaborasi dalam tim merancang, menguji, memperbaiki (*debugging*), dan memamerkan sebuah karya puncak (*Capstone Project*) yang solutif bagi sekolah.

---

### B. Karakteristik Murid Kelas 6 SD dan Pendekatan Pembelajaran Mendalam
Murid kelas 6 SD (berusia rata-rata 11-12 tahun) berada pada peralihan dari tahap operasional konkret menuju tahap operasional formal menurut teori perkembangan kognitif Piaget. Karakteristik utamanya meliputi:
* Mampu memahami konsep abstrak bersyarat jika diawali dengan analogi konkret (seperti mengaitkan percabangan koding dengan pemilihan payung saat hujan).
* Mengembangkan kesadaran sosial yang tinggi terhadap keadilan (*fair play*), aturan kelompok, dan penerimaan teman sebaya.
* Rentan terhadap pengaruh dinamika media sosial di ponsel, sehingga membutuhkan pendampingan literasi digital yang kuat dan empatik.
* Memiliki rasa bangga yang luar biasa saat karyanya diapresiasi oleh komunitas sekolah dan orang tua.

Pendekatan **Pembelajaran Mendalam (*Deep Learning*)** diimplementasikan melalui:
* **Mindful:** Setiap pertemuan diawali dengan hening sejenak (*Mindful Moment*) untuk memusatkan perhatian, menyadari tujuan belajar, dan merefleksikan nilai moral.
* **Meaningful:** Setiap tugas dikaitkan dengan konteks nyata di lingkungan sekolah atau kebudayaan Nusantara.
* **Joyful:** Menggunakan simulasi permainan gerak tubuh (*unplugged games*), tantangan kartu logika, dan pameran interaktif yang menyenangkan.

---

### C. Alokasi Waktu dan Skema Kurikulum Tahunan (64 JP)
Mata pelajaran KKA dialokasikan 2 Jam Pelajaran (JP) @ 35 menit per minggu. Dalam satu tahun ajaran (Semester 1 dan 2) dialokasikan total 32 minggu efektif pembelajaran (64 JP) yang terdistribusi ke dalam 4 bab utama:
* **Semester 1 (32 JP):**
  * Bab 1: Logika Bersyarat, Perulangan, & Pembuatan Game Kuis Edukasi (16 JP - 8 Pertemuan)
  * Bab 2: Memproduksi & Membagikan Konten Digital Berkeadaban (16 JP - 8 Pertemuan)
* **Semester 2 (32 JP):**
  * Bab 3: Menjelajahi Sensor dan Otomasi Perangkat Cerdas (16 JP - 8 Pertemuan)
  * Bab 4: Kolaborasi Proyek Terpadu (Capstone Project Fase C) (16 JP - 8 Pertemuan)

---

### D. Penilaian Autentik & Manajemen Sarana Belajar
Penilaian KKA mengedepankan **Asesmen Autentik** yang menilai proses dan kinerja nyata, bukan sekadar tes tertulis hafalan. Komponen penilaian meliputi:
1. **Asesmen Formatif Selama Pembelajaran (Bobot 40%):** Keaktifan diskusi, lembar unjuk kerja LKPD, dan catatan jurnal refleksi murid.
2. **Asesmen Kinerja Proyek / Capstone (Bobot 40%):** Kualitas logika koding Scratch, kelancaran fungsi alat prototipe, estetika poster, dan kekompakan tim saat pameran.
3. **Asesmen Sumatif Akhir Tahun (Bobot 20%):** Uji pemahaman terstandar berbasis soal kasus HOTS.

Bagi sekolah dengan keterbatasan fasilitas komputer atau jaringan internet:
* Seluruh konsep dasar dapat diajarkan dengan metode **Unplugged** (permainan fisik di lantai kelas, kartu logika kertas, dan simulasi gerak peran).
* Pembelajaran komputer dapat menggunakan pola bergantian (*sharing 2-3 siswa per komputer*), di mana murid berbagi peran sebagai arsitek logika dan pelaksana ketik.
"""

GURU_BAGIAN_2_SD6 = """# BAGIAN 2: PANDUAN KHUSUS PEMBELAJARAN BAB 1 - BAB 4

## BAB I: LOGIKA BERSYARAT, PERULANGAN, & PEMBUATAN GAME KUIS EDUKASI

### A. Gambaran Umum Pembelajaran Bab 1
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu merancang algoritma percabangan kondisi (*If-Then* dan *If-Then-Else*) pada pemrograman visual Scratch 3.0.
  2. Peserta didik mampu menerapkan perulangan (*Loops: repeat dan forever*) dan variabel sederhana untuk mencatat skor permainan.
  3. Peserta didik mampu merancang game kuis edukatif berbasis sains atau budaya Nusantara yang interaktif.
* **Profil Pelajar Pancasila:** Bernalar Kritis (menganalisis cabang kondisi), Kreatif (merancang alur kuis), dan Berakhlak Mulia (menjunjung tinggi sportivitas & menolak jalan pintas curang).
* **Media & Sumber Belajar:** Buku Siswa Bab 1, kartu kondisi kuning/hijau/merah untuk unplugged, komputer/laptop dengan Scratch 3.0 (offline/online), proyektor kelas.

---

### B. Skema Alur Pembelajaran Bab 1 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 1** (2 JP) | Apersepsi Komik & Logika If-Then | Memahami arti pengambilan keputusan bersyarat dalam keseharian. | Membaca komik apersepsi Erik & Kibo, tanya jawab pemantik tentang aturan rumah tangga, bermain tebak kondisi sederhana. | Observasi keaktifan nalar kritis |
| **Pertemuan 2** (2 JP) | Percabangan Dua Arah (If-Then-Else) | Mampu merancang alur keputusan dua cabang pada flowchart. | Guru memodelkan diagram alur percabangan; murid menggambar alur flowchart logika kuis di kertas berpetak. | Lembar kerja alur flowchart |
| **Pertemuan 3** (2 JP) | Perulangan Efisien (Repeat vs Forever) | Memahami perbedaan perulangan terhitung dan perulangan tanpa henti. | Simulasi fisik gerakan melompat 5 kali vs berjalan terus; demonstrasi blok `repeat (5)` dan `forever` di Scratch. | Latihan klasifikasi blok loop |
| **Pertemuan 4** (2 JP) | Konsep Variabel: Kotak Ajaib | Memahami variabel sebagai penyimpan angka skor dan nyawa. | Analogi toples kue dapur; murid membuat variabel baru `Skor` dan `Nyawa` di antarmuka Scratch dan menguji tombol penambah skor. | Praktik inisialisasi variabel di Scratch |
| **Pertemuan 5** (2 JP) | Praktik Terbimbing: Blok Logika Kuis | Mampu menggabungkan blok `ask`, `answer`, dan `if-then-else`. | Praktikum menyusun 1 soal kuis Scratch bersama guru: mengevaluasi input jawaban dan memberi respon audio kemenangan/kalah. | Cek fungsi logika blok kode murid |
| **Pertemuan 6** (2 JP) | Proyek LKPD 1.1: Kuis Pahlawan Nusantara | Mampu merancang minimal 3 soal kuis sejarah Indonesia. | Bekerja dalam kelompok merangkai latar panggung, karakter sprite, 3 pertanyaan pahlawan nasional, dan variabel skor/nyawa. | Rubrik unjuk kerja LKPD 1.1 |
| **Pertemuan 7** (2 JP) | Debugging & Penyempurnaan Game | Mampu menemukan dan memperbaiki kesalahan logika pada game kuis. | Uji coba saling silang antar meja (*peer testing*); melacak bug penambahan skor ganda dan memperbaiki alur program. | Catatan logbook pelacak bug |
| **Pertemuan 8** (2 JP) | Evaluasi Formatif & Refleksi Bab 1 | Menguji ketuntasan pemahaman materi Bab 1. | Mengerjakan Tes Formatif 10 Soal Pilihan Ganda & 5 Uraian HOTS; mengisi Jurnal Refleksiku dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 1 & Jurnal |

---

### C. Langkah-Langkah Pembelajaran Mendalam (Deep Learning)
1. **Fase Memahami (*Mindful Learning*):** Guru mengawali dengan pertanyaan pemantik: *"Anak-anak, apa yang terjadi jika lampu lalu lintas di perempatan jalan mati dan semua pengendara jalan terus tanpa aturan percabangan?"*. Murid diajak menyadari bahwa keteraturan logika melindungi ketertiban dunia.
2. **Fase Mengaplikasikan (*Meaningful & Joyful Learning*):** Pembelajaran di laboratorium dibuat dinamis. Guru memutar efek suara *Cheer* saat murid berhasil menyusun balok `if-then-else`. Guru menekankan bahwa pesan salah (*Oops*) bukanlah hukuman, melainkan umpan balik belajar.
3. **Fase Merefleksi (*Meaningful Consolidation*):** Murid mendiskusikan nilai kejujuran (*Fair Play*): mengapa seorang koder hebat tidak boleh menyusupkan jalan pintas curang ke dalam kreasinya.

---

### D. Panduan Diferensiasi & Remedial / Pengayaan
* **Murid Membutuhkan Bimbingan (Remedial):**
  * Berikan kartu panduan visual berisi cetakan gambar blok Scratch yang sudah berurutan untuk ditiru (*scaffolding template*).
  * Batasi proyek kuis menjadi 2 pertanyaan dengan jawaban angka sederhana (misalnya perkalian dasar).
* **Murid Mahir Cepat (Pengayaan):**
  * Tantang murid menambahkan variabel `Waktu` (*Timer*) yang menghitung mundur dari 30 ke 0 menggunakan blok `repeat until <(Waktu) = [0]>`.
  * Tambahkan sistem level: jika skor mencapai 50, latar belakang panggung otomatis berganti ke babak bonus!

---

### E. Rubrik Asesmen Unjuk Kerja Game Kuis Scratch Bab 1

| Aspek Penilaian | Sangat Baik (Skor 4) | Baik (Skor 3) | Cukup (Skor 2) | Perlu Bimbingan (Skor 1) |
|:---|:---|:---|:---|:---|
| **Struktur Percabangan** | Logika `if-then-else` berjalan sempurna pada semua soal dengan respon teks & audio yang tepat. | Logika percabangan tepat, namun efek suara belum sinkron. | Menggunakan `if-then` satu arah saja, belum ada cabang penanganan jawaban salah. | Blok percabangan belum terangkai dengan benar sehingga kuis macet. |
| **Manajemen Variabel** | Variabel `Skor` dan `Nyawa` diinisialisasi bersih di awal dan bertambah/berkurang tepat. | Variabel skor berfungsi, namun belum diinisialisasi ke 0 di awal bendera hijau. | Hanya ada 1 variabel skor tanpa nyawa. | Belum berhasil membuat variabel baru di Scratch. |
| **Penerapan Loop** | Menggunakan blok `repeat` terhitung secara efisien untuk mengulang pertanyaan. | Pertanyaan berulang namun kodenya diduplikasi panjang tanpa loop. | Loop digunakan namun jumlah perulangan tidak sesuai. | Belum memahami fungsi balok perulangan. |
| **Kemandirian & Sportivitas** | Menunjukkan kegigihan memperbaiki bug secara mandiri dan menolak cheat code. | Memperbaiki bug dengan sedikit bantuan guru dan bermain adil. | Masih sering bergantung pada teman saat ada kode eror. | Tergoda memasukkan skor instan tanpa mekanisme jawaban kuis. |

---

## BAB II: MEMPRODUKSI & MEMBAGIKAN KONTEN DIGITAL BERKEADABAN

### A. Gambaran Umum Pembelajaran Bab 2
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi Digital (LD)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu memproduksi konten digital perpaduan teks, suara, dan gambar bertema kebaikan sosial dan pelestarian lingkungan.
  2. Peserta didik mampu memahami prinsip hak cipta, lisensi terbuka Creative Commons, dan etika atribusi karya.
  3. Peserta didik mampu menyaring informasi (*fact-checking*) dan menghindari perundungan siber (*cyberbullying*).
* **Profil Pelajar Pancasila:** Berkebinekaan Global (menghargai karya cipta dunia), Berakhlak Mulia (menjaga tutur kata santun di internet), dan Mandiri.
* **Media & Sumber Belajar:** Buku Siswa Bab 2, mikrofon mini/ponsel untuk merekam suara, aplikasi Canva / Google Slides / Scratch, contoh lembar kasus hoaks.

---

### B. Skema Alur Pembelajaran Bab 2 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 9** (2 JP) | Apersepsi Komik & Memadukan Media | Memahami 3 pilar media digital: teks, suara, dan visual. | Membaca komik Siti & Kibo; praktik merekam suara dialog fabel menggunakan mikrofon mini dengan intonasi ekspresif. | Catatan kualitas rekaman audio |
| **Pertemuan 10** (2 JP) | Hak Cipta & Lisensi Creative Commons | Memahami perbedaan hak cipta penuh dan lisensi terbuka CC. | Membedah simbol lisensi (©, CC-BY, CC-BY-SA, CC-NC); simulasi mencari foto di situs perpustakaan gambar aman. | Lembar identifikasi simbol CC |
| **Pertemuan 11** (2 JP) | Menuliskan Atribusi Karya yang Sah | Mampu menuliskan atribusi sumber dengan rumus TASL. | Latihan praktik menulis kalimat atribusi untuk 3 gambar budaya Nusantara yang diunduh dari Wikimedia Commons. | Rubrik penulisan atribusi resmi |
| **Pertemuan 12** (2 JP) | Saring Sebelum Sebar: Atasi Hoaks | Mampu membedakan berita fakta dan pesan bohong. | Analisis studi kasus pesan berantai berhadiah kuota; murid menerapkan 4 langkah detektif siber melacak keaslian berita. | Lembar kerja bedah kasus hoaks |
| **Pertemuan 13** (2 JP) | Keadaban Digital & Stop Cyberbullying | Memahami pedoman komunikasi T.H.I.N.K. di dunia maya. | Diskusi reflektif tentang dampak komentar jahat bagi perasaan teman; bermain peran menjadi pembela kebaikan (*Upstander*). | Observasi empati komunikasi |
| **Pertemuan 14** (2 JP) | Proyek LKPD 2.1: Komik Strip Digital | Mampu menyusun komik strip 4 panel bertema lingkungan. | Bekerja dalam kelompok memadukan gambar foto/lukisan, teks dialog, dan pesan moral kebersihan bumi di aplikasi presentasi/Scratch. | Lembar progres draf komik |
| **Pertemuan 15** (2 JP) | Penyelesaian Komik & Pemasangan Atribusi | Melengkapi karya dengan kotak atribusi lisensi resmi. | Murid menata tata letak panel komik, memasang kalimat atribusi di bagian bawah karya, dan melakukan tinjauan teman sejawat. | Rubrik unjuk kerja LKPD 2.1 |
| **Pertemuan 16** (2 JP) | Evaluasi Formatif & Refleksi Bab 2 | Menguji ketuntasan pemahaman literasi dan etika digital. | Mengerjakan Tes Formatif Bab 2 (10 PG & 5 Uraian HOTS); pameran komik strip di mading kelas dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 2 |

---

## BAB III: MENJELAJAHI SENSOR DAN OTOMASI PERANGKAT CERDAS

### A. Gambaran Umum Pembelajaran Bab 3
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi dan Etika Kecerdasan Artifisial (LEKA) & Pemanfaatan KA (PPKA)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu memahami cara sensor menangkap rangsangan fisik (cahaya, jarak, gerak) menjadi data digital bagi komputer.
  2. Peserta didik mampu menjelaskan siklus kerja sistem otomatis cerdas (Input -> Proses -> Output).
  3. Peserta didik mampu mengidentifikasi pemanfaatan AI ramah disabilitas (*AI for Inclusivity*) dan menganalisis pentingnya tombol darurat kendali manusia (*Human Oversight*).
* **Profil Pelajar Pancasila:** Bernalar Kritis, Bergotong Royong, dan Berakhlak Mulia (empati terhadap sahabat penyandang disabilitas).
* **Media & Sumber Belajar:** Buku Siswa Bab 3, selotip kertas untuk membuat labirin mobil otonom di lantai, kain penutup mata, kit sensor sederhana (jika tersedia), kertas manila untuk poster.

---

### B. Skema Alur Pembelajaran Bab 3 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 17** (2 JP) | Apersepsi Komik & Pengantar Sensor | Memahami sensor sebagai jendela indera buatan komputer. | Membaca komik Erik & Kibo; demonstrasi mengamati cara kerja keran otomatis sekolah dan sensor cahaya ponsel guru. | Tanya jawab pemantik lisan |
| **Pertemuan 18** (2 JP) | 4 Sensor Cerdas di Sekitar Kita | Memahami fungsi sensor LDR, ultrasonik, PIR, dan kamera AI. | Menjodohkan gambar sensor dengan fungsinya; menganalisis analogi sensor ultrasonik dengan sonar kelelawar. | Lembar kerja menjodohkan sensor |
| **Pertemuan 19** (2 JP) | Siklus Kerja Sistem Otomatis Cerdas | Memahami alur Input (Sensor) -> Proses (AI) -> Output (Aktuator). | Membedah cara kerja palang pintu parkir otomatis; murid menuliskan alur siklus sistem lampu jalan pintar. | Diagram siklus otomatisasi |
| **Pertemuan 20** (2 JP) | Simulasi Unplugged: Mobil Otonom | Mempraktikkan navigasi rute berbasis data sensor rintangan. | Aktivitas labirin lantai kelas: murid berperan sebagai mobil mata tertutup, sensor ultrasonik, dan prosesor navigasi jalan. | Observasi kinerja kelompok |
| **Pertemuan 21** (2 JP) | AI untuk Inklusivitas (AI for Good) | Menumbuhkan empati teknologi bagi sahabat penyandang disabilitas. | Mengamati video kacamata cerdas tunanetra dan aplikasi teks tunarungu; dialog tentang pentingnya teknologi ramah semua kalangan. | Lembar refleksi empati inklusi |
| **Pertemuan 22** (2 JP) | Etika Kendali Manusia & Emergency Stop | Memahami mengapa tombol darurat wajib ada pada sistem robot. | Diskusi etika: manusia adalah penanggung jawab keselamatan tertinggi; simulasi menekan tombol darurat saat mesin bermasalah. | Studi kasus keselamatan robotik |
| **Pertemuan 23** (2 JP) | Proyek LKPD 3.1: Poster Sekolah Cerdas | Merancang ide konseptual alat pintar berbasis sensor di sekolah. | Bekerja dalam kelompok menggambar poster konseptual alat pintar ramah disabilitas / hemat energi di kertas manila. | Rubrik rancangan poster LKPD 3.1 |
| **Pertemuan 24** (2 JP) | Evaluasi Formatif & Refleksi Bab 3 | Menguji pemahaman menyeluruh tentang sensor dan sistem otomatis. | Mengerjakan Tes Formatif Bab 3 (10 PG & 5 Uraian HOTS); mengisi jurnal refleksi dan penganugerahan Medali Koder. | Skor Tes Formatif Bab 3 |

---

## BAB IV: KOLABORASI PROYEK TERPADU (CAPSTONE PROJECT FASE C)

### A. Gambaran Umum Pembelajaran Bab 4
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Kali Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Pemanfaatan KA (PPKA) & Berpikir Komputasional (BK)
* **Tujuan Pembelajaran (TP):**
  1. Peserta didik mampu merumuskan masalah nyata lingkungan sekolah menggunakan metode dekomposisi dan empati.
  2. Peserta didik mampu merancang dan menyelesaikan proyek kolaboratif gabungan koding blok Scratch dan model kecerdasan artifisial.
  3. Peserta didik mampu menguji (*testing*), memperbaiki (*debugging*), dan mempresentasikan karya di pameran sains Gelar Karya (*Showcase Day*).
* **Profil Pelajar Pancasila:** Mandiri, Bergotong Royong, Kreatif, dan Bernalar Kritis.
* **Media & Sumber Belajar:** Buku Siswa Bab 4, laptop pameran, kardus bekas & bahan daur ulang untuk prototipe fisik, kertas banner poster, meja pameran aula.

---

### B. Skema Alur Pembelajaran Bab 4 (8 Pertemuan @ 2 JP)

| Pertemuan | Materi Pokok | Tujuan Pertemuan | Aktivitas Pembelajaran Guru & Murid | Asesmen Formatif |
|:---:|:---|:---|:---|:---|
| **Pertemuan 25** (2 JP) | Apersepsi & Tahap 1: Empati Masalah | Mengidentifikasi masalah nyata di sekolah melalui observasi lapangan. | Membaca komik Gelar Karya; observasi ke area kantin/taman/kelas; memilih fokus Proyek A (Tempat Sampah AI) atau B (Game Energi). | Lembar perumusan masalah tim |
| **Pertemuan 26** (2 JP) | Tahap 2: Pembagian Peran & Desain | Menetapkan struktur tim dan menggambar sketsa prototipe. | Menentukan Ketua Tim, Desainer Grafis, Lead Programmer, dan Tester; membuat storyboard alur sistem dan sketsa poster pameran. | Matriks peran tim & storyboard |
| **Pertemuan 27** (2 JP) | Tahap 3: Perakitan & Koding Blok (Sesi 1) | Memulai penyusunan blok program dan perakitan fisik. | Programmer mulai menyusun logika Scratch / model AI; desainer mulai merakit bodi prototipe kardus dan banner poster. | Catatan progres mingguan 1 |
| **Pertemuan 28** (2 JP) | Tahap 3: Perakitan & Koding Blok (Sesi 2) | Menggabungkan seluruh komponen menjadi prototipe utuh. | Mengintegrasikan model deteksi dengan pergerakan motor / antarmuka game; pengujian awal fungsi tombol dan respon sensor. | Cek fungsi prototipe terpadu |
| **Pertemuan 29** (2 JP) | Tahap 4: Uji Coba Pengguna (Peer Testing) | Melakukan uji coba saling silang dan melacak bug tersembunyi. | Simulasi uji coba antar kelompok di kelas; mencatat masukan teman dengan format 3P (Puji, Perbaiki, Peluang); memperbaiki bug. | Logbook debugging & peer feedback |
| **Pertemuan 30** (2 JP) | Persiapan Stan Pameran Gelar Karya | Menyiapkan banner, meja demo, dan latihan presentasi tim. | Menata stan pameran di aula; latihan berbicara menyapa pengunjung dengan santun; menyiapkan buku tamu & toples bintang. | Gladi bersih stan pameran |
| **Pertemuan 31** (2 JP) | Puncak Gelar Karya (Showcase Day) | Merayakan karya kelulusan Fase C di hadapan publik sekolah. | Pameran akbar: mengundang Kepala Sekolah, guru, orang tua murid, dan adik kelas; demonstrasi langsung produk inovasi digital. | Rubrik Asesmen Gelar Karya |
| **Pertemuan 32** (2 JP) | Evaluasi Sumatif Akhir Tahun & Refleksi | Menguji ketuntasan kompetensi menyeluruh Fase C. | Mengerjakan Evaluasi Sumatif Akhir Tahun (25 PG & 5 Kasus Terpadu); refleksi kelulusan Fase C dan penyerahan Medali Emas Koder. | Nilai Sumatif Akhir Tahun & Rapor |

---

### C. Panduan Penyelenggaraan Gelar Karya Pameran Kelulusan Fase C
Gelar Karya (*Showcase Day*) adalah momentum perayaan belajar yang sangat sakral bagi murid kelas 6:
1. **Undangan Warga Sekolah & Orang Tua:** Buatlah surat undangan digital ramah lingkungan kepada orang tua murid seminggu sebelum acara. Kehadiran orang tua memberikan dorongan moral yang tak ternilai bagi murid.
2. **Pengaturan Ruangan Aula:** Susun meja pameran mengelilingi dinding aula dengan jarak minimal 1,5 meter antar stan agar alur lalu lintas pengunjung mengalir lancar. Pastikan stopkontak listrik aman dan tidak ada kabel berseliweran di lantai.
3. **Buku Tamu & Stiker Bintang:** Berikan setiap pengunjung 3 lembar stiker bintang saat memasuki aula. Pengunjung dapat menempelkan bintang apresiasi pada stan-stan yang menurut mereka paling inspiratif.
4. **Sertifikat Kelulusan Fase C:** Di akhir acara, Kepala Sekolah dan Guru memberikan sertifikat penghargaan kelulusan mata pelajaran KKA Fase C kepada seluruh murid sebagai bekal kebanggaan melangkah ke bangku SMP.
"""

GURU_BAGIAN_3_SD6 = """# BAGIAN 3: PANDUAN ASESMEN SUMATIF & PELAPORAN HASIL BELAJAR

### A. Rubrik Penilaian Autentik Capstone Project Kelulusan Fase C

| Dimensi Penilaian | Kriteria Skor 4 (Sangat Baik) | Kriteria Skor 3 (Baik) | Kriteria Skor 2 (Cukup) | Kriteria Skor 1 (Perlu Bimbingan) |
|:---|:---|:---|:---|:---|
| **1. Relevansi Masalah & Empati (20%)** | Masalah sangat nyata dan kontekstual di lingkungan sekolah; solusi digital memberikan dampak positif terukur bagi warga sekolah. | Masalah nyata di sekolah, namun solusi digital belum sepenuhnya menjangkau seluruh aspek masalah. | Masalah bersifat umum/teoretis, kurang relevan dengan kondisi riil lingkungan sekolah murid. | Masalah tidak jelas atau sekadar menjiplak tugas yang sudah ada tanpa empati. |
| **2. Kompleksitas Koding & Logika (30%)** | Menerapkan struktur percabangan majemuk, perulangan dinamis, manajemen variabel, atau model AI yang bekerja akurat tanpa bug fatal. | Menerapkan percabangan dan variabel dengan baik, namun terdapat 1-2 kesalahan kecil yang tidak merusak jalannya sistem. | Logika koding sangat sederhana (hanya animasi lurus tanpa percabangan interaktif). | Blok koding belum berjalan dan sistem sering mengalami kemacetan (*freeze/crash*). |
| **3. Ketahanan Prototipe & Debugging (25%)** | Produk teruji tangguh melalui peer testing; tim memiliki catatan logbook debugging yang sistematis dan rapi. | Produk berjalan stabil saat pameran, namun catatan proses debugging belum terdokumentasi lengkap. | Produk sempat mengalami kendala teknis dan membutuhkan waktu lama untuk diperbaiki saat uji coba. | Produk tidak dapat didemonstrasikan di meja demo karena kesalahan fatal belum teratasi. |
| **4. Presentasi & Gotong Royong (25%)** | Seluruh anggota tim berbagi peran secara aktif; berbicara santun, komunikatif, percaya diri, dan stan pameran tertata sangat indah. | Pembagian peran tampak baik; presentasi jelas, meskipun didominasi oleh ketua tim saja. | Tim tampak kurang kompak; stan pameran kurang tertata rapi dan poster penjelasan minim info. | Anggota tim saling menyalahkan saat presentasi berlangsung dan pasif melayani pengunjung. |

---

### B. Panduan Pengolahan Nilai Akhir Rapor KKA Fase C
Nilai Akhir Rapor Kurikulum Merdeka / Nasional dihitung menggunakan formula pembobotan proporsional:

**Formula Pembobotan Nilai Akhir:**  
*Nilai Akhir (NA) = [(2 x Rata-rata Formatif) + (2 x Nilai Capstone Project) + (1 x Nilai Sumatif Akhir)] / 5*

**Kategori Ketercapaian Tujuan Pembelajaran:**
* **85 - 100 (Sangat Mahir):** Murid telah menuntaskan seluruh capaian pembelajaran Fase C dengan sangat unggul, mandiri, kreatif memecahkan masalah, dan beretika mulia. Sangat siap melangkah ke Fase D (SMP).
* **70 - 84 (Mahir):** Murid telah menguasai konsep logika percabangan, perulangan, variabel, sensor, dan literasi digital dengan baik, membutuhkan sedikit pendampingan pada kasus kompleks.
* **60 - 69 (Cukup):** Murid memahami konsep dasar, namun masih membutuhkan bimbingan bertahap saat menyusun logika blok dan melacak bug program.
* **< 60 (Perlu Bimbingan Khusus):** Murid memerlukan bimbingan intensif dan remedial konsep berpikir komputasional mendasar.

---

### C. Profil Penulis & Fasilitator ToT Nasional

[[IMAGE: foto_penulis.jpg | Foto Penulis: Gede Erik Aktama, S.Pd., M.Pd.]]

**Gede Erik Aktama, S.Pd., M.Pd.**  
*Fasilitator Nasional Bimbingan Teknis & Training of Trainers (ToT) Koding dan Kecerdasan Artifisial Kemendikdasmen RI*  
*Dosen Lektor & Ketua Program Studi S1 Sistem Komputer, Fakultas Teknik dan Informatika, Universitas Parna Raya (UNIPAR) Manado*

Penulis adalah akademisi dan praktisi pendidikan teknologi informasi yang berdomisili di Kota Manado, Sulawesi Utara. Menyelesaikan pendidikan Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika dan gelar Magister Pendidikan (M.Pd.) pada Program Studi Pendidikan Teknologi dan Kejuruan dari Universitas Pendidikan Ganesha (UNDIKSHA), Singaraja. Saat ini, penulis aktif mengemban jabatan fungsional akademik **Lektor** (SK Mendiktisaintek RI No. 0044/LL16/KP.07/2025) serta menjabat sebagai Ketua Program Studi S1 Sistem Komputer di Universitas Parna Raya Manado.

Sebagai akademisi yang mendedikasikan diri pada transformasi digital pendidikan dasar dan menengah di Indonesia, penulis dipercaya oleh Direktorat Guru Pendidikan Dasar, Direktorat Jenderal Guru dan Tenaga Kependidikan, Kementerian Pendidikan Dasar dan Menengah RI sebagai **Fasilitator Nasional** dalam Bimbingan Teknis dan *Training of Trainers* (ToT) Pembelajaran Koding dan Kecerdasan Artifisial (KKA) untuk jenjang SD, SMP, SMA, dan SMK.

Penulis memiliki kepakaran riset dalam bidang *Computational Thinking in Primary Education*, *Artificial Intelligence for K-12*, *Educational Robotics*, dan Pengembangan Perangkat Ajar Interaktif berbasis *Deep Learning*.

*Korespondensi & Diskusi Pedagogis Guru:* erikaktama@unipar.ac.id
"""

full_guru_sd6_md = "\n\n".join([
    GURU_FRONT_MATTER_SD6,
    GURU_BAGIAN_1_SD6,
    GURU_BAGIAN_2_SD6,
    GURU_BAGIAN_3_SD6,
    DAFTAR_PUSTAKA_RESMI_SD6
])
