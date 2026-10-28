"""
Modul Naskah Bab IV Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB4_SMA11 = """# BAB IV: FONDASI MACHINE LEARNING: PIPELINE, KLASIFIKASI, DAN EVALUASI MODEL

## APERSEPSI: MENGAPA AKURASI 98% BISA MENIPU KITA?

Di ruang laboratorium kecerdasan artifisial sekolah, Arya tampak bersorak gembira sambil memamerkan hasil grafik di layar monitornya. Di hadapannya, sebuah skrip Python berbasis pustaka Scikit-Learn baru saja selesai mengeksekusi pelatihan model klasifikasi deteksi dini tumor medis.

[GAMBAR: assets/bab4_komik_pembuka_sma11.png]

"Dinda, Bagas, lihat pencapaian ini!" seru Arya dengan penuh kebanggaan. "Model kecerdasan artifisial yang kulatih berhasil meraih skor Akurasi 98,5%! Dari 1.000 data rekam medis pasien uji coba, programku hampir tidak pernah salah memprediksi!"

Dinda mendekat, mengamati struktur sebaran dataset yang digunakan Arya dengan pandangan analitis yang tajam. "Tunggu sebentar, Arya. Mari kita bedah isi dataset yang kamu gunakan. Dari 1.000 data pasien tersebut, berapa banyak pasien yang benar-benar mengidap tumor ganas, dan berapa banyak pasien yang kondisi tubuhnya sehat?"

Arya membuka tabel data mentahnya. "Hmm, di dalam dataset riil ini, pasien yang positif mengidap tumor hanya berjumlah 15 orang, sedangkan 985 pasien lainnya berstatus sehat non-tumor."

Dinda tersenyum prihatin seraya menunjuk baris prediksi model. "Lihat kenyataan pahit ini, kawan. Jika model AI-mu dirancang secara malas untuk selalu menebak bahwa 'Semua Pasien Pasti Sehat', maka secara matematis modelmu otomatis akan langsung memperoleh Akurasi 98,5% (985 dari 1.000 tebakan benar)! Namun apa yang terjadi pada 15 pasien yang sebenarnya mengidap tumor ganas? Modelmu memprediksi mereka sehat, membiarkan penyakit mematikan itu menyebar tanpa penanganan medis!"

Bagas terperangah. "Mengerikan sekali! Pasien yang sakit justru dinyatakan sehat! Itu adalah bencana kegagalan medis yang fatal!"

"Tepat sekali," tegas Dinda. "Pada dataset yang memiliki distribusi kelas sangat timpang (*imbalanced dataset*), parameter Akurasi semu bisa menjadi jebakan mematikan. Dalam rekayasa *Machine Learning* profesional, kita wajib mengevaluasi model secara objektif menggunakan **Matriks Konfusi (*Confusion Matrix*)**, membedah risiko **False Negative**, serta mengukur nilai **Recall**, **Presisi**, dan **F1-Score**!"

Arya tertegun lalu mengangguk penuh rasa hormat. "Kamu benar sekali, Dinda. Ternyata melatih kecerdasan artifisial bukan sekadar mengejar angka akurasi tinggi, melainkan memahami sains matematika evaluasi model. Mari kita bedah tuntas siklus pipeline Machine Learning ini!"

---

## A. TAKSONOMI MACHINE LEARNING: SUPERVISED, UNSUPERVISED, DAN REINFORCEMENT

Untuk memahami kecerdasan artifisial modern, kita harus memahami pergeseran mendasar dari pemrograman konvensional menuju paradigma pembelajaran mesin (*Machine Learning* / ML).

### 1. Paradigma Rule-Based vs Machine Learning

- **Pemrograman Berbasis Aturan Konvensional (*Rule-Based*):**
Manusia merumuskan aturan logika eksplisit (*Rules*) berupa percabangan `if-else` yang kaku, lalu memasukkannya bersama Data masukan ke dalam komputer untuk menghasilkan Jawaban (*Answers*). Kelemahannya: manusia tidak mampu menulis jutaan aturan jika data sangat rumit (seperti mengenali wajah atau mendeteksi sel kanker).
- **Pembelajaran Mesin (*Machine Learning*):**
Membalik paradigma tersebut secara revolusioner. Manusia memasukkan Data dan Jawaban historis ke dalam komputer, lalu algoritma matematika secara mandiri mencari dan memelajari pola aturan (*Rules/Patterns*) tersembunyi di balik data tersebut.

