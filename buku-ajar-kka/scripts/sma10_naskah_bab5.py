"""
Modul Naskah Bab V Kelas X SMA/SMK (Fase E)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB5_SMA10 = """# BAB V: PENGENALAN CITRA DIGITAL (COMPUTER VISION) DAN POLA AUDIO AI

## APERSEPSI: BAGAIMANA KOMPUTER "MELIHAT" DAN "MENDENGAR"?

Di sudut bengkel rekayasa perangkat lunak dan elektronika SMK, Bagas tampak sedang mengarahkan lensa modul kamera mini ke arah deretan resistor dan kapasitor di atas konveyor berjalan. Di sampingnya, layar komputer menampilkan aliran gambar langsung. Namun alih-alih menampilkan foto pemandangan, layar tersebut dipenuhi hamparan angka-angka berderet dari 0 hingga 255.

[GAMBAR: assets/bab5_komik_pembuka_sma10.png]

"Dinda, Arya! Coba perhatikan layar ini," seru Bagas sambil memutar kenop fokus lensa kameranya. "Bagi mata kita, kita langsung tahu bahwa benda di depan kamera ini adalah sebuah resistor dengan gelang warna oranye. Namun bagi prosesor komputer, objek ini hanyalah kumpulan baris dan kolom angka biner yang sangat abstrak!"

Dinda mendekat dan menatap layar dengan takjub. "Tepat sekali, Bagas! Bagi mata manusia, melihat adalah proses biologis instan yang diterjemahkan oleh korteks visual di otak kita. Namun bagi komputer, 'melihat' adalah murni operasi matematika matriks dua dimensi atau tiga dimensi. Warna merah, hijau, dan biru dipecah menjadi nilai numerik dari tingkat kecerahan paling gelap (0) hingga paling terang (255)."

Arya menambahkan sambil tersenyum, "Dan yang paling menakjubkan, komputer mengenali bentuk tepi fisik komponenmu melalui sebuah operasi matematika yang disebut **Konvolusi (*Convolution*)**. Sebuah matriks filter kecil berukuran 3x3 digeser di atas piksel gambar untuk mendeteksi perubahan drastis intensitas warna."

"Bahkan lebih mencengangkan lagi," sambung Dinda, "pola suara dan ucapan kita juga dapat diubah menjadi gambar visual dua dimensi yang disebut **Spektrogram** melalui transformasi gelombang suara. Dengan demikian, algoritma Computer Vision yang sama dapat digunakan untuk 'melihat' suara dan mendeteksi ucapan manusia!"

"Luar biasa sekali!" seru Bagas. "Artinya, jika kita menguasai matematika citra digital dan pengenalan pola ini, kita bisa menciptakan mobil otonom yang bisa melihat jalan, sistem medis pendeteksi rontgen penyakit, hingga asisten suara cerdas!"

"Tepat! Mari kita selami cara kerja Computer Vision, filter konvolusi piksel, spektrogram audio, dan menjelajahi peta karier masa depan di dunia kecerdasan artifisial!" ajak Arya.

---

## A. REPRESENTASI CITRA DIGITAL: MATRIKS PIKSEL WARNA MERAH, HIJAU, DAN BIRU (RGB)

Agar komputer atau algoritma kecerdasan artifisial dapat memproses sebuah foto atau video, dunia visual fisik harus diubah (*digitasi*) menjadi format yang dipahami oleh sirkuit mikroprosesor: yaitu angka numerik.

[GAMBAR: assets/bab5_diagram_matriks_konvolusi_piksel.png]

### 1. Piksel dan Skala Derajat Keabuan (Grayscale)

Unsur terkecil penyusun gambar digital disebut **Piksel** (*Picture Element*).
Pada citra skala abu-abu (*grayscale*), setiap piksel direpresentasikan oleh satu nilai angka bulat tunggal berkisar antara **0 hingga 255** (menggunakan format data biner 8-bit, di mana 2^8 = 256 tingkatan):
- Angka **0** merepresentasikan intensitas cahaya nol mutlak (Warna Hitam Pekat).
- Angka **255** merepresentasikan intensitas cahaya maksimum (Warna Putih Bersih).
- Angka di antara 1 hingga 254 merepresentasikan gradasi abu-abu dari gelap hingga terang.

