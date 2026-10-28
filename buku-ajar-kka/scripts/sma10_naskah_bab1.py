"""
Modul Naskah Bab I Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB1_SMA10 = """# BAB I: BERPIKIR KOMPUTASIONAL DAN KOMPLEKSITAS ALGORITMA

## APERSEPSI: DILEMA SISTEM PENCARIAN SKALA BESAR

Di ruang perpustakaan digital terpadu sekolah, suasana sore itu tampak begitu hening sebelum mendadak terdengar helaan napas panjang dari Bagas. Di hadapannya, laptop yang sedang menjalankan sistem katalog buku sekolah menunjukkan lingkaran berputar tanpa henti. Bagas sedang mencoba memuat dan mencari riwayat peminjaman buku referensi teknik elektronika.

[GAMBAR: assets/bab1_komik_pembuka_sma10.png]

"Ada apa, Bagas? Kenapa layarmu tampak membeku begitu lama?" tanya Dinda sambil meletakkan tablet grafisnya di atas meja.

"Aku sedang menguji coba fungsi pencarian data pada katalog buku perpustakaan digital ini," sahut Bagas seraya mengusap dahinya. "Ketika data buku hanya berjumlah 100 entri, pencarian nama buku terasa instan dalam kedipan mata. Namun, begitu aku memasukkan data uji sebanyak 500.000 judul koleksi buku dari arsip dinas pendidikan wilayah, komputernya mendadak macet hampir 15 detik hanya untuk menemukan satu judul buku yang letaknya di urutan belakang!"

Arya yang duduk di seberang meja tersenyum kecil lalu membuka buku catatannya. "Itu fenomena klasik dalam rekayasa perangkat lunak, kawan. Programmu macet bukan karena spesifikasi prosesor laptopmu yang lemah, melainkan karena kamu menggunakan algoritma pencarian linear sederhana yang memeriksa baris demi baris dari data pertama hingga terakhir. Jika datanya setengah juta, komputer harus melakukan 500.000 kali perbandingan di skenario terburuk!"

"Tepat sekali," tambah Dinda. "Bayangkan jika mesin pencari dunia seperti Google atau platform media sosial harus memeriksa miliaran laman web satu per satu dari awal setiap kali kita mengetik kata kunci. Internet di seluruh dunia pasti akan lumpuh total!"

"Lalu, bagaimana para ilmuwan komputer dan insinyur kecerdasan artifisial merancang algoritma yang tetap secepat kilat meskipun memproses miliaran data?" tanya Bagas penasaran.

Arya menggoreskan diagram kurva pada buku catatannya. "Kuncinya ada pada dua hal fundamental: pertama, bagaimana kita mengurutkan data terlebih dahulu secara terstruktur; kedua, bagaimana kita memilih algoritma yang memiliki kompleksitas waktu asimptotik berordo logaritma atau O(log n). Mari kita bedah tuntas bagaimana ilmu berpikir komputasional dan notasi Big-O menyelamatkan dunia komputasi dari kelambatan!"

---

## A. KONSEP PENCARIAN DATA: LINEAR SEARCH VS BINARY SEARCH

Dalam dunia rekayasa perangkat lunak dan sains komputasi, pencarian (*searching*) merupakan proses algoritma paling mendasar yang dieksekusi miliaran kali setiap detik oleh berbagai sistem informasi di seluruh dunia. Apakah kalian mencari berkas di ponsel cerdas, mencari nomor kontak teman, atau mencari produk di aplikasi niaga daring (*e-commerce*), sistem komputasi di balik layar selalu menjalankan algoritma pencarian.

Secara umum, terdapat dua algoritma pencarian paling populer yang wajib dikuasai oleh setiap calon ilmuwan komputer: **Linear Search** (Pencarian Sekuensial) dan **Binary Search** (Pencarian Biner).

[GAMBAR: assets/bab1_diagram_linear_vs_binary_search.png]

### 1. Linear Search (Pencarian Sekuensial)

