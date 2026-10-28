"""
Modul Naskah Bab II Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB2_SMA10 = """# BAB II: PEMROGRAMAN PYTHON TERAPAN DAN STRUKTUR DATA KOLEKSI

## APERSEPSI: MENGAPA PROGRAM KASIR MENDADAK CRASH?

Koperasi siswa SMA Garuda Kirana sore itu mendadak dipadati antrean panjang siswa yang ingin membeli perlengkapan praktikum dan makanan ringan. Di balik meja kasir, Bagas tampak panik menatap layar monitor terminal kasirnya yang mendadak dipenuhi baris tulisan merah tebal berkedip. Program kasir berbasis Python yang dirancangnya berhenti beroperasi secara mendadak (*crash*).

[GAMBAR: assets/bab2_komik_pembuka_sma10.png]

"Dinda, Arya, tolong kemari sebentar!" seru Bagas pelan dengan nada cemas. "Aplikasi kasirku mati total! Tadi seorang pembeli salah mengetikkan huruf 'O' bukannya angka '0' saat memasukkan jumlah barang. Seketika itu juga programnya berhenti paksa dan kasir tidak bisa melayani transaksi lagi!"

Dinda dan Arya bergegas menghampiri meja kasir. Dinda membaca pesan kesalahan di layar terminal. "Lihat pesan ini, Bagas: `ValueError: invalid literal for int() with base 10: 'O'`. Fungsi konversi integer programmu tidak siap menerima masukan tak terduga dari pengguna manusia."

Arya mengangguk seraya menunjuk struktur kode di layar. "Selain itu, perhatikan bagaimana kamu menyimpan daftar harga barang. Kamu menyimpannya di dalam dua buah *List* terpisah yang rentan salah indeks. Ketika kasir mencari kode barang yang belum terdaftar, program langsung melempar galat `IndexError` atau `ValueError`. Sistem perangkat lunak kelas industri tidak boleh membiarkan galat mematikan seluruh alur program!"

"Benar sekali," sambung Dinda. "Dalam dunia nyata, pengguna komputer adalah manusia biasa yang bisa salah ketik (*human error*). Perangkat lunak yang profesional harus memiliki mekanisme pertahanan yang tangguh: struktur data koleksi yang tepat seperti *Dictionary* untuk pencarian instan O(1), serta arsitektur penanganan kesalahan (*exception handling*) dengan blok `try-except` agar program tetap berjalan mulus meskipun terjadi galat."

"Menakjubkan! Jadi, kode program kita bisa dibuat kebal terhadap kesalahan masukan pengguna?" tanya Bagas dengan mata berbinar.

"Tentu saja! Mari kita pelajari struktur data koleksi Python tingkat lanjut, seni penanganan eksepsi, dan disiplin kode bersih standar PEP 8!" ajak Arya dengan antusias.

---

## A. STRUKTUR DATA KOLEKSI PYTHON: LIST, TUPLE, SET, DAN DICTIONARY

Dalam pemrograman prosedural dasar di jenjang sebelumnya, kalian telah mengenal variabel sederhana untuk menyimpan satu nilai tunggal (seperti sebuah angka bulat atau sebaris teks). Namun, dalam aplikasi nyata—mulai dari sistem manajemen inventaris hingga jaringan saraf kecerdasan artifisial—kita membutuhkan wadah komputasi yang mampu menampung, mengorganisasikan, dan memanipulasi ribuan bahkan jutaan data majemuk secara terstruktur.

Python menyediakan empat struktur data koleksi bawaan (*built-in collection data structures*) yang sangat tangguh:

[GAMBAR: assets/bab2_arsitektur_struktur_data_python.png]

### 1. List (Daftar Terurut dan Mutable)

*List* adalah kumpulan elemen berurutan yang bersifat dinamis dan dapat diubah isinya (*mutable*). Elemen dalam List dapat ditambah, dihapus, atau diubah nilainya sewaktu-waktu selama program berjalan.

**Ciri Khas List:**
- Didefinisikan menggunakan kurung siku `[...]`.
- Elemen memiliki indeks numerik terurut mulai dari 0.
- Mengizinkan keberadaan nilai duplikat (*allows duplicates*).
- Kompleksitas waktu akses elemen berdasarkan indeks adalah konstan O(1). Namun, pencarian nilai tertentu berordo O(n).

