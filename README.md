# PT AKTAMA DIGITAL ANTIKA — PORTAL UTAMA & CMS

Portal Perusahaan Resmi PT Aktama Digital Antika dan Ekosistem Bisnis Terpadu:
- **Domain Resmi**: [https://aktama.com](https://aktama.com)
- **Pelatihan Kecerdasan Artifisial (AI)** (Fasilitator Nasional Terverifikasi Kemdikdasmen & LPK Resmi)
- **Jasa Pembuatan Website & Software House Bebas Malware**
- **Aktama Academy** (Platform Kursus & LMS: [https://academy.aktama.com](https://academy.aktama.com))
- **Platform Undangan Online** ([https://undanganonline.aktama.com](https://undanganonline.aktama.com))
- **Distribusi Kopi Riil (Aktama Coffee / Kopi Distro)** ([https://coffee.aktama.com](https://coffee.aktama.com))

---

## 📖 PANDUAN PENGGUNA & KREDENSIAL AKSES
Dokumentasi lengkap mengenai link publik, link admin, akun pengguna, dan cara penggunaan CMS telah disimpan di:
- 👉 **[docs/PANDUAN_DAN_AKSES_SISTEM.md](docs/PANDUAN_DAN_AKSES_SISTEM.md)**
- 🚀 **[LANGKAH-SINGKAT.txt](LANGKAH-SINGKAT.txt)** (Panduan Cepat Deploy Niagahoster)

---

## 🔑 AKSES CEPAT ADMIN
- **Localhost**: [http://localhost:8080/aktama-main/public/admin/login](http://localhost:8080/aktama-main/public/admin/login)
- **Produksi (Live)**: [https://aktama.com/admin/login](https://aktama.com/admin/login)
- **Email**: `admin@aktama.com`
- **Password**: `AdminAktama2026!`

---

## 🚀 FITUR CMS (WORDPRESS-GRADE NO-CODE)
1. **Opsi A — Modular Section Builder**: Drag & Drop urutan seksi beranda, sembunyikan/tampilkan seksi, edit judul & teks.
2. **Opsi B — Visual Drag & Drop Canvas Builder**: GrapesJS visual editor untuk membuat halaman baru layaknya Elementor/WPBakery.
3. **Pengaturan Menu (Header & Footer)**: Drag & Drop tata letak navigasi tanpa coding.
4. **Postingan Berita / Artikel**: Manajemen konten artikel, upload gambar unggulan, dan kategori instan.
5. **Pengaturan Branding**: Upload Logo, Cap Resmi, Favicon, serta info Topbar & Footer.

---

## 🌐 DEPLOYMENT KE SERVER HOSTING (NIAGAHOSTER / CPANEL)

Proyek ini telah dikonfigurasi dengan skrip deployment otomatis teruji untuk CloudLinux Alt-PHP 8.3 Niagahoster:
- **Web Root Publik**: `/home/u107454400/domains/aktama.com/public_html`
- **Source Code**: `/home/u107454400/domains/aktama.com/public_html/aktama-main-source`
- **Skrip Deployment**: [`scripts/linux/deploy-niagahoster.sh`](scripts/linux/deploy-niagahoster.sh)
- **Template .env**: [`.env.production.example`](.env.production.example)

### Perintah Cepat Deploy via SSH:
```bash
ssh -p 65002 u107454400@147.93.80.47
cd /home/u107454400/domains/aktama.com/public_html/aktama-main-source
git pull origin main
bash scripts/linux/deploy-niagahoster.sh
```

---

## 🛠️ MENJALANKAN DI LOCALHOST (XAMPP)
- Pastikan Apache & MySQL berjalan di XAMPP.
- Aplikasi dapat diakses langsung pada: [http://localhost:8080/aktama-main/public/](http://localhost:8080/aktama-main/public/)

---
&copy; 2026 PT Aktama Digital Antika. Seluruh hak cipta dilindungi.
