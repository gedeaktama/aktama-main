"""
Modul Naskah Bab I Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB1_SMA11 = """# BAB I: PEMROGRAMAN BERORIENTASI OBJEK (OOP) DAN ENGINEERING PROCESS

## APERSEPSI: MENGAPA KODE PROSEDURAL KITA SULIT BERTAHAN?

Di laboratorium rekayasa perangkat lunak sekolah, Arya, Dinda, dan Bagas sedang berkumpul di depan monitor utama. Mereka sedang mengembangkan proyek sistem informasi klinik kesehatan dan akademik sekolah. Namun, seiring bertambahnya fitur, layar kode mereka yang sudah mencapai lebih dari 2.500 baris mulai menunjukkan kekacauan yang serius.

[GAMBAR: assets/bab1_komik_pembuka_sma11.png]

"Aduh, program kita semakin sulit dikendalikan!" keluh Bagas seraya menatap fungsi-fungsi prosedural yang bertumpuk. "Tadi aku baru saja menambahkan fungsi untuk menghitung tunjangan wali kelas, tetapi mendadak variabel global `gaji` tertimpa dan fungsi pembayaran dokter klinik ikut rusak! Semua variabel saling tumpang tindih!"

Dinda mengangguk seraya memeriksa catatan tim. "Bukan hanya itu, Bagas. Kemarin saat Arya mengedit berkas yang sama dan mengirimkannya lewat pesan percakapan, perubahan kode yang kubuat malam sebelumnya terhapus begitu saja karena tertimpa versi terbaru dari Arya. Kita tidak memiliki sistem yang melacak riwayat perubahan secara aman!"

Arya menarik napas lalu tersenyum menenangkan kedua rekannya. "Teman-teman, apa yang kita alami adalah fase pendewasaan seorang pengembang perangkat lunak. Selama ini kita terbiasa menulis kode prosedural linier di mana fungsi dan variabel global tercampur bebas. Pada proyek berskala industri, pendekatan ini tidak lagi memadai. Kita harus beralih ke paradigma **Pemrograman Berorientasi Objek (*Object-Oriented Programming* / OOP)**!"

"Dengan OOP," lanjut Arya, "kita membungkus data dan perilaku ke dalam cetak biru yang disebut **Class**, melindungi data sensitif dengan **Enkapsulasi**, memanfaatkan **Pewarisan** agar kode dapat digunakan kembali (*reusable*), dan menerapkan **Polimorfisme**. Selain itu, agar koding bersama kita tidak pernah saling menimpa lagi, kita wajib menerapkan sistem kendali versi profesional standar dunia: **Git dan platform GitHub**!"

"Luar biasa!" seru Bagas dan Dinda antusias. "Mari kita pelajari arsitektur OOP Python dan disiplin rekayasa perangkat lunak modern!"

---

## A. PARADIGMA PEMROGRAMAN: PROSEDURAL VS BERORIENTASI OBJEK (OOP)

Dalam sejarah ilmu komputer, paradigma pemrograman berkembang seiring dengan melonjaknya kompleksitas sistem perangkat lunak yang dibangun oleh manusia.

[GAMBAR: assets/bab1_diagram_arsitektur_oop_python.png]

### 1. Keterbatasan Paradigma Prosedural

Pada paradigma prosedural, program dipandang sebagai sekumpulan instruksi sekuensial yang mengeksekusi fungsi atau prosedur secara bertahap dari atas ke bawah. Data biasanya disimpan dalam variabel-variabel global atau struktur terpisah, kemudian dikirimkan sebagai argumen ke berbagai fungsi.

**Kelemahan Paradigma Prosedural pada Proyek Besar:**
- **Spaghetti Code & Variabel Global:** Ketika program membesar, variabel global rentan diubah secara tidak sengaja oleh fungsi lain, memicu galat tersembunyi (*side effects*) yang sangat sulit dilacak.
- **Rendahnya Penggunaan Ulang Kode (*Low Reusability*):** Jika kita ingin membuat entitas baru yang mirip (misalnya dari data Siswa ke data Mahasiswa), kita sering kali terpaksa menyalin-tempel (*copy-paste*) kode yang sama berulang-ulang.
- **Sulit Memodelkan Dunia Nyata:** Paradigma prosedural memisahkan antara data (kata benda) dan tindakan (kata kerja), padahal di alam nyata objek selalu memiliki karakteristik fisik (*state*) dan tindakan operasional (*behavior*) yang menyatu.

