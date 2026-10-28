"""
Modul Naskah Bab III Kelas XII SMA/SMK (Fase F Akhir)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB3_SMA12 = """# BAB III: PENGEMBANGAN MODEL AI LANJUT DAN FONDASI DEEP LEARNING

## APERSEPSI: MENGAPA MODEL SEDERHANA GAGAL MENGENALI PENYAKIT PADI?

Sore itu di laboratorium kecerdasan artifisial sekolah, Arya dan Dinda sedang memperhatikan layar monitor yang memuat hasil evaluasi model Machine Learning konvensional (Decision Tree dan SVM). Model tersebut dilatih untuk mendeteksi penyakit hawar daun bakteri pada tanaman padi petani di Minahasa berdasarkan 500 foto daun beresolusi tinggi. Bagas melangkah masuk membawa segelas air, melihat wajah kedua rekannya yang tampak serius.

[GAMBAR: assets/bab3_komik_pembuka_sma12.png]

"Ada kabar apa dari model deteksi tanaman kita, Arya?" tanya Bagas penasaran. "Apakah akurasinya sudah melampaui 90 persen?"

Arya menghela napas seraya menggelengkan kepala. "Akurasi pengujian model SVM kita mentok di angka 58 persen, Bagas. Ketika foto daun diambil di luar ruangan dengan sudut kemiringan berbeda, latar belakang tanah yang basah, atau intensitas cahaya matahari yang berubah, model kita langsung terkecoh dan salah mengklasifikasikan daun yang sakit sebagai daun sehat!"

Dinda menunjuk pada alur pipa pemrosesan fitur di papan tulis. "Masalahnya terletak pada **rekayasa fitur manual (*handcrafted feature engineering*)**, kawan. Pada Machine Learning tradisional, kitalah manusia yang harus merumuskan rumus matematika untuk mengekstrak warna hijau, tekstur bercak, atau batas tepi daun. Begitu daun terkena bayangan awan atau debu, ekstraksi fitur manual kita langsung hancur. Kita membutuhkan arsitektur komputasi yang mampu memelajari hierarki fitur visual secara otomatis dari level piksel terendah hingga bentuk utuh!"

"Itu adalah keunggulan mutlak dari **Pembelajaran Mendalam (*Deep Learning*)**, khususnya arsitektur **Convolutional Neural Network (CNN)**!" sambung Arya penuh antusias. "CNN memiliki filter konvolusi otomatis yang meniru cara kerja korteks visual mata makhluk hidup. Lapisan awal mengekstrak garis tepi (*edges*), lapisan tengah merangkai tekstur dan pola bercak, dan lapisan akhir mengenali jenis penyakit daun secara presisi!"

"Namun melatih model CNN raksasa dari nol membutuhkan jutaan foto dan komputer super yang sangat mahal, bukan?" tanya Bagas cemas.

"Tentu saja!" sahut Dinda tersenyum. "Tetapi kita tidak perlu melatihnya dari nol! Kita dapat memanfaatkan paradigma cerdas **Transfer Learning** menggunakan arsitektur model terlatih seperti **MobileNet** atau **ResNet**, lalu menyesuaikan (*fine-tuning*) beberapa lapisan akhirnya saja untuk dataset daun padi kita. Metode ini tidak hanya sangat akurat dan cepat, tetapi juga hemat energi—sebuah komitmen nyata pada prinsip **Green AI (*Kecerdasan Artifisial Ramah Lingkungan*)**!"

"Luar biasa!" seru Bagas. "Mari kita bedah arsitektur jaringan saraf tiruan, matematika konvolusi CNN, dan keajaiban Transfer Learning!"

---

## A. EVOLUSI PARADIGMA: DARI MACHINE LEARNING MENUJU JARINGAN SARAF TIRUAN (ANN)

Dalam perjalanan ilmu kecerdasan artifisial, transisi dari Machine Learning konvensional menuju Deep Learning dipicu oleh keterbatasan mendasar algoritma klasik dalam mengolah data berdimensi tinggi (*high-dimensional unstructured data*) seperti citra digital, rekaman suara, dan teks bahasa alami.

### 1. Keterbatasan Ekstraksi Fitur Manual
Pada Machine Learning tradisional, alur kerja selalu diawali dengan tahap perancangan fitur manual oleh manusia (*feature engineering*). Pada citra digital berukuran 1000 x 1000 piksel RGB, terdapat 3.000.000 nilai intensitas warna. Jika nilai-nilai piksel mentah ini langsung dimasukkan ke algoritma regresi atau pohon keputusan tanpa pemahaman spasial, algoritma akan mengalami fenomena **Kutukan Dimensi (*Curse of Dimensionality*)** dan gagal total memahami relasi bentuk objek.

