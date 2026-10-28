"""
Modul Naskah Bab II Kelas XII SMA/SMK (Fase F Akhir)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB2_SMA12 = """# BAB II: MAHADATA (BIG DATA) DAN REKAYASA ANALISIS SKALA BESAR

## APERSEPSI: MENELUSURI JEJAK DIGITAL JUTAAN TRANSAKSI

Di laboratorium komputasi sekolah, layar monitor Arya menampilkan jutaan baris data lalu lintas pengguna yang berkedip cepat tanpa henti. Data tersebut merekam aliran transaksi logistik dari jaringan koperasi perikanan lokal di pesisir Sulawesi Utara. Dinda dan Bagas duduk di samping Arya, mengamati angka-angka yang membanjiri memori RAM komputer.

[GAMBAR: assets/bab2_komik_pembuka_sma12.png]

"Arya, perangkat lunak lembar sebar (spreadsheet) kita macet total saat mencoba membuka berkas berkuran 8 Gigabyte ini!" keluh Bagas sambil memijat keningnya. "Setiap kali kita mengeklik tombol filter, komputer langsung mengalami *freeze* dan sistem operasi menampilkan peringatan *Out of Memory*!"

Arya tersenyum tenang seraya membuka terminal Linux. "Itu wajar, Bagas. Lembar sebar konvensional dirancang untuk kumpulan data statis berskala kecil hingga puluhan ribu baris. Ketika data yang kita hadapi telah mencapai skala jutaan baris dengan kecepatan transmisi milidetik dan ragam format yang tak terstruktur, kita telah memasuki teritori **Mahadata (*Big Data*)**!"

Dinda mencermati visualisasi sebaran data dengan saksama. "Perhatikan polanya, teman-teman. Di antara jutaan baris data ini, tersimpan riwayat pembelian bahan bakar kapal, koordinat tangkapan nelayan, fluktuasi harga lelang ikan harian, hingga ulasan teks para pedagang pasar. Kita tidak bisa menganalisisnya secara manual. Kita memerlukan arsitektur basis data modern dan algoritma pembelajaran mesin tak terawasi (*Unsupervised Machine Learning*) seperti **Klastering K-Means** untuk mengelompokkan pola nelayan dan rute logistik secara otomatis!"

"Tepat sekali, Dinda!" imbuh Arya. "Namun ingat, data transaksi dan pergerakan nelayan ini memuat informasi privasi warga negara. Dalam mengolah mahadata, kita memegang tanggung jawab moral dan hukum sesuai amanat **Undang-Undang Pelindungan Data Pribadi (UU PDP No. 27/2022)** untuk menjamin kedaulatan data nasional."

"Menakjubkan!" seru Bagas. "Mari kita pelajari karakteristik 5V Big Data, arsitektur basis data skala raksasa, algoritma K-Means, hingga rekayasa anonimisasi data demi melindungi privasi masyarakat!"

---

## A. KARAKTERISTIK 5V MAHADATA (BIG DATA)

Setiap menit di era modern, umat manusia memproduksi miliaran interaksi digital: pesan percakapan instan, video streaming beresolusi 4K, transaksi uang elektronik, sensor cuaca satelit, hingga sinyal telemetri kendaraan otonom. Lonjakan eksponensial ini melahirkan era **Mahadata (*Big Data*)**.

[GAMBAR: assets/bab2_infografis_karakteristik_5v_big_data.png]

Mahadata didefinisikan secara komprehensif melalui kerangka kerja **5V**:

### 1. Volume (Skala Ukuran Data Raksasa)
Volume merujuk pada kuantitas fisik data yang dihasilkan dan disimpan. Jika pada dekade lalu sistem basis data beroperasi dalam skala Megabyte (MB) hingga Gigabyte (GB), ekosistem Big Data beroperasi pada skala **Terabyte (TB)**, **Petabyte (PB)**, hingga **Zettabyte (ZB)**. Satu Petabyte setara dengan 1.000 Terabyte atau kira-kira setara dengan 500 miliar lembar teks ketikan standar.