### 2. Revolusi Berorientasi Objek (OOP)

OOP memandang perangkat lunak sebagai suatu ekosistem interaksi antarentitas mandiri yang disebut **Objek (*Object*)**. Setiap objek merupakan perwujudan konkret dari sebuah cetak biru konseptual yang dinamakan **Kelas (*Class*)**.

- **Class (Cetak Biru / Blueprint):** Definisi abstrak yang menetapkan atribut apa saja yang dimiliki serta metode apa saja yang dapat dilakukan oleh objek tersebut.
- **Object (Wujud Nyata / Instance):** Entitas fisik di dalam memori komputer yang dibuat (*diinstansiasi*) berdasarkan cetak biru Class tertentu, memiliki nilai data atribut yang spesifik.

Sebagai analogi: Class adalah cetak biru gambar teknik arsitektur sebuah rumah modern. Berdasarkan satu cetak biru tersebut, pengembang dapat membangun ratusan rumah fisik nyata (*Objects*) di berbagai kavling tanah dengan warna cat tembok, nomor rumah, dan pemilik yang berbeda-beda.

---

## B. KONSTRUKTOR, ATRIBUT INSTANS, DAN METHOD DALAM PYTHON

Dalam bahasa pemrograman Python, sebuah kelas didefinisikan menggunakan kata kunci `class`. Mari kita bedah anatomi struktur dasarnya:

### 1. Metode Konstruktor `__init__()` dan Parameter `self`

Metode `__init__()` adalah metode khusus yang otomatis dieksekusi pertama kali oleh Python saat sebuah objek baru diciptakan (*diinstansiasi*) ke dalam memori. Metode ini lazim disebut sebagai **Konstruktor (*Constructor*)**, bertugas menginisialisasi atribut-atribut awal objek.

Parameter pertama pada setiap metode di dalam kelas wajib berupa kata kunci `self`. Parameter `self` merepresentasikan referensi eksplisit ke instans objek yang sedang aktif atau sedang memanggil metode tersebut.

```python
# Mendefinisikan Kelas Siswa
class Siswa:
    # Konstruktor penginisialisasi atribut instans
    def __init__(self, nisn, nama, jurusan):
        self.nisn = nisn          # Atribut instans: nomor induk
        self.nama = nama          # Atribut instans: nama lengkap
        self.jurusan = jurusan    # Atribut instans: bidang keahlian
        self.nilai_tugas = []     # Atribut instans: koleksi nilai

    # Metode untuk menambahkan nilai tugas
    def tambah_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.nilai_tugas.append(nilai)
            print(f">> Berhasil menambahkan nilai {nilai} untuk {self.nama}")
        else:
            print("[PERINGATAN] Nilai harus berada dalam rentang 0 hingga 100!")

    # Metode untuk menghitung rata-rata nilai
    def hitung_rata_rata(self):
        if not self.nilai_tugas:
            return 0.0
        return sum(self.nilai_tugas) / len(self.nilai_tugas)

# Menginstansiasi Objek Nyata di Memori
siswa_1 = Siswa("0081234567", "Arya Dinata", "Rekayasa Perangkat Lunak")
siswa_2 = Siswa("0089876543", "Dinda Kirana", "Sains Data & AI")

# Memanggil metode objek
siswa_1.tambah_nilai(88)
siswa_1.tambah_nilai(94)
print(f"Rata-rata {siswa_1.nama} : {siswa_1.hitung_rata_rata():.2f}")
```

---

## C. TIGA PILAR UTAMA OOP: ENKAPSULASI, PEWARISAN, DAN POLIMORFISME

Kekuatan arsitektur OOP ditopang oleh tiga pilar filosofis komputasi:

### 1. Enkapsulasi (Encapsulation) & Data Hiding

Enkapsulasi adalah prinsip membungkus data atribut dan metode operasionalnya ke dalam satu kesatuan terlindung, serta menyembunyikan detail implementasi internal dari akses langsung pihak luar (*Data Hiding*).