```python
# Contoh manipulasi List
katalog_produk = ["Buku Tulis", "Pensil 2B", "Penghapus", "Penggaris"]
katalog_produk.append("Spidol")       # Menambah di akhir
katalog_produk[1] = "Pensil Mekanik"  # Mengubah nilai indeks ke-1
print("Katalog terbaru:", katalog_produk)
```

### 2. Tuple (Koleksi Terurut dan Tetap / Immutable)

*Tuple* memiliki kemiripan dengan List dalam hal keterurutan indeks, namun bersifat mutlak tidak dapat diubah (*immutable*). Sekali sebuah Tuple dibuat di memori, elemen di dalamnya tidak dapat ditambah, dihapus, atau dimodifikasi posisinya.

**Kapan Menggunakan Tuple?**
Tuple digunakan untuk menyimpan data konstanta yang harus terlindungi dari modifikasi tidak disengaja oleh bagian program lain (seperti koordinat GPS lokasi toko, resolusi layar default, atau konfigurasi koneksi database). Selain itu, Tuple mengonsumsi memori lebih hemat dan dieksekusi lebih cepat dibandingkan List.

```python
# Contoh deklarasi Tuple
koordinat_toko = (-6.175392, 106.827153) # Latitude dan Longitude
resolusi_layar = (1920, 1080)
# resolusi_layar[0] = 1280  # AKAN MENGHASILKAN GALAT TypeError!
print(f"Resolusi layar: {resolusi_layar[0]} x {resolusi_layar[1]} piksel")
```

### 3. Set (Himpunan Unik Tanpa Urutan)

*Set* mengadopsi konsep himpunan dalam matematika. Set adalah kumpulan elemen unik yang tidak berurutan (*unordered*) dan tidak memiliki sistem indeks numerik.

**Kelebihan Utama Set:**
- Menjamin tidak ada elemen duplikat secara otomatis (*unique elements*).
- Memiliki operasi himpunan bawaan yang sangat cepat: Irisan (*Intersection* `&`), Gabungan (*Union* `|`), dan Selisih (*Difference* `-`).
- Pengujian keanggotaan (`x in my_set`) beroperasi dalam waktu instan O(1) karena berbasis tabel hash (*hash table*).

```python
# Contoh penerapan Set untuk menyaring pembeli unik
pembeli_pagi = {"Arya", "Dinda", "Bagas", "Siti"}
pembeli_sore = {"Bagas", "Rian", "Dinda", "Fajar"}

# Siapakah pembeli yang berbelanja di pagi DAN sore hari? (Irisan)
pembeli_loyal = pembeli_pagi & pembeli_sore
print("Pembeli pagi dan sore:", pembeli_loyal)
```

### 4. Dictionary (Koleksi Pasangan Kunci-Nilai / Key-Value Pairs)

*Dictionary* adalah struktur data paling krusial dan serbaguna dalam ekosistem Python modern, serta menjadi fondasi format pertukaran data web (JSON) dan sistem kecerdasan artifisial. Dictionary menyimpan elemen berpasangan antara Kunci unik (*Key*) dan Nilai terkait (*Value*).

**Kekuatan Magis Dictionary:**
Pencarian data pada Dictionary tidak memerlukan perulangan penelusuran dari awal (*linear search*). Komputer menggunakan fungsi hash untuk langsung menemukan lokasi memori tempat nilai tersimpan berdasarkan kuncinya. Kompleksitas pencarian, penyisipan, dan penghapusan data rata-rata bernilai **O(1)**!

```python
# Contoh penerapan Dictionary pada katalog harga barang
daftar_harga = {
    "BRG001": {"nama": "Buku Tulis", "harga": 5000, "stok": 50},
    "BRG002": {"nama": "Pensil 2B", "harga": 3000, "stok": 120},
    "BRG003": {"nama": "Penghapus", "harga": 2000, "stok": 45}
}

# Mengakses data instan O(1)
kode = "BRG002"
print(f"Nama: {daftar_harga[kode]['nama']}, Harga: Rp{daftar_harga[kode]['harga']}")
```

---

## B. MEKANISME PENANGANAN GALAT (*EXCEPTION HANDLING*) TRY-EXCEPT-ELSE-FINALLY