Dengan demikian, citra abu-abu berukuran 640 x 480 piksel sejatinya adalah sebuah **Matriks Dua Dimensi (2D)** yang memiliki 480 baris dan 640 kolom angka.

### 2. Citra Berwarna Model Ruang Warna RGB (Red, Green, Blue)

Mata manusia memiliki sel reseptor yang peka terhadap tiga panjang gelombang utama: Merah (*Red*), Hijau (*Green*), dan Biru (*Blue*). Mengadopsi prinsip optik biologis tersebut, citra berwarna pada sistem komputer disimpan dalam **Matriks Tiga Dimensi (Tensor 3D)** yang memiliki tiga lapisan saluran warna (*Channels*):
- **Saluran R (Red):** Matriks intensitas warna merah (skala 0-255).
- **Saluran G (Green):** Matriks intensitas warna hijau (skala 0-255).
- **Saluran B (Blue):** Matriks intensitas warna biru (skala 0-255).

Setiap titik piksel pada foto berwarna merupakan kombinasi aditif dari ketiga nilai tersebut `(R, G, B)`:
- `(255, 0, 0)` menghasilkan warna Merah Murni.
- `(0, 255, 0)` menghasilkan warna Hijau Murni.
- `(0, 0, 255)` menghasilkan warna Biru Murni.
- `(255, 255, 0)` perpaduan merah dan hijau menghasilkan warna Kuning Terang.
- `(255, 255, 255)` perpaduan ketiga saluran maksimum menghasilkan warna Putih Sempurna.
- `(0, 0, 0)` ketiadaan cahaya pada ketiga saluran menghasilkan warna Hitam Pekat.

---

## B. OPERASI KONVOLUSI DASAR: FILTER KERNEL 3X3 UNTUK DETEKSI TEPI

Bagaimana komputer dapat mengetahui letak batas tepi suatu benda pada foto? Apakah sebuah bentuk merupakan lingkaran bola, rambu lalu lintas, atau wajah manusia? Jawabannya diawali dengan operasi **Konvolusi Citra (*Image Convolution*)**.

### 1. Konsep Kernel / Matriks Filter

**Kernel** (atau filter) adalah sebuah matriks angka kecil—biasanya berukuran ganjil seperti 3x3 atau 5x5—yang dirancang untuk mengekstrak fitur visual tertentu dari citra sumber.

Operasi konvolusi dilakukan dengan cara:
1. Meletakkan matriks kernel 3x3 di atas segmen piksel citra yang bersesuaian.
2. Melakukan perkalian titik (*element-wise multiplication*) antara setiap nilai piksel citra dengan bobot nilai kernel yang menimpanya.
3. Menjumlahkan seluruh hasil perkalian tersebut.
4. Nilai hasil penjumlahan menjadi nilai piksel baru pada citra keluaran di posisi titik pusat kernel.
5. Geser matriks kernel satu langkah ke samping (*stride = 1*), lalu ulangi perhitungan hingga menyapu seluruh permukaan gambar.

### 2. Ragam Jenis Filter Konvolusi Standar

