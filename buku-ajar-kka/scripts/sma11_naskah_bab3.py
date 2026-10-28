"""
Modul Naskah Bab III Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB3_SMA11 = """# BAB III: KOLABORASI MULTIMEDIA TINGKAT LANJUT UNTUK PENDUKUNG APLIKASI

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
"""
