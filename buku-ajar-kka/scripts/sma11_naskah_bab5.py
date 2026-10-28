"""
Modul Naskah Bab V Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB5_SMA11 = """# BAB V: FONDASI PEMROSESAN BAHASA ALAMI (NATURAL LANGUAGE PROCESSING - NLP)

## APERSEPSI: MENGAPA KOMPUTER KESULITAN MEMAHAMI SARKASME?

Di ruang laboratorium komputer sekolah, Bagas tampak sedang mengerutkan kening di depan layar laptopnya. Ia sedang menguji coba prototipe program analisis sentimen sederhana yang dirancangnya untuk memilah ulasan publik terhadap fasilitas kantin sekolah. Program tersebut bekerja dengan cara mencocokkan kata kunci: jika ada kata "enak" atau "hebat", program otomatis memberi label Positif.

[GAMBAR: assets/bab5_komik_pembuka_sma11.png]

"Dinda, Arya, lihat hasil analisis programku ini!" panggil Bagas seraya menunjuk salah satu baris ulasan di layar. "Seorang siswa menulis ulasan: *'Wah, hebat sekali ya kantin kita, nasi gorengnya dingin dan ada bonus semutnya!'*. Programku dengan bangga memberi label ulasan tersebut sebagai **Sentimen Positif Bintang Lima** hanya karena mendeteksi kata 'hebat'!"

Dinda tertawa kecil seraya menggelengkan kepala. "Tentu saja, Bagas. Program pencocokan kata kuncimu belum memahami konteks dan nuansa emosional bahasa manusia. Kalimat tersebut adalah sarkasme murni yang bermakna kekecewaan mendalam!"

Arya menambahkan, "Bahasa manusia (*Natural Language*) adalah sistem komunikasi paling kompleks di muka bumi. Bahasa sarat dengan metafora, peribahasa, imbuhan kata yang rumit, dan konteks antar-kata yang saling terkait erat. Komputer pada dasarnya adalah mesin hitung kalkulator yang hanya memahami angka biner 0 dan 1, bukan makna rasa di balik kata-kata."

"Lalu, bagaimana para ilmuwan kecerdasan artifisial modern membuat model bahasa besar (*Large Language Models*) seperti ChatGPT atau Gemini mampu diajak berdiskusi secara luwes layaknya manusia?" tanya Bagas penasaran.

Dinda membuka buku catatannya. "Kuncinya ada pada bidang ilmu **Pemrosesan Bahasa Alami (*Natural Language Processing* / NLP)**. Teks mentah manusia harus melalui serangkaian penyaringan pra-pemrosesan: memotong kalimat menjadi kata (*Tokenizing*), membuang kata sambung tak bermakna (*Stopwords*), mencari kata dasar (*Stemming*), lalu mengubah kata menjadi vektor angka bobot informasi (**TF-IDF**). Dan puncaknya, kita akan membedah rahasia arsitektur **Transformer** dengan mekanisme perhatian (*Self-Attention*) yang merevolusi dunia AI modern!"

"Luar biasa!" seru Bagas. "Mari kita pelajari sains komputasi bahasa manusia ini!"

---

## A. KOMPLEKSITAS BAHASA MANUSIA DAN KOMPUTASI LINGUISTIK DIGITAL

Bahasa manusia (*Natural Language*) berkembang secara organik selama ribuan tahun melalui interaksi sosial, budaya, dan emosi. Berbeda dengan bahasa pemrograman komputer (seperti Python atau SQL) yang memiliki aturan tata bahasa yang kaku, deterministik, dan bebas dari ambiguitas, bahasa manusia memiliki karakteristik yang sangat menantang bagi mesin komputasi:

1. **Ambiguitas Semantik (Makna Ganda):**
Sebuah kata yang sama dapat memiliki arti yang sangat berbeda tergantung pada konteks kalimatnya.
*Contoh:* Kata "bisa" dapat bermakna "mampu" (*can*), namun juga dapat bermakna "racun ular" (*venom*). Komputer harus mampu membedakan makna tersebut berdasarkan kata-kata di sekelilingnya.
2. **Kekayaan Imbuhan Bahasa Indonesia (Morfologi Kompleks):**
Bahasa Indonesia memiliki sistem afiksasi (awalan, akhiran, sisipan, dan gabungan) yang sangat kaya. Satu kata dasar "ajar" dapat bertransformasi menjadi *belajar, mengajar, pengajar, pelajaran, terpelajar, diajarkan, mempelajarinya*. Mesin harus mampu mengenali bahwa seluruh kata turunan tersebut memiliki akar makna yang sekeluarga.
3. **Nuansa Emosi, Sarkasme, dan Majas:**
Kalimat manusia sering kali memuat makna tersirat yang berlawanan dengan makna harfiah kata penyusunnya. Ulasan *"Pelayanannya cepat sekali, cuma butuh waktu 3 jam untuk menyajikan segelas air"* menuntut pemahaman ironi yang melampaui perhitungan frekuensi kata biasa.
4. **Bahasa Gaul (Slang), Singkatan, dan Dialek Daerah:**
Di media sosial Indonesia, masyarakat sering menggunakan singkatan informal (misal: *bgt, gpp, mager, kepo*) serta mencampuradukkan bahasa Indonesia dengan kosa kata daerah nusantara.

---

## B. ALUR PRA-PEMROSESAN TEKS (TEXT PREPROCESSING PIPELINE)

Agar teks mentah bahasa manusia dapat diproses oleh algoritma pembelajaran mesin, teks tersebut wajib dibersihkan melalui pipa saluran pra-pemrosesan (*Text Preprocessing Pipeline*) yang terstandarisasi.

[GAMBAR: assets/bab5_diagram_pipeline_nlp_text_processing.png]

Berikut adalah empat tahapan fundamental dalam rekayasa teks digital:

### 1. Case Folding (Penyeragaman Huruf)

Langkah awal untuk menyeragamkan seluruh karakter abjad menjadi huruf kecil (*lowercase*), serta menghapus tanda baca, angka yang tidak relevan, tautan URL, dan karakter khusus.
*Tujuan:* Komputer memperlakukan kata "Koding", "koding", dan "KODING" sebagai satu kata yang identik, bukan tiga entitas yang berbeda.
*Contoh:* `"Siswa-siswa SANGAT Menyukai Koding!"` -> `"siswa-siswa sangat menyukai koding"`

### 2. Tokenizing (Pemotongan Token Kata)

Proses memotong dan memecah untaian teks kalimat panjang menjadi elemen-elemen kata individual yang disebut **Token**.
*Contoh:* `"siswa sangat menyukai koding"` -> `['siswa', 'sangat', 'menyukai', 'koding']`

### 3. Stopwords Removal (Penyaringan Kata Sambung Umum)

Membuang kata-kata fungsional umum yang memiliki frekuensi kemunculan sangat tinggi dalam bahasa sehari-hari namun **tidak membawa bobot informasi unik** terkait topik atau sentimen teks (seperti kata depan dan kata hubung: *dan, di, ke, dari, yang, untuk, pada, ini, itu*).
*Tujuan:* Mengurangi dimensi komputasi secara masif dan memfokuskan model AI hanya pada kata-kata yang bermakna esensial.
*Contoh:* `['buku', 'ini', 'sangat', 'bagus', 'dan', 'menarik']` -> `['buku', 'bagus', 'menarik']` (kata *ini, sangat, dan* dibuang).

### 4. Stemming Bahasa Indonesia (Pencarian Kata Dasar)

Proses morfologis untuk memotong seluruh imbuhan (prefiks, sufiks, konfiks) dari suatu kata berimbuhan guna mengembalikannya ke bentuk **Kata Dasar (*Root Word*)**.
Dalam ekosistem Python di Indonesia, proses ini dieksekusi menggunakan pustaka sumber terbuka populer bernama **Sastrawi** yang mengadopsi algoritma morfologi Nazief-Adriani:
*Contoh:*
- *"mempelajari"* -> `"ajar"`
- *"pengembangan"* -> `"kembang"`
- *"diterapkannya"* -> `"terap"`

---

## C. VEKTORISASI TEKS: MENGUBAH KATA MENJADI ANGKA

