# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 1 Buku Siswa KKA Kelas 6 SD (Fase C)
BAB I: LOGIKA BERSYARAT, PERULANGAN, & PEMBUATAN GAME KUIS EDUKASI (16 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_1_SD6 = """# BAB I LOGIKA BERSYARAT, PERULANGAN, & PEMBUATAN GAME KUIS EDUKASI

## MISI 1: ARSITEK LOGIKA GAME CERDAS
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK)
* **Target Lencana Koder:** Medali Arsitek Logika Game Cerdas (Bintang Emas Fase C)

---

## A. PENDAHULUAN: MISTERI SKOR YANG MACET DI GAME KUIS

Siang itu, ruang laboratorium komputer SD Nusantara terasa sangat ramai dan penuh tawa. Erik dan Made sedang asyik merancang sebuah game kuis cerdas cermat sains antariksa di depan komputer. Di layar, karakter astronot cilik siap menjawab pertanyaan tentang nama planet terbesar di tata surya kita.

"Erik, coba klik pilihan jawaban Yupiter!" seru Made penasaran sambil menunjuk layar monitor.

Erik mengklik tombol Yupiter. Seketika suara tepuk tangan meriah terdengar dari speaker komputer. Namun, Made mengernyitkan dahinya.

"Tunggu dulu, Erik! Suara tepuk tangannya memang berbunyi, tapi kenapa angka skor di pojok atas layar masih tetap nol? Angkanya tidak mau bertambah!" keluh Made heran.

Erik mencoba mengklik pilihan lain yang sengaja salah, yaitu planet Merkurius. Keanehan makin menjadi-jadi: suara tepuk tangan tetap berbunyi, dan astronot di layar tetap berkata *"Hebat, kamu pintar!"*.

"Wah, kacau! Komputer kita sepertinya bingung," ujar Erik sambil menggaruk-garuk kepalanya. "Mau jawabannya benar atau salah, komputernya memberikan respon yang persis sama. Bagaimana caranya agar komputer tahu kapan harus menambah nilai dan kapan harus memberi peringatan salah?"

Siti yang duduk di samping mereka menoleh sambil tersenyum. "Itu karena program buatan kalian belum memiliki logika percabangan! Komputer itu seperti robot pelayan yang patuh: kalau kalian tidak memberi aturan dua jalan, komputer akan menjalankan semua perintah secara lurus tanpa berpikir!"

Tiba-tiba, suara dengung ceria berbunyi dari atas meja: *"Tii-tut! Bip-bip!"*  
Keluarlah **Robot Kibo**, sahabat asisten cerdas kita yang berwajah bulat biru. Lampu indikator di kepalanya berkedip gembira.

[[IMAGE: bab1_komik_pembuka_sd6.png | Gambar 1.1: Komik Sahabat Koder — Tantangan Membuat Game Kuis Cerdas Cermat]]

"Halo para arsitek game hebat!" sapa Robot Kibo ramah. "Di kelas 6 ini, kalian akan naik tingkat menjadi programmer sejati! Komputer membutuhkan mantra sakti yang disebut **PERCABANGAN KONDISIONAL (*If-Then-Else*)**, perulangan tanpa lelah **(*Loops*)**, dan kotak ajaib pencatat angka yang dinamakan **VARIABEL**! Dengan ketiga jurus ini, game buatanmu akan secerdas kuis televisi profesional!"

"Wah, asyik sekali! Kibo, ajari kami cara menyusun mantranya sekarang!" pinta Erik dan Made bersemangat.

> **Pertanyaan Pemantik Arsitek Cilik:**
> 1. Dalam kehidupan sehari-hari, bagaimana caramu mengambil keputusan jika langit pagi hari tampak mendung gelap gulita?
> 2. Mengapa sebuah game kuis terasa membosankan jika kita selalu menang meskipun menjawab salah?
> 3. Bagaimana komputer bisa mengingat nama pemain dan mencatat skor tertinggi yang pernah kita raih? Yuk, kita bedah rahasianya bersama!

---

## B. KONSEP DAN MATERI PEMBELAJARAN

### 1. Pengambilan Keputusan: Logika "Jika ... Maka ..." (*If-Then*)

Dalam kehidupan nyata, manusia selalu membuat keputusan berdasarkan kondisi tertentu. Coba perhatikan contoh sederhana ini:
* **Jika** bel sekolah berbunyi kencang pukul 07.00, **maka** seluruh murid berbaris rapi di lapangan upacara.
* **Jika** lampu lalu lintas menyala merah, **maka** pengendara kendaraan bermotor harus berhenti.

Di dunia pemrograman komputer, pola pikir tersebut disebut **LOGIKA PERCABANGAN (*Conditional Logic*)** atau pernyataan **IF - THEN**. Komputer akan memeriksa apakah sebuah kondisi bernilai **BENAR (*True*)** atau **SALAH (*False*)**.

Apabila kondisi terpenuhi (BENAR), maka komputer akan menjalankan perintah khusus yang kita tentukan. Namun, jika kondisi tidak terpenuhi (SALAH), komputer akan langsung melompati perintah tersebut dan melanjutkan ke baris berikutnya.

---

### 2. Mengatur Dua Kemungkinan: "Jika ... Maka ... Jika Tidak ..." (*If-Then-Else*)

Bagaimana jika kita menghadapi situasi dengan dua kemungkinan hasil yang berbeda? Misalnya:
* **Jika** nilai ulangan Erik mencapai 75 atau lebih, **maka** Erik dinyatakan lulus kuis.
* **Jika tidak (*Else*)**, **maka** Erik harus belajar kembali dan mengikuti remedial.

Inilah struktur **IF - THEN - ELSE**. Struktur ini adalah fondasi utama kecerdasan buatan dan game modern.

[[IMAGE: bab1_flowchart_percabangan.png | Gambar 1.2: Diagram Alur Logika Percabangan (If - Then - Else)]]

Mari kita amati alur flowchart pada Gambar 1.2 di atas:
1. Komputer menampilkan pertanyaan: *"Ibu kota negara Indonesia adalah...?"*
2. Pemain mengetikkan jawaban.
3. Kotak keputusan berbentuk belah ketupat memeriksa kondisi: **Apakah jawaban = "Nusantara"?**
   * **Cabang YA (Benar):** Komputer memutar suara kemenangan *"Cheer!"*, menampilkan pesan *"Luar Biasa, Jawaban Tepat!"*, dan menambah Skor sebesar 10 poin.
   * **Cabang TIDAK (Salah):** Komputer membunyikan efek suara *"Oops!"*, menampilkan pesan *"Jawaban belum tepat, yuk coba lagi!"*, dan mengurangi sisa Nyawa sebanyak 1 kesempatan.
4. Kedua cabang kembali bertemu di titik akhir untuk melanjutkan ke pertanyaan kuis berikutnya.

> 🔍 **Tahukah Kamu?**
> Komputer pesawat luar angkasa NASA menggunakan jutaan baris logika percabangan *If-Then-Else* setiap detik! Komputer memeriksa: *Jika suhu roket melebihi 1.000 derajat Celsius, maka semprotkan pendingin hidrogen cair secara otomatis!* Jika tidak ada logika percabangan, roket tidak akan mampu menjelajahi antariksa dengan aman!

---

### 3. Perulangan Efisien (*Loops*): Menjalankan Instruksi Tanpa Lelah

Bayangkan jika gurumu meminta kamu menulis kalimat *"Saya berjanji akan rajin belajar koding"* sebanyak 100 kali di buku tulis. Tanganmu pasti akan terasa pegal dan melelahkan, bukan?

Namun, komputer tidak pernah merasa lelah, lapar, ataupun bosan! Komputer memiliki jurus sakti bernama **PERULANGAN (*Looping*)**. Kita cukup menuliskan perintahnya satu kali, lalu memberi instruksi berapa kali perintah itu harus diulang.

Pada aplikasi pemrograman visual Scratch 3.0, terdapat dua jenis blok perulangan utama:
1. **Perulangan Terhitung (`repeat [angka]`):**  
   Perulangan ini digunakan jika kita sudah tahu pasti berapa kali perintah harus berjalan. Contohnya: `repeat (5)` digunakan untuk mengulang 5 pertanyaan kuis berturut-turut.
2. **Perulangan Selamanya (`forever`):**  
   Perulangan ini akan terus berjalan tanpa henti selama tombol bendera hijau ditekan atau hingga game ditutup. Blok ini sangat cocok untuk:
   * Menggerakkan awan latar belakang agar bergerak terus dari kanan ke kiri layar.
   * Memeriksa sepanjang waktu apakah karakter astronot menabrak meteor.

---

### 4. Variabel: Kotak Ajaib Penyimpan Nilai dalam Game

Pernahkah kamu melihat ibu menaruh toples-toples kaca di dapur bertuliskan label: *"Gula"*, *"Kopi"*, *"Tepung"*, dan *"Garam"*? Isi di dalam toples itu bisa berubah: kadang penuh, kadang berkurang saat dipakai membuat kue, atau ditambah lagi saat berbelanja.

Di dalam komputer, konsep toples kaca tersebut dinamakan **VARIABEL (*Variable*)**.

[[IMAGE: bab1_analogi_variabel.png | Gambar 1.3: Konsep Variabel — Kotak Ajaib Penyimpan Nilai dalam Game]]

Variabel adalah tempat di dalam memori komputer yang kita beri nama khusus untuk menyimpan suatu nilai data (angka atau teks) yang nilainya dapat berubah-ubah sepanjang program berjalan.

Dalam perancangan game kuis, kita menggunakan 3 variabel utama:
1. **Variabel `Skor`:**  
   Menyimpan perolehan nilai pemain. Dimulai dari angka 0 saat game dibuka, dan bertambah (+10) setiap pemain menjawab kuis dengan benar.
2. **Variabel `Nyawa` (*Health / Lives*):**  
   Menyimpan sisa kesempatan bermain. Dimulai dari angka 3, dan berkurang (-1) jika pemain salah memilih jawaban. Jika variabel `Nyawa = 0`, layar menampilkan *"Game Over!"*.
3. **Variabel `Waktu` (*Timer*):**  
   Menghitung mundur waktu berpikir (misalnya dari 30 detik ke 0 detik) untuk menguji kecepatan berpikir pemain.

---

### 5. Kartu Mantra Koding Blok Scratch 3.0

Untuk menyatukan logika percabangan, perulangan, dan variabel ke dalam game kuis nyata, kita menyusun balok kode di Scratch 3.0 sebagaimana ditampilkan pada kartu mantra berikut:

[[IMAGE: bab1_kartu_blok_scratch.png | Gambar 1.4: Kartu Mantra Blok Scratch — Percabangan, Perulangan & Variabel]]

Perhatikan struktur susunan blok koding kuis edukasi berikut:
* **Langkah 1: Inisialisasi Game (Persiapan Awal)**
  * `when green flag clicked` (Ketika bendera hijau diklik)
  * `set [Skor v] to [0]` (Mulai skor dari angka nol)
  * `set [Nyawa v] to [3]` (Berikan modal tiga nyawa)
* **Langkah 2: Menampilkan Pertanyaan & Evaluasi Jawaban**
  * `ask [Berapakah hasil dari 25 x 4?] and wait`
  * `if <(answer) = [100]> then`
    * `change [Skor v] by (10)`
    * `say [Hebat! Jawabanmu Tepat Sekali!] for (2) seconds`
    * `start sound [Cheer v]`
  * `else`
    * `change [Nyawa v] by (-1)`
    * `say [Aduh, belum tepat! Jawabannya adalah 100.] for (2) seconds`
    * `start sound [Oops v]`
  * `end`

> 💡 **Tips Koding Robot Kibo:**
> Saat membandingkan jawaban teks pada Scratch, huruf kapital dan huruf kecil tidak dibedakan (*case-insensitive*). Jawaban *"monas"*, *"Monas"*, maupun *"MONAS"* akan dianggap sama oleh Scratch! Namun pastikan pemain tidak menambahkan spasi berlebih di awal atau akhir kata!

---

### 6. Pojok Karakter & Etika: Fair Play & Kejujuran (Menolak Cheat Code)

Pernahkah kamu tergoda untuk mengubah blok kode di Scratch agar skor langsung bernilai 99.999 tanpa harus bersusah payah menjawab soal kuis? Tindakan ini dalam dunia game sering disebut menggunakan kode curang (*cheat code*).

Sebagai Pelajar Pancasila dan koder sejati yang berintegritas:
1. **Kejujuran Intelektual:** Kemenangan game yang diraih melalui kecurangan tidak akan pernah menghasilkan rasa bangga yang sejati.
2. **Sportivitas (*Fair Play*):** Saat kamu merancang game untuk teman-teman sekelasmu, buatlah aturan permainan yang adil, seimbang, dan menantang. Game yang terlalu mudah karena kecurangan akan terasa hambar dan cepat ditinggalkan pemain.
3. **Menghargai Proses:** Kesalahan (*bug*) atau kegagalan saat bermain adalah sarana melatih ketahanan mental dan ketekunan untuk belajar lebih giat lagi!

---

## C. PROSES DAN AKTIVITAS BELAJAR (AYO MENCOBA)

### Aktivitas Unplugged: Detektif Kartu Logika Kondisional

Mari kita simulasikan cara kerja logika percabangan di kelas tanpa menggunakan komputer!

**Peralatan:**
* 4 lembar kartu bertuliskan **KONDISI** (Warna Kuning).
* 4 lembar kartu bertuliskan **AKSI YA** (Warna Hijau).
* 4 lembar kartu bertuliskan **AKSI TIDAK** (Warna Merah).

**Langkah Permainan:**
1. Bentuklah kelompok beranggotakan 4 orang.
2. Murid A bertugas menjadi **Pemeriksa Kondisi (Processor)**.
3. Murid B dan C menjadi **Pelaksana Aksi (Aktuator)**.
4. Murid D bertugas mencatat nilai pada papan tulis **(Variabel Skor)**.
5. Murid A membaca kartu kondisi dengan lantang:  
   *"JIKA murid di depan memakai kacamata, MAKA berdiri dan tepuk tangan dua kali; JIKA TIDAK, melompat satu kali sambil tersenyum!"*
6. Seluruh kelompok harus merespon instruksi dalam waktu 3 detik. Murid D menambah 10 poin jika respon kelompok benar dan tepat waktu!
7. Bergantian peran agar seluruh anggota kelompok merasakan menjadi prosesor logika!

---

## D. TUGAS PROYEK KINERJA SISWA (LKPD 1.1)

### LEMBAR KERJA PESERTA DIDIK (LKPD 1.1)
**Judul Proyek:** Merancang Game Kuis Edukasi "Pahlawan Nusantara" di Scratch 3.0  
**Nama Kelompok / Anggota:** ............................................................  
**Kelas / Tanggal Praktik:** VI / ....................................................  

#### 1. Tujuan Proyek
Kalian mampu merancang game interaktif yang berisi minimal 3 soal pilihan ganda tentang pahlawan nasional Indonesia, menggunakan blok percabangan `if-then-else`, perulangan `repeat`, dan variabel `Skor`.

#### 2. Tabel Rancangan Soal Kuis
Isilah tabel rancangan berikut sebelum membuka aplikasi Scratch:

| No | Pertanyaan Kuis Pahlawan | Kunci Jawaban Benar | Respon Jika Benar (+10 Skor) | Respon Jika Salah (-1 Nyawa) |
|:---:|:---|:---|:---|:---|
| 1 | Siapakah pahlawan wanita dari Jepara pelopor emansipasi wanita? | R.A. Kartini | "Benar! Habis Gelap Terbitlah Terang!" | "Belum tepat, beliau adalah R.A. Kartini." |
| 2 | Pahlawan nasional asal Maluku yang memimpin perlawanan di Saparua adalah... | Pattimura | "Hebat! Kapitan Pattimura pahlawan gagah!" | "Belum tepat, beliau adalah Kapitan Pattimura." |
| 3 | Siapakah tokoh yang membacakan teks Proklamasi Kemerdekaan RI? | Ir. Soekarno | "Tepat sekali! Sang Proklamator bangsa!" | "Belum tepat, beliau adalah Bung Karno." |

#### 3. Panduan Langkah Pembuatan di Scratch
1. Buka aplikasi Scratch 3.0 (di browser atau aplikasi desktop).
2. Pilih latar belakang (*backdrop*) bertema panggung teater atau ruang belajar Nusantara.
3. Pilih karakter (*sprite*) favoritmu (misalnya Kucing Scratch atau karakter anak berpakaian seragam).
4. Buat variabel baru bernama `Skor` dan `Nyawa` di tab menu *Variables*.
5. Susun balok kode inisialisasi awal (`when green flag clicked`, set skor ke 0, set nyawa ke 3).
6. Masukkan balok `repeat (3)` dan masukkan balok `ask` serta `if-then-else` sesuai tabel rancangan di atas.
7. Simpan karyamu dengan format nama: `Kuis_Pahlawan_Kelompok[Nomor].sb3`.

#### 4. Rubrik Penilaian Proyek Mandiri
* [ ] Variabel `Skor` dan `Nyawa` berhasil dibuat dan muncul di layar (Skor Maksimal: 25).
* [ ] Logika percabangan `if-then-else` berjalan tepat sesuai kunci jawaban (Skor Maksimal: 35).
* [ ] Terdapat efek suara (*sound effect*) yang berbeda saat jawaban benar dan salah (Skor Maksimal: 20).
* [ ] Game berjalan mulus tanpa bug hingga akhir soal (Skor Maksimal: 20).  
* **Total Nilai Kinerja Proyek:** .................... / 100

---

## E. RANGKUMAN MATERI BAB I

1. **Logika Percabangan (*Conditional Logic*)** adalah kemampuan program komputer untuk mengambil keputusan dan memilih tindakan berdasarkan terpenuhi atau tidaknya suatu syarat kondisi (*True* atau *False*).
2. Struktur **If-Then** hanya menjalankan instruksi jika kondisi bernilai benar. Struktur **If-Then-Else** menyediakan dua jalur instruksi yang berbeda: satu jalur jika kondisi terpenuhi, dan satu jalur lain jika kondisi tidak terpenuhi.
3. **Perulangan (*Looping*)** memungkinkan komputer menjalankan sekumpulan perintah berulang kali tanpa harus menulis ulang baris kodenya. Blok `repeat` mengulang instruksi sebanyak angka tertentu, sedangkan blok `forever` mengulang instruksi tanpa henti.
4. **Variabel** adalah ruang penyimpanan memori komputer berlabel nama yang nilainya dapat diubah sewaktu-waktu oleh program, sangat bermanfaat untuk menghitung skor permainan, sisa waktu hitung mundur, dan nama pemain.
5. **Prinsip Fair Play** mengajarkan kita untuk selalu jujur dalam merancang aturan game dan menolak penggunaan jalan pintas curang (*cheat code*).

---

## F. TES FORMATIF (UJI PEMAHAMAN HOTS)

### Bagian 1: Pilihan Ganda (Pilihlah Jawaban A, B, C, atau D yang Paling Tepat!)

1. Perhatikan potongan instruksi logika berikut:  
   *"Jika suhu ruangan lebih dari 30 derajat Celsius, maka nyalakan kipas angin pendingin; Jika tidak, matikan kipas angin."*  
   Instruksi di atas merupakan contoh nyata dari penerapan struktur logika...  
   A. Dekomposisi sekuensial  
   B. Perulangan tanpa henti (*Forever Loop*)  
   C. Percabangan dua arah (*If-Then-Else*)  
   D. Abstraksi simbol angka  

2. Erik sedang memainkan game Scratch buatan temannya. Saat karakter menyentuh koin emas, nilai di sudut kiri atas layar bertambah dari angka 50 menjadi 60. Komponen pemrograman yang bertugas menyimpan dan mengubah angka tersebut adalah...  
   A. Operator warna  
   B. Variabel  
   C. Backdrop panggung  
   D. Kostum karakter  

3. Di sebuah game balap mobil, programmer ingin agar mobil rintangan di jalur kanan meluncur terus-menerus dari atas ke bawah tanpa pernah berhenti sepanjang permainan berlangsung. Blok perulangan Scratch yang paling tepat digunakan adalah...  
   A. `repeat (1)`  
   B. `repeat until <key space pressed>`  
   C. `forever`  
   D. `wait until <touching edge>`  

4. Perhatikan potongan blok kode Scratch berikut:  
   `set [Skor v] to [10]`  
   `repeat (3)`  
   `    change [Skor v] by (5)`  
   `end`  
   Berapakah nilai akhir dari variabel `Skor` setelah potongan blok kode di atas selesai dieksekusi oleh komputer?  
   A. 15  
   B. 20  
   C. 25  
   D. 30  

5. Siti menyusun kuis matematika perkalian:  
   `ask [Berapakah hasil 8 x 7?] and wait`  
   `if <(answer) = [56]> then`  
   `    say [Hebat, Benar!] for (2) secs`  
   `    change [Skor v] by (10)`  
   `else`  
   `    say [Maaf, coba hitung lagi!] for (2) secs`  
   `end`  
   Jika Made memainkan game tersebut dan mengetikkan angka 54 di kotak jawaban, maka peristiwa yang akan terjadi adalah...  
   A. Skor bertambah 10 dan karakter berkata *"Hebat, Benar!"*  
   B. Skor berkurang 10 dan layar komputer menutup otomatis  
   C. Karakter berkata *"Maaf, coba hitung lagi!"* dan skor tidak bertambah  
   D. Komputer menampilkan pesan eror dan permainan macet  

6. Mengapa pada awal permainan kuis edukasi, kita harus meletakkan blok `set [Skor v] to [0]` tepat di bawah blok `when green flag clicked`?  
   A. Agar karakter bergerak melompat ke tengah layar panggung  
   B. Untuk memastikan nilai skor kembali bersih dari angka nol setiap kali game baru dimulai  
   C. Agar komputer menghapus seluruh pertanyaan kuis yang lama  
   D. Supaya suara musik latar belakang berhenti berbunyi  

7. Perhatikan kasus logika berikut: Made ingin membuat pintu otomatis perpustakaan sekolah. Pintu hanya boleh bergeser membuka jika sensor mendeteksi ada orang pada jarak kurang dari 50 cm DAN kartu perpustakaan berhasil dipindai. Konsep logika yang digunakan Made adalah...  
   A. Percabangan dengan dua kondisi bersyarat  
   B. Perulangan tunggal tak terhingga  
   C. Dekomposisi gambar piksel  
   D. Variabel acak tanpa sensor  

8. Suatu game kuis dirancang menggunakan blok `repeat (5)`. Di dalam perulangan tersebut terdapat satu pertanyaan kuis. Jika setiap pertanyaan yang dijawab benar bernilai 20 poin dan pemain berhasil menjawab 4 soal dengan benar serta 1 soal keliru, maka nilai akhir variabel `Skor` adalah...  
   A. 60  
   B. 80  
   C. 100  
   D. 20  

9. Made tergoda untuk mengubah baris kode program game kuis buatan kelompoknya menjadi `change [Skor v] by (1000)` agar kelompoknya langsung mendapatkan nilai tertinggi tanpa perlu menjawab pertanyaan. Sikap Made tersebut bertentangan dengan profil Pelajar Pancasila, khususnya dimensi...  
   A. Bergotong Royong  
   B. Mandiri dan Berakhlak Mulia (Kejujuran & Integritas)  
   C. Berkebinekaan Global  
   D. Kecepatan Mengetik Keyboard  

10. Jika kita ingin membuat game kuis berdurasi waktu, misalnya pemain hanya diberi waktu 60 detik untuk menjawab sebanyak mungkin soal sebelum permainan otomatis berhenti, variabel tambahan yang wajib kita ciptakan adalah...  
    A. Variabel Warna Karakter  
    B. Variabel Timer (Waktu Mundur)  
    C. Variabel Ukuran Huruf  
    D. Variabel Volume Speaker  

---

### Bagian 2: Soal Uraian Bernalar Kritis (Jawablah dengan Lengkap dan Jelas!)

1. Jelaskan perbedaan mendasar antara struktur percabangan `If-Then` dan struktur percabangan `If-Then-Else`! Berikan masing-masing 1 contoh penerapannya dalam kehidupan sehari-hari anak sekolah!
2. Mengapa variabel di dalam komputer diibaratkan seperti toples kue berlabel nama di dapur? Sebutkan 3 contoh variabel yang sering digunakan dalam permainan komputer beserta nilai awal yang tepat saat game dimulai!
3. Perhatikan situasi berikut: Siti membuat game petualangan labirin. Ia ingin agar karakter kucing dapat dikendalikan dengan tombol panah keyboard sepanjang permainan tanpa henti. Blok perulangan manakah yang harus dipilih Siti antara `repeat (10)` dan `forever`? Berikan alasan logismu!
4. Tulislah rancangan algoritma (langkah demi langkah) untuk sebuah mesin penjual tiket wahana permainan otomatis yang memeriksa tinggi badan anak: anak yang memiliki tinggi badan minimal 120 cm diizinkan naik, sedangkan anak dengan tinggi di bawah 120 cm harus didampingi orang tua!
5. Apa bahaya dan dampak negatif bagi diri sendiri jika seorang programmer terbiasa menggunakan *cheat code* (jalan pintas curang) dalam membuat atau memainkan game? Hubungkan penjelasanmu dengan nilai sportivitas dan kegigihan belajar!

---

## G. KUNCI JAWABAN & PEMBAHASAN TES FORMATIF BAB I

### Kunci Jawaban Pilihan Ganda:
1. **C** (Percabangan dua arah *If-Then-Else*: menyediakan 2 cabang aksi berdasarkan suhu ruangan).
2. **B** (Variabel: kotak memori penyimpanan data yang dapat berubah nilainya).
3. **C** (`forever`: mengulang instruksi tanpa batas selama permainan berjalan).
4. **C** (Skor awal = 10; diulang 3 kali menambah 5: 10 + 5 + 5 + 5 = 25).
5. **C** (Karena 54 != 56, maka masuk ke cabang `else`: karakter berkata *"Maaf, coba hitung lagi!"* dan skor tidak bertambah).
6. **B** (Inisialisasi variabel skor agar permainan baru dimulai dari angka bersih 0, bukan melanjutkan sisa nilai game sebelumnya).
7. **A** (Percabangan dua kondisi bersyarat majemuk: jarak < 50 cm DAN kartu terpindai).
8. **B** (4 soal benar x 20 poin = 80 poin).
9. **B** (Dimensi Berakhlak Mulia & Mandiri: mengedepankan integritas dan kejujuran akademik).
10. **B** (Variabel Timer / Waktu Mundur untuk membatasi durasi permainan).

### Pedoman Pembahasan Soal Uraian:
1. **Perbedaan:** `If-Then` hanya memiliki 1 jalur aksi (jika kondisi salah, tidak ada aksi balasan khusus). Sedangkan `If-Then-Else` memiliki 2 jalur aksi alternatif (jalur Benar dan jalur Salah). Contoh: *Jika hujan bawa payung (If-Then)* vs *Jika nilai >= 75 dapat medali, jika tidak remedial (If-Then-Else)*.
2. **Analogi Variabel:** Seperti toples berlabel karena nama labelnya tetap (wadah), tetapi isinya dapat bertambah, berkurang, atau diganti kapan saja. Contoh: Variabel `Skor` (awal = 0), Variabel `Nyawa` (awal = 3), Variabel `Waktu` (awal = 60 detik).
3. **Pemilihan Loop:** Siti harus memilih blok `forever`. Alasan: input penekanan tombol panah oleh pemain bisa terjadi kapan saja secara acak sepanjang game. Jika menggunakan `repeat (10)`, setelah 10 kali pengecekan program akan mati dan tombol tidak bisa ditekan lagi.
4. **Algoritma Mesin Tiket:**
   * Langkah 1: Sensor mengukur tinggi badan pengunjung.
   * Langkah 2: JIKA tinggi badan >= 120 cm, MAKA cetak tiket bertuliskan *"Kategori Mandiri: Selamat Bermain!"*.
   * Langkah 3: JIKA TIDAK (< 120 cm), MAKA cetak tiket bertuliskan *"Kategori Pendampingan: Wajib Ditemani Orang Dewasa!"*.
   * Langkah 4: Palang pintu wahana terbuka.
5. **Dampak Negatif Cheat Code:** Menghilangkan esensi belajar dan pemecahan masalah, menumbuhkan sifat malas dan tidak jujur, serta merusak kepuasan batin karena keberhasilan diraih tanpa kerja keras nyata.

---

## H. POJOK DISKUSI BERSAMA AYAH DAN BUNDA DI RUMAH

Halo Ayah dan Bunda! Minggu ini ananda telah mempelajari bagaimana logika percabangan (*If-Then-Else*) dan variabel bekerja dalam membentuk pola pikir analitis.

Yuk, luangkan waktu 10-15 menit bersama ananda untuk mendiskusikan topik hangat berikut:
1. Tanyakan kepada ananda: *"Kak/Dek, coba sebutkan 3 aturan penting di rumah kita yang menggunakan logika 'Jika... Maka...'!"* (Misal: *Jika sudah selesai makan malam, maka piring dicuci di wastafel*).
2. Ajak ananda mendemonstrasikan game kuis Scratch sederhana yang telah dirancangnya di sekolah. Berikan apresiasi atas kreativitas logika ananda!
3. Diskusikan pentingnya bersikap jujur dan adil (*fair play*) saat bermain bersama saudara atau teman di lingkungan rumah.

---

## I. JURNAL REFLEKSIKU & LENCANA MEDALI BINTANG KODER

Salinlah tabel jurnal refleksi ini ke buku catatan kodingmu dan berikan tanda centang (✓) sesuai dengan perasaan jujurmu hari ini:

| No | Pernyataan Refleksi Pembelajaran | Sangat Paham 😊 | Cukup Paham 😐 | Perlu Belajar Lagi 😢 |
|:---:|:---|:---:|:---:|:---:|
| 1 | Saya memahami arti logika percabangan *If-Then* dan *If-Then-Else*. | [ ] | [ ] | [ ] |
| 2 | Saya dapat membedakan fungsi blok `repeat` dan blok `forever` di Scratch. | [ ] | [ ] | [ ] |
| 3 | Saya mampu membuat variabel `Skor` dan mengatur nilainya agar bertambah. | [ ] | [ ] | [ ] |
| 4 | Saya berhasil menyelesaikan proyek kuis interaktif pahlawan nasional. | [ ] | [ ] | [ ] |
| 5 | Saya selalu menjunjung tinggi kejujuran dan menolak bermain curang. | [ ] | [ ] | [ ] |

**Lencana Pencapaian Bab I:**  
Selamat! Kalian resmi meraih:  
🎖️ **LENCANA MEDALI ARSITEK LOGIKA GAME CERDAS TINGKAT 1 (FASE C)** 🎖️  
*"Teruslah bernalar kritis, karena logika yang teratur adalah kunci pembuka pintu inovasi masa depan!"*
"""