### 2. Konsep Dasar Neuron Tiruan (Perceptron)
Jaringan Saraf Tiruan (*Artificial Neural Network* / ANN) terinspirasi dari struktur sel saraf biologis (neuron) di otak manusia. Unit pemrosesan terkecil dalam ANN disebut **Perceptron**, yang diperkenalkan oleh Frank Rosenblatt pada tahun 1958.

Sebuah neuron buatan menerima sejumlah sinyal masukan berbobot, menambahkan nilai bias, lalu melewatkan total akumulasi ke fungsi aktivasi non-linear untuk menghasilkan keluaran:

```text
z = (x1 * w1) + (x2 * w2) + ... + (xn * wn) + b
y = f(z)
```

Di mana:
- `x1, x2, ..., xn` adalah nilai fitur masukan (*input values*).
- `w1, w2, ..., wn` adalah bobot keterhubungan (*weights*), yang merepresentasikan kekuatan sinyal koneksi sinapsis antar-neuron.
- `b` adalah nilai bias (*bias*), yang memungkinkan fungsi aktivasi bergeser secara fleksibel untuk menyesuaikan data.
- `f(z)` adalah fungsi aktivasi (*activation function*).

### 3. Ragam Fungsi Aktivasi Non-Linear
Tanpa fungsi aktivasi non-linear, berapapun banyaknya lapisan neuron yang ditumpuk, jaringan saraf hanya akan setara dengan sebuah operasi regresi linier sederhana. Ragam fungsi aktivasi esensial meliputi:

1. **Rectified Linear Unit (ReLU):**
Fungsi aktivasi paling dominan pada lapisan tersembunyi (*hidden layers*) Deep Learning modern:
```text
f(z) = max(0, z)
```
Jika nilai z negatif, keluaran bernilai 0. Jika z positif, keluaran sama dengan nilai z. Keunggulan mutlak ReLU adalah komputasinya yang sangat cepat serta mampu mengatasi masalah **Lenyapnya Gradien (*Vanishing Gradient Problem*)** saat algoritma perambatan balik (*Backpropagation*) dijalankan.

2. **Sigmoid:**
Mengubah nilai bilangan riil menjadi rentang probabilitas antara 0 dan 1:
```text
f(z) = 1 / (1 + e^(-z))
```
Sangat umum digunakan pada lapisan keluaran (*output layer*) untuk klasifikasi biner (dua kelas).

3. **Softmax:**
Generalisasi dari fungsi Sigmoid untuk klasifikasi multi-kelas (*multi-class classification*). Fungsi Softmax mengubah larik nilai skor akhir menjadi distribusi probabilitas probabilitas di mana jumlah total probabilitas seluruh kelas tepat sama dengan 1,0 (100%).

---

## B. ARSITEKTUR CONVOLUTIONAL NEURAL NETWORK (CNN)

Untuk memproses data citra digital secara efisien tanpa kehilangan informasi hubungan ketetanggaan spasial antar-piksel (*spatial locality*), para ilmuwan komputer mengembangkan arsitektur **Convolutional Neural Network (CNN)**.

[GAMBAR: assets/bab3_diagram_arsitektur_cnn_deep_learning.png]

Arsitektur CNN standar tersusun atas tiga lapisan inti yang bekerja secara terkoordinasi:

### 1. Lapisan Konvolusi (Convolutional Layer)
Lapisan konvolusi adalah jantung utama pengekstraksi fitur visual. Lapisan ini menggunakan matriks kecil berukuran ganjil (seperti matriks kernel filter berukuran 3x3 piksel) yang digeserkan (*sliding window*) melintasi seluruh matriks citra masukan.

Pada setiap langkah pergeseran, dilakukan operasi perkalian titik (*dot product*) elemen-per-elemen antara nilai kernel dan piksel citra lokal, lalu seluruh hasilnya dijumlahkan untuk menghasilkan satu nilai pada **Peta Fitur (*Feature Map*)**.
- **Filter Lapisan Awal:** Mendeteksi fitur sederhana berfrekuensi tinggi seperti tepi garis horizontal, garis vertikal, dan perubahan kontras warna.
- **Filter Lapisan Lanjutan:** Menggabungkan fitur sederhana untuk mengenali pola geometris, tekstur lengkung, lingkaran, hingga bentuk utuh organ objek (seperti mata, daun, atau roda).