Dalam siklus hidup perangkat lunak, terdapat perbedaan mendasar antara kesalahan sintaks (*syntax error*) dan galat waktu berjalan (*runtime error/exception*). Kesalahan sintaks terjadi saat kode melanggar tata bahasa Python dan terdeteksi sebelum program dijalankan. Namun, eksepsi terjadi ketika sintaks kode benar, tetapi timbul situasi abnormal saat eksekusi—seperti pembagian dengan nol, berkas tidak ditemukan, atau pengguna memasukkan teks huruf ketika program meminta angka.

[GAMBAR: assets/bab2_alur_exception_handling_try_except.png]

### 1. Anatomi Blok Penanganan Eksepsi Python

Python menyediakan arsitektur penanganan kesalahan yang elegan melalui struktur empat blok: `try`, `except`, `else`, dan `finally`:

1. **Blok `try`:** Menampung baris kode berbahaya yang berpotensi memicu galat.
2. **Blok `except`:** Menangkap eksepsi spesifik yang timbul, mengisolasi galat, dan mengeksekusi instruksi pemulihan tanpa mematikan program.
3. **Blok `else`:** Dieksekusi secara otomatis HANYA JIKA tidak ada eksepsi yang muncul pada blok `try`.
4. **Blok `finally`:** Dieksekusi secara mutlak dalam kondisi apa pun, baik terjadi galat maupun tidak. Blok ini sangat vital untuk membersihkan sumber daya sistem, seperti menutup koneksi basis data atau menutup berkas dokumen.

### 2. Jenis-Jenis Eksepsi Standar yang Wajib Dikenali

- `ValueError`: Nilai masukan memiliki tipe yang sesuai namun konten nilainya tidak valid (misalnya `int("abc")`).
- `ZeroDivisionError`: Percobaan operasi matematika pembagian suatu bilangan dengan angka nol.
- `KeyError`: Percobaan mengakses kunci yang tidak eksis di dalam sebuah Dictionary.
- `IndexError`: Percobaan mengakses indeks di luar rentang kapasitas sebuah List atau Tuple.
- `FileNotFoundError`: Percobaan membuka berkas fisik di media penyimpanan yang tidak ditemukan lokasinya.

Perhatikan perbandingan arsitektur penanganan galat berikut:

```python
# Contoh penanganan eksepsi kokoh pada transaksi kasir
def proses_transaksi(total_belanja, uang_bayar):
    try:
        belanja = float(total_belanja)
        bayar = float(uang_bayar)
        
        if bayar < belanja:
            raise ValueError("Uang pembayaran kurang dari total belanja!")
            
        kembalian = bayar - belanja
    except ValueError as err:
        print(f"[PERINGATAN SISTEM] Terjadi galat nilai: {err}")
        return False, 0
    except Exception as err_umum:
        print(f"[GALAT TIDAK TERDUGA] Sistem mendeteksi: {err_umum}")
        return False, 0
    else:
        print("[SUKSES] Transaksi valid tanpa galat!")
        return True, kembalian
    finally:
        print("[LOG KEAMANAN] Sesi pemrosesan pembayaran selesai dicatat.")

# Pengujian skenario aman dan galat
status, kembali = proses_transaksi(50000, 75000)
print(f"Status: {status}, Kembalian: Rp{kembali}")
```

---

## C. KONVENSI PENULISAN STANDAR PEP 8 DAN TEKNIK DEBUGGING MANDIRI

Menulis kode yang dapat dieksekusi oleh mesin hanyalah separuh dari tugas seorang pengembang perangkat lunak. Separuh tugas lainnya yang tidak kalah penting adalah menulis kode yang bersih, rapi, dan mudah dibaca oleh manusia (*clean code*).

### 1. Konvensi Gaya Kode Resmi: PEP 8 (Python Enhancement Proposal 8)

PEP 8 adalah dokumen konsensus resmi komunitas Python dunia mengenai tata cara penulisan kode sumber yang baku:

1. **Aturan Indentasi:** Gunakan persis 4 spasi untuk setiap level indentasi blok kode. Hindari mencampuradukkan spasi dengan tombol *Tab*.
2. **Panjang Baris Maksimum:** Batasi panjang satu baris kode maksimal 79 karakter agar mudah dibaca di layar terpisah (*split editor*).
3. **Konvensi Penamaan Variabel dan Fungsi:**
   - Variabel dan Fungsi: Menggunakan gaya `snake_case` (huruf kecil semua dipisahkan garis bawah), contoh: `hitung_total_belanja()`, `harga_satuan`.
   - Nama Kelas (Class): Menggunakan gaya `PascalCase` (setiap awal kata berhuruf kapital tanpa pemisah), contoh: `SistemKasirSekolah`.
   - Nama Konstanta: Menggunakan huruf kapital seluruhnya `UPPER_CASE`, contoh: `PAJAK_PPN = 0.11`, `BATAS_MAKSIMUM_LOGIN = 3`.
4. **Spasi di Sekitar Operator:** Berikan satu spasi sebelum dan sesudah operator penugasan (`=`) dan operator aritmatika (`+`, `-`, `*`, `/`). Hindari spasi di dalam tanda kurung langsung (`fungsi( x )` salah, yang benar `fungsi(x)`).

### 2. Seni Debugging: Membaca Pesan Traceback

Ketika program mengalami galat, interpreter Python akan menampilkan pesan pelacakan jejak eksekusi (*Traceback*). Keterampilan membaca Traceback dari baris terbawah ke atas merupakan modal utama seorang programmer tangguh:
- **Baris Paling Bawah:** Menunjukkan nama kelas eksepsi dan deskripsi akar penyebab galat.
- **Baris di Atasnya:** Menunjukkan nomor baris persis di mana galat terpantik beserta cuplikan baris kodenya.
- **Baris Bagian Awal:** Menunjukkan riwayat panggilan fungsi (*call stack*) yang memicu rantai kejadian tersebut.

---

## D. LEMBAR KERJA PESERTA DIDIK (LKPD) 2.1

### Rancang Bangun Sistem Kasir Toko Retail Bebas Crash

**Tujuan Pembelajaran:**
Peserta didik mampu merancang aplikasi sistem kasir berbasis konsol interaktif menggunakan struktur data koleksi Dictionary, menerapkan penanganan eksepsi `try-except-finally` berlapis agar sistem tahan terhadap masukan tak terduga pengguna, serta menyusun kode sesuai standar estetika PEP 8.

**Alat dan Bahan:**
1. Perangkat komputer dengan sistem operasi Windows, Linux, atau macOS.
2. Lingkungan pengembang kode (VS Code / PyCharm / IDLE).

**Petunjuk Penugasan Proyek:**
1. Buatlah berkas Python baru bernama `sistem_kasir_tangguh.py`.
2. Kembangkan modul program kasir yang memenuhi kriteria fungsional berikut:
   - Data katalog barang disimpan dalam struktur Dictionary dengan kode barang sebagai Kunci (*Key*).
   - Pengguna kasir dapat memasukkan kode barang dan jumlah pembelian berulang kali.
   - Program tidak boleh mati (*crash*) jika kasir memasukkan kode barang yang tidak terdaftar (tangani `KeyError`).
   - Program tidak boleh mati jika kasir salah mengetikkan huruf saat diminta jumlah barang (tangani `ValueError`).
   - Sediakan mekanisme pembatalan atau konfirmasi akhir transaksi.
3. Gunakan kerangka kode program di bawah ini sebagai landasan awal:

```python
# Kerangka Awal Sistem Kasir Bebas Crash
KATALOG_PRODUK = {
    "K01": {"nama": "Buku Catatan A5", "harga": 8000},
    "K02": {"nama": "Pulpen Gel Hitam", "harga": 3500},
    "K03": {"nama": "Map Dokumen Plastik", "harga": 5000},
    "K04": {"nama": "Kalkulator Ilmiah", "harga": 75000}
}

def cetak_katalog():
    print("=" * 45)
    print("   KATALOG BARANG KOPERASI SISWA MANDIRI")
    print("=" * 45)
    for kode, info in KATALOG_PRODUK.items():
        print(f"[{kode}] {info['nama']:<22} : Rp{info['harga']:,}")
    print("=" * 45)

def jalankan_kasir():
    keranjang = []
    total_tagihan = 0
    cetak_katalog()

    while True:
        try:
            kode_input = input("Masukkan kode barang (ketik 'SELESAI' untuk bayar): ").strip().upper()
            if kode_input == "SELESAI":
                break
            
            if kode_input not in KATALOG_PRODUK:
                raise KeyError(f"Kode '{kode_input}' tidak terdaftar dalam katalog!")
            
            input_jumlah = input(f"Jumlah '{KATALOG_PRODUK[kode_input]['nama']}' yang dibeli: ")
            jumlah = int(input_jumlah)
            
            if jumlah <= 0:
                raise ValueError("Jumlah barang harus bilangan bulat positif lebih dari 0!")

            subtotal = KATALOG_PRODUK[kode_input]["harga"] * jumlah
            total_tagihan += subtotal
            keranjang.append((KATALOG_PRODUK[kode_input]["nama"], jumlah, subtotal))
            print(f">> Berhasil menambahkan ke keranjang. Subtotal: Rp{subtotal:,}")

        except KeyError as err_kunci:
            print(f"[KESALAHAN INPUT] {err_kunci}. Silakan periksa kembali daftar katalog!")
        except ValueError as err_nilai:
            print(f"[KESALAHAN NILAI] {err_nilai}. Pastikan Anda memasukkan angka yang valid!")
        except Exception as err_asing:
            print(f"[ANOMALI SISTEM] Terjadi kendala teknis: {err_asing}")

    # Sesi Pembayaran Akhir
    print("\n" + "=" * 45)
    print("           STRUK RINCIAN BELANJA")
    print("=" * 45)
    for item, qty, sub in keranjang:
        print(f"{item:<25} x{qty:<3} = Rp{sub:,}")
    print("-" * 45)
    print(f"TOTAL YANG HARUS DIBAYAR      : Rp{total_tagihan:,}")
    print("=" * 45)

if __name__ == "__main__":
    jalankan_kasir()
```

**Pertanyaan Analisis Laboratorium:**
1. Lakukan pengujian sengaja (*negative testing*) dengan memasukkan teks string acak pada kolom jumlah barang. Amati apakah sistem tetap bertahan dan menampilkan peringatan ramah pengguna!
2. Mengapa struktur Dictionary dengan kompleksitas O(1) jauh lebih unggul digunakan pada katalog barang dibandingkan menggunakan dua struktur List sejajar?
3. Modifikasilah kode di atas agar menambahkan blok `finally` yang mencetak waktu transaksi dan pesan terima kasih kepada pelanggan!

---

## E. RANGKUMAN MATERI BAB II

1. **Struktur Data Koleksi:**
   - *List:* Bersifat mutable, terurut dengan indeks numerik, mengizinkan nilai duplikat.
   - *Tuple:* Bersifat immutable (tidak dapat diubah), hemat memori, cocok untuk data koordinat dan konstanta sistem.
   - *Set:* Kumpulan elemen unik tanpa urutan, mengeliminasi duplikasi secara otomatis, mendukung operasi himpunan instan.
   - *Dictionary:* Kumpulan pasangan Kunci-Nilai (*Key-Value*), memberikan kecepatan akses dan pencarian instan berordo O(1) berbasis fungsi hash.
2. **Arsitektur Penanganan Eksepsi:**
   - Blok `try` mengisolasi kode rawan galat.
   - Blok `except` menangani tipe kesalahan spesifik (`ValueError`, `KeyError`, `IndexError`, dll.) agar program tidak mati mendadak.
   - Blok `else` berjalan jika eksekusi sukses tanpa galat.
   - Blok `finally` selalu dieksekusi untuk pembersihan sumber daya sistem (*resource cleanup*).
3. **Disiplin Kode Bersih (PEP 8):** Mengatur konvensi indentasi 4 spasi, panjang baris, gaya penamaan variabel (`snake_case`), kelas (`PascalCase`), dan konstanta (`UPPER_CASE`) demi menjamin keterbacaan kode (*code readability*) dan kemudahan pemeliharaan perangkat lunak jangka panjang.

---

## F. UJI KOMPETENSI BAB II

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Struktur data koleksi Python yang bersifat tidak dapat diubah nilainya (*immutable*) setelah dideklarasikan di memori adalah...
   A. List
   B. Set
   C. Tuple
   D. Dictionary