Setelah teks dibersihkan menjadi daftar kata dasar, komputer tetap belum dapat memprosesnya karena algoritma Machine Learning hanya mampu melakukan operasi aljabar pada angka numerik. Tahap berikutnya adalah **Vektorisasi Teks (*Text Vectorization*)**.

### 1. Pendekatan Kantung Kata (Bag of Words / BoW)

Metode BoW menyusun sebuah kamus kosakata (*vocabulary*) dari seluruh kata unik yang muncul di seluruh dokumen, lalu memetakan setiap kalimat menjadi vektor frekuensi kemunculan kata.
*Kelemahan BoW:* Mengabaikan urutan tata bahasa dan memberikan nilai bobot yang sama tingginya pada kata-kata umum yang sering berulang di semua dokumen, padahal kata tersebut kurang informatif.

### 2. Algoritma Pembobotan TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF adalah standar emas dalam sains penelusuran informasi (*Information Retrieval*) dan NLP klasik. Algoritma ini memberikan bobot nilai tinggi pada kata yang **sering muncul di dokumen tertentu**, namun **jarang muncul di dokumen-dokumen lainnya** (menandakan kata tersebut adalah kata kunci unik pembeda topik).

Rumus Matematis TF-IDF:
1. **Term Frequency (TF):** Frekuensi kemunculan kata $t$ di dalam dokumen spesifik $d$.
   `TF(t, d) = Jumlah kemunculan kata t dalam dokumen d / Total kata dalam dokumen d`
2. **Inverse Document Frequency (IDF):** Ukuran seberapa langka kata $t$ di seluruh koleksi total $N$ dokumen.
   `IDF(t) = log( Total seluruh dokumen N / Jumlah dokumen yang memuat kata t )`
3. **Bobot Akhir TF-IDF:**
   `TF-IDF(t, d) = TF(t, d) * IDF(t)`

Jika sebuah kata (misal: "sekolah") muncul di hampir setiap dokumen, nilai IDF-nya akan mendekati nol, sehingga bobot akhirnya menjadi sangat rendah. Sebaliknya, kata langka dan spesifik (misal: "konvolusi" atau "algoritma") akan memperoleh bobot nilai yang sangat tinggi.

---

## D. PENGANTAR ARSITEKTUR TRANSFORMER DAN MEKANISME PERHATIAN (SELF-ATTENTION)

Dalam sejarah pembelajaran mendalam untuk teks, model generasi lama seperti Recurrent Neural Networks (RNN) dan LSTM memiliki keterbatasan fatal: model membaca kata satu demi satu secara sekuensial dari kiri ke kanan. Ketika memproses paragraf yang sangat panjang, model RNN menderita fenomena "lupa ingatan" (*catastrophic forgetting*) di mana konteks kata di awal paragraf telah pudar saat model mencapai akhir paragraf.

### 1. Terobosan Bersejarah: "Attention Is All You Need" (2017)

Pada tahun 2017, tim peneliti Google mempublikasikan makalah ilmiah legendaris berjudul *"Attention Is All You Need"*. Makalah ini memperkenalkan arsitektur baru bernama **Transformer**, yang membuang mekanisme perulangan sekuensial dan menggantinya dengan pemrosesan paralel penuh yang ditenagai oleh **Mekanisme Perhatian Diri Sendiri (*Self-Attention Mechanism*)**.

### 2. Cara Kerja Mekanisme Self-Attention

Mekanisme Attention memungkinkan model komputasi untuk menimbang dan menghitung derajat keterkaitan semantik antara setiap kata dengan seluruh kata lainnya dalam kalimat secara simultan.

Perhatikan kalimat kompleks berikut:
*"Kucing itu tidak mau menyeberang jalan raya karena **ia** terlalu lelah."*
Bagi manusia, akal budi kita langsung memahami bahwa kata ganti **"ia"** merujuk pada **kucing**, bukan pada jalan raya.
Bagi komputer konvensional, penentuan rujukan ini sangat membingungkan. Namun dengan mekanisme Self-Attention, model Transformer menghitung matriks probabilitas hubungan bobot kata. Model memberikan skor perhatian (*attention score*) yang sangat tinggi antara token kata `"ia"` dan kata `"kucing"`, sehingga makna semantik utuh kalimat dapat dipahami secara akurat tanpa distorsi.

