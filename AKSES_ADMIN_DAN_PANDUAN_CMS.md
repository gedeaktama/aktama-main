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

## 5. 🚀 CARA UPDATE SERVER PRODUKSI NIAGAHOSTER (1-KLIK)

Setiap kali ada pembaruan kode atau artikel dari GitHub, Anda cukup menjalankan perintah 1-baris berikut di terminal SSH Niagahoster:

```bash
cd /home/u107454400/domains/aktama.com/public_html/aktama-main-source && git pull origin main && bash update.sh
```

Skrip ini akan mengeksekusi secara otomatis:
1. `git pull origin main` (tarik pembaruan terbaru dari GitHub).
2. Menjalankan migrasi database via binary Alt-PHP 8.3 (`/opt/alt/php83/usr/bin/php artisan migrate --force`).
3. Menjalankan seeder artikel komprehensif (`db:seed --force`).
4. Menyinkronkan aset gambar artikel, upload media, dan build ke folder publik `public_html`.
5. Membersihkan cache dan mengoptimalkan cache produksi Laravel.

---

&copy; 2026 PT Aktama Digital Antika. Seluruh hak cipta dilindungi.