2. Perhatikan potongan kode berikut:
   ```python
   data_angka = [10, 20, 10, 30, 20, 40]
   hasil = set(data_angka)
   print(len(hasil))
   ```
   Berapakah nilai keluaran yang dicetak pada layar terminal?
   A. 6
   B. 4
   C. 2
   D. 0

3. Karakteristik utama dari struktur data Dictionary dalam bahasa pemrograman Python adalah...
   A. Elemen diakses menggunakan indeks numerik negatif
   B. Menyimpan pasangan data kunci dan nilai (*key-value pairs*)
   C. Seluruh elemen harus memiliki tipe data yang identik
   D. Tidak dapat menyimpan nilai angka desimal

4. Blok kode dalam mekanisme exception handling Python yang dijamin akan selalu dieksekusi baik ketika terjadi galat maupun saat eksekusi berjalan lancar tanpa kendala adalah...
   A. Blok `try`
   B. Blok `except`
   C. Blok `else`
   D. Blok `finally`

5. Galat waktu berjalan (*runtime exception*) yang muncul saat program mencoba mengakses elemen pada Dictionary menggunakan kunci yang tidak terdapat dalam kamus data tersebut adalah...
   A. `IndexError`
   B. `KeyError`
   C. `ValueError`
   D. `ZeroDivisionError`

6. Berdasarkan pedoman penulisan kode resmi Python (PEP 8), gaya penamaan yang dianjurkan untuk variabel dan fungsi biasa adalah...
   A. `camelCase`
   B. `PascalCase`
   C. `snake_case`
   D. `kebab-case`

7. Perhatikan kode program berikut:
   ```python
   try:
       angka = int("dua puluh lima")
       hasil = 100 / angka
   except ValueError:
       print("Galat konversi angka!")
   except ZeroDivisionError:
       print("Galat pembagian nol!")
   ```
   Apakah pesan keluaran yang akan tampil pada layar terminal?
   A. 4
   B. Galat pembagian nol!
   C. Galat konversi angka!
   D. Program terhenti (*crash*)

8. Berapakah jumlah spasi indentasi standar yang diwajibkan oleh panduan PEP 8 untuk setiap level blok penulisan kode Python?
   A. 2 spasi
   B. 4 spasi
   C. 6 spasi
   D. 8 spasi

9. Manakah di antara operasi struktur data Set berikut yang digunakan untuk mencari elemen-elemen yang sama-sama dimiliki oleh dua himpunan data yang berbeda?
   A. Gabungan (*Union*)
   B. Irisan (*Intersection*)
   C. Selisih (*Difference*)
   D. Komplemen (*Complement*)

10. Mengapa pencarian data pada struktur Dictionary dapat dilakukan dalam waktu konstan O(1) terlepas dari seberapa besar ukuran data yang tersimpan?
    A. Karena Dictionary selalu diurutkan ulang setiap milidetik
    B. Karena Dictionary menggunakan algoritma Binary Search internal
    C. Karena Dictionary memanfaatkan fungsi hash yang memetakan kunci secara langsung ke alamat memori fisik
    D. Karena Dictionary menyimpan seluruh data dalam bentuk matriks dua dimensi

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Uraikan perbedaan mendasar antara struktur data List dan Dictionary dari segi metode pengindeksan elemen, karakteristik keterurutan, dan kompleksitas waktu pencarian data spesifik!
2. Jelaskan peranan vital blok `else` dan blok `finally` dalam arsitektur penanganan kesalahan `try-except`! Berikan contoh skenario nyata pengelolaan berkas (*file handling*) yang mewajibkan penggunaan blok `finally`!
3. Diberikan kasus: Sebuah portal pendaftaran siswa baru meminta calon peserta mengunggah data umur (angka bulat) dan nomor kontak darurat. Rancanglah fungsi Python yang dilengkapi penanganan eksepsi `ValueError` untuk memastikan data umur yang dimasukkan valid (berkisar antara 14 hingga 20 tahun) serta tidak boleh berupa teks abjad!
4. Jelaskan mengapa kepatuhan terhadap panduan gaya penulisan PEP 8 sangat penting dalam pengembangan perangkat lunak skala industri dan riset kecerdasan artifisial yang melibatkan tim kolaboratif lintas negara!
5. Analisislah jejak galat (*traceback*) berikut dan tentukan letak baris kesalahan, penyebab galat, serta solusi perbaikannya:
   ```text
   Traceback (most recent call last):
     File "aplikasi.py", line 14, in <module>
       rata_rata = total_nilai / jumlah_siswa
   ZeroDivisionError: division by zero
   ```

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB II