### 2. Tiga Cabang Utama Taksonomi Machine Learning

1. **Supervised Learning (Pembelajaran Terawasi):**
Algoritma dilatih menggunakan dataset yang telah memiliki label kebenaran (*labeled data*). Ibarat seorang murid yang belajar mengerjakan latihan soal disertai kunci jawaban di sampingnya.
Terbagi menjadi dua tugas utama:
- *Klasifikasi:* Memprediksi label kategori diskret (misal: menentukan email Spam vs Bukan Spam, atau memilah tumor Jinak vs Ganas).
- *Regresi:* Memprediksi nilai angka kontinu (misal: memprediksi harga jual rumah berdasarkan luas tanah atau memprediksi suhu udara harian).
2. **Unsupervised Learning (Pembelajaran Tanpa Pengawasan):**
Algoritma diberikan data mentah tanpa label kunci jawaban (*unlabeled data*). Komputer bertugas menemukan struktur alami, kemiripan kelompok, atau pola tersembunyi secara mandiri.
Contoh: Segmentasi pengelompokan pelanggan (*Customer Clustering*) pada aplikasi belanja daring.
3. **Reinforcement Learning (Pembelajaran Berbasis Penguatan):**
Model agen cerdas belajar mengambil keputusan terbaik melalui proses coba-coba (*trial and error*) dalam sebuah lingkungan interaktif, dengan tujuan memaksimalkan penghargaan (*Reward*) dan meminimalkan hukuman (*Penalty*).
Contoh: Agen AI pengemudi mobil otonom atau bot pemain catur profesional (AlphaZero).

---

## B. TAHAPAN PRA-PEMROSESAN DATA DAN PEMBAGIAN DATASET (TRAIN-TEST SPLIT)

Dalam pepatah sains data terkenal: *"Garbage In, Garbage Out"*—jika kita melatih algoritma AI menggunakan data mentah yang kotor, model cerdas apa pun pasti akan menghasilkan prediksi yang kacau dan menyesatkan.

[GAMBAR: assets/bab4_alur_kerja_pipeline_machine_learning.png]

### 1. Siklus Alur Kerja Pipeline Machine Learning

Tahapan rekayasa data standar industri mencakup langkah-langkah berurutan:
1. **Pembersihan Data Nilai Kosong (*Handling Missing Values*):** Mengisi sel data kosong menggunakan nilai rata-rata (*Mean*), nilai tengah (*Median*), atau menghapus baris data jika kerusakannya parah.
2. **Pengkodean Fitur Kategori (*Encoding Categorical Data*):** Komputer hanya memahami angka. Fitur bertipe teks harus dikonversi:
   - *Label Encoding:* Mengubah kategori berjenjang menjadi angka urut (misal: SD=0, SMP=1, SMA=2).
   - *One-Hot Encoding:* Membuat kolom biner baru (0 atau 1) untuk kategori yang setara (misal: Jurusan RPL, Jurusan TKJ, Jurusan DKV) agar model tidak salah mengartikan adanya tingkatan matematis.
3. **Penskalaan Fitur (*Feature Scaling*):** Menyeragamkan rentang skala angka antar-fitur (misal: fitur Umur 15-18 tahun dan fitur Pendapatan Rp2.000.000 - Rp10.000.000) menggunakan metode *Min-Max Normalization* (rentang 0 hingga 1) atau *StandardScaler* (skor-Z). Tanpa penskalaan, fitur dengan angka besar akan mendominasi perhitungan secara tidak adil.

### 2. Pembagian Dataset Latih dan Dataset Uji (Train-Test Split)

Prinsip paling sakral dalam evaluasi pembelajaran mesin adalah **pemisahan data latih dan data uji**. Kita membagi dataset mentah menjadi dua bagian independen:
- **Data Latih (*Training Set* - 80%):** Diberikan kepada algoritma untuk mempelajari pola hubungan antar-fitur dan label.
- **Data Uji (*Testing Set* - 20%):** Disimpan secara rahasia dan **sama sekali tidak boleh dilihat oleh algoritma selama proses pelatihan**. Data uji digunakan murni untuk menguji kemampuan generalisasi model terhadap data baru yang belum pernah dijumpai sebelumnya.