Dua hiperparameter penting dalam operasi konvolusi:
- **Stride:** Besaran langkah pergeseran kernel piksel per piksel (biasanya bernilai 1 atau 2).
- **Padding:** Penambahan baris dan kolom berisi angka nol (*Zero Padding*) di sekeliling batas tepi citra masukan agar dimensi peta fitur keluaran tidak menyusut drastis.

### 2. Lapisan Penggabungan (Pooling Layer)
Pooling bertugas mereduksi dimensi ukuran spasial (lebar dan tinggi) peta fitur secara progresif, tanpa mengubah kedalaman (*channel*). Manfaat operasi pooling:
- Mengurangi jumlah parameter bobot komputasi sehingga pelatihan model menjadi jauh lebih cepat dan hemat memori RAM.
- Mencegah fenomena kejenuhan hafalan (*Overfitting*).
- Menghasilkan sifat **Ketahanan Translasi (*Translation Invariance*)**, artinya jika objek dalam foto bergeser sedikit ke kiri atau ke kanan, model tetap mampu mengenalinya dengan benar.

Jenis pooling yang paling umum adalah **Max Pooling 2x2 dengan Stride 2**, di mana matriks peta fitur dibagi menjadi kotak-kotak berukuran 2x2 piksel, dan hanya nilai piksel tertinggi (*maksimum*) di dalam setiap kotak yang diambil, memangkas 75% ukuran spasial matriks.

### 3. Lapisan Terhubung Penuh (Fully Connected / Dense Layer)
Setelah citra melewati serangkaian lapisan konvolusi dan pooling bergantian, peta fitur dua dimensi yang tersisa diratakan (*Flattening*) menjadi sebuah vektor satu dimensi berderet panjang. Vektor ini kemudian dihubungkan ke jaringan saraf tiruan standar (*Dense Layer*) untuk memetakan kombinasi fitur visual tingkat tinggi ke probabilitas kelas keluaran menggunakan fungsi aktivasi Softmax.

---

## C. STRATEGI TRANSFER LEARNING DAN PENYESUAIAN AKHIR (FINE-TUNING)

Melatih arsitektur model CNN berkapasitas besar dari nol (*from scratch*) menuntut ketersediaan ratusan ribu hingga jutaan citra teranotasi rapi, serta kluster kartu grafis (GPU) berdaya ribuan Watt yang memakan biaya sangat mahal dan waktu pelatihan berminggu-minggu.

Bagi pelajar dan pengembang perangkat lunak praktis, solusi cerdas yang menjadi standar industri global adalah **Transfer Pembelajaran (*Transfer Learning*)**.

### 1. Prinsip Kerja Transfer Learning
Transfer Learning memanfaatkan bobot pengetahuan (*pre-trained weights*) dari model raksasa yang telah dilatih oleh laboratorium kelas dunia (seperti Google atau universitas riset) menggunakan dataset berskala kolosal seperti **ImageNet** (berisi lebih dari 14 juta gambar terbagi ke dalam 1.000 kelas objek).

Karena model terlatih tersebut telah menguasai cara mengekstrak fitur visual universal dunia (garis tepi, tekstur, pencahayaan, bayangan), kita dapat memanfaatkan fondasi pengekstraksi fiturnya (*base feature extractor*) dan hanya melatih ulang beberapa lapisan klasifikasi paling atas untuk tugas spesifik kita.

### 2. Ragam Arsitektur Model Terlatih Populer
1. **MobileNet (MobileNetV2 / MobileNetV3):** Dirancang khusus oleh Google untuk perangkat dengan sumber daya terbatas (ponsel pintar dan mikrokontroler Edge AI) menggunakan teknik konvolusi terpisah mendalam (*Depthwise Separable Convolution*). Ukuran model sangat ringkas (kurang dari 20 MB) namun memiliki akurasi yang luar biasa tinggi.
2. **ResNet (ResNet50 / ResNet101):** Memperkenalkan konsep koneksi residual pintas (*Skip Connections / Residual Blocks*) yang memungkinkan jaringan saraf dilatih hingga ratusan lapisan kedalaman tanpa mengalami degradasi gradien.