Tujuannya adalah menjaga integritas data agar tidak diubah sembarangan oleh kode di luar kelas. Dalam Python, penandaan hak akses privat dilakukan dengan memberikan awalan garis bawah ganda (`__`) pada nama atribut:
- **Atribut Publik (`self.nama`):** Dapat dibaca dan diubah bebas dari luar kelas.
- **Atribut Privat (`self.__saldo`):** Tidak dapat diakses langsung dari luar kelas. Akses hanya diizinkan melalui metode perantara yang aman: **Getter** (mengambil nilai) dan **Setter** (memvalidasi nilai sebelum diubah).

```python
class RekeningSekolah:
    def __init__(self, nomor_rekening, saldo_awal):
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo_awal  # Atribut privat (Encapsulated)

    # Getter: Metode membaca saldo secara aman
    def get_saldo(self):
        return self.__saldo

    # Setter: Metode mengubah saldo dengan validasi ketat
    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"[SETOR] Berhasil menambah Rp{jumlah:,}. Saldo baru: Rp{self.__saldo:,}")
        else:
            print("[GAGAL] Jumlah setoran harus lebih dari nol!")

akun = RekeningSekolah("REK-001", 500000)
# akun.__saldo = 100000000  # Tidak akan memengaruhi atribut privat asli!
akun.setor_tunai(150000)
print(f"Saldo resmi terverifikasi: Rp{akun.get_saldo():,}")
```

### 2. Pewarisan (Inheritance)

Pewarisan adalah mekanisme di mana sebuah kelas baru (**Kelas Turunan / Child Class**) dapat mewarisi seluruh atribut dan metode dari kelas yang sudah ada (**Kelas Induk / Parent Class**).