- **Filter Deteksi Tepi Horizontal (Kernel Sobel Horizontal):**
Mendeteksi perubahan mendadak intensitas warna dari atas ke bawah untuk menemukan garis horizon dan tepi mendatar.
Matriks Kernel:
`[[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]]`
- **Filter Deteksi Tepi Vertikal (Kernel Sobel Vertikal):**
Mendeteksi batas kontras tegak dari kiri ke kanan (seperti tiang listrik atau tepi pintu).
Matriks Kernel:
`[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
- **Filter Pengaburan (Blur / Box Blur):**
Menghaluskan citra dan menghilangkan derau (*noise*) dengan cara menghitung rata-rata nilai piksel di sekitarnya.
Matriks Kernel (semua elemen bernilai 1/9):
`[[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]`
- **Filter Penajaman (Sharpening):**
Mempertegas detail tekstur gambar dengan memberi bobot positif sangat tinggi di titik tengah dan bobot negatif di sekelilingnya:
`[[ 0, -1,  0], [-1,  5, -1], [ 0, -1,  0]]`

Operasi konvolusi inilah yang menjadi blok bangunan paling mendasar dari arsitektur jaringan saraf tiruan canggih **Convolutional Neural Networks (CNN)** yang menggerakkan sistem kemudi mobil otonom dan pengenalan wajah dunia modern.

---

## C. REPRESENTASI SUARA DIGITAL: DARI GELOMBANG AKUSTIK KE SPEKTROGRAM FREKUENSI

Suara di alam nyata adalah gelombang tekanan mekanik udara kontinu yang bergetar secara analog. Agar dapat diproses oleh AI, mikrofon menangkap gelombang tersebut dan mengubahnya menjadi sinyal listrik yang kemudian disampel (*sampling*) ke dalam angka-angka diskret.

### 1. Sampling Frekuensi Audio

Berdasarkan Teorema Nyquist-Shannon, agar suara dapat direkonstruksi dengan sempurna tanpa distorsi, frekuensi pengambilan sampel minimal harus dua kali lipat dari frekuensi tertinggi yang dapat didengar manusia (~20 kHz). Oleh karena itu, audio digital standar menggunakan laju sampel **44.100 Hz (44,1 kHz)**, yang berarti komputer merekam 44.100 data amplitudo getaran setiap satu detiknya.

### 2. Transformasi Fourier Cepat (Fast Fourier Transform / FFT)

Gelombang suara ucapan manusia sangatlah rumit karena merupakan gabungan dari puluhan nada harmonik yang bercampur menjadi satu. Melalui rumus matematika algoritma **Transformasi Fourier Cepat (FFT)**, gelombang suara yang rumit dalam ranah waktu (*time domain*) dapat diurai menjadi komponen-komponen frekuensi penyusunnya (*frequency domain*).

### 3. Keajaiban Spektrogram: Mengubah Suara Menjadi Gambar Visual

Dengan membagi rekaman audio menjadi potongan-potongan jendela waktu kecil yang berurutan lalu menerapkan transformasi FFT pada setiap jendela, kita memperoleh representasi visual dua dimensi yang disebut **Spektrogram**:
- **Sumbu Horizontal (X):** Menunjukkan aliran waktu (dalam detik).
- **Sumbu Vertikal (Y):** Menunjukkan spektrum frekuensi suara (dari nada rendah / Bass di bawah hingga nada tinggi / Treble di atas).
- **Intensitas Warna (Kecerahan):** Menunjukkan besarnya amplitudo energi desibel (dB) pada frekuensi tersebut. Warna yang terang menyala menandakan suara vokal atau instrumen yang sedang berbunyi lantang.

**Mengapa ini menjadi revolusi dalam AI Audio?**
Karena spektrogram adalah gambar visual dua dimensi, para insinyur kecerdasan artifisial dapat memanfaatkan model Computer Vision (seperti CNN) untuk memproses suara ucapan manusia! Model AI "melihat" bentuk pola spektrum kata "Buka Pintu" persis seperti melihat foto sebuah rambu lalu lintas, memungkinkan sistem pengenalan suara (*Automatic Speech Recognition*) bekerja dengan akurasi yang luar biasa tinggi.

---

## D. PETA PELUANG KARIER DAN LANSKAP KEAHLIAN DI ERA KECERDASAN ARTIFISIAL

Revolusi kecerdasan artifisial bukan hanya mengubah cara kerja perangkat lunak, melainkan juga melahirkan lanskap profesi baru dengan permintaan pasar kerja global yang sangat tinggi.

[GAMBAR: assets/bab5_peta_ekosistem_karier_ai_masa_depan.png]

Berikut adalah profesi masa depan paling bergengsi di ekosistem kecerdasan artifisial yang dapat menjadi cita-cita karier kalian:

1. **Machine Learning / Deep Learning Engineer:**
Bertugas merancang, melatih, dan mengoptimalkan arsitektur model matematika cerdas (seperti CNN untuk visi komputer atau Transformer untuk pemrosesan bahasa alami). Membutuhkan fondasi kuat dalam aljabar linear, kalkulus, dan pemrograman Python.
2. **Computer Vision Specialist:**
Insinyur yang fokus mengembangkan algoritma pengolahan citra dan video cerdas, seperti sistem deteksi cacat manufaktur pada pabrik industri, navigasi robot otonom, drone pemantau pertanian cerdas, dan analisis citra medis radiologi.
3. **Data Scientist & Data Analyst:**
Pakar yang bertugas mengekstrak wawasan strategis dari tumpukan mahadata (*Big Data*), mengidentifikasi tren tersembunyi, serta membersihkan dan menyiapkan data berkualitas tinggi untuk melatih model AI.
4. **Prompt Engineer & AI Solution Architect:**
Profesi baru yang mahir menyusun instruksi terstruktur untuk model fondasi AI generatif, mengintegrasikan antarmuka pemrograman aplikasi (API AI) ke dalam sistem perbankan, kesehatan, atau niaga digital.
5. **AI Ethics & Compliance Officer:**
Ahli hukum dan sosial-teknologi yang bertugas mengaudit sistem AI untuk memastikan model tidak mengandung bias diskriminasi SARA, menjaga kerahasiaan privasi data pengguna, dan mematuhi regulasi perlindungan data pribadi nasional maupun global.
6. **MLOps (Machine Learning Operations) Engineer:**
Jembatan antara ilmu data dan rekayasa infrastruktur server, yang mengelola penyebaran (*deployment*), pemantauan, dan pemeliharaan model AI di lingkungan komputasi awan (*cloud*) secara stabil 24/7.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 5.1

### Eksperimen Deteksi Tepi Citra Menggunakan Operasi Konvolusi Matriks Sederhana

**Tujuan Pembelajaran:**
Peserta didik mampu memahami representasi citra sebagai matriks angka numerik dua dimensi, serta mengimplementasikan operasi matematika konvolusi kernel 3x3 secara mandiri menggunakan bahasa Python murni untuk mendeteksi tepi garis gambar.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terinstal.
2. Kode editor teks.

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `praktikum_konvolusi_citra.py`.
2. Ketikkan kode program simulasi konvolusi matriks berikut:

```python
# Simulasi Citra Sederhana Berukuran 6x6 Piksel
# Angka mewakili nilai intensitas cahaya (0 = Gelap, 255 = Terang)
# Bayangkan ini adalah gambar sebuah objek putih di atas latar hitam
citra_masukan = [
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255],
    [0,   0,   0, 255, 255, 255]
]