Algoritma Linear Search bekerja dengan prinsip yang sangat intuitif: memeriksa setiap elemen dalam sekumpulan data (*array* atau daftar) satu per satu secara berurutan mulai dari indeks ke-0 hingga indeks terakhir sampai elemen sasaran ditemukan atau seluruh elemen selesai diperiksa.

**Keunggulan Linear Search:**
- Sangat sederhana untuk diimplementasikan dalam berbagai bahasa pemrograman.
- Tidak membutuhkan prasyarat khusus: data boleh berada dalam kondisi acak sama sekali (*unsorted*).

**Kelemahan Linear Search:**
- Sangat tidak efisien untuk data skala menengah hingga raksasa. Jika jumlah data adalah n, dan elemen yang dicari berada di posisi paling ujung (atau bahkan tidak ada dalam daftar), algoritma harus melakukan n kali operasi perbandingan.

Berikut adalah implementasi algoritma Linear Search dalam bahasa Python:

```python
# Implementasi Algoritma Linear Search
def linear_search(data_list, target):
    langkah = 0
    for indeks in range(len(data_list)):
        langkah += 1
        if data_list[indeks] == target:
            return indeks, langkah
    return -1, langkah

# Pengujian dengan data acak
daftar_nilai = [45, 12, 89, 34, 78, 90, 23, 67, 100, 56]
kunci_cari = 67
posisi, total_langkah = linear_search(daftar_nilai, kunci_cari)

if posisi != -1:
    print(f"Elemen {kunci_cari} ditemukan pada indeks ke-{posisi} setelah {total_langkah} langkah.")
else:
    print(f"Elemen {kunci_cari} tidak ditemukan setelah {total_langkah} langkah.")
```

### 2. Binary Search (Pencarian Biner)

Binary Search adalah algoritma pencarian cerdas berbasis paradigma pemecahan masalah *Divide and Conquer* (Bagi dan Taklukkan). Berbeda dengan Linear Search yang memeriksa data satu demi satu, Binary Search selalu membelah rentang pencarian menjadi dua bagian yang sama besar pada setiap langkahnya.

**Prasyarat Wajib Binary Search:**
Data dalam daftar **HARUS SUDAH TERURUT** (*sorted*), baik secara menaik (*ascending*) maupun menurun (*descending*). Jika data masih acak, algoritma biner akan menghasilkan kesimpulan yang salah.

**Langkah Matematis Binary Search:**
1. Tentukan batas kiri (*left*) pada indeks ke-0 dan batas kanan (*right*) pada indeks terakhir (n - 1).
2. Hitung titik tengah (*mid*) menggunakan rumus pembagian bulat:
   mid = (left + right) // 2
3. Bandingkan nilai pada indeks tengah (`data[mid]`) dengan nilai sasaran (*target*):
   - Jika `data[mid] == target`, pencarian berhasil dan indeks tengah dikembalikan.
   - Jika `data[mid] < target`, berarti nilai sasaran pasti berada di belahan kanan. Geser batas kiri menjadi `left = mid + 1`.
   - Jika `data[mid] > target`, berarti nilai sasaran pasti berada di belahan kiri. Geser batas kanan menjadi `right = mid - 1`.
4. Ulangi proses ini selama `left <= right`. Jika batas kiri melampaui batas kanan dan nilai belum ditemukan, kembalikan nilai -1 (data tidak ditemukan).

Mari kita analisis keajaiban matematis dari Binary Search. Jika kita memiliki data sebanyak n = 1.000.000 (satu juta) elemen yang sudah terurut:
- Linear Search membutuhkan hingga 1.000.000 kali perbandingan di skenario terburuk.
- Binary Search hanya membutuhkan maksimal 20 kali perbandingan! Angka 20 ini berasal dari nilai logaritma basis 2 dari satu juta: ceil(log2(1.000.000)) = 20 langkah, karena 2 pangkat 20 = 1.048.576. Penghematan daya komputasi ini mencapai lebih dari 99,998%!

