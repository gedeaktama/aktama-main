"""
Modul Naskah Bab II Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB2_SMA11 = """# BAB II: REKAYASA BASIS DATA TERINTEGRASI, DATA ENCODING, DAN REST API

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
print("\n===== DATA DITERIMA & DIPROSES (DESERIALISASI) =====")
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
        print("\n[INFO] Server dihentikan oleh pengguna.")
        httpd.server_close()

if __name__ == '__main__':
    jalankan_server_api()
```

3. Jalankan skrip di terminal: `python server_api_sekolah.py`.
4. Buka peramban (*web browser*) dan akses URL `http://localhost:8080/api/v1/siswa`. Amati bagaimana peramban menampilkan teks data berformat JSON secara instan!
5. Buka tab terminal kedua, lalu uji pengiriman data baru menggunakan perintah `curl`:
   ```bash
   curl -X POST http://localhost:8080/api/v1/siswa -H "Content-Type: application/json" -d "{\"nama\": \"Bagas Perkasa\", \"jurusan\": \"Teknik Komputer\"}"
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
"""
