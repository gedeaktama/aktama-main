# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 3 Buku Siswa KKA Kelas 7 SMP (Fase D)
BAB III: MENYELAMI KECERDASAN ARTIFISIAL GENERATIF (GENAI) & ETIKA KRITIS (16 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_3_SMP7 = """# BAB III MENYELAMI KECERDASAN ARTIFISIAL GENERATIF (GENAI) & ETIKA KRITIS

## MISI 3: PENYELIDIK FAKTA & ETIKA KECERDASAN ARTIFISIAL
* **Alokasi Waktu:** 16 Jam Pelajaran (8 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi dan Etika Kecerdasan Artifisial (LEKA)
* **Target Lencana Koder:** Medali Penyelidik Fakta & Etika AI (Bintang Emas Fase D)

---

## A. PENDAHULUAN: JEBAKAN HALUSINASI & DEEPFAKE AI

Pagi itu, suasana di laboratorium komputer SMP Nusantara mendadak heboh. Fajar memanggil kedua sahabatnya, Rian dan Ayu, untuk melihat layar komputernya dengan mata membelalak takjub.

"Teman-teman, cepat kemari! Lihat teknologi luar biasa ini!" seru Fajar penuh decak kagum. "Aku baru saja mencoba sebuah aplikasi kecerdasan artifisial generatif berbasis web. Aku mengetikkan satu kalimat perintah: *'Buatkan artikel sejarah lengkap tentang Kejayaan Kerajaan Majapahit'*, dan hanya dalam waktu tiga detik, komputer langsung mengetik sendiri naskah sepanjang lima halaman dengan tata bahasa yang sangat rapi dan meyakinkan!"

Ayu ikut membungkuk menatap layar monitor. "Wah, hebat sekali! Bahasanya tampak seperti tulisan seorang profesor sejarah di universitas! Tidak ada salah ketik sedikit pun!"

Namun, Rian yang memiliki ketelitian tinggi sebagai analis data membaca baris demi baris teks tersebut secara cermat. Tiba-tiba, telunjuk Rian terhenti di paragraf ketiga. Keningnya berkerut rapat.

"Tunggu dulu, Fajar! Coba kamu baca kalimat di baris ini baik-baik!" kata Rian dengan nada serius.

Fajar membaca kalimat yang ditunjuk Rian: *"Pada tahun 1355 Masehi, Raja Hayam Wuruk segera mengirimkan pesan darurat melalui sambungan telepon seluler satelit kepada Mahapatih Gajah Mada untuk memerintahkan armada laut berkumpul di pelabuhan Tuban."*

Seketika tawa Ayu meledak. "Hahaha! Telepon seluler di zaman Majapahit abad ke-14? Itu mustahil sekali! Tujuh ratus tahun yang lalu listrik saja belum ditemukan manusia, apalagi menara sinyal telepon seluler!"

Fajar tertegun dengan wajah memerah. "Lho, tapi kenapa komputernya menulis kalimat itu dengan sangat yakin dan percaya diri? Padahal kalimat sebelum dan sesudahnya adalah fakta sejarah yang benar!"

[[IMAGE: bab3_komik_pembuka_smp7.png | Gambar 3.1: Komik Inovator Remaja — Jebakan Halusinasi & Deepfake Kecerdasan Artifisial]]

"Itulah yang di dunia sains komputer dinamakan **HALUSINASI KECERDASAN ARTIFISIAL (*AI Hallucination*)**!" jelas Rian dengan lugas. "Banyak orang mengira kecerdasan artifisial adalah makhluk pintar yang tahu segalanya. Padahal kenyataannya, AI generatif tidak memiliki akal budi sejati. AI hanya mesin penebak kata statistik! Jika kita tidak bersikap kritis, kita bisa terjerumus menyebarkan berita palsu!"

"Tidak hanya itu," tambah Ayu dengan mimik serius. "Kemarin pamanku hampir kehilangan uang tabungan karena menerima panggilan telepon video dari seseorang yang wajah dan suaranya persis kepala desa kami, padahal itu adalah rekayasa video palsu **DEEPFAKE** buatan AI!"

Fajar menghela napas panjang dan menyadari betapa pentingnya ilmu etika teknologi. "Ternyata kecerdasan buatan menyimpan jebakan yang sangat berbahaya jika kita menelannya mentah-mentah! Yuk, kita selidiki rahasia di balik dapur kerja AI dan cara membedah kebenarannya!"

> **Pertanyaan Pemantik Kritis:**
> 1. Mengapa sebuah program komputer yang sangat canggih bisa mengarang cerita fiktif yang salah total dengan gaya bahasa yang begitu percaya diri?
> 2. Bagaimana sebuah model bahasa kecerdasan artifisial dapat dilatih membaca miliaran teks internet namun tetap tidak memahami makna kebenaran yang sesungguhnya?
> 3. Apa yang membedakan integritas berpikir seorang pelajar sejati dengan seseorang yang hanya mengandalkan salin-tempel (*copy-paste*) jawaban dari kecerdasan artifisial? Mari kita bedah bersama!

---

## B. KONSEP DAN MATERI PEMBELAJARAN

### 1. Apa Itu AI Generatif? Dari Meniru Pola Menjadi Pencipta Konten

Pada jenjang Sekolah Dasar, kalian telah mempelajari **AI Diskriminatif / Klasifikasi (*Classification AI*)**, yaitu sistem cerdas yang bertugas memilah, mengelompokkan, atau mengenali objek yang sudah ada (misalnya: membedakan foto kucing vs anjing, atau membaca pelat nomor mobil).

Namun, dalam beberapa tahun terakhir, dunia menyaksikan revolusi raksasa bernama **KECERDASAN ARTIFISIAL GENERATIF (*Generative AI / GenAI*)**. AI generatif tidak hanya mengklasifikasikan benda, melainkan memiliki kemampuan untuk **MENCIPTAKAN KONTEN BARU (*Generate New Content*)** berupa naskah teks, lukisan citra, musik orkestra, video animasi, hingga baris kode pemrograman berdasarkan instruksi masukan (*prompt*) dari manusia!

Tiga rumpun utama AI Generatif meliputi:
1. **Generator Teks (Large Language Models - LLM):** Mampu menjawab pertanyaan, menulis puisi, merangkum dokumen ilmiah, dan menerjemahkan antarbahasa manusia (contoh: ChatGPT, Google Gemini, Claude).
2. **Generator Gambar & Seni Visual (*Image Generators*):** Mengubah deskripsi teks menjadi lukisan atau foto fotorealistik dalam hitungan detik (contoh: Midjourney, DALL-E, Stable Diffusion).
3. **Generator Audio & Vokal (*Voice & Music Synthesis*):** Menghasilkan komposisi musik instrumen atau menirukan suara vokal manusia (*Voice Cloning*).

---

### 2. Di Balik Dapur Model Bahasa Besar (LLM): Penebak Kata Berikutnya

Bagaimana sebuah Model Bahasa Besar (LLM) bekerja di balik layar sirkuit komputernya? Apakah AI benar-benar 'berpikir' dan memiliki kesadaran seperti manusia? Jawabannya adalah: **TIDAK**.

Secara ilmiah, LLM bekerja menggunakan prinsip **PREDIKSI PROBABILISTIK KATA BERIKUTNYA (*Next Token Prediction*)**.

[[IMAGE: bab3_arsitektur_llm_probabilistik.png | Gambar 3.2: Di Balik Dapur Model Bahasa Besar (LLM) — Penebak Kata Berikutnya]]

Mari kita amati alur kerja pada Gambar 3.2 di atas:
1. **Membaca Miliaran Teks:** Selama masa pelatihan (*training*), AI diberi makan ratusan miliar kalimat dari buku digital, artikel Wikipedia, berita daring, dan forum internet.
2. **Memetakan Hubungan Kata (*Neural Network Weights*):** AI mencatat secara statistik kata apa saja yang paling sering muncul berdampingan dalam bahasa manusia.
3. **Menebak Token Berikutnya:** Ketika pengguna mengetikkan kalimat:  
   *"Ibu kota negara Indonesia saat ini adalah..."*  
   Komputer tidak memahami geografi atau tanah air Indonesia. Komputer hanya menghitung skor probabilitas kata berikutnya:
   * Peluang kata "Jakarta": **78%**
   * Peluang kata "Nusantara": **18%**
   * Peluang kata "Bandung": **3%**
   * Peluang kata "Bulan": **1%**
4. Komputer memilih kata dengan skor tertinggi, yaitu *"Jakarta"*, lalu proses ini diulang untuk menebak kata selanjutnya satu demi satu hingga terbentuk satu paragraf utuh!

---

### 3. Tiga Tantangan & Keterbatasan Utama AI Generatif

Karena cara kerjanya murni berbasis statistik probabilitas susunan kata dan bukan pemahaman nalar sejati, AI generatif memiliki keterbatasan kritis yang wajib diwaspadai:

[[IMAGE: bab3_infografis_keterbatasan_ai.png | Gambar 3.3: 3 Tantangan & Keterbatasan Utama Kecerdasan Artifisial Generatif]]

#### A. Fenomena Halusinasi AI (*AI Hallucination*)
Halusinasi terjadi ketika model AI menyajikan fakta palsu, angka statistik fiktif, kutipan tokoh karangan, atau judul buku ilmiah yang tidak pernah ada di dunia nyata, dengan susunan tata bahasa yang sangat meyakinkan dan percaya diri.  
*Penyebab:* AI tidak memiliki verifikator fakta (*Fact Checker*) di dalam otaknya. Target AI hanyalah menyusun kalimat yang terdengar masuk akal secara gramatikal, terlepas dari apakah isi kalimat itu benar atau salah!

#### B. Bias Algoritma (*Algorithmic Bias*)
AI adalah cerminan dari data internet yang dipelajarinya. Jika data internet di masa lalu penuh dengan prasangka sosial atau ketimpangan informasi, maka AI akan mereproduksi prasangka tersebut:
* *Contoh Bias Gender:* Ketika diminta membuat gambar dengan prompt *"Seorang dokter sedang memimpin rapat bersama perawat"*, AI generator sering kali otomatis melukiskan dokter sebagai pria dan perawat sebagai wanita.
* *Contoh Bias Budaya:* Informasi tentang sejarah lokal Nusantara sering kali kalah lengkap atau terdistorsi dibandingkan sejarah negara-negara barat, karena mayoritas data latih internet berbahasa Inggris.

#### C. Keterbatasan Data Kedaluwarsa (*Knowledge Cutoff*)
Model AI memiliki batas tanggal akhir data latih (*Cutoff Date*). AI tidak mengetahui peristiwa yang terjadi kemarin sore kecuali model tersebut telah dihubungkan secara khusus dengan mesin peramban web (*web search retrieval*).

---

### 4. Rekayasa Manipulasi Deepfake & Panduan Detektif Digital

Salah satu dampak paling berbahaya dari perkembangan AI generatif adalah teknologi **DEEPFAKE**, yaitu rekayasa media digital sintetis yang menggabungkan kecerdasan buatan untuk mengubah wajah seseorang (*Face Swap*) atau menirukan suara vokal seseorang secara identik (*Voice Cloning*).

Teknologi deepfake kerap disalahgunakan oleh penjahat siber untuk:
* Melakukan penipuan telepon darurat palsu kepada keluarga mengatasnamakan anak yang diculik atau ditahan polisi.
* Membuat video hoaks manipulasi pejabat negara seolah-olah mengumumkan kebijakan kontroversial untuk memicu kerusuhan publik.

[[IMAGE: bab3_poster_deteksi_deepfake.png | Gambar 3.4: Panduan Detektif Digital — 4 Ciri Rekayasa Video Deepfake]]

Untuk melindungi diri dan masyarakat, terapkan **4 Jurus Detektif Siber Mendeteksi Deepfake** pada Gambar 3.4:
1. **Periksa Gerakan Kedipan Mata (*Blinking Patterns*):**  
   Video deepfake buatan AI versi gratis sering kali memiliki ekspresi mata yang kaku, jarang berkedip secara alami, atau arah tatapan pupil mata tidak simetris.
2. **Sinkronisasi Gerak Bibir (*Lip-Sync Lag*):**  
   Perhatikan gerakan mulut saat mengucapkan huruf vokal (A, I, U, E, O) atau konsonan letup (B, P, M). Pada video palsu, sering terdapat keterlambatan sepersekian detik antara bentuk bibir dengan suara yang terdengar.
3. **Periksa Tepian Garis Wajah (*Edge Artifacts*):**  
   Amati perbatasan antara dagu dengan leher atau garis rambut dengan dahi. Biasanya tampak bercak buram (*blur*), warna kulit yang tidak merata, atau efek kilatan cahaya yang aneh saat kepala menoleh cepat.
4. **Anomali Detail Anggota Tubuh:**  
   AI generator sering kali kesulitan melukiskan anatomi yang rumit, seperti jumlah jari tangan yang lebih dari lima, telinga yang bentuknya tidak wajar, atau kacamata yang gagangnya melayang tanpa menempel di hidung.

---

### 5. Pojok Karakter & Etika: Integritas Akademik Siswa Abad ke-21

Kehadiran kecerdasan artifisial generatif menguji nilai kejujuran dan kemandirian moral setiap pelajar:
1. **Bahaya Ketergantungan Kognitif (*Brain Atrophy*):**  
   Jika setiap tugas esai, karangan puisi, atau pemecahan soal matematika selalu kalian serahkan bulat-bulat kepada AI untuk mengerjakannya, maka otot nalar dan daya kritis otak kalian akan melemah karena tidak pernah dilatih berpikir!
2. **Larangan Plagiarisme AI:**  
   Menyalin (*copy-paste*) teks keluaran AI lalu mengklaimnya sebagai hasil karya pikiran sendiri di hadapan guru adalah pelanggaran etika kejujuran akademik yang sangat memalukan.
3. **Posisikan AI sebagai Teman Diskusi (*Tutor*), Bukan Pengganti Diri:**  
   Gunakan AI untuk membantu mencari sudut pandang baru, mengoreksi tata bahasa tulisanmu sendiri, atau memberikan analogi konsep sains yang sulit. Namun, hasil akhir karya dan pemikiran harus tetap murni lahir dari kecerdasan nurani kalian sendiri!

> 🔍 **Jendela Fakta Sains & Teknologi:**
> Pada Konferensi Tingkat Tinggi AI Seoul 2024, para pemimpin dunia menyepakati pembentukan kerangka keselamatan global **AI Safety Institute** untuk memantau risiko model AI super canggih agar tidak disalahgunakan untuk perang siber atau penyebaran disinformasi massal!

---

## C. PROSES DAN AKTIVITAS BELAJAR (AYO MENCOBA)

### Aktivitas Detektif: Komparasi Kritis Teks AI vs Ensiklopedia Sejarah

Mari kita uji ketajaman analisismu dalam melacak halusinasi data kecerdasan artifisial!

**Langkah Eksperimen di Laboratorium:**
1. Masuklah ke platform AI edukasi terkurasi di bawah bimbingan guru.
2. Ketikkan prompt uji sejarah lokal Indonesia berikut:  
   *"Jelaskan peran tokoh pahlawan I Gusti Ngurah Rai dalam pertempuran Puputan Margarana di Bali, sebutkan tanggal peristiwa, jumlah pasukan, dan nama benteng pertahanannya!"*
3. Salin teks jawaban yang dihasilkan oleh AI ke dokumen kerjamu.
4. Bukalah buku teks resmi Sejarah Indonesia dari Kementerian Pendidikan Dasar dan Menengah atau ensiklopedia daring resmi Perpustakaan Nasional RI.
5. Lakukan **Uji Silang Fakta (*Cross-Checking*)**:
   * [ ] Apakah tanggal peristiwa yang disebutkan AI cocok dengan buku sejarah resmi?
   * [ ] Apakah nama-nama lokasi geografis dan pasukan yang disebut AI benar-benar ada di Bali?
   * [ ] Apakah kamu menemukan adanya halusinasi data fiktif pada teks AI tersebut?
6. Lingkari setiap kalimat yang tidak akurat menggunakan spidol merah dan diskusikan hasilnya bersama teman sekelas!

---

## D. TUGAS PROYEK KINERJA SISWA (LKPD 3.1)

### LEMBAR KERJA PESERTA DIDIK (LKPD 3.1)
**Judul Portofolio:** Lembar Audit Integritas Informasi Hasil AI Generatif  
**Nama Anggota Kelompok:** ............................................................  
**Kelas / Tanggal Praktik:** VII / ....................................................  

#### 1. Tujuan Praktikum
Kalian mampu mengidentifikasi keterbatasan model bahasa besar (LLM), menemukan bukti halusinasi data ilmiah, dan merumuskan langkah verifikasi kebenaran (*Fact-Checking*) secara sistematis.

#### 2. Tabel Formulir Audit Informasi Teks AI

| Parameter Audit | Klaim yang Dihasilkan oleh AI | Hasil Verifikasi Buku / Sumber Resmi | Status Fakta (Akurat / Halusinasi) | Bukti Sumber Resmi Rujukan |
|:---|:---|:---|:---:|:---|
| Tanggal Peristiwa | ........................................... | ........................................... | [ ] Akurat / [ ] Halusinasi | .................................... |
| Nama Tokoh Terkait | ........................................... | ........................................... | [ ] Akurat / [ ] Halusinasi | .................................... |
| Kutipan / Referensi | ........................................... | ........................................... | [ ] Akurat / [ ] Halusinasi | .................................... |

#### 3. Strategi Tiga Langkah Penyelamat Verifikasi (3-Cek)
Jelaskan tindakan kelompokmu dalam memverifikasi berita atau konten digital mencurigakan:
* **Cek 1 (Cek Sumber Asli):** `.........................................................................................................`
* **Cek 2 (Cek Tanggal & Konteks):** `...............................................................................................`
* **Cek 3 (Cek Verifikasi Ahli):** `...................................................................................................`

#### 4. Rubrik Penilaian Proyek Mandiri
* [ ] Ketelitian menemukan kejanggalan atau potensi halusinasi teks AI (Skor: 35).
* [ ] Kualitas sumber referensi pembanding resmi yang terpercaya (Skor: 30).
* [ ] Kejelasan rumusan strategi 3-Cek dalam melawan deepfake dan disinformasi (Skor: 20).
* [ ] Menunjukkan komitmen integritas moral dan etika akademik yang tinggi (Skor: 15).  
* **Total Nilai Kinerja Proyek:** .................... / 100

---

## E. RANGKUMAN MATERI BAB III

1. **AI Generatif (GenAI)** adalah cabang kecerdasan buatan mutakhir yang mampu memproduksi konten orisinal baru (teks, gambar, audio, kode program) berdasarkan perintah bahasa alami (*prompt*) dari manusia.
2. Model Bahasa Besar (LLM) tidak memiliki pemahaman kebenaran sejati seperti pikiran manusia, melainkan bekerja murni berdasarkan **Prediksi Probabilitas Kata Berikutnya (*Next Token Prediction*)** dari statistik data pelatihan.
3. **Tiga Keterbatasan Kritis AI Generatif:**
   * **Halusinasi AI:** Menghasilkan informasi keliru atau fiktif dengan gaya bahasa yang sangat meyakinkan.
   * **Bias Algoritma:** Meniru dan memperkuat prasangka gender, ras, atau ketimpangan budaya masa lalu.
   * **Keterbatasan Data Kedaluwarsa:** Tidak mengetahui fakta terkini di luar batasan masa latihannya.
4. **Teknologi Deepfake** merekayasa wajah (*Face Swap*) dan suara vokal (*Voice Cloning*) secara sintetis yang berpotensi disalahgunakan untuk penipuan siber. Ciri deteksinya meliputi kedipan mata kaku, kelambatan gerak bibir, anomali garis tepi wajah, dan ketidakwajaran detail fisik.
5. **Integritas Akademik Abad 21** menuntut setiap pelajar untuk memosisikan AI sebagai mitra belajar (*tutor reflektif*), menolak jalan pintas plagiarisme salin-tempel, dan memegang tanggung jawab penuh atas setiap karya yang dipublikasikan.

---

## F. TES FORMATIF (UJI PEMAHAMAN HOTS)

### Bagian 1: Pilihan Ganda (Pilihlah Jawaban A, B, C, atau D yang Paling Tepat!)

1. Sistem kecerdasan artifisial yang mampu menghasilkan esai narasi sejarah, menyusun kode program Python, dan melukis gambar pemandangan baru berdasarkan instruksi teks pengguna dikelompokkan ke dalam kategori...  
   A. AI Diskriminatif  
   B. AI Generatif (GenAI)  
   C. Kalkulator Mekanik  
   D. Scanner Optik  

2. Di balik layar komputasi, cara kerja utama Model Bahasa Besar (LLM) seperti Google Gemini atau ChatGPT dalam menyusun kalimat adalah...  
   A. Merenungkan makna filosofis kehidupan menggunakan hati nurani buatan  
   B. Menghitung probabilitas statistik kemunculan kata atau potongan kata berikutnya (*Next Token Prediction*)  
   C. Mengirimkan operator manusia rahasia untuk mengetikkan jawaban secara sembunyi-sembunyi  
   D. Membaca pikiran pengguna melalui gelombang elektromagnetik layar  

3. Fajar meminta sebuah model AI menyebutkan nama ilmuwan penemu vaksin penyakit tertentu. AI memberikan jawaban berupa nama seorang ilmuwan fiktif lengkap dengan nama jurnal ilmiah dan nomor halaman yang setelah dilacak di perpustakaan nasional ternyata tidak pernah ada. Kejadian ini merupakan contoh nyata dari fenomena...  
   A. Hardware Failure  
   B. Halusinasi AI (*AI Hallucination*)  
   C. Cache Memory  
   D. Enkripsi Data  

4. Ketika sebuah AI generator gambar diminta melukiskan *"Sosok Pilot Pesawat Terbang"* dan dalam 100 kali percobaan selalu menghasilkan gambar laki-laki tanpa pernah menghasilkan gambar pilot perempuan satu pun, masalah etika yang sedang terjadi pada sistem AI tersebut adalah...  
   A. Halusinasi grafis  
   B. Bias algoritma (*Algorithmic Bias*)  
   C. Kerusakan piksel layar monitor  
   D. Efisiensi daya listrik  

5. Ibu guru menerima pesan suara (*Voice Note*) WhatsApp dari kepala sekolah yang meminta mentransfer dana kas sekolah sebesar lima juta rupiah ke rekening pribadi yang tidak dikenal. Suara pada rekaman tersebut terdengar persis seperti suara asli kepala sekolah. Tindakan paling aman dan kritis yang wajib diambil ibu guru sebelum bertindak adalah...  
   A. Langsung mentransfer uang tersebut karena takut dimarahi kepala sekolah  
   B. Membagikan pesan suara tersebut ke seluruh grup kelas agar siswa tahu  
   C. Melakukan verifikasi langsung (*Cross-Check*) dengan menemui kepala sekolah secara fisik atau menelepon ke nomor telepon seluler resminya untuk memastikan kebenaran pesan  
   D. Menghapus nomor kontak kepala sekolah dari ponsel  

6. Rekayasa media digital yang mengganti wajah seorang aktor film dengan wajah tokoh politik terkenal menggunakan algoritma kecerdasan buatan disebut teknologi...  
   A. Face Swap Deepfake  
   B. Algoritma Flowchart  
   C. Format Atribusi TASL  
   D. Infinite Loop  

7. Manakah di antara ciri-ciri visual berikut yang merupakan petunjuk kuat bahwa sebuah video rekaman pidato di internet adalah hasil manipulasi rekayasa Deepfake?  
   A. Video memiliki resolusi layar 4K yang sangat jernih  
   B. Gerakan kedipan mata tidak alami, sinkronisasi gerakan bibir terlambat dibandingkan audio, dan ada bayangan buram aneh di garis batas dagu  
   C. Pembicara mengenakan kemeja batik resmi  
   D. Rekaman video diunggah di situs berita resmi pemerintah  

8. Rian diberikan tugas oleh guru bahasa Indonesia untuk menulis sebuah cerpen bertema persahabatan. Rian menggunakan AI untuk menulis seluruh cerita dari awal sampai akhir dalam waktu 5 detik, lalu langsung mengumpulkannya dengan nama dirinya sendiri tanpa membaca atau mengeditnya. Tindakan Rian tersebut melanggar prinsip...  
   A. Prinsip Desain Proximity  
   B. Integritas dan kejujuran akademik  
   C. Protokol keamanan jaringan WiFi  
   D. Standardisasi Flowchart ISO  

9. Cara pemanfaatan kecerdasan artifisial generatif yang paling positif, etis, dan mendukung perkembangan nalar kritis bagi seorang siswa SMP adalah...  
   A. Menyuruh AI mengerjakan seluruh PR matematika dan menyalin hasilnya mentah-mentah ke buku tugas  
   B. Menggunakan AI sebagai mitra diskusi untuk mengecek kelemahan argumen esai pribadi, mencari analogi konsep sains yang sulit, dan memverifikasi faktanya kembali lewat buku teks resmi  
   C. Menggunakan AI untuk membuat gambar ejekan foto teman sekelas  
   D. Meminta AI meretas kata sandi akun media sosial teman  

10. Mengapa kita tidak boleh memasukkan data sensitif—seperti nomor induk kependudukan (NIK), foto kartu keluarga, atau kata sandi pribadi—ke dalam kotak obrolan prompt AI publik di internet?  
    A. Karena teks tersebut dapat disimpan dan digunakan kembali oleh perusahaan AI untuk melatih model bahasa mereka sehingga privasi data kita bocor ke pengguna lain  
    B. Karena komputer akan langsung mati mendadak  
    C. Karena server AI akan kelebihan beban daya  
    D. Karena huruf kapital pada kata sandi merusak tampilan AI  

---

### Bagian 2: Soal Uraian Pemecahan Masalah Sistematis

1. Jelaskan perbedaan mendasar antara cara kerja sistem Kecerdasan Artifisial Klasifikasi (seperti deteksi wajah kamera) dengan Kecerdasan Artifisial Generatif (seperti model bahasa LLM)!
2. Uraikan secara ilmiah mengapa fenomena **Halusinasi AI** dapat terjadi pada model bahasa besar (LLM)! Hubungkan penjelasanmu dengan mekanisme *Next Token Prediction*!
3. Jelaskan apa yang dimaksud dengan **Bias Algoritma** pada kecerdasan artifisial! Berikan sebuah contoh kasus bagaimana bias tersebut dapat merugikan keadilan di tengah masyarakat!
4. Teknologi rekayasa video dan audio *Deepfake* kini semakin marak disalahgunakan untuk tindak kejahatan penipuan. Jelaskan 4 langkah konkret yang dapat dilakukan oleh masyarakat awam untuk mendeteksi keaslian sebuah video yang dicurigai sebagai deepfake!
5. Tuliskan sebuah esai reflektif singkat (1-2 paragraf) tentang bagaimana sikap moralmu sebagai seorang pelajar SMP dalam menghadapi godaan menggunakan kecerdasan artifisial untuk jalan pintas menyelesaikan tugas-tugas sekolah! Mengapa proses berpikir mandiri tetap jauh lebih berharga daripada hasil instan mesin?

---

## G. KUNCI JAWABAN & PEMBAHASAN TES FORMATIF BAB III

### Kunci Jawaban Pilihan Ganda:
1. **B** (AI Generatif / GenAI: memiliki kemampuan menghasilkan konten baru yang orisinal).
2. **B** (Prediksi probabilitas statistik kata berikutnya berdasarkan pola miliaran teks latih).
3. **B** (Halusinasi AI: menghasilkan klaim fiktif meyakinkan yang tidak memiliki rujukan nyata).
4. **B** (Bias algoritma: ketidakseimbangan representasi gender pada data latih internet).
5. **C** (Verifikasi langsung multi-kanal untuk mencegah jeratan penipuan kloning suara AI).
6. **A** (Face Swap Deepfake: manipulasi pertukaran wajah berbasis deep learning).
7. **B** (Ciri anomali deepfake: kelambatan sinkronisasi bibir, mata kaku, dan artefak blur pada perbatasan kulit).
8. **B** (Pelanggaran integritas akademik dan perilaku plagiarisme digital).
9. **B** (Mitra belajar reflektif: melatih nalar kritis tanpa menggantikan proses berpikir mandiri).
10. **A** (Data prompt publik diserap kembali ke dalam korpus data latih AI yang membahayakan privasi).

### Pedoman Pembahasan Soal Uraian:
1. **Perbedaan Klasifikasi vs Generatif:** AI Klasifikasi hanya menganalisis dan melabeli data masukan yang ada ke dalam kategori tertentu (misal: "Foto ini 95% wajah Rian"). AI Generatif menciptakan data atau representasi baru yang belum pernah ada sebelumnya (misal: "Melukiskan wajah Rian mengenakan seragam astronot di planet Mars").
2. **Mekanisme Halusinasi AI:** LLM tidak memiliki koneksi ke dunia fisik nyata atau basis data kebenaran mutlak. LLM hanya mesin probabilistik yang mengoptimalkan kelancaran aliran kalimat (*syntactic fluency*). Ketika menghadapi celah informasi, model akan memilih kata yang memiliki skor keterkaitan statistik tertinggi meskipun secara fakta sejarah atau sains kata tersebut salah total.
3. **Bias Algoritma & Dampak Sosial:** Bias terjadi saat data latih mencerminkan diskriminasi historis masyarakat. Contoh: AI penyaring lamaran kerja yang secara otomatis menolak berkas pelamar perempuan untuk posisi manajer teknologi karena data masa lalu didominasi laki-laki, sehingga melanggengkan ketidakadilan sosial.
4. **4 Langkah Deteksi Deepfake:**
   * Amati kedipan mata dan arah sorot tatapan pupil.
   * Cek keselarasan gerak bibir (*lip-sync*) dengan gelombang suara ucapan vokal.
   * Periksa anomali batas fisik (blur di dagu, leher, atau bentuk telinga asimetris).
   * Lakukan verifikasi sumber (*3-Cek*): konfirmasi langsung ke orang yang bersangkutan lewat jalur terpercaya.
5. **Refleksi Moral Pelajar:** Penekanan bahwa nilai sekolah sejati bukan sekadar angka di atas kertas, melainkan terbentuknya ketangguhan berpikir, daya kreasi, dan kejujuran nurani. Mengandalkan AI secara buta akan menumpulkan potensi intelektual manusia. AI harus dijadikan pemicu ide, namun penalaran dan keputusan akhir tetap berada di tangan manusia.

---

## H. REFLEKSI & METAKOGNISI DIRI

Salinlah tabel refleksi metakognisi ini ke buku jurnal kodingmu dan berikan tanda centang (✓) sesuai dengan evaluasi belajarmu:

| No | Indikator Kompetensi Pembelajaran | Sangat Menguasai 🌟 | Cukup Menguasai 👍 | Perlu Pendampingan 📖 |
|:---:|:---|:---:|:---:|:---:|
| 1 | Saya memahami perbedaan mendasar AI Klasifikasi dan AI Generatif. | [ ] | [ ] | [ ] |
| 2 | Saya memahami cara kerja LLM sebagai penebak kata probabilitas. | [ ] | [ ] | [ ] |
| 3 | Saya mampu mengenali fenomena halusinasi data dan bias pada AI. | [ ] | [ ] | [ ] |
| 4 | Saya mengetahui teknik deteksi visual dan audio rekayasa Deepfake. | [ ] | [ ] | [ ] |
| 5 | Saya berkomitmen menjaga integritas akademik dan menolak plagiarisme AI. | [ ] | [ ] | [ ] |

**Pencapaian Misi Bab III:**  
Selamat! Kalian resmi meraih:  
🎖️ **LENCANA MEDALI PENYELIDIK FAKTA & ETIKA AI (FASE D KELAS VII)** 🎖️  
*"Jadilah penunggang teknologi yang bijak: pertajam nalarmu, uji setiap fakta, dan tegakkan kebenaran!"*
"""