Arsitektur Transformer inilah yang menjadi fondasi tunggal yang menggerakkan seluruh revolusi model bahasa cerdas dunia (*Generative Pre-trained Transformer* / GPT, Gemini, LLaMA, dan Claude).

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 5.1

### Membangun Model Analisis Sentimen Ulasan Berbasis Teks Menggunakan Python

**Tujuan Pembelajaran:**
Peserta didik mampu menerapkan tahapan pra-pemrosesan teks sederhana, mentransformasikan ulasan kalimat menjadi representasi numerik menggunakan pembobotan TF-IDF, serta melatih model klasifikasi Naive Bayes / Decision Tree untuk memprediksi sentimen ulasan positif dan negatif secara otomatis.

**Alat dan Bahan:**
1. Komputer/Laptop dengan Python 3 terpasang.
2. Pustaka Scikit-Learn terinstal (`pip install scikit-learn`).

**Instruksi Kerja Praktikum:**
1. Buatlah berkas Python baru bernama `praktikum_sentimen_nlp.py`.
2. Ketikkan dan pelajari kode implementasi analisis sentimen teks berikut:

```python
# Klasifikasi Analisis Sentimen Ulasan dengan TF-IDF & Naive Bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def jalankan_analisis_sentimen():
    print("===== 1. MENYIAPKAN DATASET TEKS PELATIHAN =====")
    # Sampel dataset opini ulasan kantin sekolah
    data_ulasan = [
        "Makanan kantin hari ini sangat enak lezat dan bersih sekali",
        "Pelayanan ramah tempat duduk nyaman makanannya sedap",
        "Menu ayam bakar gurih sekali porsinya mengenyangkan puas",
        "Rasa makanan nikmat higienis dan harga sangat terjangkau",
        "Makanannya dingin hambar tidak enak pelayanannya lambat",
        "Sangat kecewa porsi sedikit harga mahal dan tempat kotor",
        "Jus buahnya basi berbau masam bikin sakit perut parah",
        "Pelayan kantin judes tidak sopan makanan dingin mengecewakan"
    ]
    # Label: 1 = Positif, 0 = Negatif
    label_sentimen = [1, 1, 1, 1, 0, 0, 0, 0]

    # 2. Membangun Pipeline NLP: TfidfVectorizer + Klasifier Naive Bayes
    # Pipeline mengotomasi proses vektorisasi dan inferensi model
    model_nlp = make_pipeline(
        TfidfVectorizer(lowercase=True, stop_words=None),
        MultinomialNB()
    )

    # 3. Melatih Model
    model_nlp.fit(data_ulasan, label_sentimen)
    print("[SUKSES] Model NLP berhasil dilatih menggunakan vektor TF-IDF!")

    # 4. Pengujian dengan Kalimat Opini Baru yang Belum Pernah Dilihat
    kalimat_uji = [
        "Tempatnya sangat bersih dan ayam gorengnya lezat mantap",
        "Kecewa sekali makanannya dingin dan sangat mahal",
        "Pelayanannya ramah makanannya sangat memuaskan",
        "Harganya mahal rasanya hambar bikin kapok"
    ]

    print("\n===== 2. PENGUJIAN PREDIKSI SENTIMEN REAL-TIME =====")
    prediksi = model_nlp.predict(kalimat_uji)
    probabilitas = model_nlp.predict_proba(kalimat_uji)

    for i, teks in enumerate(kalimat_uji):
        kategori = "POSITIF (+)" if prediksi[i] == 1 else "NEGATIF (-)"
        skor_keyakinan = probabilitas[i][prediksi[i]] * 100
        print(f"Kalimat : \"{teks}\"")
        print(f"Hasil   : {kategori} (Tingkat Keyakinan: {skor_keyakinan:.2f}%)")
        print("-" * 65)

if __name__ == "__main__":
    jalankan_analisis_sentimen()
```

3. Eksekusi program di terminal dan amatilah bagaimana model mampu mengenali sentimen positif dan negatif pada kalimat-kalimat baru secara akurat!
4. Masukkan kalimat uji coba kalian sendiri yang memuat kata-kata unik, lalu amati tingkat keyakinan probabilitas yang dihasilkan oleh model!