Pelanggaran terhadap prinsip ini disebut **Kebocoran Data (*Data Leakage*)**, yang mengakibatkan model tampak sangat pintar saat diuji di laboratorium (*Overfitting*), namun gagal total saat diterapkan di dunia nyata.

---

## C. EKSPLORASI ALGORITMA KLASIFIKASI: KNN DAN DECISION TREE

Ada dua algoritma klasifikasi terawasi paling fundamental yang wajib dikuasai calon praktisi AI:

### 1. K-Nearest Neighbors (KNN)

Algoritma KNN bekerja berdasarkan prinsip filosofis pepatah kuno: *"Tunjukkan siapa teman-teman terdekatmu, maka aku akan tahu siapa dirimu."* KNN tidak membangun rumus matematika rumit saat pelatihan, melainkan memprediksi label data baru berdasarkan mayoritas label dari sejumlah **k** tetangga terdekatnya.

Jarak geometris antara data baru dan data historis dihitung menggunakan rumus **Jarak Euclidean (*Euclidean Distance*)**:
`Jarak = Akar_Kuadrat( (x2 - x1)^2 + (y2 - y1)^2 + ... + (zn - z1)^2 )`

**Aturan Penentuan Nilai k:**
Gunakan selalu **bilangan ganjil** (misal k = 3, 5, atau 7) untuk menghindari terjadinya kondisi seri (*tie vote*) ketika model menentukan keputusan mayoritas antardua kelas.

### 2. Decision Tree (Pohon Keputusan)

Decision Tree bekerja memodelkan logika pengambilan keputusan menyerupai struktur pohon terbalik: dimulai dari simpul akar (*Root Node*), bercabang melalui pengujian kondisi (*Internal Nodes*), hingga berakhir pada daun kesimpulan (*Leaf Nodes*).

**Bagaimana Algoritma Memilih Fitur Pemisah Terbaik?**
Algoritma mengukur derajat ketidakmurnian (*impurity*) data. Parameter standar yang digunakan adalah **Gini Impurity**:
`Gini = 1 - Jumlah( p_i^2 )`
di mana `p_i` adalah probabilitas kemunculan kelas ke-i pada simpul tersebut. Simpul yang murni sempurna (seluruh anggotanya berasal dari kelas yang sama) memiliki nilai Gini = 0. Fitur yang menghasilkan penurunan nilai Gini paling drastis (*Information Gain* terbesar) akan dipilih sebagai simpul pemecah cabang.

---

## D. EVALUASI OBJEKTIF KINERJA MODEL: MATRIKS KONFUSI (CONFUSION MATRIX)

Bagaimana kita mengukur kinerja model secara adil, ilmiah, dan tidak tertipu oleh akurasi semu? Jawabannya adalah membedah prediksi model ke dalam **Matriks Konfusi (*Confusion Matrix*)**.

[GAMBAR: assets/bab4_diagram_matriks_konfusi_evaluasi.png]

### 1. Anatomi Tabel Kontingensi 2x2

Misalkan kita menguji model pendeteksi Penyakit Kanker (di mana Positif = Terkena Kanker, Negatif = Sehat):
- **True Positive (TP):** Pasien AKTUAL POSITIF, dan model MEMPREDIKSI POSITIF (Tepat & Menyelamatkan Nyawa).
- **True Negative (TN):** Pasien AKTUAL NEGATIF, dan model MEMPREDIKSI NEGATIF (Tepat & Membawa Ketenangan).
- **False Positive (FP / Galat Tipe I):** Pasien AKTUAL NEGATIF, namun model SALAH MEMPREDIKSI POSITIF (Alarm Palsu / Pasien panik namun bisa dikoreksi lewat tes lanjutan).
- **False Negative (FN / Galat Tipe II - SANGAT BERBAHAYA!):** Pasien AKTUAL POSITIF KANKER, namun model SALAH MEMPREDIKSI NEGATIF SEHAT (Pasien pulang tanpa pengobatan hingga penyakitnya terlambat ditangani).

### 2. Empat Pilar Metrik Evaluasi Matematis

1. **Akurasi (Accuracy):**
   `Akurasi = (TP + TN) / (TP + TN + FP + FN)`
   Hanya relevan digunakan jika jumlah kelas positif dan negatif di dalam dataset seimbang (*balanced*).