Berikut adalah implementasi algoritma Binary Search dalam bahasa Python:

```python
# Implementasi Algoritma Binary Search
def binary_search(data_terurut, target):
    left = 0
    right = len(data_terurut) - 1
    langkah = 0

    while left <= right:
        langkah += 1
        mid = (left + right) // 2
        
        if data_terurut[mid] == target:
            return mid, langkah
        elif data_terurut[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, langkah

# Pengujian dengan data terurut
buku_terurut = [10, 25, 38, 49, 52, 67, 74, 88, 91, 105, 120, 145, 180, 200]
target_id = 91
posisi_biner, iterasi = binary_search(buku_terurut, target_id)

print(f"Target {target_id} ditemukan di indeks {posisi_biner} dalam {iterasi} kali pemeriksaan!")
```

---

## B. ALGORITMA PENGURUTAN: BUBBLE SORT, SELECTION SORT, DAN INSERTION SORT

Karena Binary Search dan berbagai algoritma kecerdasan artifisial tingkat lanjut membutuhkan data yang terurut rapi, pemahaman mendalam tentang cara kerja algoritma pengurutan (*sorting algorithms*) menjadi mutlak diperlukan.

[GAMBAR: assets/bab1_visualisasi_sorting_swapping.png]

Ada tiga algoritma pengurutan dasar berbasis perbandingan (*comparison-based sort*) yang menjadi fondasi pembelajaran berpikir komputasional:

### 1. Bubble Sort (Pengurutan Gelembung)

Bubble Sort bekerja dengan menganalogikan elemen data seperti gelembung udara di dalam air: elemen yang bernilai besar akan mengapung secara bertahap menuju indeks paling belakang melalui serangkaian pertukaran (*swapping*) antar-dua elemen yang bersebelahan.

**Prinsip Kerja Bubble Sort:**
- Mulai dari elemen pertama, bandingkan `data[j]` dengan `data[j+1]`.
- Jika `data[j] > data[j+1]`, tukar posisi kedua elemen tersebut.
- Lanjutkan perbandingan hingga akhir daftar. Pada akhir putaran (*pass*) pertama, elemen terbesar dijamin telah berada di posisi paling akhir.
- Ulangi putaran berikutnya untuk sisa elemen yang belum terurut.

```python
def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Operasi penukaran elemen (swap)
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        # Optimasi: jika tidak ada penukaran, data sudah terurut sempurna
        if not swapped:
            break
    return data

contoh_angka = [64, 34, 25, 12, 22, 11, 90]
print("Hasil Bubble Sort:", bubble_sort(contoh_angka))
```

### 2. Selection Sort (Pengurutan Seleksi Minimum)

Selection Sort bekerja dengan strategi mencari nilai minimum secara berulang dari bagian daftar yang belum terurut, lalu menempatkan nilai minimum tersebut di posisi paling depan yang bersesuaian.

**Prinsip Kerja Selection Sort:**
- Telusuri seluruh daftar untuk menemukan indeks dari elemen yang bernilai paling kecil (*min_idx*).
- Tukar elemen pada `data[min_idx]` dengan elemen pertama dari segmen belum terurut.
- Pindahkan batas segmen terurut satu langkah ke kanan, lalu ulangi penelusuran minimum untuk sisa elemen.

```python
def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        # Tukar elemen minimum dengan elemen di posisi i
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

contoh_angka = [29, 10, 14, 37, 13]
print("Hasil Selection Sort:", selection_sort(contoh_angka))
```

### 3. Insertion Sort (Pengurutan Penyisipan Kartu)

Insertion Sort bekerja menyerupai cara seseorang menyusun kartu remi di tangannya. Elemen diambil satu per satu dari bagian yang belum terurut, lalu disisipkan ke posisi yang tepat di antara elemen-elemen yang sudah terurut di sebelah kirinya dengan cara menggeser (*shifting*) elemen-elemen yang lebih besar ke kanan.