# Matriks Kernel Sobel Vertikal untuk Deteksi Tepi Tegak
kernel_vertikal = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

def terapkan_konvolusi(citra, kernel):
    tinggi = len(citra)
    lebar = len(citra[0])
    k_size = len(kernel)
    offset = k_size // 2

    # Menyiapkan matriks keluaran kosong (berukuran 4x4 untuk citra 6x6 tanpa padding)
    hasil = []
    
    for i in range(offset, tinggi - offset):
        baris_baru = []
        for j in range(offset, lebar - offset):
            total_nilai = 0
            # Operasi perkalian titik pada jendela 3x3
            for ki in range(k_size):
                for kj in range(k_size):
                    piksel = citra[i - offset + ki][j - offset + kj]
                    bobot = kernel[ki][kj]
                    total_nilai += piksel * bobot
            
            # Membatasi nilai keluaran antara 0 hingga 255 (Clamping)
            nilai_akhir = max(0, min(255, abs(total_nilai)))
            baris_baru.append(nilai_akhir)
        hasil.append(baris_baru)
    
    return hasil

# Jalankan konvolusi deteksi tepi
citra_tepi = terapkan_konvolusi(citra_masukan, kernel_vertikal)

print("===== HASIL MATRIKS CITRA SETELAH OPERASI KONVOLUSI SOBEL =====")
for baris in citra_tepi:
    for nilai in baris:
        print(f"{nilai:5}", end=" ")
    print()
