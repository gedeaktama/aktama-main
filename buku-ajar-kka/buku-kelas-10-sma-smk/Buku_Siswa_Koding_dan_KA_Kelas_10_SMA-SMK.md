# KODING DAN KECERDASAN ARTIFISIAL

## BUKU SISWA KELAS X SMA/SMK (FASE E)

**Penulis:**
Gede Erik Aktama, S.Pd., M.Pd.

**Penerbit:**
PT Aktama Mega Persada
Bekerja sama dengan Tim Pengembang Kurikulum Koding dan Kecerdasan Artifisial

---

# HAK CIPTA DAN KREDIT

**Judul Buku:** Koding dan Kecerdasan Artifisial untuk Siswa SMA/SMK Kelas X (Fase E)
**Penulis Utama:** Gede Erik Aktama, S.Pd., M.Pd.
**Penelaah Ahli:** Tim Pengembang Kurikulum Informatika & KKA Nasional
**Penyelia Penerbitan:** PT Aktama Mega Persada
**Desain Cover & Ilustrasi:** Tim Desain Visual Aktama Studio
**Tata Letak (Layout):** Tim Grafika dan Percetakan Komputasi

**Katalog Terbitan Kemendikdasmen RI:**
Hak cipta dilindungi oleh Undang-Undang Republik Indonesia Nomor 28 Tahun 2014 tentang Hak Cipta. Dilarang memperbanyak atau memindahkan sebagian atau seluruh isi buku ini dalam bentuk apa pun dan dengan cara apa pun, baik secara elektronik maupun mekanik, termasuk memfotokopi, merekam, atau dengan sistem penyimpanan lainnya, tanpa izin tertulis dari penerbit dan penulis, kecuali untuk kepentingan kutipan akademis dan tinjauan literatur ilmiah.

Edisi Pertama: Tahun 2025
Diterbitkan di: Manado, Sulawesi Utara
Ukuran Buku Standar Internasional: Format UNESCO (15,5 cm x 23,0 cm)

---

# PRAKATA

Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan karunia-Nya, sehingga buku ajar *Koding dan Kecerdasan Artifisial (KKA) untuk SMA/SMK Kelas X (Fase E)* ini dapat diselesaikan dengan standar mutu akademik dan pedagogis yang paripurna.

Era Revolusi Industri 4.0 dan transformasi digital abad ke-21 menempatkan kecerdasan artifisial (Artificial Intelligence/AI), komputasi awan, dan pemrosesan data skala besar sebagai lokomotif utama peradaban. Peserta didik pada jenjang Sekolah Menengah Atas (SMA) dan Sekolah Menengah Kejuruan (SMK) Fase E berada pada fase krusial: transisi dari pemahaman logika komputasi prosedural dasar menuju pemikiran abstraksi tingkat lanjut, perancangan arsitektur perangkat lunak, serta penerapan etika digital dan kecerdasan artifisial terapan dalam memecahkan permasalahan nyata di masyarakat dan dunia industri.

Buku ajar ini disusun secara berkesinambungan mengacu pada Kurikulum KKA yang diterbitkan oleh Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) RI. Pendekatan pembelajaran yang digunakan adalah *Deep Learning* (pembelajaran bermakna, kontekstual, dan menantang daya nalar tingkat tinggi/HOTS), didukung metode praktikum langsung berbasis proyek nyata (*Project-Based Learning*). Melalui kehadiran tiga sahabat belajar inspiratif—Arya (siswa SMA peminat sains komputasi dan matematika algoritma), Dinda (siswi peminat analisis data sosial, estetika multimedia, dan etika AI), serta Bagas (siswa SMK rekayasa perangkat lunak dan elektronika cerdas)—peserta didik diajak menjelajahi konsep-konsep inti Fase E:
1. Berpikir komputasional mendalam, perbandingan algoritma pencarian (Linear vs Binary Search), teknik pengurutan data, serta analisis efisiensi waktu asimptotik Big-O Notation.
2. Pemrograman Python terapan berbasis struktur data koleksi (List, Tuple, Set, Dictionary), mekanisme penanganan galat (*exception handling* `try-except`), dan disiplin kode bersih standar PEP 8.
3. Arsitektur basis data relasional, pemodelan ERD notasi Crow's Foot, eksekusi perintah SQL (DDL dan DML), serta integrasi database lokal `sqlite3` dengan bahasa Python.
4. Produksi konten multimedia interaktif berstandar profesional, manajemen resolusi (16:9 vs 9:16), bitrate, kompresi data, prinsip desain antarmuka berpusat pengguna (*User-Centered Design*), dan etika Hak Kekayaan Intelektual (HKI).
5. Pemahaman prinsip dasar Computer Vision melalui manipulasi matriks piksel warna RGB dan operasi konvolusi kernel, spektrogram frekuensi suara, serta peta ekosistem karier masa depan di ranah AI.
6. Rekayasa prompt cerdas (*Prompt Engineering*) tingkat lanjut dengan kerangka kerja ROCCF (*Role, Objective, Context, Constraint, Format*), strategi *Chain-of-Thought*, serta metode *Design Thinking* dalam merancang solusi sistemik kecerdasan artifisial yang etis, aman, dan berdaya guna.

Penulis menyampaikan apresiasi dan penghargaan yang setinggi-tingginya kepada Kemendikdasmen RI, Universitas Parna Raya (UNIPAR) Manado, para fasilitator nasional, pendidik informatika se-Indonesia, serta segenap tim redaksi yang telah berkontribusi mencurahkan dedikasi terbaik bagi terwujudnya buku ini. Semoga karya ini mampu menjadi jembatan akselerasi lahirnya generasi talenta emas Indonesia yang cakap digital, kreatif, inovatif, berintegritas moral, dan siap memimpin peradaban teknologi dunia.

Selamat belajar, bereksperimen, dan berinovasi!

Manado,   2025

**Gede Erik Aktama, S.Pd., M.Pd.**
*Penulis & Fasilitator Nasional KKA*

---

# PETUNJUK PENGGUNAAN BUKU

Buku ajar ini dirancang dengan tata letak visual modern, pedagogi bertahap, dan dilengkapi berbagai ikon panduan aktivitas belajar untuk memastikan pengalaman belajar yang menyenangkan, mendalam, dan terstruktur:

1. **Apersepsi & Komik Inspiratif:** Kisah ilustratif di setiap awal bab yang mengaitkan fenomena teknologi nyata dengan dilema komputasi yang dihadapi siswa.
2. **Uraian Konsep Matematis & Teknis:** Pembahasan konsep ilmiah secara runut, mendalam, dan gamblang, disertai diagram visual beresolusi tinggi 300 DPI.
3. **Eksplorasi Kode Python Terapan:** Blok kode program Python fungsional yang disertai ulasan baris demi baris, studi kasus kesalahan umum, dan petunjuk debugging.
4. **Laboratorium Komputasi Mandiri & Kelompok (LKPD):** Lembar Kerja Peserta Didik berbasis proyek nyata untuk mengasah keterampilan kolaboratif, logika kritis, dan kreasi rekayasa perangkat lunak.
5. **Zona Karakter & Integritas Digital:** Refleksi nilai-nilai moral, privasi data, kejujuran akademik, dan mitigasi bias dalam penerapan teknologi AI.
6. **Rangkuman Bab & Peta Konsep:** Intisari materi komprehensif untuk memudahkan pengulangan materi (*retrieval practice*).
7. **Uji Kompetensi Komprehensif:** 10 Soal Pilihan Ganda berbobot HOTS (*Higher Order Thinking Skills*) dan 5 Soal Uraian Pemecahan Kasus Nyata di setiap akhir bab, disertai kunci jawaban dan pembahasan analitis.

---

# MENGENAL TOKOH SAHABAT BELAJAR FASE E

Dalam perjalanan mempelajari Koding dan Kecerdasan Artifisial di Kelas X SMA/SMK ini, kalian akan didampingi oleh tiga sahabat muda yang penuh semangat inovasi:

[GAMBAR: assets/gambar_tokoh_sahabat_sma10.png]

1. **Arya (Siswa SMA Peminat Sains Komputasi & Matematika):**
Arya adalah sosok yang sangat gemar membedah struktur logika di balik program komputer. Ia terpesona oleh cara algoritma bekerja menghemat waktu eksekusi jutaan data, menganalisis kurva efisiensi Big-O, dan merancang kode Python yang bersih, terstruktur, serta berkinerja tinggi. Arya selalu menantang dirinya untuk mencari solusi komputasi yang paling optimal.

2. **Dinda (Siswi Peminat Analisis Sosial, Multimedia, & Etika AI):**
Dinda memiliki kepekaan rasa yang tinggi terhadap interaksi antara manusia dan teknologi. Ia menyukai visualisasi data, desain multimedia interaktif yang ramah pengguna (UI/UX), serta sangat peduli terhadap aspek sosial teknologi. Dinda selalu mengingatkan pentingnya etika, kejujuran data, perlindungan hak cipta, serta pencegahan bias diskriminatif dalam sistem kecerdasan artifisial.

3. **Bagas (Siswa SMK Peminat Rekayasa Perangkat Lunak & Sistem Cerdas):**
Bagas adalah siswa yang sangat menyukai penerapan teknologi langsung di ranah perangkat keras dan industri terapan. Ia gemar bereksperimen dengan basis data SQL, pengolahan matriks citra piksel (Computer Vision), pengenalan suara sensorik, serta perakitan prototipe berbasis Internet of Things (IoT). Bagas percaya bahwa teknologi cerdas harus mampu memecahkan masalah nyata di lingkungan sekolah dan dunia kerja.

---

# DAFTAR ISI