**Pertanyaan Analisis Laboratorium:**
1. Mengapa teknik pembobotan TF-IDF jauh lebih akurat digunakan pada pengolahan teks dibandingkan hanya menghitung panjang karakter kalimat?
2. Apa yang terjadi jika sebuah model NLP yang dilatih menggunakan bahasa Indonesia baku diuji dengan kalimat yang dipenuhi bahasa gaul singkatan (*slang*)? Langkah pra-pemrosesan tambahan apa yang wajib ditambahkan pada pipeline?
3. Uraikan mengapa pemahaman konteks antar-kata melalui mekanisme perhatian (*Attention*) menjadi kunci utama yang membedakan model bahasa modern (LLM) dari sistem klasifikasi teks berbasis kata kunci sederhana!

---

## F. RANGKUMAN MATERI BAB V

1. **Kompleksitas Komputasi Bahasa:** Bahasa alami manusia sarat dengan ambiguitas semantik, afiksasi morfologis bertingkat, nuansa emosi sarkasme, dan dialek sosial yang menuntut pemrosesan komputasi melampaui pencocokan kata kunci linier.
2. **Tahapan Pra-Pemrosesan Teks:** Rangkaian pembersihan data teks yang mencakup *Case Folding* (penyeragaman huruf kecil), *Tokenizing* (pemotongan kata), *Stopwords Removal* (pembuangan kata sambung umum), dan *Stemming* (reduksi imbuhan ke bentuk kata dasar menggunakan algoritma Nazief-Adriani / Sastrawi).
3. **Vektorisasi TF-IDF:** Mentransformasikan kata menjadi bobot numerik berdasarkan frekuensi kemunculan kata dalam dokumen lokal (*Term Frequency*) dikalikan kelangkaan kata tersebut di seluruh koleksi dokumen (*Inverse Document Frequency*), menonjolkan kata kunci informatif.
4. **Revolusi Arsitektur Transformer:** Membuang keterbatasan model sekuensial lama (RNN/LSTM) dan menggantinya dengan mekanisme *Self-Attention* paralel yang menghitung bobot keterkaitan antarkata dalam kalimat secara komprehensif, menjadi landasan teknologi di balik lahirnya model bahasa besar dunia (LLM).

---

## G. UJI KOMPETENSI BAB V

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Cabang ilmu kecerdasan artifisial yang berfokus pada kemampuan komputer untuk memahami, menginterpretasikan, memanipulasi, dan menghasilkan bahasa alami manusia dinamakan...
   A. Computer Vision
   B. Natural Language Processing (NLP)
   C. Internet of Things
   D. Cryptographic Hashing

2. Tahapan pra-pemrosesan teks yang bertujuan menyeragamkan seluruh karakter abjad di dalam dokumen menjadi huruf kecil (*lowercase*) untuk menghindari duplikasi kata disebut...
   A. Tokenizing
   B. Case Folding
   C. Stemming
   D. Lemmatization

3. Proses memecah satu paragraf atau kalimat panjang menjadi potongan-potongan kata individual yang berdiri sendiri di dalam struktur daftar dinamakan...
   A. Tokenizing
   B. Normalisasi
   C. Penskalaan Fitur
   D. Serialisasi

4. Kata-kata umum seperti "dan", "di", "ke", "dari", "yang", dan "adalah" yang sering dibuang dalam pemrosesan teks karena tidak membawa bobot informasi unik dikenal dengan istilah...
   A. Rare words
   B. Stopwords
   C. Keywords
   D. Root words

5. Proses morfologis dalam bahasa Indonesia untuk menghilangkan seluruh imbuhan (awalan, sisipan, dan akhiran) guna mengembalikan kata ke bentuk aslinya dinamakan...
   A. Stemming
   B. Tokenizing
   C. Vectorizing
   D. Parsing

6. Algoritma pembobotan teks yang memberikan skor tinggi pada kata yang sering muncul dalam dokumen tertentu tetapi jarang muncul di seluruh dokumen lain dalam suatu korpus koleksi adalah...
   A. One-Hot Encoding
   B. Bag of Words
   C. TF-IDF (Term Frequency - Inverse Document Frequency)
   D. Label Encoder