### 2. Velocity (Kecepatan Aliran Data Real-Time)
Velocity menyoroti laju kecepatan data yang diproduksi, ditransmisikan, dan harus diproses dalam waktu nyata (*real-time*). Sebagai contoh, sistem deteksi penipuan perbankan harus mampu memvalidasi jutaan otentikasi transaksi kartu kredit global dalam waktu kurang dari 50 milidetik sebelum otorisasi pembayaran disetujui.

### 3. Variety (Keberagaman Format dan Struktur Data)
Data modern tidak lagi tersusun rapi dalam bentuk tabel dua dimensi (baris dan kolom). Big Data mencakup:
- **Data Terstruktur (Structured):** Tersimpan rapi dalam tabel basis data relasional berindeks (seperti SQL).
- **Data Semi-Terstruktur (Semi-Structured):** Memiliki skema fleksibel seperti dokumen JSON, XML, atau berkas konfigurasi YAML.
- **Data Tidak Terstruktur (Unstructured):** Format bebas yang mendominasi lebih dari 80% data dunia, mencakup rekaman audio, video, citra satelit, dokumen PDF, dan unggahan status media sosial.

### 4. Veracity (Akurasi, Kualitas, dan Keandalan Data)
Veracity mencerminkan tingkat kepercayaan (*trustworthiness*) dan kebersihan data. Di tengah samudra data, terdapat gangguan (*noise*), ketidakkonsistenan, data duplikat, informasi bias, hingga manipulasi data (*hoaks*). Rekayasa mahadata menuntut proses kurasi, pembersihan (*data cleansing*), dan validasi integritas data yang ketat sebelum model analitik dijalankan.

### 5. Value (Nilai Manfaat Strategis dan Dampak Sosial)
Value adalah muara terpenting dari seluruh investasi teknologi Big Data. Data berskala Petabyte tidak memiliki arti apa pun jika tidak dapat diekstraksi menjadi wawasan bernilai (*actionable insights*) yang memandu pengambilan keputusan bisnis, mitigasi bencana alam, peningkatan layanan kesehatan publik, maupun kebijakan ketahanan pangan nasional.

---

## B. ARSITEKTUR PENYIMPANAN: SQL VS NOSQL VS DATA LAKE

Untuk menampung dan memproses data dengan karakteristik 5V, industri rekayasa perangkat lunak mengembangkan arsitektur penyimpanan bertingkat:

### 1. Basis Data Relasional (SQL - Relational Database Management System)
Sistem seperti PostgreSQL dan MySQL mengorganisasikan data ke dalam tabel dengan skema (*schema*) yang kaku dan relasi antar-tabel menggunakan kunci primer (*Primary Key*) dan kunci asing (*Foreign Key*).
- **Kelebihan:** Menjamin kepatuhan prinsip **ACID (*Atomicity, Consistency, Isolation, Durability*)**, menjadikannya standar mutlak untuk transaksi keuangan dan pencatatan saldo perbankan yang tidak boleh mentoleransi inkonsistensi data.
- **Keterbatasan:** Sulit diskalakan secara horizontal (*Horizontal Scaling*) ke puluhan peladen terdistribusi saat volume data menembus miliaran entitas.

### 2. Basis Data Dokumen NoSQL (Not Only SQL)
Sistem seperti **MongoDB** menyimpan data dalam format dokumen hierarkis fleksibel mirip JSON (BSON). Setiap dokumen dapat memiliki bidang data (*field*) yang berbeda tanpa perlu migrasi skema tabel yang rumit.
- **Kelebihan:** Sangat cepat untuk operasi baca/tulis berskala masif, mudah diskalakan secara terdistribusi (*sharding*), dan ideal untuk aplikasi dinamis modern, katalog produk e-commerce, serta data telemetri IoT.
- **Kelemahan:** Mengorbankan tingkat konsistensi ketat ACID demi mengejar ketersediaan tinggi (*High Availability*) berdasarkan **Teorema CAP (*Consistency, Availability, Partition Tolerance*)**.

### 3. Data Lake (Danau Data)
Data Lake (seperti Apache Hadoop HDFS atau Amazon S3) adalah repositori penyimpanan terpusat berskala tak terbatas yang menampung data mentah (*raw data*) dalam format aslinya tanpa perlu transformasi skema di awal (*Schema-on-Read*). Data teks, log peladen, rekaman audio, hingga citra satelit dapat dicurahkan ke dalam Data Lake, lalu diolah menggunakan mesin komputasi terdistribusi seperti Apache Spark saat analisis mendalam dibutuhkan.