2. **Presisi (Precision):**
   `Presisi = TP / (TP + FP)`
   Mengukur seberapa akurat tebakan positif model. Sangat krusial pada kasus di mana biaya akibat False Positive sangat mahal (misal: sistem penyaring spam email atau prediksi kelayakan investasi saham).
3. **Recall (Sensitivitas / True Positive Rate):**
   `Recall = TP / (TP + FN)`
   Mengukur kemampuan model menangkap seluruh data yang sebenarnya positif. **Sangat krusial pada kasus di mana False Negative berakibat fatal** (misal: pendeteksi kanker, sistem peringatan dini tsunami, atau deteksi kebakaran pabrik).
4. **F1-Score:**
   `F1-Score = 2 * (Presisi * Recall) / (Presisi + Recall)`
   Rata-rata harmonik penyeimbang antara Presisi dan Recall. Nilai F1-Score yang tinggi menjamin model bekerja andal tanpa mengorbankan salah satu metrik.

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 4.1

### Pelatihan dan Evaluasi Model Klasifikasi dengan Python Scikit-Learn

**Tujuan Pembelajaran:**
Peserta didik mampu memuat dataset tabular, membagi data latih dan data uji (80:20), melatih model klasifikasi K-Nearest Neighbors (KNN), mengekstrak matriks konfusi, serta menghitung nilai Akurasi, Presisi, Recall, dan F1-Score menggunakan pustaka Scikit-Learn.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terpasang.
2. Pustaka eksternal terinstal: `pip install scikit-learn pandas numpy`.
3. Editor Visual Studio Code atau Google Colab.

**Instruksi Kerja Praktikum:**
1. Buatlah berkas baru bernama `praktikum_ml_evaluasi.py`.
2. Ketikkan skrip implementasi alur kerja pipeline Machine Learning terpadu berikut:

```python
# Pipeline Machine Learning Terapan & Evaluasi Model
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def jalankan_eksperimen_ai():
    print("===== 1. PEMBUATAN DATASET SIMULASI MEDIS TIMPANG =====")
    # Membuat 1000 data sampel: 95% Sehat (0), 5% Pasien Kritis (1)
    X, y = make_classification(
        n_samples=1000, 
        n_features=5, 
        weights=[0.95, 0.05], 
        random_state=42
    )
    print(f"Total Sampel : {len(y)}")
    print(f"Kelas Sehat (0)  : {np.sum(y == 0)} pasien")
    print(f"Kelas Kritis (1) : {np.sum(y == 1)} pasien (Timpang)")

    # 2. Pembagian Dataset (Train-Test Split 80:20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 3. Penskalaan Fitur (Feature Scaling)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Pelatihan Model K-Nearest Neighbors (k=3)
    model_knn = KNeighborsClassifier(n_neighbors=3)
    model_knn.fit(X_train_scaled, y_train)

    # 5. Pengujian Prediksi pada Data Uji yang Dirahasiakan
    y_pred = model_knn.predict(X_test_scaled)

    # 6. Analisis Matriks Konfusi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    print("\n===== 2. MATRIKS KONFUSI (CONFUSION MATRIX) =====")
    print(f"True Negative  (TN) : {tn} (Pasien sehat diprediksi tepat)")
    print(f"False Positive (FP) : {fp} (Alarm palsu)")
    print(f"False Negative (FN) : {fn} (Pasien kritis terlewat / FATAL!)")
    print(f"True Positive  (TP) : {tp} (Pasien kritis terdeteksi tepat)")

    # 7. Perhitungan Metrik Evaluasi Ilmiah
    akurasi = accuracy_score(y_test, y_pred)
    presisi = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (presisi * recall) / (presisi + recall) if (presisi + recall) > 0 else 0

    print("\n===== 3. LAPORAN METRIK KINERJA MODEL =====")
    print(f"Akurasi Total : {akurasi * 100:.2f}%")
    print(f"Presisi Model : {presisi * 100:.2f}%")
    print(f"Recall Model  : {recall * 100:.2f}% (Sensitivitas Nyata)")
    print(f"F1-Score      : {f1 * 100:.2f}% (Keseimbangan)")
    print("=" * 45)

if __name__ == "__main__":
    jalankan_eksperimen_ai()
```

