# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 1 Buku Siswa KKA Kelas 8 SMP (Fase D)
BAB I: LOGIKA PEMROGRAMAN TINGKAT LANJUT & STRUKTUR BERSARANG (18 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_1_SMP8 = """# BAB I LOGIKA PEMROGRAMAN TINGKAT LANJUT & STRUKTUR BERSARANG

## MISI 1: ARSITEK LOGIKA MODULAR & CLEAN CODE
* **Alokasi Waktu:** 18 Jam Pelajaran (9 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK)
* **Target Lencana Koder:** Medali Emas Arsitek Logika Modular (Fase D)

---

## A. PENDAHULUAN: MISTERI SIMULATOR PEMADAM KEBAKARAN HUTAN

Ruang laboratorium komputer SMP Nusantara tampak hening. Layar monitor di hadapan Rian menampilkan puluhan blok kode warna-warni yang saling bertumpuk panjang ke bawah. Di sudut meja, Ayu dan Fajar memperhatikan simulasi helikopter penyelamat yang bergerak tersendat-sendat di atas kanvas peta hutan yang dipenuhi titik-titik api merah menyala.

"Ada yang tidak beres dengan logikanya," keluh Rian sambil memijat keningnya. "Helikopter penyelamat ini seharusnya hanya boleh menyemprotkan air jika tangki air terisi penuh DAN posisi helikopter tepat berada di atas koordinat titik api. Tapi kenyataannya, helikopter malah menyiram air di mana saja, bahkan saat tangkinya kosong melompong!"

[[IMAGE: bab1_komik_pembuka_smp8.png | Gambar 1.1: Komik Pembuka Bab 1: Tantangan Simulasi Pemadam Kebakaran Hutan]]

Fajar mengamati deretan blok pengkondisian yang ditulis Rian. "Lihat di sini, Rian. Kamu membuat blok `jika (menyentuh titik api)` dan di dalamnya kamu menumpuk lima belas blok perintah gerak, suara, dan skor sekaligus. Ketika kita ingin menambahkan kondisi kedua—misalnya helikopter harus memeriksa apakah arah angin bertiup kencang—kodenya menjadi bertumpuk rumit seperti mie instan yang kusut (*spaghetti code*)!"

"Fajar benar," sahut Ayu tersenyum sambil membuka buku catatannya. "Di kelas VII kemarin kita sudah belajar algoritma dasar. Di kelas VIII ini, proyek simulasi kita jauh lebih realistis. Kita tidak bisa lagi hanya mengandalkan logika satu kondisi. Kita harus menggunakan **Operator Logika Majemuk (AND, OR, NOT)**, menyusun **Percabangan Bersarang (*Nested If*)**, dan membungkus instruksi berulang ke dalam **Fungsi Mandiri (*Custom Blocks*)**. Dengan begitu, kode kita menjadi bersih, rapi, dan mudah diperbaiki!"

Mata Rian kembali berbinar. "Tantangan diterima! Mari kita bedah bagaimana programmer profesional merancang logika berlapis agar simulator kebakaran hutan kita bekerja sempurna!"

---

## B. OPERATOR LOGIKA MAJEMUK: AND, OR, DAN NOT

Dalam kehidupan sehari-hari, keputusan yang kita ambil jarang sekali hanya bergantung pada satu syarat tunggal. Perhatikan contoh berikut:
* "Kalian boleh mengikuti ujian praktik komputer JIKA membawa kartu peserta **DAN** hadir tepat waktu." (Kedua syarat wajib dipenuhi).
* "Kalian bisa membuka pintu laboratorium JIKA memiliki kunci fisik **ATAU** memindai kartu akses digital." (Cukup salah satu syarat terpenuhi).
* "Alarm keamanan akan berbunyi JIKA pintu terbuka dan sistem pengaman **TIDAK** dalam status nonaktif." (Membalik kondisi status pengaman).

Dalam sains komputasi, penyatuan beberapa syarat pengkondisian dilakukan menggunakan **Operator Logika Boolean**. Terdapat tiga operator logika utama yang wajib dikuasai oleh seorang programmer:

[[IMAGE: bab1_diagram_logika_saklar_and_or.png | Gambar 1.2: Diagram Logika Saklar Listrik: Perbedaan Kondisi AND (Seri), OR (Paralel), dan NOT (Inverter)]]

### 1. Operator Logika AND (Konjungsi / Hubungan Seri)
Operator **AND** menghasilkan nilai `BENAR (TRUE)` hanya jika **SELURUH** kondisi yang digabungkan bernilai benar. Jika ada satu saja kondisi yang salah, maka hasil akhir pengkondisian otomatis bernilai `SALAH (FALSE)`.
Analogi fisika yang paling mudah dipahami adalah **rangkaian saklar listrik seri**. Arus listrik dari baterai hanya akan mengalir menyalakan lampu jika Saklar A ditutup (ON) **DAN** Saklar B ditutup (ON). Jika salah satu saklar terbuka (OFF), arus terputus dan lampu tetap padam.

Tabel Kebenaran Logika AND:
| Kondisi A | Kondisi B | Hasil (A AND B) |
| :---: | :---: | :---: |
| BENAR (True) | BENAR (True) | **BENAR (True)** |
| BENAR (True) | SALAH (False) | **SALAH (False)** |
| SALAH (False) | BENAR (True) | **SALAH (False)** |
| SALAH (False) | SALAH (False) | **SALAH (False)** |

Dalam Scratch, operator ini diwakili oleh blok hijau `( ... dan ... )`. Dalam bahasa Python, digunakan kata kunci `and`. Contoh penerapannya pada simulator pemadam kebakaran:
```python
if posisi_menyentuh_api and volume_air > 0:
    semprotkan_air()
    kurangi_volume_air(10)
```

### 2. Operator Logika OR (Disjungsi / Hubungan Paralel)
Operator **OR** menghasilkan nilai `BENAR (TRUE)` jika **SALAH SATU** atau **KEDUA** kondisi bernilai benar. Hasil baru bernilai `SALAH (FALSE)` hanya jika seluruh kondisi bernilai salah.
Analogi fisika untuk operator OR adalah **rangkaian saklar listrik paralel**. Arus listrik memiliki dua jalur alternatif untuk mencapai lampu. Jika Saklar A dinyalakan (meskipun Saklar B mati), arus tetap mengalir lewat jalur atas sehingga lampu menyala.

Tabel Kebenaran Logika OR:
| Kondisi A | Kondisi B | Hasil (A OR B) |
| :---: | :---: | :---: |
| BENAR (True) | BENAR (True) | **BENAR (True)** |
| BENAR (True) | SALAH (False) | **BENAR (True)** |
| SALAH (False) | BENAR (True) | **BENAR (True)** |
| SALAH (False) | SALAH (False) | **SALAH (False)** |

Contoh penerapan pada game mitigasi bencana: Helikopter penyelamat harus segera mendarat darurat jika tangki bahan bakar habis **ATAU** baling-baling mengalami kerusakan mesin:
```python
if bahan_bakar == 0 or status_baling_baling == "RUSAK":
    lakukan_pendaratan_darurat()
```

### 3. Operator Logika NOT (Negasi / Pembalik Nilai)
Operator **NOT** berfungsi membalik nilai kebenaran suatu kondisi. Jika kondisi bernilai `BENAR`, operator NOT akan mengubahnya menjadi `SALAH`, dan sebaliknya.
Operator NOT sangat berguna untuk mengevaluasi kondisi kebalikan, seperti memeriksa apakah tombol keyboard sedang *tidak* ditekan, atau mendeteksi sensor yang mendadak tidak merespons:
```python
if not sensor_terhubung:
    tampilkan_peringatan_koneksi_putus()
```

---

## C. STRUKTUR PERCABANGAN BERSARANG (NESTED IF-ELSE)

Dalam skenario pemecahan masalah yang lebih kompleks, keputusan sering kali harus diambil secara bertahap atau berlapis. Hasil dari keputusan pertama akan menentukan pertanyaan pengkondisian berikutnya yang harus dijawab. Struktur ini dikenal dengan istilah **Percabangan Bersarang (*Nested If-Else*)**.

[[IMAGE: bab1_struktur_percabangan_nested_if.png | Gambar 1.3: Diagram Alur Keputusan Berlapis (Nested If-Else) dalam Algoritma]]

### Membedah Logika Berlapis
Bayangkan algoritma keputusan helikopter patroli hutan dalam merespons laporan asap:
1. **Tingkat 1 (Kondisi Luar):** Sistem memeriksa apakah sensor mendeteksi asap tebal di koordinat hutan?
   * Jika **TIDAK**: Helikopter melanjutkan rute patroli rutin keliling hutan.
   * Jika **YA**: Jangan langsung menyiram air! Masuki evaluasi tingkat kedua.
2. **Tingkat 2 (Kondisi Bersarang / Dalam):** Sistem memeriksa apakah ada pemukiman warga di sekitar koordinat asap tersebut?
   * Jika **YA**: Prioritaskan evakuasi warga terlebih dahulu dan kirim sinyal sirine bahaya!
   * Jika **TIDAK**: Segera luncurkan bom air (*water bombing*) untuk memadamkan api sebelum merembet luas!

Mari kita telaah bentuk kode perbandingan logika bertingkat ini dalam bahasa visual dan tekstual:
```python
# Contoh Implementasi Percabangan Bersarang
if sensor_deteksi_asap == True:
    print("Peringatan: Asap pekat terdeteksi!")
    # Percabangan bersarang di dalam blok IF pertama
    if jarak_ke_pemukiman < 500:
        bunyikan_sirine_evakuasi()
        panggil_tim_penyelamat_darat()
    else:
        luncurkan_bom_air()
else:
    lanjutkan_patroli_rutin()
```

> **Wawasan Koder: Waspadai Jebakan Kedalaman Sarang (*Nesting Depth*)**  
> Hindari membuat percabangan bersarang lebih dari 3 tingkat ke dalam (misal: IF di dalam IF, di dalam IF, di dalam IF lagi). Struktur sarang yang terlalu dalam membuat kode sulit dibaca, memicu kesalahan logika tersembunyi (*logic bugs*), dan sangat menyulitkan rekan tim saat melakukan penelusuran kesalahan (*debugging*). Solusinya: gabungkan kondisi menggunakan operator AND/OR atau pisahkan menjadi fungsi modular!

---

## D. PERULANGAN BERSYARAT (WHILE / REPEAT-UNTIL) & VARIABEL COUNTER

Di kelas sebelumnya, kalian terbiasa menggunakan blok perulangan dengan jumlah putaran yang pasti (misalnya `ulangi 10 kali`). Namun, dalam simulasi dunia nyata dan game interaktif, kita jarang mengetahui secara pasti berapa kali suatu aksi harus diulang. 

### Perulangan Bersyarat: Berhenti Saat Syarat Terpenuhi
Helikopter pemadam kebakaran tidak boleh menyiram air sebanyak angka tetap 10 kali; helikopter harus terus menyemprotkan air **selama** titik api masih menyala **DAN** volume air di tangki masih tersedia. Jenis perulangan ini disebut **Perulangan Bersyarat (*Conditional Loop / While Loop*)**.

Perbedaan mendasar dua jenis perulangan:
1. **Perulangan Terhitung (*Counted Loop / For*):** Jumlah putaran telah ditentukan di awal. Contoh: Menembakkan 5 suar sinyal darurat ke udara.
2. **Perulangan Bersyarat (*Conditional Loop / While / Repeat-Until*):** Perulangan terus berjalan berulang-ulang sampai sebuah kondisi tertentu bernilai benar atau salah. Contoh: Mengisi tangki air helikopter di danau sampai sensor tangki menunjukkan status `PENUH`.

### Peran Variabel Counter dan Accumulator
Untuk mengendalikan jalannya perulangan dan mencatat kemajuan simulasi, programmer memanfaatkan dua jenis variabel:
* **Counter (Pencacah):** Variabel yang nilainya bertambah secara konstan (biasanya bertambah 1) setiap kali perulangan terjadi. Contoh: Menghitung berapa kali helikopter bolak-balik mengambil air ke danau.
* **Accumulator (Penampung):** Variabel yang menampung akumulasi nilai yang berubah-ubah. Contoh: Menghitung total liter air yang telah disiramkan ke hutan sepanjang operasi penanganan bencana.

---

## E. MODULARISASI PROGRAM: MEMBUAT CUSTOM BLOCKS BERPARAMETER

Ketika program komputer berkembang semakin besar, menuliskan ratusan blok kode secara memanjang ke bawah adalah kebiasaan buruk. Jika ada algoritma yang harus dipanggil di beberapa tempat berbeda—seperti animasi ledakan api, suara sirine, atau perhitungan pengurangan skor—kalian tidak boleh menyalin-tempel (*copy-paste*) blok tersebut berulang-ulang!

[[IMAGE: bab1_arsitektur_modular_custom_block.png | Gambar 1.4: Arsitektur Pemrograman Modular: Perbandingan Kode Spaghetti vs Custom Blocks Berparameter]]

### Mengapa Kita Membutuhkan Fungsi Modular?
Konsep **Modularisasi** adalah teknik memecah program besar yang rumit menjadi bagian-bagian kecil mandiri yang disebut **Fungsi (*Functions / Custom Blocks / Subroutines*)**.

Keuntungan utama pemrograman modular:
1. **Kode Bersih (*Clean Code*):** Program utama menjadi sangat ringkas dan mudah dipahami alur ceritanya hanya dalam sekali baca.
2. **Bisa Digunakan Kembali (*Reusability*):** Fungsi yang sudah dibuat dapat dipanggil puluhan kali dari berbagai sprite tanpa perlu menulis ulang instruksinya.
3. **Kemudahan Debugging:** Jika terjadi kesalahan pada animasi helikopter, kalian hanya perlu memperbaiki satu blok fungsi terkait, dan seluruh bagian program otomatis ikut terperbaiki.

### Merancang Blok Mandiri dengan Parameter Dinamis
Kehebatan fungsi mandiri bertambah berlipat ganda ketika kita menambahkan **Parameter Masukan (*Arguments*)**. Parameter adalah wadah nilai dinamis yang kita kirimkan ke dalam fungsi saat fungsi tersebut dipanggil.

Perhatikan perancangan blok custom pada Scratch dan Python berikut:
* **Nama Blok:** `PadamkanApi`
* **Parameter Masukan 1:** `Koordinat_X` (Menentukan posisi titik api yang dituju)
* **Parameter Masukan 2:** `Koordinat_Y`
* **Parameter Masukan 3:** `Kekuatan_Air` (Menentukan seberapa deras semprotan air yang dikeluarkan)

```python
# Mendefinisikan Fungsi Modular dengan Parameter
def padamkan_api(target_x, target_y, kekuatan_air):
    terbangkan_helikopter(target_x, target_y)
    buka_katup_tangki(kekuatan_air)
    mainkan_suara_semprotan()
    kurangi_intensitas_api(kekuatan_air * 2)

# Memanggil Fungsi dengan Argumen Berbeda
padamkan_api(120, -50, 80)   # Padamkan api di sektor timur dengan kekuatan 80
padamkan_api(-90, 110, 40)   # Padamkan api di sektor barat dengan kekuatan 40
```

---

## F. LKPD PLUGGED 1.1: MEMBANGUN GAME SIMULASI PEMADAM KEBAKARAN HUTAN

### Aktivitas Praktik Mandiri dan Kolaboratif (Plugged Activity)
* **Alat & Bahan:** Komputer / Laptop dengan peramban web dan aplikasi Scratch 3.0 (daring/luring).
* **Durasi Pengerjaan:** 4 JP (2 Pertemuan Praktik Terbimbing).
* **Peran Tim:** Berpasangan (*Pair Programming*) — 1 Siswa sebagai *Driver* (mengetik dan menyusun blok), 1 Siswa sebagai *Navigator* (membaca rancangan algoritma dan mengecek bug).

### Langkah-Langkah Pembuatan Game Simulasi:
1. **Persiapan Sprite dan Latar:**
   * Latar panggung: Peta Hutan Tropis Nusantara dengan area hijau, danau penampung air di kiri bawah, dan menara pantau di kanan atas.
   * Sprite 1: Helikopter Penyelamat (memiliki kostum baling-baling berputar dan kostum semprot air).
   * Sprite 2: Titik Api (memiliki variabel lokal `IntensitasApi`).
   * Buat variabel global: `VolumeAir`, `SkorPenyelamatan`, dan `WaktuOperasi`.

2. **Memprogram Mekanisme Helikopter Mengambil Air di Danau:**
   * Helikopter dikendalikan menggunakan tombol panah keyboard.
   * Gunakan percabangan bersarang:
     ```scratch
     jika <menyentuh [Danau v] ?> maka
         jika <(VolumeAir) < [100]> maka
             ubah [VolumeAir v] sebesar (5)
             tunggu (0.1) detik
         akhir
     akhir
     ```

3. **Membuat Custom Block Modular `SemprotkanAir (Dosis)`:**
   * Buka kategori blok **My Blocks** -> Klik **Make a Block**.
   * Beri nama `SemprotkanAir` dan tambahkan input angka bernama `Dosis`.
   * Di bawah blok definisi `define SemprotkanAir (Dosis)`:
     * Periksa apakah `VolumeAir >= Dosis` DAN `menyentuh [TitikApi v]`.
     * Jika kedua syarat terpenuhi: kurangi `VolumeAir` sebesar `Dosis`, mainkan suara deburan air, dan kirim pesan siaran (*broadcast*) `KenaAir`.

4. **Pengujian dan Evaluasi Program:**
   * Uji coba jalankan simulasi dengan menekan bendera hijau.
   * Catat pada tabel pengujian: Apakah helikopter bisa menyemprot saat air di tangki 0? (Seharusnya tidak bisa). Apakah api padam jika disemprot berkali-kali?

---

## POJOK KARAKTER & ETIKA KODER: BUDAYA GOTONG ROYONG MELALUI CLEAN CODE

Dalam industri perangkat lunak modern, sebuah aplikasi komputer tidak pernah dibuat oleh satu orang saja. Ribuan insinyur perangkat lunak bekerja sama merawat jutaan baris kode secara bersamaan. Jika setiap programmer menulis kode sesuka hatinya tanpa aturan, sistem akan kacau balau dan mudah runtuh!

Menulis program yang bersih (*clean code*)—dengan memberi nama variabel yang jelas (misal `JumlahKorban` alih-alih `x1`), menata inden yang rapi, dan memecah kode menjadi blok fungsi modular—merupakan cerminan nyata dari nilai luhur **Gotong Royong** dan **Tanggung Jawab**. Dengan menulis kode yang rapi, kalian sedang menghargai waktu dan tenaga sahabat kalian yang akan membaca dan menyempurnakan program tersebut di masa depan. Koder sejati bukan hanya koder yang programnya jalan, tetapi koder yang karyanya membahagiakan orang lain yang membacanya!

---

## RANGKUMAN MATERI BAB 1

1. **Operator Logika Majemuk** menggabungkan dua atau lebih kondisi Boolean:
   * **AND:** Bernilai Benar hanya jika SEMUA kondisi terpenuhi (analogi saklar seri).
   * **OR:** Bernilai Benar jika SALAH SATU atau KEDUA kondisi terpenuhi (analogi saklar paralel).
   * **NOT:** Membalik nilai kebenaran suatu kondisi dari Benar menjadi Salah, atau sebaliknya.
2. **Percabangan Bersarang (*Nested If-Else*)** adalah penempatan blok pengkondisian di dalam blok pengkondisian lain untuk memecahkan keputusan bertingkat yang realistis di dunia nyata.
3. **Perulangan Bersyarat (*While / Repeat-Until*)** mengeksekusi instruksi berulang-ulang sampai kondisi penghenti terpenuhi, dikendalikan oleh variabel *counter* dan *accumulator*.
4. **Modularisasi Kode (*Custom Blocks*)** mengelompokkan baris instruksi berulang menjadi fungsi mandiri berparameter dinamis, mewujudkan prinsip *Clean Code* yang efisien, mudah dirawat, dan hemat memori.

---

## UJI PEMAHAMAN HOTS BAB 1

### I. Pilihan Ganda (Pilihlah Jawaban yang Paling Tepat!)

1. Perhatikan potongan kode berikut:
   `Kondisi = (Nilai_Matematika >= 80) and (Kehadiran >= 90)`
   Jika seorang siswa memperoleh Nilai Matematika 85 namun persentase Kehadirannya hanya 88%, maka nilai dari variabel `Kondisi` adalah...
   A. True  
   B. False  
   C. Error  
   D. Null  

2. Analogi rangkaian listrik yang paling tepat untuk menggambarkan cara kerja operator logika OR dalam komputasi adalah...
   A. Dua saklar dipasang berurutan pada satu kabel lurus (seri)  
   B. Dua saklar dipasang pada dua cabang kabel terpisah menuju satu lampu (paralel)  
   C. Satu saklar otomatis yang mematikan listrik saat terjadi korsleting  
   D. Saklar pemutar putaran kipas angin  

3. Diberikan variabel Boolean: `P = True`, `Q = False`, dan `R = True`. Berapakah hasil evaluasi dari ekspresi: `(P and Q) or (not Q and R)`?
   A. False  
   B. True  
   C. None  
   D. Tidak dapat ditentukan  

4. Mengapa programmer profesional sangat menghindari struktur *Nested If* yang bersarang lebih dari tiga tingkat ke dalam?
   A. Karena komputer tidak mampu mengeksekusi lebih dari tiga kondisi bersarang  
   B. Karena ukuran file program akan membengkak hingga puluhan gigabyte  
   C. Karena kode menjadi sangat rumit dibaca dan menyulitkan proses penelusuran bug (*spaghetti code*)  
   D. Karena bahasa pemrograman modern melarang penggunaan kata kunci IF berulang  

5. Perhatikan skenario game simulasi: Sebuah kapal penyelamat hanya boleh menembakkan jaring jika menyentuh perahu korban, kecepatan kapal di bawah 10 knot, DAN kapasitas penumpang di dek belum penuh. Struktur logika yang tepat adalah...
   A. `if menyentuh_korban or kecepatan < 10 or kapasitas_belum_penuh:`  
   B. `if menyentuh_korban and (kecepatan < 10 or not kapasitas_belum_penuh):`  
   C. `if menyentuh_korban and kecepatan < 10 and kapasitas_belum_penuh:`  
   D. `if not menyentuh_korban and kecepatan < 10 and kapasitas_belum_penuh:`  

6. Perbedaan mendasar antara perulangan `Repeat 10` dengan `Repeat Until (Nyawa == 0)` terletak pada...
   A. Warna blok yang digunakan pada palet pemrograman Scratch  
   B. Kecepatan eksekusi instruksi di dalam prosesor komputer  
   C. Kepastian jumlah putaran di awal eksekusi program  
   D. Tipe data variabel yang digunakan dalam perhitungan matematika  

7. Sebuah blok custom dibuat dengan definisi: `define LompatKarakter (Ketinggian, Durasi)`. Nilai angka 50 dan 0.5 yang dimasukkan saat blok tersebut dipanggil disebut sebagai...
   A. Algoritma  
   B. Variabel Global  
   C. Parameter / Argumen  
   D. Konstanta Tetap  

8. Rian menemukan bahwa game buatannya mengalami lag berat karena ia menyalin-tempel 20 baris blok kode animasi yang sama sebanyak 12 kali pada 12 sprite musuh berbeda. Prinsip perbaikan terbaik yang harus dilakukan Rian adalah...
   A. Menghapus 11 sprite musuh agar game berjalan cepat  
   B. Mengubah seluruh sprite musuh menjadi bentuk lingkaran sederhana  
   C. Melakukan modularisasi kode dengan membungkus animasi ke dalam Custom Block yang dapat dipanggil bersama  
   D. Mengganti latar belakang panggung menjadi warna hitam polos  

9. Perhatikan potongan kode percabangan bersarang berikut:
   ```
   jika <Hari = "Minggu"> maka
       jika <Cuaca = "Cerah"> maka
           Katakan "Piknik ke Pantai"
       jika tidak
           Katakan "Nonton Film di Rumah"
       akhir
   jika tidak
       Katakan "Belajar di Sekolah"
   akhir
   ```
   Jika variabel `Hari` bernilai "Sabtu" dan `Cuaca` bernilai "Cerah", teks apa yang akan diucapkan oleh karakter?
   A. Piknik ke Pantai  
   B. Nonton Film di Rumah  
   C. Belajar di Sekolah  
   D. Tidak mengatakan apa pun  

10. Praktik memberi nama fungsi mandiri dengan kata kerja yang deskriptif—seperti `HitungLuasSegitiga()` alih-alih `Fungsi_1()`—merupakan penerapan prinsip...
    A. Closed Source  
    B. Clean Code  
    C. Machine Learning  
    D. Data Mining  

---

### II. Uraian Pemecahan Masalah (Jawablah Secara Rinci dan Terstruktur!)

1. Jelaskan perbedaan prinsip kerja antara operator logika AND dan operator logika OR! Sertakan masing-masing satu contoh kasus nyata penerapannya dalam sebuah game edukasi!
2. Mengapa teknik modularisasi kode menggunakan *Custom Blocks* dianggap sangat penting dalam pengembangan perangkat lunak berskala besar? Sebutkan tiga keuntungan konkret yang diperoleh programmer!
3. Diberikan kasus penerimaan beasiswa prestasi di SMP Nusantara dengan kriteria berlapis:
   * Calon penerima beasiswa WAJIB memiliki rata-rata nilai rapor minimal 85.
   * JIKA rata-rata nilai terpenuhi, calon penerima harus memenuhi SALAH SATU syarat tambahan: Memenangkan kejuaraan sains tingkat kota ATAU memiliki persentase kehadiran 100%.
   Tuliskan rancangan algoritma keputusan beasiswa tersebut menggunakan struktur *Nested If* dan operator logika yang tepat!
4. Jelaskan apa yang dimaksud dengan variabel *Counter* dan variabel *Accumulator* dalam sebuah blok perulangan bersyarat (*Conditional Loop*)! Berikan contoh penggunaannya pada game simulator pemadam kebakaran hutan!
5. Bagaimana penerapan prinsip *Clean Code* dalam penulisan program dapat menjadi wujud nyata pengamalan nilai gotong royong dan etika profesional antar sesama pembuat kode?

---

## KUNCI JAWABAN UJI PEMAHAMAN TERPILIH BAB 1

### Kunci Jawaban Pilihan Ganda:
1. **B** (Pada operator AND, kedua syarat wajib bernilai benar; karena kehadiran 88% < 90%, hasil akhir otomatis False).
2. **B** (Rangkaian saklar paralel memungkinkan arus listrik mengalir jika salah satu saklar tertutup/ON).
3. **B** (Evaluasi: `P and Q` -> `True and False` = `False`. `not Q and R` -> `True and True` = `True`. `False or True` = `True`).
4. **C** (Struktur sarang bertingkat yang terlalu dalam menciptakan *spaghetti code* yang sangat membingungkan alur bacanya).
5. **C** (Semua kriteria harus dipenuhi bersamaan menggunakan operator AND).
6. **C** (Perulangan terhitung memiliki batasan angka pasti, sedangkan perulangan bersyarat bergantung pada kondisi dinamis saat program berjalan).
7. **C** (Nilai konkret yang disuplai saat memanggil fungsi disebut argumen/parameter masukan).
8. **C** (Modularisasi kode mengeliminasi duplikasi kode yang memboroskan memori dan memicu penurunan performa).
9. **C** (Karena kondisi luar `Hari = "Minggu"` bernilai salah/Sabtu, eksekusi langsung melompat ke blok `jika tidak` terluar, yaitu "Belajar di Sekolah").
10. **B** (Penamaan fungsi dan variabel yang jelas dan ekspresif adalah pilar utama budaya *Clean Code*).
"""