### 3. Tahapan Implementasi Transfer Learning
- **Tahap 1: Pembekuan Lapisan Dasar (*Freezing*):** Lapisan konvolusi dasar model terlatih dibekukan bobotnya (*trainable = False*) agar representasi visual universal yang telah dipelajari tidak rusak.
- **Tahap 2: Penggantian Lapisan Kepala (*Head Replacement*):** Menghapus lapisan klasifikasi 1.000 kelas ImageNet bawaan, lalu menggantinya dengan lapisan Dense baru yang disesuaikan dengan jumlah kelas proyek kita (misal: 3 kelas penyakit daun padi).
- **Tahap 3: Pelatihan Cepat Lapisan Kepala:** Melatih hanya bobot pada lapisan Dense baru selama beberapa epoch awal.
- **Tahap 4: Penyesuaian Halus (*Fine-Tuning* - Opsional):** Membuka sebagian kecil lapisan konvolusi paling atas, lalu melatihnya kembali secara bersama-sama dengan laju pembelajaran (*learning rate*) yang sangat kecil (misal: 0.00001) untuk mengadaptasi filter visual secara presisi pada karakteristik dataset lokal.

---

## D. INTEGRASI CLOUD AI API DAN KESADARAN GREEN AI

Selain melatih model secara lokal, pengembang modern kerap mengintegrasikan kemampuan model kecerdasan artifisial raksasa yang disediakan oleh penyedia layanan awan melalui **Application Programming Interface (Cloud AI API)**.

### 1. Memanggil Layanan Cloud AI API via HTTP REST
Penyedia layanan awan (seperti Google Cloud Vision, Azure Cognitive Services, atau OpenAI) menyediakan titik akhir (*endpoint*) API yang dapat dipanggil menggunakan skrip Python sederhana:

```python
import requests
import json

# Menyiapkan titik akhir peladen dan kunci otentikasi API
url_endpoint = "https://api.layanan-ai.com/v1/vision/analyze"
headers = {
    "Authorization": "Bearer KUNCI_RAHASIA_API_ANDA",
    "Content-Type": "application/json"
}

# Payload data citra yang akan dianalisis
data_payload = {
    "image_url": "https://server-sekolah.id/foto_daun_padi.jpg",
    "features": ["LABEL_DETECTION", "OBJECT_LOCALIZATION"]
}

# Mengirimkan permintaan POST ke peladen awan
response = requests.post(url_endpoint, headers=headers, json=data_payload)

if response.status_code == 200:
    hasil = response.json()
    print("Hasil Prediksi AI Awan:")
    print(json.dumps(hasil, indent=2))
else:
    print(f"Terjadi kesalahan komunikasi API. Kode status: {response.status_code}")
```

### 2. Gerakan Green AI (Kecerdasan Artifisial Ramah Lingkungan)
Pelatihan model Deep Learning berparameter ratusan miliar menghasilkan jejak karbon (*carbon footprint*) yang sangat masif akibat konsumsi listrik raksasa di pusat data peladen dunia. Paradigma **Green AI** menyerukan komunitas pengembang kecerdasan artifisial untuk:
1. Mengutamakan efisiensi komputasi dan kesederhanaan arsitektur di atas pengejaran margin akurasi 0,1% yang membutuhkan daya listrik berlipat ganda (*Red AI*).
2. Memprioritaskan penggunaan Transfer Learning dan teknik pemangkasan bobot model (*Model Pruning and Quantization*) agar model dapat berjalan di perangkat berdaya rendah.
3. Memilih pusat data awan yang beroperasi menggunakan 100% energi terbarukan (tenaga surya, angin, atau hidroelektrik).

---

## E. LKPD 3.1: LABORATORIUM PELATIHAN MODEL KLASIFIKASI CITRA TRANSFER LEARNING

Pada aktivitas laboratorium ini, kalian akan melatih model klasifikasi citra daun tanaman menggunakan arsitektur MobileNetV2 dan pustaka TensorFlow/Keras.

### 1. Alat dan Bahan
- Perangkat komputer dengan koneksi internet aktif.
- Lingkungan kerja Google Colaboratory (dengan akselerator GPU T4 gratis diaktifkan).
- Pustaka: `tensorflow`, `numpy`, `matplotlib`.

### 2. Kode Program Pelatihan Transfer Learning MobileNetV2

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

# 1. Menentukan parameter dimensi citra dan batch size
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 3  # Misal: Sehat, Hawar Bakteri, Bercak Cokelat

# 2. Mengunduh basis model terlatih MobileNetV2 (tanpa lapisan kepala klasifikasi)
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# 3. Membekukan seluruh bobot lapisan pengekstraksi fitur dasar
base_model.trainable = False

