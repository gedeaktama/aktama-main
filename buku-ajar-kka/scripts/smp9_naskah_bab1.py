# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 1 Buku Siswa KKA Kelas 9 SMP (Fase D)
BAB I: JEMBATAN KODING BLOK MENUJU PEMROGRAMAN TEKSTUAL PYTHON (18 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_1_SMP9 = """# BAB I JEMBATAN KODING BLOK MENUJU PEMROGRAMAN TEKSTUAL PYTHON

## MISI 1: PROGRAMMER PYTHON MUDA NUSANTARA
* **Alokasi Waktu:** 18 Jam Pelajaran (9 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK)
* **Target Lencana Koder:** Medali Emas Programmer Python Muda (Fase D)

---

## A. PENDAHULUAN: LANGKAH BESAR MENUJU DUNIA TEKS PYTHON

Suasana laboratorium komputer SMP Nusantara terasa berbeda pagi ini. Tidak ada lagi kucing oranye Scratch atau blok-blok puzzle warna-warni di layar monitor siswa. Di hadapan Rian, Ayu, dan Fajar, layar komputer menampilkan antarmuka editor teks modern dengan latar belakang gelap yang elegan.

"Aduh, Rian!" keluh Ayu sambil menatap kursor berkedip di layar konsol yang masih kosong. "Biasanya kita tinggal menyeret balok biru untuk bergerak atau balok kuning untuk pengkondisian. Sekarang tidak ada tombol bantuan visual sama sekali! Semuanya harus kita ketik secara manual huruf demi huruf. Bagaimana kalau kita salah ketik satu huruf saja?"

[[IMAGE: bab1_komik_pembuka_smp9.png | Gambar 1.1: Komik Pembuka Bab 1: Langkah Besar Menuju Dunia Teks Python]]

Rian tersenyum tenang sambil mengetikkan sebaris perintah pendek: `print("Halo Ayu dan Fajar! Selamat datang di dunia Python!")`. Seketika, saat tombol *Run* ditekan, kalimat ramah itu muncul seketika di layar terminal bawah.

"Lihat, Ayu! Ternyata tidak seseram yang kita bayangkan, kan?" ujar Rian ramah. "Bahasa pemrograman teks bernama **Python** ini dirancang dengan filosofi keindahan dan kemudahan baca (*readability*). Kata-katanya sangat mirip dengan percakapan bahasa Inggris sehari-hari. Kita tidak perlu lagi disibukkan oleh tanda kurung kurawal yang rumit seperti pada bahasa C++ atau Java kuno."

Fajar menimpali dengan antusias. "Dan yang paling membanggakan, Python bukan sekadar alat latihan di sekolah! Bahasa Python adalah bahasa nomor satu yang digunakan oleh para ilmuwan data di NASA, pengembang kecerdasan artifisial di Google, hingga pembuat efek visual film di Hollywood! Dengan menguasai Python di kelas IX ini, kita sedang memegang paspor menuju panggung teknologi global!"

Ayu menarik napas lega, rasa cemasnya kini berganti menjadi semangat menyala. "Baiklah! Mari kita seberangi jembatan koding blok ini dan buktikan bahwa kita mampu menjadi programmer Python muda yang tangguh!"

---

## B. MENGAPA SAINS KOMPUTASI MODERN MENGGUNAKAN BAHASA PYTHON?

Di kelas VII dan VIII, kalian telah membangun fondasi logika komputasi yang kokoh menggunakan lingkungan pemrograman visual (*visual block coding*). Mengapa sekarang, di kelas IX, kita harus beralih ke bahasa pemrograman tekstual (*text-based programming*)?

[[IMAGE: bab1_jembatan_scratch_ke_python.png | Gambar 1.2: Jembatan Komputasi: Perbandingan Blok Visual Scratch Menuju Sintaks Bersih Python]]

### Keterbatasan Koding Blok vs Keunggulan Bahasa Tekstual
Meskipun koding blok sangat ramah bagi pemula, lingkungan blok memiliki beberapa keterbatasan mendasar ketika kita ingin memecahkan masalah komputasi dunia nyata:
1. **Kecepatan dan Skala Proyek:** Menyeret ribuan balok visual untuk aplikasi pengolah data besar akan membuat layar menjadi sangat penuh, lambat, dan melelahkan tangan. Mengetik kode teks jauh lebih cepat dan efisien.
2. **Keterbatasan Ekosistem:** Aplikasi koding blok umumnya berdiri sendiri di dalam ekosistem tertutup (hanya bisa berjalan di situs pembuatnya). Sementara bahasa Python dapat berinteraksi langsung dengan sistem operasi komputer, database perbankan, kamera sensor fisik, hingga server web di seluruh dunia.
3. **Standar Industri Kecerdasan Artifisial:** Bahasa Python diciptakan oleh seorang matematikawan dan programmer Belanda bernama **Guido van Rossum** pada tahun 1991. Van Rossum merancang Python dengan prinsip: *"Kode program jauh lebih sering dibaca oleh manusia daripada dieksekusi oleh mesin."* Oleh karena itu, sintaks Python dibuat sangat bersih, elegan, dan minim simbol rumit, menjadikannya pilihan mutlak bagi pengembangan model *Machine Learning* dan *Artificial Intelligence* modern.

---

## C. LINGKUNGAN KERJA PYTHON & PERINTAH CETAK PERTAMA: print()

Untuk menulis dan menjalankan program Python, kita dapat menggunakan editor gratis seperti **IDLE Python**, **Visual Studio Code**, atau lingkungan komputasi awan ramah pemula seperti **Google Colaboratory (Google Colab)** yang dapat diakses langsung melalui peramban web tanpa perlu instalasi rumit.

[[IMAGE: bab1_anatomi_sintaks_python_dasar.png | Gambar 1.3: Anatomi Sintaks Dasar Bahasa Python: Variabel, Input, dan Aturan Indentasi]]

### Perintah Paling Legendaris: print()
Perintah dasar pertama yang wajib dikuasai adalah fungsi `print()`. Fungsi ini bertugas menampilkan keluaran (*output*) berupa teks, angka, atau hasil perhitungan ke layar konsol monitor pengguna.

Perhatikan aturan penulisan `print()` berikut:
```python
# Mencetak teks string (wajib diapit tanda petik satu ' atau petik dua ")
print("Selamat datang di Laboratorium Sains Komputasi SMP!")

# Mencetak angka matematika (tidak boleh menggunakan tanda petik)
print(2025)

# Mencetak hasil operasi hitung otomatis
print(15 + 25 * 2)   # Hasil yang keluar di layar adalah 65
```

> **Wawasan Koder: Jangan Lupakan Baris Komentar (#)**  
> Tanda pagar (`#`) digunakan untuk menuliskan **Komentar (*Comments*)**. Komputer akan secara otomatis mengabaikan teks apa pun yang berada di belakang tanda `#`. Komentar ditulis murni untuk membantu diri kita sendiri atau rekan satu tim mengingat fungsi dari blok kode tersebut. Menulis komentar yang jelas adalah tanda koder yang bertanggung jawab!

---

## D. VARIABEL, TIPE DATA, & INPUT INTERAKTIF

Program komputer tidak akan berguna jika hanya menampilkan teks statis. Sebuah program harus mampu menyimpan data di memori dan berinteraksi secara dinamis dengan penggunanya.

### 1. Mengenal Variabel dan Tiga Tipe Data Utama
Variabel adalah sebuah "kotak penyimpanan berlabel" di dalam memori komputer yang dapat menyimpan sebuah nilai. Nilai di dalam kotak tersebut dapat diubah-ubah (*variable*) sepanjang program berjalan.

Di dalam Python, terdapat tiga tipe data dasar yang paling sering digunakan:
* **String (`str`):** Tipe data teks atau kumpulan karakter alfabet/simbol yang selalu diapit tanda petik. Contoh: `"Rian Pratama"`, `"SMP Nusantara"`, `"A"`.
* **Integer (`int`):** Tipe data bilangan bulat (positif, negatif, atau nol) tanpa pecahan. Contoh: `14`, `-5`, `100`.
* **Float (`float`):** Tipe data bilangan desimal atau pecahan yang ditandai dengan tanda titik (*bukan koma!*). Contoh: `3.14`, `72.5`, `0.08`.

```python
# Membuat variabel dan menetapkan nilainya
nama_siswa = "Ayu Sekar"    # Tipe data String
usia = 14                   # Tipe data Integer
tinggi_badan = 158.5        # Tipe data Float
```

### 2. Menerima Input Dinamis dari Pengguna: input()
Untuk membuat program interaktif yang meminta data dari pengguna melalui papan ketik (*keyboard*), kita menggunakan fungsi `input()`.

Perhatikan hal sangat krusial ini: **Fungsi `input()` di Python secara baku (default) SELALU menghasilkan data bertipe String (teks)!**
Jika kalian meminta pengguna memasukkan angka untuk dijumlahkan:
```python
# PERINGATAN: Cara yang salah!
angka1 = input("Ketik angka pertama: ")   # Pengguna mengetik 5 (disimpan sebagai teks "5")
angka2 = input("Ketik angka kedua: ")     # Pengguna mengetik 3 (disimpan sebagai teks "3")
print(angka1 + angka2)                   # Hasilnya BUKAN 8, melainkan teks "53"!
```

Agar komputer memperlakukan masukan tersebut sebagai angka matematika murni, kita wajib melakukan **Konversi Tipe Data (*Type Casting*)** menggunakan fungsi `int()` atau `float()`:
```python
# CARA YANG BENAR DENGAN TYPE CASTING:
angka1 = int(input("Ketik angka pertama: "))   # Dikonversi menjadi integer 5
angka2 = int(input("Ketik angka kedua: "))     # Dikonversi menjadi integer 3
print("Hasil penjumlahan:", angka1 + angka2)  # Menghasilkan angka 8 yang benar!
```

---

## E. STRUKTUR KEPUTUSAN MULTI-KONDISI: if - elif - else & ATURAN INDENTASI

Dalam kehidupan sehari-hari, kita sering membuat keputusan bertingkat. Jika nilai rapor kita di atas 85, kita mendapat predikat A; jika nilai antara 70-84 mendapat B; jika nilai antara 60-69 mendapat C; dan jika di bawah 60 kita harus mengikuti remedial.

Dalam bahasa Python, keputusan multi-kondisi ini disusun menggunakan struktur: `if - elif - else`. Kata `elif` merupakan singkatan elegan dari *else-if*.

[[IMAGE: bab1_struktur_kondisi_if_elif_else.png | Gambar 1.4: Struktur Keputusan Multi-Kondisi: Diagram Alur dan Kode if - elif - else]]

### Aturan Emas Indentasi Python (The 4-Space Rule)
Berbeda dengan bahasa pemrograman lain yang menggunakan tanda kurung kurawal `{ }` untuk menandai blok percabangan, Python menggunakan **Indentasi** (ruang kosong menjorok ke dalam, standarnya adalah **4 spasi** atau satu kali tombol *Tab*).

Setiap kali kalian menuliskan tanda titik dua (`:`) di akhir baris `if`, `elif`, atau `else`, baris di bawahnya **WAJIB MENJOROK** ke dalam! Jika spasinya tidak lurus atau lupa menjorok, Python akan langsung memprotes dengan pesan galat: `IndentationError`!

```python
# Program Penentu Kategori Nilai Ujian
nilai = int(input("Masukkan nilai ujian sains komputasi (0-100): "))

if nilai >= 85:
    print("Predikat: A (Istimewa / Sangat Mahir)")
    print("Selamat atas pencapaian belajarmu yang luar biasa!")
elif nilai >= 70:
    print("Predikat: B (Mahir / Tuntas)")
    print("Hasil yang sangat baik, terus pertahankan!")
elif nilai >= 60:
    print("Predikat: C (Cukup)")
    print("Perlu sedikit penguatan pada konsep logika lanjutan.")
else:
    print("Predikat: D (Perlu Bimbingan Khusus)")
    print("Jangan putus asa! Mari pelajari kembali modul latihan bersama tutor.")
```

---

## F. PERULANGAN OTOMATIS BERHITUNG: for DAN range()

Bayangkan jika guru meminta kalian menuliskan teks *"Saya berjanji akan belajar koding dengan tekun"* sebanyak 100 kali. Jika diketik manual baris demi baris, jari kalian pasti akan kram dan lelah!

Di dalam Python, kita dapat memanfaatkan perulangan `for` yang dipadukan dengan fungsi pencacah deret angka `range()`.

### Memahami Fungsi range()
Fungsi `range(awal, akhir, langkah)` menghasilkan urutan deretan angka.
* `range(5)` -> Menghasilkan angka: 0, 1, 2, 3, 4 (Perhatikan: angka batas akhir 5 tidak diikutsertakan!).
* `range(1, 6)` -> Menghasilkan angka: 1, 2, 3, 4, 5.
* `range(2, 11, 2)` -> Menghasilkan deret bilangan genap: 2, 4, 6, 8, 10 (melompat 2 langkah).

Contoh mencetak tabel perkalian 7 secara otomatis hanya dalam 3 baris kode:
```python
print("--- TABEL PERKALIAN 7 OTOMATIS ---")
for i in range(1, 11):
    hasil = i * 7
    print(f"7 x {i} = {hasil}")
```

Hanya dalam sekejap mata, komputer akan menghitung dan mencetak sepuluh baris perkalian dengan rapi tanpa ada satu pun angka yang keliru!

---

## G. LKPD PLUGGED 1.1: MEMBANGUN KALKULATOR INDEKS MASSA TUBUH (IMT) REMAJA

### Aktivitas Praktik Mandiri dan Kolaboratif (Plugged Activity)
* **Tujuan Proyek:** Membangun aplikasi konsol Python interaktif untuk menghitung Indeks Massa Tubuh (IMT / BMI) siswa dan memberikan saran gaya hidup sehat.
* **Rumus Medis IMT:** `IMT = Berat_Badan (kg) / (Tinggi_Badan (m) * Tinggi_Badan (m))`
* **Kategori Standar Kesehatan Kemenkes RI:**
  * IMT < 17.0: Sangat Kurus (Kekurangan berat badan tingkat berat)
  * 17.0 <= IMT < 18.5: Kurus (Kekurangan berat badan tingkat ringan)
  * 18.5 <= IMT <= 25.0: Normal (Berat badan ideal sehat)
  * 25.0 < IMT <= 27.0: Gemuk (Kelebihan berat badan tingkat ringan)
  * IMT > 27.0: Obesitas (Kelebihan berat badan tingkat berat)

### Langkah-Langkah Penulisan Kode Program:
Buka editor Python (IDLE / Colab), buat file baru `kalkulator_imt.py`, dan ketikkan kode berikut dengan teliti:

```python
# ==============================================================
# PROYEK SAINS KODING KELAS IX SMP NUSANTARA
# APLIKASI KALKULATOR INDEKS MASSA TUBUH (IMT) REMAJA
# Penulis: Rian, Ayu, dan Fajar
# ==============================================================

print("==================================================")
print("   PROGRAM DETEKTIF KESEHATAN REMAJA: KALKULATOR IMT")
print("==================================================")

# 1. Mengambil input data dari pengguna
nama = input("Nama Lengkap Siswa : ")
berat = float(input("Berat Badan (kg)   : "))
tinggi_cm = float(input("Tinggi Badan (cm)  : "))

# 2. Mengonversi tinggi badan dari centimeter ke meter
tinggi_m = tinggi_cm / 100.0

# 3. Menghitung nilai IMT berdasarkan rumus matematika
imt = berat / (tinggi_m * tinggi_m)

# 4. Melakukan pembulatan 2 angka di belakang desimal
imt_bulat = round(imt, 2)

print("\n---------------- HASIL EVALUASI KESEHATAN ----------------")
print(f"Halo, sahabat {nama}!")
print(f"Skor Indeks Massa Tubuh (IMT) Anda: {imt_bulat}")

# 5. Struktur keputusan if-elif-else menentukan kategori
if imt < 17.0:
    kategori = "Sangat Kurus"
    saran = "Tingkatkan asupan kalori bergizi dan konsultasi ke dokter gizi."
elif imt < 18.5:
    kategori = "Kurus"
    saran = "Perbanyak konsumsi makanan tinggi protein sehat dan istirahat cukup."
elif imt <= 25.0:
    kategori = "Normal / Ideal"
    saran = "Luar biasa! Pertahankan pola makan sehat dan rutin berolahraga."
elif imt <= 27.0:
    kategori = "Gemuk (Kelebihan Berat)"
    saran = "Kurangi makanan manis dan perbanyak aktivitas jalan kaki 30 menit."
else:
    kategori = "Obesitas"
    saran = "Atur pola makan seimbang dan konsultasikan program diet sehat."

print(f"Status Kategori Fisik : {kategori}")
print(f"Saran Gaya Hidup Sehat: {saran}")
print("==========================================================")
```

### Lembar Pengujian Siswa:
Jalankan program di atas dengan menekan tombol F5 / Run, lalu uji dengan data tiga orang teman sekelas kalian. Catat hasilnya pada tabel berikut:
| Nama Responden | Berat (kg) | Tinggi (cm) | Hasil IMT | Kategori Status | Sesuai Rumus? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1. ... | ... | ... | ... | ... | Ya / Tidak |
| 2. ... | ... | ... | ... | ... | Ya / Tidak |
| 3. ... | ... | ... | ... | ... | Ya / Tidak |

---

## POJOK KARAKTER & ETIKA KODER: KETELITIAN MENGHADAPI PESAN GALAT (SYNTAX ERROR)

Ketika kalian beralih ke pemrograman teks Python, kalian pasti akan menjumpai layar merah bertuliskan: `SyntaxError: invalid syntax` atau `NameError: name 'hasil' is not defined`. 

Jangan pernah merasa cemas, frustrasi, atau menganggap diri kalian tidak berbakat menjadi programmer! Bagi seorang insinyur perangkat lunak profesional, **pesan galat (*error message*) bukanlah tanda kegagalan, melainkan petunjuk kompas yang sangat berharga**. Komputer sedang berbaik hati memberitahukan kepada kalian: pada baris nomor berapa kesalahan terjadi, dan tanda baca apa yang terlewat (misal: kurang tanda tutup kurung atau salah ketik huruf besar-kecil).

Belajar koding teks melatih karakter **Ketelitian**, **Kesabaran**, dan **Daya Juang (*Resilience*)**. Seorang pembelajar sejati tersenyum saat menemukan galat, membaca pesannya dengan cermat, memperbaikinya dengan tenang, dan bersorak gembira saat program berhasil dieksekusi dengan sempurna!

---

## RANGKUMAN MATERI BAB 1

1. **Bahasa Python** adalah bahasa pemrograman tekstual berstandar internasional yang dirancang dengan sintaks sederhana, bersih, dan mudah dibaca menyerupai bahasa Inggris, serta menjadi standar baku pengembangan sains data dan kecerdasan artifisial global.
2. **Fungsi print()** digunakan untuk mencetak keluaran teks (diapit tanda petik) atau angka ke layar konsol terminal. Tanda `#` digunakan untuk menuliskan baris komentar penjelas yang diabaikan komputer.
3. **Variabel dan Tipe Data:**
   * `str` untuk teks karakter alfabet.
   * `int` untuk bilangan bulat tanpa pecahan.
   * `float` untuk bilangan desimal bertanda titik.
4. **Fungsi input()** secara baku menghasilkan tipe data string, sehingga memerlukan konversi eksplisit (*type casting*) seperti `int(input())` atau `float(input())` jika akan digunakan dalam operasi matematika.
5. **Struktur if - elif - else** digunakan untuk mengambil keputusan bertingkat multi-kondisi, di mana setiap blok kode di bawah tanda titik dua wajib mematuhi aturan baku **Indentasi 4 Spasi**.
6. **Perulangan for dan range()** mengotomatisasi eksekusi deret instruksi hitung berulang dengan efisiensi tinggi dan presisi mutlak.

---

## UJI PEMAHAMAN HOTS BAB 1

### I. Pilihan Ganda (Pilihlah Jawaban yang Paling Tepat!)

1. Perhatikan sebaris kode Python berikut:
   `print("10" + "20")`
   Keluaran yang akan tampil pada layar terminal saat program dijalankan adalah...
   A. 30  
   B. 1020  
   C. Error  
   D. 10 20  

2. Fajar ingin membuat program yang meminta pengguna memasukkan umur dalam bentuk bilangan bulat. Sintaks Python yang paling tepat dan tidak menghasilkan galat saat umur dijumlahkan adalah...
   A. `umur = input("Masukkan umur: ")`  
   B. `umur = int(input("Masukkan umur: "))`  
   C. `umur = print("Masukkan umur: ")`  
   D. `umur = float("Masukkan umur: ")`  

3. Ayu menuliskan kode program berikut di komputernya:
   ```python
   skor = 90
   if skor > 75:
   print("Selamat Anda Lulus!")
   ```
   Saat dijalankan, program menolak dieksekusi dan memunculkan pesan galat: `IndentationError: expected an indented block`. Penyebab kesalahan tersebut adalah...
   A. Kata `skor` tidak boleh diawali huruf kecil  
   B. Angka 90 seharusnya diapit tanda petik dua  
   C. Baris `print` tidak menjorok ke dalam (kurang spasi indentasi) setelah tanda titik dua pada pernyataan `if`  
   D. Tanda lebih besar `>` dilarang digunakan dalam bahasa Python  

4. Perhatikan potongan kode berikut:
   ```python
   suhu = 28.5
   print(type(suhu))
   ```
   Tipe data yang akan ditampilkan oleh fungsi `type()` adalah...
   A. `<class 'int'>`  
   B. `<class 'str'>`  
   C. `<class 'float'>`  
   D. `<class 'bool'>`  

5. Diberikan skrip Python penentu status tiket bioskop:
   ```python
   usia = 16
   if usia >= 18:
       kategori = "Dewasa"
   elif usia >= 13:
       kategori = "Remaja"
   else:
       kategori = "Anak-anak"
   print(kategori)
   ```
   Keluaran teks yang akan tercetak di layar adalah...
   A. Dewasa  
   B. Remaja  
   C. Anak-anak  
   D. Tidak ada keluaran  

6. Berapakah deret angka yang dihasilkan oleh fungsi `range(2, 9, 3)` di dalam sebuah perulangan `for`?
   A. 2, 3, 4, 5, 6, 7, 8, 9  
   B. 2, 5, 8  
   C. 3, 6, 9  
   D. 2, 9, 3  

7. Perhatikan potongan kode berikut:
   ```python
   total = 0
   for i in range(1, 4):
       total = total + i
   print(total)
   ```
   Nilai akhir variabel `total` yang dicetak di layar adalah...
   A. 4  
   B. 6  
   C. 10  
   D. 3  

8. Karakter khusus dalam bahasa Python yang digunakan untuk menandai awal sebuah baris komentar yang tidak dieksekusi oleh komputer adalah...
   A. `//`  
   B. `<!--`  
   C. `#`  
   D. `/* ... */`  

9. Mengapa para peneliti kecerdasan artifisial dan sains data di seluruh dunia lebih memilih bahasa Python dibandingkan bahasa pemrograman visual blok?
   A. Karena bahasa Python tidak membutuhkan listrik untuk menjalankannya  
   B. Karena Python memiliki sintaks teks yang ringkas, mudah dibaca, dan didukung ribuan pustaka (*libraries*) matematika dan AI siap pakai  
   C. Karena bahasa Python adalah satu-satunya bahasa yang diizinkan PBB  
   D. Karena ukuran file installer Python di komputer selalu di bawah 1 Kilobyte  

10. Sikap mental ilmiah yang paling tepat ketika seorang siswa mendapati kodenya mengalami pesan galat (*syntax error*) di layar komputer adalah...
    A. Langsung mematikan paksa komputer dan menyerah belajar  
    B. Menyalahkan teman sekelompok yang duduk di sebelahnya  
    C. Bersikap tenang, membaca nomor baris dan keterangan galat yang tertulis, lalu menelusuri letak kesalahan tanda baca dengan teliti  
    D. Menghapus seluruh file pekerjaan dari harddisk  

---

### II. Uraian Pemecahan Masalah (Jawablah Secara Rinci dan Terstruktur!)

1. Jelaskan perbedaan mendasar antara pemrograman visual berbasis blok (seperti Scratch) dengan pemrograman tekstual (seperti Python)! Sebutkan dua alasan mengapa siswa kelas IX SMP perlu menguasai koding berbasis teks!
2. Mengapa aturan indentasi spasi dalam bahasa Python sangat penting dan bersifat wajib? Apa perbedaan pendekatan Python dalam menandai blok kode dibandingkan bahasa pemrograman yang menggunakan tanda kurung kurawal `{ }`?
3. Analisislah mengapa potongan kode Python berikut menghasilkan keluaran yang keliru:
   ```python
   panjang = input("Masukkan panjang lapangan: ")
   lebar = input("Masukkan lebar lapangan: ")
   luas = panjang * lebar
   print("Luas lapangan adalah:", luas)
   ```
   Jelaskan letak kesalahannya dan tuliskan perbaikan baris kode yang benar!
4. Rancanglah sebuah skrip program Python lengkap untuk menentukan tarif parkir kendaraan bermotor di area sekolah dengan ketentuan:
   * 2 jam pertama dikenakan tarif flat Rp2.000.
   * Setiap jam berikutnya dikenakan tarif tambahan Rp1.000 per jam.
   Program meminta input lama jam parkir dari pengguna dan mencetak total biaya parkir yang harus dibayar!
5. Bagaimana proses penelusuran pesan galat (*debugging*) saat belajar bahasa pemrograman tekstual dapat melatih ketelitian nalar kritis dan daya juang (*growth mindset*) seorang siswa?

---

## KUNCI JAWABAN UJI PEMAHAMAN TERPILIH BAB 1

### Kunci Jawaban Pilihan Ganda:
1. **B** (Karena "10" dan "20" diapit tanda petik, keduanya diperlakukan sebagai teks string sehingga operator `+` menggabungkan keduanya menjadi "1020", bukan menjumlahkan nilainya).
2. **B** (Fungsi `int(input())` wajib digunakan untuk mengonversi masukan teks dari pengguna menjadi bilangan bulat).
3. **C** (Python mewajibkan indentasi spasi pada blok di bawah pernyataan `if`).
4. **C** (Nilai 28.5 adalah bilangan desimal bertanda titik yang diklasifikasikan sebagai tipe data float).
5. **B** (Karena usia 16 tahun memenuhi syarat kondisi kedua `usia >= 13`, kategori yang ditetapkan adalah "Remaja").
6. **B** (Fungsi `range(2, 9, 3)` mulai dari angka 2, melompat 3 angka: 2, 5, 8; angka batas akhir 9 tidak diikutsertakan).
7. **B** (Perulangan berjalan untuk i = 1, 2, 3. Perhitungan akumulasi: 0 + 1 = 1 -> 1 + 2 = 3 -> 3 + 3 = 6).
8. **C** (Tanda `#` adalah simbol resmi penulisan komentar satu baris di Python).
9. **B** (Python digemari karena keterbacaan kodenya yang tinggi dan ekosistem pustaka sains data/AI yang sangat luas).
10. **C** (Membaca pesan galat secara tenang dan sistematis adalah etika koder tangguh berdaya nalar kritis).
"""