7. Apabila sebuah kata muncul di hampir seluruh dokumen di dalam pangkalan data perpustakaan digital, maka nilai *Inverse Document Frequency* (IDF) dari kata tersebut akan...
   A. Mendekati angka tak hingga
   B. Bernilai negatif
   C. Mendekati angka nol sehingga bobot informasinya menjadi sangat rendah
   D. Berubah menjadi karakter gambar

8. Makalah ilmiah legendaris terbitan Google Research pada tahun 2017 yang memperkenalkan arsitektur Transformer dan mekanisme perhatian (*Attention Mechanism*) berjudul...
   A. Deep Learning in Practice
   B. Attention Is All You Need
   C. The Master Algorithm
   D. Computer Machinery and Intelligence

9. Komponen utama dalam arsitektur Transformer yang memungkinkan model menimbang derajat keterkaitan semantik antara suatu kata ganti (misal kata "ia") dengan subjek aslinya di dalam kalimat panjang secara simultan adalah...
   A. Convolutional Kernel
   B. Self-Attention Mechanism
   C. Pooling Layer
   D. Sigmoid Activation

10. Mengapa model klasifikasi teks berbasis kamus kata kunci sederhana (*keyword matching*) sering kali salah dalam menganalisis kalimat yang memuat majas sarkasme atau sindiran halus?
    A. Karena kamus kata kunci mengonsumsi daya listrik terlalu besar
    B. Karena kamus kata kunci hanya mencocokkan kata positif secara harfiah tanpa mempertimbangkan konteks relasi antarkata di sekelilingnya
    C. Karena kata sarkasme selalu ditulis menggunakan bahasa asing
    D. Karena model kamus tidak dapat membaca huruf vokal

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan mengapa bahasa alami manusia (*Natural Language*) jauh lebih sulit dipahami oleh sistem komputasi dibandingkan bahasa pemrograman komputer formal (seperti Python atau SQL)! Uraikan minimal tiga faktor penyebabnya!
2. Diberikan kalimat mentah dari sebuah ulasan media sosial:
   `"Siswa-siswa SANGAT MENGAPRESIASI pembelajaran koding di sekolah ini!"`
   Tuliskan perubahan bentuk kalimat tersebut secara bertahap melalui empat fase pra-pemrosesan teks: Case Folding, Tokenizing, Stopwords Removal, dan Stemming Bahasa Indonesia!
3. Jelaskan prinsip kerja matematis dari pembobotan TF-IDF! Mengapa kata "komputasi" pada artikel jurnal sains komputer akan memperoleh bobot TF-IDF yang jauh lebih tinggi daripada kata "adalah"?
4. Uraikan keterbatasan mendasar dari arsitektur model sekuensial lama seperti Recurrent Neural Networks (RNN) saat memproses teks panjang, dan jelaskan bagaimana arsitektur Transformer menyelesaikan kelemahan tersebut melalui mekanisme pemrosesan paralel dan *Self-Attention*!
5. Rancanglah sebuah alur kerja sistem deteksi ujaran kebencian (*Hate Speech Detection*) otomatis untuk mengawal kolom komentar portal berita daring sekolah! Sebutkan tahapan pipeline yang harus dilalui serta pertimbangan etika dalam membedakan antara kritik konstruktif dan ujaran kebencian!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB V

**Kunci Pilihan Ganda:**
1. **B** (NLP berfokus pada komputasi pemrosesan bahasa manusia).
2. **B** (Case Folding menyeragamkan seluruh karakter abjad menjadi huruf kecil).
3. **A** (Tokenizing memecah kalimat menjadi token kata individual).
4. **B** (Stopwords adalah kata fungsional umum yang disaring dan dibuang).
5. **A** (Stemming memotong imbuhan untuk mengembalikan kata ke bentuk dasar).
6. **C** (TF-IDF menimbang frekuensi kemunculan terhadap kelangkaan dokumen).
7. **C** (Kata pasaran yang muncul di semua dokumen memiliki IDF mendekati nol).
8. **B** ("Attention Is All You Need" adalah judul makalah revolusioner Vaswani et al., 2017).
9. **B** (Self-Attention mechanism menghitung bobot keterkaitan semantik antarkata).
10. **B** (Keyword matching gagal menangkap sarkasme karena mengabaikan konteks semantik kalimat).