```

**Pertanyaan Analisis Laboratorium:**
1. Amatilah nilai matriks hasil konvolusi di layar terminal. Pada kolom manakah nilai angka melonjak tinggi (mendekati 255 atau lebih), dan pada kolom mana nilainya mendekati 0?
2. Mengapa nilai pada kolom yang terjadi lonjakan drastis dari 0 ke 255 menghasilkan angka yang sangat besar pada matriks keluaran?
3. Apa perbedaan konseptual antara cara kerja filter pengaburan (*blur*) yang menghitung rata-rata nilai sekitar dengan filter pendeteksi tepi yang menghitung selisih gradien kontras?

---

## F. RANGKUMAN MATERI BAB V

1. **Representasi Citra Digital:** Citra hitam-putih tersusun atas matriks dua dimensi dengan nilai piksel 0 (hitam) hingga 255 (putih). Citra berwarna tersusun atas tensor tiga dimensi dengan tiga saluran warna utama: Merah (*Red*), Hijau (*Green*), dan Biru (*Blue*).
2. **Operasi Konvolusi:** Proses matematika perkalian titik antara segmen piksel citra dengan matriks filter kecil (kernel 3x3) yang digeser menyapu seluruh citra. Berguna untuk mendeteksi tepi (*edge detection*), menajamkan gambar, maupun menyaring derau visual.
3. **Representasi Audio ke Spektrogram:** Gelombang suara analog disampel menjadi data diskret (standar 44,1 kHz). Melalui Transformasi Fourier Cepat (FFT), sinyal suara diurai menjadi spektrogram dua dimensi (waktu vs frekuensi vs amplitudo) yang memungkinkan model penglihatan komputer menganalisis ucapan manusia.
4. **Lanskap Ekosistem Karier AI:** Revolusi kecerdasan artifisial membuka peluang karier masif bagi generasi muda Indonesia, meliputi insinyur pembelajaran mesin, spesialis visi komputer, saintis data, arsitek prompt, petugas kepatuhan etika AI, hingga insinyur operasional MLOps.

---

## G. UJI KOMPETENSI BAB V

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Rentang nilai intensitas derajat keabuan (*grayscale*) 8-bit yang merepresentasikan tingkat kecerahan sebuah piksel citra digital dari gelap pekat hingga putih sempurna adalah...
   A. -128 hingga 127
   B. 0 hingga 255
   C. 1 hingga 100
   D. 0 hingga 1.024

2. Sebuah piksel pada citra berwarna memiliki kode koordinat warna RGB: `(0, 255, 0)`. Warna yang akan terpancar pada layar monitor untuk piksel tersebut adalah...
   A. Merah Murni
   B. Biru Terang
   C. Hijau Murni
   D. Putih Bersih

3. Operasi matematika mendasar dalam pemrosesan citra digital di mana sebuah matriks filter kecil digeser di atas piksel citra untuk menghitung perkalian titik dan menghasilkan fitur visual baru dinamakan...
   A. Faktorisasi
   B. Konvolusi
   C. Diferensiasi
   D. Interpolasi

4. Manakah di antara matriks kernel 3x3 berikut yang biasa digunakan untuk operasi penghalusan citra dan peredam derau (*Box Blur*)?
   A. `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`
   B. `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
   C. Semua elemen bernilai sama yaitu 1/9
   D. `[[1, 0, 0], [0, 1, 0], [0, 0, 1]]`

5. Berdasarkan Teorema Nyquist-Shannon, berapakah frekuensi pengambilan sampel (*sampling rate*) minimum yang dibutuhkan untuk merekam suara manusia agar seluruh spektrum frekuensi hingga 20.000 Hz dapat ditangkap secara utuh tanpa distorsi (*aliasing*)?
   A. 10.000 Hz
   B. 20.000 Hz
   C. 40.000 Hz
   D. 5.000 Hz

