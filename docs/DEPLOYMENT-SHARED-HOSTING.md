# PANDUAN DEPLOYMENT SHARED HOSTING (cPanel / Niagahoster / Hostinger)
## Sistem Portal Utama & Ekosistem Bisnis PT Aktama Digital Antika (Laravel 12)

Dokumen ini merupakan panduan teknis resmi langkah-demi-langkah untuk mempublikasikan website **Aktama Digital** (`aktama.com`) ke layanan **Shared Hosting** berbasis cPanel, DirectAdmin, atau hPanel.

---

## 1. MENGAPA ARSITEKTUR INI AMAN DARI MALWARE & JUDOL?
Banyak website perusahaan di Indonesia yang dibangun menggunakan WordPress rentan terhadap peretasan otomatis, backdoor plugin, dan injeksi kata kunci judi online (judol) yang merusak reputasi SEO di Google.

Aplikasi **Aktama Digital** dibangun dengan arsitektur **Laravel 12**:
1. **Pemisahan Inti Sistem**: File sensitif (`.env`, `routes`, `app`, `database`, `vendor`) terkunci di luar direktori akses publik web.
2. **Ketiadaan Plugin Pihak Ketiga Rentan**: Menggunakan CMS terstruktur native tanpa plugin bloated atau theme nulled.
3. **Proteksi Bawaan**: Dilengkapi CSRF Token otomatis, Rate Limiter login, SQL Parameterization (Eloquent ORM), dan HTTP Security Headers (`X-Frame-Options`, `X-Content-Type-Options`).

---

## 2. PILIHAN METODE STRUKTUR DIREKTORI DI CPANEL

### METODE A: Pemisahan Folder (SANGAT DIREKOMENDASIKAN - STANDAR INDUSTRI)
Metode ini adalah standar keamanan tertinggi di mana source code inti diletakkan sejajar dengan `public_html`, bukan di dalamnya.

```text
/home/username_cpanel/
├── aktama-source/            <-- SEMUA file Laravel diletakkan di sini (KECUALI isi folder public)
│   ├── app/
│   ├── bootstrap/
│   ├── config/
│   ├── database/
│   ├── resources/
│   ├── routes/
│   ├── storage/
│   ├── vendor/
│   ├── .env
│   └── artisan
└── public_html/              <-- HANYA berisi isi dari folder 'public' Laravel
    ├── build/                <-- Hasil compile Vite (css & js)
    ├── storage/              <-- Symlink ke aktama-source/storage/app/public
    ├── .htaccess             <-- File htaccess dari folder public
    ├── favicon.ico
    └── index.php             <-- File index.php (disesuaikan path-nya)
```

#### Modifikasi File `public_html/index.php`:
Buka file `public_html/index.php` di File Manager cPanel, ubah path pemanggilan autoloader dan bootstrap menjadi:
```php
// 1. Arahkan maintenance driver ke direktori aktama-source
if (file_exists($maintenance = __DIR__.'/../aktama-source/storage/framework/maintenance.php')) {
    require $maintenance;
}

// 2. Arahkan vendor autoloader ke aktama-source
require __DIR__.'/../aktama-source/vendor/autoload.php';

// 3. Jalankan aplikasi Laravel dari aktama-source
(require_once __DIR__.'/../aktama-source/bootstrap/app.php')
    ->handleRequest(Request::capture());
```

---

### METODE B: Domain Mengarah ke Subfolder `public` (Bila cPanel Mendukung)
Jika Anda menggunakan **Addon Domain** atau **Subdomain** di cPanel:
1. Masuk menu **Domains** di cPanel.
2. Ubah kolom **Document Root** untuk domain `aktama.com` menjadi:
   `aktama-main/public`
3. Dengan demikian, Anda dapat mengunggah seluruh folder `aktama-main` apa adanya tanpa mengubah baris kode apa pun.

---