3. Jalankan program di terminal dan amatilah perbandingan antara nilai Akurasi Total dengan nilai Recall!
4. Modifikasilah parameter jumlah tetangga `n_neighbors` dari k = 3 menjadi k = 7 dan amati apakah nilai Recall mengalami perubahan!

**Pertanyaan Analisis Laboratorium:**
1. Mengapa fungsi penskalaan `scaler.fit_transform()` hanya diterapkan pada `X_train`, sedangkan untuk `X_test` kita hanya memanggil `scaler.transform()` tanpa pemanggilan fungsi `fit()`? Jelaskan hubungannya dengan bahaya *Data Leakage*!
2. Jika sebuah model AI pendeteksi spam email memiliki nilai Presisi 99% tetapi Recall-nya hanya 40%, apakah dampak yang dirasakan oleh pengguna kotak masuk email tersebut?
3. Uraikan mengapa pada kasus sistem pendeteksi kebocoran gas beracun di pabrik, para insinyur lebih memilih model yang memiliki nilai Recall 99% meskipun nilai Presisinya hanya 75%!

---

## F. RANGKUMAN MATERI BAB IV

1. **Taksonomi Pembelajaran Mesin:** Paradigma Machine Learning membiarkan komputer memelajari pola aturan dari data historis secara mandiri. Terbagi menjadi *Supervised Learning* (berbasis label: klasifikasi dan regresi), *Unsupervised Learning* (tanpa label: klastering), dan *Reinforcement Learning* (pembelajaran agen berbasis reward).
2. **Pipeline dan Pencegahan Data Leakage:** Siklus data mencakup penanganan nilai kosong, pengkodean kategori (Label / One-Hot Encoding), dan penskalaan rentang numerik (*StandardScaler*). Pembagian dataset menjadi data latih (80%) dan data uji rahasia (20%) mutlak diwajibkan untuk menguji generalisasi model bebas bias.
3. **Algoritma Klasifikasi Populer:** K-Nearest Neighbors (KNN) mengklasifikasikan data berdasarkan voting mayoritas k tetangga terdekat dengan jarak Euclidean. Decision Tree membagi simpul data berdasarkan penurunan nilai ketidakmurnian Gini (*Gini Impurity*).
4. **Evaluasi Matriks Konfusi (Confusion Matrix):** Tabel pemetaan True Positive, True Negative, False Positive, dan False Negative. Pada dataset timpang, nilai Akurasi semu sering kali menipu. Evaluasi sistem kritis mengutamakan nilai **Recall** (untuk meminimalkan bahaya fatal False Negative) dan **F1-Score** sebagai tolok ukur keandalan paripurna.

---

## G. UJI KOMPETENSI BAB IV

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Perbedaan mendasar antara paradigma pemrograman konvensional (*Rule-Based*) dan paradigma pembelajaran mesin (*Machine Learning*) adalah...
   A. Pemrograman konvensional tidak membutuhkan komputer
   B. Machine Learning memasukkan Data dan Jawaban ke dalam komputer untuk menghasilkan aturan pola (*Rules*), sedangkan pemrograman konvensional memasukkan Aturan dan Data untuk menghasilkan Jawaban
   C. Machine Learning hanya dapat dijalankan pada ponsel cerdas
   D. Pemrograman konvensional menghasilkan keluaran berupa gambar tiga dimensi

2. Cabang pembelajaran mesin yang melatih model menggunakan kumpulan data yang telah memiliki label jawaban yang benar dinamakan...
   A. Unsupervised Learning
   B. Reinforcement Learning
   C. Supervised Learning
   D. Heuristic Learning

3. Praktik rekayasa data yang memisahkan dataset mentah menjadi data latih (80%) dan data uji rahasia (20%) bertujuan utama untuk...
   A. Menghemat kapasitas penyimpanan harddisk komputer
   B. Menghindari kebocoran data (*Data Leakage*) dan menguji kemampuan generalisasi model terhadap data baru
   C. Mempercepat koneksi internet saat mengunggah kode
   D. Mengubah tipe data teks menjadi gambar vektor

4. Algoritma klasifikasi terawasi yang memprediksi label suatu data baru berdasarkan mayoritas label dari data terdekat di sekitarnya menggunakan rumus jarak Euclidean adalah...
   A. Decision Tree
   B. K-Nearest Neighbors (KNN)
   C. K-Means Clustering
   D. Linear Regression