**Prinsip Kerja Insertion Sort:**
- Asumsikan elemen pertama pada indeks ke-0 sudah terurut secara mandiri.
- Ambil elemen pada indeks ke-i sebagai kunci (*key*).
- Bandingkan kunci dengan elemen-elemen sebelumnya (indeks j = i - 1 mundur ke 0). Selama elemen sebelumnya lebih besar dari kunci, geser elemen tersebut satu langkah ke kanan.
- Letakkan kunci pada rongga kosong yang tersedia.

```python
def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        # Menggeser elemen yang lebih besar dari key ke posisi kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

contoh_angka = [12, 11, 13, 5, 6]
print("Hasil Insertion Sort:", insertion_sort(contoh_angka))
```

---

## C. ANALISIS KOMPLEKSITAS WAKTU ASIMPTOTIK (BIG-O NOTATION)

Mengapa para insinyur perangkat lunak dan arsitek kecerdasan artifisial tidak cukup hanya memastikan programnya berjalan dengan benar? Mengapa efisiensi komputasi menjadi parameter hidup-mati dalam industri teknologi modern?

Jawabannya terletak pada **Analisis Kompleksitas Algoritma**. Ketika ukuran masukan (n) bertambah dari puluhan menjadi jutaan atau miliaran, perbedaan efisiensi antar-algoritma akan menentukan apakah program selesai dalam hitungan milidetik atau membutuhkan waktu berhari-hari hingga menyebabkan kehabisan memori (*Out of Memory*).

[GAMBAR: assets/bab1_kurva_kompleksitas_big_o.png]

### 1. Hakikat Notasi Big-O

**Notasi Big-O (O)** adalah notasi matematika formal yang mendeskripsikan perilaku batas atas (*upper bound*) dari laju pertumbuhan waktu eksekusi atau kebutuhan memori suatu algoritma seiring dengan pertambahan ukuran masukan data n menuju tak hingga (asimptotik).

Dalam notasi Big-O, kita mengabaikan konstanta pengali dan suku-suku berderajat rendah. Misalnya, jika suatu algoritma membutuhkan f(n) = 3n^2 + 5n + 100 operasi dasar, maka dalam analisis asimptotik kita menyatakan kompleksitas waktunya adalah **O(n^2)**. Hal ini karena ketika n bernilai sangat besar (misalnya satu juta), nilai n^2 mendominasi secara mutlak dan konstanta tidak lagi memengaruhi laju kelengkungan kurva secara signifikan.

### 2. Spektrum Ordo Kompleksitas dari Paling Efisien hingga Paling Buruk

Berikut adalah hierarki kelas kompleksitas waktu asimptotik yang paling sering dijumpai:

1. **O(1) - Waktu Konstan (Constant Time):**
Waktu eksekusi sama sekali tidak bergantung pada ukuran data n. Berapa pun banyaknya data, algoritma selesai dalam jumlah operasi yang tetap.
*Contoh:* Mengakses elemen daftar berdasarkan indeks spesifik (`data[0]`), memeriksa panjang daftar yang tercatat di memori (`len(data)`), atau mengakses data pada Dictionary menggunakan kunci unik.

2. **O(log n) - Waktu Logaritmik (Logarithmic Time):**
Waktu eksekusi bertambah sangat lambat meskipun ukuran data melonjak drastis. Setiap langkah komputasi memotong ruang pencarian menjadi separuhnya.
*Contoh:* Binary Search pada daftar terurut. Ketika data n naik 1.000 kali lipat dari 1.000 menjadi 1.000.000, jumlah langkah hanya bertambah dari ~10 menjadi ~20 langkah!

3. **O(n) - Waktu Linear (Linear Time):**
Waktu eksekusi bertambah lurus secara proporsional dengan pertambahan ukuran data n. Jika data dilipatgandakan 10 kali, waktu eksekusi juga meningkat sekitar 10 kali.
*Contoh:* Linear Search, menghitung nilai rata-rata dari seluruh elemen daftar, atau mencetak seluruh isi daftar satu per satu.