---

## C. PENAMBANGAN DATA TAK TERAWASI: KLASTERING K-MEANS

Ketika berhadapan dengan jutaan entitas data yang belum memiliki label kelas sama sekali, algoritma pembelajaran mesin terawasi (*Supervised Learning*) tidak dapat digunakan. Di sinilah **Pembelajaran Mesin Tak Terawasi (*Unsupervised Machine Learning*)** memainkan peranan kunci melalui teknik **Klastering (Pengelompokan)**.

Algoritma klastering paling populer dan efisien di industri adalah **K-Means**. Algoritma ini mempartisi sejumlah *n* data ke dalam *k* kelompok (klaster), di mana setiap data menjadi anggota klaster dengan titik pusat (*centroid*) terdekat.

### 1. Tahapan Eksekusi Matematis Algoritma K-Means

1. **Inisialisasi Nilai k:** Menentukan jumlah klaster *k* yang diinginkan.
2. **Penempatan Centroid Awal:** Memilih secara acak *k* titik dalam ruang data sebagai titik pusat klaster sementara.
3. **Penetapan Anggota Klaster (Assignment Step):** Menghitung jarak geometris antara setiap titik data *x* ke setiap centroid *c* menggunakan rumus **Jarak Euclidean (*Euclidean Distance*)**:

```text
Jarak Euclidean = sqrt( (x1 - c1)^2 + (x2 - c2)^2 + ... + (xn - cn)^2 )
```

Setiap data dimasukkan ke dalam klaster yang memiliki jarak terpendek ke centroid-nya.

4. **Pembaruan Posisi Centroid (Update Step):** Menghitung ulang koordinat posisi setiap centroid berdasarkan rata-rata (*mean*) seluruh anggota yang berada dalam klaster tersebut:

```text
Centroid Baru = (Jumlah seluruh koordinat anggota) / (Banyaknya anggota klaster)
```

5. **Pemeriksaan Konvergensi (Convergence):** Mengulangi langkah 3 dan 4 hingga posisi centroid tidak lagi berpindah secara signifikan, atau batas iterasi maksimum tercapai.

### 2. Menentukan Nilai k Optimal: Metode Siku (Elbow Method)
Bagaimana kita mengetahui berapa jumlah klaster *k* yang paling tepat untuk sebuah dataset? Pendekatan standar yang digunakan adalah **Metode Siku (*Elbow Method*)** dengan menghitung metrik **WCSS (*Within-Cluster Sum of Squares*)** atau inersia:

```text
WCSS = Jumlah kuadrat jarak antara setiap titik data ke centroid klasternya
```

Ketika kita memplot grafik nilai WCSS terhadap penambahan nilai *k* (dari k=1, 2, 3, hingga 10), nilai WCSS akan turun drastis pada awalnya, lalu laju penurunannya melambat secara tajam. Titik belok tempat terjadinya perubahan sudut penurunan menyerupai bentuk tekukan siku tangan manusia (*elbow*). Titik siku tersebut merepresentasikan nilai *k* paling optimal yang menyeimbangkan antara homogenitas kelompok dan kesederhanaan model.

---

## D. ETIKA MAHADATA, ANONIMISASI, DAN KEDAULATAN DATA NASIONAL

Mahadata menyimpan potensi kemanfaatan peradaban yang spektakuler, namun sekaligus membawa ancaman pelanggaran hak asasi manusia jika disalahgunakan. Privasi warga negara, integritas identitas digital, dan kedaulatan informasi nasional harus dijaga dengan kokoh.

### 1. Ancaman Pengawasan Massal (Mass Surveillance)
Kompilasi mahadata lokasi GPS, riwayat pencarian web, rekaman kamera CCTV publik, dan aktivitas transaksi belanja dapat digunakan oleh oknum tidak bertanggung jawab untuk melakukan pemrofilan psikologis (*psychological profiling*) dan pengawasan massal tanpa izin warga (*unauthorized mass surveillance*). Ini bertentangan dengan prinsip kebebasan individu dan demokrasi modern.

