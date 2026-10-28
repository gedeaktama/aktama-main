# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 3 Buku Siswa KKA Kelas 6 SD (Fase C)
BAB III: MENJELAJAHI SENSOR DAN OTOMASI PERANGKAT CERDAS (16 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_3_SD6 = """# BAB III MENJELAJAHI SENSOR DAN OTOMASI PERANGKAT CERDAS

## MISI 3: PENJELAJAH SENSOR & KOTA PINTAR
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi dan Etika Kecerdasan Artifisial (LEKA) & Pemanfaatan KA (PPKA)
* **Target Lencana Koder:** Medali Penjelajah Sensor & Otomasi Cerdas (Bintang Emas Fase C)

---

## A. PENDAHULUAN: MISTERI PINTU KACA & KERAN AIR TANPA SENTUH

Waktu istirahat kedua baru saja dimulai. Erik bergegas menuju tempat wudhu di samping musala sekolah untuk bersiap salat zuhur. Saat Erik mengulurkan kedua telapak tangannya ke bawah mulut keran air, tiba-tiba: *Cyuuurrr!* Air jernih langsung mengalir deras membasahi tangannya. Namun, begitu Erik menarik tangannya ke belakang, aliran air seketika berhenti sendiri tanpa ada gagang putaran yang disentuh!

"Wah, luar biasa sekali keran baru ini!" seru Erik kagum. "Tidak ada tombol yang ditekan, tapi airnya bisa tahu persis kapan tanganku datang dan kapan tanganku pergi!"

Made yang baru saja kembali dari minimarket di seberang sekolah ikut menimpali dengan penuh semangat. "Erik, di pintu masuk minimarket tadi juga ajaib sekali! Begitu Made melangkah mendekati pintu kaca geser, pintunya langsung bergeser membuka dengan mulus: *Sreeek!* Lalu setelah Made masuk ke dalam toko, pintunya menutup kembali dengan rapat. Apakah ada orang tersembunyi yang menarik tali di atas pintu?"

Siti tersenyum mendengar tebakan Made. "Tentu saja tidak ada orang yang menarik tali, Made! Di atas pintu kaca itu terpasang mata elektronik canggih yang selalu berjaga!"

*"Tii-tut! Bip-bip! Seratus untuk Siti!"* sambut **Robot Kibo** yang melayang riang di pundak Erik. Layar bulat di wajah Kibo berkedip-kedip menampilkan gambar sepasang mata dan telinga robot.

[[IMAGE: bab3_komik_pembuka_sd6.png | Gambar 3.1: Komik Sahabat Koder — Misteri Pintu & Keran Ajaib yang Menyala Sendiri]]

"Teman-teman koder cilik!" jelas Robot Kibo penuh antusiasme. "Manusia memiliki pancaindra: mata untuk melihat, telinga untuk mendengar, kulit untuk meraba, hidung untuk mencium, dan lidah untuk mengecap. Nah, bagaimana dengan komputer dan robot? Komputer membutuhkan alat peniru pancaindra yang dinamakan **SENSOR**!"

"Sensor?" ulang Erik dan Made serempak.

"Tepat sekali! Sensor adalah indera buatan yang dipasang pada komputer untuk menangkap rangsangan fisik dari alam—seperti cahaya matahari, jarak benda, suhu udara, gerakan manusia, hingga rekaman gambar—lalu mengubahnya menjadi sinyal data digital. Berkat sensor dan koding kecerdasan artifisial, lahirlah **SISTEM OTOMASI PINTAR (*Smart Automation*)** yang membuat lingkungan kita menjadi jauh lebih hemat energi, aman, dan ramah bagi semua orang, termasuk sahabat kita penyandang disabilitas!"

Mata Erik, Siti, dan Made berbinar-binar kagum. Mereka tidak sabar ingin membedah bagaimana cara kerja indera buatan komputer tersebut!

> **Pertanyaan Pemantik Penjelajah Cilik:**
> 1. Menurutmu, mengapa keran air otomatis tanpa sentuh jauh lebih higienis dan hemat air dibandingkan keran putar biasa di sekolah?
> 2. Bagaimana sebuah lampu jalanan di kotamu bisa tahu persis bahwa matahari sudah terbenam sehingga lampu harus menyala terang benderang?
> 3. Jika sebuah mobil masa depan bisa menyetir sendiri tanpa sopir (*self-driving car*), sensor apa sajakah yang wajib dipasang agar mobil tersebut tidak menabrak kucing yang melintas mendadak? Yuk, kita temukan jawabannya!

---

## B. KONSEP DAN MATERI PEMBELAJARAN

### 1. Sensor: Jendela Dunia Komputer Peniru Pancaindra Manusia

Bayangkan jika kamu harus menutup mata, menyumbat telinga, dan mengenakan sarung tangan tebal secara bersamaan. Kamu pasti akan kesulitan berjalan di dalam ruangan karena tidak dapat merasakan lingkungan sekitarmu, bukan?

Hal itulah yang terjadi pada komputer tanpa sensor! Tanpa sensor, komputer hanyalah kotak sirkuit yang 'buta' dan 'tuli'. Sensor adalah pintu gerbang yang menghubungkan dunia fisik tempat kita tinggal dengan dunia digital di dalam chip komputer.

[[IMAGE: bab3_infografis_4_sensor.png | Gambar 3.2: 4 Sensor Cerdas di Sekitar Kita vs Pancaindra Manusia]]

Mari kita kenali **4 Sensor Cerdas Utama** yang paling banyak digunakan di sekitar kita pada Gambar 3.2 di atas:

1. **Sensor Cahaya (LDR - *Light Dependent Resistor*):**  
   * *Meniru Fungsi:* **Mata Manusia (Sensitivitas Terang-Gelap)**.  
   * *Cara Kerja:* Nilai hambatan listriknya berubah sesuai terang atau redupnya cahaya yang mengenainya. Saat siang benderang nilai data tinggi, saat gelap gulita nilai data turun mendekati nol.  
   * *Penerapan Nyata:* Lampu penerangan jalan umum (PJU) otomatis menyala saat waktu magrib tiba dan mati sendiri saat fajar menyingsing.
2. **Sensor Jarak Ultrasonik (*Ultrasonic Distance Sensor*):**  
   * *Meniru Fungsi:* **Pendengaran & Sonar Kelelawar / Lumba-Lumba**.  
   * *Cara Kerja:* Memancarkan gelombang suara ultrasonik berfrekuensi tinggi (tidak terdengar telinga manusia), lalu menghitung waktu pantulan gema saat gelombang membentur benda di depannya.  
   * *Penerapan Nyata:* Sensor parkir mobil belakang yang berbunyi *"Bip... Bip... Bip... BIIIP!"* semakin kencang saat bagian belakang mobil mendekati dinding garasi.
3. **Sensor Gerak Inframerah Pasif (PIR - *Passive Infrared*):**  
   * *Meniru Fungsi:* **Kulit Perasa Panas Tubuh**.  
   * *Cara Kerja:* Menangkap radiasi hawa hangat yang dipancarkan secara alami oleh tubuh manusia atau hewan yang bergerak melintas di depannya.  
   * *Penerapan Nyata:* Lampu tangga atau pendingin ruangan (AC) pintar di ruang rapat yang otomatis menyala ketika ada orang masuk dan mati jika ruangan kosong selama 10 menit.
4. **Kamera Cerdas Vision AI (*Computer Vision*):**  
   * *Meniru Fungsi:* **Mata + Otak Manusia**.  
   * *Cara Kerja:* Tidak hanya menangkap gambar, tetapi menggunakan algoritma AI machine learning untuk mengenali pola wajah, membaca huruf pada pelat nomor kendaraan, atau memilah jenis sampah.  
   * *Penerapan Nyata:* Palang pintu otomatis gerbang tol tanpa henti (*e-toll gate*) dan sistem presensi wajah digital di sekolah.

---

### 2. Diagram Siklus Kerja Sistem Otomatis Cerdas: Input -> Proses -> Output

Bagaimana sebuah sistem otomatis bekerja secara utuh? Setiap mesin pintar di dunia selalu mengikuti siklus 3 langkah teratur:

[[IMAGE: bab3_diagram_sistem_otomatis.png | Gambar 3.3: Siklus Kerja Sistem Otomatis Cerdas (Input -> Proses -> Output)]]

1. **Langkah 1: Masukan (*INPUT* - Dunia Nyata ke Komputer):**  
   Sensor mendeteksi keadaan fisik. Contoh: Sensor ultrasonik pada palang pintu parkir mendeteksi bodi mobil pada jarak 50 cm di depan gerbang. Data jarak "50 cm" dikirimkan ke komputer prosesor.
2. **Langkah 2: Proses (*PROCESS* - Pengambilan Keputusan Logika AI):**  
   Chip mikroprosesor membaca data masukan dan mengevaluasi aturan koding yang telah ditanamkan oleh programmer:  
   `Jika Jarak <= 50 cm DAN Pelat Nomor Valid -> Perintahkan Buka Palang!`
3. **Langkah 3: Keluaran (*OUTPUT* - Komputer Melakukan Aksi Nyata):**  
   Komputer mengalirkan listrik ke komponen penggerak fisik yang dinamakan **AKTUATOR (*Actuator*)**—seperti motor listrik yang memutar poros palang ke atas, lampu indikator berubah dari warna merah menjadi hijau, dan speaker berbunyi *"Silakan Masuk!"*.

---

### 3. Penerapan Nyata Sistem Otomasi Cerdas di Lingkungan Kita

Otomasi cerdas membawa manfaat raksasa bagi kehidupan masyarakat:
* **Penghematan Energi & Air (*Green Technology*):**  
  Keran air otomatis mencegah air wudhu meluap sia-sia karena murid lupa memutar keran. Lampu pintar menghemat tagihan listrik sekolah hingga 40%!
* **Pertanian Cerdas (*Smart Farming* di Nusantara):**  
  Petani modern di berbagai daerah di Indonesia menanam sensor kelembapan tanah di sawah. Saat tanah mulai kering kerontang, pompa air otomatis menyala menyiram tanaman padi dan mati sendiri saat tanah cukup basah.
* **Keamanan Lingkungan Sekolah:**  
  Kamera CCTV ber-AI dapat membunyikan sirine alarm jika mendeteksi ada asap kebakaran di laboratorium sebelum api membesar.

---

### 4. Kecerdasan Artifisial Ramah Disabilitas (*AI for Inclusivity*)

Salah satu keindahan terbesar dari perkembangan koding dan kecerdasan artifisial adalah kemampuannya menjadi jembatan kasih sayang bagi sahabat-sahabat kita penyandang disabilitas (*AI for Good*).

[[IMAGE: bab3_ai_inklusi_disabilitas.png | Gambar 3.4: Kecerdasan Artifisial untuk Inklusivitas (AI for Inclusivity)]]

Mari kita pelajari dua inovasi teknologi inklusif yang luar biasa ini:
1. **Kacamata Cerdas Tunanetra (*Smart Vision Glasses*):**  
   Sahabat tunanetra memiliki keterbatasan dalam melihat. Dengan kacamata cerdas yang dilengkapi kamera AI mini dan earphone konduksi tulang, AI membaca lingkungan di depan:  
   *"Ada lampu merah di depan jarak dua meter,"* atau *"Uang kertas di tanganmu bernilai Rp50.000."* Suara ramah ini memandu mereka berjalan mandiri dan percaya diri di tempat umum!
2. **Aplikasi Penerjemah Suara-ke-Teks Langsung (*Live Transcribe* untuk Tunarungu):**  
   Di ruang kelas inklusi, sahabat kita yang tunarungu sering kesulitan menangkap penjelasan guru yang diucapkan secara lisan. Menggunakan kecerdasan artifisial pengenal suara (*Speech Recognition*), suara bapak/ibu guru langsung diubah menjadi huruf dan teks berjalan di layar tablet murid secara *real-time*. Sahabat tunarungu dapat membaca setiap materi pelajaran tanpa ada yang terlewat!

---

### 5. Pojok Karakter & Etika: Mengapa Tombol Darurat (*Emergency Stop*) Wajib Ada?

Meskipun sistem otomatis dan robot AI tampak sangat pintar dan mandiri, sebuah prinsip etika mutlak yang tidak boleh dilupakan adalah: **MANUSIA ADALAH PENANGGUNG JAWAB TERTINGGI KESELAMATAN (*Human Oversight & Responsibility*)**.

Pernahkah kamu memperhatikan tombol merah berukuran besar bertuliskan **EMERGENCY STOP** pada eskalator mal, mesin pabrik, atau robot perakit mobil?
1. **Mesin Tidak Memiliki Hati Nurani:** Sensor bisa mengalami gangguan (kotor oleh debu tebal, tersiram air, atau kabel putus) sehingga salah membaca kondisi darurat.
2. **Kewajiban Kendali Manusia:** Pada mobil otonom tanpa sopir sekalipun, undang-undang keselamatan mewajibkan adanya setir manual dan pedal rem yang dapat diambil alih oleh manusia kapan saja saat bahaya mengancam.
3. **Nilai Tanggung Jawab:** Sebagai calon pencipta teknologi masa depan, kita tidak boleh menyalahkan mesin jika terjadi kesalahan (*"Bukan salah saya, komputernya yang salah!"*). Perancang dan pengawas manusialah yang wajib memastikan setiap teknologi aman dan bermanfaat bagi keselamatan jiwa sesama.

> 🔍 **Tahukah Kamu?**
> Di Ibu Kota Nusantara (IKN) Kalimantan Timur, Indonesia sedang membangun konsep **Kota Cerdas (*Smart City*)**, di mana bus listrik tanpa sopir akan berlalu lalang di jalur khusus dipandu oleh puluhan sensor canggih dan jaringan internet super cepat 5G! Anak-anak Indonesia seperti kalianlah yang kelak akan menjadi insinyur pengembangnya!

---

## C. PROSES DAN AKTIVITAS BELAJAR (AYO MENCOBA)

### Aktivitas Unplugged: Simulasi Mobil Otonom Cerdas di Lantai Kelas

Mari kita simulasikan cara kerja sensor mobil pintar yang menelusuri rute labirin di lantai kelas!

**Peralatan:**
* Selotip kertas berwarna untuk membuat garis jalur labirin jalan raya di lantai kelas (ukuran 4 x 4 meter).
* 3 buah kardus rintangan (diibaratkan sebagai lubang jalan atau mobil mogok).
* 1 boneka kecil (diibaratkan sebagai pejalan kaki yang menyeberang zebra cross).
* 1 kain penutup mata untuk murid yang menjadi **"Mobil Otonom"**.
* 1 set kartu suara untuk murid yang menjadi **"Sensor Ultrasonik"**.

**Langkah Permainan:**
1. Bentuklah kelompok beranggotakan 4 orang:
   * Murid 1 menjadi **Mobil Otonom** (mata ditutup kain, hanya bergerak sesuai instruksi suara).
   * Murid 2 menjadi **Sensor Ultrasonik & Kamera AI** (berjalan tepat di depan mobil mengamati rintangan).
   * Murid 3 menjadi **Komputer Prosesor (AI Decision Maker)** (menerjemahkan data sensor menjadi komando belok atau rem).
   * Murid 4 menjadi **Pengawas Tombol Darurat (Safety Officer)** (memegang peluit, siap meniup jika mobil berjarak kurang dari 10 cm dari tabrakan).
2. Aturan Navigasi Sensor:
   * Jarak aman (> 1 meter): Sensor berbisik *"Jalur Bersih!"* -> AI memberi instruksi *"Maju perlahan 3 langkah!"*.
   * Jarak dekat (< 50 cm): Sensor berbunyi *"Bip-bip Bahaya!"* -> AI memberi instruksi *"Berhenti, belok kanan 90 derajat!"*.
   * Pejalan kaki menyeberang: Sensor berteriak *"Manusia Menyeberang!"* -> AI memberi komando *"Rem Penuh sampai pejalan kaki lewat!"*.
3. Setiap kelompok menguji ketepatan navigasi mereka hingga mobil tiba dengan selamat di garis finis tanpa menyenggol rintangan. Bergantianlah peran!

---

## D. TUGAS PROYEK KINERJA SISWA (LKPD 3.1)

### LEMBAR KERJA PESERTA DIDIK (LKPD 3.1)
**Judul Proyek:** Merancang Poster Konseptual "Alat Pintar Sekolah Masa Depan"  
**Nama Kelompok / Anggota:** ............................................................  
**Kelas / Tanggal Praktik:** VI / ....................................................  

#### 1. Tujuan Proyek
Kalian mampu merancang sebuah konsep inovasi alat otomatis cerdas berbasis sensor untuk memecahkan satu masalah nyata di lingkungan sekolah (kebersihan kantin, penghematan listrik kelas, keamanan gerbang, atau kemudahan bagi sahabat disabilitas), lengkap dengan diagram siklus Input -> Proses -> Output.

#### 2. Lembar Analisis Inovasi Alat Pintar

* **Nama Alat Cerdas yang Dirancang:** `.........................................................................................`
* **Masalah Sekolah yang Ingin Diatasi:** `.........................................................................................`
* **Sensor yang Digunakan (Input):** `.........................................................................................`  
  *(Alasan pemilihan sensor: .....................................................................................................)*
* **Logika Pemrosesan (Decision Rules):**  
  * JIKA: `...................................................................................................................................`
  * MAKA: `...................................................................................................................................`
  * JIKA TIDAK: `.........................................................................................................................`
* **Aktuator & Keluaran Nyata (Output):** `.........................................................................................`
* **Fitur Tombol Darurat / Kendali Manusia:** `................................................................................`

#### 3. Rubrik Penilaian Proyek Mandiri
* [ ] Keaslian ide inovasi dan kebermanfaatannya bagi warga sekolah (Skor: 30).
* [ ] Ketepatan pemilihan jenis sensor sesuai dengan besaran fisik yang dideteksi (Skor: 25).
* [ ] Kejelasan alur logika diagram siklus Input -> Proses -> Output (Skor: 25).
* [ ] Memperhatikan faktor keselamatan (*Human Oversight / Emergency Stop*) dan estetika poster (Skor: 20).  
* **Total Nilai Kinerja Proyek:** .................... / 100

---

## E. RANGKUMAN MATERI BAB III

1. **Sensor** adalah perangkat keras peniru pancaindra manusia yang berfungsi menangkap besaran fisik dunia nyata (cahaya, jarak, gerak, suara, suhu) dan mengubahnya menjadi sinyal data digital bagi komputer.
2. Ragam sensor utama di sekitar kita meliputi: **Sensor Cahaya LDR** (meniru mata untuk mendeteksi gelap/terang), **Sensor Ultrasonik** (meniru sonar kelelawar untuk mengukur jarak benda), **Sensor Gerak PIR** (mendeteksi hawa hangat tubuh bergerak), dan **Kamera Vision AI** (mengenali objek dan pola).
3. Siklus kerja sistem otomatis cerdas selalu berurutan: **Masukan (*Input*)** dari sensor -> **Pemrosesan (*Process*)** oleh koding kecerdasan buatan -> **Keluaran (*Output*)** berupa aksi nyata komponen aktuator (motor listrik, suara, atau layar).
4. Kecerdasan artifisial dapat dimanfaatkan untuk tujuan kemanusiaan dan inklusivitas (*AI for Good*), seperti kacamata pintar bersuara bagi tunanetra dan aplikasi penerjemah audio ke teks langsung bagi sahabat tunarungu di kelas inklusi.
5. Prinsip **Kendali Manusia (*Human Oversight*)** dan keberadaan tombol darurat (*Emergency Stop*) adalah keharusan mutlak dalam setiap sistem otomatis karena keselamatan manusia selalu menjadi prioritas tertinggi.

---

## F. TES FORMATIF (UJI PEMAHAMAN HOTS)

### Bagian 1: Pilihan Ganda (Pilihlah Jawaban A, B, C, atau D yang Paling Tepat!)

1. Komponen elektronik yang bertugas menangkap rangsangan fisik dari alam sekitar (seperti perubahan suhu, jarak, dan intensitas cahaya) lalu mengubahnya menjadi data digital untuk komputer disebut...  
   A. Flashdisk  
   B. Sensor  
   C. Keyboard  
   D. Monitor  

2. Di sebuah kota cerdas, seluruh lampu penerangan jalan umum menyala serentak secara otomatis begitu langit petang mulai gelap gulita tanpa perlu ada petugas yang menekan saklar manual. Jenis sensor yang dipasang pada tiang-tiang lampu tersebut adalah...  
   A. Sensor Sidik Jari  
   B. Sensor Sentuhan Kapasitif  
   C. Sensor Cahaya (LDR)  
   D. Sensor Pengukur Berat Badan  

3. Sensor ultrasonik mengukur jarak benda di depannya dengan cara memancarkan gelombang suara frekuensi tinggi lalu menghitung waktu pantulannya. Prinsip kerja sensor ini meniru kemampuan alami hewan...  
   A. Katak dan Ikan Mas  
   B. Kucing dan Harimau  
   C. Kelelawar dan Lumba-lumba  
   D. Kupu-kupu dan Cacing Tanah  

4. Perhatikan alur kerja sistem berikut:  
   *Tahap 1: Kamera mendeteksi wajah murid pada jarak 1 meter.*  
   *Tahap 2: Komputer mencocokkan wajah dengan basis data sekolah.*  
   *Tahap 3: Pintu gerbang otomatis terbuka dan speaker berkata "Selamat Pagi, Erik!".*  
   Komponen yang berperan sebagai **MASUKAN (*Input*)** dan **KELUARAN (*Output*)** berturut-turut adalah...  
   A. Kamera dan Pintu Gerbang/Speaker  
   B. Komputer dan Kamera  
   C. Pintu Gerbang dan Layar Monitor  
   D. Wajah Murid dan Kabel Listrik  

5. Sebuah robot pembersih lantai otomatis menabrak lemari kaca berulang kali dan tidak mau berbelok arah. Setelah diperiksa oleh teknisi, ternyata kaca pemancar pada sensor ultrasoniknya tertutup oleh debu tebal dan stiker mainan. Kejadian ini membuktikan bahwa...  
   A. Komputer robot sedang marah dan ingin mogok kerja  
   B. Gangguan kebersihan fisik pada sensor dapat membuat komputer salah menerima data lingkungan  
   C. Robot pembersih lantai harus diganti dengan sapu lidi manual  
   D. Sensor tidak memiliki hubungan dengan pergerakan motor robot  

6. Sahabat kita penyandang disabilitas tunanetra dapat berjalan menyeberang jalan raya secara lebih mandiri dengan bantuan kacamata cerdas. Cara kerja utama dari kacamata cerdas tersebut adalah...  
   A. Memancarkan sinar laser panas untuk menghancurkan rintangan di jalan  
   B. Kamera AI membaca situasi rambu dan jarak kendaraan lalu membisikkan instruksi suara lewat earphone pengguna  
   C. Menarik tangan pengguna secara paksa menggunakan tali magnet  
   D. Menghentikan seluruh arus lalu lintas kendaraan di kota  

7. Di kelas inklusi SD Nusantara, seorang murid penyandang tunarungu dapat mengikuti penjelasan materi pelajaran guru dengan sangat baik melalui aplikasi *Live Transcribe*. Teknologi kecerdasan artifisial yang bekerja pada aplikasi tersebut adalah...  
   A. Pengenalan Wajah Tiga Dimensi (*3D Face Recognition*)  
   B. Pengubah Suara Menjadi Teks (*Speech-to-Text Recognition*)  
   C. Perancang Animasi Tiga Dimensi  
   D. Pemindai Barcode Belanjaan  

8. Mengapa pada setiap mobil listrik otonom canggih yang dapat menyetir sendiri tetap wajib dipasang setir manual dan pedal rem fisik untuk pengemudi manusia?  
   A. Hanya sebagai hiasan agar mobil tampak antik  
   B. Supaya harga jual mobil menjadi jauh lebih mahal  
   C. Untuk memastikan manusia pemegang kendali tertinggi (*Human Oversight*) dapat mengambil alih stir saat sensor mengalami malfungsi darurat  
   D. Agar anak-anak kecil bisa bermain stir saat mobil berjalan  

9. Perhatikan kasus di laboratorium sains: Pak Guru memasang sensor gas di dekat tabung gas elpiji. Aturan koding yang ditanamkan adalah:  
   `Jika kadar gas > 200 ppm, maka nyalakan sirine bahaya dan buka ventilasi darurat; Jika tidak, lampu indikator hijau tetap menyala.`  
   Komponen aktuator penggerak fisik pada sistem tersebut adalah...  
   A. Udara di dalam ruangan  
   B. Tabung gas elpiji  
   C. Sirine bahaya dan motor penggerak ventilasi darurat  
   D. Buku catatan panduan praktikum  

10. Sikap etika seorang ilmuwan koding dan robotika yang bertanggung jawab terhadap sistem otomatis buatannya tercermin pada pernyataan...  
    A. Menjual alat otomatis tanpa melakukan uji coba keselamatan terlebih dahulu  
    B. Memasang tombol darurat (*Emergency Stop*), menguji ketahanan sensor berulang kali, dan mengutamakan keselamatan pengguna  
    C. Menyalahkan pengguna jika alat pintarnya menabrak dan melukai orang  
    D. Merahasiakan cara mematikan robot agar orang lain ketakutan  

---

### Bagian 2: Soal Uraian Bernalar Kritis (Jawablah dengan Lengkap dan Jelas!)

1. Jelaskan bagaimana sensor diibaratkan sebagai jendela atau indera buatan bagi komputer! Sebutkan 3 pasang perbandingan antara organ pancaindra manusia dengan sensor elektronik komputer!
2. Gambarkan dan jelaskan dengan kata-katamu sendiri siklus 3 langkah kerja sistem otomatis cerdas (*Input -> Proses -> Output*) pada sistem palang pintu parkir otomatis yang membaca pelat nomor kendaraan!
3. Mengapa pemanfaatan sensor otomatis pada tempat wudhu sekolah atau wastafel toilet dinilai sangat mendukung gerakan pelestarian lingkungan (*Green School*) dan kesehatan murid?
4. Uraikan sebuah contoh nyata bagaimana kecerdasan artifisial dan teknologi sensor dapat membantu seorang anak penyandang disabilitas di sekolah agar dapat belajar bersama teman-temannya secara setara dan menyenangkan!
5. Jelaskan mengapa keberadaan tombol darurat (*Emergency Stop*) dan kendali pengawasan manusia (*Human Oversight*) merupakan syarat mutlak yang tidak boleh dihilangkan pada sistem robotika canggih masa kini!

---

## G. KUNCI JAWABAN & PEMBAHASAN TES FORMATIF BAB III

### Kunci Jawaban Pilihan Ganda:
1. **B** (Sensor: peranti penangkap besaran fisik dunia nyata menjadi sinyal data komputer).
2. **C** (Sensor Cahaya LDR: mendeteksi intensitas terang-gelap untuk otomasi lampu jalan).
3. **C** (Kelelawar dan lumba-lumba yang memanfaatkan gelombang pantulan suara/sonar).
4. **A** (Masukan = Kamera Vision AI; Keluaran = Pintu gerbang terbuka dan suara speaker).
5. **B** (Sensor yang terhalang kotoran fisik akan mengirim data cacat sehingga aksi komputer keliru).
6. **B** (Kamera AI mengidentifikasi objek lalu menarasikannya lewat suara ramah kepada tunanetra).
7. **B** (Speech-to-Text: mengubah gelombang vokal suara guru menjadi tulisan teks huruf berjalan).
8. **C** (Prinsip Human Oversight: manusia adalah penentu keselamatan tertinggi saat situasi darurat).
9. **C** (Aktuator adalah komponen fisik yang merespon keputusan: sirine dan motor pembuka ventilasi).
10. **B** (Integritas etika rekayasa teknologi: mengutamakan keselamatan, uji coba ketat, dan tombol darurat).

### Pedoman Pembahasan Soal Uraian:
1. **Sensor sebagai Jendela Komputer:** Tanpa sensor, komputer terisolasi. Sensor mengubah getaran fisik menjadi sinyal biner. Perbandingan:
   * Mata manusia <-> Sensor Cahaya (LDR) / Kamera Cerdas.
   * Telinga manusia <-> Sensor Suara Mikrofon / Sensor Ultrasonik.
   * Kulit peraba manusia <-> Sensor Sentuh Kapasitif / Sensor Suhu Termokopel.
2. **Siklus Palang Parkir:**
   * *Input:* Kamera AI memotret pelat kendaraan yang mendekat.
   * *Proses:* Komputer memproses gambar pelat nomor dan memeriksa masa aktif tiket langganan di database.
   * *Output:* Motor servo memutar palang pintu ke atas dan layar menampilkan pesan *"Selamat Datang"*.
3. **Manfaat Wastafel Sensor:** Mencegah pemborosan air (air langsung berhenti saat tangan ditarik, tidak ada kran lupa dimatikan) serta menjaga kebersihan/higiene karena tangan tidak perlu menyentuh gagang kran yang penuh kuman.
4. **AI for Inclusivity:** Contoh: Kacamata cerdas dengan audio visual AI membantu murid tunanetra membaca buku teks cetak secara mandiri karena kamera membaca teks buku dan membacakannya ke telinga murid secara lancar.
5. **Urgensi Emergency Stop:** Komputer dan sensor adalah buatan manusia yang rentan mengalami *bug*, korsleting, atau kesalahan prediksi data tak terduga (*unexpected glitch*). Manusia memiliki akal sehat, empati moral, dan naluri keselamatan sehingga kendali pemutus daya (*kill switch*) wajib berada di tangan manusia untuk mencegah kecelakaan fatal.

---

## H. POJOK DISKUSI BERSAMA AYAH DAN BUNDA DI RUMAH

Halo Ayah dan Bunda! Minggu ini ananda telah mempelajari teknologi masa depan yang sangat menarik: sensor dan sistem otomasi pintar, serta etika keselamatan teknologi.

Yuk, jadikan ruang keluarga sebagai laboratorium penjelajah teknologi:
1. Ajak ananda berkeliling di dalam rumah atau lingkungan sekitar (misalnya saat berkunjung ke pusat perbelanjaan): *"Ayo kita cari, di manakah ada perangkat otomatis yang menggunakan sensor?"* (seperti termometer tembak dahi, dispenser air otomatis, lampu sensor gerak, atau sensor parkir mobil keluarga).
2. Diskusikan dengan ananda: *"Mengapa kita harus bersyukur atas kesempurnaan pancaindra yang Tuhan anugerahkan, dan bagaimana kita dapat memanfaatkan kepintaran koding untuk menolong sesama yang memiliki keterbatasan fisik?"*.
3. Berikan ruang apresiasi bagi ananda untuk menceritakan ide poster "Alat Pintar Sekolah Masa Depan" yang dirancangnya di sekolah.

---

## I. JURNAL REFLEKSIKU & LENCANA MEDALI BINTANG KODER

Salinlah tabel jurnal refleksi ini ke buku catatan kodingmu dan berikan tanda centang (✓) sesuai dengan perasaan jujurmu hari ini:

| No | Pernyataan Refleksi Pembelajaran | Sangat Paham 😊 | Cukup Paham 😐 | Perlu Belajar Lagi 😢 |
|:---:|:---|:---:|:---:|:---:|
| 1 | Saya memahami fungsi sensor sebagai indera buatan komputer. | [ ] | [ ] | [ ] |
| 2 | Saya dapat membedakan 4 sensor utama (LDR, Ultrasonik, PIR, Kamera AI). | [ ] | [ ] | [ ] |
| 3 | Saya memahami siklus kerja sistem otomatis: Input -> Proses -> Output. | [ ] | [ ] | [ ] |
| 4 | Saya menyadari pentingnya AI ramah disabilitas (*AI for Inclusivity*). | [ ] | [ ] | [ ] |
| 5 | Saya paham mengapa kendali manusia dan tombol darurat wajib ada pada robot. | [ ] | [ ] | [ ] |

**Lencana Pencapaian Bab III:**  
Selamat! Kalian resmi meraih:  
🎖️ **LENCANA MEDALI PENJELAJAH SENSOR & OTOMASI CERDAS (FASE C)** 🎖️  
*"Gunakan kecerdasan teknologi bukan untuk menguasai dunia, melainkan untuk melayani dan memuliakan harkat sesama manusia!"*
"""