5. Mengapa dalam menentukan nilai parameter tetangga k pada algoritma KNN sangat disarankan menggunakan bilangan ganjil (seperti k = 3, 5, atau 7)?
   A. Agar komputer tidak mengalami kehabisan memori
   B. Untuk menghindari terjadinya hasil imbang atau seri (*tie vote*) saat proses penentuan kelas mayoritas
   C. Karena bilangan genap tidak dapat dibagi oleh rumus jarak
   D. Agar model secara otomatis berubah menjadi pohon keputusan

6. Ukuran derajat ketidakmurnian data yang digunakan oleh algoritma Decision Tree untuk menentukan simpul pemecah cabang terbaik dinamakan...
   A. Euclidean Metric
   B. Gini Impurity
   C. Cosine Similarity
   D. Manhattan Distance

7. Dalam sebuah Matriks Konfusi pada sistem pendeteksi penyakit medis, kondisi di mana seorang pasien sebenarnya sehat normal namun sistem AI secara keliru memprediksinya sebagai pasien sakit (alarm palsu) dikategorikan sebagai...
   A. True Positive (TP)
   B. True Negative (TN)
   C. False Positive (FP)
   D. False Negative (FN)

8. Kondisi paling berbahaya pada sistem medis pendeteksi penyakit jantung, di mana pasien yang sebenarnya terkena serangan jantung fatal justru diprediksi sehat oleh sistem AI dan dipulangkan tanpa obat, merupakan manifestasi dari...
   A. False Negative (FN)
   B. False Positive (FP)
   C. True Positive (TP)
   D. True Negative (TN)

9. Metrik evaluasi kinerja model klasifikasi yang dihitung dengan membagi jumlah True Positive terhadap total data yang sebenarnya positif (TP / [TP + FN]) dinamakan...
   A. Akurasi
   B. Recall (Sensitivitas)
   C. Presisi
   D. Spesifisitas

10. Metrik evaluasi yang merupakan rata-rata harmonik penyeimbang antara nilai Presisi dan nilai Recall, sangat andal digunakan pada dataset dengan sebaran kelas yang timpang (*imbalanced dataset*), dinamakan...
    A. Mean Squared Error
    B. R-Squared
    C. F1-Score
    D. Z-Score

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan mengapa metrik Akurasi Total (*Accuracy*) dapat menjadi parameter evaluasi yang sangat menyesatkan (*misleading*) ketika diterapkan pada dataset yang memiliki ketimpangan kelas ekstrem (*imbalanced dataset*)! Berikan ilustrasi kasus nyatanya!
2. Uraikan tahapan alur kerja standar (*Machine Learning Pipeline*) mulai dari pengumpulan data mentah hingga model siap diterapkan ke lingkungan produksi (*deployment*)!
3. Diberikan matriks konfusi dari pengujian model pendeteksi transaksi penipuan kartu kredit (*Fraud Detection*) terhadap 1.000 transaksi uji:
   - True Positive (TP) = 40 transaksi penipuan terdeteksi tepat
   - False Positive (FP) = 10 transaksi sah salah dituduh penipuan
   - False Negative (FN) = 5 transaksi penipuan lolos tak terdeteksi
   - True Negative (TN) = 945 transaksi sah diprediksi tepat
   Hitunglah nilai Akurasi, Presisi, Recall, dan F1-Score dari model tersebut secara matematis!
4. Dalam perancangan sistem keselamatan mobil otonom yang bertugas mendeteksi pejalan kaki yang menyeberang jalan, analisislah mana yang membawa dampak risiko kemanusiaan lebih fatal antara *False Positive* atau *False Negative*! Jelaskan konsekuensi operasional dari masing-masing jenis galat tersebut!
5. Jelaskan perbedaan mendasar antara kondisi model yang mengalami *Overfitting* dan *Underfitting*! Bagaimana cara seorang pengembang AI mendeteksi dan mengatasi masalah overfitting saat melatih model Decision Tree?

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB IV