### 2. Teknik Anonimisasi dan De-Identifikasi Data
Sebelum dataset dipublikasikan atau dianalisis oleh pihak ketiga, pengembang wajib menerapkan teknik pengaburan identitas:
- **Masking:** Mengganti sebagian digit informasi sensitif dengan simbol bintang (contoh: NIK 717101******0001).
- **Pseudonimisasi:** Menggantikan identitas asli dengan token atau kode unik acak berbasis algoritma hash satu arah (SHA-256).
- **Generalisasi (K-Anonymity):** Mengaburkan nilai presisi menjadi rentang kategori umum (contoh: usia 17 tahun diubah menjadi rentang '15-20 tahun', alamat jalan diubah menjadi 'Kota Manado').
- **Penambahan Derau Diferensial (Differential Privacy):** Menyisipkan derau statistik acak terkontrol ke dalam agregasi data agar identitas spesifik individu tidak dapat direkonstruksi (*re-identification attack*).

### 3. Regulasi UU Pelindungan Data Pribadi (UU PDP No. 27/2022)
Negara Kesatuan Republik Indonesia telah mengesahkan payung hukum tertinggi pelindungan data yaitu **Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)**. Prinsip fundamental dalam UU PDP meliputi:
1. **Persetujuan yang Sah (*Consent*):** Pemrosesan data pribadi wajib memperoleh persetujuan eksplisit dan tertulis dari pemilik data (*Data Subject*).
2. **Keterbatasan Tujuan (*Purpose Limitation*):** Data hanya boleh digunakan untuk tujuan spesifik yang telah diberitahukan sebelumnya.
3. **Hak untuk Dihapus (*Right to Erasure / Right to be Forgotten*):** Pemilik data berhak meminta penghapusan seluruh data pribadinya dari sistem penyelenggara elektronik jika tidak lagi relevan.
4. **Kedaulatan Data (*Data Sovereignty*):** Kewajiban menyimpan data strategis kependudukan, keuangan negara, dan infrastruktur kritis di pusat data (*Data Center*) yang berlokasi fisik di dalam yurisdiksi wilayah Negara Kesatuan Republik Indonesia.

---

## E. LKPD 2.1: LABORATORIUM SEGMENTASI DATA PELANGGAN DENGAN PYTHON K-MEANS

Pada praktikum tingkat akhir ini, kalian akan menganalisis dataset transaksi e-commerce untuk mengelompokkan pelanggan berdasarkan pendapatan tahunan dan skor pengeluaran belanja menggunakan pustaka ilmiah Scikit-Learn.

### 1. Alat dan Bahan
- Perangkat komputer/laptop dengan Python 3 terpasang.
- Pustaka data: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.
- Lingkungan kerja: Jupyter Notebook atau Google Colaboratory.

### 2. Kode Program Segmentasi Mahadata Pelanggan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Menyiapkan dataset sintetis transaksi pelanggan (100 pelanggan)
np.random.seed(42)
pendapatan = np.concatenate([
    np.random.normal(25, 5, 30),   # Kelompok pendapatan rendah
    np.random.normal(60, 10, 40),  # Kelompok pendapatan menengah
    np.random.normal(100, 15, 30)  # Kelompok pendapatan tinggi
])
skor_belanja = np.concatenate([
    np.random.normal(80, 8, 30),   # Pengeluaran tinggi
    np.random.normal(50, 10, 40),  # Pengeluaran sedang
    np.random.normal(20, 8, 30)    # Pengeluaran hemat
])

df_pelanggan = pd.DataFrame({
    'Pendapatan_Juta': pendapatan,
    'Skor_Belanja_1_100': skor_belanja
})

# 2. Penskalaan fitur data menggunakan StandardScaler
scaler = StandardScaler()
fitur_scaled = scaler.fit_transform(df_pelanggan)

# 3. Menerapkan Metode Siku (Elbow Method) untuk mencari k optimal
wcss = []
k_range = range(1, 8)
for k in k_range:
    model_kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    model_kmeans.fit(fitur_scaled)
    wcss.append(model_kmeans.inertia_)

print("Nilai WCSS untuk k=1 s.d. 7:")
for k, nilai in zip(k_range, wcss):
    print(f"k = {k}: WCSS = {nilai:.2f}")