**Kunci Pilihan Ganda:**
1. **C** (Tuple bersifat immutable sehingga nilainya tidak dapat dimodifikasi setelah dideklarasikan).
2. **B** (Set menyaring duplikasi angka 10 dan 20, sehingga tersisa 4 elemen unik: {10, 20, 30, 40}).
3. **B** (Dictionary mengorganisasikan data dalam pasangan Kunci dan Nilai).
4. **D** (Blok `finally` selalu dieksekusi dalam kondisi apa pun untuk menjamin pembersihan sumber daya).
5. **B** (Mengakses kunci yang tidak eksis pada Dictionary akan memicu `KeyError`).
6. **C** (PEP 8 menganjurkan gaya `snake_case` untuk penamaan fungsi dan variabel).
7. **C** (Fungsi `int("dua puluh lima")` langsung memicu `ValueError` sebelum baris pembagian dieksekusi).
8. **B** (PEP 8 secara tegas menetapkan indentasi standar sebesar 4 spasi).
9. **B** (Operasi irisan/intersection mengambil elemen yang beririsan di antara dua himpunan).
10. **C** (Sistem hash table memetakan kunci unik secara langsung ke alamat lokasi data di memori tanpa perlu pencarian sekuensial).

**Pembahasan Soal Uraian:**
1. *Komparasi List vs Dictionary:*
   - List menggunakan indeks numerik bilangan bulat (0, 1, 2, ...). Pencarian nilai tertentu membutuhkan waktu linear O(n) karena komputer harus memeriksa satu per satu.
   - Dictionary menggunakan Kunci unik (*Key*) bertipe data hashable (seperti string atau angka unik). Pencarian nilai berdasarkan kuncinya beroperasi sangat cepat dalam waktu konstan O(1) berbasis fungsi pemetaan hash.
2. *Peranan Blok Else dan Finally:*
   - Blok `else` memisahkan logika yang hanya boleh dijalankan jika operasi utama pada blok `try` berhasil sempurna tanpa ada galat sama sekali.
   - Blok `finally` menjamin eksekusi pembersihan sumber daya sistem (*cleanup*). Pada skenario pembacaan berkas (`file handling`), jika berkas berhasil dibuka pada blok `try`, blok `finally` wajib memanggil `file.close()` agar alokasi memori berkas dilepaskan kembali ke sistem operasi meskipun di tengah pembacaan data terjadi galat pemrosesan.
3. *Rancangan Fungsi Validasi Umur:*
   ```python
   def validasi_umur(input_teks):
       try:
           umur = int(input_teks)
           if umur < 14 or umur > 20:
               raise ValueError("Umur calon siswa harus berada dalam rentang 14 hingga 20 tahun.")
           return True, umur
       except ValueError as galat:
           return False, str(galat)
   ```
4. *Pentingnya Standar PEP 8:*
   Dalam industri perangkat lunak modern dan laboratorium riset AI, kode program dikembangkan dan dipelihara bersama oleh puluhan atau ratusan insinyur perangkat lunak selama bertahun-tahun. Kepatuhan pada standar PEP 8 menjamin kode memiliki struktur visual yang seragam, menghindari kebingungan interpretasi indentasi, mempercepat penelaahan kode (*code review*), serta meminimalkan potensi galat tersembunyi (*subtle bugs*).
5. *Analisis Traceback ZeroDivisionError:*
   - Letak galat: Berkas `aplikasi.py`, baris ke-14 pada ekspresi `rata_rata = total_nilai / jumlah_siswa`.
   - Penyebab: Variabel pembagi `jumlah_siswa` bernilai 0 (mungkin karena belum ada data siswa yang masuk ke dalam sistem atau filter data menghasilkan himpunan kosong), sehingga operasi pembagian dengan nol tidak dapat didefinisikan secara matematis.
   - Solusi: Tambahkan pengkondisian pengecekan sebelum pembagian: `if jumlah_siswa > 0:` atau bungkus operasi ke dalam blok penanganan `try-except ZeroDivisionError:` untuk memberikan nilai rata-rata default 0.
"""