### METODE C: Seluruh Proyek di dalam `public_html` (Menggunakan Root `.htaccess`)
Jika hosting Anda tidak mengizinkan akses di luar `public_html` dan tidak dapat mengubah Document Root:
1. Unggah seluruh proyek ke `public_html`.
2. Pastikan file `.htaccess` di root proyek aktif. File `.htaccess` yang telah kami sertakan di root proyek otomatis memblokir akses ke `.env`, `.git`, `storage/logs/`, dan me-rewrite traffic ke subdirektori `/public/`.

---

## 3. LANGKAH-LANGKAH DEPLOYMENT DARI NOL

### Langkah 1: Build Asset Vite di Komputer Lokal
Sebelum mengunggah, pastikan asset CSS & JS Bootstrap telah ter-compile ke dalam folder `public/build/`:
```bash
npm run build
```
Pastikan folder `public/build/assets/` berisi file `app-*.css` dan `app-*.js` serta `public/build/manifest.json`.

### Langkah 2: Buat Arsip ZIP
Kemas file proyek ke dalam file ZIP (`aktama-release.zip`).
**JANGAN sertakan folder berikut untuk menghemat kuota dan mempercepat upload:**
- `node_modules/` (TIDAK diperlukan di server produksi)
- `.git/`
- `tests/` (opsional diabaikan)

*Catatan: Folder `vendor/` HARUS disertakan jika hosting Anda tidak memiliki akses SSH / composer.*

### Langkah 3: Upload dan Ekstrak di cPanel
1. Login ke cPanel hosting Anda (misal: `https://aktama.com:2083`).
2. Buka menu **File Manager**.
3. Upload file `aktama-release.zip` ke direktori tujuan (sesuai Metode A, B, atau C).
4. Klik kanan file ZIP, pilih **Extract**.

### Langkah 4: Pembuatan Database MySQL di cPanel
1. Buka menu **MySQL Database Wizard** di cPanel.
2. **Step 1**: Buat database baru, contoh: `u1234567_aktama`.
3. **Step 2**: Buat user database baru, contoh: `u1234567_dbuser` dengan password yang kuat.
4. **Step 3**: Berikan centang pada **ALL PRIVILEGES** untuk menghubungkan user ke database tersebut.
5. Simpan nama database, user, dan password untuk konfigurasi `.env`.

### Langkah 5: Konfigurasi File `.env` Produksi
Buka file `.env` di File Manager (pastikan opsi *Show Hidden Files* aktif di File Manager):
```ini
APP_NAME="Aktama Digital"
APP_ENV=production
APP_KEY=base64:GKsZPLa2tA287n+Geva7SpMykHlichZUi1VWyMWmm6c=
APP_DEBUG=false
APP_URL=https://aktama.com

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=u1234567_aktama
DB_USERNAME=u1234567_dbuser
DB_PASSWORD=PasswordDatabaseKuatAnda123!

SESSION_DRIVER=database
CACHE_STORE=database
QUEUE_CONNECTION=sync
```
> **PENTING**: Pastikan `APP_DEBUG=false` untuk mencegah kebocoran informasi error teknis kepada pengunjung umum.

### Langkah 6: Migrasi Database & Seeder
**Cara 1: Lewat Terminal cPanel (Jika Tersedia):**
```bash
php artisan migrate --force
php artisan db:seed --force
```

**Cara 2: Lewat phpMyAdmin cPanel:**
Jika tidak ada Terminal SSH:
1. Ekspor database lokal `aktama_main` dari XAMPP (`http://localhost:8080/phpmyadmin`) ke file `.sql`.
2. Buka **phpMyAdmin** di cPanel hosting Anda.
3. Pilih database `u1234567_aktama`.
4. Klik tab **Import**, pilih file `.sql` tadi, lalu klik **Go**.

### Langkah 7: Pembuatan Symlink Storage (`storage:link`)
Storage link diperlukan agar file media atau gambar yang diunggah dapat diakses publik.

**Opsi A (Via Terminal cPanel):**
```bash
php artisan storage:link
```