# 4. Pelatihan model final dengan k=3 klaster optimal
model_final = KMeans(n_clusters=3, init='k-means++', random_state=42)
df_pelanggan['Klaster'] = model_final.fit_predict(fitur_scaled)

# 5. Menampilkan 5 sampel data hasil segmentasi
print("\nHasil Segmentasi Pelanggan (5 Teratas):")
print(df_pelanggan.head())
```

### 3. Tugas Analisis dan Eksplorasi Siswa
1. Berdasarkan nilai WCSS yang dicetak program, amatilah pada nilai *k* berapakah penurunan inersia mulai melandai secara signifikan!
2. Deskripsikan karakteristik perilaku konsumen untuk masing-masing dari ketiga klaster yang terbentuk (misal: Klaster Mahasiswa Hedon, Klaster Keluarga Bijak, Klaster Konglomerat Hemat)!
3. Rancanglah satu strategi rekomendasi promosi produk yang dipersonalisasi untuk masing-masing klaster tersebut!

---

## F. RANGKUMAN MATERI BAB II

1. **Mahadata (*Big Data*)** adalah himpunan data berskala sangat masif yang tidak dapat ditampung atau dianalisis menggunakan perangkat lunak konvensional, dicirikan oleh kerangka kerja **5V**: *Volume* (ukuran petabyte), *Velocity* (kecepatan aliran real-time), *Variety* (keberagaman terstruktur hingga non-terstruktur), *Veracity* (akurasi dan kualitas data), serta *Value* (nilai manfaat sosial dan bisnis).
2. **Arsitektur Penyimpanan Data** berevolusi dari basis data relasional **SQL** yang mengutamakan integritas transaksi ketat (**ACID**), menuju pangkalan data dokumen **NoSQL** yang fleksibel dan berkinerja tinggi pada sistem terdistribusi, hingga **Data Lake** yang menampung data mentah multi-format tanpa transformasi awal.
3. **Klastering K-Means** merupakan algoritma pembelajaran mesin tak terawasi (*Unsupervised Learning*) yang mempartisi data ke dalam *k* kelompok berdasarkan kedekatan jarak Euclidean terhadap titik pusat kelompok (*Centroid*).
4. Penentuan jumlah kelompok paling ideal dianalisis menggunakan **Metode Siku (*Elbow Method*)**, yaitu mencari titik belok penurunan grafik nilai **WCSS (*Within-Cluster Sum of Squares*)**.
5. Pengolahan mahadata wajib menjamin hak privasi masyarakat melalui teknik de-identifikasi (masking, pseudonimisasi, differensial privacy) serta tunduk pada amanat **UU Pelindungan Data Pribadi (UU PDP No. 27/2022)** yang mewajibkan persetujuan pemilik data dan kedaulatan data nasional.

---

## G. UJI KOMPETENSI BAB II

### Bagian 1: Pilihan Ganda (10 Soal Berbobot HOTS)

1. Sebuah perusahaan logistik maritim menerima aliran data koordinat GPS dari 12.000 kapal nelayan setiap 200 milidetik secara kontinu. Karakteristik Big Data yang paling dominan menjadi tantangan teknis dalam menerima dan memproses data seketika ini adalah...
A. Volume  
B. Velocity  
C. Variety  
D. Veracity  
E. Value  

2. Perhatikan potongan dokumen berikut:
```text
{
  "id_transaksi": "TRX-99812",
  "waktu": "2025-05-12T08:30:00Z",
  "pelanggan": {"nama_samaran": "User_88", "kota": "Manado"},
  "item_belanja": [
    {"nama": "Sensor DHT22", "qty": 3, "harga": 45000},
    {"nama": "Kabel Jumper", "qty": 1, "tipe": "Female-to-Female"}
  ]
}
```
Format penyimpanan data semi-terstruktur di atas berbasis dokumen hierarkis yang paling optimal dikelola oleh jenis basis data...
A. RDBMS PostgreSQL  
B. Basis Data Relasional MySQL  
C. Basis Data Dokumen NoSQL MongoDB  
D. Microsoft Access  
E. SQLite  

3. Mengapa sistem perbankan konvensional tetap mempertahankan arsitektur basis data relasional (SQL) untuk pencatatan transaksi penarikan uang, meskipun basis data NoSQL menawarkan kecepatan tulis yang jauh lebih tinggi?
A. SQL tidak membutuhkan memori RAM pada peladen.  
B. SQL secara ketat menjamin sifat ACID sehingga mencegah mutasi saldo yang korup atau inkonsisten.  
C. SQL dapat menyimpan rekaman video dan audio secara otomatis tanpa pengindeksan.  
D. NoSQL tidak mendukung sistem operasi Linux dan Windows.  
E. SQL tidak memerlukan lisensi perangkat lunak apa pun.  

4. Dalam algoritma klastering K-Means, apa yang terjadi pada tahapan *Update Step* setelah semua titik data dikelompokkan ke centroid terdekat?
A. Menghapus titik data yang berada di tepi terjauh klaster.  
B. Menghitung kembali posisi titik centroid baru berdasarkan rata-rata koordinat seluruh anggota di klaster tersebut.  
C. Mengubah nilai parameter k menjadi dua kali lipat.  
D. Mengalikan jarak Euclidean dengan faktor konstanta kuadratik.  
E. Menghentikan program secara mendadak.  

5. Perhatikan data evaluasi inersia (WCSS) dari pengujian klastering K-Means berikut:
- k = 1: WCSS = 8.500
- k = 2: WCSS = 3.200
- k = 3: WCSS = 1.100
- k = 4: WCSS = 1.020
- k = 5: WCSS = 960
Berdasarkan pendekatan Elbow Method, jumlah klaster *k* yang paling ideal dan optimal untuk dipilih adalah...
A. k = 1  
B. k = 2  
C. k = 3  
D. k = 5  
E. k = 7  

6. Sebelum melakukan perhitungan jarak Euclidean pada algoritma K-Means, Arya melakukan proses penskalaan fitur (*Feature Scaling*) menggunakan `StandardScaler`. Tujuan utama proses ini adalah...
A. Mengubah seluruh nilai data teks menjadi huruf kapital.  
B. Menyamakan rentang skala antar-variabel agar fitur dengan rentang angka besar (seperti pendapatan jutaan rupiah) tidak mendominasi fitur berangka kecil (seperti skor 1-10).  
C. Menghilangkan data yang bernilai desimal menjadi bilangan bulat.  
D. Menghapus seluruh data duplikat secara otomatis.  
E. Mengubah algoritma unsupervised menjadi supervised learning.  

7. Sebuah institusi kesehatan ingin membagikan dataset rekam medis pasien untuk keperluan riset akademis kecerdasan artifisial. Agar identitas pasien terlindungi sesuai etika privasi, tim rekayasa mengganti nama asli pasien dengan kode hash acak seperti `e3b0c44298fc...`. Teknik rekayasa pelindungan data ini disebut...
A. Enkripsi Simetris  
B. Kompresi Data  
C. Pseudonimisasi  
D. Normalisasi Skema  
E. Overfitting  

8. Manakah dari skenario berikut yang mencerminkan pelanggaran serius terhadap prinsip *Keterbatasan Tujuan (*Purpose Limitation*)* dalam Undang-Undang Pelindungan Data Pribadi (UU PDP No. 27/2022)?
A. Pengguna meminta penyedia aplikasi untuk menghapus riwayat akunnya (*Right to Erasure*).  
B. Rumah sakit menyimpan data rekam medis pasien di peladen lokal terenkripsi.  
C. Aplikasi peta penunjuk jalan meminta izin akses GPS saat navigasi rute aktif.  
D. Lembaga pinjaman online menjual basis data nomor kontak darurat penggunanya kepada biro iklan pihak ketiga tanpa persetujuan tertulis pemilik data.  
E. Perusahaan melakukan backup basis data mingguan ke media penyimpanan terisolasi.  

9. Prinsip Kedaulatan Data (*Data Sovereignty*) mewajibkan data strategis instansi pemerintah dan kependudukan Indonesia disimpan di pusat data di dalam negeri. Alasan utama di balik regulasi ini ditinjau dari kedaulatan bangsa adalah...
A. Mencegah kabel bawah laut kelebihan beban transmisi.  
B. Memastikan yurisdiksi hukum Indonesia berlaku mutlak atas perlindungan, pengawasan, dan keamanan data nasional dari intervensi asing.  
C. Biaya pendingin peladen di iklim tropis lebih murah daripada negara subtropis.  
D. Agar seluruh sistem operasi komputer di Indonesia dapat diganti dengan bahasa daerah.  
E. Menjamin kecepatan internet di daerah pedesaan sama dengan kota metropolitan.  

10. Kelemahan mendasar dari algoritma K-Means konvensional yang wajib diwaspadai oleh rekayasawan data adalah...
A. Algoritma K-Means tidak dapat dijalankan pada bahasa pemrograman Python.  
B. Hasil akhir klastering sangat peka terhadap penentuan posisi centroid awal secara acak (*local optima trap*).  
C. K-Means hanya mampu memproses data dengan format berkas gambar biner.  
D. K-Means mewajibkan seluruh data telah memiliki label kelas yang teruji di laboratorium.  
E. Nilai WCSS pada K-Means selalu bernilai nol pada setiap iterasi.  

---

### Bagian 2: Uraian dan Pemecahan Masalah Sistemik (5 Soal)

1. Jelaskan perbedaan fundamental antara paradigma **Supervised Learning (Klasifikasi)** dan **Unsupervised Learning (Klastering)**! Berikan satu contoh kasus nyata penerapan klastering dalam sektor logistik perikanan di Indonesia!

2. Uraikan secara rinci karakteristik **5V** dalam ekosistem Big Data! Mengapa aspek **Veracity (Kebenaran Data)** menjadi tantangan paling berat ketika kita menganalisis opini masyarakat dari media sosial?

3. Jelaskan cara kerja **Metode Siku (*Elbow Method*)** dalam menentukan jumlah kelompok *k* pada algoritma K-Means! Gambarkan konsep kurva inersia WCSS dan titik perubahannya!

4. Mengapa arsitektur penyimpanan **Data Lake** sangat ideal digunakan untuk menampung data mentah telemetri perangkat IoT dan multimedia dibanding basis data relasional PostgreSQL konvensional?

5. Sebagai arsitek data terpercaya, sebutkan dan jelaskan 3 langkah teknis dan hukum yang wajib kalian terapkan untuk mematuhi amanat **Undang-Undang Pelindungan Data Pribadi (UU PDP No. 27/2022)** ketika merancang sistem kecerdasan artifisial yang mengumpulkan data masyarakat!

---

### KUNCI JAWABAN DAN PEMBAHASAN LENGKAP BAB II

#### Kunci Jawaban Pilihan Ganda:
1. **B (Velocity)** — Aliran data koordinat dari 12.000 kapal setiap 200 milidetik berfokus pada kecepatan laju transmisi dan pemrosesan seketika (*real-time processing*), yang merupakan inti dari karakteristik *Velocity*.
2. **C (Basis Data Dokumen NoSQL MongoDB)** — Format data pasangan kunci-nilai dan larik bersarang (JSON/BSON) adalah karakteristik murni dari basis data dokumen NoSQL seperti MongoDB.
3. **B (SQL secara ketat menjamin sifat ACID sehingga mencegah mutasi saldo yang korup atau inkonsisten)** — Kepatuhan ACID menjamin bahwa transaksi perbankan dieksekusi secara utuh atau dibatalkan sama sekali (*All-or-Nothing*), menghindari saldo hilang di tengah jalan.
4. **B (Menghitung kembali posisi titik centroid baru berdasarkan rata-rata koordinat seluruh anggota di klaster tersebut)** — Tahap pembaruan (*Update Step*) menghitung mean vektor posisi seluruh data yang terdaftar dalam klaster tersebut untuk menjadi koordinat centroid baru.
5. **C (k = 3)** — Dari k=1 ke k=2 inersia turun 5.300 poin, dari k=2 ke k=3 turun 2.100 poin, namun dari k=3 ke k=4 penurunan hanya melambat drastis sebesar 80 poin. Titik tekukan siku (*elbow*) terjadi tepat pada k = 3.
6. **B (Menyamakan rentang skala antar-variabel agar fitur dengan rentang angka besar tidak mendominasi fitur berangka kecil)** — Penskalaan fitur mencegah rumus jarak Euclidean didominasi oleh dimensi dengan magnitude skala ribuan/jutaan.
7. **C (Pseudonimisasi)** — Menggantikan informasi pengenal langsung dengan kode pengenal semu (pseudonim/hash) sehingga data tidak dapat diatribusikan ke subjek data spesifik tanpa informasi tambahan terpisah.
8. **D (Lembaga pinjaman online menjual basis data kontak darurat ke pihak ketiga tanpa persetujuan)** — Merupakan pelanggaran berat terhadap prinsip keterbatasan tujuan dan ketiadaan konsen pemilik data.
9. **B (Memastikan yurisdiksi hukum Indonesia berlaku mutlak atas perlindungan, pengawasan, dan keamanan data nasional dari intervensi asing)** — Penempatan data di dalam yurisdiksi nasional menjamin supremasi hukum dan kedaulatan negara dalam mengawasi informasi strategis bangsa.
10. **B (Hasil akhir klastering sangat peka terhadap penentuan posisi centroid awal secara acak)** — Inisialisasi centroid acak dapat menjebak algoritma pada optimum lokal (*local optima*), yang diatasi di industri dengan algoritma `k-means++`.

#### Pembahasan Soal Uraian:
1. **Perbedaan Klasifikasi vs Klastering:**
   - *Supervised Learning (Klasifikasi):* Membutuhkan dataset berlabel (*ground truth*) di awal untuk melatih model memetakan input ke kategori output tertentu.
   - *Unsupervised Learning (Klastering):* Bekerja tanpa label awal; algoritma mencari pola alami, kesamaan fitur, dan kepadatan geometris data secara mandiri.
   - *Contoh Kasus:* Pengelompokan 10.000 kapal nelayan berdasarkan rute jelajah dan kapasitas palka kapal tanpa label awal, menghasilkan klaster "Nelayan Pantai Harian", "Kapal Cakalang Lepas Pantai", dan "Armada Industri Laut Dalam" untuk penataan kuota BBM bersubsidi.
2. **Karakteristik 5V dan Tantangan Veracity:**
   - 5V: *Volume* (kuantitas), *Velocity* (kecepatan), *Variety* (keberagaman format), *Veracity* (keandalan/kebenaran), dan *Value* (nilai manfaat).
   - Veracity menjadi tantangan paling berat pada data media sosial karena tingginya tingkat subjektivitas bahasa kiasan, sarkasme, akun bot otomatis, kesalahan pengetikan (*typo*), serta keberadaan berita bohong (*disinformasi*) yang dapat menyesatkan model analisis sentimen.
3. **Metode Siku (Elbow Method):**
   - Dihitung dengan menjumlahkan kuadrat jarak seluruh anggota ke centroid-nya (WCSS / Inersia) untuk variasi nilai k (1 s.d. n).
   - Kurva WCSS menurun secara eksponensial seiring bertambahnya k. Titik di mana laju penurunan melambat secara drastis (membentuk sudut siku tajam) menunjukkan penambahan klaster berikutnya tidak lagi memberikan reduksi inersia yang signifikan, menandai jumlah k paling optimal.
4. **Keunggulan Data Lake dibanding PostgreSQL:**
   - Data Lake mengadopsi paradigma *Schema-on-Read*, mampu menelan berkas biner mentah, log JSON, berkas video, dan sinyal telemetri berkecepatan gigabyte per detik tanpa proses konversi skema yang lambat. Sementara PostgreSQL (*Schema-on-Write*) mewajibkan data distrukturkan ke tabel relasional yang kaku sebelum disimpan.
5. **3 Langkah Kepatuhan terhadap UU PDP No. 27/2022:**
   - *Langkah 1 (Persetujuan Eksplisit / Consent):* Menyediakan lembar persetujuan digital yang transparan dan mudah dipahami pengguna mengenai data apa saja yang diambil dan tujuan pemrosesannya.
   - *Langkah 2 (Anonimisasi & Enkripsi Data):* Menerapkan enkripsi AES-256 pada data saat tersimpan (*data at rest*) dan saat dikirim (*data in transit*), serta menerapkan teknik pseudonimisasi/masking pada atribut identitas warga.
   - *Langkah 3 (Kedaulatan & Mekanisme Penghapusan):* Menempatkan server database utama di pusat data nasional Indonesia dan menyediakan tombol fitur hak penghapusan akun beserta seluruh data riwayat pengguna (*Right to Erasure*).
"""