Pewarisan mengeliminasi duplikasi kode secara drastis (*Don't Repeat Yourself / DRY*). Python menyediakan fungsi bawaan `super()` yang memungkinkan kelas turunan memanggil konstruktor atau metode kelas induknya secara mulus.

```python
# Kelas Induk (Parent Class)
class AnggotaSekolah:
    def __init__(self, id_anggota, nama, email):
        self.id_anggota = id_anggota
        self.nama = nama
        self.email = email

    def tampilkan_profil(self):
        return f"[{self.id_anggota}] {self.nama} | Surel: {self.email}"

# Kelas Turunan 1: Siswa mewarisi AnggotaSekolah
class SiswaAkademik(AnggotaSekolah):
    def __init__(self, id_anggota, nama, email, kelas):
        super().__init__(id_anggota, nama, email)  # Panggil konstruktor induk
        self.kelas = kelas

# Kelas Turunan 2: Guru mewarisi AnggotaSekolah
class GuruPengajar(AnggotaSekolah):
    def __init__(self, id_anggota, nama, email, mata_pelajaran):
        super().__init__(id_anggota, nama, email)
        self.mata_pelajaran = mata_pelajaran
```

### 3. Polimorfisme (Polymorphism) & Method Overriding

Kata *Polimorfisme* berasal dari bahasa Yunani yang berarti "memiliki banyak bentuk". Dalam rekayasa perangkat lunak, polimorfisme memungkinkan metode dengan nama yang sama pada kelas-kelas yang berbeda mengeksekusi perilaku yang disesuaikan secara dinamis (*Method Overriding*).

```python
class Karyawan:
    def __init__(self, nama, gaji_dasar):
        self.nama = nama
        self.gaji_dasar = gaji_dasar

    def hitung_tunjangan(self):
        return 0  # Perilaku default kelas induk

class ManajerTeknis(Karyawan):
    def hitung_tunjangan(self):
        # Override: Manajer mendapat tunjangan manajerial 30%
        return self.gaji_dasar * 0.30

class StafAdmin(Karyawan):
    def hitung_tunjangan(self):
        # Override: Staf admin mendapat tunjangan operasional tetap
        return 500000

# Pengujian Polimorfisme dalam sebuah perulangan seragam
daftar_karyawan = [
    ManajerTeknis("Arya", 10000000),
    StafAdmin("Bagas", 5000000)
]

for k in daftar_karyawan:
    print(f"Karyawan: {k.nama} | Tunjangan: Rp{k.hitung_tunjangan():,}")
```

---

## D. REKAYASA PERANGKAT LUNAK: SIKLUS SDLC DAN MANAJEMEN VERSI GIT/GITHUB

Menulis kode yang elegan tidak akan bernilai komersial jika tidak dikelola dalam proses rekayasa perangkat lunak (*Software Engineering Process*) yang terstandarisasi.

[GAMBAR: assets/bab1_alur_kerja_git_github_flow.png]

### 1. Siklus Hidup Perangkat Lunak: SDLC (Software Development Life Cycle)

Perangkat lunak industri dikembangkan melalui pendekatan metodologi tangkas (**Agile / Scrum**) yang melibatkan tahapan berulang (*sprint iteratif*):
1. **Analisis Kebutuhan (*Requirements Analysis*):** Menghimpun spesifikasi fitur yang diinginkan pengguna akhir (*User Stories*).
2. **Perancangan Arsitektur (*System & Architecture Design*):** Menyusun diagram kelas UML, diagram basis data ERD, dan antarmuka UI/UX.
3. **Implementasi Koding (*Implementation*):** Menulis kode sumber modular berbasis standar OOP dan konvensi PEP 8.
4. **Pengujian Mandiri & Sistem (*Testing & Quality Assurance*):** Menjalankan pengujian fungsional dan penanganan galat (*Unit Testing*).
5. **Penerapan & Pemeliharaan (*Deployment & Maintenance*):** Merilis sistem ke lingkungan server produksi dan memantau kinerjanya.

### 2. Kolaborasi Tanpa Konflik: Git & GitHub

**Git** adalah sistem kendali versi terdistribusi (*Distributed Version Control System*) yang mencatat setiap jengkal riwayat perubahan kode sumber seperti mesin penjelajah waktu. **GitHub** adalah platform awan global tempat tim pengembang menyimpan repositori bersama, meninjau kode (*Code Review*), dan menyatukan hasil kerja (*Merge*).

**Perintah Terminal Git Esensial yang Wajib Dikuasai:**
- `git init`: Menginisialisasi direktori lokal menjadi repositori Git aktif.
- `git status`: Memeriksa kondisi berkas (apakah ada berkas baru atau yang dimodifikasi).
- `git add .`: Memindahkan seluruh perubahan berkas ke area persiapan (*Staging Area*).
- `git commit -m "Pesan Deskriptif"`: Mengabadikan snapshot versi kode ke riwayat lokal.
- `git branch nama-fitur`: Membuat cabang kerja terpisah agar eksperimen koding tidak merusak kode utama.
- `git switch nama-fitur`: Berpindah ke cabang fitur yang diinginkan.
- `git push origin nama-fitur`: Mengunggah cabang kode lokal ke repositori awan GitHub.
- **Pull Request (PR):** Mekanisme di GitHub di mana pengembang meminta izin kepada ketua tim untuk menggabungkan cabang fiturnya ke cabang utama (`main`) setelah melalui proses penelaahan kode secara teliti.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 1.1

### Rancang Bangun Sistem Manajemen Akademik OOP Berbasis Git

**Tujuan Pembelajaran:**
Peserta didik mampu merancang struktur kelas berorientasi objek yang memadukan konstruktor, enkapsulasi atribut privat, pewarisan kelas, dan polimorfisme, serta mengelola kode tersebut dalam alur kerja cabang (*branching*) sistem kendali versi Git secara kolaboratif.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 dan Git terpasang di terminal.
2. Akun GitHub aktif.
3. Visual Studio Code.

**Instruksi Kerja Praktikum:**
1. Buatlah folder proyek baru bernama `proyek_akademik_oop`.
2. Buka terminal di VS Code, lalu inisialisasi repositori Git lokal:
   ```bash
   git init
   git config user.name "Nama Siswa"
   git config user.email "email.siswa@sekolah.sch.id"
   ```
3. Buat berkas `akademik.py` dan ketikkan implementasi arsitektur OOP terpadu berikut:

```python
# Sistem Manajemen Akademik OOP Terpadu
class CivitasAkademika:
    def __init__(self, id_unik, nama_lengkap):
        self.id_unik = id_unik
        self.nama_lengkap = nama_lengkap
        self.__status_kehadiran = "Alfa"  # Privat: Data terenkapsulasi

    # Getter status
    def get_status(self):
        return self.__status_kehadiran

    # Setter presensi aman
    def set_presensi(self, status):
        status_valid = ["Hadir", "Sakit", "Izin", "Alfa"]
        if status in status_valid:
            self.__status_kehadiran = status
            print(f">> Presensi {self.nama_lengkap} dicatat: {status}")
        else:
            print("[GALAT] Status presensi tidak valid!")

    # Metode polimorfik dasar
    def get_peran(self):
        return "Civitas Sekolah Umum"

class Siswa(CivitasAkademika):
    def __init__(self, id_unik, nama_lengkap, kelas, jurusan):
        super().__init__(id_unik, nama_lengkap)
        self.kelas = kelas
        self.jurusan = jurusan

    # Method Overriding
    def get_peran(self):
        return f"Siswa Jurusan {self.jurusan} (Kelas {self.kelas})"

class Guru(CivitasAkademika):
    def __init__(self, id_unik, nama_lengkap, mata_pelajaran):
        super().__init__(id_unik, nama_lengkap)
        self.mata_pelajaran = mata_pelajaran

    # Method Overriding
    def get_peran(self):
        return f"Guru Pengampu: {self.mata_pelajaran}"

if __name__ == "__main__":
    daftar_warga = [
        Siswa("SIS-101", "Arya Dinata", "XI", "RPL"),
        Siswa("SIS-102", "Dinda Kirana", "XI", "Sains Data"),
        Guru("GUR-001", "Gede Erik Aktama", "Koding dan Kecerdasan Artifisial")
    ]

    print("===== DAFTAR WARGA AKADEMIK SEKOLAH =====")
    for w in daftar_warga:
        w.set_presensi("Hadir")
        print(f"[{w.id_unik}] {w.nama_lengkap} | Peran: {w.get_peran()} | Presensi: {w.get_status()}")
        print("-" * 50)
```

4. Simpan riwayat kerja ke Git:
   ```bash
   git add akademik.py
   git commit -m "feat: inisialisasi arsitektur OOP CivitasAkademika"
   ```
5. Buat cabang baru bernama `fitur-validasi`, tambahkan validasi panjang ID unik minimal 5 karakter, lalu lakukan *commit* dan gabungkan (*merge*) kembali ke cabang `main`!

**Pertanyaan Analisis Laboratorium:**
1. Apa yang terjadi jika kode di luar kelas mencoba mengubah status presensi secara langsung dengan perintah `siswa_1.__status_kehadiran = "Hadir"`? Mengapa enkapsulasi melindunginya?
2. Bagaimana pemanggilan fungsi `super().__init__()` membantu kita menghindari pengetikan ulang kode pada kelas turunan?
3. Mengapa di industri perangkat lunak modern para insinyur dilarang melakukan commit langsung ke cabang `main` dan diwajibkan menggunakan cabang fitur (*feature branch*) serta *Pull Request*?

---

## F. RANGKUMAN MATERI BAB I

1. **Paradigma OOP vs Prosedural:** Pendekatan prosedural rentan kekacauan akibat variabel global yang saling tumpang tindih pada proyek besar. OOP mengorganisasikan perangkat lunak sebagai interaksi objek nyata (*Object*) yang dibangun berdasarkan cetak biru konseptual (*Class*).
2. **Konstruktor dan Instansiasi:** Metode `__init__()` adalah konstruktor penginisialisasi data awal objek di memori, di mana parameter `self` merepresentasikan objek spesifik yang sedang aktif.
3. **Tiga Pilar Inti OOP:**
   - *Enkapsulasi:* Membungkus data dan melindungi variabel privat (`__atribut`) dengan metode perantara *getter* dan *setter*.
   - *Pewarisan (Inheritance):* Menurunkan atribut dan metode dari kelas induk ke kelas turunan melalui fungsi `super()`.
   - *Polimorfisme:* Menimpa metode induk (*method overriding*) agar metode bernama sama mengeksekusi perilaku yang kontekstual pada kelas turunan yang berbeda.
4. **SDLC dan Git/GitHub:** Pengembangan sistem profesional mengadopsi siklus hidup tangkas (Agile/Scrum). Version Control System Git dan platform GitHub memfasilitasi kerja tim yang aman, memungkinkan pelacakan riwayat perubahan kode, percabangan fitur terisolasi (*branching*), serta penelaahan kode sebelum disatukan (*Pull Request*).

---

## G. UJI KOMPETENSI BAB I

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Paradigma pemrograman yang memandang perangkat lunak sebagai sekumpulan entitas mandiri yang menggabungkan karakteristik data fisik dan perilaku operasional ke dalam satu unit disebut...
   A. Pemrograman Fungsional Murni
   B. Pemrograman Prosedural Terstruktur
   C. Pemrograman Berorientasi Objek (OOP)
   D. Pemrograman Logika Deklaratif

2. Dalam sintaksis bahasa Python, metode khusus yang otomatis pertama kali dijalankan ketika sebuah objek baru diinstansiasi ke dalam memori komputer adalah...
   A. `__main__()`
   B. `__init__()`
   C. `__start__()`
   D. `__class__()`

3. Peran utama dari kata kunci `self` pada definisi metode di dalam sebuah kelas Python adalah...
   A. Mengimpor pustaka eksternal secara otomatis
   B. Menghentikan program saat terjadi pembagian dengan angka nol
   C. Mereferensikan instans spesifik dari objek yang sedang memanggil metode tersebut
   D. Menghapus objek dari memori secara permanen

4. Prinsip dalam OOP yang menyembunyikan detail atribut internal objek menggunakan awalan garis bawah ganda (`__`) dan membatasi manipulasi langsung dari luar kelas dinamakan...
   A. Enkapsulasi (*Encapsulation*)
   B. Pewarisan (*Inheritance*)
   C. Polimorfisme (*Polymorphism*)
   D. Abstraksi Sekuensial

5. Perhatikan potongan kode berikut:
   ```python
   class Mobil:
       def klakson(self):
           return "Tin tin!"

   class Truk(Mobil):
       def klakson(self):
           return "Tonton!"
   ```
   Kemampuan kelas `Truk` untuk mengubah implementasi metode `klakson` yang diwarisi dari kelas `Mobil` merupakan penerapan dari pilar...
   A. Enkapsulasi
   B. Kompresi Data
   C. Polimorfisme (*Method Overriding*)
   D. Rekursi

6. Fungsi bawaan Python yang digunakan pada kelas turunan untuk memanggil metode konstruktor atau atribut yang dimiliki oleh kelas induk secara elegan adalah...
   A. `parent()`
   B. `super()`
   C. `master()`
   D. `base()`

7. Tahapan dalam Software Development Life Cycle (SDLC) yang berfokus pada penerjemahan spesifikasi kebutuhan dan diagram UML menjadi baris-baris kode fungsional di lingkungan pengembang dinamakan...
   A. Requirements Analysis
   B. Implementation (Coding)
   C. System Testing
   D. Maintenance

8. Perintah dasar terminal Git yang berfungsi untuk mengabadikan perubahan berkas yang telah berada di area *Staging* menjadi riwayat versi permanen disertai catatan penjelasan adalah...
   A. `git init`
   B. `git add .`
   C. `git commit -m "Pesan"`
   D. `git branch -d`

9. Mengapa dalam alur kolaborasi tim menggunakan Git dan GitHub, para pengembang dilarang melakukan commit langsung ke cabang `main`?
   A. Karena cabang main hanya bisa menampung berkas bertipe gambar
   B. Karena cabang main harus selalu dijaga dalam kondisi stabil, bebas galat, dan siap dirilis ke produksi melalui mekanisme penelaahan kode (*Pull Request*)
   C. Karena server GitHub akan menghapus akun jika ada commit di cabang main
   D. Karena cabang main tidak mendukung bahasa pemrograman Python

10. Perintah Git yang tepat untuk membuat sebuah cabang kerja baru bernama `fitur-pembayaran` sekaligus langsung berpindah ke cabang tersebut adalah...
    A. `git switch -c fitur-pembayaran`
    B. `git delete fitur-pembayaran`
    C. `git merge origin main`
    D. `git push --all`

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara Class dan Object dalam paradigma OOP! Berikan analogi konkret di dunia nyata selain analogi rumah dan cetak biru!
2. Mengapa keberadaan atribut privat (`__atribut`) dan penyediaan metode getter/setter (Enkapsulasi) sangat krusial dalam sistem transaksi perbankan atau kasir toko? Apa bahaya yang timbul jika seluruh atribut dibiarkan bersifat publik?
3. Rancanglah hierarki pewarisan kelas (*Inheritance*) untuk sistem perpustakaan:
   - Kelas Induk: `Buku` (atribut: `isbn`, `judul`, `pengarang`).
   - Kelas Turunan: `EBook` (tambahan atribut: `ukuran_berkas_mb` dan format berkas).
   Tuliskan blok kode Python lengkapnya menggunakan fungsi `super().__init__()`!
4. Jelaskan apa yang dimaksud dengan *Method Overriding* dalam pilar Polimorfisme! Bagaimana teknik ini membantu pengembang membangun sistem perangkat lunak yang fleksibel dan mudah diperluas (*scalable*)?
5. Uraikan alur kerja kolaborasi standar industri (*GitHub Flow*) ketika seorang anggota tim hendak menambahkan fitur baru ke dalam proyek perangkat lunak sekolah, mulai dari pembuatan cabang lokal hingga penggabungan (*merge*) di repositori awan!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB I

**Kunci Pilihan Ganda:**
1. **C** (OOP mengorganisasikan perangkat lunak sebagai objek yang menggabungkan state dan behavior).
2. **B** (Metode `__init__()` adalah konstruktor inisialisasi awal objek di memori).
3. **C** (`self` mereferensikan instans spesifik dari objek yang sedang memanggil metode).
4. **A** (Enkapsulasi membungkus data dan menyembunyikannya dari modifikasi langsung di luar kelas).
5. **C** (Method overriding menimpa metode induk, menerapkan pilar polimorfisme).
6. **B** (Fungsi `super()` merujuk pada pemanggilan konstruktor atau metode kelas induk).
7. **B** (Implementation adalah fase penulisan kode sumber program).
8. **C** (`git commit -m` mencatat snapshot permanen ke riwayat versi repositori lokal).
9. **B** (Cabang main dijaga kestabilannya agar selalu dalam status bebas galat siap produksi).
10. **A** (`git switch -c` membuat dan langsung berpindah ke cabang baru).

**Pembahasan Soal Uraian:**
1. *Class vs Object:*
   - Class adalah konsep cetak biru atau resep generik. Analoginya: cetakan kue aluminium berbentuk bintang.
   - Object adalah benda nyata fisik yang dihasilkan dari cetakan tersebut. Analoginya: kue bolu bintang rasa cokelat atau vanila yang dapat kita cicipi di piring.
2. *Pentingnya Enkapsulasi Saldo Bank:*
   Jika atribut `saldo` bersifat publik, kode di bagian lain sistem (atau skrip peretas) dapat langsung mengetikkan `rekening.saldo = 999999999` tanpa melalui prosedur validasi. Dengan enkapsulasi dan setter (`setor_tunai`), sistem dapat menyaring bahwa penambahan saldo hanya sah jika nilai uang bertipe numerik positif, melewati verifikasi PIN keamanan, dan dicatat dalam riwayat audit bank.
3. *Implementasi Pewarisan Perpustakaan:*
   ```python
   class Buku:
       def __init__(self, isbn, judul, pengarang):
           self.isbn = isbn
           self.judul = judul
           self.pengarang = pengarang

   class EBook(Buku):
       def __init__(self, isbn, judul, pengarang, ukuran_mb, format_file):
           super().__init__(isbn, judul, pengarang)
           self.ukuran_mb = ukuran_mb
           self.format_file = format_file
   ```
4. *Method Overriding dan Skalabilitas:*
   Method overriding adalah teknik di mana kelas turunan mendefinisikan ulang metode yang sudah ada di kelas induk untuk memberikan perilaku spesifik yang sesuai dengan karakteristik kelas turunan. Ini memungkinkan sistem diperluas tanpa mengubah kode yang sudah berjalan (*Open-Closed Principle*). Ketika modul baru ditambahkan (misalnya jenis metode pembayaran baru), pengembang cukup mewarisi kelas induk dan meng-override metode `bayar()`, sementara sistem utama tetap dapat memanggil metode tersebut secara seragam melalui polimorfisme.
5. *Alur Kerja GitHub Flow:*
   (1) Tarik pembaruan terbaru dari cabang utama (`git pull origin main`); (2) Buat cabang fitur baru (`git switch -c fitur-baru`); (3) Tulis kode program dan uji hingga berjalan sempurna; (4) Simpan riwayat perubahan lokal (`git add .` dan `git commit -m "feat: deskripsi"`); (5) Unggah cabang ke GitHub (`git push origin fitur-baru`); (6) Buat *Pull Request (PR)* di antarmuka web GitHub; (7) Anggota tim lain melakukan penelaahan kode (*code review*); (8) Jika disetujui, cabang fitur digabungkan (*merged*) ke cabang `main` dan cabang fitur dihapus.
"""