**Opsi B (Via File PHP Runner Satu Kali Pakai):**
Jika tidak ada terminal, buat file baru di `public_html/storage-link-runner.php`:
```php
<?php
// Ganti path sesuai Metode A atau B
$target = __DIR__ . '/../aktama-source/storage/app/public';
$shortcut = __DIR__ . '/storage';

if (symlink($target, $shortcut)) {
    echo "Symlink Berhasil Dibuat!";
} else {
    echo "Gagal membuat symlink. Periksa izin direktori.";
}
// HAPUS FILE INI SETELAH DIJALANKAN DARI BROWSER (https://aktama.com/storage-link-runner.php)
```
Buka `https://aktama.com/storage-link-runner.php` sekali di browser, lalu **segera hapus file tersebut**.

### Langkah 8: Optimasi Kecepatan Produksi (Cache Artisan)
Jalankan perintah ini di Terminal cPanel untuk performa load di bawah 1 detik:
```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

### Langkah 9: Pasang SSL (HTTPS) Gratis
1. Di cPanel, buka menu **SSL/TLS Status**.
2. Pilih domain Anda (`aktama.com` dan `www.aktama.com`).
3. Klik tombol **Run AutoSSL**.
4. Di menu **Domains**, aktifkan toggle **Force HTTPS Redirect**.

---

## 4. KREDENSIAL DEFAULT LOGIN CMS
Setelah deployment, Anda dapat langsung masuk ke portal CMS admin melalui:
- **URL Login**: `https://aktama.com/admin/login`
- **Email**: `admin@aktama.com`
- **Password Default**: `AdminAktama2026!`

> **TINDAKAN WAJIB SETELAH DEPLOY**: Segera masuk ke menu **Pengaturan Situs** atau database untuk memperbarui password admin Anda.

---

## 5. PANDUAN INTEGRASI BISNIS
Website utama ini berfungsi sebagai **Hub Induk** ekosistem bisnis:
1. **Layanan Jasa Pembuatan Website & Aplikasi**: Menampilkan katalog layanan anti-malware judol dengan formulir konsultasi terhubung langsung ke WhatsApp.
2. **Pelatihan AI & Komputer**: Program pelatihan terverifikasi dengan instruktur resmi (Gede Erik Aktama, S.Pd., M.Pd. - Dosen Univ. Parna Raya & Fasilitator Nasional KKA).
3. **Katalog Kopi (Aktama Coffee)**: Menampilkan varian eceran dan paket pasokan grosir untuk kafe/reseller dengan tombol pesanan otomatis ke WhatsApp. Nama brand kopi dapat diganti dinamis kapan saja melalui CMS `/admin/settings`.
4. **Aktama Academy**: Terintegrasi ke portal LMS online (`app.aktama.com` / `aktama.com/academy`).
5. **Undangan Online**: Menampilkan paket dan tema undangan digital dengan tombol live demo langsung.
6. **Lead Management**: Setiap formulir konsultasi masuk ke CMS `/admin/leads` dengan status follow-up dan link WhatsApp prefilled.

---

## 6. TROUBLESHOOTING KENDALA UMUM

| Gejala Masalah | Penyebab Utama | Solusi |
| :--- | :--- | :--- |
| **Error 500 Internal Server Error** | Folder `storage` atau `bootstrap/cache` tidak writable | Ubah permission folder `storage/` dan `bootstrap/cache/` menjadi `775` atau `755` via File Manager cPanel. |
| **Vite Manifest Not Found** | Folder `public/build` belum diunggah | Jalankan `npm run build` di lokal dan pastikan folder `public/build` terunggah lengkap ke hosting. |
| **Gambar Produk / Berita 404** | Symlink `storage` belum dibuat | Jalankan langkah 7 (Opsi A atau Opsi B) untuk membuat symlink. |
| **Halaman Admin Redirect Berulang (Loop)** | Konfigurasi `APP_URL` di `.env` berbeda dengan protokol domain (misal `http://` padahal sudah `https://`) | Buka `.env`, pastikan `APP_URL=https://aktama.com` (sesuai HTTPS). |
| **Database Connection Refused** | Nama DB atau User cPanel keliru (biasanya lupa prefix username cPanel) | Pastikan nama database di `.env` lengkap dengan prefix, misal `u1234567_aktama`. |