**Pembahasan Soal Uraian:**
1. *Tantangan Komputasi Bahasa Manusia:*
   - Ambiguitas Kontekstual: Satu kata memiliki banyak arti yang bergantung pada kata sekitarnya (polisemi).
   - Morfologi Fleksibel: Sistem imbuhan yang kompleks (afiksasi) mengubah struktur dan fungsi gramatikal kata secara dinamis.
   - Bahasa Kiasan & Sarkasme: Makna sesungguhnya sering kali bertolak belakang dengan makna harfiah kata penyusunnya. Sebaliknya, bahasa pemrograman dirancang formal, memiliki tata bahasa kaku (*context-free grammar*), dan bebas dari ambiguitas tafsir.
2. *Tahapan Preprocessing Kalimat:*
   - Kalimat Asli: `"Siswa-siswa SANGAT MENGAPRESIASI pembelajaran koding di sekolah ini!"`
   - Case Folding: `"siswa-siswa sangat mengapresiasi pembelajaran koding di sekolah ini"` (huruf kecil dan tanda seru dibuang).
   - Tokenizing: `['siswa-siswa', 'sangat', 'mengapresiasi', 'pembelajaran', 'koding', 'di', 'sekolah', 'ini']`.
   - Stopwords Removal: `['siswa-siswa', 'mengapresiasi', 'pembelajaran', 'koding', 'sekolah']` (kata *sangat, di, ini* dibuang).
   - Stemming: `['siswa', 'apresiasi', 'ajar', 'koding', 'sekolah']` (kata dikembalikan ke akar kata dasar).
3. *Prinsip Matematis TF-IDF:*
   - TF mengukur frekuensi kemunculan lokal: seberapa sering kata tersebut muncul dalam satu artikel spesifik.
   - IDF mengukur kelangkaan global: logaritma dari total dokumen dibagi jumlah dokumen yang memuat kata tersebut.
   - Kata "adalah" muncul di hampir 100% dokumen, sehingga nilai N/DF mendekati 1 dan log(1) = 0. Akibatnya bobot TF-IDF kata "adalah" menjadi 0 (tidak berharga). Sebaliknya kata "komputasi" hanya muncul di beberapa dokumen khusus, sehingga nilai IDF-nya tinggi dan bobot akhirnya sangat besar, menjadikannya pembeda topik yang kuat.
4. *Kelemahan RNN vs Terobosan Transformer:*
   - RNN membaca kata secara sekuensial satu per satu dari kiri ke kanan. Informasi kata awal dialirkan melalui status tersembunyi (*hidden state*) yang semakin lama semakin memudar (*vanishing gradient*), sehingga model melupakan konteks awal pada kalimat panjang. Selain itu, proses sekuensial tidak dapat diparalelkan di kartu grafis (GPU).
   - Transformer memproses seluruh kata dalam kalimat secara paralel sekaligus. Mekanisme Self-Attention menghitung matriks korelasi langsung antara setiap pasangan kata tanpa peduli seberapa jauh jarak posisinya di dalam teks, melipatgandakan kecepatan pelatihan dan mempertahankan pemahaman konteks panjang secara sempurna.
5. *Alur Deteksi Ujaran Kebencian & Etika:*
   - Pipeline: Pengumpulan data komentar -> Pra-pemrosesan teks (Pembersihan slang & normalisasi singkatan) -> Vektorisasi TF-IDF / Word Embedding -> Model Klasifikasi berbasis probabilitas -> Penandaan otomatis.
   - Pertimbangan Etika: Sistem harus dilatih secara cermat agar mampu membedakan antara ekspresi kritik konstruktif (misal: *"Kebijakan ini kurang tepat dan perlu diperbaiki sistemnya"*) dengan ujaran kebencian yang menyerang martabat SARA individu. Komentar yang terdeteksi tidak boleh langsung dihapus permanen oleh AI (*No Black Box tyranny*), melainkan dialirkan ke moderator manusia (*Human-in-the-Loop*) untuk menjamin kebebasan berpendapat yang sehat.
"""