4. **O(n log n) - Waktu Linear-Logaritmik (Quasilinear Time):**
Kompleksitas standar emas bagi algoritma pengurutan modern skala industri. Lebih lambat sedikit dari O(n), namun jauh lebih cepat daripada O(n^2).
*Contoh:* Merge Sort, Quick Sort (kasus rata-rata), dan Timsort (algoritma bawaan perintah `sort()` pada bahasa Python).

5. **O(n^2) - Waktu Kuadratik (Quadratic Time):**
Waktu eksekusi berbanding lurus dengan kuadrat dari ukuran masukan. Pola ini biasanya muncul pada perulangan bersarang (*nested loops*) di mana setiap elemen dibandingkan dengan seluruh elemen lainnya.
*Contoh:* Bubble Sort, Selection Sort, dan Insertion Sort di skenario rata-rata dan terburuk. Jika n = 100.000, jumlah operasi mendekati 10.000.000.000 (sepuluh miliar operasi)!

6. **O(2^n) - Waktu Eksponensial (Exponential Time):**
Waktu eksekusi berlipat ganda pada setiap pertambahan satu unit data n. Algoritma dengan kompleksitas ini praktis tidak dapat digunakan untuk masukan data skala menengah karena waktu eksekusinya dapat melampaui usia alam semesta!
*Contoh:* Algoritma rekursif Fibonacci naif tanpa memoisasi atau pemecahan masalah kombinatorial *Traveling Salesperson Problem* secara brute force.

---

## D. LEMBAR KERJA PESERTA DIDIK (LKPD) 1.1

### Komparasi Efisiensi Algoritma Pengurutan Berbasis Waktu Eksekusi Nyata

**Tujuan Pembelajaran:**
Peserta didik mampu mengukur, membandingkan, dan menganalisis secara empiris perbedaan waktu eksekusi nyata antara Bubble Sort, Insertion Sort, dan algoritma bawaan Python (`Timsort`) terhadap variasi ukuran masukan data menggunakan modul `time`.

**Alat dan Bahan:**
1. Komputer/Laptop dengan interpreter Python 3 terpasang.
2. Kode editor (Visual Studio Code, PyCharm, atau Jupyter Notebook).
3. Modul Python bawaan: `time` dan `random`.

**Instruksi Kerja Praktikum:**
1. Bukalah aplikasi kode editor kalian dan buatlah berkas baru bernama `praktikum_sorting.py`.
2. Ketikkan kode program eksperimen berikut ini dengan cermat:

```python
import time
import random

# Definisi algoritma Bubble Sort
def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

# Definisi algoritma Insertion Sort
def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Fungsi pengujian komparasi waktu
def uji_kinerja_sorting(ukuran):
    print(f"===== PENGUJIAN DENGAN UKURAN DATA N = {ukuran} =====")
    # Membuat daftar angka acak
    data_uji = [random.randint(1, 100000) for _ in range(ukuran)]
    
    # 1. Uji Bubble Sort
    mulai = time.perf_counter()
    bubble_sort(data_uji)
    selesai = time.perf_counter()
    waktu_bubble = selesai - mulai
    print(f"Bubble Sort    : {waktu_bubble:.6f} detik")

    # 2. Uji Insertion Sort
    mulai = time.perf_counter()
    insertion_sort(data_uji)
    selesai = time.perf_counter()
    waktu_insertion = selesai - mulai
    print(f"Insertion Sort : {waktu_insertion:.6f} detik")

    # 3. Uji Built-in Python Timsort (sort())
    data_timsort = data_uji.copy()
    mulai = time.perf_counter()
    data_timsort.sort()
    selesai = time.perf_counter()
    waktu_timsort = selesai - mulai
    print(f"Python Timsort : {waktu_timsort:.6f} detik")
    print("-" * 50)

# Jalankan pengujian bertahap
for n in [1000, 3000, 6000]:
    uji_kinerja_sorting(n)
```