6. Representasi visual grafis dua dimensi yang memetakan spektrum frekuensi suara pada sumbu Y terhadap perubahan waktu pada sumbu X dengan intensitas warna yang menunjukkan besaran energi suara disebut...
   A. Histogram Warna
   B. Spektrogram
   C. Osiloskop
   D. Diagram Kartesius

7. Mengapa model kecerdasan artifisial Computer Vision (seperti CNN) dapat dimanfaatkan untuk mengenali perintah suara manusia (*speech recognition*)?
   A. Karena sinyal suara selalu memiliki warna merah dan biru alami
   B. Karena gelombang suara dapat diubah terlebih dahulu menjadi citra visual berupa spektrogram
   C. Karena speaker komputer memiliki kamera tersembunyi
   D. Karena suara tidak membutuhkan pemrosesan numerik

8. Profesi di era kecerdasan artifisial yang bertugas secara spesifik mengaudit model AI agar tidak menghasilkan keputusan yang mendiskriminasi kelompok masyarakat tertentu serta menjamin kepatuhan privasi data adalah...
   A. Full-stack Web Developer
   B. AI Ethics & Compliance Officer
   C. Hardware Network Technician
   D. Game Asset 3D Animator

9. Apa yang terjadi pada matriks hasil konvolusi ketika kernel pendeteksi tepi Sobel melintasi area citra yang memiliki warna seragam sempurna (misalnya seluruh pikselnya bernilai 120)?
   A. Seluruh hasil perhitungannya bernilai 0 (tidak ada tepi yang terdeteksi)
   B. Hasilnya meledak menjadi angka tak hingga
   C. Layar komputer seketika mati
   D. Seluruh piksel berubah menjadi warna merah terang

10. Praktisi teknologi yang bertanggung jawab menjembatani model kecerdasan artifisial dari lingkungan riset laboratorium menuju sistem produksi peladen awan (*cloud server*) yang stabil dan terpantau 24/7 dikenal sebagai...
    A. MLOps Engineer
    B. Database Operator
    C. Prompt Reader
    D. Desktop Technician

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan bagaimana sebuah gambar foto berwarna disimpan di dalam memori komputer dalam bentuk tensor tiga dimensi! Sebutkan peran masing-masing saluran warnanya!
2. Uraikan secara sistematis tahapan operasi konvolusi ketika sebuah matriks kernel berukuran 3x3 menyapu sebuah matriks piksel citra digital!
3. Diberikan jendela citra 3x3:
   `[[10, 10, 200], [10, 10, 200], [10, 10, 200]]`
   dan matriks kernel Sobel vertikal:
   `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`.
   Hitunglah nilai perkalian konvolusi pada titik pusat tersebut dan jelaskan maknanya!
4. Jelaskan bagaimana gelombang suara analog dari percakapan manusia dapat ditransformasikan menjadi citra dua dimensi (Spektrogram) menggunakan algoritma Transformasi Fourier Cepat (FFT)!
5. Dari berbagai prospek karier di era kecerdasan artifisial yang telah kalian pelajari, pilihlah salah satu profesi yang paling menarik minat kalian. Uraikan peran strategis profesi tersebut serta keahlian teknis apa saja yang perlu kalian persiapkan sejak duduk di bangku SMA/SMK!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB V

**Kunci Pilihan Ganda:**
1. **B** (Skala grayscale 8-bit berkisar dari 0 hingga 255).
2. **C** (RGB 0, 255, 0 merepresentasikan warna Hijau Murni).
3. **B** (Operasi pergeseran filter dan perkalian titik tersebut dinamakan konvolusi).
4. **C** (Filter Box Blur memiliki seluruh bobot yang seragam senilai 1/9 untuk menghitung nilai rata-rata lokal).
5. **C** (Teorema Nyquist mensyaratkan frekuensi sampling minimal 2x frekuensi tertinggi, yaitu 2 x 20.000 = 40.000 Hz, sehingga standar audio komersial menggunakan 44.100 Hz).
6. **B** (Spektrogram adalah visualisasi 2D frekuensi terhadap waktu).
7. **B** (Spektrogram mengubah audio menjadi gambar visual yang dapat diolah oleh algoritma visi komputer).
8. **B** (AI Ethics Officer bertugas mengawal aspek keadilan, non-bias, dan etika hukum sistem AI).
9. **A** (Pada area seragam tanpa perbedaan kontras, selisih perhitungan kernel bernilai nol murni).
10. **A** (MLOps Engineer bertanggung jawab atas deployment dan otomatisasi siklus hidup model AI di produksi).