- Prakata
- Petunjuk Penggunaan Buku
- Mengenal Tokoh Sahabat Belajar Fase E
- Capaian Pembelajaran Fase E (KKA Kelas X)
- BAB I: Berpikir Komputasional dan Kompleksitas Algoritma
  - A. Konsep Pencarian Data: Linear Search vs Binary Search
  - B. Algoritma Pengurutan: Bubble Sort, Selection Sort, dan Insertion Sort
  - C. Analisis Kompleksitas Waktu Asimptotik (Big-O Notation)
  - D. LKPD 1.1: Komparasi Efisiensi Algoritma Pengurutan Berbasis Waktu Eksekusi
  - E. Rangkuman Materi Bab I
  - F. Uji Kompetensi Bab I (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB II: Pemrograman Python Terapan dan Struktur Data Koleksi
  - A. Struktur Data Koleksi Python: List, Tuple, Set, dan Dictionary
  - B. Mekanisme Penanganan Galat (Exception Handling) try-except-else-finally
  - C. Konvensi Penulisan Standar PEP 8 dan Teknik Debugging Mandiri
  - D. LKPD 2.1: Rancang Bangun Sistem Kasir Toko Retail Bebas Crash
  - E. Rangkuman Materi Bab II
  - F. Uji Kompetensi Bab II (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB III: Basis Data Relasional dan Perintah SQL
  - A. Fondasi Basis Data Relasional: Entitas, Atribut, Primary Key, dan Foreign Key
  - B. Perancangan Model Data: Entity Relationship Diagram (ERD) Notasi Crow's Foot
  - C. Sintaks Dasar SQL: Data Definition Language (DDL) dan Data Manipulation Language (DML)
  - D. Integrasi Database Relasional Python Menggunakan Modul Lokal sqlite3
  - E. LKPD 3.1: Proyek Sistem Inventarisasi Fasilitas Laboratorium Komputer Sekolah
  - F. Rangkuman Materi Bab III
  - G. Uji Kompetensi Bab III (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB IV: Produksi Konten Multimedia Interaktif dan Desain Antarmuka
  - A. Anatomi Multimedia Digital: Aspek Rasio (16:9 vs 9:16), Resolusi, dan Bitrate
  - B. Prinsip Kompresi Data: Lossless vs Lossy Audio-Visual
  - C. Prinsip Perancangan Desain Antarmuka Berpusat Pengguna (User-Centered Design)
  - D. Etika Digital, Hak Kekayaan Intelektual (HKI), dan Diseminasi Informasi Bertanggung Jawab
  - E. LKPD 4.1: Kampanye Publik Digital Sosialisasi Literasi AI untuk Komunitas Sekolah
  - F. Rangkuman Materi Bab IV
  - G. Uji Kompetensi Bab IV (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB V: Pengenalan Citra Digital (Computer Vision) dan Pola Audio AI
  - A. Representasi Citra Digital: Matriks Piksel Warna Merah, Hijau, dan Biru (RGB)
  - B. Operasi Konvolusi Dasar: Filter Kernel 3x3 untuk Deteksi Tepi (Edge Detection)
  - C. Representasi Suara Digital: Dari Gelombang Akustik ke Spektrogram Frekuensi
  - D. Peta Peluang Karier dan Lanskap Keahlian di Bidang Kecerdasan Artifisial
  - E. LKPD 5.1: Eksperimen Deteksi Pola Citra Piksel dan Spektrogram Suara Mandiri
  - F. Rangkuman Materi Bab V
  - G. Uji Kompetensi Bab V (10 PG, 5 Uraian, Pembahasan & Kunci Jawaban)
- BAB VI: Rekayasa Prompt Tingkat Lanjut dan Perancangan Solusi Sistem AI
  - A. Kerangka Kerja Rekayasa Prompt Cerdas ROCCF (Role, Objective, Context, Constraint, Format)
  - B. Teknik Rekayasa Penalaran: Few-Shot Prompting dan Chain-of-Thought (CoT)
  - C. Perancangan Prototipe Sistem Berbasis AI Menggunakan Metode Design Thinking
  - D. Mitigasi Risiko Halusinasi AI, Keamanan Data Pribadi, dan Tanggung Jawab Moral Inovator
  - E. LKPD 6.1: Capstone Project Merancang Solusi Otomasi Berkelanjutan Sekolah Ramah Lingkungan
  - F. Rangkuman Materi Bab VI
  - G. Evaluasi Akhir Tahun Fase E (15 Soal PG, 5 Soal Pemecahan Kasus Sistemik, Kunci Jawaban)
- Glosarium Istilah Fase E
- Indeks Istilah
- Daftar Pustaka Resmi
- Profil Penulis

---

# CAPAIAN PEMBELAJARAN FASE E (KELAS X SMA/SMK)

Pada akhir Fase E, peserta didik memiliki pemahaman mendalam dan kecakapan komputasional terapan yang mencakup domain:
1. **Berpikir Komputasional (BK):** Mampu mengabstraksikan masalah kompleks, membandingkan efisiensi algoritma pencarian dan pengurutan data secara matematis, serta menganalisis kompleksitas waktu asimptotik Big-O untuk menentukan solusi paling efisien pada sistem komputasi berdaya tampung besar.
2. **Pemrograman & Struktur Data (PL):** Mahir menulis kode program fungsional terstruktur dalam bahasa Python, mengelola struktur data koleksi majemuk (List, Tuple, Set, Dictionary), menerapkan arsitektur penanganan kesalahan (*exception handling*) untuk mencegah program macet (*crash*), dan mematuhi konvensi tata kelola kode bersih standar industri (PEP 8).
3. **Sistem Informasi & Basis Data (SIBD):** Mampu merancang diagram hubungan antar-entitas (ERD) notasi Crow's Foot dengan relasi kunci (Primary Key & Foreign Key), mengeksekusi operasi basis data relasional standar (DDL dan DML), serta menghubungkan aplikasi perangkat lunak dengan basis data lokal relasional.
4. **Multimedia Interaktif & Desain UI/UX (MI):** Memahami karakteristik teknis media digital (resolusi, rasio aspek, bitrate, kompresi), menerapkan prinsip desain antarmuka berorientasi pengguna, serta memiliki kesadaran hukum dan etika terkait Hak Kekayaan Intelektual (HKI).
5. **Kecerdasan Artifisial & Pembelajaran Mesin Terapan (AI):** Memahami prinsip matematis pembentukan citra visual sebagai matriks angka piksel, cara kerja filter kernel konvolusi pada Computer Vision, representasi frekuensi suara pada spektrogram, serta mengenali prospek karier transformatif di era AI.
6. **Rekayasa Prompt & Solusi Sistemik AI (RP-SAI):** Terampil memformulasikan perintah multi-kondisi berstruktur ROCCF, memandu model penalaran kompleks menggunakan teknik *Chain-of-Thought*, serta mengintegrasikan metodologi *Design Thinking* untuk menciptakan solusi sistem cerdas yang berdampak positif bagi peradaban masyarakat.


# BAB I: BERPIKIR KOMPUTASIONAL DAN KOMPLEKSITAS ALGORITMA

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


# BAB II: PEMROGRAMAN PYTHON TERAPAN DAN STRUKTUR DATA KOLEKSI

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
    print("
" + "=" * 45)
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


# BAB III: BASIS DATA RELASIONAL DAN PERINTAH SQL

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

    print("
" + "=" * 80)
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


# BAB IV: PRODUKSI KONTEN MULTIMEDIA INTERAKTIF DAN DESAIN ANTARMUKA

## APERSEPSI: MENGAPA VIDEO EDUKASI KITA BURAM DAN TERPOTONG?

Di laboratorium multimedia sekolah, Dinda, Bagas, dan Arya sedang menatap layar ponsel pintar dengan ekspresi heran bercampur kecewa. Video edukasi bertajuk "Mengenal Kecerdasan Artifisial di Sekolah Kita" yang mereka rekam dan sunting selama dua hari penuh baru saja diunggah ke saluran media sosial sekolah. Namun, hasil tayangannya jauh dari harapan.

[GAMBAR: assets/bab4_komik_pembuka_sma10.png]

"Dinda, lihat ini!" tunjuk Bagas ke layar ponselnya. "Video kita memiliki bilah hitam tebal (*black bars*) di bagian atas dan bawah layar ponsel saat diputar secara vertikal. Teks penjelasan di bagian pinggir terpotong separuh, dan saat teman-teman di asrama mencoba memutarnya menggunakan koneksi seluler, videonya tersendat-sendat (*buffering*) setiap tiga detik!"

Dinda memeriksa properti berkas ekspor di laptop pengeditan. "Ya ampun, Bagas! Kamu mengekspor video ini dengan resolusi horizontal 4K standar lanskap (3840 x 2160 piksel) dengan rasio aspek 16:9, padahal platform media sosial ponsel pintar mengutamakan format potret vertikal rasio 9:16 (1080 x 1920 piksel)! Selain itu, bitrate videonya kamu pasang di angka 80 Mbps tanpa kompresi yang efisien. Ukuran berkas video yang berdurasi hanya 1 menit ini mencapai hampir 600 Megabyte!"

Arya mengangguk seraya tersenyum bijak. "Dalam rekayasa multimedia digital dan desain antarmuka modern, kualitas visual bukan sekadar membesarkan resolusi mentah secara membabi buta. Ada sains komputasi yang mengatur keseimbangan antara rasio aspek, *bitrate*, *frame rate*, dan efisiensi algoritma kompresi data (*lossy vs lossless*). Selain itu, antarmuka media kita harus mematuhi prinsip desain berpusat pengguna (*User-Centered Design*) dan menghormati etika Hak Kekayaan Intelektual (HKI)."

"Luar biasa," ujar Dinda penuh semangat. "Mari kita pelajari rahasia teknis di balik produksi multimedia profesional yang ramah pita lebar (*bandwidth*), nyaman ditonton, beretika, dan memukau pengguna!"

---

## A. ANATOMI MULTIMEDIA DIGITAL: ASPEK RASIO, RESOLUSI, DAN BITRATE

Di era konvergensi media modern, konten multimedia digital tidak lagi hanya dinikmati di layar televisi atau proyektor bioskop, melainkan didistribusikan ke berbagai gawai (*devices*) dengan dimensi fisik dan kecepatan koneksi internet yang sangat beragam.

[GAMBAR: assets/bab4_diagram_aspek_rasio_bitrate.png]

### 1. Rasio Aspek (Aspect Ratio)

Rasio aspek adalah perbandingan proporsional antara lebar (*width*) dan tinggi (*height*) suatu tampilan visual atau bidang sensor kamera digital, yang dituliskan dalam format `Lebar:Tinggi`.

- **Format 16:9 (Lanskap Horizontal Standar Layar Lebar / Widescreen):**
Merupakan standar baku internasional untuk layar monitor komputer, laptop, televisi resolusi tinggi (Full HD / 4K), proyektor bioskop, dan platform video panjang seperti YouTube. Resolusi umum: 1920 x 1080 piksel (Full HD) atau 3840 x 2160 piksel (4K UHD).
- **Format 9:16 (Potret Vertikal Layar Ponsel Cerdas):**
Merupakan rotasi vertikal dari rasio 16:9 yang menjadi standar baku platform konten seluler modern (TikTok, Instagram Reels, YouTube Shorts). Resolusi standar: 1080 x 1920 piksel. Mengoptimalkan kenyamanan pandangan pengguna ponsel yang menggenggam perangkat dalam posisi tegak satu tangan.
- **Format 1:1 dan 4:5:** Format persegi dan potret sedang yang banyak digunakan untuk unggahan gambar feed media sosial dan antarmuka katalog digital.

### 2. Resolusi Spasial dan Kerapatan Piksel

Resolusi menyatakan jumlah total piksel (titik warna terkecil) yang menyusun citra visual pada sumbu horizontal dan vertikal:
- **720p (HD):** 1280 x 720 piksel (sekitar 0,92 Megapiksel).
- **1080p (Full HD):** 1920 x 1080 piksel (sekitar 2,07 Megapiksel) — standar emas efisiensi web dan pembelajaran saat ini.
- **2160p (4K UHD):** 3840 x 2160 piksel (sekitar 8,29 Megapiksel) — ketajaman ultra tinggi untuk layar besar.

### 3. Bitrate dan Rumus Matematis Ukuran Berkas Multimedia

*Bitrate* adalah laju aliran data yang diproses atau ditransmisikan per satuan detik, dinyatakan dalam satuan *kilobit per second* (kbps) atau *megabit per second* (Mbps). Bitrate menentukan kualitas ketajaman audio-visual sekaligus ukuran akhir berkas digital.

Ukuran berkas multimedia dapat dihitung secara matematis menggunakan rumus dasar komputasi:
`Ukuran Berkas (Megabyte) = (Total Bitrate dalam Mbps * Durasi dalam Detik) / 8`

*Contoh Perhitungan:*
Sebuah video edukasi berdurasi 120 detik (2 menit) direkam dengan bitrate video 5 Mbps dan bitrate audio 128 kbps (~0,128 Mbps). Total bitrate = 5,128 Mbps.
Ukuran berkas = (5,128 * 120) / 8 = 615,36 / 8 = **76,92 Megabyte**.
Jika bitrate dinaikkan menjadi 40 Mbps tanpa perhitungan, ukuran berkas melonjak menjadi lebih dari 600 Megabyte, menyebabkan video tidak dapat dimuat dengan lancar pada jaringan seluler yang terbatas.

---

## B. PRINSIP KOMPRESI DATA: LOSSLESS VS LOSSY

Kamera digital modern merekam data mentah (*RAW*) dengan ukuran raksasa. Satu detik rekaman video mentah 1080p tanpa kompresi pada kecepatan 30 bingkai per detik (FPS) dapat menghabiskan memori sebesar 180 Megabyte (lebih dari 10 Gigabyte per menit!). Agar media dapat disimpan di kartu memori dan dialirkan melalui internet, diperlukan algoritma kompresi data (*codec*).

### 1. Kompresi Tanpa Kehilangan Data (Lossless Compression)

Algoritma *Lossless* bekerja dengan cara mengidentifikasi dan mengeliminasi redundansi statistik data matematika tanpa membuang satu bit pun informasi asli. Ketika berkas didekompresi, citra atau suara yang dihasilkan persis 100% sama dengan data sumber.

- **Karakteristik:** Kualitas sempurna tanpa degradasi, namun rasio pengecilan ukuran relatif moderat (biasanya hanya berkurang 30% hingga 50%).
- **Contoh Format Lossless:**
  - Gambar: **PNG** (Portable Network Graphics), TIFF, BMP.
  - Audio: **FLAC** (Free Lossless Audio Codec), WAV PCM mentah, ALAC.
  - Dokumen/Arsip: ZIP, RAR, 7z.

### 2. Kompresi dengan Pengurangan Data Persepsi (Lossy Compression)

Algoritma *Lossy* memanfaatkan kelemahan batas persepsi indra penglihatan dan pendengaran manusia (*psikoakustik* dan *psikovisual*). Detail frekuensi warna yang sangat halus atau gelombang suara di luar ambang sensitivitas telinga manusia sengaja dieliminasi secara cerdas untuk menghasilkan ukuran berkas yang sangat drastis mengecil (sering kali terkompresi hingga 90% dari ukuran aslinya).

- **Karakteristik:** Ukuran berkas sangat ringkas, sangat efisien untuk streaming jaringan internet, namun data yang dihilangkan tidak dapat dikembalikan lagi secara permanen.
- **Contoh Format Lossy:**
  - Gambar: **JPEG/JPG**, WebP lossy.
  - Audio: **MP3**, AAC, Ogg Vorbis.
  - Video: **H.264 / AVC (MP4)**, H.265 / HEVC, VP9, AV1.

---

## C. PRINSIP PERANCANGAN DESAIN ANTARMUKA BERPUSAT PENGGUNA (USER-CENTERED DESIGN)

Produksi media digital interaktif tidak hanya berkaitan dengan video pasif, melainkan juga mencakup perancangan antarmuka aplikasi, portal pembelajaran interaktif, dan situs web. Arsitek sistem harus memastikan antarmuka yang dibuat ramah pengguna (*User-Friendly*).

Berdasarkan teori desain legendaris dari **Don Norman** (*The Design of Everyday Things*), ada empat pilar penting dalam perancangan antarmuka:

1. **Affordance (Keterjangkauan):** Sifat visual suatu objek yang memberikan petunjuk alami kepada pengguna tentang bagaimana objek tersebut harus dioperasikan. Misalnya, tombol virtual yang memiliki bayangan timbul secara alami mengisyaratkan bahwa elemen tersebut dapat ditekan (*clickable*).
2. **Signifiers (Penanda):** Tanda atau label eksplisit yang mengomunikasikan tindakan apa yang diharapkan. Contoh: Ikon kaca pembesar di samping kotak teks yang menegaskan fungsi pencarian.
3. **Feedback (Umpan Balik Instan):** Respons langsung dari sistem saat pengguna melakukan interaksi. Contoh: Warna tombol berubah saat disentuh, bilah progres berjalan (*progress bar*) saat berkas diunggah, atau suara klik lembut saat aksi berhasil.
4. **Constraints (Batasan Aman):** Membatasi tindakan tertentu untuk mencegah pengguna membuat kesalahan fatal (*error prevention*). Contoh: Menonaktifkan tombol "Kirim" (*disabled state*) hingga seluruh formulir wajib terisi dengan benar.

Selain pilar Norman, perancang wajib mematuhi standar aksesibilitas web internasional **WCAG (Web Content Accessibility Guidelines)**: menjamin rasio kontras teks terhadap latar belakang minimal 4,5:1 agar mudah dibaca oleh penyandang tunanetra parsial atau saat layar terkena pantulan sinar matahari terik.

---

## D. ETIKA DIGITAL, HAK KEKAYAAN INTELEKTUAL (HKI), DAN KONTEN KECERDASAN ARTIFISIAL

Di tengah maraknya pemanfaatan teknologi Generative AI yang mampu menciptakan gambar, musik, dan teks sintetis dalam sekejap, kesadaran hukum dan etika Hak Kekayaan Intelektual (HKI) menjadi benteng moral seorang insan terpelajar.

### 1. Spektrum Lisensi Hak Cipta dan Lisensi Creative Commons (CC)

Tidak semua gambar dan musik di mesin pencari internet boleh diunduh dan digunakan begitu saja. Sebagian besar karya dilindungi hak cipta penuh (*All Rights Reserved*). Untuk karya yang dibagikan secara terbuka, pencipta biasanya menyematkan lisensi **Creative Commons (CC)**:

- **CC BY (Attribution):** Karya boleh diubah, disebarkan, dan digunakan bahkan untuk tujuan komersial, dengan syarat **wajib mencantumkan atribusi/kredit nama pencipta aslinya**.
- **CC SA (ShareAlike):** Karya turunan wajib disebarluaskan di bawah lisensi yang identik dengan karya aslinya.
- **CC NC (NonCommercial):** Karya hanya boleh digunakan untuk tujuan non-komersial (edukasi/sosial).
- **CC ND (NoDerivatives):** Karya boleh disebarkan secara utuh namun dilarang diubah, dipotong, atau dimodifikasi dalam bentuk apa pun.
- **Public Domain (CC0):** Karya yang telah dilepaskan hak ciptanya ke publik atau masa perlindungan hak ciptanya telah kedaluwarsa, bebas digunakan oleh siapa pun tanpa syarat.

### 2. Bahaya Manipulasi Digital dan Etika Konten Berbasis AI

Dengan maraknya perangkat lunak pengubah wajah dan suara (*Deepfake*), siswa wajib memiliki integritas digital tinggi:
1. **Transparansi Sumber:** Selalu sertakan label keterangan jika suatu konten multimedia dihasilkan atau dimodifikasi oleh perangkat kecerdasan artifisial.
2. **Larangan Fitnah dan Disinformasi:** Dilarang keras memproduksi atau menyebarkan media manipulasi sintetis yang menyerang kehormatan, privasi, atau menyebarkan berita bohong (*hoax*).
3. **Pemberian Atribusi:** Hargai hak moral seniman, fotografer, dan musisi yang karyanya dijadikan referensi dalam proyek kreatif kalian.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 4.1

### Kampanye Publik Digital Sosialisasi Literasi AI untuk Komunitas Sekolah

**Tujuan Pembelajaran:**
Peserta didik secara berkelompok mampu memproduksi satu paket konten multimedia edukasi interaktif berdurasi 60-90 detik bertema "Etika & Pemanfaatan AI yang Aman di Sekolah", menerapkan rasio aspek tepat (9:16 atau 16:9), mengoptimalkan bitrate kompresi, serta menyertakan atribusi HKI dan prinsip desain berpusat pengguna.

**Alat dan Bahan:**
1. Kamera ponsel cerdas / perekam layar komputer.
2. Perangkat lunak penyunting video (CapCut, DaVinci Resolve, Kdenlive, atau platform berbasis web).
3. Pustaka musik dan ikon berlisensi Creative Commons (CC-BY atau Domain Publik).

**Langkah Kerja Proyek:**
1. Bentuklah kelompok kerja beranggotakan 3 orang (membagi peran: Penulis Naskah & Sutradara, Kameramen & Editor Video, serta Desainer Grafis & Audio).
2. Tentukan target media penyebaran:
   - Jika menargetkan media sosial seluler (Instagram Reels / TikTok): Atur kanvas proyek ke resolusi 1080 x 1920 piksel (Rasio 9:16).
   - Jika menargetkan portal web sekolah / YouTube: Atur kanvas proyek ke resolusi 1920 x 1080 piksel (Rasio 16:9).
3. Terapkan prinsip desain Norman:
   - Gunakan teks penjelasan (*subtitles*) berukuran tegas dengan kontras warna tinggi (WCAG compliant) di zona aman pandang (*safe area*).
   - Berikan umpan balik visual animasi lembut saat poin penting ditekankan.
4. Ekspor video dengan parameter kompresi teroptimasi:
   - Codec: H.264 / MP4.
   - Bitrate Video: Target 4 hingga 6 Mbps (menghasilkan ukuran berkas di bawah 45 MB).
   - Bitrate Audio: AAC 128 kbps stereo.
5. Cantumkan kartu kredit (*credit roll*) di akhir tayangan yang mencantumkan nama anggota kelompok, sumber aset visual/audio berlisensi Creative Commons, dan deklarasi pemanfaatan perangkat AI.

**Tabel Penilaian Produk:**
- Kesesuaian rasio aspek dan resolusi (25%)
- Kualitas kompresi dan kelancaran pemutaran berkas (25%)
- Penerapan prinsip keterbacaan antarmuka WCAG (25%)
- Kepatuhan etika HKI dan transparansi atribusi (25%)

---

## F. RANGKUMAN MATERI BAB IV

1. **Anatomi Multimedia:** Rasio aspek 16:9 adalah standar layar horizontal, sedangkan 9:16 adalah standar layar ponsel vertikal. Resolusi Full HD (1080p) merupakan standar emas keseimbangan detail dan efisiensi internet. Bitrate menentukan laju data per detik dan berbanding lurus dengan ukuran fisik berkas.
2. **Prinsip Kompresi:**
   - *Lossless:* Mengecilkan data tanpa membuang informasi (PNG, FLAC, ZIP), cocok untuk master arsip dan grafis teks bergaris tegas.
   - *Lossy:* Membuang data persepsi yang tidak disadari indra manusia (JPEG, MP3, MP4 H.264), menghasilkan berkas sangat ringkas yang ideal untuk distribusi jaringan internet.
3. **Desain Berpusat Pengguna (UCD):** Mengadopsi prinsip Don Norman (Affordance, Signifiers, Feedback, Constraints) serta standar aksesibilitas WCAG untuk menciptakan pengalaman pengguna yang inklusif, nyaman, dan bebas galat.
4. **Integritas dan Etika HKI:** Menggunakan karya pihak ketiga wajib mematuhi lisensi Creative Commons (CC) dan domain publik. Pemanfaatan AI generatif mewajibkan transparansi deklarasi demi mencegah bahaya disinformasi dan pelanggaran hak cipta.

---

## G. UJI KOMPETENSI BAB IV

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Format rasio aspek proporsional yang menjadi standar industri global untuk video vertikal pada layar ponsel pintar (seperti konten Shorts dan Reels) adalah...
   A. 4:3
   B. 16:9
   C. 9:16
   D. 21:9

2. Sebuah video pembelajaran berdurasi 80 detik diekspor dengan total bitrate 6 Mbps. Berapakah perkiraan ukuran berkas (*file size*) video tersebut dalam satuan Megabyte?
   A. 480 MB
   B. 60 MB
   C. 80 MB
   D. 12 MB

3. Karakteristik utama dari metode kompresi data *Lossless* dibandingkan dengan metode *Lossy* adalah...
   A. Ukuran berkas hasil kompresi selalu lebih kecil daripada Lossy
   B. Menghapus frekuensi suara tinggi untuk menghemat kapasitas penyimpanan
   C. Mampu merekonstruksi data secara sempurna 100% identik dengan berkas asli tanpa ada bit yang hilang
   D. Hanya dapat diterapkan pada berkas teks dan tidak bisa untuk gambar

4. Format berkas audio digital berikut ini yang menggunakan algoritma kompresi tanpa kehilangan data (*lossless*) adalah...
   A. MP3
   B. AAC
   C. FLAC
   D. WMA

5. Sifat fisik atau visual dari suatu elemen desain pada layar antarmuka yang mengomunikasikan secara alami kepada pengguna mengenai cara interaksinya (misalnya tombol yang tampak timbul dan mengundang untuk diklik) dalam teori Don Norman disebut...
   A. Signifiers
   B. Affordance
   C. Constraints
   D. Feedback

6. Standar internasional yang mengatur panduan aksesibilitas konten web (seperti rasio kontras teks minimal 4,5:1 agar ramah bagi semua pengguna) dikenal dengan singkatan...
   A. IEEE
   B. WCAG
   C. ISO 9001
   D. ANSI

7. Simbol lisensi Creative Commons dengan kode **CC BY** memiliki arti bahwa pengguna lain diperbolehkan menyalin, memodifikasi, dan menyebarkan karya tersebut dengan kewajiban utama...
   A. Membayar royalti bulanan kepada pencipta
   B. Tidak boleh mengubah karya sama sekali
   C. Wajib mencantumkan atribusi kredit kepada pencipta aslinya
   D. Hanya boleh digunakan untuk kepentingan militer

8. Mengapa gambar ikonik dengan latar belakang transparan dan teks grafis bergaris tegas lebih disarankan disimpan dalam format PNG daripada format JPEG?
   A. Karena format JPEG tidak mendukung saluran transparansi (*alpha channel*) dan kompresi lossy-nya dapat menimbulkan artefak buram di sekitar garis tepi teks
   B. Karena ukuran berkas JPEG selalu lebih besar daripada PNG
   C. Karena format PNG hanya dapat dibuka pada sistem operasi Linux
   D. Karena format JPEG membalikkan warna secara acak

9. Fitur antarmuka yang membuat tombol "Konfirmasi Pembayaran" menjadi berwarna abu-abu redup dan tidak dapat diklik sebelum kotak centang syarat dan ketentuan dicentang merupakan penerapan dari prinsip...
   A. Feedback
   B. Constraints
   C. Affordance
   D. Dissemination

10. Praktik etis yang wajib dilakukan oleh seorang pembuat konten multimedia ketika menggunakan bantuan alat Generative AI dalam menyusun ilustrasi atau narasi video adalah...
    A. Mengklaim bahwa seluruh karya tersebut dibuat 100% secara manual dengan tangan
    B. Menjual karya tersebut ke museum seni tanpa lisensi
    C. Memberikan label transparansi atau atribusi yang menyatakan bahwa konten tersebut dibantu oleh teknologi AI
    D. Menghapus tanda air (*watermark*) hak cipta milik orang lain

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan keterkaitan teknis antara parameter Resolusi, Frame Rate (FPS), dan Bitrate terhadap ukuran berkas dan kelancaran pemutaran (*streaming*) video melalui jaringan internet seluler!
2. Uraikan perbedaan mendasar antara kompresi *Lossless* dan *Lossy*! Mengapa untuk kebutuhan pencetakan baliho grafis resolusi tinggi format PNG/TIFF lebih disukai, sedangkan untuk katalog belanja daring format WebP/JPEG lebih diprioritaskan?
3. Analisislah empat pilar desain antarmuka menurut Don Norman (Affordance, Signifiers, Feedback, Constraints) pada aplikasi pemutar video digital yang biasa kalian gunakan di ponsel cerdas!
4. Jelaskan apa yang dimaksud dengan lisensi Creative Commons varian **CC BY-NC-SA**! Sebutkan hak dan kewajiban apa saja yang melekat pada pihak yang ingin memanfaatkan karya berlisensi tersebut!
5. Fenomena konten manipulasi wajah dan suara sintetis (*Deepfake*) semakin marak di ruang publik digital. Jelaskan minimal tiga ancaman bahaya sosial dari penyalahgunaan teknologi ini dan langkah mitigasi etis yang harus diambil oleh generasi muda!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB IV

**Kunci Pilihan Ganda:**
1. **C** (Rasio 9:16 adalah rasio potret standar ponsel cerdas).
2. **B** (Perhitungan: Ukuran = (6 Mbps * 80 detik) / 8 = 480 / 8 = 60 Megabyte).
3. **C** (Kompresi lossless merekonstruksi berkas secara sempurna persis seperti data asli).
4. **C** (FLAC adalah Free Lossless Audio Codec).
5. **B** (Affordance adalah karakteristik visual yang mengisyaratkan cara pengoperasian objek).
6. **B** (WCAG singkatan dari Web Content Accessibility Guidelines).
7. **C** (CC BY mewajibkan pemberian atribusi/kredit pencipta asli).
8. **A** (JPEG tidak mendukung transparansi alpha dan kompresi lossy-nya menimbulkan artefak ringing pada batas teks tegas).
9. **B** (Constraints membatasi tindakan salah pengguna dengan menonaktifkan kontrol).
10. **C** (Transparansi deklarasi pemanfaatan AI adalah prinsip etika dan integritas digital modern).

**Pembahasan Soal Uraian:**
1. *Hubungan Resolusi, FPS, Bitrate, dan Streaming:*
   - Resolusi menentukan jumlah piksel per bingkai gambar (dimensi visual).
   - Frame Rate (FPS) menentukan jumlah bingkai gambar yang diputar per detik (kelancaran gerak animasi).
   - Bitrate adalah volume bit data yang dialirkan per detik. Semakin tinggi resolusi dan FPS, bitrate yang dibutuhkan semakin besar untuk mempertahankan kejernihan. Namun jika bitrate melampaui kapasitas pita lebar jaringan internet seluler pengguna, pemutar video akan sering mengalami *buffering* (jeda putar) dan menguras kuota data pengguna secara cepat.
2. *Lossless vs Lossy pada Grafis:*
   - Lossless mempertahankan seluruh bit data asli. Format PNG/TIFF tidak mengalami artefak penurunan kualitas sehingga saat dicetak pada ukuran baliho raksasa, garis dan teks tetap tajam sempurna.
   - Lossy (JPEG/WebP) membuang detail mikroskopis yang tidak disadari mata manusia untuk mereduksi ukuran berkas hingga 80-90%. Ukuran yang sangat kecil ini esensial bagi katalog belanja daring agar ribuan gambar produk dapat dimuat dalam waktu di bawah 1 detik pada koneksi internet seluler pelanggan.
3. *Empat Pilar Norman pada Pemutar Video Seluler:*
   - Affordance: Tombol segitiga horizontal secara intuitif dipersepsikan sebagai pemicu untuk memulai pemutaran.
   - Signifiers: Tulisan label durasi waktu "01:25 / 03:00" dan ikon roda gigi untuk pengaturan kualitas resolusi.
   - Feedback: Munculnya ikon animasi jeda (pause) di tengah layar saat layar disentuh dan garis pemutar (*scrubber*) berubah warna saat ditarik.
   - Constraints: Penggeser waktu tidak dapat ditarik melampaui batas durasi maksimum video.
4. *Ketentuan Lisensi CC BY-NC-SA:*
   - BY (Attribution): Wajib mencantumkan nama pembuat asli karya.
   - NC (Non-Commercial): Karya tidak boleh dimanfaatkan untuk mencari keuntungan finansial atau kepentingan komersial.
   - SA (Share-Alike): Jika karya tersebut dimodifikasi atau dijadikan materi dasar karya turunan baru, karya baru tersebut wajib disebarluaskan di bawah lisensi yang sama persis (CC BY-NC-SA).
5. *Bahaya Deepfake dan Mitigasi Etis:*
   - Tiga bahaya sosial: (1) Penipuan rekayasa sosial (*social engineering*) dengan meniru suara keluarga untuk meminta transfer uang; (2) Penyebaran disinformasi dan fitnah politik berupa video pernyataan palsu tokoh masyarakat yang memicu perpecahan bangsa; (3) Pencemaran nama baik dan pelecehan kehormatan individu melalui manipulasi foto wajah.
   - Langkah mitigasi pemuda: Selalu menerapkan prinsip verifikasi fakta (*cross-checking*), tidak langsung membagikan video mencurigakan, memeriksa kejanggalan visual (kedipan mata tidak alami, sinkronisasi bibir dan suara yang ganjil), serta menggunakan perangkat lunak digital berbasis etika untuk mendeteksi rekayasa media sintetis.


# BAB V: PENGENALAN CITRA DIGITAL (COMPUTER VISION) DAN POLA AUDIO AI

## APERSEPSI: BAGAIMANA KOMPUTER "MELIHAT" DAN "MENDENGAR"?

Di sudut bengkel rekayasa perangkat lunak dan elektronika SMK, Bagas tampak sedang mengarahkan lensa modul kamera mini ke arah deretan resistor dan kapasitor di atas konveyor berjalan. Di sampingnya, layar komputer menampilkan aliran gambar langsung. Namun alih-alih menampilkan foto pemandangan, layar tersebut dipenuhi hamparan angka-angka berderet dari 0 hingga 255.

[GAMBAR: assets/bab5_komik_pembuka_sma10.png]

"Dinda, Arya! Coba perhatikan layar ini," seru Bagas sambil memutar kenop fokus lensa kameranya. "Bagi mata kita, kita langsung tahu bahwa benda di depan kamera ini adalah sebuah resistor dengan gelang warna oranye. Namun bagi prosesor komputer, objek ini hanyalah kumpulan baris dan kolom angka biner yang sangat abstrak!"

Dinda mendekat dan menatap layar dengan takjub. "Tepat sekali, Bagas! Bagi mata manusia, melihat adalah proses biologis instan yang diterjemahkan oleh korteks visual di otak kita. Namun bagi komputer, 'melihat' adalah murni operasi matematika matriks dua dimensi atau tiga dimensi. Warna merah, hijau, dan biru dipecah menjadi nilai numerik dari tingkat kecerahan paling gelap (0) hingga paling terang (255)."

Arya menambahkan sambil tersenyum, "Dan yang paling menakjubkan, komputer mengenali bentuk tepi fisik komponenmu melalui sebuah operasi matematika yang disebut **Konvolusi (*Convolution*)**. Sebuah matriks filter kecil berukuran 3x3 digeser di atas piksel gambar untuk mendeteksi perubahan drastis intensitas warna."

"Bahkan lebih mencengangkan lagi," sambung Dinda, "pola suara dan ucapan kita juga dapat diubah menjadi gambar visual dua dimensi yang disebut **Spektrogram** melalui transformasi gelombang suara. Dengan demikian, algoritma Computer Vision yang sama dapat digunakan untuk 'melihat' suara dan mendeteksi ucapan manusia!"

"Luar biasa sekali!" seru Bagas. "Artinya, jika kita menguasai matematika citra digital dan pengenalan pola ini, kita bisa menciptakan mobil otonom yang bisa melihat jalan, sistem medis pendeteksi rontgen penyakit, hingga asisten suara cerdas!"

"Tepat! Mari kita selami cara kerja Computer Vision, filter konvolusi piksel, spektrogram audio, dan menjelajahi peta karier masa depan di dunia kecerdasan artifisial!" ajak Arya.

---

## A. REPRESENTASI CITRA DIGITAL: MATRIKS PIKSEL WARNA MERAH, HIJAU, DAN BIRU (RGB)

Agar komputer atau algoritma kecerdasan artifisial dapat memproses sebuah foto atau video, dunia visual fisik harus diubah (*digitasi*) menjadi format yang dipahami oleh sirkuit mikroprosesor: yaitu angka numerik.

[GAMBAR: assets/bab5_diagram_matriks_konvolusi_piksel.png]

### 1. Piksel dan Skala Derajat Keabuan (Grayscale)

Unsur terkecil penyusun gambar digital disebut **Piksel** (*Picture Element*).
Pada citra skala abu-abu (*grayscale*), setiap piksel direpresentasikan oleh satu nilai angka bulat tunggal berkisar antara **0 hingga 255** (menggunakan format data biner 8-bit, di mana 2^8 = 256 tingkatan):
- Angka **0** merepresentasikan intensitas cahaya nol mutlak (Warna Hitam Pekat).
- Angka **255** merepresentasikan intensitas cahaya maksimum (Warna Putih Bersih).
- Angka di antara 1 hingga 254 merepresentasikan gradasi abu-abu dari gelap hingga terang.

Dengan demikian, citra abu-abu berukuran 640 x 480 piksel sejatinya adalah sebuah **Matriks Dua Dimensi (2D)** yang memiliki 480 baris dan 640 kolom angka.

### 2. Citra Berwarna Model Ruang Warna RGB (Red, Green, Blue)

Mata manusia memiliki sel reseptor yang peka terhadap tiga panjang gelombang utama: Merah (*Red*), Hijau (*Green*), dan Biru (*Blue*). Mengadopsi prinsip optik biologis tersebut, citra berwarna pada sistem komputer disimpan dalam **Matriks Tiga Dimensi (Tensor 3D)** yang memiliki tiga lapisan saluran warna (*Channels*):
- **Saluran R (Red):** Matriks intensitas warna merah (skala 0-255).
- **Saluran G (Green):** Matriks intensitas warna hijau (skala 0-255).
- **Saluran B (Blue):** Matriks intensitas warna biru (skala 0-255).

Setiap titik piksel pada foto berwarna merupakan kombinasi aditif dari ketiga nilai tersebut `(R, G, B)`:
- `(255, 0, 0)` menghasilkan warna Merah Murni.
- `(0, 255, 0)` menghasilkan warna Hijau Murni.
- `(0, 0, 255)` menghasilkan warna Biru Murni.
- `(255, 255, 0)` perpaduan merah dan hijau menghasilkan warna Kuning Terang.
- `(255, 255, 255)` perpaduan ketiga saluran maksimum menghasilkan warna Putih Sempurna.
- `(0, 0, 0)` ketiadaan cahaya pada ketiga saluran menghasilkan warna Hitam Pekat.

---

## B. OPERASI KONVOLUSI DASAR: FILTER KERNEL 3X3 UNTUK DETEKSI TEPI

Bagaimana komputer dapat mengetahui letak batas tepi suatu benda pada foto? Apakah sebuah bentuk merupakan lingkaran bola, rambu lalu lintas, atau wajah manusia? Jawabannya diawali dengan operasi **Konvolusi Citra (*Image Convolution*)**.

### 1. Konsep Kernel / Matriks Filter

**Kernel** (atau filter) adalah sebuah matriks angka kecil—biasanya berukuran ganjil seperti 3x3 atau 5x5—yang dirancang untuk mengekstrak fitur visual tertentu dari citra sumber.

Operasi konvolusi dilakukan dengan cara:
1. Meletakkan matriks kernel 3x3 di atas segmen piksel citra yang bersesuaian.
2. Melakukan perkalian titik (*element-wise multiplication*) antara setiap nilai piksel citra dengan bobot nilai kernel yang menimpanya.
3. Menjumlahkan seluruh hasil perkalian tersebut.
4. Nilai hasil penjumlahan menjadi nilai piksel baru pada citra keluaran di posisi titik pusat kernel.
5. Geser matriks kernel satu langkah ke samping (*stride = 1*), lalu ulangi perhitungan hingga menyapu seluruh permukaan gambar.

### 2. Ragam Jenis Filter Konvolusi Standar

- **Filter Deteksi Tepi Horizontal (Kernel Sobel Horizontal):**
Mendeteksi perubahan mendadak intensitas warna dari atas ke bawah untuk menemukan garis horizon dan tepi mendatar.
Matriks Kernel:
`[[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]]`
- **Filter Deteksi Tepi Vertikal (Kernel Sobel Vertikal):**
Mendeteksi batas kontras tegak dari kiri ke kanan (seperti tiang listrik atau tepi pintu).
Matriks Kernel:
`[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
- **Filter Pengaburan (Blur / Box Blur):**
Menghaluskan citra dan menghilangkan derau (*noise*) dengan cara menghitung rata-rata nilai piksel di sekitarnya.
Matriks Kernel (semua elemen bernilai 1/9):
`[[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]`
- **Filter Penajaman (Sharpening):**
Mempertegas detail tekstur gambar dengan memberi bobot positif sangat tinggi di titik tengah dan bobot negatif di sekelilingnya:
`[[ 0, -1,  0], [-1,  5, -1], [ 0, -1,  0]]`

Operasi konvolusi inilah yang menjadi blok bangunan paling mendasar dari arsitektur jaringan saraf tiruan canggih **Convolutional Neural Networks (CNN)** yang menggerakkan sistem kemudi mobil otonom dan pengenalan wajah dunia modern.

---

## C. REPRESENTASI SUARA DIGITAL: DARI GELOMBANG AKUSTIK KE SPEKTROGRAM FREKUENSI

Suara di alam nyata adalah gelombang tekanan mekanik udara kontinu yang bergetar secara analog. Agar dapat diproses oleh AI, mikrofon menangkap gelombang tersebut dan mengubahnya menjadi sinyal listrik yang kemudian disampel (*sampling*) ke dalam angka-angka diskret.

### 1. Sampling Frekuensi Audio

Berdasarkan Teorema Nyquist-Shannon, agar suara dapat direkonstruksi dengan sempurna tanpa distorsi, frekuensi pengambilan sampel minimal harus dua kali lipat dari frekuensi tertinggi yang dapat didengar manusia (~20 kHz). Oleh karena itu, audio digital standar menggunakan laju sampel **44.100 Hz (44,1 kHz)**, yang berarti komputer merekam 44.100 data amplitudo getaran setiap satu detiknya.

### 2. Transformasi Fourier Cepat (Fast Fourier Transform / FFT)

Gelombang suara ucapan manusia sangatlah rumit karena merupakan gabungan dari puluhan nada harmonik yang bercampur menjadi satu. Melalui rumus matematika algoritma **Transformasi Fourier Cepat (FFT)**, gelombang suara yang rumit dalam ranah waktu (*time domain*) dapat diurai menjadi komponen-komponen frekuensi penyusunnya (*frequency domain*).

### 3. Keajaiban Spektrogram: Mengubah Suara Menjadi Gambar Visual

Dengan membagi rekaman audio menjadi potongan-potongan jendela waktu kecil yang berurutan lalu menerapkan transformasi FFT pada setiap jendela, kita memperoleh representasi visual dua dimensi yang disebut **Spektrogram**:
- **Sumbu Horizontal (X):** Menunjukkan aliran waktu (dalam detik).
- **Sumbu Vertikal (Y):** Menunjukkan spektrum frekuensi suara (dari nada rendah / Bass di bawah hingga nada tinggi / Treble di atas).
- **Intensitas Warna (Kecerahan):** Menunjukkan besarnya amplitudo energi desibel (dB) pada frekuensi tersebut. Warna yang terang menyala menandakan suara vokal atau instrumen yang sedang berbunyi lantang.

**Mengapa ini menjadi revolusi dalam AI Audio?**
Karena spektrogram adalah gambar visual dua dimensi, para insinyur kecerdasan artifisial dapat memanfaatkan model Computer Vision (seperti CNN) untuk memproses suara ucapan manusia! Model AI "melihat" bentuk pola spektrum kata "Buka Pintu" persis seperti melihat foto sebuah rambu lalu lintas, memungkinkan sistem pengenalan suara (*Automatic Speech Recognition*) bekerja dengan akurasi yang luar biasa tinggi.

---

## D. PETA PELUANG KARIER DAN LANSKAP KEAHLIAN DI ERA KECERDASAN ARTIFISIAL

Revolusi kecerdasan artifisial bukan hanya mengubah cara kerja perangkat lunak, melainkan juga melahirkan lanskap profesi baru dengan permintaan pasar kerja global yang sangat tinggi.

[GAMBAR: assets/bab5_peta_ekosistem_karier_ai_masa_depan.png]

Berikut adalah profesi masa depan paling bergengsi di ekosistem kecerdasan artifisial yang dapat menjadi cita-cita karier kalian:

1. **Machine Learning / Deep Learning Engineer:**
Bertugas merancang, melatih, dan mengoptimalkan arsitektur model matematika cerdas (seperti CNN untuk visi komputer atau Transformer untuk pemrosesan bahasa alami). Membutuhkan fondasi kuat dalam aljabar linear, kalkulus, dan pemrograman Python.
2. **Computer Vision Specialist:**
Insinyur yang fokus mengembangkan algoritma pengolahan citra dan video cerdas, seperti sistem deteksi cacat manufaktur pada pabrik industri, navigasi robot otonom, drone pemantau pertanian cerdas, dan analisis citra medis radiologi.
3. **Data Scientist & Data Analyst:**
Pakar yang bertugas mengekstrak wawasan strategis dari tumpukan mahadata (*Big Data*), mengidentifikasi tren tersembunyi, serta membersihkan dan menyiapkan data berkualitas tinggi untuk melatih model AI.
4. **Prompt Engineer & AI Solution Architect:**
Profesi baru yang mahir menyusun instruksi terstruktur untuk model fondasi AI generatif, mengintegrasikan antarmuka pemrograman aplikasi (API AI) ke dalam sistem perbankan, kesehatan, atau niaga digital.
5. **AI Ethics & Compliance Officer:**
Ahli hukum dan sosial-teknologi yang bertugas mengaudit sistem AI untuk memastikan model tidak mengandung bias diskriminasi SARA, menjaga kerahasiaan privasi data pengguna, dan mematuhi regulasi perlindungan data pribadi nasional maupun global.
6. **MLOps (Machine Learning Operations) Engineer:**
Jembatan antara ilmu data dan rekayasa infrastruktur server, yang mengelola penyebaran (*deployment*), pemantauan, dan pemeliharaan model AI di lingkungan komputasi awan (*cloud*) secara stabil 24/7.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 5.1

### Eksperimen Deteksi Tepi Citra Menggunakan Operasi Konvolusi Matriks Sederhana

**Tujuan Pembelajaran:**
Peserta didik mampu memahami representasi citra sebagai matriks angka numerik dua dimensi, serta mengimplementasikan operasi matematika konvolusi kernel 3x3 secara mandiri menggunakan bahasa Python murni untuk mendeteksi tepi garis gambar.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terinstal.
2. Kode editor teks.

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `praktikum_konvolusi_citra.py`.
2. Ketikkan kode program simulasi konvolusi matriks berikut:

```python
# Simulasi Citra Sederhana Berukuran 6x6 Piksel
# Angka mewakili nilai intensitas cahaya (0 = Gelap, 255 = Terang)
# Bayangkan ini adalah gambar sebuah objek putih di atas latar hitam
citra_masukan = [
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255]
]

# Matriks Kernel Sobel Vertikal untuk Deteksi Tepi Tegak
kernel_vertikal = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

def terapkan_konvolusi(citra, kernel):
    tinggi = len(citra)
    lebar = len(citra[0])
    k_size = len(kernel)
    offset = k_size // 2

    # Menyiapkan matriks keluaran kosong (berukuran 4x4 untuk citra 6x6 tanpa padding)
    hasil = []
    
    for i in range(offset, tinggi - offset):
        baris_baru = []
        for j in range(offset, lebar - offset):
            total_nilai = 0
            # Operasi perkalian titik pada jendela 3x3
            for ki in range(k_size):
                for kj in range(k_size):
                    piksel = citra[i - offset + ki][j - offset + kj]
                    bobot = kernel[ki][kj]
                    total_nilai += piksel * bobot
            
            # Membatasi nilai keluaran antara 0 hingga 255 (Clamping)
            nilai_akhir = max(0, min(255, abs(total_nilai)))
            baris_baru.append(nilai_akhir)
        hasil.append(baris_baru)
    
    return hasil

# Jalankan konvolusi deteksi tepi
citra_tepi = terapkan_konvolusi(citra_masukan, kernel_vertikal)

print("===== HASIL MATRIKS CITRA SETELAH OPERASI KONVOLUSI SOBEL =====")
for baris in citra_tepi:
    for nilai in baris:
        print(f"{nilai:5}", end=" ")
    print()
```

**Pertanyaan Analisis Laboratorium:**
1. Amatilah nilai matriks hasil konvolusi di layar terminal. Pada kolom manakah nilai angka melonjak tinggi (mendekati 255 atau lebih), dan pada kolom mana nilainya mendekati 0?
2. Mengapa nilai pada kolom yang terjadi lonjakan drastis dari 0 ke 255 menghasilkan angka yang sangat besar pada matriks keluaran?
3. Apa perbedaan konseptual antara cara kerja filter pengaburan (*blur*) yang menghitung rata-rata nilai sekitar dengan filter pendeteksi tepi yang menghitung selisih gradien kontras?

---

## F. RANGKUMAN MATERI BAB V

1. **Representasi Citra Digital:** Citra hitam-putih tersusun atas matriks dua dimensi dengan nilai piksel 0 (hitam) hingga 255 (putih). Citra berwarna tersusun atas tensor tiga dimensi dengan tiga saluran warna utama: Merah (*Red*), Hijau (*Green*), dan Biru (*Blue*).
2. **Operasi Konvolusi:** Proses matematika perkalian titik antara segmen piksel citra dengan matriks filter kecil (kernel 3x3) yang digeser menyapu seluruh citra. Berguna untuk mendeteksi tepi (*edge detection*), menajamkan gambar, maupun menyaring derau visual.
3. **Representasi Audio ke Spektrogram:** Gelombang suara analog disampel menjadi data diskret (standar 44,1 kHz). Melalui Transformasi Fourier Cepat (FFT), sinyal suara diurai menjadi spektrogram dua dimensi (waktu vs frekuensi vs amplitudo) yang memungkinkan model penglihatan komputer menganalisis ucapan manusia.
4. **Lanskap Ekosistem Karier AI:** Revolusi kecerdasan artifisial membuka peluang karier masif bagi generasi muda Indonesia, meliputi insinyur pembelajaran mesin, spesialis visi komputer, saintis data, arsitek prompt, petugas kepatuhan etika AI, hingga insinyur operasional MLOps.

---

## G. UJI KOMPETENSI BAB V

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Rentang nilai intensitas derajat keabuan (*grayscale*) 8-bit yang merepresentasikan tingkat kecerahan sebuah piksel citra digital dari gelap pekat hingga putih sempurna adalah...
   A. -128 hingga 127
   B. 0 hingga 255
   C. 1 hingga 100
   D. 0 hingga 1.024

2. Sebuah piksel pada citra berwarna memiliki kode koordinat warna RGB: `(0, 255, 0)`. Warna yang akan terpancar pada layar monitor untuk piksel tersebut adalah...
   A. Merah Murni
   B. Biru Terang
   C. Hijau Murni
   D. Putih Bersih

3. Operasi matematika mendasar dalam pemrosesan citra digital di mana sebuah matriks filter kecil digeser di atas piksel citra untuk menghitung perkalian titik dan menghasilkan fitur visual baru dinamakan...
   A. Faktorisasi
   B. Konvolusi
   C. Diferensiasi
   D. Interpolasi

4. Manakah di antara matriks kernel 3x3 berikut yang biasa digunakan untuk operasi penghalusan citra dan peredam derau (*Box Blur*)?
   A. `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`
   B. `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
   C. Semua elemen bernilai sama yaitu 1/9
   D. `[[1, 0, 0], [0, 1, 0], [0, 0, 1]]`

5. Berdasarkan Teorema Nyquist-Shannon, berapakah frekuensi pengambilan sampel (*sampling rate*) minimum yang dibutuhkan untuk merekam suara manusia agar seluruh spektrum frekuensi hingga 20.000 Hz dapat ditangkap secara utuh tanpa distorsi (*aliasing*)?
   A. 10.000 Hz
   B. 20.000 Hz
   C. 40.000 Hz
   D. 5.000 Hz

6. Representasi visual grafis dua dimensi yang memetakan spektrum frekuensi suara pada sumbu Y terhadap perubahan waktu pada sumbu X dengan intensitas warna yang menunjukkan besaran energi suara disebut...
   A. Histogram Warna
   B. Spektrogram
   C. Osiloskop
   D. Diagram Kartesius

7. Mengapa model kecerdasan artifisial Computer Vision (seperti CNN) dapat dimanfaatkan untuk mengenali perintah suara manusia (*speech recognition*)?
   A. Karena sinyal suara selalu memiliki warna merah dan biru alami
   B. Karena gelombang suara dapat diubah terlebih dahulu menjadi citra visual berupa spektrogram
   C. Karena speaker komputer memiliki kamera tersembunyi
   D. Karena suara tidak membutuhkan pemrosesan numerik

8. Profesi di era kecerdasan artifisial yang bertugas secara spesifik mengaudit model AI agar tidak menghasilkan keputusan yang mendiskriminasi kelompok masyarakat tertentu serta menjamin kepatuhan privasi data adalah...
   A. Full-stack Web Developer
   B. AI Ethics & Compliance Officer
   C. Hardware Network Technician
   D. Game Asset 3D Animator

9. Apa yang terjadi pada matriks hasil konvolusi ketika kernel pendeteksi tepi Sobel melintasi area citra yang memiliki warna seragam sempurna (misalnya seluruh pikselnya bernilai 120)?
   A. Seluruh hasil perhitungannya bernilai 0 (tidak ada tepi yang terdeteksi)
   B. Hasilnya meledak menjadi angka tak hingga
   C. Layar komputer seketika mati
   D. Seluruh piksel berubah menjadi warna merah terang

10. Praktisi teknologi yang bertanggung jawab menjembatani model kecerdasan artifisial dari lingkungan riset laboratorium menuju sistem produksi peladen awan (*cloud server*) yang stabil dan terpantau 24/7 dikenal sebagai...
    A. MLOps Engineer
    B. Database Operator
    C. Prompt Reader
    D. Desktop Technician

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan bagaimana sebuah gambar foto berwarna disimpan di dalam memori komputer dalam bentuk tensor tiga dimensi! Sebutkan peran masing-masing saluran warnanya!
2. Uraikan secara sistematis tahapan operasi konvolusi ketika sebuah matriks kernel berukuran 3x3 menyapu sebuah matriks piksel citra digital!
3. Diberikan jendela citra 3x3:
   `[[10, 10, 200], [10, 10, 200], [10, 10, 200]]`
   dan matriks kernel Sobel vertikal:
   `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`.
   Hitunglah nilai perkalian konvolusi pada titik pusat tersebut dan jelaskan maknanya!
4. Jelaskan bagaimana gelombang suara analog dari percakapan manusia dapat ditransformasikan menjadi citra dua dimensi (Spektrogram) menggunakan algoritma Transformasi Fourier Cepat (FFT)!
5. Dari berbagai prospek karier di era kecerdasan artifisial yang telah kalian pelajari, pilihlah salah satu profesi yang paling menarik minat kalian. Uraikan peran strategis profesi tersebut serta keahlian teknis apa saja yang perlu kalian persiapkan sejak duduk di bangku SMA/SMK!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB V

**Kunci Pilihan Ganda:**
1. **B** (Skala grayscale 8-bit berkisar dari 0 hingga 255).
2. **C** (RGB 0, 255, 0 merepresentasikan warna Hijau Murni).
3. **B** (Operasi pergeseran filter dan perkalian titik tersebut dinamakan konvolusi).
4. **C** (Filter Box Blur memiliki seluruh bobot yang seragam senilai 1/9 untuk menghitung nilai rata-rata lokal).
5. **C** (Teorema Nyquist mensyaratkan frekuensi sampling minimal 2x frekuensi tertinggi, yaitu 2 x 20.000 = 40.000 Hz, sehingga standar audio komersial menggunakan 44.100 Hz).
6. **B** (Spektrogram adalah visualisasi 2D frekuensi terhadap waktu).
7. **B** (Spektrogram mengubah audio menjadi gambar visual yang dapat diolah oleh algoritma visi komputer).
8. **B** (AI Ethics Officer bertugas mengawal aspek keadilan, non-bias, dan etika hukum sistem AI).
9. **A** (Pada area seragam tanpa perbedaan kontras, selisih perhitungan kernel bernilai nol murni).
10. **A** (MLOps Engineer bertanggung jawab atas deployment dan otomatisasi siklus hidup model AI di produksi).

**Pembahasan Soal Uraian:**
1. *Penyimpanan Citra Berwarna dalam Tensor 3D:*
   Citra berwarna disimpan dalam bentuk susunan matriks tiga dimensi dengan dimensi `(Tinggi, Lebar, Saluran)`. Terdapat tiga saluran (channels) terpisah, yaitu Saluran R (Red), Saluran G (Green), dan Saluran B (Blue). Setiap sel pada masing-masing saluran berisi nilai skalar bilangan bulat 0-255 yang menyatakan intensitas kecerahan warna primer tersebut. Perpaduan intensitas ketiga saluran pada koordinat piksel yang sama merekonstruksi spektrum lebih dari 16,7 juta variasi warna yang ditangkap mata manusia.
2. *Tahapan Operasi Konvolusi:*
   - Letakkan kernel di atas jendela piksel citra yang bersesuaian.
   - Lakukan perkalian titik (element-wise multiplication) antara setiap nilai sel kernel dengan nilai piksel citra di bawahnya.
   - Jumlahkan seluruh hasil perkalian tersebut untuk memperoleh satu angka skalar tunggal.
   - Terapkan fungsi pemotongan (clamping) jika nilai melebihi rentang 0-255.
   - Simpan nilai hasil tersebut pada matriks citra keluaran baru di koordinat titik pusat.
   - Geser kernel ke posisi piksel berikutnya sesuai nilai stride yang ditentukan.
3. *Perhitungan Konvolusi Sobel Vertikal:*
   - Baris 1: (10 * -1) + (10 * 0) + (200 * 1) = -10 + 0 + 200 = 190.
   - Baris 2: (10 * -2) + (10 * 0) + (200 * 2) = -20 + 0 + 400 = 380.
   - Baris 3: (10 * -1) + (10 * 0) + (200 * 1) = -10 + 0 + 200 = 190.
   - Total Penjumlahan: 190 + 380 + 190 = **760**.
   - Makna: Nilai positif yang sangat tinggi (760) membuktikan adanya lonjakan kontras yang sangat tajam dari gelap (10) ke terang (200) secara vertikal. Ini mengindikasikan bahwa algoritma berhasil mendeteksi adanya garis tepi tegak lurus pada batas kolom kedua dan ketiga.
4. *Transformasi Suara Menjadi Spektrogram:*
   Sinyal audio analog disampel menjadi deretan angka amplitudo terhadap waktu. Sinyal yang panjang dipotong menjadi bingkai-bingkai waktu pendek (misalnya durasi 25 milidetik). Pada setiap bingkai, algoritma FFT (Fast Fourier Transform) dijalankan untuk menguraikan getaran gabungan menjadi spektrum frekuensi individual beserta kekuatannya. Spektrum-spektrum frekuensi ini kemudian disusun berjajar dari kiri ke kanan sesuai urutan waktu, menghasilkan citra dua dimensi (Spektrogram) di mana tinggi menyatakan nada dan warna menyatakan volume suara.
5. *Eksplorasi Karier Masa Depan (Contoh Analisis):*
   Jika memilih menjadi seorang *Computer Vision Specialist*, peran strategisnya adalah merancang mata cerdas buatan bagi peradaban industri—seperti sistem inspeksi kualitas pangan otomatis atau navigasi robotik ramah disabilitas. Keahlian teknis yang harus dipersiapkan sejak bangku SMA/SMK meliputi: penguasaan matematika matriks dan aljabar linear, keterampilan koding Python tingkat lanjut, pemahaman pemrosesan citra digital, serta pembiasaan diri membedah arsitektur jaringan saraf tiruan melalui berbagai proyek praktikum nyata.


# BAB VI: REKAYASA PROMPT TINGKAT LANJUT DAN PERANCANGAN SOLUSI SISTEM AI

## APERSEPSI: INOVASI CAPSTONE PROJECT SEKOLAH HIJAU CERDAS

Pagi itu, aula serbaguna sekolah dipenuhi antusiasme ratusan siswa dan dewan guru dalam pameran karya inovasi teknologi akhir tahun. Di stan pameran kelas Fase E, sebuah prototipe tempat sampah cerdas berpanel surya yang dilengkapi kamera pemilah otomatis dan asisten analisis energi sekolah menarik perhatian dewan juri. Stan tersebut dijaga oleh Arya, Dinda, dan Bagas.

[GAMBAR: assets/bab6_komik_pembuka_sma10.png]

"Luar biasa sekali prototipe ini!" puji salah seorang dewan juri sambil mengamati sistem kamera yang membedakan botol plastik dan daun kering. "Namun bagaimana kalian merancang sistem kecerdasan artifisial di baliknya agar mampu menghasilkan laporan efisiensi energi yang akurat tanpa mengalami halusinasi informasi atau bias data?"

Dinda tersenyum mantap dan membuka panel interaktif di tabletnya. "Kunci utamanya terletak pada penerapan metodologi **Design Thinking** sejak hari pertama kami mengamati permasalahan timbunan sampah di kantin sekolah. Kami tidak langsung melompat membuat kode, melainkan berempati dengan petugas kebersihan dan menganalisis kebutuhan riil sekolah."

Arya menambahkan, "Dan untuk modul asisten perencana energinya, kami tidak menggunakan instruksi sembarangan. Kami menerapkan rekayasa prompt tingkat lanjut berbasis kerangka kerja **ROCCF (*Role, Objective, Context, Constraint, Format*)** yang dipadukan dengan teknik penalaran terstruktur ***Chain-of-Thought* (CoT)**. Sistem AI dipaksa berpikir bertahap langkah demi langkah sebelum menarik kesimpulan matematis."

Bagas mengangguk seraya menunjuk sensorik perangkat kerasnya. "Dan kami memastikan bahwa seluruh data masukan disaring secara ketat agar privasi warga sekolah tetap terlindungi sejalan dengan etika kecerdasan artifisial global."

"Kerja tim yang sangat matang!" puji sang juri. "Kalian telah memadukan sains algoritma, rekayasa perangkat lunak, dan kepekaan sosial menjadi sebuah karya inovasi berdaya guna nyata!"

---

## A. KERANGKA KERJA REKAYASA PROMPT CERDAS: ROCCF FRAMEWORK

Di era model bahasa besar (*Large Language Models / LLM*), kemampuan berinteraksi dengan AI bukan lagi sekadar mengetik pertanyaan santai di kolom obrolan. Interaksi tingkat profesional menuntut keahlian **Rekayasa Prompt (*Prompt Engineering*)** yang presisi, deterministik, dan bebas ambiguitas.

[GAMBAR: assets/bab6_piramida_framework_roccf_prompt.png]

Salah satu kerangka kerja paling komprehensif dan diakui dalam industri teknologi adalah **ROCCF Framework**:

### 1. Lima Pilar Anatomi ROCCF

1. **Role (Peran Spesifik):** Menetapkan persona, kepakaran akademis, dan sudut pandang profesional yang wajib diadopsi oleh AI.
   *Contoh:* "Bertindaklah sebagai Konsultan Audit Energi Lingkungan bersertifikasi internasional dan Spesialis Sistem Berkelanjutan."
2. **Objective (Tujuan Terukur):** Menjelaskan tugas utama apa yang harus diselesaikan secara jelas, tegas, dan spesifik tanpa tafsir ganda.
   *Contoh:* "Analisis data konsumsi daya listrik sekolah pada tabel terlampir dan susun 3 rekomendasi penghematan biaya bulanan."
3. **Context (Konteks Latar Belakang):** Memberikan informasi pelengkap, batasan operasional, kondisi geografis, profil pengguna, dan latar masalah riil.
   *Contoh:* "Gedung sekolah ini memiliki 3 lantai, 24 ruang kelas dengan 48 unit AC, dan tarif listrik dasar Rp1.444 per kWh. Beban puncak terjadi pukul 10.00 hingga 14.00."
4. **Constraint (Batasan Ketat & Larangan):** Menetapkan batasan tegas mengenai apa yang TIDAK BOLEH dilakukan, panjang kata, nada bahasa, batasan anggaran, dan larangan membuat asumsi tanpa data.
   *Contoh:* "Jangan merekomendasikan penggantian genset mahal. Batasi estimasi investasi di bawah Rp5.000.000. Wajib sertakan perhitungan rumus matematis penghematan."
5. **Format (Format Luaran Terstruktur):** Menentukan bentuk akhir penyajian data agar mudah diintegrasikan ke sistem lain (misalnya format Tabel Markdown, dokumen JSON, atau poin bernomor).
   *Contoh:* "Sajikan luaran akhir dalam bentuk Tabel Markdown yang terdiri atas kolom: No, Nama Solusi, Estimasi Biaya, Penghematan Bulanan (Rp), dan Waktu Balik Modal (Bulan)."

---

## B. TEKNIK REKAYASA PENALARAN: FEW-SHOT PROMPTING DAN CHAIN-OF-THOUGHT (COT)

Ketika dihadapkan pada tugas yang membutuhkan perhitungan matematika rumit, logika penalaran multi-tahap, atau analisis kausalitas, perintah instruksi langsung (*Zero-Shot*) sering kali membuat model AI mengalami kesalahan logika (*logical fallacy*). Untuk mengatasi kendala tersebut, digunakan dua teknik penalaran mutakhir:

### 1. Few-Shot Prompting (Pembelajaran Berbasis Contoh Pasangan)

Berbeda dengan *Zero-Shot* (memerintahkan AI memecahkan masalah tanpa contoh sebelumnya), **Few-Shot Prompting** membekali model AI dengan 2 hingga 5 contoh pasangan Masukan (*Input*) dan Luaran (*Output*) standar yang diharapkan sebelum memberikan tugas sebenarnya.

Dengan melihat pola contoh tersebut, model AI secara otomatis menyesuaikan parameter distribusinya untuk meniru struktur logika, gaya bahasa, dan akurasi yang diinginkan.

### 2. Chain-of-Thought (CoT) Prompting: "Mari Berpikir Langkah demi Langkah"

Ditemukan oleh para peneliti Google Research, teknik *Chain-of-Thought* memandu model AI untuk menguraikan tahapan penalaran secara eksplisit sebelum menyimpulkan jawaban akhir.

Secara mengejutkan, hanya dengan menyematkan kalimat pemicu sederhana seperti:
*"Uraikan penalaran logis Anda langkah demi langkah secara bertahap sebelum menuliskan jawaban final!"*
tingkat keberhasilan model AI dalam memecahkan soal matematika dan logika algoritma melonjak drastis dari ~17% menjadi lebih dari 80%! Hal ini terjadi karena proses penguraian token kata demi kata memberikan "ruang kerja memori kerja (*scratchpad*)" bagi jaringan transformer untuk menghitung keterkaitan relasi konsep secara mendalam.

---

## C. PERANCANGAN PROTOTIPE SISTEM BERBASIS AI DENGAN METODE DESIGN THINKING

Teknologi AI secanggih apa pun tidak akan memiliki nilai jika tidak menyelesaikan permasalahan nyata manusia. Oleh karena itu, para pengembang profesional memadukan rekayasa teknologi dengan metodologi **Design Thinking** yang berpusat pada manusia (*Human-Centered Design*).

Proses perancangan mencakup lima fase iteratif:

1. **Empathize (Membangun Empati Mendalam):**
Mengamati, mewawancarai, dan merasakan secara langsung kesulitan yang dialami oleh calon pengguna di lingkungan sekitar (misalnya mewawancarai petugas kebersihan sekolah tentang kendala memilah sampah organik dan anorganik).
2. **Define (Merumuskan Inti Masalah):**
Menyintesis hasil observasi menjadi rumusan masalah yang tajam dalam format *Point of View (POV)*: *"Petugas kebersihan sekolah membutuhkan cara otomatis memilah sampah di sumbernya karena volume sampah melonjak drastis saat jam istirahat dan fasilitas pemilahan manual memakan waktu berjam-jam."*
3. **Ideate (Eksplorasi Ide Solusi AI):**
Melakukan curah gagasan (*brainstorming*) berbagai alternatif solusi berbasis komputasi cerdas tanpa batasan awal, lalu memilih ide paling berdampak tinggi dan layak direalisasikan (*High Impact, High Feasibility*).
4. **Prototype (Membangun Purwarupa Cepat):**
Membuat model kerja sederhana—menggabungkan skrip kode Python, kamera mini, papan mikrokontroler, dan prompt ROCCF—untuk memvisualisasikan cara kerja solusi sebelum diproduksi massal.
5. **Test (Pengujian dan Uji Validasi Pengguna):**
Meletakkan purwarupa di lokasi riil, mengamati interaksi pengguna nyata, mengukur tingkat akurasi dan kegagalan, serta mengumpulkan umpan balik untuk perbaikan berkelanjutan (*continuous improvement*).

---

## D. MITIGASI RISIKO HALUSINASI AI, PRIVASI DATA, DAN TANGGUNG JAWAB INOVATOR

Sebagai generasi penerus bangsa yang menguasai teknologi kecerdasan artifisial, integritas etika adalah kompas moral yang tidak boleh ditawar.

### 1. Fenomena Halusinasi AI (*AI Hallucination*)

Halusinasi AI adalah fenomena di mana model AI menghasilkan jawaban yang terdengar sangat meyakinkan, runtut, dan percaya diri, namun secara faktual sepenuhnya salah, palsu, atau hasil karangan fiktif belaka. Hal ini terjadi karena model LLM bekerja memprediksi probabilitas kata berikutnya (*next-token prediction*), bukan memahami hakikat kebenaran seperti akal budi manusia.

**Cara Mencegah Halusinasi AI:**
- Sertakan data rujukan resmi di dalam prompt (*Ground Truth Anchoring*).
- Berikan batasan tegas: *"Jika jawaban tidak terdapat dalam dokumen terlampir, nyatakan secara jujur bahwa Anda tidak mengetahuinya. Dilarang mengarang fakta!"*
- Selalu lakukan verifikasi silang (*cross-examination*) terhadap rumus, angka statistik, dan kutipan undang-undang.

### 2. Perlindungan Data Pribadi (PII) dan Mitigasi Bias

- **Larangan Mengunggah PII:** Jangan pernah memasukkan data pribadi yang dapat mengidentifikasi seseorang (*Personally Identifiable Information* / PII)—seperti Nomor Induk Kependudukan (NIK), riwayat rekam medis, kata sandi, atau nomor rekening bank—ke dalam layanan AI publik yang terhubung dengan internet.
- **Audit Bias Sosial:** Model AI dilatih menggunakan data dari internet yang mungkin memuat prasangka ras, gender, atau stereotip negatif. Inovator wajib menguji sistemnya secara ketat untuk menjamin keadilan (*fairness*) perlakuan terhadap seluruh lapisan masyarakat.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 6.1

### Capstone Project: Prototipe Solusi AI Sekolah Ramah Lingkungan

**Tujuan Pembelajaran:**
Peserta didik secara kolaboratif mampu merancang satu konsep solusi sistemik berbasis kecerdasan artifisial untuk memecahkan isu keberlanjutan lingkungan di sekolah, menerapkan framework prompt ROCCF berantai, serta menyusun dokumen spesifikasi kebutuhan sistem berbasis Design Thinking.

**Petunjuk Pelaksanaan Proyek:**
1. Bentuklah tim proyek beranggotakan 3 orang. Pilihlah salah satu tema lingkungan sekolah:
   - Manajemen Pengurangan Sampah Makanan Kantin.
   - Otomasi Penghematan Listrik dan Pendingin Ruangan (AC) Cerdas.
   - Sistem Pemantauan Kualitas Udara dan Penghijauan Taman Sekolah.
2. Lakukan wawancara singkat (*Empathize*) kepada minimal dua warga sekolah (guru, pengelola kantin, atau petugas kebersihan).
3. Rumuskan dokumen spesifikasi proyek dengan format terstruktur:
   - **Judul Proyek:** Nama sistem inovasi.
   - **Pernyataan Masalah (Define):** Rumusan POV kendala nyata yang ditemukan.
   - **Arsitektur Sistem (Ideate & Prototype):** Diagram alur data masukan (sensor/kamera/teks) -> modul pemrosesan Python / model AI -> aksi luaran sistem.
   - **Formulasi Prompt ROCCF:** Rancang satu prompt lengkap yang digunakan sistem AI untuk menganalisis data lingkungan tersebut.
   - **Strategi Mitigasi Etika & Halusinasi:** Langkah konkret untuk melindungi data privasi dan menjamin akurasi laporan.
4. Presentasikan poster cetak atau tayangan digital prototipe solusi kalian di hadapan kelas!

---

## F. RANGKUMAN MATERI BAB VI

1. **Rekayasa Prompt ROCCF:** Kerangka kerja terstruktur penyusunan instruksi AI yang mencakup *Role* (Peran kepakaran), *Objective* (Tujuan terukur), *Context* (Latar situasi), *Constraint* (Batasan & larangan ketat), dan *Format* (Bentuk luaran spesifik) guna menghasilkan respon AI yang presisi dan profesional.
2. **Teknik Penalaran CoT & Few-Shot:** Memberikan contoh pasangan input-output (*Few-Shot*) dan menyematkan instruksi penalaran langkah demi langkah (*Chain-of-Thought*) melipatgandakan akurasi AI dalam memecahkan persoalan matematika dan logika rumit.
3. **Metodologi Design Thinking:** Proses perancangan solusi teknologi berorientasi pengguna melalui 5 siklus berkesinambungan: *Empathize* (empati), *Define* (definisi masalah), *Ideate* (curah ide), *Prototype* (purwarupa), dan *Test* (validasi lapangan).
4. **Etika dan Mitigasi Halusinasi:** Inovator bertanggung jawab mencegah disinformasi akibat halusinasi AI dengan teknik *ground truth anchoring*, melindungi kerahasiaan informasi pribadi (PII), serta mengeliminasi bias diskriminatif dalam sistem cerdas.

---

## G. EVALUASI AKHIR TAHUN FASE E

### I. Pilihan Ganda Komprehensif (Bab I - VI)
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Berapakah jumlah langkah perbandingan maksimum yang dibutuhkan algoritma Binary Search untuk mencari data sasaran pada himpunan data terurut sebanyak 2.048 elemen?
   A. 2.048 langkah
   B. 1.024 langkah
   C. 11 langkah
   D. 1 langkah

2. Algoritma pengurutan yang bekerja dengan membandingkan dua elemen bersebelahan dan menukarnya secara berulang hingga elemen terbesar bergeser ke posisi paling belakang adalah...
   A. Selection Sort
   B. Insertion Sort
   C. Bubble Sort
   D. Quick Sort

3. Kompleksitas waktu asimptotik dari sebuah fungsi yang mengakses elemen pada struktur data Dictionary Python berdasarkan kunci uniknya adalah...
   A. O(1)
   B. O(log n)
   C. O(n)
   D. O(n^2)

4. Blok kode yang dijamin akan selalu dijalankan dalam arsitektur penanganan kesalahan (*exception handling*) Python, baik saat terjadi galat maupun saat program berjalan mulus adalah...
   A. `try`
   B. `except`
   C. `else`
   D. `finally`

5. Atribut dalam sebuah tabel basis data relasional yang berfungsi mengikat relasi dengan merujuk pada Primary Key tabel induk lain dinamakan...
   A. Composite Key
   B. Foreign Key
   C. Candidate Key
   D. Alternate Key

6. Manakah perintah SQL kelompok Data Manipulation Language (DML) yang tepat untuk memperbarui kolom status menjadi 'Selesai' pada tabel `tugas`?
   A. `ALTER tugas SET status = 'Selesai';`
   B. `UPDATE tugas SET status = 'Selesai';`
   C. `INSERT INTO tugas (status) VALUES ('Selesai');`
   D. `SELECT * FROM tugas WHERE status = 'Selesai';`

7. Di era media digital modern, rasio aspek standar internasional yang dirancang khusus untuk kenyamanan pandangan layar ponsel cerdas vertikal adalah...
   A. 4:3
   B. 16:9
   C. 9:16
   D. 21:9

8. Kompresi berkas digital yang mampu mengembalikan data secara sempurna persis 100% sama dengan berkas asli tanpa ada bit yang hilang disebut kompresi...
   A. Lossy
   B. Lossless
   C. Sinyal Analog
   D. Destruktif

9. Representasi sebuah citra digital skala abu-abu (*grayscale*) 8-bit dalam sistem komputasi disimpan sebagai matriks angka dengan nilai kecerahan pada rentang...
   A. 0 hingga 100
   B. 0 hingga 255
   C. -128 hingga 127
   D. 1 hingga 1.000

10. Operasi matematika menggeser matriks kernel kecil di atas piksel gambar untuk menghasilkan citra baru pendeteksi tepi pada Computer Vision disebut...
    A. Interpolasi
    B. Konvolusi
    C. Regresi
    D. Binerisasi

11. Representasi visual dua dimensi yang menggambarkan perubahan spektrum frekuensi suara terhadap waktu dengan warna yang menyatakan intensitas energi dinamakan...
    A. Histogram
    B. Spektrogram
    C. Piezogram
    D. Monokrom

12. Dalam pilar rekayasa prompt cerdas kerangka kerja ROCCF, huruf **C** pertama merepresentasikan...
    A. Code
    B. Context
    C. Computer
    D. Constant

13. Menambahkan kalimat instruksi *"Mari kita pikirkan langkah demi langkah secara bertahap"* pada prompt model bahasa besar merupakan penerapan teknik rekayasa penalaran...
    A. Zero-Shot Prompting
    B. Chain-of-Thought (CoT) Prompting
    C. SQL Injection
    D. Brute Force Query

14. Kondisi di mana model kecerdasan artifisial menghasilkan informasi yang terdengar meyakinkan namun secara faktual sepenuhnya keliru atau fiktif disebut...
    A. Overfitting
    B. AI Hallucination
    C. Data Bleeding
    D. Deadlock

15. Tahap pertama dalam metodologi *Design Thinking* yang berfokus pada upaya memahami dan merasakan secara langsung kesulitan yang dihadapi pengguna nyata adalah...
    A. Prototype
    B. Ideate
    C. Empathize
    D. Define

---

### II. Uraian Pemecahan Kasus Sistemik Berbobot HOTS
Jawablah pertanyaan-pertanyaan berikut dengan uraian mendalam, analitis, dan sistematis!

1. **Analisis Algoritma dan Basis Data:**
Sebuah aplikasi seleksi beasiswa sekolah memiliki basis data berisi 100.000 data nilai siswa yang belum terurut. Jika panitia ingin mencari data siswa dengan nomor pendaftaran tertentu:
a. Berapakah jumlah perbandingan terburuk (*worst case*) jika menggunakan Linear Search?
b. Jika data tersebut diurutkan terlebih dahulu, berapakah jumlah perbandingan terburuk menggunakan Binary Search?
c. Berikan pertimbangan arsitektural: apakah proses pengurutan data terlebih dahulu sepadan (*worth it*) jika pencarian hanya dilakukan satu kali seumur hidup versus jika pencarian dilakukan puluhan ribu kali setiap hari?

2. **Rekayasa Perangkat Lunak Bebas Crash:**
Rancanglah sebuah fungsi Python bernama `hitung_indeks_prestasi(daftar_nilai)` yang menerima daftar angka. Fungsi tersebut harus menghitung rata-rata nilai, namun harus kebal dari galat jika:
a. Pengguna memasukkan daftar kosong (tangani `ZeroDivisionError`).
b. Terdapat elemen data di dalam daftar yang bertipe string atau teks (tangani `TypeError`).
Tuliskan blok kode lengkap dengan struktur `try-except-else-finally` yang rapi sesuai standar PEP 8!

3. **Perancangan Sistem Basis Data Laboratorium (ERD):**
Laboratorium IoT sekolah memiliki tiga entitas: `Siswa`, `Alat_Sensor`, dan `Peminjaman`. Rancanglah relasi ketiga entitas tersebut! Sebutkan nama kolom atribut Primary Key dan Foreign Key untuk masing-masing tabel agar memenuhi kaidah integritas referensial dan bebas anomali!

4. **Rekayasa Prompt ROCCF:**
Sekolah kalian ingin membuat panduan hemat air di lingkungan kantin dan toilet sekolah. Rancanglah sebuah prompt lengkap dan profesional menggunakan kerangka kerja ROCCF (*Role, Objective, Context, Constraint, Format*) untuk diujikan pada sistem asisten AI cerdas!

5. **Integritas Inovator dan Etika AI:**
Sebuah kelompok siswa mengembangkan aplikasi pendeteksi emosi wajah siswa di kelas menggunakan kamera cerdas untuk menilai tingkat stres belajar. Analisislah proyek ini dari sudut pandang etika kecerdasan artifisial:
a. Apa potensi pelanggaran privasi dan risiko penyalahgunaan data (*Personally Identifiable Information*)?
b. Apa bahaya bias sistem jika model AI dilatih hanya menggunakan sampel wajah dari satu kelompok suku tertentu?
c. Rekomendasikan tiga langkah regulasi etis yang wajib dipenuhi sebelum sistem tersebut diizinkan beroperasi di sekolah!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS EVALUASI AKHIR TAHUN

**Kunci Pilihan Ganda Komprehensif:**
1. **C** (2 pangkat 11 = 2.048, sehingga worst case Binary Search adalah 11 langkah).
2. **C** (Bubble Sort menukarkan dua elemen bersebelahan secara berulang).
3. **A** (Pencarian berbasis kunci unik pada Dictionary memakan waktu konstan O(1)).
4. **D** (Blok `finally` selalu dieksekusi dalam kondisi apa pun).
5. **B** (Foreign Key merujuk pada Primary Key tabel lain untuk menjaga integritas data).
6. **B** (`UPDATE nama_tabel SET kolom = nilai` adalah sintaks DML yang tepat).
7. **C** (Rasio 9:16 adalah standar potret vertikal layar ponsel cerdas).
8. **B** (Kompresi Lossless mempertahankan seluruh data asli tanpa pengurangan bit).
9. **B** (Grayscale 8-bit berkisar dari 0 [hitam] hingga 255 [putih]).
10. **B** (Operasi pergeseran matriks filter tersebut dinamakan konvolusi).
11. **B** (Spektrogram memetakan frekuensi terhadap waktu dengan intensitas warna).
12. **B** (Huruf C pertama pada ROCCF bermakna Context / Konteks latar belakang).
13. **B** (Chain-of-Thought memicu model AI berpikir runtut langkah demi langkah).
14. **B** (AI Hallucination adalah kondisi saat AI mengarang fakta fiktif secara meyakinkan).
15. **C** (Empathize adalah tahap pertama menggali kebutuhan dan rasa empati pengguna).

**Pembahasan Soal Uraian Kasus Sistemik:**
1. *Analisis Pencarian Beasiswa:*
   a. Linear Search worst case = 100.000 kali perbandingan.
   b. Binary Search worst case = ceil(log2(100.000)) = 17 kali perbandingan.
   c. Pertimbangan Arsitektural: Mengurutkan 100.000 data membutuhkan waktu komputasi O(n log n) sekitar 1.660.000 operasi. Jika sistem hanya melakukan pencarian 1 kali seumur hidup, pengurutan tidak sepadan karena Linear Search hanya butuh maksimal 100.000 operasi. Namun, jika pencarian dilakukan ribuan kali setiap hari oleh para pendaftar, biaya awal (*initial cost*) pengurutan data sangat sepadan karena setiap pencarian berikutnya hanya butuh 17 langkah instan, menghemat jutaan siklus komputasi server.
2. *Kode Python Bebas Crash:*
   ```python
   def hitung_indeks_prestasi(daftar_nilai):
       try:
           if not isinstance(daftar_nilai, list):
               raise TypeError("Masukan data harus berupa struktur List!")
           
           total = 0
           for n in daftar_nilai:
               if not isinstance(n, (int, float)):
                   raise TypeError(f"Elemen '{n}' bukan angka valid!")
               total += n
           
           rata_rata = total / len(daftar_nilai)
       except ZeroDivisionError:
           print("[GALAT] Daftar nilai kosong, tidak dapat menghitung rata-rata.")
           return 0.0
       except TypeError as err:
           print(f"[GALAT TIPE DATA] {err}")
           return 0.0
       else:
           print(f"[SUKSES] Rata-rata berhasil dihitung: {rata_rata:.2f}")
           return rata_rata
       finally:
           print("[LOG AUDIT] Fungsi hitung_indeks_prestasi selesai dijalankan.")
   ```
3. *Perancangan Skema Tabel Laboratorium IoT:*
   - Tabel `siswa`: `nisn` (PK), `nama_siswa`, `kelas`.
   - Tabel `alat_sensor`: `id_alat` (PK), `nama_alat`, `spesifikasi`, `stok_tersedia`.
   - Tabel `peminjaman` (Junction Table): `id_pinjam` (PK), `nisn` (FK merujuk ke tabel siswa), `id_alat` (FK merujuk ke tabel alat_sensor), `tanggal_pinjam`, `status_kembali`.
   Skema ini memecah relasi Many-to-Many menjadi dua relasi One-to-Many, menjamin integritas referensial dan bebas anomali redundansi.
4. *Formulasi Prompt ROCCF Panduan Hemat Air:*
   - **Role:** Bertindaklah sebagai Insinyur Konservasi Lingkungan Hidup dan Pakar Manajemen Sanitasi Fasilitas Publik.
   - **Objective:** Buatlah draf panduan operasional standar (SOP) perilaku hemat air untuk warga sekolah.
   - **Context:** Sekolah kami memiliki 800 siswa, 50 guru, area kantin basah, dan 12 ruang toilet. Sumber air berasal dari sumur bor dengan pompa listrik.
   - **Constraint:** Batasi rekomendasi pada aksi berbiaya nol hingga sangat rendah. Dilarang menyarankan pemasangan sensor otomatis mahal. Gunakan bahasa persuasif yang mudah dipahami remaja. Panjang teks maksimal 300 kata.
   - **Format:** Sajikan luaran dalam bentuk 4 poin bernomor utama, di mana setiap poin memiliki judul tebal dan satu kalimat aksi nyata.
5. *Etika dan Mitigasi Sistem AI Deteksi Emosi:*
   a. Potensi Pelanggaran: Rekaman citra wajah merupakan data biometrik sensitif (PII). Jika pangkalan data diretas, wajah siswa dapat disalahgunakan untuk rekayasa deepfake. Pemantauan tanpa henti dapat menimbulkan kecemasan psikologis (*panopticon effect*).
   b. Bahaya Bias: Jika model hanya dilatih pada etnis tertentu, sistem akan mengalami tingkat kesalahan prediksi (*false positive*) sangat tinggi pada siswa etnis lain (misalnya salah mengidentifikasi ekspresi netral sebagai ekspresi marah atau malas).
   c. Tiga Regulasi Wajib: (1) Kewajiban persetujuan tertulis (*informed consent*) dari orang tua siswa sebelum kamera diaktifkan; (2) Data citra diproses di perangkat lokal (*edge computing*) dan langsung dihapus tanpa diunggah ke server awan; (3) Hasil deteksi emosi dilarang keras digunakan sebagai dasar pemberian sanksi atau nilai akademis rapor siswa.


# GLOSARIUM ISTILAH FASE E

- **Aspek Rasio (Aspect Ratio):** Perbandingan proporsional antara lebar dan tinggi suatu tampilan media digital (misalnya 16:9 untuk format horizontal bioskop/laptop dan 9:16 untuk format vertikal smartphone).
- **Big-O Notation:** Notasi matematika formal yang digunakan dalam ilmu komputer untuk mendeskripsikan batas atas perilaku asimptotik dan efisiensi waktu eksekusi atau konsumsi memori suatu algoritma terhadap pertumbuhan ukuran masukan (n).
- **Binary Search:** Algoritma pencarian efisien berordo O(log n) yang bekerja pada sekumpulan data terurut dengan cara membagi rentang pencarian menjadi dua bagian secara berulang hingga elemen sasaran ditemukan.
- **Bitrate:** Jumlah bit data yang diproses atau ditransmisikan dalam satuan waktu tertentu (biasanya bit per detik atau bps), menentukan kualitas dan ukuran file video atau audio.
- **Chain-of-Thought (CoT):** Teknik rekayasa prompt yang memandu model bahasa cerdas (Large Language Model) untuk menguraikan tahapan penalaran logis secara bertahap sebelum memberikan kesimpulan akhir, meningkatkan akurasi pemecahan masalah rumit.
- **Computer Vision:** Cabang ilmu kecerdasan artifisial yang memungkinkan komputer mengekstrak makna, menganalisis, dan memahami informasi visual tingkat tinggi dari gambar digital atau video.
- **Design Thinking:** Metodologi perancangan solusi inovatif yang berpusat pada empati terhadap kebutuhan manusia, melalui tahapan Empathize, Define, Ideate, Prototype, dan Test.
- **Dictionary:** Struktur data koleksi bawaan Python yang menyimpan elemen data berpasangan dalam format kunci dan nilai (*key-value pairs*), memungkinkan pencarian data instan berordo O(1).
- **Entity Relationship Diagram (ERD):** Diagram visual standar rekayasa perangkat lunak yang menggambarkan struktur basis data, entitas data, atribut, dan hubungan antarentitas menggunakan notasi Crow's Foot.
- **Exception Handling:** Mekanisme arsitektur pemrograman untuk menangkap, mengisolasi, dan merespons kesalahan atau anomali saat program dieksekusi (runtime error) sehingga aplikasi tidak mengalami penghentian paksa (*crash*).
- **Foreign Key:** Atribut atau kolom dalam sebuah tabel basis data relasional yang merujuk pada Primary Key tabel lain untuk membentuk hubungan relasi integritas referensial antarentitas.
- **Konvolusi (Convolution):** Operasi matematika pada pengolahan citra digital yang mengalikan matriks nilai piksel tetangga dengan matriks filter berukuran kecil (kernel) untuk menghasilkan fitur baru seperti deteksi tepi, penajaman, atau pengaburan gambar.
- **Linear Search:** Algoritma pencarian sekuensial paling sederhana yang memeriksa setiap elemen data satu per satu dari awal hingga akhir dengan kompleksitas waktu berordo O(n).
- **Lossless Compression:** Metode kompresi berkas digital yang mengecilkan ukuran data tanpa menghilangkan satu bit pun informasi asli, memungkinkan rekonstruksi berkas yang sempurna persis seperti aslinya.
- **Lossy Compression:** Metode kompresi berkas digital yang mengorbankan sebagian detail data yang kurang disadari oleh indra manusia untuk mencapai ukuran berkas yang jauh lebih kecil dan efisien untuk transmisi jaringan.
- **PEP 8 (Python Enhancement Proposal 8):** Panduan gaya resmi yang menetapkan konvensi standar penulisan kode sumber bahasa Python agar bersih, rapi, seragam, dan mudah dipelihara secara kolaboratif.
- **Primary Key:** Atribut unik dalam sebuah tabel basis data yang berfungsi sebagai pengidentifikasi tunggal dan pasti untuk membedakan setiap baris data tanpa kemungkinan duplikasi.
- **ROCCF Framework:** Kerangka kerja sistematis dalam rekayasa prompt tingkat lanjut yang mencakup penentuan Peran (*Role*), Tujuan (*Objective*), Konteks (*Context*), Batasan (*Constraint*), dan Format Keluaran (*Format*).
- **Spektrogram (Spectrogram):** Representasi visual dua dimensi yang memetakan spektrum frekuensi sinyal suara terhadap perubahan waktu, di mana intensitas warna menunjukkan kekuatan amplitudo gelombang suara.
- **SQL (Structured Query Language):** Bahasa pemrograman domain-khusus standar internasional yang digunakan untuk mengelola, mendefinisikan, dan memanipulasi data dalam sistem manajemen basis data relasional (RDBMS).

---

# INDEKS ISTILAH

- **A**
  - Algoritma Pengurutan, 12, 16, 21
  - Aspek Rasio, 84, 86, 91
  - Atribut Basis Data, 55, 58
- **B**
  - Big-O Notation, 13, 23, 25
  - Binary Search, 14, 15, 17
  - Bitrate, 87, 88
  - Bubble Sort, 18, 19
- **C**
  - Chain-of-Thought, 128, 130
  - Computer Vision, 103, 105, 108
  - Crow's Foot Notasi, 59, 61
- **D**
  - Data Manipulation Language (DML), 64, 66
  - Data Definition Language (DDL), 63, 65
  - Design Thinking, 132, 135
  - Dictionary Python, 37, 40
- **E**
  - Entity Relationship Diagram (ERD), 58, 60
  - Exception Handling, 42, 44
- **F**
  - Few-Shot Prompting, 126, 127
  - Foreign Key, 56, 57
- **I**
  - Insertion Sort, 20, 22
- **K**
  - Kernel Konvolusi, 106, 107
  - Kompleksitas Asimptotik, 24, 26
- **L**
  - Linear Search, 13, 15
  - List Python, 35, 36
  - Lossless vs Lossy, 89, 90
- **M**
  - Matriks RGB, 104, 105
- **P**
  - PEP 8, 46, 47
  - Primary Key, 55, 56
- **R**
  - ROCCF Framework, 124, 125
- **S**
  - Selection Sort, 19, 20
  - Spektrogram Suara, 109, 111
  - sqlite3 Python, 67, 69
- **T**
  - Try-Except, 43, 45
  - Tuple Python, 36, 37
- **U**
  - User-Centered Design, 92, 94

---

# DAFTAR PUSTAKA RESMI

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). Cambridge, MA: The MIT Press.
2. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Boston: Addison-Wesley Professional.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. Cambridge, MA: The MIT Press.
4. IEEE Computer Society. (2023). *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide V4.0)*. Los Alamitos, CA: IEEE Computer Society Press.
5. Kementerian Pendidikan Dasar dan Menengah RI. (2025). *Panduan Pembelajaran dan Asesmen Kurikulum Koding dan Kecerdasan Artifisial Jenjang SMA/SMK (Fase E)*. Jakarta: Pusat Kurikulum dan Pembelajaran, Kemendikdasmen RI.
6. McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter* (3rd ed.). Sebastopol, CA: O'Reilly Media.
7. Norman, D. (2013). *The Design of Everyday Things* (Revised and Expanded ed.). New York: Basic Books.
8. Python Software Foundation. (2024). *PEP 8 – Style Guide for Python Code*. Diakses dari https://peps.python.org/pep-0008/
9. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Hoboken, NJ: Pearson Education.
10. Szeliski, R. (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Cham, Switzerland: Springer Nature.
11. Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database System Concepts* (7th ed.). New York: McGraw-Hill Education.
12. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. Paris: United Nations Educational, Scientific and Cultural Organization.

---

# PROFIL PENULIS

[GAMBAR: assets/foto_penulis.jpg]

**Gede Erik Aktama, S.Pd., M.Pd.** adalah seorang akademisi, peneliti, dan praktisi pendidikan di bidang sains komputer dan kecerdasan artifisial berkebangsaan Indonesia. Beliau menyelesaikan pendidikan Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Teknik Informatika di Universitas Pendidikan Ganesha (UNDIKSHA) Singaraja, Bali, dan menuntaskan gelar Magister Pendidikan (M.Pd.) dengan fokus konsentrasi pada penelitian teknologi pembelajaran dan rekayasa media digital interaktif.

Saat ini, beliau mengemban amanah sebagai dosen tetap dengan jabatan fungsional akademik **Lektor** (berdasarkan Keputusan Menteri Pendidikan Tinggi, Sains, dan Teknologi Republik Indonesia Nomor: 0044/LL16/KP.07/2025) sekaligus menjabat sebagai **Ketua Program Studi S1 Sistem Komputer** di Fakultas Sains dan Teknologi, Universitas Parna Raya (UNIPAR) Manado, Sulawesi Utara.

Di tingkat nasional, Gede Erik Aktama aktif berperan sebagai **Fasilitator Nasional Bimbingan Teknis dan Training of Trainers (ToT) Kurikulum Koding dan Kecerdasan Artifisial (KKA)** yang diselenggarakan oleh Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) Republik Indonesia. Dalam kiprahnya, beliau telah melatih ribuan guru informatika dan praktisi komputasi di berbagai pelosok nusantara guna mempersiapkan fondasi talenta digital Indonesia menuju era kedaulatan sains dan teknologi masa depan.

Bidang riset dan kepakaran beliau berfokus pada arsitektur pembelajaran mendalam (*Deep Learning*), rekayasa sistem berbasis kecerdasan artifisial, etika sistem cerdas, dan pengembangan kurikulum vokasi berbasis komputasi modern. Beliau dapat dihubungi melalui surel akademik di: *erik.aktama@parnaraya.ac.id*.
