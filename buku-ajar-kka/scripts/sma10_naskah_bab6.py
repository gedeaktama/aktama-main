"""
Modul Naskah Bab VI Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB6_SMA10 = """# BAB VI: REKAYASA PROMPT TINGKAT LANJUT DAN PERANCANGAN SOLUSI SISTEM AI

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
"""