**Pertanyaan Diskusi dan Analisis Hasil:**
1. Catatlah durasi waktu eksekusi untuk ketiga algoritma pada tabel pengamatan di buku catatan kalian untuk setiap nilai n (1.000, 3.000, dan 6.000 elemen)!
2. Ketika nilai n meningkat dari 1.000 menjadi 3.000 (meningkat 3 kali lipat), berapakah perkiraan faktor peningkatan waktu eksekusi pada Bubble Sort? Apakah peningkatannya mendekati 3^2 = 9 kali lipat? Jelaskan kaitannya dengan notasi O(n^2)!
3. Mengapa metode bawaan Python (`data.sort()`) mampu berjalan ribuan kali lebih cepat dibandingkan Bubble Sort buatan sendiri? Telusuri pustaka algoritma di balik fungsi bawaan tersebut!

---

## E. RANGKUMAN MATERI BAB I

1. **Pencarian Data (Searching):** Linear Search memeriksa data satu per satu dari awal hingga akhir dengan kompleksitas waktu O(n) dan tidak membutuhkan data terurut. Sebaliknya, Binary Search membagi ruang pencarian menjadi dua bagian secara berulang dengan kompleksitas waktu O(log n), namun wajib mensyaratkan data dalam kondisi terurut sempurna.
2. **Algoritma Pengurutan Dasar:**
   - *Bubble Sort:* Bekerja dengan menukarkan dua elemen bersebelahan secara terus-menerus hingga elemen terbesar mengapung ke ujung akhir.
   - *Selection Sort:* Memilih elemen terkecil secara berulang dari segmen belum terurut lalu menukarnya ke posisi awal.
   - *Insertion Sort:* Mengambil elemen satu per satu lalu menyisipkannya pada posisi yang tepat di antara elemen-elemen yang sudah terurut dengan cara menggeser nilai yang lebih besar.
3. **Analisis Kompleksitas Asimptotik (Big-O):** Notasi matematika untuk mengukur batas atas laju pertumbuhan waktu eksekusi algoritma terhadap pertambahan masukan n. Urutan efisiensi dari yang paling optimal hingga paling tidak efisien adalah O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n).
4. **Signifikansi Terapan:** Pemilihan algoritma yang tepat dan analisis kompleksitas Big-O merupakan keterampilan inti rekayasa komputasi untuk memastikan sistem kecerdasan artifisial dan basis data skala raksasa dapat berjalan secara efisien, responsif, dan hemat sumber daya perangkat keras.

---

## F. UJI KOMPETENSI BAB I

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Algoritma pencarian yang memeriksa setiap elemen secara berurutan mulai dari indeks ke-0 hingga indeks terakhir tanpa mensyaratkan data harus terurut disebut...
   A. Binary Search
   B. Linear Search
   C. Insertion Search
   D. Hash Search

2. Diberikan sekumpulan data terurut berisi 1.024 elemen angka unik. Berapakah jumlah langkah perbandingan maksimum (worst case) yang dibutuhkan oleh algoritma Binary Search untuk menemukan nilai kunci pencarian?
   A. 1.024 langkah
   B. 512 langkah
   C. 10 langkah
   D. 1 langkah

3. Perhatikan potongan kode berikut:
   ```python
   def ambil_data(daftar_angka, indeks):
       return daftar_angka[indeks]
   ```
   Berdasarkan analisis asimptotik, kompleksitas waktu eksekusi dari fungsi di atas adalah...
   A. O(1)
   B. O(log n)
   C. O(n)
   D. O(n^2)

4. Algoritma pengurutan yang bekerja dengan cara mencari elemen bernilai minimum dari bagian daftar yang belum terurut, kemudian menukarnya dengan elemen pertama dari segmen tersebut adalah...
   A. Bubble Sort
   B. Selection Sort
   C. Insertion Sort
   D. Merge Sort