**Pembahasan Soal Uraian:**
1. *Penyimpanan Citra Berwarna dalam Tensor 3D:*
   Citra berwarna disimpan dalam bentuk susunan matriks tiga dimensi dengan dimensi `(Tinggi, Lebar, Saluran)`. Terdapat tiga saluran (channels) terpisah, yaitu Saluran R (Red), Saluran G (Green), dan Saluran B (Blue). Setiap sel pada masing-masing saluran berisi nilai skalar bilangan bulat 0-255 yang menyatakan intensitas kecerahan warna primer tersebut. Perpaduan intensitas ketiga saluran pada koordinat piksel yang sama merekonstruksi spektrum lebih dari 16,7 juta variasi warna yang ditangkap mata manusia.
2. *Tahapan Operasi Konvolusi:*
   - Letakkan kernel di atas jendela piksel citra yang bersesuaian.
   - Lakukan perkalian titik (element-wise multiplication) antara setiap nilai sel kernel dengan nilai piksel citra di bawahnya.
   - Jumlahkan seluruh hasil perkalian tersebut untuk memperoleh satu angka skalar tunggal.
   - Terapkan fungsi pemotongan (clamping) jika nilai melebihi rentang 0-255.
   - Simpan nilai hasil tersebut pada matriks citra keluaran baru di koordinat titik pusat.
   - Geser kernel ke posisi piksel berikutnya sesuai nilai stride yang ditentukan.
3. *Perhitungan Konvolusi Sobel Vertikal:*
   - Baris 1: (10 * -1) + (10 * 0) + (200 * 1) = -10 + 0 + 200 = 190.
   - Baris 2: (10 * -2) + (10 * 0) + (200 * 2) = -20 + 0 + 400 = 380.
   - Baris 3: (10 * -1) + (10 * 0) + (200 * 1) = -10 + 0 + 200 = 190.
   - Total Penjumlahan: 190 + 380 + 190 = **760**.
   - Makna: Nilai positif yang sangat tinggi (760) membuktikan adanya lonjakan kontras yang sangat tajam dari gelap (10) ke terang (200) secara vertikal. Ini mengindikasikan bahwa algoritma berhasil mendeteksi adanya garis tepi tegak lurus pada batas kolom kedua dan ketiga.
4. *Transformasi Suara Menjadi Spektrogram:*
   Sinyal audio analog disampel menjadi deretan angka amplitudo terhadap waktu. Sinyal yang panjang dipotong menjadi bingkai-bingkai waktu pendek (misalnya durasi 25 milidetik). Pada setiap bingkai, algoritma FFT (Fast Fourier Transform) dijalankan untuk menguraikan getaran gabungan menjadi spektrum frekuensi individual beserta kekuatannya. Spektrum-spektrum frekuensi ini kemudian disusun berjajar dari kiri ke kanan sesuai urutan waktu, menghasilkan citra dua dimensi (Spektrogram) di mana tinggi menyatakan nada dan warna menyatakan volume suara.
5. *Eksplorasi Karier Masa Depan (Contoh Analisis):*
   Jika memilih menjadi seorang *Computer Vision Specialist*, peran strategisnya adalah merancang mata cerdas buatan bagi peradaban industri—seperti sistem inspeksi kualitas pangan otomatis atau navigasi robotik ramah disabilitas. Keahlian teknis yang harus dipersiapkan sejak bangku SMA/SMK meliputi: penguasaan matematika matriks dan aljabar linear, keterampilan koding Python tingkat lanjut, pemahaman pemrosesan citra digital, serta pembiasaan diri membedah arsitektur jaringan saraf tiruan melalui berbagai proyek praktikum nyata.
"""
