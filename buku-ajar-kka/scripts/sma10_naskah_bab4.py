"""
Modul Naskah Bab IV Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB4_SMA10 = """# BAB IV: PRODUKSI KONTEN MULTIMEDIA INTERAKTIF DAN DESAIN ANTARMUKA

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
"""
