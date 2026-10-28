"""
Modul Naskah Bab III Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB3_SMA10 = """# BAB III: BASIS DATA RELASIONAL DAN PERINTAH SQL

## APERSEPSI: MENGAPA SPREADSHEET GAGAL MENGELOLA DATA SEKOLAH?

Di ruang laboratorium komputer sekolah, guru pembina bidang sarana dan prasarana tampak sedang memeriksa tumpukan lembar kerja spreadsheet di komputernya. Dinda, Bagas, dan Arya yang bertugas sebagai tim asisten teknis lab memperhatikan bahwa ada kekacauan data yang cukup serius: beberapa komputer tercatat dipinjam oleh siswa yang namanya tertulis berbeda di lembar terpisah, sejumlah data perangkat keras memiliki nomor seri ganda, dan saat nama seorang guru diganti gelarnya, puluhan baris data lama tidak ikut terbarui.

[GAMBAR: assets/bab3_komik_pembuka_sma10.png]

"Pak Guru sedang mengalami masalah klasik yang disebut anomali data redundan," bisik Bagas kepada kedua sahabatnya. "Ketika data inventaris, data siswa, dan data peminjaman digabungkan dalam satu lembar spreadsheet datar (*flat sheet*), setiap kali ada transaksi baru, nama siswa dan spesifikasi komputer harus diketik ulang berulang-ulang."

"Benar sekali," sambung Dinda. "Jika ada 500 siswa yang meminjam laptop lab, nama siswa dan nomor induknya diketik 500 kali. Jika seorang siswa pindah kelas, petugas harus mengedit ratusan baris satu per satu. Jika terlewat satu baris saja, data sekolah menjadi inkonsisten dan tidak dapat dipercaya!"

Arya mengangguk setuju. "Itulah alasan mengapa dunia teknologi informasi beralih ke arsitektur **Basis Data Relasional (Relational Database Management System / RDBMS)**. Dengan memisahkan data ke dalam tabel-tabel terpisah yang saling terhubung menggunakan relasi kunci utama (*Primary Key*) dan kunci asing (*Foreign Key*), integritas data dijamin secara mutlak. Tidak ada data yang berulang secara sia-sia!"

"Dan kita bisa mengendalikan seluruh aliran data tersebut menggunakan bahasa standar dunia yang disebut SQL (*Structured Query Language*), bahkan menghubungkannya langsung dengan program Python kita!" seru Bagas bersemangat.

"Tepat sekali! Mari kita bedah bagaimana merancang arsitektur basis data relasional yang kokoh, membuat diagram ERD standar industri, dan mengeksekusi perintah SQL secara profesional!" ajak Arya.

---

## A. FONDASI BASIS DATA RELASIONAL: ENTITAS, ATRIBUT, PRIMARY KEY, DAN FOREIGN KEY

Basis data relasional pertama kali diperkenalkan oleh ilmuwan komputer Dr. Edgar F. Codd pada tahun 1970 di laboratorium riset IBM. Konsep ini merevolusi cara manusia menyimpan, mengorganisasikan, dan mengamankan informasi terstruktur dalam skala raksasa.

Dalam basis data relasional, dunia nyata dimodelkan ke dalam sekumpulan tabel dua dimensi yang terdiri atas baris (*records/tuples*) dan kolom (*fields/attributes*).

### 1. Komponen Inti Basis Data Relasional

1. **Entitas (Entity):** Suatu objek, orang, tempat, benda, atau peristiwa di dunia nyata yang informasinya ingin kita rekam dan kelola dalam sistem.
   *Contoh:* Siswa, Guru, Komputer_Lab, Peminjaman.
2. **Atribut (Attribute):** Ciri khas, karakteristik, atau data spesifik yang melekat pada suatu entitas (menjadi nama kolom dalam tabel).
   *Contoh pada Entitas Siswa:* `nisn`, `nama_lengkap`, `kelas`, `jurusan`, `tanggal_lahir`.
3. **Kunci Utama (Primary Key - PK):** Sebuah atribut atau kombinasi atribut unik yang dipilih untuk mengidentifikasi setiap baris data di dalam tabel secara pasti dan tunggal. Syarat mutlak Primary Key adalah nilainya **tidak boleh kosong (*NOT NULL*)** dan **tidak boleh ada duplikasi (*UNIQUE*)**.
   *Contoh:* Nomor Induk Siswa Nasional (`nisn`) pada tabel Siswa, atau nomor seri perangkat pada tabel Perangkat.