# 4. Merangkai arsitektur model lengkap dengan lapisan kepala baru
model = models.Sequential([
    layers.Input(shape=(224, 224, 3)),
    # Prapemrosesan normalisasi nilai piksel khusus MobileNet (-1 hingga 1)
    tf.keras.applications.mobilenet_v2.preprocess_input,
    # Basis pengekstraksi fitur MobileNetV2
    base_model,
    # Lapisan Global Average Pooling untuk mereduksi matriks 7x7 menjadi vektor
    layers.GlobalAveragePooling2D(),
    # Lapisan Dropout untuk mencegah overfitting hafalan
    layers.Dropout(0.2),
    # Lapisan keluaran klasifikasi dengan fungsi aktivasi Softmax
    layers.Dense(NUM_CLASSES, activation='softmax')
])

# 5. Mengompilasi model dengan optimizer Adam dan fungsi rugi Categorical Crossentropy
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Menampilkan ringkasan arsitektur model
model.summary()

print("\\nModel Transfer Learning berhasil dikonfigurasi dan siap dilatih!")
```

### 3. Tugas Praktikum dan Refleksi Siswa
1. Berdasarkan keluaran `model.summary()`, amati berapakah total parameter bobot model, dan berapa persen parameter yang terdaftar sebagai *Non-trainable params* (bobot yang dibekukan)!
2. Jelaskan fungsi dari lapisan `layers.Dropout(0.2)` dalam mencegah fenomena overfitting!
3. Jika model kalian nantinya akan diunggah ke mikrokontroler ESP32-CAM yang bertenaga baterai di kebun sekolah, mengapa arsitektur MobileNetV2 jauh lebih disarankan dibanding arsitektur ResNet152?

---

## F. RANGKUMAN MATERI BAB III

1. **Deep Learning** memecahkan keterbatasan Machine Learning konvensional dengan mengeliminasi tahapan rekayasa fitur manual melalui kemampuan memelajari hierarki representasi representasi fitur visual secara mandiri langsung dari data mentah.
2. Komponen fundamental **Jaringan Saraf Tiruan (ANN)** adalah **Perceptron**, yang mengkombinasikan jumlahan berbobot masukan, nilai bias, dan **Fungsi Aktivasi Non-Linear** seperti **ReLU** (pada lapisan tersembunyi), **Sigmoid** (klasifikasi biner), dan **Softmax** (distribusi probabilitas klasifikasi multi-kelas).
3. **Convolutional Neural Network (CNN)** dirancang khusus untuk memproses data berstruktur grid spasial seperti citra, terdiri atas:
   - **Convolutional Layer:** Mengoperasikan kernel filter geser untuk menghasilkan peta fitur (*Feature Map*).
   - **Pooling Layer (Max Pooling):** Mereduksi ukuran matriks spasial untuk memangkas beban komputasi dan menciptakan ketahanan translasi.
   - **Fully Connected Layer:** Menghubungkan fitur spasial terintegrasi menuju simpul klasifikasi probabilitas akhir.
4. **Transfer Learning** memungkinkan pemanfaatan bobot model industri terlatih raksasa (seperti MobileNet atau ResNet) pada dataset lokal terbatas dengan cara membekukan lapisan dasar pengekstraksi fitur dan melatih lapisan klasifikasi baru, menghemat waktu dan biaya komputasi secara dramatis.
5. Prinsip **Green AI** mengajak pengembang untuk menyeimbangkan performa akurasi sistem dengan efisiensi energi komputasi guna menekan emisi jejak karbon peladen dunia demi keberlanjutan kelestarian lingkungan bumi.

---

## G. UJI KOMPETENSI BAB III

### Bagian 1: Pilihan Ganda (10 Soal Berbobot HOTS)

1. Perhatikan skenario berikut: Sebuah model Machine Learning konvensional yang dilatih mengenali foto buah mangga mengalami penurunan akurasi drastis ketika posisi buah mangga di dalam foto digeser ke sudut kanan bawah atau terkena bayangan dedaunan. Penyebab utama kelemahan model tersebut adalah...
A. Komputer kekurangan daya baterai saat proses inferensi.  
B. Algoritma konvensional bergantung pada fitur manual dan tidak memiliki sifat ketahanan spasial (*spatial invariance*).  
C. Model Machine Learning konvensional selalu berjalan pada resolusi 1 piksel saja.  
D. Bahasa pemrograman Python tidak mampu memproses warna hijau.  
E. Sensor kamera mengalami kerusakan optik permanen.  

2. Sebuah neuron buatan memiliki tiga masukan: x1 = 2, x2 = 1, x3 = 3 dengan bobot masing-masing w1 = 0,5, w2 = -1, w3 = 2, serta nilai bias b = -4. Jika fungsi aktivasi yang digunakan adalah ReLU f(z) = max(0, z), maka nilai keluaran y dari neuron tersebut adalah...
A. -2  
B. 0  
C. 2  
D. 6  
E. 10  

3. Mengapa fungsi aktivasi ReLU (*Rectified Linear Unit*) jauh lebih populer digunakan pada lapisan tersembunyi (*hidden layers*) jaringan saraf tiruan mendalam dibanding fungsi Sigmoid?
A. ReLU menghasilkan nilai keluaran berupa teks alfabet.  
B. ReLU mampu mengatasi masalah lenyapnya gradien (*Vanishing Gradient Problem*) dan memiliki komputasi gradien yang sangat sederhana dan cepat.  
C. ReLU secara otomatis menghapus seluruh piksel gambar yang berwarna gelap.  
D. Sigmoid hanya dapat dijalankan pada perangkat keras buatan Apple.  
E. ReLU mengubah model deep learning menjadi sistem pakar berbasis aturan.  

4. Sebuah citra abu-abu berdimensi 28 x 28 piksel diproses oleh lapisan konvolusi dengan kernel filter berukuran 5 x 5 piksel, nilai langkah (*stride*) = 1, dan tanpa penambahan batas nol (*valid padding / no padding*). Berapakah dimensi matriks Peta Fitur (*Feature Map*) keluaran yang dihasilkan?
A. 28 x 28 piksel  
B. 24 x 24 piksel  
C. 20 x 20 piksel  
D. 14 x 14 piksel  
E. 5 x 5 piksel  

5. Perhatikan matriks peta fitur 4 x 4 berikut:
```text
[ 12   8  |  15  22 ]
[  4  19  |   7  11 ]
---------------------
[  9   3  |  30  14 ]
[ 16   2  |   8  25 ]
```
Jika terhadap matriks di atas diterapkan operasi **Max Pooling 2x2 dengan Stride 2**, matriks hasil reduksi berukuran 2x2 yang tepat adalah...
A. 
[ 12  22 ]
[ 16  30 ]
B. 
[ 19  22 ]
[ 16  30 ]
C. 
[ 19  15 ]
[  9  25 ]
D. 
[  4   7 ]
[  2   8 ]
E. 
[ 43  55 ]
[ 30  77 ]

6. Mengapa operasi Max Pooling sangat krusial disisipkan di antara lapisan-lapisan konvolusi pada arsitektur CNN?
A. Untuk menambah resolusi gambar menjadi format 8K Ultra High Definition.  
B. Untuk mereduksi jumlah dimensi komputasi matriks serta memberikan ketahanan translasi (*translation invariance*) terhadap pergeseran posisi objek.  
C. Untuk mengubah citra berwarna RGB menjadi berkas audio MP3.  
D. Untuk menghapus lapisan konvolusi sebelumnya secara permanen.  
E. Untuk menghentikan proses perambatan balik (*backpropagation*).  

7. Pada arsitektur klasifikasi citra multi-kelas (misal membedakan antara kucing, anjing, dan kelinci), lapisan keluaran (*output layer*) menggunakan fungsi aktivasi Softmax. Karakteristik utama dari keluaran fungsi Softmax adalah...
A. Mengubah seluruh nilai masukan menjadi bilangan bulat genap.  
B. Seluruh probabilitas keluaran bernilai negatif di bawah nol.  
C. Menghasilkan vektor probabilitas untuk setiap kelas di mana jumlah total probabilitas seluruh kelas tepat sama dengan 1,0 (100%).  
D. Mengembalikan hanya satu nilai skalar berupa rata-rata deviasi standar.  
E. Menolak data masukan yang memiliki resolusi di bawah 1 Megapiksel.  

8. Perhatikan tabel perbandingan strategi pelatihan model Deep Learning berikut:
- Strategi X: Menginisialisasi seluruh bobot secara acak, membutuhkan 500.000 citra, memakan waktu 12 hari pelatihan di peladen multi-GPU.
- Strategi Y: Mengunduh bobot MobileNetV2 yang telah terlatih pada ImageNet, membekukan lapisan dasar, hanya melatih lapisan Dense baru dengan 1.200 citra daun lokal selama 25 menit di Google Colab.
Strategi Y merepresentasikan penerapan paradigma...
A. Genetic Algorithm  
B. Unsupervised K-Means  
C. Transfer Learning  
D. Reinforcement Q-Learning  
E. Decision Tree Pruning  

9. Arya mengamati bahwa model klasifikasi citra yang ia latih memperoleh nilai akurasi 99,8% pada data latih (*training set*), namun saat diuji dengan data baru yang belum pernah dilihat (*validation set*), akurasinya anjlok drastis ke angka 61,2%. Fenomena kegagalan generalisasi model ini disebut...
A. Underfitting  
B. Overfitting  
C. Konvergensi Sempurna  
D. Vanishing Gradient  
E. Multicollinearity  

10. Paradigma **Green AI** mengajarkan para pengembang sistem cerdas untuk tidak hanya mengejar metrik akurasi tertinggi semata, melainkan juga mempertimbangkan faktor...
A. Kecepatan mengetik kode program di papan ketik.  
B. Jumlah baris komentar yang ditulis dalam skrip Python.  
C. Jejak emisi karbon dan efisiensi konsumsi energi listrik perangkat keras komputasi selama siklus pelatihan dan inferensi.  
D. Penggunaan warna tema hijau pada tampilan antarmuka dasbor.  
E. Ketebalan lapisan casing pelindung komputer.  

---

### Bagian 2: Uraian dan Pemecahan Masalah Sistemik (5 Soal)

1. Jelaskan secara matematis dan konseptual struktur sebuah **Neuron Buatan (Perceptron)**! Apa peran esensial dari nilai **Bobot (*Weights*)** dan **Bias** dalam memelajari representasi data?

2. Jelaskan fungsi dan cara kerja dari tiga lapisan utama pada arsitektur **Convolutional Neural Network (CNN)**: Lapisan Konvolusi (*Convolutional Layer*), Lapisan Penggabungan (*Pooling Layer*), dan Lapisan Terhubung Penuh (*Fully Connected Layer*)!

3. Sebuah tim pengembang di sekolah kalian ingin membuat aplikasi cerdas pendeteksi kematangan buah kopi lokal berbasis ponsel pintar Android. Mengapa tim kalian lebih disarankan menggunakan teknik **Transfer Learning** berbasis **MobileNetV2** dibanding melatih model arsitektur CNN raksasa dari nol? Uraikan 3 alasan teknisnya!

4. Jelaskan apa yang dimaksud dengan fenomena **Lenyapnya Gradien (*Vanishing Gradient Problem*)** pada jaringan saraf tiruan mendalam, dan bagaimana fungsi aktivasi **ReLU** berhasil memecahkan permasalahan kritis tersebut!

5. Mengapa gerakan **Green AI (Kecerdasan Artifisial Ramah Lingkungan)** menjadi agenda moral dan etika yang sangat mendesak bagi komunitas teknologi global saat ini? Berikan 2 contoh konkret tindakan yang dapat dilakukan pengembang muda untuk mendukung Green AI!

---

### KUNCI JAWABAN DAN PEMBAHASAN LENGKAP BAB III

#### Kunci Jawaban Pilihan Ganda:
1. **B (Algoritma konvensional bergantung pada fitur manual dan tidak memiliki sifat ketahanan spasial)** — Model ML tradisional mengandalkan ekstraksi fitur manual yang rapuh terhadap variasi sudut, bayangan, dan pergeseran spasial objek.
2. **C (2)** — Perhitungan z = (2 * 0,5) + (1 * -1) + (3 * 2) + (-4) = 1 - 1 + 6 - 4 = 2. Karena z = 2 (positif), maka f(z) = max(0, 2) = 2.
3. **B (ReLU mampu mengatasi masalah lenyapnya gradien dan memiliki komputasi gradien yang sangat sederhana dan cepat)** — Gradien ReLU bernilai konstan 1 untuk daerah positif sehingga sinyal perambatan balik tidak menyusut ke nol pada jaringan saraf berlapis banyak.
4. **B (24 x 24 piksel)** — Rumus dimensi keluaran konvolusi tanpa padding: W_out = (W_in - Kernel + 2*Padding)/Stride + 1 = (28 - 5 + 0)/1 + 1 = 23 + 1 = 24.
5. **B ([19, 22], [16, 30])** — Kuadran kiri atas: max(12, 8, 4, 19) = 19; kuadran kanan atas: max(15, 22, 7, 11) = 22; kuadran kiri bawah: max(9, 3, 16, 2) = 16; kuadran kanan bawah: max(30, 14, 8, 25) = 30.
6. **B (Untuk mereduksi jumlah dimensi komputasi matriks serta memberikan ketahanan translasi)** — Max Pooling memadatkan fitur paling signifikan dan membuat deteksi kebal terhadap pergeseran minor piksel.
7. **C (Menghasilkan vektor probabilitas untuk setiap kelas di mana jumlah total probabilitas seluruh kelas tepat sama dengan 1,0)** — Softmax menormalkan bilangan eksponensial riil menjadi distribusi probabilitas komparatif multi-kelas.
8. **C (Transfer Learning)** — Pemanfaatan arsitektur dan bobot terlatih dari dataset skala besar untuk diterapkan pada dataset baru yang lebih kecil adalah definisi baku Transfer Learning.
9. **B (Overfitting)** — Fenomena ketika model menghafal detail dan derau data latih secara berlebihan sehingga gagal melakukan inferensi akurat pada data baru (*validation/test set*).
10. **C (Jejak emisi karbon dan efisiensi konsumsi energi listrik perangkat keras komputasi)** — Green AI berfokus pada keberlanjutan ekologis dengan meminimalkan jejak karbon pemrosesan kecerdasan artifisial.

#### Pembahasan Soal Uraian:
1. **Struktur Neuron Buatan (Perceptron):**
   - Neuron menerima input bervektor x = [x1, x2, ..., xn].
   - *Bobot (Weights):* Menentukan signifikansi atau kontribusi relatif masing-masing fitur masukan terhadap keputusan neuron. Nilai bobot dioptimasi selama proses pelatihan.
   - *Bias:* Konstanta independen yang memungkinkan batas keputusan bergeser ke kiri atau kanan agar fungsi aktivasi dapat memetakan data yang tidak berpusat di titik origin (0,0).
   - *Keluaran:* Ditentukan oleh fungsi aktivasi f(sum(xi * wi) + b) untuk memperkenalkan sifat non-linearitas.
2. **Tiga Lapisan Utama CNN:**
   - *Lapisan Konvolusi:* Melakukan filtering matriks spasial menggunakan kernel filter geser untuk mengekstrak peta fitur hierarkis visual (tepi, sudut, tekstur).
   - *Lapisan Pooling:* Memangkas resolusi spasial peta fitur (misal dengan Max Pooling 2x2) guna mereduksi beban komputasi dan memberikan invariansi posisi objek.
   - *Lapisan Fully Connected (Dense):* Meratakan peta fitur menjadi vektor 1D dan mengintegrasikan seluruh fitur visual untuk memprediksi probabilitas label kelas menggunakan fungsi Softmax.
3. **Keunggulan Transfer Learning MobileNetV2 untuk Ponsel Pintar:**
   - *Efisiensi Ukuran & Memori:* MobileNetV2 menggunakan Depthwise Separable Convolution yang memangkas parameter bobot hingga 80-90% dibanding CNN standar, menjadikannya sangat ringan (kurang dari 20 MB).
   - *Kecepatan Inferensi Nyata:* Mampu mengeksekusi prediksi dalam hitungan milidetik langsung pada CPU/NPU ponsel tanpa latensi jaringan internet.
   - *Kebutuhan Data Latih Minimal:* Karena telah menguasai fitur visual dari ImageNet, model hanya membutuhkan beberapa ratus foto daun kopi lokal untuk mencapai akurasi tinggi.
4. **Vanishing Gradient Problem dan Solusi ReLU:**
   - Pada fungsi Sigmoid, turunan matematis maksimalnya hanya 0,25. Ketika jaringan saraf memiliki puluhan lapisan, perkalian turunan berantai (*chain rule*) pada perambatan balik menyebabkan nilai gradien mengecil secara eksponensial mendekati nol di lapisan-lapisan awal, sehingga bobot berhenti belajar.
   - *Solusi ReLU:* Turunan dari ReLU bernilai konstan 1 untuk semua nilai masukan positif (z > 0). Akibatnya, gradien dapat mengalir deras tanpa mengalami penyusutan berapapun dalamnya lapisan jaringan saraf.
5. **Urgensi Green AI dan Contoh Tindakan Nyata:**
   - *Urgensi:* Pelatihan satu model AI skala raksasa dapat melepaskan ratusan ton gas karbon dioksida ke atmosfer. Green AI mendesak transformasi agar kecerdasan artifisial tidak memperparah krisis perubahan iklim global.
   - *2 Contoh Tindakan Nyata:*
     1. Menerapkan teknik Transfer Learning dan pemangkasan model (*Quantization* / INT8) agar model dapat beroperasi pada perangkat tepi berdaya rendah (baterai) tanpa memerlukan server awan bertenaga tinggi.
     2. Mematikan peladen komputasi GPU awan secara terjadwal setelah proses pelatihan selesai dan memilih penyedia komputasi awan yang memanfaatkan sumber daya listrik energi terbarukan.
"""