5. Karakteristik utama dari algoritma Insertion Sort yang membedakannya secara visual dari Selection Sort adalah...
   A. Selalu membagi data menjadi dua kelompok yang sama besar
   B. Menggeser elemen-elemen yang bernilai lebih besar ke kanan untuk menyediakan rongga penyisipan elemen kunci
   C. Memeriksa elemen secara acak menggunakan fungsi probabilitas
   D. Membutuhkan struktur data pohon biner terindeks

6. Manakah di antara kelas kompleksitas waktu berikut yang menunjukkan performa paling efisien dan paling cepat ketika memproses masukan data berukuran raksasa (n menuju tak hingga)?
   A. O(n^2)
   B. O(n)
   C. O(n log n)
   D. O(log n)

7. Suatu algoritma memiliki persamaan fungsi komputasi f(n) = 7n^2 + 150n + 900. Dalam kaidah notasi Big-O, kompleksitas asimptotik dari algoritma tersebut dinotasikan sebagai...
   A. O(900)
   B. O(150n)
   C. O(n^2)
   D. O(n^3)

8. Di sebuah platform toko buku daring dengan 1.000.000 judul buku yang sudah terindeks rapi secara alfabetis, arsitek sistem memutuskan beralih dari Linear Search ke Binary Search. Rasio perbandingan perkiraan jumlah langkah terburuk antara Linear Search dan Binary Search adalah sekitar...
   A. 10 banding 1
   B. 100 banding 1
   C. 1.000 banding 1
   D. 50.000 banding 1

9. Mengapa dalam implementasi Bubble Sort modern ditambahkan variabel penanda boolean `swapped`?
   A. Agar algoritma dapat berhenti lebih awal (early stopping) jika data ternyata sudah terurut sempurna pada putaran tertentu
   B. Untuk mengubah algoritma Bubble Sort menjadi berordo O(1) pada setiap kondisi
   C. Untuk membalikkan urutan data dari ascending menjadi descending secara otomatis
   D. Untuk menghapus elemen ganda yang terdapat di dalam daftar

10. Algoritma pengurutan bawaan Python (`list.sort()`) menggunakan Timsort yang memiliki kompleksitas waktu rata-rata berordo...
    A. O(1)
    B. O(log n)
    C. O(n log n)
    D. O(n^2)

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara mekanisme pencarian Linear Search dan Binary Search dari segi prasyarat data dan kompleksitas waktu! Berikan analogi konkret dalam kehidupan sehari-hari!
2. Diberikan sebuah daftar angka acak: `[42, 16, 8, 35, 20]`. Tuliskan langkah demi langkah penelusuran (*trace pass*) pengurutan data tersebut hingga terurut menaik menggunakan algoritma Bubble Sort!
3. Mengapa dalam notasi Big-O para ilmuwan komputer mengabaikan konstanta pengali (seperti angka 5 pada 5n) dan suku-suku berderajat rendah? Jelaskan dengan landasan matematika perilaku asimptotik!
4. Suatu program pemrosesan data antrean rumah sakit memiliki perulangan bersarang (*nested loop*) di mana perulangan luar berjalan sebanyak n kali dan perulangan dalam juga berjalan sebanyak n kali. Tentukan kompleksitas Big-O dari program tersebut dan jelaskan dampaknya terhadap waktu eksekusi jika jumlah pasien n meningkat dari 100 menjadi 10.000!
5. Sebagai calon arsitek perangkat lunak, dalam situasi nyata seperti apakah kalian akan tetap memilih menggunakan Linear Search daripada Binary Search? Jelaskan minimal dua kondisi spesifik yang membenarkan keputusan tersebut!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB I

