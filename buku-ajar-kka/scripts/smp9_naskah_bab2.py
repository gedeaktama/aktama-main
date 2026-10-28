# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 2 Buku Siswa KKA Kelas 9 SMP (Fase D)
BAB II: PENGOLAHAN & VISUALISASI DATA UNTUK SOLUSI MASALAH SOSIAL (14 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_2_SMP9 = """# BAB II PENGOLAHAN & VISUALISASI DATA UNTUK SOLUSI MASALAH SOSIAL

## MISI 2: DATA STORYTELLER & PENGGERAK PERUBAHAN
* **Alokasi Waktu:** 14 Jam Pelajaran (7 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Berpikir Komputasional (BK) & Literasi Digital (LD)
* **Target Lencana Koder:** Medali Emas Data Storyteller Nusantara (Fase D)

---

## A. PENDAHULUAN: DETEKTIF DATA MENGUNGKAP MISTERI KEBIASAAN SARAPAN

Jam dinding di ruang guru menunjukkan pukul 11.00 siang. Ibu Rina, guru Bimbingan dan Konseling (BK) SMP Nusantara, tampak sedang berbincang serius dengan kepala sekolah. Dalam seminggu terakhir, catatan absensi mencatat ada puluhan siswa yang mengeluh pusing dan tertidur di meja kelas saat jam pelajaran ketiga berlangsung.

"Banyak guru menduga anak-anak terlalu sering begadang bermain game daring di ponsel mereka," tutur Ibu Rina prihatin saat Ayu, Rian, dan Fajar kebetulan sedang berada di ruang konseling untuk mengembalikan lembar kuesioner OSIS.

[[IMAGE: bab2_komik_pembuka_smp9.png | Gambar 2.1: Komik Pembuka Bab 2: Detektif Data Mengungkap Misteri Kebiasaan Sarapan dan Konsentrasi Belajar]]

Ayu mengangkat tangannya dengan sopan. "Ibu Rina, bolehkah tim koding dan literasi digital kami membantu menyelidiki masalah ini secara ilmiah? Kita tidak boleh menyimpulkan penyebab masalah hanya berdasarkan dugaan atau prasangka tanpa bukti!"

"Bagaimana cara kalian membuktikannya, Ayu?" tanya Kepala Sekolah tertarik.

Rian melangkah maju dengan percaya diri. "Kami akan bertindak sebagai **Detektif Data Sosial**! Kami akan merancang instrumen kuesioner digital anonim yang disebarkan kepada 150 siswa dari kelas VII hingga kelas IX. Kami akan mengumpulkan data jam tidur malam, kebiasaan menu sarapan pagi, jumlah gelas air putih yang diminum, serta tingkat konsentrasi belajar mereka di kelas!"

Fajar menambahkan, "Setelah data terkumpul, kami akan membersihkannya, mengolahnya menggunakan rumus statistik pada aplikasi spreadsheet, dan menyajikan hasilnya dalam bentuk grafik **Data Storytelling** yang memukau. Dengan data yang valid, pihak sekolah bisa mengambil keputusan yang tepat untuk membantu teman-teman kita!"

Kepala sekolah mengangguk kagum dan memberikan izin penuh. Petualangan sains data sosial dimulai!

---

## B. SIKLUS LENGKAP ANALISIS DATA: DARI MASALAH LAPANGAN MENUJU REKOMENDASI

Dalam sains komputasi dan analisis kebijakan modern, data dipandang sebagai "emas hitam baru" (*the new oil*). Namun tumpukan angka mentah tidak ada gunanya jika tidak diolah secara terstruktur. Para ilmuwan data mengikuti **Lima Langkah Siklus Analisis Data**:

[[IMAGE: bab2_siklus_analisis_data_sosial.png | Gambar 2.2: Siklus Lengkap Analisis Data Kuantitatif: Dari Masalah Lapangan Menuju Aksi Nyata]]

### Lima Tahapan Siklus Sains Data:
1. **Perumusan Masalah & Hipotesis Kunci (*Problem Formulation*):**  
   Menentukan pertanyaan pemantik yang ingin dijawab. Contoh hipotesis: *"Siswa yang mengonsumsi sarapan berprotein memiliki tingkat fokus belajar 30% lebih tinggi dibandingkan siswa yang melewatkan sarapan pagi."*
2. **Pengumpulan Data Lapangan (*Data Collection*):**  
   Menyusun instrumen survei digital terstandar yang menjamin kejujuran jawaban responden tanpa tekanan.
3. **Pembersihan Data (*Data Cleaning*):**  
   Memeriksa lembar kerja data mentah untuk membuang isian yang tidak wajar (misalnya responden yang mengisi jam tidur 25 jam sehari), menghapus data ganda (*duplicate rows*), dan merapikan format teks.
4. **Analisis Statistik Komputasional (*Exploratory Data Analysis*):**  
   Menerapkan rumus matematika spreadsheet (seperti `AVERAGE`, `COUNTIF`, `MAX`, `MIN`) untuk menemukan pola korelasi tersembunyi antar variabel.
5. **Narasi Visual & Rekomendasi Kebijakan (*Data Storytelling & Action*):**  
   Mengubah tabel angka yang membosankan menjadi grafik berwarna interaktif disertai rekomendasi konkret bagi pimpinan sekolah.

---

## C. MERANCANG SURVEI KUESIONER DIGITAL YANG ETIS

Sebuah analisis data yang akurat berawal dari instrumen kuesioner yang dirancang dengan baik. Jika pertanyaan kuesioner ambigu, membingungkan, atau bernada menghakimi, data yang terkumpul pasti akan bias dan tidak mencerminkan kenyataan.

### Prinsip Merancang Formulir Digital (Google Forms / MS Forms):
1. **Gunakan Pertanyaan Tertutup (*Closed-Ended Questions*):**  
   Hindari terlalu banyak pertanyaan esai terbuka yang panjang karena sulit diolah secara kuantitatif. Gunakan opsi pilihan ganda (*multiple choice*) atau kotak centang (*checkboxes*).
2. **Terapkan Skala Sikap Likert (1 - 5):**  
   Untuk mengukur perasaan atau tingkat konsentrasi subjektif, gunakan skala angka:  
   * 1 = Sangat Tidak Fokus  
   * 2 = Kurang Fokus  
   * 3 = Cukup Fokus  
   * 4 = Fokus  
   * 5 = Sangat Fokus Penuh  
3. **Bahasa Ramah Remaja dan Netral:**  
   Hindari pertanyaan yang mengarahkan jawaban (*leading questions*).  
   * *Contoh Salah (Mengarahkan):* *"Apakah kamu setuju bahwa kantin sekolah menjual makanan yang tidak sehat?"*  
   * *Contoh Benar (Netral):* *"Seberapa sering kamu membeli sarapan di kantin sekolah dalam seminggu terakhir?"*

---

## D. OLAH DATA KUANTITATIF DENGAN RUMUS SPREADSHEET

Setelah survei ditutup dan terkumpul 150 tanggapan, data mentah otomatis tersimpan di dalam lembar kerja digital (*Spreadsheet*). Untuk membedah pola data ini, kita tidak perlu menghitung manual menggunakan kalkulator genggam satu per satu!

### Lima Rumus Sakti Spreadsheet untuk Analisis Data:
1. **=AVERAGE(Rentang_Sel):** Menghitung nilai rata-rata dari sekelompok angka.  
   * Contoh: `=AVERAGE(D2:D151)` -> Menghitung rata-rata jam tidur malam seluruh siswa.
2. **=COUNTIF(Rentang_Sel; "Kriteria"):** Menghitung berapa banyak baris yang memenuhi syarat tertentu.  
   * Contoh: `=COUNTIF(E2:E151; "Tidak Sarapan")` -> Menghitung berapa orang siswa yang sama sekali tidak sarapan pagi.
3. **=SUM(Rentang_Sel):** Menjumlahkan seluruh total angka pada sebuah kolom.  
   * Contoh: `=SUM(F2:F151)` -> Menghitung total porsi air putih yang diminum seluruh responden.
4. **=MAX(Rentang_Sel) & =MIN(Rentang_Sel):** Menemukan nilai tertinggi dan nilai terendah dalam dataset.
5. **Penyaringan Cerdas (*Filter Data*):** Fitur untuk menampilkan hanya kelompok tertentu, misalnya: menyaring siswa yang memiliki skor fokus < 3 untuk melihat menu sarapan apa yang paling banyak mereka konsumsi.

---

## E. SENI NARASI VISUAL (DATA STORYTELLING): MEMILIH GRAFIK YANG TEPAT

Pernahkah kalian melihat seseorang mempresentasikan data survei dengan menampilkan tabel berisi 500 angka kecil-kecil di layar proyektor? Seluruh audiens di ruangan pasti akan menguap bosan dan tidak memahami intisari pesan yang disampaikan!

Inilah mengapa seorang ilmuwan komputasi wajib menguasai seni **Data Storytelling**: menyajikan data angka dalam bentuk grafik visual yang memikat dan mudah dipahami dalam sekali pandang.

[[IMAGE: bab2_panduan_pemilihan_grafik_data.png | Gambar 2.3: Panduan Pemilihan Grafik: Memilih Visual yang Tepat untuk Audiens]]

### Tiga Jenis Grafik Utama dan Panduan Penggunaannya:
1. **Diagram Batang (*Bar / Column Chart*):**  
   * *Fungsi Terbaik:* Membandingkan jumlah kuantitas antar kategori yang berbeda.  
   * *Contoh Tepat:* Membandingkan jumlah siswa yang sarapan roti, nasi uduk, bubur, atau tidak sarapan sama sekali.
2. **Diagram Garis (*Line Chart*):**  
   * *Fungsi Terbaik:* Menampilkan tren fluktuasi perubahan nilai dari waktu ke waktu (*continuous time-series*).  
   * *Contoh Tepat:* Memperlihatkan grafik penurunan tingkat rasa kantuk siswa dari jam pelajaran ke-1 (pukul 07.30) hingga jam ke-6 (pukul 13.00).
3. **Diagram Lingkaran (*Pie Chart*):**  
   * *Fungsi Terbaik:* Menampilkan proporsi bagian dari sebuah total kesatuan utuh (100%).  
   * *Peringatan Desain:* Hanya gunakan jika kategori tidak lebih dari 5 potong! Jika potongannya ada 15 buah, diagram lingkaran akan tampak seperti roda yang semrawut dan sulit dibedakan warnanya.

---

## F. ETIKA PRIVASI DATA: DE-IDENTIFIKASI & ANONIMITAS RESPONDEN

Dalam era digital saat ini, data pribadi warga negara dilindungi secara ketat oleh hukum negara melalui **Undang-Undang Perlindungan Data Pribadi (UU No. 27 Tahun 2022 / UU PDP)**.

[[IMAGE: bab2_infografis_deidentifikasi_data.png | Gambar 2.4: Etika Privasi Riset: De-identifikasi dan Anonimitas Responden Survei]]

### Kewajiban Moral Peneliti: De-identifikasi Data
Ketika kalian membagikan kuesioner survei di lingkungan sekolah atau masyarakat, responden bersedia menjawab jujur karena percaya bahwa identitas mereka tidak akan disalahgunakan atau dipermalukan di depan umum.

Sebelum lembar data survei dipublikasikan atau ditunjukkan ke pihak lain, kalian **WAJIB** melakukan proses **De-identifikasi Data**:
1. **Hapus Kolom Identitas Langsung:** Hapus permanen kolom nama lengkap, nomor induk siswa (NIS), alamat rumah, dan nomor telepon seluler.
2. **Gunakan Kode Anonim (*Pseudonymization*):** Ganti nama responden dengan nomor urut acak, misalnya: `Responden_#001`, `Responden_#002`.
3. **Sajikan Data Agregat:** Jangan mempublikasikan catatan perorangan; sajikan kesimpulan dalam bentuk persentase kelompok (misal: *"82% siswa kelas IX sarapan dengan menu seimbang"*).

---

## G. LKPD PLUGGED 2.1: PROYEK MINI SURVEI GAYA HIDUP SISWA & DASHBOARD VISUAL

### Aktivitas Kolaboratif Sains Data (Plugged Activity)
* **Tema Riset:** *"Hubungan Pola Sarapan, Kualitas Tidur, dan Konsentrasi Belajar Siswa SMP"*
* **Target Data:** Minimal 30 Responden dari teman sebaya di sekolah.
* **Alat:** Google Forms / Microsoft Forms dan Aplikasi Spreadsheet (Google Sheets / Excel).
* **Durasi Pengerjaan:** 4 JP (2 Pertemuan Praktik Terbimbing).

### Panduan Alur Kerja Tim:
1. **Pembuatan Kuesioner Digital:**
   * Susun 5 pertanyaan terstruktur:
     1. Kelas / Tingkat (Pilihan Ganda: VII, VIII, IX)
     2. Rata-rata jam tidur malam (Angka: misal 6, 7, 8 jam)
     3. Apakah sarapan sebelum berangkat sekolah? (Ya / Kadang-kadang / Tidak Pernah)
     4. Jenis sarapan dominan (Karbohidrat murni / Karbohidrat + Protein / Susu saja / Tidak ada)
     5. Skor fokus belajar di jam ke-3 (Skala Likert 1-5)
2. **Pengolahan Rumus Spreadsheet:**
   * Impor tanggapan ke spreadsheet. Lakukan de-identifikasi data.
   * Buat tabel rekapitulasi menggunakan rumus:
     * `=AVERAGE(...)` untuk rata-rata jam tidur.
     * `=COUNTIF(...)` untuk menghitung jumlah siswa per kategori sarapan.
3. **Pembuatan Grafik Narasi (*Data Storytelling*):**
   * Buat satu Diagram Batang yang membandingkan rata-rata skor fokus belajar antara kelompok siswa yang sarapan vs kelompok yang tidak sarapan.
   * Tambahkan judul grafik yang persuasif: *"Siswa yang Sarapan Protein Terbukti Memiliki Fokus Belajar 40% Lebih Tinggi!"*
4. **Penyusunan Rekomendasi Solusi:**
   * Tuliskan selembar surat rekomendasi santun kepada pihak pengelola kantin dan sekolah mengenai pentingnya menyediakan paket sarapan sehat terjangkau di pagi hari.

---

## POJOK KARAKTER & ETIKA KODER: INTEGRITAS ILMIAH MELAWAN MANIPULASI SKALA GRAFIK

Dalam dunia jurnalisme data dan politik, sering kali ada oknum tidak bertanggung jawab yang sengaja memotong titik nol sumbu vertikal (*truncated graph axis*) pada grafik batang untuk membuat perbedaan angka yang kecil terlihat sangat drastis dan menakutkan masyarakat demi kepentingan tertentu!

Sebagai koder dan analis data yang berintegritas tinggi, tolaklah segala bentuk manipulasi grafik yang menyesatkan pembaca! Integritas ilmiah menuntut kita untuk selalu menyajikan data apa adanya secara jujur, adil, dan transparan. Kejujuran data adalah fondasi utama dari kepercayaan publik dan pengambilan keputusan yang adil bagi seluruh lapisan masyarakat!

---

## RANGKUMAN MATERI BAB 2

1. **Siklus Analisis Data** mencakup lima tahapan sistematis: Perumusan masalah -> Pengumpulan survei digital -> Pembersihan data (*cleaning*) -> Analisis rumus statistik -> Penyajian narasi visual (*data storytelling*).
2. **Kuesioner Digital yang Baik** memanfaatkan pertanyaan tertutup, skala sikap Likert (1-5), serta bahasa yang netral tanpa menggiring opini responden.
3. **Rumus Spreadsheet Esensial:** `AVERAGE` untuk nilai tengah, `COUNTIF` untuk pencacahan bersyarat, `SUM` untuk akumulasi, serta `MAX`/`MIN` untuk nilai batas ekstrem.
4. **Data Storytelling** memilih grafik visual yang tepat: Diagram Batang untuk komparasi kategori, Diagram Garis untuk tren waktu, dan Diagram Lingkaran untuk proporsi dari 100%.
5. **De-identifikasi Data** adalah kewajiban etika dan hukum (UU PDP No. 27/2022) untuk menghapus data pribadi sensitif dan menjamin anonimitas mutlak responden riset.

---

## UJI PEMAHAMAN HOTS BAB 2

### I. Pilihan Ganda (Pilihlah Jawaban yang Paling Tepat!)

1. Tahapan dalam siklus sains data yang bertujuan membuang data duplikat, memperbaiki format teks yang keliru, dan mengeliminasi angka pencilan yang tidak masuk akal disebut...
   A. Data Mining  
   B. Data Cleaning (Pembersihan Data)  
   C. Data Warehousing  
   D. Data Encryption  

2. Fajar ingin menghitung berapa banyak siswa di kolom C (dari baris 2 hingga 100) yang memilih opsi menu "Nasi Kuning" pada kuesioner kantin. Rumus spreadsheet yang benar adalah...
   A. `=SUM(C2:C100; "Nasi Kuning")`  
   B. `=AVERAGE(C2:C100; "Nasi Kuning")`  
   C. `=COUNTIF(C2:C100; "Nasi Kuning")`  
   D. `=MAX(C2:C100; "Nasi Kuning")`  

3. Jenis grafik yang paling tepat digunakan untuk menggambarkan data penurunan suhu udara laboratorium komputer dari pukul 07.00 pagi hingga pukul 16.00 sore adalah...
   A. Diagram Lingkaran (Pie Chart)  
   B. Diagram Garis (Line Chart)  
   C. Diagram Radar  
   D. Diagram Donat  

4. Mengapa seorang analis data dilarang menggunakan diagram lingkaran (*pie chart*) jika kategori pilihan jawaban berjumlah lebih dari 10 kategori berbeda?
   A. Karena software spreadsheet akan langsung rusak  
   B. Karena irisan juring lingkaran akan menjadi sangat tipis dan sulit dibedakan warnanya oleh mata audiens  
   C. Karena diagram lingkaran hanya boleh digunakan untuk data mata pelajaran matematika  
   D. Karena ukuran file gambar akan melebihi batas memori komputer  

5. Perhatikan grafik batang yang dipresentasikan seorang siswa: Sumbu Y dimulai dari angka 80 (bukan dari angka 0), sehingga perbedaan nilai antara kelas 85 dan 88 terlihat sangat jomplang seperti sepuluh kali lipat. Kesalahan etika visual ini dinamakan...
   A. Clean Code  
   B. Truncated Graph (Grafik dengan Sumbu Terpotong yang Menyesatkan)  
   C. Data Science  
   D. Pie Chart Slicing  

6. Menghapus nama lengkap, nomor induk siswa, dan nomor telepon seluler responden dari lembar data survei sebelum dianalisis merupakan penerapan prinsip...
   A. De-identifikasi Data (Anonimitas Privasi)  
   B. Digital Watermarking  
   C. Machine Learning  
   D. Cloud Computing  

7. Undang-undang resmi di Republik Indonesia yang mengatur perlindungan data pribadi dan sanksi hukum atas kebocoran data digital adalah...
   A. UU Hak Cipta No. 28 Tahun 2014  
   B. UU Perlindungan Data Pribadi (UU No. 27 Tahun 2022)  
   C. UU Guru dan Dosen No. 14 Tahun 2005  
   D. UU Perbankan Nasional  

8. Ayu mengukur tingkat kepuasan siswa terhadap fasilitas komputer sekolah menggunakan pilihan: Sangat Tidak Puas (1), Tidak Puas (2), Ragu-ragu (3), Puas (4), dan Sangat Puas (5). Skala pengukuran ini dalam metodologi penelitian disebut...
   A. Skala Richter  
   B. Skala Kelvin  
   C. Skala Likert  
   D. Skala Beaufort  

9. Apa keuntungan utama menyajikan hasil survei dalam bentuk *Data Storytelling* dibanding hanya menampilkan tabel angka mentah?
   A. Penonton dapat langsung menangkap intisari pola data dan terdorong melakukan aksi nyata pemecahan masalah  
   B. Ukuran kertas presentasi menjadi dua kali lipat lebih besar  
   C. Menghilangkan kebutuhan untuk melakukan analisis matematika  
   D. Presentasi tidak memerlukan sambungan aliran listrik proyektor  

10. Manakah di antara pertanyaan survei berikut yang memenuhi kaidah pertanyaan netral dan tidak menggiring opini responden?
    A. "Bukankah pelajaran koding adalah pelajaran paling menyenangkan di sekolah kita?"  
    B. "Berapa jam waktu yang kamu luangkan untuk belajar mandiri di rumah setiap hari?"  
    C. "Mengapa kamu sangat malas mengerjakan PR komputer?"  
    D. "Setujukah kamu bahwa game online merusak otak remaja?"  

---

### II. Uraian Pemecahan Masalah (Jawablah Secara Rinci dan Terstruktur!)

1. Jelaskan lima tahapan dalam Siklus Analisis Data secara runtut! Mengapa tahapan *Pembersihan Data (Data Cleaning)* wajib dilakukan sebelum data dianalisis dengan rumus matematika?
2. Sebutkan dan jelaskan fungsi dari tiga rumus spreadsheet: `AVERAGE`, `COUNTIF`, dan `MAX`! Berikan contoh sintaks penggunaannya pada tabel data hasil survei sekolah!
3. Anda diminta mempresentasikan hasil survei mengenai *"Pilihan Minat Ekstrakurikuler Siswa Kelas VII-IX"*. Tentukan jenis grafik apa yang paling tepat untuk menyajikan data tersebut dan kemukakan alasan desainnya!
4. Mengapa proses *De-identifikasi Data* menjadi kewajiban mutlak bagi seorang peneliti muda sebelum mempublikasikan hasil surveinya? Jelaskan dampaknya terhadap kepatuhan regulasi UU Perlindungan Data Pribadi (UU PDP)!
5. Bagaimana seorang analis data menjaga integritas moral ilmiahnya agar tidak memanipulasi tampilan grafik demi memenangkan suatu argumen kelompok yang keliru?

---

## KUNCI JAWABAN UJI PEMAHAMAN TERPILIH BAB 2

### Kunci Jawaban Pilihan Ganda:
1. **B** (*Data Cleaning* adalah proses membuang data duplikat, memperbaiki galat ketik, dan menyeleksi data mentah).
2. **C** (Rumus `=COUNTIF(Rentang; Kriteria)` menghitung jumlah baris yang memenuhi kriteria teks tertentu).
3. **B** (Diagram garis paling ideal untuk memvisualisasikan data kontinu yang berubah dari waktu ke waktu).
4. **B** (Terlalu banyak juring pada pie chart membuat visual menjadi padat, membingungkan, dan sulit dibaca).
5. **B** (Grafik dengan sumbu terpotong memanipulasi persepsi visual pembaca seolah perbedaan kecil tampak sangat besar).
6. **A** (De-identifikasi melindungi privasi individu dengan menghapus data pribadi yang dapat dilacak).
7. **B** (UU PDP No. 27 Tahun 2022 adalah payung hukum resmi perlindungan data pribadi di Indonesia).
8. **C** (Skala Likert adalah skala psikometrik standar untuk mengukur sikap dan preferensi responden).
9. **A** (*Data Storytelling* menjembatani data statistik yang kaku menjadi wawasan yang bermakna bagi pengambil kebijakan).
10. **B** (Pertanyaan jam belajar bersifat objektif, netral, dan tidak memuat kata-kata yang menghakimi).
"""
