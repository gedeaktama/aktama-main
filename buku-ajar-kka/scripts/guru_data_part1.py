# -*- coding: utf-8 -*-
"""
Modul Naskah Buku Panduan Guru KKA Kelas 5 SD - Bagian 1
Panduan Umum, Bab 1, Bab 2, dan Bab 3
Format Standar Kemendikdasmen RI & Pusbuk BSKAP
"""

GURU_FRONT_MATTER = """# PANDUAN GURU: KODING DAN KECERDASAN ARTIFISIAL
## BUKU PANDUAN GURU KELAS V SD/MI
### Mata Pelajaran Pilihan — Fase C

**Penulis:**  
Gede Erik Aktama, S.Pd., M.Pd.  
*(Fasilitator Nasional Koding dan Kecerdasan Artifisial Kemendikdasmen RI)*  
*(Dosen Lektor & Ketua Program Studi S1 Sistem Komputer, Universitas Parna Raya)*  

**Penelaah & Konsultan Teknis:**  
Tim Pengembang Kurikulum KKA Direktorat Guru Pendidikan Dasar Kemendikdasmen RI  

**Penerbit:**  
Pusat Perbukuan  
Badan Standar, Kurikulum, dan Asesmen Pendidikan  
Kementerian Pendidikan Dasar dan Menengah Republik Indonesia  
Tahun 2025 / 2026  

---

## IDENTITAS PENERBITAN
**Judul Buku:** Buku Panduan Guru: Koding dan Kecerdasan Artifisial untuk SD/MI Kelas V  
**Sasaran Pengguna:** Guru Pengampu Mata Pelajaran KKA Kelas V SD/MI (Fase C)  
**Penulis:** Gede Erik Aktama, S.Pd., M.Pd.  
**Penyunting / Editor:** Tim Fasilitator Bimtek KKA Kemendikdasmen  
**Ukuran Buku:** Format UNESCO Standar Buku Ajar (15,5 cm x 23,0 cm)  
**Dasar Hukum:** Permendikdasmen No. 13 Tahun 2025 & Permendikbudristek No. 22 Tahun 2022  

---

## KATA PENGANTAR KEMENDIKDASMEN
Puji syukur ke hadirat Tuhan Yang Maha Esa atas terbitnya Buku Panduan Guru Mata Pelajaran Pilihan Koding dan Kecerdasan Artifisial (KKA) untuk jenjang SD/MI Kelas V ini. Penerbitan buku ini menandai langkah historis pembaruan pendidikan dasar Indonesia dalam membekali generasi muda menghadapi era revolusi digital dan disrupsi kecerdasan artifisial.

Buku Panduan Guru ini dirancang khusus untuk mendampingi Bapak dan Ibu Guru di seluruh tanah air, baik yang telah memiliki latar belakang pendidikan informatika maupun para guru kelas yang baru pertama kali mengajarkan koding dan kecerdasan artifisial. Dengan memegang teguh filosofi *Pembelajaran Mendalam (Deep Learning)* yang berkesadaran, bermakna, dan menggembirakan, buku ini memandu pendidik menghadirkan pengalaman belajar sains komputasi yang ramah anak, berpusat pada nalar kritis, dan berakar pada nilai-nilai luhur Pancasila.

Kami menyampaikan apresiasi dan terima kasih setinggi-tingginya kepada Saudara Gede Erik Aktama, S.Pd., M.Pd. selaku Fasilitator Nasional beserta segenap tim pengembang yang telah bekerja keras menyusun karya monumental ini. Semoga buku ini menjadi suluh penerang bagi para guru perintis teknologi di setiap ruang kelas nusantara.

Jakarta, 2025  
**Direktur Jenderal Guru dan Tenaga Kependidikan**  
Kementerian Pendidikan Dasar dan Menengah Republik Indonesia

---

## PRAKATA PENULIS
Salam hangat dan salam perjuangan untuk seluruh Bapak dan Ibu Guru hebat di penjuru tanah air!

Mengajarkan Koding dan Kecerdasan Artifisial kepada peserta didik usia sekolah dasar bukanlah tentang mencetak pemrogram profesional dalam semalam, bukan pula tentang mewajibkan setiap sekolah memiliki laboratorium komputer yang mewah dan mahal. Inti sejati dari mata pelajaran KKA di sekolah dasar adalah **menumbuhkan kemerdekaan berpikir, melatih ketangkasan memecahkan masalah (problem-solving), dan membentuk kesadaran etis peserta didik sebagai tuan atas teknologi, bukan hamba teknologi**.

Buku Panduan Guru ini disusun dengan format praktis dan operasional untuk memandu langkah Bapak/Ibu guru di kelas:
1. Memberikan alternatif kegiatan belajar berimbang: **Aktivitas Unplugged (tanpa komputer)** yang memanfaatkan media manipulatif sederhana di sekitar sekolah, dan **Aktivitas Plugged (dengan komputer/laptop)** menggunakan platform edukatif gratis seperti Scratch dan Google Teachable Machine.
2. Menyajikan strategi **Pembelajaran Berdiferensiasi** untuk melayani keberagaman kecepatan belajar murid di kelas.
3. Melengkapi setiap bab dengan instrumen asesmen autentik, rubrik penilaian kinerja, serta pembahasan mendalam soal-soal Buku Siswa.

Semoga buku ini dapat menjadi sahabat setia Bapak/Ibu guru dalam menyalakan api kreativitas anak-anak Indonesia. Selamat menginspirasi!

Penulis,  
**Gede Erik Aktama, S.Pd., M.Pd.**  
*(Fasilitator Nasional KKA Kemendikdasmen RI)*  
*(Dosen Lektor & Kaprodi Sistem Komputer, Universitas Parna Raya)*

---

# BAGIAN 1: PETUNJUK UMUM PEMBELAJARAN

### A. Hakikat Mata Pelajaran Koding & Kecerdasan Artifisial di SD
Berdasarkan Permendikdasmen Nomor 13 Tahun 2025, Koding dan Kecerdasan Artifisial (KKA) merupakan mata pelajaran pilihan yang resmi diperkenalkan pada jenjang sekolah dasar mulai **Fase C (Kelas V dan VI)** dengan alokasi waktu ideal **2 Jam Pelajaran (JP) per minggu** (setara 72 JP dalam satu tahun ajaran).

KKA di jenjang SD tidak menekankan hafalan sintaks teks pemrograman yang rumit, melainkan berfokus pada 4 elemen esensial:
1. **Berpikir Komputasional (BK):** Landasan cara bernalar sistematis menggunakan 4 pilar (Dekomposisi, Pengenalan Pola, Abstraksi, Algoritma).
2. **Literasi Digital (LD):** Pengenalan fungsi perangkat digital, etika berkomunikasi, dan keamanan identitas pribadi di internet.
3. **Pemanfaatan Kecerdasan Artifisial (PKA):** Pemahaman konsep dasar cara kerja AI (pembelajaran dari data) dan pemanfaatannya secara bijak untuk membantu kehidupan sehari-hari.
4. **Koding & Algoritma (KA):** Penerjemahan logika algoritma ke dalam media visual (Scratch) untuk menciptakan animasi dan permainan edukasi interaktif.

---

### B. Capaian Pembelajaran (CP) dan Alur Tujuan Pembelajaran (ATP) Kelas V
Pada akhir Fase C, peserta didik mampu:
* Memahami dan menerapkan 4 pilar berpikir komputasional dalam menyelesaikan masalah terstruktur di lingkungan sekolah dan rumah secara logis dan kolaboratif.
* Mengenal arsitektur dasar sistem komputer (perangkat masukan, pemroses, keluaran, dan penyimpanan) serta menerapkan prinsip ergonomi dan kesehatan digital.
* Menjaga kerahasiaan data pribadi, kata sandi, dan menghindari jebakan perundungan siber (*cyberbullying*) serta penipuan digital (*phishing*).
* Menjelaskan konsep kecerdasan artifisial sebagai sistem buatan manusia yang belajar dari data, membedakannya dari kecerdasan alami manusia, serta menyadari pentingnya etika AI.
* Melakukan eksperimen pengumpulan dan klasifikasi data gambar/audio sederhana menggunakan platform AI visual (Teachable Machine).
* Menyusun program visual blok puzzle (Scratch) menggunakan runtutan logika, percabangan sederhana, dan perulangan untuk menghasilkan karya digital bermakna.

| Bab | Alokasi Waktu | Elemen CP | Fokus Pembelajaran |
|:---|:---|:---|:---|
| **Bab 1:** Berpikir Komputasional dan Pemecahan Masalah | 16 JP (8 Pertemuan) | Berpikir Komputasional (BK) | 4 Pilar BK, Dekomposisi tugas sekolah, Pengenalan Pola, Abstraksi, Algoritma rute, Debugging logika unplugged |
| **Bab 2:** Mengenal Teknologi Digital dan Perangkat Komputer | 12 JP (6 Pertemuan) | Literasi Digital (LD) | Dampak teknologi, Arsitektur komputer (Hardware, Software, Brainware), Praktik ergonomi sehat, Konten digital sehat |
| **Bab 3:** Menjaga Rahasia dan Keamanan Data Pribadi | 8 JP (4 Pertemuan) | Literasi Digital & Etika | Identitas pribadi vs publik, Formula kata sandi kuat, Waspada phishing, Etika bermedia sosial, Anti-cyberbullying |
| **Bab 4:** Mengenal Kecerdasan Artifisial (KA) | 12 JP (6 Pertemuan) | Pemanfaatan AI (PKA) | Definisi AI, Perbedaan AI vs Otomatisasi, Sensor dan persepsi mesin, Manfaat AI di Indonesia, Etika Human-Centered AI |
| **Bab 5:** Eksperimen Klasifikasi Data Bersama AI | 12 JP (6 Pertemuan) | Pemanfaatan AI & Data | Konsep Data dan Fitur, Pengumpulan dataset gambar, Latih model Teachable Machine, Uji akurasi, Bias data |
| **Bab 6:** Berkreasi dengan Koding Blok Visual & Gelar Karya | 12 JP (6 Pertemuan) | Koding & Algoritma (KA) | Lingkungan Scratch, Sprite, Event handler, Gerak, Perulangan, Proyek Capstone Game Animasi, Showcase Day |

---

### C. Implementasi Prinsip Pembelajaran Mendalam (Deep Learning)
Kemendikdasmen menekankan pendekatan Pembelajaran Mendalam (*Deep Learning*) yang berpusat pada 3 prinsip utama:
1. **Berkesadaran (Mindful):**
   * Guru mengawali sesi dengan mengajak murid menyadari napas, memfokuskan pikiran, dan merefleksikan peran mereka sebagai pengendali teknologi.
   * Murid diajak sadar bahwa setiap tombol yang ditekan dan setiap data yang dibagikan memiliki dampak nyata bagi diri sendiri dan orang lain.
2. **Bermakna (Meaningful):**
   * Setiap konsep koding dan AI selalu dikaitkan dengan konteks kehidupan nyata peserta didik (contoh: membersihkan sampah sekolah, merawat tanaman, mengamankan barang berharga di rumah).
   * Menghindari pengajaran rumus atau langkah koding yang terisolasi dari tujuan memecahkan masalah kemanusiaan/lingkungan.
3. **Menggembirakan (Joyful):**
   * Pembelajaran dikemas dalam bentuk permainan kartu edukatif (*unplugged games*), simulasi peran (*role-play*), petualangan eksplorasi, dan proyek kreatif bersama teman sebaya.
   * Kesalahan koding (*bug*) tidak dipandang sebagai kegagalan atau kebodohan, melainkan sebagai teka-teki seru yang mengasah rasa ingin tahu detektif cilik.

#### 3 Fase Pengalaman Belajar di Setiap Sesi:
* **Fase 1: Memahami (Apersepsi & Ekplorasi Makna):** Guru memantik dialog interaktif melalui cerita tokoh (Erik, Siti, Made, Robot Kibo) dan pertanyaan pemantik yang merangsang nalar kritis murid.
* **Fase 2: Mengaplikasikan (Aktivitas Konkret & Berkreasi):** Murid berkolaborasi dalam kelompok kecil menyelesaikan LKPD (bermain simulasi kartu algoritma, eksperimen input-output, atau merangkai balok kode).
* **Fase 3: Merefleksi (Konsolidasi & Evaluasi Diri):** Murid mengisi jurnal refleksi hatiku, saling memberikan umpan balik bintang apresiasi, dan menarik hikmah nilai karakter.

---

### D. Manajemen Pembelajaran Kelas Berfasilitas Terbatas (Unplugged vs Plugged)
Salah satu tantangan terbesar guru di daerah adalah keterbatasan jumlah komputer atau akses jaringan internet di sekolah. Bapak/Ibu guru TIDAK PERLU BERKECIL HATI. 

**Panduan Pengaturan Praktik:**
1. **Sekolah Tanpa Komputer / Lab Terbatas:**
   * Seluruh aktivitas Bab 1, 2, dan 3 dapat dilakukan 100% secara **Unplugged** menggunakan papan tulis, kertas karton warna, kardus bekas, dan kartu instruksi panah.
   * Untuk Bab 4 dan 5, konsep AI dapat disimulasikan melalui permainan peran *"Komputer Cerdas vs Komputer Buta"* di mana murid memerankan algoritma pengenalan pola kartu fitur gambar.
   * Untuk Bab 6, konsep logika blok Scratch dapat dipraktikkan menggunakan potongan balok puzzle kertas karton warna (*Paper Scratch*).
2. **Sekolah dengan Rasio Komputer Terbatas (1 komputer untuk 3-4 murid):**
   * Terapkan strategi **Pair Programming (Pemrograman Berpasangan)**: satu murid berperan sebagai *Driver* (memegang mouse/keyboard), murid lainnya berperan sebagai *Navigator* (membaca rancangan alur program dan memandu logika). Peran ditukar setiap 15 menit.
3. **Sekolah dengan Fasilitas Lengkap (1 murid 1 perangkat):**
   * Tetap dahului dengan aktivitas *unplugged* selama 15-20 menit pertama untuk mematangkan konsep logika berpikir sebelum murid membuka layar laptop. Terlalu cepat membuka laptop sering kali membuat fokus murid terdistraksi oleh tampilan visual tanpa memahami esensi logikanya.

---

### E. Strategi Pembelajaran Berdiferensiasi
Di dalam satu rombongan belajar kelas 5, guru akan menemukan keragaman profil belajar murid yang mencolok:
1. **Diferensiasi Konten:**
   * Murid yang membutuhkan bimbingan diberikan contoh kasus sederhana dengan instruksi visual langsung bertahap (scaffolding).
   * Murid yang mahir diberikan tantangan eksplorasi logika percabangan ganda atau penambahan variabel skor.
2. **Diferensiasi Proses:**
   * Murid kinestetik belajar algoritma dengan melangkahkan kaki di atas ubin lantai berpola.
   * Murid visual belajar dengan membuat diagram alir (*flowchart*) bergambar warna-warni.
   * Murid auditori belajar dengan mendiskusikan cerita kasus dan membacakan skenario naskah game.
3. **Diferensiasi Produk:**
   * Murid dapat memilih bentuk unjuk kerja tugas akhir: membuat poster fisik kampanye internet aman, membuat komik strip digital, atau mendemonstrasikan game interaktif Scratch di depan kelas.
"""