**Kunci Pilihan Ganda:**
1. **B** (Linear Search memeriksa setiap elemen berurutan tanpa syarat data harus terurut).
2. **C** (2 pangkat 10 = 1.024, sehingga logaritma basis 2 dari 1.024 adalah 10 langkah).
3. **A** (Mengakses elemen daftar berdasarkan indeks spesifik memakan waktu konstan O(1)).
4. **B** (Selection Sort mencari nilai minimum berulang kali lalu menukarnya ke posisi awal).
5. **B** (Insertion Sort menggeser elemen yang lebih besar ke arah kanan untuk menyisipkan elemen kunci).
6. **D** (O(log n) adalah kelas kompleksitas paling efisien di antara pilihan yang tersedia).
7. **C** (Dalam notasi Big-O, suku dengan derajat pangkat tertinggi yaitu n^2 yang diambil, sedangkan koefisien dan suku berpangkat lebih rendah diabaikan).
8. **D** (1.000.000 langkah berbanding 20 langkah adalah 50.000 banding 1).
9. **A** (Flag `swapped` mendeteksi ketiadaan pertukaran data sehingga perulangan dapat langsung dihentikan pada skenario data sudah terurut).
10. **C** (Timsort memiliki kompleksitas waktu rata-rata dan terburuk berordo O(n log n)).

**Pembahasan Soal Uraian:**
1. *Perbedaan Linear vs Binary Search:*
   - Linear Search dapat dijalankan pada data acak, memeriksa data satu demi satu berordo O(n). Analoginya seperti mencari nama teman pada secarik kertas coretan acak dari baris paling atas ke bawah.
   - Binary Search wajib mensyaratkan data telah terurut rapi, membagi ruang pencarian menjadi separuhnya di setiap langkah berordo O(log n). Analoginya seperti membuka buku kamus cetak tebal di halaman tengah, lalu memutuskan apakah kata yang dicari berada di bagian kiri atau kanan secara berulang.
2. *Trace Bubble Sort untuk [42, 16, 8, 35, 20]:*
   - Pass 1: Bandingkan (42, 16) -> tukar [16, 42, 8, 35, 20]; (42, 8) -> tukar [16, 8, 42, 35, 20]; (42, 35) -> tukar [16, 8, 35, 42, 20]; (42, 20) -> tukar [16, 8, 35, 20, 42]. (Elemen 42 terkunci di akhir).
   - Pass 2: (16, 8) -> tukar [8, 16, 35, 20, 42]; (16, 35) -> tetap; (35, 20) -> tukar [8, 16, 20, 35, 42]. (Elemen 35 terkunci).
   - Pass 3: (8, 16) -> tetap; (16, 20) -> tetap. Tidak ada penukaran lagi. Data terurut sempurna menjadi [8, 16, 20, 35, 42].
3. *Pengabaian Konstanta pada Big-O:*
   Notasi Big-O berfokus pada laju percepatan pertumbuhan (*rate of growth*) fungsi ketika nilai masukan n mendekati tak hingga. Ketika n bernilai 1.000.000, suku n^2 menghasilkan 1.000.000.000.000 (satu triliun), sementara suku 150n hanya bernilai 150.000.000. Konstanta pengali tidak mengubah bentuk kurva matematika secara kualitatif pada skala tak hingga.
4. *Analisis Perulangan Bersarang (Nested Loop):*
   Kompleksitasnya adalah O(n * n) = O(n^2). Ketika n = 100, operasi yang terjadi adalah 100^2 = 10.000 operasi. Namun ketika pasien bertambah menjadi n = 10.000, operasi melonjak menjadi 10.000^2 = 100.000.000 (seratus juta) operasi. Peningkatan ukuran data 100 kali menyebabkan waktu eksekusi melonjak 10.000 kali lipat, yang dapat menyebabkan sistem antrean rumah sakit mengalami *lag* parah atau kelebihan beban server.
5. *Kondisi Tepat Memilih Linear Search:*
   - Pertama, ketika ukuran data sangat kecil (misalnya hanya 5 hingga 10 elemen), di mana biaya (*overhead*) untuk mengurutkan data terlebih dahulu justru memakan waktu lebih banyak daripada sekadar memeriksa data satu per satu.
   - Kedua, ketika data bersifat aliran dinamis (*streaming data*) yang terus bertambah setiap saat dan hanya dicari satu kali saja, sehingga proses pengurutan data terlebih dahulu menjadi sia-sia dan memboroskan memori.
"""
