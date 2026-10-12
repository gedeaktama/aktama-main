# PANDUAN RESMI UPDATE & DEPLOYMENT EKOSISTEM AKTAMA DIGITAL
**Niagahoster / cPanel CloudLinux (Server IP: 147.93.80.47 | SSH Port: 65002)**
*Dokumen ini menjadi rujukan resmi pengelolaan seluruh platform website di bawah naungan PT Aktama Digital Antika.*

---

## 1. PETA ARSITEKTUR & REPOSITORI EKOSISTEM

| Layanan / Website | Domain Live | Folder Lokal | Repositori GitHub | Folder Source di Server | Web Root Publik Server |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Web Utama (Portal & CMS)** | `https://aktama.com` | `d:\Xampp2\htdocs\aktama-main` | [aktama-main.git](https://github.com/gedeaktama/aktama-main.git) | `public_html/aktama-main-source` | `public_html/` |
| **Undangan Online** | `https://undanganonline.aktama.com` | `d:\Xampp2\htdocs\undanganonline` | [undanganonline.git](https://github.com/gedeaktama/undanganonline.git) | `public_html/webutama-source` | `public_html/undanganonline/` |
| **Aktama Coffee (Kopi Distro)** | `https://coffee.aktama.com` | `d:\Xampp2\htdocs\kopi` | [aktama-coffee.git](https://github.com/gedeaktama/aktama-coffee.git) | `public_html/kopi-source` | `public_html/coffee/` |
| **Aktama Academy (LMS)** | `https://academy.aktama.com` | `d:\Xampp2\htdocs\aktamaacademy` | *(WordPress Standar)* | `public_html/aktama-source` | `public_html/academy/` |

---

## 2. AKSES SSH SERVER
- **Perintah Login**:
  ```bash
  ssh -p 65002 u107454400@147.93.80.47
  ```
- **Path Root Proyek**:
  ```bash
  cd /home/u107454400/domains/aktama.com/public_html
  ```

---

## 3. PROSEDUR UPDATE HARIAN (RUTIN)

Kapan pun Anda melakukan pembaruan kode, fitur, styling, atau artikel di komputer lokal:

### A. Update Web Utama (`https://aktama.com`)

**1. Di Komputer Lokal (`d:\Xampp2\htdocs\aktama-main`):**
```bash
npm run build
git add .
git commit -m "update web utama"
git push origin main
```

**2. Di Terminal SSH Server:**
```bash
cd /home/u107454400/domains/aktama.com/public_html/aktama-main-source
git pull origin main
bash scripts/linux/deploy-niagahoster.sh
```

---

### B. Update Undangan Online (`https://undanganonline.aktama.com`)

**1. Di Komputer Lokal (`d:\Xampp2\htdocs\undanganonline`):**
```bash
npm run build
git add .
git commit -m "update website undangan"
git push origin main
```

**2. Di Terminal SSH Server:**
```bash
cd /home/u107454400/domains/aktama.com/public_html/webutama-source
git pull origin main
bash scripts/linux/deploy-niagahoster.sh
```

---

### C. Update Aktama Coffee (`https://coffee.aktama.com`)

**1. Di Komputer Lokal (`d:\Xampp2\htdocs\kopi`):**
```bash
git add .
git commit -m "update website coffee"
git push origin main
```

**2. Di Terminal SSH Server:**
```bash
cd /home/u107454400/domains/aktama.com/public_html/kopi-source
git pull origin main
bash scripts/linux/deploy-hosting.sh
```

---

## 4. KREDENSIAL DATABASE PRODUKSI (TERVERIFIKASI)

| Proyek | Nama Database | Username | Catatan Password |
| :--- | :--- | :--- | :--- |
| **Web Utama (`aktama-main`)** | `u107454400_aktamamain` | `u107454400_aktamamain` | `DB_PASSWORD='|Cd*8$Ao:59'` *(Wajib diapit petik tunggal di .env)* |
| **Undangan Online** | `u107454400_DB_WebUtama` | `u107454400_webutama` | `DB_PASSWORD=Pr161024pr@@` |

> **PENTING**: Jika membuat database atau mengganti password di cPanel, selalu pastikan di menu **MySQL Databases** bagian **"Add User To Database"** bahwa User telah dihubungkan ke Database dengan **ALL PRIVILEGES** & klik **Make Changes**.

---

## 5. APA YANG DILAKUKAN SKRIP OTOMATIS SAAT DEPLOY?

Skrip `deploy-*.sh` di masing-masing repositori otomatis melakukan hal-hal berikut:
1. Menarik update kode terbaru dari Git (`git pull origin main`).
2. Menjalankan dependensi PHP produksi (`composer install --no-dev --optimize-autoloader`).
3. Menjalankan migrasi database baru (`php artisan migrate --force`).
4. Menjalankan seeder tema / pengaturan sistem (`php artisan db:seed --force`).
5. Membersihkan cache lama dan menyusun cache baru (`config:cache`, `route:cache`, `view:cache`).
6. Memastikan symlink `storage` publik aktif.
7. Menerbitkan aset terkompilasi ke direktori web publik tanpa mengganggu subdomain lainnya.
8. Mengatur izin folder writable (`chmod -R 775 storage bootstrap/cache`).

---
&copy; 2026 PT Aktama Digital Antika. Seluruh hak cipta dilindungi.
