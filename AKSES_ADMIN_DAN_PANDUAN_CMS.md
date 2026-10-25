# 🔐 PANDUAN AKSES ADMIN & PENGELOLAAN CMS AKTAMA DIGITAL
**PT AKTAMA DIGITAL ANTIKA** (NIB: `1703250057018`)

Dokumen ini berisi informasi kredensial akses panel administrator, link login, dan panduan penggunaan fitur posting berita serta pembuatan halaman baru bergaya **WordPress**.

---

## 1. 🔑 KREDENSIAL LOGIN ADMINISTRATOR

Gunakan kredensial berikut untuk masuk ke panel admin:

| Keterangan | Nilai Kredensial |
| :--- | :--- |
| **Alamat Email** | `admin@aktama.com` |
| **Kata Sandi (Password)** | `AdminAktama2026!` |
| **Hak Akses (Role)** | `admin` (Administrator Penuh) |

> [!TIP]
> Anda dapat mengganti kata sandi kapan saja setelah masuk melalui menu **Profil & Kata Sandi** (`/admin/profile`).

---

## 2. 🌐 ALAMAT URL LOGIN ADMIN

### A. Server Produksi (Online / Live)
- **URL Login Langsung**: [https://aktama.com/admin/login](https://aktama.com/admin/login)
- **Alternatif**: Kunjungi [https://aktama.com](https://aktama.com) lalu scroll ke bagian paling bawah (footer) dan klik tombol **"Login Admin"**.

### B. Komputer Lokal (XAMPP)
- **URL Login XAMPP**: [http://localhost:8080/aktama-main/public/admin/login](http://localhost:8080/aktama-main/public/admin/login)  
  *(Atau `http://localhost/aktama-main/public/admin/login` jika port Apache XAMPP default 80)*
- **URL Artisan Serve**: [http://127.0.0.1:8000/admin/login](http://127.0.0.1:8000/admin/login)

---

## 3. 📝 PANDUAN FITUR POSTING BERITA / ARTIKEL (ALA WORDPRESS)
Akses menu: **Postingan / Berita** (`/admin/articles`)

Fitur-fitur yang tersedia menyerupai WordPress Classic Editor & Gutenberg:
1. **Judul & Permalink Otomatis:**
   - Masukkan judul berita, permalink slug akan dibuat otomatis dan dapat diedit secara manual dengan tombol *Edit*.
2. **Editor Teks Kaya (WYSIWYG TinyMCE 6):**
   - Format heading (H1-H4), paragraf, tebal, miring, coret, warna teks, perataan teks, bullet, numbering, quote, tabel interaktif, hingga mode layar penuh (*fullscreen*).
3. **Tombol "Tambah Media" (WordPress Add Media):**
   - Terletak di atas editor teks. Klik untuk memilih foto/gambar dari komputer Anda. Sistem akan langsung mengunggah file ke server (`/images/uploads/`) dan menyematkannya ke dalam teks di posisi kursor secara otomatis.
4. **Tab Visual vs Teks / HTML:**
   - Anda dapat berpindah antara mode tampilan visual atau mode kode sumber HTML kapan saja.
5. **Yoast / Rank Math SEO Simulator (Live):**
   - Melihat tampilan judul dan cuplikan artikel di hasil pencarian Google secara *real-time*.
   - Dilengkapi penghitung batas karakter optimal (Meta Title maks 60 karakter, Meta Description maks 160 karakter).
6. **Metabox Terbitkan (Publish Box):**
   - Pilihan status: **Diterbitkan (Published)** atau **Simpan Draf (Draft)**.
   - Pilihan tanggal dan waktu publikasi.
7. **Metabox Kategori Interaktif:**
   - Memilih kategori berita yang ada, atau klik **"+ Tambah Kategori Baru"** untuk membuat kategori baru secara instan tanpa perlu reload halaman.
8. **Metabox Gambar Unggulan (Featured Image):**
   - Mengunggah thumbnail artikel dengan rasio 16:9 (1200x675 px). Dilengkapi pratinjau, tombol ganti gambar, dan tombol hapus gambar.
9. **Metabox Tag:**
   - Menambahkan kata kunci berita yang dipisahkan tanda koma dan otomatis tampil sebagai badge label.

---

## 4. 📄 PANDUAN TAMBAH HALAMAN BARU (ALA WORDPRESS)
Akses menu: **Halaman & Visual Canvas** (`/admin/pages`)

Mendukung 2 mode pembuatan halaman (*Dual Engine*):
1. **Mode A — Editor Standar (WYSIWYG):**
   - Sangat cocok untuk halaman dokumen, profil institusi, visi misi, regulasi, kebijakan privasi, atau syarat ketentuan.
   - Menggunakan TinyMCE dengan dukungan gambar, tabel, dan format teks lengkap.
2. **Mode B — Visual Drag & Drop Canvas (Elementor Style):**
   - Sangat cocok untuk mendesain landing page interaktif dengan blok-blok siap pakai (Hero Banner, 3 Kolom Fitur, Tabel Harga, CTA).
3. **Atribut Halaman (Page Attributes):**
   - **Template Layout:**
     - *Default*: Container standar dengan breadcrumb dan judul.
     - *Full Width*: Layar penuh 100% tanpa batas container (pas untuk landing page visual).
     - *Blank Canvas*: Halaman polos tanpa banner header standar.
   - **Urutan Menu (*Order*):** Menentukan urutan prioritas halaman di navigasi.
   - **Gambar Unggulan Halaman:** Digunakan untuk thumbnail kartu dan Open Graph saat tautan halaman dibagikan di WhatsApp.
   - **SEO Simulator Google:** Peninjau tampilan judul dan deskripsi di hasil pencarian.

---

## 5. 🛠️ PANDUAN POSTING JASA, PELATIHAN AI & PORTOFOLIO (ALA WORDPRESS)
Seluruh modul postingan di panel admin kini telah diseragamkan dengan antarmuka 2-kolom ala WordPress lengkap dengan Editor Teks Kaya (**TinyMCE 6**) dan tombol **"Tambah Media"**:

### A. Jasa Web & Aplikasi (`/admin/services`)
- **Editor Deskripsi Lengkap:** Buat rincian paket layanan menggunakan heading, bullet points, tabel perbandingan, gambar pendukung, dan tombol CTA.
- **Tombol Tambah Media:** Sisipkan infografis alur pembuatan website atau arsitektur sistem langsung ke dalam deskripsi.
- **Sidebar Kanan:**
  - *Kategori Layanan:* Pengembangan Web & Aplikasi, AI & Data Science, Sistem Informasi Terpadu, Desain UI/UX.
  - *Estimasi Harga:* Format mata uang (contoh: `Mulai Rp 5.000.000` atau `Kustom`).
  - *Ikon / Badge:* Pilihan ikon Lucide / FontAwesome.
  - *Gambar Unggulan (Thumbnail):* Banner representatif jasa untuk kartu katalog dan Open Graph.
  - *Poin Fitur Unggulan:* Daftar fitur per baris yang otomatis dirender sebagai checklist bercentang hijau.

### B. Program Pelatihan AI (`/admin/training`)
- **Editor Silabus & Sasaran Kompetensi:** Format tujuan pembelajaran, kurikulum modul, dan studi kasus dengan editor teks kaya.
- **Tombol Tambah Media:** Sisipkan foto dokumentasi pelatihan sebelumnya, sertifikat contoh, atau bagan materi.
- **Sidebar Kanan:**
  - *Kategori & Format:* AI untuk Pendidikan / Guru, AI Produktivitas Kantor, Pemrograman AI / Edge Computing, LPK & Sertifikasi; Format Tatap Muka (In-House / Onsite) atau Daring (Online / Webinar).
  - *Durasi & Investasi Biaya:* Contoh `2 Hari (16 Jam Pelajaran)` dan `Rp 2.500.000 / Peserta`.
  - *Status Pendaftaran:* Buka Pendaftaran, Penuh, atau Selesai.
  - *Gambar Unggulan Pelatihan:* Poster kegiatan atau foto kelas pelatihan.

### C. Portofolio Proyek (`/admin/portfolios`)
- **Editor Studi Kasus Proyek:** Tulis latar belakang masalah, solusi teknis yang dibangun, tantangan implementasi, dan dampak positif untuk klien.
- **Tombol Tambah Media:** Unggah tangkapan layar antarmuka dashboard, ERD database, atau foto serah terima sistem langsung di dalam artikel.
- **Sidebar Kanan:**
  - *Tangkapan Layar Unggulan (Mockup):* Foto mockup layar sistem/aplikasi (disarankan rasio 16:9).
  - *Tautan Proyek / Demo:* Link URL sistem yang berjalan (otomatis menghasilkan tombol "Kunjungi Proyek" live).
  - *Tumpukan Teknologi (Tech Stack):* Tag teknologi (contoh: `Laravel 11`, `Python`, `YOLOv8`, `MySQL`, `TailwindCSS`).
  - *Nama & Tipe Klien:* Pemerintah Daerah, Instansi Kepolisian, Sekolah/Kampus, UMKM, atau Perusahaan Swasta.
  - *Tahun Penyelesaian:* Tahun rilis proyek.

---

## 6. 💎 FITUR BARU & UPGRADE SISTEM TERAKHIR (LENGKAP)

### A. Pustaka Media Terpusat (*WordPress Media Library Modal*)
- Tersedia pada seluruh form postingan admin (Artikel, Halaman, Jasa, Pelatihan, dan Portofolio).
- Tombol **"📁 Pustaka Media"** membuka galeri pop-up dengan fitur:
  - Pencarian file gambar real-time.
  - Filter berdasarkan folder (`uploads`, `articles`, `services`, `training`, `portfolios`, `pages`).
  - Panel rincian lampiran (pratinjau, ukuran file KB, dimensi piksel, tanggal, teks alternatif / Alt Text).
  - Tombol **"Sisipkan ke Postingan"** (*Insert into post*) langsung di posisi kursor TinyMCE.
  - Tab **"Unggah Berkas Baru"** dengan area tarik-lepas (*drag & drop*) dan indikator progres.

### B. Pencarian & Filter Live pada Artikel & Portofolio Publik
- Halaman `/artikel` kini dilengkapi bilah pencarian cerdas yang memfilter judul, ringkasan, isi konten, dan tag tanpa menghilangkan filter kategori yang sedang aktif.
- Halaman `/portofolio` dilengkapi tombol filter kategori dinamis dan pencarian teknologi (misal: `Laravel`, `Python`, `POS`, `Kepolisian`).
- Dilengkapi badge status pencarian aktif dan tombol reset 1-klik jika ingin kembali ke semua data.

### C. Daftar Isi Otomatis (*Table of Contents*) & Tombol Bagikan (*Social Share*)
- Pada setiap halaman baca artikel (`/artikel/{slug}`):
  - Sistem secara otomatis memindai sub-judul `<h2>` dan `<h3>` untuk menghasilkan kotak **Daftar Isi Interaktif** dengan tautan lompat (*anchor jump*) dan tombol sembunyikan/tampilkan.
  - Tombol berbagi instan ke **WhatsApp**, **LinkedIn**, **Facebook**, **X**, serta tombol **Salin Tautan** dengan notifikasi tersalin.
  - Banner ajakan konsultasi dan pelatihan in-house resmi PT Aktama Digital Antika.

### D. 4 Seksi Baru Beranda Utama (*Social Proof & Kredibilitas*)
1. **Mitra Kerjasama & Social Proof:** Menampilkan segmen instansi kepolisian, pendidik sekolah KKA, legalitas LPK, dan UMKM retail.
2. **Dokumentasi Lapangan:** Galeri foto kelas pelatihan tatap muka di Polres Minahasa Tenggara, pelatihan guru sekolah, dan pendampingan keamanan website.
3. **Ulasan & Testimoni:** 4 testimoni nyata dari perwakilan kepolisian, koordinator kurikulum sekolah, pengurus yayasan klien website, dan pemilik usaha retail.
4. **FAQ Interaktif:** Accordion tanya jawab seputar legalitas sertifikat LPK (NIB: `1703250057018`), jaminan website bebas dari celah peretasan judi online, alur pelatihan luar kota, estimasi pengerjaan, dan garansi bug.

### E. Kepatuhan Regulasi UU Pelindungan Data Pribadi (UU PDP)
- Halaman resmi **Kebijakan Privasi** (`/kebijakan-privasi` atau `/halaman/kebijakan-privasi`) yang mengacu pada UU RI No. 27 Tahun 2022.
- Halaman resmi **Syarat & Ketentuan Layanan** (`/syarat-ketentuan` atau `/halaman/syarat-ketentuan`).
- Terintegrasi pada tautan footer di seluruh halaman web.

### F. Benteng Keamanan Anti-Hack & Anti-Webshell Judi Online (*Security Hardening*)
- File proteksi server [public/images/.htaccess](file:///d:/Xampp2/htdocs/aktama-main/public/images/.htaccess) telah dipasang untuk **mematikan eksekusi script PHP** di seluruh folder media.
- Apache akan otomatis menolak akses (`403 Forbidden`) terhadap segala file berekstensi `.php`, `.phtml`, `.cgi`, `.sh` di folder upload, sehingga website **100% steril dari injeksi backdoor dan script judi online**.

---

## 7. 🚀 CARA UPDATE SERVER PRODUKSI NIAGAHOSTER (1-KLIK)

Setiap kali ada pembaruan kode atau artikel dari GitHub, Anda cukup menjalankan perintah 1-baris berikut di terminal SSH Niagahoster:

```bash
cd /home/u107454400/domains/aktama.com/public_html/aktama-main-source && git pull origin main && bash update.sh
```

Skrip ini akan mengeksekusi secara otomatis:
1. `git pull origin main` (tarik seluruh pembaruan fitur, seeder, dan benteng keamanan dari GitHub).
2. Menjalankan migrasi database via binary Alt-PHP 8.3 (`/opt/alt/php83/usr/bin/php artisan migrate --force`).
3. Menjalankan seeder database lengkap (`db:seed --force`) yang otomatis mengaktifkan seluruh seksi baru dan halaman legalitas.
4. Menyinkronkan aset gambar, upload media, file `.htaccess` keamanan, dan build ke folder publik `public_html`.
5. Membersihkan cache dan mengoptimalkan cache produksi Laravel.

---

&copy; 2026 PT Aktama Digital Antika. Seluruh hak cipta dilindungi.