4. **Kunci Asing (Foreign Key - FK):** Sebuah atribut di dalam suatu tabel yang nilainya merujuk pada Primary Key tabel lain. Keberadaan Foreign Key inilah yang menjembatani hubungan relasional antartabel dan menegakkan prinsip **Integritas Referensial (*Referential Integrity*)**.

### 2. Bahaya Redudansi dan Anomali Data pada Spreadsheet Datar

Jika kita memaksakan diri menyimpan seluruh informasi dalam satu lembar kerja tabel datar tanpa relasi, sistem akan menderita tiga anomali mematikan:
- **Anomali Penyisipan (Insertion Anomaly):** Ketidakmampuan merekam data entitas tertentu sebelum data entitas lain tersedia (misalnya kita tidak bisa mendaftarkan perangkat komputer baru di lab jika belum ada siswa yang meminjamnya).
- **Anomali Penghapusan (Deletion Anomaly):** Terhapusnya data penting yang tidak sengaja hilang ketika kita menghapus data transaksi (misalnya menghapus riwayat peminjaman siswa mengakibatkan data spesifikasi teknis komputer ikut lenyap terhapus).
- **Anomali Pembaruan (Update Anomaly):** Terjadinya inkonsistensi saat pembaruan data hanya berhasil pada sebagian baris namun gagal pada baris lainnya karena data yang sama diketik berulang di banyak tempat.

---

## B. PERANCANGAN MODEL DATA: ENTITY RELATIONSHIP DIAGRAM (ERD) NOTASI CROW'S FOOT

