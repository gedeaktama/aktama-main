# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 3 Buku Siswa KKA Kelas 8 SMP (Fase D)
BAB III: PENGINDERAAN MESIN, FUSI SENSOR, & KUALITAS DATA DALAM AI (18 JP)
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_3_SMP8 = """# BAB III PENGINDERAAN MESIN, FUSI SENSOR, & KUALITAS DATA DALAM AI

## MISI 3: PENYELIDIK FUSI SENSOR & DATA LATIH OBJEKTIF
* **Alokasi Waktu:** 18 Jam Pelajaran (9 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Literasi dan Etika Kecerdasan Artifisial (LEKA) & Pemanfaatan KA (PPKA)
* **Target Lencana Koder:** Medali Emas Penyelidik Fusi Sensor & Data Objektif (Fase D)

---

## A. PENDAHULUAN: MISI DRONE PENYELAMAT DI KABUT GUNUNG

Layar proyektor di laboratorium sains komputasi menampilkan siaran berita langsung tim Badan Penanggulangan Bencana Daerah (BPBD). Di kawasan lereng Gunung Merapi, dua orang pendaki remaja dilaporkan tersesat di tengah cuaca ekstrem. Kabut tebal berwarna putih susu menyelimuti jurang-jurang terjal, membuat jarak pandang mata manusia tidak lebih dari dua meter.

"Misi pencarian darat dihentikan sementara demi keselamatan tim evakuasi," suara narator berita terdengar tegang. "Namun tim penyelamat kini mengerahkan armada drone otonom generasi terbaru yang dibekali kecerdasan artifisial dan multi-sensor canggih!"

[[IMAGE: bab3_komik_pembuka_smp8.png | Gambar 3.1: Komik Pembuka Bab 3: Misi Penyelamatan Drone di Kabut Tebal]]

Fajar terpaku menatap layar siaran langsung tersebut. "Kamera biasa pasti tidak akan sanggup melihat apa pun di dalam kabut pekat seperti itu. Bagaimana mungkin drone penyelamat itu bisa menemukan manusia di balik kepungan asap dan kabut tebal?"

"Itulah kehebatan **Persepsi Mesin (*Machine Perception*)** dan **Fusi Sensor (*Sensor Fusion*)**, Fajar!" sahut Rian penuh semangat. "Drone penyelamat itu tidak hanya mengandalkan mata kamera optik. Di tubuhnya terpasang sensor inframerah yang mendeteksi radiasi panas tubuh, sensor gelombang suara ultrasonik, radar gelombang mikro, serta giroskop penyeimbang. Seluruh data sensor digabungkan oleh komputer cerdas di dalam drone!"

Ayu mengangguk setuju. "Tetapi ingat, sistem cerdas sehebat apa pun sangat bergantung pada **kualitas data (*data quality*)**. Jika data latih yang dipelajari AI di masa lalu keliru, bising, atau timpang (*imbalanced*), sistem cerdas bisa membuat keputusan yang fatal! Mari kita bongkar bersama bagaimana komputer membaca dunia fisik kita dan bagaimana menjaga kejernihan data latih kecerdasan artifisial!"

---

## B. KONSEP FUSI MULTI-SENSOR (SENSOR FUSION) PADA SISTEM CERDAS

Manusia diciptakan Tuhan dengan panca indera yang saling melengkapi. Ketika kita berada di dapur dalam kondisi mati lampu gulita, mata kita mungkin tidak dapat melihat, namun hidung kita bisa mencium bau kue yang baru matang, dan tangan kita dapat meraba permukaan meja untuk mencari lilin. Otak kita secara otomatis menggabungkan seluruh informasi indera tersebut menjadi satu kesimpulan utuh.

Dalam dunia robotika dan kecerdasan artifisial, proses penggabungan informasi dari berbagai sensor yang berbeda ini dinamakan **Fusi Sensor (*Sensor Fusion*)**.

[[IMAGE: bab3_arsitektur_sensor_fusion_drone.png | Gambar 3.2: Arsitektur Fusi Sensor (Sensor Fusion): Mata dan Telinga Sistem Cerdas]]

### Mengapa Satu Sensor Saja Tidak Pernah Cukup?
Setiap jenis sensor di dunia memiliki kelebihan sekaligus kelemahan mendasar (*blind spots*):
1. **Kamera Optik RGB (Mata Visual):**
   * *Kelebihan:* Sangat kaya informasi detail warna, bentuk objek, dan tekstur gambar.
   * *Kelemahan:* Menjadi buta total saat malam hari tanpa cahaya, tertutup kabut tebal, atau terkena pantulan sinar matahari yang menyilaukan (*glare*).
2. **Sensor Inframerah / Thermal (Pendeteksi Suhu):**
   * *Kelebihan:* Mampu menembus kegelapan malam dan kabut pekat untuk mendeteksi radiasi kalor tubuh makhluk hidup (suhu ~36.5°C).
   * *Kelemahan:* Tidak bisa membaca warna pakaian, tidak bisa mengenali raut wajah seseorang, dan mudah terkelabui jika ada batu yang baru saja terpapar terik matahari.
3. **Sensor Jarak LiDAR / Ultrasonik (Gelombang Pantul):**
   * *Kelebihan:* Mampu mengukur jarak fisik dinding atau jurang dengan presisi milimeter menggunakan pantulan laser atau suara.
   * *Kelemahan:* Tidak tahu apakah objek di depannya adalah tumpukan salju lunak atau dinding batu keras.
4. **Modul GPS & IMU (Inertial Measurement Unit):**
   * *Kelebihan:* Memberikan koordinat garis lintang/bujur bumi dan menjaga keseimbangan posisi terbang drone terhadap terpaan angin.
   * *Kelemahan:* Sinyal GPS bisa hilang total saat drone masuk ke dalam gua atau lembah sempit di bawah kanopi hutan rimba yang rapat.

### Prinsip Kerja Unit Fusi Sensor
Ketika drone penyelamat terbang di atas kabut pegunungan, prosesor AI tidak mengambil keputusan hanya berdasarkan satu sensor:
* Data kamera optik (tertutup putih kabut) diberi bobot kepercayaan rendah (*low confidence*).
* Data sensor thermal mendeteksi titik panas 37°C di koordinat tertentu di lereng jurang.
* Data sensor LiDAR mengonfirmasi jarak lereng tebing aman untuk didekati drone.
* Unit Fusi Sensor menyatukan ketiga informasi ini: *"Ditemukan korban selamat di koordinat tebing, jarak aman 5 meter, luncurkan paket selimut dan obat darurat!"*

Prinsip fundamental: *"Satu sensor bisa salah atau tertipu kondisi alam, namun gabungan multi-sensor saling menutupi kelemahan satu sama lain untuk melahirkan kebenaran yang andal."*

---

## C. BAGAIMANA KOMPUTER MEMBACA ALAM: DARI GELOMBANG FISIK MENJADI BIT BINER

Pernahkah kalian berpikir: Komputer pada dasarnya hanyalah mesin elektronik yang hanya mengenal angka biner `0` (mati) dan `1` (hidup). Bagaimana sebuah mesin hitung bisa memahami suhu udara yang panas, hembusan angin kencang, atau warna merah kelopak bunga mawar?

[[IMAGE: bab3_siklus_sinyal_fisik_ke_biner.png | Gambar 3.3: Bagaimana Komputer Membaca Alam: Dari Gelombang Fisik Menjadi Bit Biner]]

### Perjalanan Empat Langkah Konversi Sinyal
Proses perubahan fenomena alam menjadi data biner di dalam otak komputer melalui tahapan ilmiah yang teratur:

1. **Tahap 1: Fenomena Fisik di Alam Bebas (Sinyal Analog):**  
   Di alam semesta, segala sesuatu bersifat kontinu (*analog*) dan berubah tanpa henti. Suhu udara di siang hari berfluktuasi secara halus dari 28.1°C menjadi 28.105°C, lalu 28.112°C. Gelombang suara vokal manusia bergetar di udara dalam bentuk gelombang tekanan udara yang meliuk-liuk lembut.
2. **Tahap 2: Transduser Sensor (Mengubah Tekanan ke Voltase Listrik):**  
   Sensor (disebut juga *transduser*) memiliki material khusus yang peka terhadap perubahan fisik. Misalnya pada sensor suhu termistor: saat udara memanas, hambatan listrik (*resistansi*) material berubah, sehingga tegangan listrik (*voltase*) yang melaluinya naik dari 1.2 Volt menjadi 2.4 Volt.
3. **Tahap 3: Pencuplikan & Konversi (Sampling & ADC):**  
   Komputer memiliki gerbang elektronik bernama **Analog-to-Digital Converter (ADC)**. ADC melakukan pengukuran (*sampling*) tegangan listrik ribuan kali dalam satu detik. Misalnya pada frekuensi audio standar 44.100 Hz, voltase listrik diukur sebanyak 44.100 kali setiap detiknya dan dibulatkan menjadi angka desimal tertentu.
4. **Tahap 4: Deretan Bit Biner & Ekstraksi Ciri (*Feature Extraction*):**  
   Angka desimal tersebut kemudian dikonversi menjadi barisan kode biner: deretan bit 0 dan 1. Komputer tidak memproses seluruh piksel gambar mentah secara membabi buta, melainkan melakukan **Ekstraksi Ciri**: mendeteksi garis tepi (*edges*), sudut bentuk (*corners*), dan pola tekstur. Kumpulan ciri matematis inilah yang kemudian dimasukkan ke dalam algoritma model kecerdasan artifisial!

---

## D. KUALITAS DATA LATIH AI: DATA BERSIH VS DATA BISING (NOISE)

Dalam sains kecerdasan artifisial, ada sebuah pepatah klasik yang sangat terkenal: **"Garbage In, Garbage Out" (GIGO)**. Artinya: Jika kalian melatih model kecerdasan artifisial menggunakan data yang kotor seperti sampah, maka keputusan yang dikeluarkan oleh AI tersebut juga akan menjadi sampah yang tidak berguna dan berbahaya!

[[IMAGE: bab3_infografis_kualitas_data_bias.png | Gambar 3.4: Kualitas Data Latih AI: Data Bersih Seimbang vs Data Bising dan Timpang (Biased)]]

### Mengenal Data Bising (*Noisy Data*)
Data bising adalah data yang terkontaminasi oleh gangguan acak yang merusak kejelasan ciri objek. Contoh derau dalam kehidupan sehari-hari:
* Lensa kamera keamanan sekolah yang kotor berdebu atau buram terkena tetesan air hujan.
* Rekaman mikrofon pengenal suara yang dipenuhi dengung kipas angin keras.
* Data survei siswa yang diisi secara asal-asalan dengan jawaban yang ngawur (*outliers*).

Jika model AI dilatih menggunakan foto-foto mobil yang buram dan terhalang bayangan tiang listrik, AI akan bingung: apakah garis vertikal hitam di tengah jalan itu bagian dari mobil ataukah tiang jalan? Akibatnya, saat diterapkan pada mobil otonom yang melaju kencang di jalan raya, mobil bisa mendadak mengerem mendadak tanpa alasan di tengah jalan sepi!

---

## E. BAHAYA DATASET TIDAK SEIMBANG (IMBALANCED DATA) & BIAS ALGORITMA

Selain masalah derau, bahaya terbesar yang mengancam keadilan sistem kecerdasan artifisial modern adalah fenomena **Dataset Tidak Seimbang (*Imbalanced Dataset*)** yang memicu lahirnya **Bias Algoritma**.

### Mengapa AI Bisa Menjadi "Pilih Kasih"?
Bayangkan seorang guru di kelas yang ingin melatih muridnya membedakan antara buah Jeruk dan buah Pisang. Namun selama sebulan penuh, sang guru memperlihatkan 500 foto buah Jeruk dari berbagai sudut yang cerah, tetapi hanya memperlihatkan 3 lembar foto buah Pisang yang buram di sudut gelap.

Ketika ujian tiba dan guru memperlihatkan sebuah buah pisang berkulit kuning di bawah terik matahari, sang murid dengan yakin menjawab: *"Itu pasti Jeruk!"* Mengapa murid salah menjawab? Bukan karena murid tersebut bodoh, melainkan karena data latih yang diterimanya sangat timpang dan tidak mewakili kenyataan!

### Kasus Nyata Kegagalan Sistem Cerdas di Dunia Nyata
1. **Kegagalan Kamera Pengenal Wajah (*Facial Recognition*):**  
   Sebuah sistem absensi cerdas di sebuah sekolah internasional berjalan mulus saat mengenali siswa berkulit terang, namun berulang kali gagal mendeteksi siswa berkulit gelap. Setelah diselidiki para ilmuwan, ternyata 90% foto dalam dataset latih pengembang aplikasi hanya berisi wajah orang-orang dari negara Barat berkulit terang. Sistem AI tersebut mengalami kebutaan representasi budaya!
2. **Mobil Otonom dan Deteksi Pejalan Kaki di Malam Hari:**  
   Sebuah model deteksi rintangan mobil swakemudi dilatih menggunakan ribuan foto jalanan di siang hari yang terik. Ketika diuji melaju pada malam hari saat hujan gerimis, model gagal mendeteksi seorang penyeberang jalan yang mengenakan mantel hujan gelap karena dalam dataset latihnya tidak pernah ada contoh pejalan kaki dengan kondisi pencahayaan malam.

> **Wawasan Koder: Kunci Dataset Berkualitas Tinggi**  
> Sebuah dataset latih yang unggul dan etis wajib memenuhi tiga kriteria:
> 1. **Keseimbangan Jumlah (*Balance*):** Jumlah sampel antar kelas kategori setara (misal: 100 foto kucing dan 100 foto anjing).
> 2. **Variasi Lingkungan (*Diversity*):** Objek difoto dalam berbagai kondisi pencahayaan (siang, malam, remang), berbagai latar belakang, dan sudut pandang berbeda.
> 3. **Pelabelan yang Akurat (*Ground Truth Labeling*):** Setiap data diberi label kategori yang benar tanpa kekeliruan manusia.

---

## F. LKPD PLUGGED 3.1: EKSPERIMEN KUALITAS DATA LATIH MODEL KLASIFIKASI GAMBAR

### Aktivitas Praktik Mandiri dan Kolaboratif (Plugged Activity)
* **Platform:** Google Teachable Machine (*teachablemachine.withgoogle.com*) menggunakan peramban web komputer/laptop yang memiliki kamera web (*webcam*).
* **Durasi:** 4 JP (2 Pertemuan Praktik Laboratorium Terbimbing).
* **Tujuan Eksperimen:** Membuktikan secara ilmiah pengaruh variasi dataset latih terhadap tingkat akurasi prediksi model klasifikasi citra cerdas.

### Langkah-Langkah Eksperimen:
1. **Skenario Klasifikasi Dua Kelas Objek:**
   * Kita akan melatih model untuk membedakan dua benda di meja kelas: **Buku Pelajaran** (Kelas 1) dan **Tempat Pensil** (Kelas 2).

2. **Uji Coba Tahap 1: Dataset Timpang & Monoton (Dataset Buruk):**
   * Masukkan hanya **5 foto** Buku Pelajaran (semua diambil dari sudut depan statis).
   * Masukkan **50 foto** Tempat Pensil (berbagai posisi).
   * Klik tombol **Train Model** dan tunggu proses pelatihan selesai.
   * *Uji Model di Kolom Preview:* Tunjukkan Buku Pelajaran dari sudut miring atau di ruangan yang sedikit gelap. Amati grafik probabilitasnya! Catat: Apakah AI salah menebak buku sebagai tempat pensil?

3. **Uji Coba Tahap 2: Dataset Berkualitas & Seimbang (Dataset Ideal):**
   * Buka proyek baru. Kumpulkan **50 foto** Buku Pelajaran dari berbagai sudut (depan, miring, tegak, jarak dekat, jarak jauh, tangan memegang buku).
   * Kumpulkan **50 foto** Tempat Pensil dengan variasi sudut dan pencahayaan yang sama seimbangnya.
   * Latih ulang model (*Train Model*).
   * Uji kembali dengan berbagai posisi ekstrim. Amati grafik probabilitas akurasi yang dihasilkan!

4. **Tabel Analisis Hasil Eksperimen:**
| Parameter Pengujian | Uji Coba 1 (Data Timpang 5 vs 50) | Uji Coba 2 (Data Seimbang 50 vs 50) |
| :--- | :--- | :--- |
| Prediksi saat Buku tegak | ... % | ... % |
| Prediksi saat Buku miring | ... % | ... % |
| Prediksi saat lampu dimatikan | ... % | ... % |
| Kesimpulan Tingkat Keandalan | **Rentan Salah / Bias** | **Sangat Akurat & Stabil** |

---

## POJOK KARAKTER & ETIKA KODER: KEADILAN ALGORITMA (ALGORITHMIC FAIRNESS)

Kecerdasan artifisial tidak lahir dari ruang hampa. Komputer tidak memiliki prasangka atau kebencian alami; ia hanya meniru cermin dari data yang kita berikan kepadanya. Jika data yang kita kumpulkan memuat diskriminasi, stereotip suku, atau mengabaikan kelompok minoritas, maka model kecerdasan artifisial akan mewarisi ketidakadilan tersebut dengan kecepatan dan skala yang berlipat ganda!

Sebagai generasi koder dan ilmuwan masa depan bangsa Indonesia yang bersemboyankan *Bhinneka Tunggal Ika*, kita memiliki kewajiban moral untuk memperjuangkan **Keadilan Algoritma (*Algorithmic Fairness*)**. Menjadi programmer cerdas bukan hanya tentang menulis kode matematika yang rumit, melainkan tentang memiliki hati nurani yang peka: memastikan bahwa teknologi yang kita ciptakan memperlakukan setiap insan manusia—tanpa memandang warna kulit, suku bangsa, kondisi fisik, maupun latar belakang ekonominya—dengan rasa hormat, adil, dan setara!

---

## RANGKUMAN MATERI BAB 3

1. **Fusi Sensor (*Sensor Fusion*)** adalah teknik penggabungan data dari berbagai jenis sensor (kamera optik, thermal inframerah, LiDAR, GPS, dan IMU) untuk saling melengkapi kelemahan masing-masing sehingga sistem otonom dapat mengambil keputusan lingkungan secara akurat dan andal.
2. **Konversi Sinyal Fisik ke Digital** berlangsung melalui 4 fase: Fenomena fisik analog di alam -> Perubahan voltase pada transduser sensor -> Pencuplikan frekuensi dan kuantisasi oleh *Analog-to-Digital Converter (ADC)* -> Representasi deretan biner 0 dan 1 yang diekstraksi ciri-cirinya.
3. **Prinsip "Garbage In, Garbage Out"** menegaskan bahwa keakuratan model AI mutlak dibatasi oleh kejernihan data latihnya. Data bising (*noisy data*) memicu kesalahan interpretasi yang berbahaya.
4. **Dataset Tidak Seimbang (*Imbalanced Dataset*)** dan sampel yang tidak representatif melahirkan fenomena **Bias Algoritma**, di mana sistem cerdas gagal mengenali kategori minoritas secara adil.
5. **Keadilan Algoritma (*Algorithmic Fairness*)** menuntut para perancang kecerdasan artifisial untuk aktif mengaudit keberagaman dataset demi menjamin kesetaraan hak asasi seluruh umat manusia.

---

## UJI PEMAHAMAN HOTS BAB 3

### I. Pilihan Ganda (Pilihlah Jawaban yang Paling Tepat!)

1. Kelemahan mendasar dari kamera optik RGB konvensional pada drone penyelamat saat beroperasi di lereng gunung berkabut tebal adalah...
   A. Bobot kamera terlalu berat sehingga menghabiskan baterai drone  
   B. Gelombang cahaya tampak terserap dan terhamburkan oleh partikel uap air kabut sehingga gambar menjadi buram putih  
   C. Kamera optik tidak mampu merekam gambar beresolusi tinggi di atas 1080p  
   D. Memori kartu penyimpanan drone akan langsung terkunci otomatis jika terkena kabut  

2. Jenis sensor yang paling andal dipadukan dengan kamera optik untuk mendeteksi keberadaan tubuh manusia yang terperangkap di reruntuhan bangunan gelap saat malam hari adalah...
   A. Sensor Barometer Tekanan Udara  
   B. Sensor Thermal Inframerah (Pendeteksi Kalor)  
   C. Sensor Kompas Magnetik  
   D. Sensor Pengukur Kelembapan Tanah  

3. Komponen perangkat keras elektronik yang bertugas mencuplik tegangan listrik gelombang analog yang berubah-ubah menjadi deretan angka biner komputer disebut...
   A. Central Processing Unit (CPU)  
   B. Analog-to-Digital Converter (ADC)  
   C. Random Access Memory (RAM)  
   D. Liquid Crystal Display (LCD)  

4. Perhatikan kasus berikut: Sebuah model AI pengenal rambu lalu lintas dilatih dengan 1.000 foto rambu di jalanan kota Tokyo yang terang benderang. Ketika sistem tersebut dipasang pada kendaraan otonom di jalan pedesaan Indonesia yang remang-remang diapit pepohonan, sistem sering gagal membaca rambu batas kecepatan. Akar penyebab utama kegagalan tersebut adalah...
   A. Kecepatan prosesor komputer mobil kurang tinggi  
   B. Kurangnya variasi pencahayaan dan representasi lingkungan nyata (*domain shift*) pada dataset latih awal  
   C. Mobil kehabisan bahan bakar minyak saat melaju di pedesaan  
   D. Bahasa pemrograman yang digunakan mobil bukan bahasa Python  

5. Istilah komputasi klasik yang menyatakan bahwa kualitas data masukan yang buruk secara pasti akan menghasilkan luaran keputusan sistem yang buruk pula adalah...
   A. What You See Is What You Get (WYSIWYG)  
   B. Garbage In, Garbage Out (GIGO)  
   C. Artificial General Intelligence (AGI)  
   D. High Performance Computing (HPC)  

6. Fajar melatih model AI untuk mengenali ekspresi wajah bahagia vs sedih. Namun Fajar hanya memasukkan 5 foto wajah sedih dan 150 foto wajah bahagia. Kondisi dataset ini disebut sebagai...
   A. Clean Dataset  
   B. Imbalanced Dataset (Data Timpang)  
   C. Overfitted Algorithm  
   D. Augmented Data  

7. Dampak nyata yang akan terjadi pada model klasifikasi gambar jika dilatih menggunakan *Imbalanced Dataset* seperti pada soal nomor 6 adalah...
   A. Model akan menolak untuk dilatih oleh sistem komputer  
   B. Model akan memiliki bias tinggi dan cenderung selalu menebak 'wajah bahagia' meskipun yang diperlihatkan adalah wajah sedih  
   C. Komputer akan mengalami mati mendadak (*blue screen*)  
   D. Tingkat akurasi pada kedua kelas wajah akan sama-sama mencapai 100% sempurna  

8. Manakah dari langkah berikut yang paling tepat untuk mengeliminasi derau bising (*noise*) pada kumpulan data audio perintah suara (*voice control*)?
   A. Mempercepat tempo rekaman menjadi dua kali lipat lebih cepat  
   B. Menerapkan algoritma penyaring frekuensi (*band-pass filter*) dan membersihkan profil derau hening sebelum pelatihan model  
   C. Menambahkan musik rock yang keras di belakang suara perintah  
   D. Mengubah seluruh suara manusia menjadi suara robot buatan  

9. Mengapa fusi sensor (*Sensor Fusion*) menjadi standar wajib dalam teknologi mobil swakemudi otonom modern di jalan raya?
   A. Agar biaya pembuatan mobil menjadi semakin mahal dan mewah  
   B. Karena tidak ada satu sensor pun di dunia yang sempurna dalam segala cuaca buruk dan kondisi pencahayaan ekstrem  
   C. Agar mobil dapat terbang melompati kemacetan lalu lintas  
   D. Karena aturan kepolisian mewajibkan mobil memiliki minimal sepuluh kabel data  

10. Komitmen seorang pengembang perangkat lunak untuk memastikan bahwa sistem AI rekrutmen kerja tidak mendiskriminasi pelamar berdasarkan gender atau ras merupakan penerapan prinsip...
    A. Monetisasi Algoritma  
    B. Keadilan Algoritma (*Algorithmic Fairness*)  
    C. Kecepatan Pemrosesan Data  
    D. Hak Cipta Komersial Tertutup  

---

### II. Uraian Pemecahan Masalah (Jawablah Secara Rinci dan Terstruktur!)

1. Jelaskan konsep *Sensor Fusion* dan kemukakan alasan mengapa gabungan beberapa sensor yang berbeda jauh lebih unggul dibandingkan satu sensor tunggal yang paling canggih sekalipun! Berikan contoh penerapannya pada drone pemadam kebakaran hutan!
2. Uraikan perjalanan panjang sebuah fenomena fisik di alam (misalnya hembusan angin kencang) hingga akhirnya dapat diproses sebagai deretan angka biner 0 dan 1 di dalam memori komputer!
3. Jelaskan apa yang dimaksud dengan prinsip *Garbage In, Garbage Out (GIGO)* dalam pembelajaran mesin kecerdasan artifisial! Berikan satu contoh skenario nyata di mana data bising memicu kegagalan sistem cerdas di bidang transportasi!
4. Apa yang dimaksud dengan *Imbalanced Dataset* (Dataset Timpang)? Mengapa kondisi ini memicu terjadinya *Bias Algoritma* yang merugikan kelompok minoritas? Bagaimana solusi teknis yang dapat dilakukan oleh seorang koder untuk menyeimbangkannya kembali?
5. Sebagai calon ilmuwan komputer Indonesia, bagaimana kalian menerapkan nilai-nilai Profil Pelajar Pancasila (khususnya Bernalar Kritis dan Berakhlak Mulia) saat mengumpulkan dan menyeleksi dataset untuk melatih sistem kecerdasan artifisial di sekolah kalian?

---

## KUNCI JAWABAN UJI PEMAHAMAN TERPILIH BAB 3

### Kunci Jawaban Pilihan Ganda:
1. **B** (Partikel kabut menyerap dan membiaskan spektrum cahaya tampak sehingga kamera optik kehilangan kontras visual).
2. **B** (Sensor thermal inframerah membaca radiasi panas tubuh makhluk hidup yang menembus kegelapan malam).
3. **B** (ADC adalah sirkuit elektronik pengubah voltase kontinu analog menjadi nilai diskrit biner komputer).
4. **B** (Model gagal karena dataset latihnya tidak memuat variasi pencahayaan malam hari pedesaan).
5. **B** (GIGO adalah prinsip klasik: jika input data buruk, maka keputusan luaran sistem dipastikan cacat).
6. **B** (Perbedaan perbandingan jumlah sampel yang sangat mencolok 5 vs 150 adalah definisi dataset timpang).
7. **B** (Model secara statistik akan memprioritaskan kelas mayoritas dan buta terhadap kelas minoritas).
8. **B** (Penyaringan frekuensi derau dan noise profiling membersihkan sinyal vokal sebelum proses ekstraksi ciri).
9. **B** (Setiap sensor memiliki titik buta fisik; penggabungan multi-sensor menjamin keselamatan sistem di segala cuaca).
10. **B** (*Algorithmic Fairness* adalah komitmen etika perancangan AI yang adil, setara, dan non-diskriminatif).
"""