**Kunci Pilihan Ganda:**
1. **B** (Machine Learning memelajari aturan pola dari data dan jawaban historis secara otomatis).
2. **C** (Supervised Learning dilatih menggunakan data berlabel kunci jawaban).
3. **B** (Train-Test Split menguji generalisasi model dan mencegah kebocoran data / data leakage).
4. **B** (KNN mengklasifikasikan data berdasarkan voting tetangga terdekat dengan jarak Euclidean).
5. **B** (Nilai k ganjil mencegah terjadinya seri/tie vote pada klasifikasi biner).
6. **B** (Gini Impurity mengukur ketidakmurnian simpul pemisah pada Decision Tree).
7. **C** (False Positive adalah alarm palsu, aktual negatif namun diprediksi positif).
8. **A** (False Negative adalah kondisi paling berbahaya di mana kasus aktual positif gagal terdeteksi).
9. **B** (Recall mengukur rasio kasus aktual positif yang berhasil ditangkap sistem).
10. **C** (F1-Score adalah rata-rata harmonik penyeimbang antara Presisi dan Recall).

**Pembahasan Soal Uraian:**
1. *Kelemahan Akurasi pada Imbalanced Data:*
   Pada dataset yang timpang (misalnya 990 data transaksi normal dan 10 data penipuan perbankan), sebuah model bodoh yang memprediksi seluruh transaksi berstatus normal tanpa berpikir akan langsung memperoleh akurasi 990/1.000 = 99%. Namun model tersebut memiliki nilai Recall 0% karena gagal mendeteksi satupun penipuan kartu kredit. Akurasi tinggi memberikan rasa aman semu padahal sistem sama sekali tidak berguna secara operasional.
2. *Tahapan Machine Learning Pipeline:*
   (1) Pengumpulan dataset mentah; (2) Pembersihan data (imputasi nilai kosong missing values); (3) Rekayasa fitur (One-Hot Encoding untuk teks kategori, Penskalaan fitur StandardScaler); (4) Pemisahan data latih (80%) dan data uji (20%); (5) Pelatihan algoritma model pada data latih; (6) Evaluasi objektif performa model pada data uji menggunakan Confusion Matrix; (7) Penerapan model (Deployment) melalui antarmuka REST API.
3. *Perhitungan Evaluasi Fraud Detection:*
   - Total Sampel = TP + FP + FN + TN = 40 + 10 + 5 + 945 = 1.000.
   - Akurasi = (TP + TN) / Total = (40 + 945) / 1000 = 985 / 1000 = **98,5% (0,985)**.
   - Presisi = TP / (TP + FP) = 40 / (40 + 10) = 40 / 50 = **80,0% (0,800)**.
   - Recall = TP / (TP + FN) = 40 / (40 + 5) = 40 / 45 = **88,89% (0,889)**.
   - F1-Score = 2 * (Presisi * Recall) / (Presisi + Recall) = 2 * (0,80 * 0,8889) / (0,80 + 0,8889) = 1,4222 / 1,6889 = **84,21% (0,842)**.
4. *False Positive vs False Negative pada Mobil Otonom:*
   - False Positive: Sensor mengira ada pejalan kaki padahal jalanan kosong (misal bayangan daun). Konsekuensinya mobil melakukan pengereman mendadak yang mengagetkan penumpang, namun tidak merenggut korban jiwa.
   - False Negative: Ada pejalan kaki nyata yang menyeberang, namun sistem salah memprediksi bahwa jalanan kosong. Konsekuensinya mobil melaju kencang tanpa mengerem dan menabrak korban hingga tewas. Oleh karena itu, False Negative membawa risiko kemanusiaan yang mutlak jauh lebih fatal dan nilai Recall pendeteksian manusia wajib dioptimalkan mendekati 100%.
5. *Overfitting vs Underfitting:*
   - Underfitting terjadi saat model terlalu sederhana sehingga tidak mampu menangkap pola dasar data baik pada data latih maupun data uji (akurasi rendah di kedua dataset).
   - Overfitting terjadi saat model terlalu kompleks dan menghafal detail derau (*noise*) data latih. Ciri-cirinya: akurasi data latih sangat tinggi (~99%), namun saat diuji pada data uji performanya anjlok drastis (~60%).
   - Cara mengatasi overfitting pada Decision Tree: Menerapkan pemangkasan cabang (*Pruning*), membatasi kedalaman maksimum pohon keputusan (`max_depth`), serta menetapkan batas minimum sampel daun (`min_samples_leaf`).
"""