Sebelum menuliskan perintah kode basis data, seorang arsitek data profesional wajib merancang cetak biru model konseptual menggunakan **Entity Relationship Diagram (ERD)**. Notasi visual yang menjadi standar de facto industri perangkat lunak global saat ini adalah **Notasi Kaki Gagak (*Crow's Foot Notation*)**.

[GAMBAR: assets/bab3_diagram_erd_crows_foot_sekolah.png]

### 1. Kardinalitas dan Modalitas Relasi Crow's Foot

Notasi Crow's Foot menggunakan simbol visual di ujung garis relasi untuk menunjukkan kardinalitas (jumlah minimum dan maksimum kemunculan hubungan entitas):

- **Garis Lurus Ganda (`||`):** Menunjukkan relasi *Exactly One* (Pasti Satu dan Wajib).
- **Lingkaran dan Garis Lurus (`O|`):** Menunjukkan relasi *Zero or One* (Nol atau Satu / Opsional Tunggal).
- **Kaki Gagak dengan Garis Lurus (`|<`):** Menunjukkan relasi *One or Many* (Satu atau Banyak / Wajib Jamak).
- **Lingkaran dengan Kaki Gagak (`O<`):** Menunjukkan relasi *Zero or Many* (Nol atau Banyak / Opsional Jamak).

### 2. Tiga Jenis Relasi Fundamental dalam Basis Data

1. **Relasi Satu ke Satu (One-to-One / 1:1):**
Satu baris pada Tabel A hanya boleh berpasangan dengan maksimal satu baris pada Tabel B, dan sebaliknya.
*Contoh:* Setiap Siswa memiliki tepat satu Akun_Portal_Sekolah.
2. **Relasi Satu ke Banyak (One-to-Many / 1:N):**
Satu baris pada Tabel A dapat berpasangan dengan banyak baris pada Tabel B, namun setiap baris pada Tabel B hanya boleh merujuk pada satu baris di Tabel A.
*Contoh:* Satu Jurusan memiliki banyak Siswa, namun seorang Siswa hanya terdaftar di satu Jurusan.
3. **Relasi Banyak ke Banyak (Many-to-Many / M:N):**
Satu baris pada Tabel A dapat berpasangan dengan banyak baris di Tabel B, dan satu baris di Tabel B dapat berpasangan dengan banyak baris di Tabel A. Dalam arsitektur RDBMS fisik, relasi M:N tidak dapat dibuat langsung dan **wajib dipecah** menjadi dua relasi 1:N menggunakan sebuah tabel perantara (*Junction Table / Associative Entity*).
*Contoh:* Banyak Siswa dapat meminjam banyak Buku di perpustakaan. Tabel perantaranya adalah tabel `Peminjaman` yang menampung FK dari Siswa dan FK dari Buku.

---

## C. SINTAKS DASAR SQL: DDL DAN DML

**SQL (Structured Query Language)** adalah bahasa deklaratif terstandarisasi yang dirancang khusus untuk berinteraksi dengan RDBMS. Perintah dalam SQL dikelompokkan menjadi dua pilar utama:

[GAMBAR: assets/bab3_tabel_arsitektur_perintah_sql.png]

### 1. Data Definition Language (DDL)

DDL adalah kelompok perintah SQL yang digunakan untuk mendefinisikan, mengubah, atau menghapus struktur arsitektur basis data dan tabel (cetak biru skema):
- `CREATE TABLE`: Membuat tabel baru beserta definisi nama kolom, tipe data, dan konstrain integritas.
- `ALTER TABLE`: Memodifikasi struktur tabel yang sudah ada (menambah kolom baru atau mengubah tipe data).
- `DROP TABLE`: Menghapus tabel beserta seluruh data di dalamnya secara permanen dari sistem.

```sql
-- Contoh Perintah DDL Membuat Tabel Kategori dan Tabel Perangkat
CREATE TABLE kategori (
    id_kategori INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kategori TEXT NOT NULL UNIQUE
);

CREATE TABLE perangkat (
    id_perangkat TEXT PRIMARY KEY,
    nama_perangkat TEXT NOT NULL,
    id_kategori INTEGER NOT NULL,
    kondisi TEXT DEFAULT 'Baik',
    FOREIGN KEY (id_kategori) REFERENCES kategori (id_kategori)
);
```

### 2. Data Manipulation Language (DML)

DML adalah kelompok perintah SQL yang digunakan untuk mengelola dan memanipulasi data yang tersimpan di dalam baris-baris tabel:
- `INSERT INTO`: Menambahkan baris data baru ke dalam tabel.
- `SELECT`: Mengambil, menampilkan, menyaring, dan menganalisis data dari satu atau banyak tabel.
- `UPDATE`: Memperbarui nilai kolom pada baris data yang memenuhi kondisi tertentu.
- `DELETE`: Menghapus baris data tertentu berdasarkan filter kriteria yang ditentukan.

```sql
-- Menambahkan data baru (INSERT)
INSERT INTO kategori (nama_kategori) VALUES ('Komputer PC'), ('Laptop'), ('Proyektor');

INSERT INTO perangkat (id_perangkat, nama_perangkat, id_kategori, kondisi)
VALUES ('PC-LAB-01', 'PC All-in-One Core i5', 1, 'Baik'),
       ('LPT-05', 'Laptop ThinkPad L14', 2, 'Baik');

-- Menampilkan data dengan relasi JOIN dan filter WHERE
SELECT p.id_perangkat, p.nama_perangkat, k.nama_kategori, p.kondisi
FROM perangkat p
JOIN kategori k ON p.id_kategori = k.id_kategori
WHERE p.kondisi = 'Baik'
ORDER BY p.id_perangkat ASC;

-- Memperbarui kondisi perangkat (UPDATE)
UPDATE perangkat 
SET kondisi = 'Perbaikan' 
WHERE id_perangkat = 'PC-LAB-01';

-- Menghapus data perangkat tertentu (DELETE)
DELETE FROM perangkat 
WHERE id_perangkat = 'LPT-05';
```

---

## D. INTEGRASI DATABASE RELASIONAL PYTHON MENGGUNAKAN MODUL LOKAL SQLITE3

Salah satu keistimewaan bahasa Python adalah tersedianya modul bawaan bernama `sqlite3`. Modul ini memungkinkan kita membuat, mengelola, dan menghubungkan aplikasi perangkat lunak dengan mesin basis data relasional mandiri tanpa perlu menginstal perangkat lunak server database eksternal yang rumit.

### 1. Siklus Aliran Kerja Koneksi Python ke SQLite

1. Membuka koneksi basis data menggunakan `sqlite3.connect("nama_file.db")`.
2. Membuat objek kursor perantara (*Cursor*) menggunakan `conn.cursor()`. Kursor bertindak sebagai eksekutor perintah SQL ke mesin database.
3. Menjalankan perintah SQL melalui metode `cursor.execute()`.
4. Mengamankan perubahan data permanen ke media penyimpanan dengan `conn.commit()`.
5. Mengambil hasil kueri penelusuran data dengan `cursor.fetchall()` atau `cursor.fetchone()`.
6. Menutup kursor dan koneksi database secara aman (`conn.close()`).

### 2. Pencegahan Serangan Keamanan SQL Injection

Dalam pemrograman perangkat lunak komersial, jangan pernah menggabungkan variabel teks pengguna secara langsung (*string concatenation*) ke dalam sintaks perintah SQL:
- **BERBAHAYA (Rentan Injeksi):** `cursor.execute(f"SELECT * FROM user WHERE nama = '{input_user}'")`
- **AMAN (Parameterized Query):** `cursor.execute("SELECT * FROM user WHERE nama = ?", (input_user,))`

Tanda tanya (`?`) adalah *placeholder* parameter aman yang memastikan mesin database memperlakukan masukan pengguna murni sebagai data mentah, bukan sebagai instruksi kode SQL yang dapat meretas sistem.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 3.1

### Proyek Sistem Inventarisasi Fasilitas Laboratorium Komputer Sekolah

**Tujuan Pembelajaran:**
Peserta didik mampu merancang struktur basis data relasional inventaris lab komputer, menulis skrip Python integratif dengan pustaka `sqlite3` untuk membuat tabel, menyisipkan data, melakukan kueri relasional `JOIN`, serta menyajikan laporan inventaris yang rapi dan konsisten.

**Alat dan Bahan:**
1. Komputer/Laptop dengan interpreter Python 3.
2. Kode editor (Visual Studio Code atau editor teks lainnya).

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `inventaris_lab_sekolah.py`.
2. Ketikkan dan pelajari kode implementasi lengkap basis data relasional berikut:

```python
import sqlite3

def inisialisasi_basis_data():
    # Membuat koneksi ke berkas database lokal
    koneksi = sqlite3.connect("inventaris_lab.db")
    kursor = koneksi.cursor()

    # Mengaktifkan penegakan integritas kunci asing (Foreign Key)
    kursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Membuat Tabel Ruang Laboratorium
    kursor.execute('''
        CREATE TABLE IF NOT EXISTS ruang_lab (
            id_ruang TEXT PRIMARY KEY,
            nama_ruang TEXT NOT NULL,
            kapasitas INTEGER NOT NULL
        )
    ''')

    # 2. Membuat Tabel Aset Komputer
    kursor.execute('''
        CREATE TABLE IF NOT EXISTS aset_komputer (
            kode_aset TEXT PRIMARY KEY,
            merk_spesifikasi TEXT NOT NULL,
            id_ruang TEXT NOT NULL,
            status_operasional TEXT DEFAULT 'Normal',
            FOREIGN KEY (id_ruang) REFERENCES ruang_lab (id_ruang)
                ON UPDATE CASCADE ON DELETE RESTRICT
        )
    ''')

    # Menyisipkan Data Sampel Ruang Lab
    daftar_ruang = [
        ("LAB-RPL", "Laboratorium Rekayasa Perangkat Lunak", 36),
        ("LAB-AI", "Laboratorium Komputasi Cerdas & AI", 30),
        ("LAB-MM", "Laboratorium Multimedia & Desain", 32)
    ]
    kursor.executemany('''
        INSERT OR IGNORE INTO ruang_lab (id_ruang, nama_ruang, kapasitas)
        VALUES (?, ?, ?)
    ''', daftar_ruang)

    # Menyisipkan Data Sampel Aset Komputer
    daftar_komputer = [
        ("PC-RPL-01", "Core i7 Gen 13, RAM 16GB, SSD 512GB", "LAB-RPL", "Normal"),
        ("PC-RPL-02", "Core i7 Gen 13, RAM 16GB, SSD 512GB", "LAB-RPL", "Normal"),
        ("PC-AI-01", "Ryzen 9, RTX 4070 12GB, RAM 32GB", "LAB-AI", "Normal"),
        ("PC-AI-02", "Ryzen 9, RTX 4070 12GB, RAM 32GB", "LAB-AI", "Perbaikan"),
        ("PC-MM-01", "Apple iMac 24 inch M3, RAM 16GB", "LAB-MM", "Normal")
    ]
    kursor.executemany('''
        INSERT OR IGNORE INTO aset_komputer (kode_aset, merk_spesifikasi, id_ruang, status_operasional)
        VALUES (?, ?, ?, ?)
    ''', daftar_komputer)

    koneksi.commit()
    koneksi.close()
    print("[SUKSES] Skema basis data dan data awal berhasil diinisialisasi!")

def tampilkan_laporan_inventaris():
    koneksi = sqlite3.connect("inventaris_lab.db")
    kursor = koneksi.cursor()

    # Kueri Relasional JOIN antar-tabel
    kueri = '''
        SELECT a.kode_aset, a.merk_spesifikasi, r.nama_ruang, a.status_operasional
        FROM aset_komputer a
        JOIN ruang_lab r ON a.id_ruang = r.id_ruang
        ORDER BY r.id_ruang ASC, a.kode_aset ASC
    '''
    kursor.execute(kueri)
    hasil = kursor.fetchall()

    print("\n" + "=" * 80)
    print("        LAPORAN REKAPITULASI ASET LABORATORIUM KOMPUTER SEKOLAH")
    print("=" * 80)
    print(f"{'KODE ASET':<12} | {'SPESIFIKASI PERANGKAT':<34} | {'LOKASI RUANG':<18} | {'STATUS'}")
    print("-" * 80)
    for baris in hasil:
        print(f"{baris[0]:<12} | {baris[1]:<34} | {baris[2]:<18} | {baris[3]}")
    print("=" * 80)

    koneksi.close()

if __name__ == "__main__":
    inisialisasi_basis_data()
    tampilkan_laporan_inventaris()
```

**Pertanyaan dan Tugas Analisis:**
1. Jalankan kode di atas, kemudian periksa tabel yang terbentuk menggunakan ekstensi penampil SQLite!
2. Tambahkan satu fungsi baru bernama `ubah_status_komputer(kode_aset, status_baru)` yang mengeksekusi perintah SQL `UPDATE` berbasis parameter aman!
3. Ujilah prinsip integritas referensial: Apa yang terjadi jika kalian mencoba menghapus baris ruang lab `LAB-RPL` sementara di tabel aset komputer masih terdapat perangkat yang merujuk padanya? Mengapa sistem menolak perintah tersebut?

---

## F. RANGKUMAN MATERI BAB III

1. **Fondasi Basis Data Relasional:** Menyimpan data dalam tabel dua dimensi terstruktur. Kunci Utama (*Primary Key*) menjamin keunikan identitas baris data, sedangkan Kunci Asing (*Foreign Key*) membangun jembatan relasi integritas referensial antartabel untuk mengeliminasi anomali redundansi data.
2. **Entity Relationship Diagram (ERD) Notasi Crow's Foot:** Standar pemodelan visual untuk memetakan hubungan antarentitas dengan simbol kardinalitas tunggal, jamak, wajib, dan opsional. Relasi Banyak ke Banyak (M:N) harus dinormalisasi menjadi dua relasi 1:N menggunakan tabel perantara (*Junction Table*).
3. **Pilar Perintah SQL:**
   - *DDL (Data Definition Language):* Mendefinisikan cetak biru struktur tabel (`CREATE`, `ALTER`, `DROP`).
   - *DML (Data Manipulation Language):* Memanipulasi data di dalam tabel (`INSERT`, `SELECT`, `UPDATE`, `DELETE`).
4. **Integrasi Python dan Keamanan Database:** Modul `sqlite3` menyediakan mesin RDBMS lokal yang praktis dan ringan. Penerapan *Parameterized Queries* (`?`) wajib digunakan untuk menangkal ancaman serangan siber *SQL Injection*.

---

## G. UJI KOMPETENSI BAB III

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Atribut atau kolom khusus dalam sebuah tabel basis data yang dipilih untuk mengidentifikasi setiap rekaman baris secara unik, tidak boleh bernilai kosong (NOT NULL), dan tidak boleh duplikat disebut...
   A. Foreign Key
   B. Primary Key
   C. Composite Index
   D. Candidate View

2. Dalam perancangan diagram ERD dengan notasi Crow's Foot, simbol ujung garis yang digambarkan dengan lingkaran kecil diikuti oleh cabang tiga kaki gagak merepresentasikan kardinalitas relasi...
   A. Tepat satu (Exactly One)
   B. Satu atau banyak (One or Many)
   C. Nol atau banyak (Zero or Many)
   D. Nol atau satu (Zero or One)

3. Perintah SQL yang tergolong ke dalam kelompok Data Definition Language (DDL) dan digunakan untuk menambahkan kolom baru pada tabel yang sudah ada adalah...
   A. `UPDATE TABLE`
   B. `ALTER TABLE`
   C. `INSERT INTO`
   D. `MODIFY COLUMN`

4. Manakah di antara perintah SQL berikut yang digunakan untuk menampilkan data dari tabel `siswa` yang hanya memiliki nilai ujian di atas 85 dan diurutkan dari nilai tertinggi ke terendah?
   A. `SELECT * FROM siswa WHERE nilai > 85 ORDER BY nilai DESC;`
   B. `SELECT * FROM siswa HAVING nilai > 85 GROUP BY nilai ASC;`
   C. `SELECT ALL FROM siswa WHERE nilai > 85 SORT BY nilai DOWN;`
   D. `INSERT INTO siswa WHERE nilai > 85 ORDER BY nilai DESC;`

5. Apabila dua entitas memiliki hubungan Banyak ke Banyak (Many-to-Many / M:N), solusi arsitektural yang wajib diterapkan dalam perancangan basis data relasional fisik adalah...
   A. Menggabungkan kedua tabel menjadi satu spreadsheet datar
   B. Menghapus salah satu entitas agar tidak terjadi relasi jamak
   C. Menambahkan tabel perantara (*Junction Table*) yang menampung Foreign Key dari kedua entitas
   D. Mengubah tipe data Primary Key menjadi teks desimal

6. Klausa dalam perintah SQL `SELECT` yang berfungsi untuk menggabungkan dua atau lebih tabel berdasarkan kolom kunci yang berkesesuaian adalah...
   A. `WHERE`
   B. `JOIN`
   C. `UNION`
   D. `GROUP BY`

7. Pada modul Python `sqlite3`, metode manakah yang wajib dipanggil untuk memastikan perubahan penambahan, pembaruan, atau penghapusan data tersimpan secara permanen ke dalam berkas media penyimpanan?
   A. `cursor.execute()`
   B. `cursor.fetchall()`
   C. `connection.commit()`
   D. `connection.close()`

8. Praktik perancangan kode kueri SQL berikut ini:
   `cursor.execute("SELECT * FROM akun WHERE username = ?", (input_nama,))`
   bertujuan utama untuk melindungi sistem perangkat lunak dari ancaman siber yang dinamakan...
   A. Denial of Service (DoS)
   B. Cross-Site Scripting (XSS)
   C. SQL Injection
   D. Phishing Attack

9. Perintah SQL yang tepat untuk mengubah data kolom `kondisi` menjadi 'Rusak Ringan' pada tabel `perangkat` khusus untuk perangkat yang memiliki `id_perangkat` bernilai 'PC-04' adalah...
   A. `ALTER perangkat SET kondisi = 'Rusak Ringan' WHERE id_perangkat = 'PC-04';`
   B. `UPDATE perangkat SET kondisi = 'Rusak Ringan' WHERE id_perangkat = 'PC-04';`
   C. `INSERT INTO perangkat (kondisi) VALUES ('Rusak Ringan') WHERE id_perangkat = 'PC-04';`
   D. `SELECT perangkat SET kondisi = 'Rusak Ringan' WHERE id_perangkat = 'PC-04';`

10. Keberadaan konsep Integritas Referensial (*Referential Integrity*) dalam sistem basis data relasional berfungsi untuk...
    A. Menjamin bahwa data dalam format tabel dapat diekspor menjadi format gambar
    B. Mempercepat koneksi internet yang menghubungkan pengguna dengan server
    C. Menjamin bahwa nilai kunci asing (Foreign Key) selalu merujuk secara valid pada baris data kunci utama (Primary Key) yang benar-benar ada di tabel induk
    D. Menghapus seluruh baris data secara otomatis setiap 24 jam sekali

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara Data Definition Language (DDL) dan Data Manipulation Language (DML) dalam sintaks SQL! Berikan masing-masing dua contoh perintah nyatanya beserta fungsinya!
2. Mengapa sebuah basis data relasional jauh lebih unggul dan aman dibandingkan penyimpanan arsip menggunakan berkas spreadsheet konvensional dalam konteks pengelolaan data berskala besar? Uraikan kaitannya dengan anomali redundansi!
3. Diberikan kasus: Sebuah perpustakaan sekolah ingin mencatat peminjaman buku oleh siswa. Hubungan antara Siswa dan Buku bersifat *Many-to-Many*. Rancanglah struktur tiga tabel relasional yang diperlukan (sebutkan nama tabel, kolom atribut, Primary Key, dan Foreign Key yang menghubungkannya)!
4. Tuliskan blok sintaks SQL DDL lengkap untuk membuat sebuah tabel bernama `guru_pengampu` dengan kolom: `nip` (teks, Primary Key), `nama_guru` (teks, tidak boleh kosong), `mata_pelajaran` (teks), dan `email` (teks, unik)!
5. Jelaskan mekanisme kerja serangan siber *SQL Injection* pada aplikasi web atau sistem informasi, dan jelaskan secara teknis mengapa teknik *Parameterized Query* pada Python mampu menangkal serangan tersebut hingga ke akarnya!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB III

**Kunci Pilihan Ganda:**
1. **B** (Primary Key mengidentifikasi rekaman secara unik, NOT NULL, dan UNIQUE).
2. **C** (Simbol lingkaran dan kaki gagak menunjukkan kardinalitas Nol atau Banyak / Zero or Many).
3. **B** (`ALTER TABLE` adalah perintah DDL untuk memodifikasi struktur skema tabel).
4. **A** (`SELECT ... WHERE nilai > 85 ORDER BY nilai DESC` menyaring nilai dan mengurutkannya menurun).
5. **C** (Relasi Many-to-Many dipecah menggunakan tabel perantara/junction table).
6. **B** (Klausa `JOIN` menggabungkan data antartabel berbasis kolom kunci relasi).
7. **C** (`connection.commit()` menyimpan transaksi secara permanen ke media penyimpanan).
8. **C** (Parameterized query mencegah manipulasi instruksi perintah melalui serangan SQL Injection).
9. **B** (`UPDATE ... SET ... WHERE ...` adalah sintaks standar DML pembaruan data).
10. **C** (Integritas referensial memastikan Foreign Key selalu merujuk pada data Primary Key yang sah di tabel master).

**Pembahasan Soal Uraian:**
1. *Perbedaan DDL dan DML:*
   - DDL (Data Definition Language) berurusan dengan perancangan struktur skema tabel. Contoh: `CREATE TABLE` (membuat tabel baru) dan `DROP TABLE` (menghapus tabel dari skema).
   - DML (Data Manipulation Language) berurusan dengan manipulasi isi baris data di dalam tabel. Contoh: `INSERT INTO` (menambah data) dan `SELECT` (mengambil data).
2. *Keunggulan RDBMS atas Spreadsheet:*
   RDBMS memecah data ke dalam tabel-tabel ternormalisasi sehingga tidak ada penulisan data yang berulang-ulang (*redundansi*). Pada spreadsheet, jika data ditulis berkali-kali, pembaruan data di satu sel rawan menimbulkan anomali di mana data lain tidak terbarui (*update anomaly*). Selain itu, RDBMS memiliki mekanisme proteksi integritas referensial dan manajemen transaksi ACID (*Atomicity, Consistency, Isolation, Durability*).
3. *Rancangan Tiga Tabel Perpustakaan (Many-to-Many):*
   - Tabel 1 `siswa`: `nisn` (PK), `nama`, `kelas`.
   - Tabel 2 `buku`: `kode_buku` (PK), `judul`, `penulis`, `stok`.
   - Tabel 3 `peminjaman` (Junction Table): `id_pinjam` (PK), `nisn` (FK merujuk ke tabel siswa), `kode_buku` (FK merujuk ke tabel buku), `tanggal_pinjam`, `status_kembali`.
4. *Sintaks SQL DDL Tabel guru_pengampu:*
   ```sql
   CREATE TABLE guru_pengampu (
       nip TEXT PRIMARY KEY,
       nama_guru TEXT NOT NULL,
       mata_pelajaran TEXT NOT NULL,
       email TEXT UNIQUE
   );
   ```
5. *Mekanisme SQL Injection dan Mitigasinya:*
   SQL Injection terjadi ketika masukan pengguna digabungkan langsung secara mentah ke dalam string kueri SQL. Peretas dapat memasukkan teks berbahaya seperti `' OR '1'='1` yang mengubah logika kueri dan membobol autentikasi. Teknik *Parameterized Query* (`?`) memisahkan sintaks perintah SQL dengan nilai parameter. Interpreter SQL mengompilasi struktur perintah terlebih dahulu sebelum parameter disisipkan, sehingga karakter kutip atau operator peretas diperlakukan murni sebagai teks data biasa dan tidak akan dieksekusi sebagai instruksi bahasa.
"""
