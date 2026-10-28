# -*- coding: utf-8 -*-
"""
Naskah Lengkap Bab 4 Buku Siswa KKA Kelas 8 SMP (Fase D)
BAB IV: REKAYASA PROMPT TINGKAT LANJUT & KEAMANAN RUANG SIBER (18 JP)
Dan Evaluasi Komprehensif Sumatif Akhir Tahun Fase D Kelas VIII
Standar: Buku Ajar Kemendikdasmen RI / Pembelajaran Mendalam (Deep Learning)
"""

BAB_4_SMP8 = """# BAB IV REKAYASA PROMPT TINGKAT LANJUT & KEAMANAN RUANG SIBER

## MISI 4: DETEKTIF SIBER & ARSITEK PROMPTING ANALITIS
* **Alokasi Waktu:** 18 Jam Pelajaran (9 Pertemuan @ 2 JP)
* **Elemen Capaian Pembelajaran:** Pemanfaatan KA (PPKA) & Literasi Digital (LD)
* **Target Lencana Koder:** Medali Emas Detektif Siber & Arsitek Prompting Nusantara (Fase D)

---

## A. PENDAHULUAN: MISTERI JEBAKAN UNDIAN BERHADIAH DI PONSEL

Sore hari di teras perpustakaan sekolah, Fajar tiba-tiba berseru kaget sambil menatap layar ponsel pintarnya. Layar menampilkan sebuah pesan WhatsApp masuk dari nomor kontak tak dikenal dengan foto profil logo resmi sebuah perusahaan telekomunikasi terkenal.

"Rian! Ayu! Lihat ini!" seru Fajar dengan mata berbinar. "Ponselku baru saja menerima pesan luar biasa! Tertulis di sini: *'Selamat! Nomor Anda terpilih memenangkan saldo dompet digital senilai Rp1.000.000 dan voucher game 5.000 diamond! Klaim hadiah sekarang dengan klik tautan: hadiah-resmi-telekomunikasi.xyz/klaim-sekarang dan masukkan kode verifikasi SMS (OTP) Anda dalam waktu 5 menit atau hadiah hangus!'*"

[[IMAGE: bab4_komik_pembuka_smp8.png | Gambar 4.1: Komik Pembuka Bab 4: Detektif Siber & Jebakan Phishing Rekayasa Sosial]]

Fajar sudah bersiap menyentuh tautan biru tersebut dengan jempolnya, namun dengan sigap Ayu menahan tangan Fajar. 

"Tunggu, Fajar! Jangan diklik!" sergah Ayu tegas. "Perhatikan alamat tautannya baik-baik. Domain resminya seharusnya berekstensi *.co.id*, bukan *.xyz*! Dan perhatikan bahasanya: menciptakan rasa panik dengan batasan waktu lima menit serta meminta kode rahasia OTP. Ini adalah perangkap klasik kejahatan siber!"

Rian memeriksa pesan itu dengan kacamata analitisnya. "Ayu benar 100%. Ini adalah taktik **Rekayasa Sosial (*Social Engineering*)** melalui metode **Phishing**. Penjahat siber sedang memanipulasi rasa penasaran dan keserakahanmu untuk membajak akun ponselmu! Jika kamu memasukkan kode OTP itu, saldo pulsamu dan akun pesan singkatmu akan langsung dikuasai peretas!"

Fajar menelan ludah, wajahnya memucat menyadari bahaya yang nyaris menimpanya. "Mengerikan sekali... Mereka menyamar begitu meyakinkan! Bagaimana caranya kita bisa selalu waspada mendeteksi manipulasi digital ini? Dan bagaimana kita bisa memanfaatkan kecerdasan artifisial secara analitis melalui teknik **Chain-of-Thought Prompting** untuk membantu kita menganalisis bahaya siber ini?"

"Ayo kita buka markas detektif siber kita!" ajak Rian penuh semangat. "Di bab pamungkas kelas VIII ini, kita akan membongkar tuntas rahasia rekayasa prompt tingkat tinggi dan merancang benteng pertahanan digital yang kokoh bagi diri kita, keluarga, dan masyarakat!"

---

## B. PROMPTING BERNALAR BERTAHAP: TEKNIK CHAIN-OF-THOUGHT (CoT)

Di kelas VII, kalian telah menguasai seni menyusun prompt terstruktur menggunakan formula empat pilar (Peran, Tugas, Konteks, dan Format). Namun, ketika kita berhadapan dengan masalah matematika yang rumit, teka-teki logika komputasi, atau analisis studi kasus yang mendalam, model bahasa besar (*Large Language Models / LLM*) sering kali melakukan kesalahan perhitungan jika kita hanya meminta jawaban secara langsung.

Mengapa hal ini terjadi? Karena LLM pada hakikatnya adalah mesin pemrediksi kata berikutnya berbasis probabilitas statistik. Jika diminta langsung menebak jawaban akhir, model sering terburu-buru "menebak" angka yang terdengar meyakinkan di permukaan, padahal keliru (*halusinasi logika*).

[[IMAGE: bab4_alur_chain_of_thought_prompting.png | Gambar 4.2: Diagram Alur Chain-of-Thought (CoT) Prompting: Mengajak AI Bernalar Selangkah demi Selangkah]]

### Prinsip Dasar Chain-of-Thought (CoT) Prompting
Teknik **Chain-of-Thought (CoT) Prompting** pertama kali dirumuskan oleh para peneliti kecerdasan artifisial (Wei et al., 2022). Inti dari teknik ini sangat sederhana namun revolusioner: **Instruksikan model AI untuk menguraikan rantai pemikiran penalarannya secara bertahap selangkah demi selangkah (*step-by-step reasoning*) sebelum menuliskan jawaban final!**

Perhatikan perbandingan konkret berikut:

#### 1. Prompt Biasa (Tanpa CoT) - Rawan Halusinasi:
* **Prompt Murid:** *"Sebuah mobil melaju menempuh jarak 135 km dalam waktu 2 jam 15 menit. Berapakah kecepatan rata-ratanya?"*
* **Respon AI yang Terburu-buru:** *"Kecepatan rata-rata mobil adalah 65 km/jam."* (SALAH! AI sering bingung membagi menit dengan jam).

#### 2. Prompt dengan Chain-of-Thought (CoT) - Akurat & Mendidik:
* **Prompt Murid Berpikir Kritis:**
  > *"Bertindaklah sebagai guru fisika dan sains komputasi yang teliti. Selesaikan soal kecepatan mobil berikut dengan menguraikan langkah penalarannya selangkah demi selangkah:*
  > *Langkah 1: Konversikan waktu 2 jam 15 menit menjadi bentuk jam desimal murni.*
  > *Langkah 2: Tuliskan rumus fisika kecepatan rata-rata (v = s / t).*
  > *Langkah 3: Lakukan operasi pembagian secara rinci.*
  > *Langkah 4: Tuliskan kesimpulan akhir beserta satuannya.*
  > *Jarak tempuh = 135 km, Waktu = 2 jam 15 menit."*
* **Respon AI Terstruktur (CoT):**
  > *Langkah 1: 15 menit diubah ke jam: 15 / 60 = 0.25 jam. Maka total waktu t = 2 + 0.25 = 2.25 jam.*
  > *Langkah 2: Rumus kecepatan rata-rata: v = s / t.*
  > *Langkah 3: Perhitungan matematis: v = 135 / 2.25 = 60.*
  > *Langkah 4: Kesimpulan: Kecepatan rata-rata mobil tersebut adalah tepat 60 km/jam.*

Dengan memecah instruksi ke dalam urutan rantai berpikir (*chain of thought*), kita memaksa model AI mengalokasikan ruang pemrosesan token untuk memverifikasi kebenaran setiap tahap. Tingkat akurasi pemecahan masalah logika meningkat drastis hingga lebih dari 80%!

---

## C. MEMBEDAH REKAYASA SOSIAL (SOCIAL ENGINEERING) & PHISHING SIBER

Sebagian besar orang mengira bahwa pembobolan sistem komputer selalu terjadi karena peretas jenius mengetikkan kode virus rahasia di layar gelap. Padahal kenyataan di dunia keamanan siber justru sebaliknya: **Titik terlemah dalam benteng pertahanan digital bukanlah mesin komputer, melainkan manusia yang mengoperasikannya!**

Metode manipulasi psikologis manusia untuk mencuri informasi rahasia ini dinamakan **Rekayasa Sosial (*Social Engineering*)**.

[[IMAGE: bab4_infografis_social_engineering_phishing.png | Gambar 4.3: Anatomi Serangan Rekayasa Sosial (Social Engineering) & Rumus Deteksi Phishing]]

### Empat Senjata Manipulasi Psikologis Pelaku Kejahatan Siber
Para penjahat siber mengeksploitasi emosi dasar manusia untuk meruntuhkan akal sehat dan nalar kritis korban:
1. **Menciptakan Kepanikan Ekstrem (*Urgency & Panic*):**  
   *'Peringatan Keamanan! Akun media sosial Anda telah dilaporkan melakukan pelanggaran! Akun akan dihapus permanen dalam 10 menit jika Anda tidak mengonfirmasi kata sandi Anda di tautan ini!'* Korban yang panik kehilangan kemampuan berpikir jernih dan buru-buru memasukkan kata sandinya.
2. **Memicu Keserakahan & Euforia Palsu (*Greed & Excitement*):**  
   Memberikan iming-iming hadiah uang tunai ratusan juta, sepeda motor gratis, atau item game langka tanpa usaha apa pun.
3. **Menyamar Sebagai Figur Otoritas Resmi (*Authority Impersonation*):**  
   Pelaku memasang logo resmi perbankan, kepolisian, kementerian pendidikan, atau perusahaan kurir paket ternama untuk meyakinkan korban.
4. **Memanfaatkan Rasa Penasaran & Empati (*Curiosity & Sympathy*):**  
   Mengirimkan pesan berisi cerita fiktif kecelakaan teman dekat atau dokumen unduhan berkedok surat undangan pernikahan digital palsu (file berekstensi *.APK* jahat) yang jika diunduh akan menyadap seluruh isi pesan ponsel korban!

### Mengenal Jebakan Pancingan: Phishing
Istilah **Phishing** berasal dari kata *fishing* (memancing). Penjahat menyebarkan "umpan pancing" berupa tautan palsu secara massal. Begitu ada korban yang memakan umpan tersebut dan memasukkan nama pengguna serta kata sandi pada formulir tiruan, data tersebut langsung terkirim ke komputer peretas.

Rumus Praktis Deteksi Phishing bagi Remaja:
* **Periksa Nama Domain (URL):** Jangan terkecoh tampilan halaman! Perhatikan tulisan di bilah alamat peramban. Pelaku sering menggunakan salah eja sengaja (*typosquatting*), misalnya `www.g00gle.com` atau `www.bank-nusantara-resmi.cc`.
* **Ketiadaan Ikon Gembok Enkripsi (HTTPS):** Situs resmi perbankan dan sekolah selalu menggunakan protokol aman HTTPS dengan sertifikat digital yang valid.
* **Tuntutan Kode Rahasia:** Layanan resmi apa pun di dunia tidak akan pernah meminta kode **One-Time Password (OTP)** atau PIN transaksi rahasia kalian melalui pesan obrolan biasa!

---

## D. JEJAK DIGITAL (DIGITAL FOOTPRINT): PASIF VS AKTIF

Setiap kali kalian menyalakan perangkat elektronik dan berselancar di dunia maya, kalian tidak pernah benar-benar tak terlihat. Seperti seseorang yang berjalan di atas hamparan pasir pantai yang basah, setiap langkah kalian meninggalkan jejak yang nyata dan abadi, yang dikenal dengan istilah **Jejak Digital (*Digital Footprint*)**.

[[IMAGE: bab4_diagram_jejak_digital_remaja.png | Gambar 4.4: Jejak Digital (Digital Footprint): Perbedaan Jejak Pasif vs Aktif dan Dampak Jangka Panjangnya]]

### Membedah Dua Jenis Jejak Digital:
1. **Jejak Digital Pasif (Ditinggalkan Tanpa Sadar):**  
   Data yang terekam secara otomatis oleh server internet di latar belakang saat kalian mengunjungi sebuah situs web:
   * Alamat IP (*Internet Protocol*) perangkat dan perkiraan lokasi kota tempat kalian berada.
   * Jenis peramban web dan sistem operasi yang kalian gunakan.
   * Berkas pelacak (*cookies*) yang mencatat barang apa saja yang pernah kalian lihat di toko daring atau berapa menit kalian menonton video komedi tertentu.
2. **Jejak Digital Aktif (Ditinggalkan Secara Sadar):**  
   Data yang secara sengaja kalian unggah dan bagikan ke ruang publik digital:
   * Unggahan foto, video *reels*, dan status di media sosial.
   * Komentar, kritik, dan perdebatan di kolom komentar forum publik.
   * Riwayat pesan dalam obrolan grup terbuka.

> **Wawasan Koder: Pepatah 'Internet Never Forgets' (Internet Tak Pernah Lupa)**  
> Meskipun kalian telah menekan tombol "Hapus Postingan" pada akun media sosial kalian, konten tersebut sangat mungkin telah disimpan tangkapan layarnya (*screenshot*) oleh orang lain, diarsipkan oleh mesin pencari web, atau disimpan di server penyedia layanan.  
> Banyak universitas bergengsi dunia dan perusahaan multinasional saat ini melakukan pemeriksaan riwayat jejak digital (*digital background check*) pada para calon penerima beasiswa dan karyawan. Komentar penuh kebencian, perundungan siber (*cyberbullying*), atau lelucon kasar yang diunggah saat kalian duduk di bangku SMP bisa saja menjadi penghalang impian kalian meraih beasiswa sepuluh tahun yang akan datang!

---

## E. MERANCANG BENTENG KEAMANAN AKUN KELUARGA: KATA SANDI KUAT & 2FA

Sebagai generasi melek komputasi di keluarga, kalian memiliki peran mulia menjadi pahlawan pelindung digital bagi orang tua, adik, dan kakek-nenek di rumah. Salah satu cara paling efektif mencegah pembobolan akun adalah menerapkan standar keamanan otentikasi ganda.

### Rumus Merancang Kata Sandi yang Tangguh
Hindari menggunakan kata sandi lemah yang mudah ditebak oleh peretas menggunakan perangkat lunak otomatis (*dictionary attack*), seperti: `123456`, `password`, atau tanggal lahir kalian `01012012`.

Gunakan rumus **Frasa Sandi Unik (*Passphrase*)**:
* Panjang minimal 12 karakter.
* Gabungkan huruf kapital, huruf kecil, angka, dan simbol khusus.
* Gunakan kalimat unik yang hanya kalian yang tahu maknanya.  
  Contoh: *"Kucing_Hitam#Melompat2025!"* (Sangat mudah diingat di kepala kalian, namun butuh waktu miliaran tahun bagi komputer peretas untuk menebaknya!).

### Mengaktifkan Otentikasi Dua Faktor (Two-Factor Authentication / 2FA)
Kunci pintu rumah yang hanya memiliki satu gembok mudah dibobol jika kunci tiruannya dicuri. Konsep **Two-Factor Authentication (2FA)** menambahkan gembok kedua yang terpisah:
1. **Faktor 1: Sesuatu yang Kalian Tahu (*Something You Know*):** Kata sandi atau PIN akun kalian.
2. **Faktor 2: Sesuatu yang Kalian Miliki (*Something You Have*):** Ponsel fisik kalian yang menerima kode OTP sekali pakai atau aplikasi autentikator (*Google Authenticator*).

Bahkan jika ada peretas jahat yang berhasil mencuri kata sandi akun kalian melalui tautan phishing, peretas tersebut tetap tidak akan bisa masuk ke dalam akun kalian karena mereka tidak memegang ponsel fisik kalian untuk membaca kode faktor kedua!

---

## F. LKPD PLUGGED 4.1: PROYEK CAPSTONE BOOKLET KEAMANAN SIBER KELUARGA

### Proyek Kolaboratif Akhir Fase D Kelas VIII (Capstone Mini-Project)
* **Produk Akhir:** Booklet Digital / Infografis Cetak 4 Halaman Berjudul: *"Pedoman Cerdas Keluarga Tangguh Siber & Bebas Penipuan Digital"*.
* **Sasaran Pembaca:** Orang tua, anggota keluarga di rumah, dan masyarakat sekitar lingkungan sekolah.
* **Alokasi Waktu:** 4 JP (2 Pertemuan Praktik & Presentasi Karya).

### Struktur Rancangan Halaman Booklet:
1. **Halaman 1 (Sampul Depan Memikat):** Judul menarik, ilustrasi pencegahan penipuan online, dan identitas kelompok siswa.
2. **Halaman 2 (Anatomi Penipuan Online & Ciri Phishing):** Uraian visual mengenai ciri-ciri pesan penipuan WhatsApp, bahaya file APK jahat, dan cara memeriksa alamat situs resmi.
3. **Halaman 3 (Panduan Praktis Mengamankan Akun):** Langkah demi langkah mengaktifkan fitur Verifikasi Dua Langkah (2FA) pada aplikasi WhatsApp dan akun Google keluarga.
4. **Halaman 4 (Etika Jejak Digital & Nomor Kontak Darurat):** Pesan moral tentang menjaga martabat diri di media sosial, serta daftar nomor kontak darurat pengaduan kejahatan siber resmi kepolisian dan perbankan.

### Rubrik Penilaian Proyek Capstone:
| Kriteria Penilaian | Indikator Sangat Mahir (Skor 85-100) | Indikator Mahir (Skor 70-84) | Indikator Cukup (Skor 60-69) |
| :--- | :--- | :--- | :--- |
| **Keakuratan Materi Siber** | Penjelasan phishing, rekayasa sosial, dan 2FA sangat tepat dan mendalam | Konsep siber dijelaskan dengan benar, sedikit kekurangan pada detail teknis | Penjelasan masih bersifat umum dan ada kekeliruan konsep |
| **Kualitas Bahasa & Visual** | Bahasa santai mudah dipahami orang tua, tata letak visual sangat menarik | Bahasa cukup komunikatif, tata letak rapi | Teks terlalu padat dan sulit dibaca oleh orang awam |
| **Pemanfaatan AI Analitis** | Menggunakan Chain-of-Thought Prompting untuk menyusun tips praktis | Menggunakan prompt standar untuk mencari materi tambahan | Tidak memanfaatkan asisten AI dalam proses pengerjaan |
| **Dampak Sosial Keluarga** | Booklet telah diujicobakan dan dipraktikkan langsung bersama orang tua | Booklet telah ditunjukkan kepada anggota keluarga | Booklet baru sebatas rancangan di laboratorium komputer |

---

## POJOK KARAKTER & ETIKA KODER: MENJAGA MARTABAT DIRI DI RUANG MAYA

Di balik anonimitas layar monitor dan papan ketik komputer, terkadang ada godaan besar untuk ikut-ikutan berkomentar kasar, menyebarkan rahasia teman (*doxing*), atau melontarkan ejekan yang menyakitkan hati orang lain. Ingatlah selalu bahwa di balik setiap akun media sosial yang kalian komentari, ada manusia sejati yang memiliki perasaan dan harga diri.

Seorang koder dan pembelajar yang berakhlak mulia selalu memegang teguh prinsip **Integritas Digital**. Jadikan jari-jemari kalian di atas keyboard sebagai pena yang mengalirkan kata-kata penyemangat, inspirasi ilmu pengetahuan, dan perlindungan bagi sesama. Kehormatan dan martabat sejati kalian tidak ditentukan oleh berapa banyak pujian semu di media sosial, melainkan oleh ketulusan budi pekerti kalian saat tidak ada orang lain yang melihat!

---

## RANGKUMAN MATERI BAB 4

1. **Chain-of-Thought (CoT) Prompting** adalah teknik rekayasa masukan pada AI yang memandu model untuk menguraikan proses penalaran bertahap selangkah demi selangkah, sangat terbukti meminimalisasi kesalahan logika dan halusinasi komputasi.
2. **Rekayasa Sosial (*Social Engineering*)** adalah manipulasi psikologis yang mengeksploitasi kepanikan, keserakahan, dan rasa penasaran manusia demi mencuri informasi berharga.
3. **Phishing** merupakan bentuk serangan siber menggunakan tautan tiruan palsu untuk memancing korban menyerahkan data sensitif seperti sandi dan kode OTP.
4. **Jejak Digital (*Digital Footprint*)** terbagi menjadi jejak pasif (alamat IP dan cookies) serta jejak aktif (unggahan foto dan komentar publik) yang bersifat permanen di ruang siber.
5. **Benteng Keamanan Akun** dibangun melalui perancangan *Passphrase* yang panjang dan rumit serta pengaktifan *Two-Factor Authentication (2FA)* sebagai gembok pertahanan ganda.

---

## UJI PEMAHAMAN HOTS BAB 4

### I. Pilihan Ganda (Pilihlah Jawaban yang Paling Tepat!)

1. Keunggulan utama dari penerapan teknik *Chain-of-Thought (CoT) Prompting* dibanding prompt instruksi langsung saat menyelesaikan soal analisis rumit dengan AI adalah...
   A. Waktu yang dibutuhkan AI untuk menjawab menjadi seratus kali lebih singkat  
   B. Model AI dipandu menguraikan langkah-langkah logika penalaran secara bertahap sehingga meminimalisasi kesalahan halusinasi angka  
   C. Menghilangkan kebutuhan sambungan internet saat mengakses server AI  
   D. Mengubah otomatis seluruh teks respon AI menjadi file animasi video 3D  

2. Fajar menerima pesan SMS: *"Akun perbankan Anda diblokir! Segera klik www.bca-verifikasi-darurat.xyz untuk aktivasi kembali dalam 15 menit!"* Taktik rekayasa sosial yang sedang dilancarkan oleh pelaku adalah...
   A. Mengeksploitasi rasa panik korban dengan batasan waktu yang mendesak (*Urgency & Panic*)  
   B. Menawarkan beasiswa pendidikan perguruan tinggi  
   C. Menghibur korban dengan video komedi  
   D. Memberikan bantuan pulsa gratis secara sukarela  

3. Manakah di antara pilihan alamat situs web berikut yang mengindikasikan adanya indikasi kuat jebakan *Phishing (Typosquatting)*?
   A. `https://kemdikbud.go.id/portal`  
   B. `https://www.instagr4m-login-keamanan.cc/auth`  
   C. `https://scratch.mit.edu/projects`  
   D. `https://unipar.ac.id/profil`  

4. Seseorang yang berselancar di internet meninggalkan jejak alamat IP perangkat, jenis sistem operasi, dan riwayat situs yang dikunjungi secara otomatis oleh server web. Jejak jenis ini dikategorikan sebagai...
   A. Jejak Digital Aktif  
   B. Jejak Digital Pasif  
   C. Jejak Komersial Berbayar  
   D. Jejak Fisik Lingkungan  

5. Mengapa mengunggah foto kartu identitas (KTP/Kartu Pelajar) atau tiket pesawat ke media sosial merupakan tindakan yang sangat berbahaya?
   A. Karena dapat menghabiskan kuota internet pengikut akun kita  
   B. Karena memuat data pribadi sensitif (NIK, nama lengkap, tanggal lahir, dan barcode) yang dapat dieksploitasi penjahat untuk pinjaman online ilegal atau pencurian identitas  
   C. Karena warna kartu identitas tidak sesuai dengan tema profil media sosial  
   D. Karena ukuran resolusi foto kartu identitas terlalu kecil  

6. Manakah dari pilihan kombinasi kata sandi berikut yang memenuhi standar *Passphrase* tangguh dan paling sulit dibobol peretas?
   A. `12345678`  
   B. `admin2025`  
   C. `Keluarga_Harmonis#99Lestari!`  
   D. `rahasia`  

7. Konsep keamanan *Two-Factor Authentication (2FA)* melindungi akun pengguna karena mengharuskan verifikasi berdasarkan dua hal, yaitu...
   A. Dua buah kata sandi yang diketik pada waktu yang sama persis  
   B. Sesuatu yang diketahui pengguna (kata sandi) dan sesuatu yang dimiliki secara fisik oleh pengguna (perangkat ponsel / kode OTP)  
   C. Dua nama teman sekelas yang wajib dituliskan di kolom komentar  
   D. Dua aplikasi peramban web yang dibuka secara bersamaan di komputer  

8. Sebuah pesan WhatsApp dari nomor asing mengirimkan berkas dokumen dengan nama `SuratUndanganPernikahan.apk`. Tindakan paling bijak dan aman yang harus diambil adalah...
   A. Segera mengunduh dan memasang aplikasi tersebut agar bisa membaca undangannya  
   B. Meneruskan berkas tersebut ke seluruh grup obrolan kelas  
   C. Jangan pernah mengklik atau memasang berkas tersebut, segera hapus pesan dan blokir nomor pengirimnya  
   D. Mengubah ekstensi file dari .APK menjadi file video MP4  

9. Fakta bahwa rekam jejak komentar kasar dan unggahan masa lalu di internet dapat ditemukan kembali oleh calon pemberi beasiswa perguruan tinggi di masa depan mencerminkan prinsip...
   A. Internet Bersifat Anonim Selamanya  
   B. Internet Tak Pernah Lupa (*Internet Never Forgets*)  
   C. Hak Cipta Perangkat Lunak Tertutup  
   D. Pemrograman Berorientasi Objek  

10. Tindakan membongkar dan menyebarkan data pribadi seseorang (seperti alamat rumah dan nomor ponsel keluarga) ke forum publik maya tanpa izin demi memicu perundungan disebut...
    A. Phishing  
    B. Doxing  
    C. Debugging  
    D. Prompting  

---

### II. Uraian Pemecahan Masalah (Jawablah Secara Rinci dan Terstruktur!)

1. Jelaskan bagaimana mekanisme teknik *Chain-of-Thought (CoT) Prompting* bekerja dalam meningkatkan ketepatan penalaran model AI! Tuliskan satu contoh prompt bertingkat untuk membantu siswa memecahkan persoalan konversi satuan kecepatan internet!
2. Mengapa manusia sering kali disebut sebagai "mata rantai terlemah" (*the weakest link*) dalam sistem keamanan siber? Berikan dua contoh nyata taktik manipulasi psikologis yang digunakan pelaku kejahatan siber!
3. Uraikan perbedaan mendasar antara Jejak Digital Pasif dan Jejak Digital Aktif! Mengapa seorang remaja wajib berhati-hati dalam meninggalkan jejak digital aktif di ruang media sosial?
4. Jelaskan cara kerja sistem keamanan *Two-Factor Authentication (2FA)*! Mengapa akun yang telah mengaktifkan 2FA tetap terlindungi meskipun kata sandi utamanya berhasil diketahui oleh pelaku phishing?
5. Anda mendapati bahwa salah satu anggota keluarga di rumah (misalnya kakek atau adik) baru saja menerima pesan undian berhadiah mencurigakan di ponselnya. Langkah-langkah edukasi dan teknis apa saja yang akan kalian lakukan untuk mengamankan perangkat mereka dari potensi kejahatan digital?

---

## EVALUASI SUMATIF AKHIR TAHUN FASE D KELAS VIII
*(Paket Evaluasi Komprehensif Mengintegrasikan Materi Bab 1, 2, 3, dan 4)*

### I. Pilihan Ganda Komprehensif (15 Soal)

1. Dalam perancangan algoritma simulator kebakaran hutan, jika helikopter harus terus menyiram air selama variabel `ApiMenyala == True` dan `VolumeAir > 0`, maka jenis struktur kontrol yang digunakan adalah...
   A. Percabangan Tunggal (Single If)  
   B. Perulangan Bersyarat (Conditional While Loop) dengan Operator AND  
   C. Perulangan Terhitung (Counted Loop) 5 Kali  
   D. Percabangan Bersarang tanpa Operator Logika  

2. Perhatikan blok ekspresi logika: `Hasil = not (A or B)`. Jika `A = True` dan `B = False`, berapakah nilai dari `Hasil`?
   A. True  
   B. False  
   C. Null  
   D. Error  

3. Memecah blok program game yang rumit menjadi beberapa *Custom Blocks* berparameter mandiri merupakan penerapan pilar berpikir komputasional, yaitu...
   A. Abstraksi dan Dekomposisi  
   B. Pengenalan Pola saja  
   C. Penulisan Kode Spaghetti  
   D. Pencarian Biner  

4. Pada alur produksi podcast edukasi, pembuatan naskah obrolan 5 babak dan pengisian formulir *Informed Consent* dilaksanakan pada...
   A. Fase Pascaproduksi  
   B. Fase Pra-Produksi  
   C. Fase Rendering Media  
   D. Fase Siaran Langsung  

5. Fitur pada software editor video yang secara otomatis mengecilkan volume musik latar saat narator mulai berbicara dinamakan...
   A. Noise Reduction  
   B. Audio Ducking  
   C. Speech to Text  
   D. Keyframing  

6. Mengapa penyertaan takarir teks (*subtitles*) pada video pembelajaran digital merupakan perwujudan prinsip inklusivitas sosial?
   A. Menjamin akses kesetaraan belajar bagi sahabat teman tuli dan penonton di lingkungan yang bising  
   B. Agar video dapat diputar tanpa kartu memori  
   C. Mempercepat proses ekspor video pada komputer  
   D. Mengurangi penggunaan kapasitas baterai ponsel penonton  

7. Kelemahan mendasar dari kamera optik RGB konvensional pada drone penyelamat saat beroperasi di tengah kabut tebal pegunungan adalah...
   A. Lensa kamera akan langsung pecah jika terkena uap air  
   B. Hamburan cahaya tampak pada partikel kabut menyebabkan gambar kehilangan kontras visual (*blind spot*)  
   C. Memori kamera hanya mampu merekam gambar berwarna hitam-putih  
   D. Kamera optik tidak dapat bekerja jika dihubungkan dengan mikrokontroler  

8. Peran utama komponen *Analog-to-Digital Converter (ADC)* dalam sistem penginderaan mesin cerdas adalah...
   A. Menyimpan file video ke dalam keping CD  
   B. Mengubah fluktuasi sinyal voltase fisik analog menjadi kode biner diskrit 0 dan 1  
   C. Mendinginkan suhu prosesor komputer saat bekerja keras  
   D. Memutar baling-baling motor drone secara mekanik  

9. Jika model kecerdasan artifisial dilatih menggunakan dataset yang bising (*noisy data*) dan timpang (*imbalanced*), maka luaran keputusan sistem akan mengalami...
   A. Peningkatan kecepatan komputasi hingga seratus kali lipat  
   B. Bias Algoritma dan rentan menghasilkan keputusan yang keliru serta tidak adil (*GIGO*)  
   C. Transformasi otomatis menjadi kecerdasan umum buatan (AGI)  
   D. Penurunan suhu perangkat keras komputer secara permanen  

10. Penerapan prinsip *Algorithmic Fairness* dalam pengembangan AI bertujuan untuk...
    A. Memastikan perusahaan pembuat software mendapatkan keuntungan finansial terbesar  
    B. Menjamin bahwa sistem cerdas memberikan keputusan yang adil, setara, dan bebas dari diskriminasi terhadap seluruh kelompok manusia  
    C. Melarang masyarakat menggunakan teknologi kecerdasan artifisial  
    D. Mengganti seluruh tenaga guru manusia dengan robot pintar  

11. Perbedaan mendasar antara prompt biasa dengan teknik *Chain-of-Thought (CoT) Prompting* adalah...
    A. CoT mengharuskan instruksi ditulis dalam bahasa pemrograman C++  
    B. CoT memandu model AI untuk menguraikan tahapan nalar logikanya selangkah demi selangkah sebelum menuliskan kesimpulan  
    C. CoT hanya dapat digunakan pada komputer berharga mahal  
    D. CoT mengubah suara pengguna menjadi gambar animasi secara langsung  

12. Rekayasa sosial (*Social Engineering*) pada hakikatnya merupakan serangan keamanan siber yang menargetkan kerentanan pada...
    A. Sirkuit kabel tembaga internet bawah laut  
    B. Psikologis dan perilaku manusia pengguna teknologi  
    C. Lapisan pendingin prosesor laptop  
    D. Antena pemancar sinyal satelit luar angkasa  

13. Manakah di antara kombinasi berikut yang mencerminkan penerapan *Two-Factor Authentication (2FA)* yang benar?
    A. Memasukkan kata sandi akun email, kemudian memasukkan tanggal lahir sendiri  
    B. Memasukkan kata sandi akun (faktor pengetahuan), lalu memasukkan kode OTP dari aplikasi authenticator di ponsel fisik (faktor kepemilikan)  
    C. Mengetikkan kata sandi yang sama sebanyak dua kali di dua jendela browser berbeda  
    D. Membagikan kata sandi kepada dua orang teman sekelas yang dipercaya  

14. Mengapa jejak digital aktif seperti unggahan status bernada kebencian di media sosial dapat berdampak buruk hingga sepuluh tahun ke depan?
    A. Karena server internet akan otomatis meledak jika menyimpan data lama  
    B. Karena jejak digital bersifat abadi (*Internet Never Forgets*) dan dapat diakses saat proses seleksi beasiswa atau rekrutmen kerja profesional di masa depan  
    C. Karena ukuran file teks komentar di internet sangat berat  
    D. Karena aturan internasional melarang orang menghapus akun media sosial  

15. Praktik menyebarkan data pribadi narasumber tanpa persetujuan yang sah melanggar prinsip etika penyiaran, yaitu...
    A. Open Source License  
    B. Informed Consent  
    C. Modular Programming  
    D. Sensor Fusion  

---

### II. Uraian Kasus Studi Terpadu (5 Soal Analisis Kasus HOTS)

1. **Kasus 1 (Berpikir Komputasional & Pemrograman Modular):**  
   Tim koder SMP Nusantara sedang merancang game edukasi simulasi mitigasi gempa bumi. Karakter relawan harus mengevakuasi korban dengan ketentuan:
   * Jika relawan berada di dekat korban DAN kapasitas tandu belum penuh, masukkan korban ke tandu.
   * Jika tandu telah penuh, relawan harus membawanya ke posko medis terdekat dan mengosongkan tandu kembali.
   Rancanglah algoritma logika program tersebut menggunakan percabangan bersarang (*Nested If*) dan buatlah sebuah *Custom Block* berparameter `EvakuasiKorban(JumlahKorban, StatusTandu)`!

2. **Kasus 2 (Literasi Digital & Produksi Podcast):**  
   Kelompok Ayu akan memproduksi siniar video berdurasi 5 menit mengenai bahaya kecanduan game daring. Susunlah rancangan pembagian trek pada *Multi-Track Timeline* penyuntingan video (dari Track 1 hingga Track 5) agar hasil tayangan rapi, indah, dan ramah bagi teman-teman berkebutuhan khusus!

3. **Kasus 3 (Literasi KA & Sensor Fusion):**  
   Jelaskan bagaimana sebuah mobil pemadam kebakaran otonom masa depan memanfaatkan konsep *Sensor Fusion* (menggabungkan data sensor kamera termal, sensor gas karbon monoksida, dan radar ultrasonik) untuk memutuskan rute penyelamatan terbaik di dalam gedung yang terbakar pekat!

4. **Kasus 4 (Etika KA & Kualitas Data):**  
   Sebuah model AI pengenal suara bel sekolah cerdas diuji coba di laboratorium yang sangat hening dan berhasil 100%. Namun saat dipasang di lorong sekolah yang ramai oleh suara gelak tawa siswa saat istirahat, sistem bel cerdas tersebut mendadak sering berbunyi sendiri tanpa instruksi. Analisislah akar masalah kegagalan sistem tersebut berlandaskan konsep *Noisy Data* dan *Domain Shift*, serta rumuskan solusinya!

5. **Kasus 5 (Keamanan Siber & Investigasi Rekayasa Sosial):**  
   Rian menerima pesan dari seseorang yang mengaku sebagai panitia lomba olimpiade koding nasional. Orang tersebut meminta Rian mengirimkan tangkapan layar kode verifikasi SMS (OTP) yang baru saja masuk ke ponselnya dengan dalih "untuk memverifikasi keaslian nomor peserta lomba". Jelaskan langkah-langkah investigasi kritis yang harus dilakukan Rian untuk membuktikan bahwa pesan tersebut adalah upaya peretasan, serta tindakan preventif apa yang wajib diambil!

---

## KUNCI JAWABAN EVALUASI SUMATIF AKHIR TAHUN KELAS VIII

### Kunci Jawaban Pilihan Ganda Komprehensif:
1. **B** (Perulangan bersyarat While dengan operator logika AND mengontrol pengulangan aksi pemadaman selama dua syarat terpenuhi bersamaan).
2. **B** (`A or B` -> `True or False` = `True`. `not (True)` = `False`).
3. **A** (Membagi program rumit menjadi fungsi modular berparameter adalah wujud dekomposisi dan abstraksi koding).
4. **B** (Penyusunan naskah script dan penandatanganan informed consent dilakukan pada fase Pra-Produksi sebelum perekaman dimulai).
5. **B** (*Audio Ducking* adalah teknik mixing otomatis untuk menurunkan volume instrumen pengiring saat ada suara manusia).
6. **A** (Takarir teks memastikan hak aksesibilitas belajar yang setara bagi sahabat teman tuli).
7. **B** (Partikel air pada kabut menyebarkan gelombang cahaya tampak sehingga kamera optik kehilangan kejernihan visual).
8. **B** (ADC bertugas mencuplik dan mengonversi sinyal voltase fisik analog menjadi data biner diskrit komputer).
9. **B** (Prinsip GIGO: Data latih yang bising dan timpang melahirkan bias algoritma yang membahayakan keandalan sistem).
10. **B** (*Algorithmic Fairness* menjamin perancangan sistem cerdas yang memperlakukan semua orang secara adil dan bebas diskriminasi).
11. **B** (Teknik Chain-of-Thought mengajak AI bernalar selangkah demi selangkah untuk meminimalisasi kesalahan halusinasi logika).
12. **B** (Rekayasa sosial mengeksploitasi celah psikologis rasa panik, penasaran, dan keserakahan manusia).
13. **B** (2FA memadukan faktor pengetahuan kata sandi dan faktor kepemilikan fisik perangkat ponsel / OTP).
14. **B** (Jejak digital bersifat permanen dan terekam di internet sehingga dapat ditelusuri di masa depan).
15. **B** (*Informed Consent* adalah mandat etika persetujuan narasumber atas penggunaan citra dan datanya).
"""
