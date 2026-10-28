"""
Modul Naskah Bab I Kelas XII SMA/SMK (Fase F Akhir)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

BAB1_SMA12 = """# BAB I: PEMROGRAMAN PERANGKAT KERAS CERDAS: INTERNET OF THINGS (IOT) TERHUBUNG AI

## APERSEPSI: KETIKA SENSOR CERDAS KEHABISAN DAYA DI TENGAH LADANG

Di kebun percobaan agrikultura sekolah pagi itu, Bagas tampak sedang berjongkok memeriksa sebuah kotak sirkuit plastik tahan air yang terpasang pada tiang bambu di tengah bedengan tanaman cabai. Kotak tersebut memuat sebuah modul mikrokontroler dan sensor kelembapan tanah yang seharusnya mengalirkan data ke komputer laboratorium. Namun, layar dasbor di ponsel Bagas menunjukkan status mati (*offline*).

[GAMBAR: assets/bab1_komik_pembuka_sma12.png]

"Dinda, Arya, sistem pemantau otomatis kita mati lagi!" seru Bagas sambil melepas penutup sirkuitnya. "Baterai lithium berkapasitas besar ini baru dipasang kemarin sore, tetapi pagi ini tegangannya sudah drop total di bawah 3 Volt. Modul mikrokontroler ini terus-menerus mencoba mengirimkan permintaan HTTP berukuran besar ke peladen web awan setiap lima detik sekali, dan ketika sinyal seluler di kebun melemah, sistem terus mencoba mengulang (*retry*) hingga baterai terkuras habis!"

Arya mengamati log jaringan pada laptopnya seraya mengangguk paham. "Itu kelemahan mendasar protokol HTTP pada perangkat keras nirkabel mandiri, Bagas. Protokol HTTP membawa beban data tambahan (*header overhead*) yang sangat boros kuota, dan arsitektur *Request-Response*-nya memaksa perangkat keras tetap terjaga penuh tanpa sempat memasuki mode tidur hemat daya (*deep sleep mode*). Kita harus beralih ke protokol telemetri nirkabel standar industri IoT: **MQTT (*Message Queuing Telemetry Transport*)**!"

Dinda menimpali dengan ide revolusioner, "Dan bukan hanya itu, kawan. Mengapa kita harus mengirimkan seluruh data mentah sensor ke peladen awan yang jauh hanya untuk memutuskan apakah katup air irigasi harus dibuka atau ditutup? Kita bisa menanamkan model kecerdasan artifisial ringan langsung di dalam cip mikrokontroler itu sendiri! Ini adalah paradigma mutakhir yang disebut **Edge AI (*Kecerdasan di Ujung Perangkat*)**!"

"Luar biasa!" mata Bagas kembali berbinar penuh semangat. "Dengan Edge AI dan protokol MQTT, alat kita bisa beroperasi mandiri tanpa latensi, tidak bergantung pada koneksi internet, dan baterainya bisa bertahan berbulan-bulan!"

"Tepat sekali!" sambung Arya. "Mari kita bedah arsitektur sistem siber-fisik, akuisisi sensor, aktuator daya tinggi, protokol MQTT, hingga implementasi Edge AI pada perangkat keras nyata!"

---

## A. ARSITEKTUR TIGA LAPISAN SISTEM INTERNET OF THINGS (IOT)

Dalam perkembangan teknologi modern, komputer tidak lagi terisolasi di dalam kotak CPU atau layar monitor ponsel. Komputer kini merasuk ke dalam benda-benda fisik di sekitar kita—mulai dari lampu jalan, mesin cuci, hingga sensor ladang pertanian. Penyatuan harmonis antara dunia komputasi digital dan dunia fisik dinamakan **Sistem Siber-Fisik (*Cyber-Physical System* / CPS)**, yang fondasinya dibangun oleh arsitektur **Internet of Things (IoT)**.

[GAMBAR: assets/bab1_diagram_arsitektur_iot_edge_ai.png]

Arsitektur standar sistem IoT komersial tersusun atas tiga lapisan hierarkis berkesinambungan:

### 1. Lapisan Persepsi Fisik (Perception Layer)
Merupakan ujung tombak fisik yang bersentuhan langsung dengan lingkungan nyata. Terdiri atas:
- **Sensor:** Mengubah besaran fisik analog di alam (suhu, kelembapan, intensitas cahaya, konsentrasi gas) menjadi sinyal data listrik terukur.
- **Aktuator:** Melakukan aksi mekanik atau fisik balasan berdasarkan instruksi sistem (misal: menyalakan pompa air, memutar motor servo, atau mengaktifkan alarm sirine).
- **Unit Pengendali Mikro (*Microcontroller Unit* / MCU):** Cip pemroses lokal berdaya rendah (seperti ESP32) yang bertugas membaca sinyal sensor dan mengatur siklus kerja aktuator.

### 2. Lapisan Jaringan Komunikasi (Network Layer)
Jembatan transmisi data yang mengalirkan paket informasi dari perangkat keras lapangan menuju infrastruktur pemrosesan terpusat. Lapisan ini memanfaatkan teknologi nirkabel hemat daya seperti Wi-Fi, Bluetooth Low Energy (BLE), LoRaWAN (*Long Range Wide Area Network*), maupun jaringan seluler 4G/5G, menggunakan protokol perpesanan ringan seperti **MQTT** atau **CoAP**.

### 3. Lapisan Aplikasi dan Pengguna (Application Layer)
Puncak arsitektur tempat data disajikan kepada pengguna manusia dalam bentuk dasbor visual analitik (*real-time dashboard*), sistem peringatan dini SMS/WhatsApp, serta pengambil keputusan strategis berbasis mahadata dan AI.

---

## B. KOMPUTASI FISIK: AKUISISI DATA SENSOR DAN PENGENDALIAN AKTUATOR

Jantung dari komputasi fisik modern adalah cip **ESP32**, sebuah mikrokontroler berbiaya terjangkau yang dilengkapi prosesor ganda bertenaga, antena Wi-Fi dan Bluetooth bawaan, serta puluhan pin **GPIO (*General Purpose Input/Output*)**.

### 1. Ragam Sensor Esensial dalam Ekosistem IoT

1. **Sensor Suhu dan Kelembapan Udara (DHT22 / AM2302):**
Sensor digital yang mengukur suhu (-40 hingga 80 derajat Celcius) dan kelembapan relatif (0-100% RH) dengan akurasi tinggi menggunakan elemen kapasitif dan termistor presisi.
2. **Sensor Jarak Ultrasonik (HC-SR04):**
Bekerja menyerupai sistem ekolokasi kelelawar: memancarkan gelombang ultrasonik 40 kHz melalui pin *Trigger*, lalu menghitung selang waktu pantulan gelombang yang diterima kembali oleh pin *Echo* untuk mengukur jarak benda dalam satuan sentimeter.
3. **Sensor Kualitas Udara dan Kebocoran Gas (MQ-2 / MQ-135):**
Menggunakan lapisan sensitif Timah Dioksida (SnO2) yang konduktivitas listriknya berubah seiring meningkatnya konsentrasi gas mudah terbakar (LPG, metana, asap, atau karbon monoksida).
4. **Modul Penglihatan Mini (ESP32-CAM):**
Modul mikrokontroler yang dilengkapi kamera OV2640 beresolusi 2 Megapiksel dan slot kartu memori, mampu mengambil gambar dan mengalirkan video langsung.

### 2. Pengendalian Aktuator Daya Tinggi Menggunakan Modul Relay

Pin keluaran mikrokontroler ESP32 hanya mampu memancarkan tegangan listrik searah kecil sebesar 3,3 Volt dengan arus maksimum sekitar 12 miliampere. Tegangan ini sama sekali tidak mampu menggerakkan pompa air berdaya 220 Volt PLN atau motor listrik industri.

Untuk mengendalikan perangkat bertegangan tinggi secara aman, digunakan **Modul Relay Optocoupler**:
- Relay bertindak sebagai sakelar elektromekanik yang memisahkan secara fisik (*galvanic isolation*) sirkuit digital mikro 3,3V yang sensitif dari sirkuit listrik daya tinggi 220V.
- Ketika pin GPIO mengirimkan sinyal logika `HIGH`, kumparan elektromagnetik di dalam relay menarik plat kontak sakelar, menyalakan pompa air secara aman tanpa risiko korsleting merusak mikrokontroler.

---

## C. PROTOKOL KOMUNIKASI TELEMETRI RINGAN: MQTT PUBLISH-SUBSCRIBE VS HTTP

Pada perancangan aplikasi web biasa, protokol HTTP (*Hypertext Transfer Protocol*) sangat populer. Namun pada perangkat IoT bertenaga baterai yang diletakkan di ladang terpencil dengan sinyal seluler tidak stabil, protokol HTTP menjadi pilihan yang sangat buruk.

### 1. Mengapa Protokol HTTP Tidak Cocok untuk Perangkat IoT Mandiri?

- **Header Overhead yang Boros:** Setiap kali mengirimkan data angka sederhana (misal: "suhu: 28"), HTTP menyertakan header teks panjang (metode, user-agent, cookies, content-type) yang berukuran ratusan byte. Data pembungkus jauh lebih besar daripada data intinya!
- **Model Request-Response yang Statis:** Sensor harus bertindak sebagai klien yang terus-menerus bertanya (*polling*) ke server, memaksa sirkuit antena radio nirkabel menyala terus-menerus dan menguras daya baterai secara masif.

### 2. Keunggulan Arsitektur Publish-Subscribe Protokol MQTT

**MQTT (Message Queuing Telemetry Transport)** diciptakan khusus oleh Andy Stanford-Clark (IBM) dan Arlen Nipper pada tahun 1999 untuk memantau jaringan pipa minyak melalui satelit. MQTT dirancang sangat ringan (ukuran header minimum hanya 2 Byte!), hemat daya, dan menggunakan arsitektur **Publish-Subscribe**:

1. **Broker MQTT (Peladen Pusat):** Jantung perantara pesan (misal: HiveMQ, Eclipse Mosquitto, EMQX). Broker bertugas menerima pesan dari pengirim dan meneruskannya hanya kepada pihak yang berminat.
2. **Topik Telemetri (*Topics*):** Jalur saluran pesan yang disusun secara hierarkis menggunakan tanda garis miring. Contoh topik: `sekolah/kebun/suhu` atau `sekolah/lab/relay1`.
3. **Publisher (Pengirim Data):** Perangkat mikrokontroler yang mengirimkan data telemetri ke topik tertentu.
4. **Subscriber (Penerima Data):** Aplikasi dasbor ponsel atau komputer pengguna yang berlangganan pada topik tertentu untuk menerima pembaruan data secara instan saat ada data baru masuk.

### 3. Tiga Tingkat Jaminan Pengiriman (Quality of Service / QoS)

- **QoS 0 (At most once / Paling banyak sekali):** Pesan dikirim tanpa konfirmasi (*fire and forget*). Sangat cepat dan hemat kuota, cocok untuk pembacaan suhu rutin yang hilang satu paket tidak menjadi masalah.
- **QoS 1 (At least once / Paling tidak sekali):** Menjamin pesan pasti sampai dengan meminta konfirmasi penerimaan (*PUBACK*). Jika belum ada jawaban, pesan dikirim ulang (ada kemungkinan pesan ganda).
- **QoS 2 (Exactly once / Tepat sekali):** Jaminan tingkat tertinggi melalui jabat tangan 4 langkah. Memastikan pesan diterima tepat satu kali tanpa duplikasi, cocok untuk instruksi perintah penagihan transaksi keuangan atau alarm darurat kritis.

---

## D. PARADIGMA EDGE AI: MENJALANKAN MODEL CERDAS DI MIKROKONTROLER

Kecerdasan artifisial konvensional bekerja dengan konsep **Cloud AI**: perangkat lokal mengambil gambar atau audio, mengirimkannya melalui jaringan internet ke peladen raksasa di awan (*Cloud*), peladen mengeksekusi model Deep Learning, lalu mengirimkan kesimpulan kembali ke perangkat lokal.

Namun, bagaimana jika koneksi internet terputus di tengah bencana alam? Bagaimana jika sistem rem otomatis mobil harus menunggu respons awan selama 2 detik? Dua detik tersebut dapat merenggut nyawa manusia!

Inilah alasan lahirnya revolusi **Edge AI** dan **TinyML (Tiny Machine Learning)**.

### 1. Keunggulan Mutlak Edge AI

1. **Zero Latency (Respons Tanpa Jeda):** Inferensi keputusan dieksekusi dalam hitungan milidetik secara lokal di sirkuit prosesor mikrokontroler.
2. **Kedaulatan Privasi Tinggi (*Privacy-Preserving*):** Data citra kamera atau suara sensorik diproses langsung di perangkat dan tidak pernah dikirimkan ke internet, melindungi kerahasiaan data pengguna dari peretasan siber.
3. **Hemat Biaya & Bandwidth Jaringan:** Tidak memerlukan kuota internet seluler berbayar bulanan dan memangkas biaya sewa peladen komputasi awan.
4. **Keandalan Mandiri 100% (*Offline Resilience*):** Alat tetap bekerja mengambil keputusan cerdas meskipun berada di dasar hutan belantara, di bawah laut, atau di area tanpa sinyal seluler sama sekali.

### 2. Kuantisasi Model: Dari Float32 Menuju Int8

Model jaringan saraf tiruan standar biasanya menyimpan bobot neuron menggunakan format angka desimal presisi tunggal 32-bit (*Floating Point 32* / Float32). Model berukuran ratusan Megabyte ini mustahil dimasukkan ke dalam memori RAM mikrokontroler ESP32 yang hanya berukuran 520 Kilobyte.

Melalui teknik **Kuantisasi (*Model Quantization*)** pada kerangka kerja **TensorFlow Lite for Microcontrollers**, nilai bobot neuron 32-bit dikompresi menjadi angka bulat 8-bit (*Integer 8* / Int8):
- Ukuran model menyusut drastis hingga 75% lebih kecil.
- Kebutuhan memori RAM berkurang masif.
- Komputasi angka bulat dieksekusi jauh lebih cepat oleh prosesor cip dengan penurunan akurasi yang sangat minimal (kurang dari 1%).

---

## E. LEMBAR KERJA PESERTA DIDIK (LKPD) 1.1

### Rancang Bangun Sistem Pemantau Lingkungan Cerdas Berbasis ESP32 dan MQTT

**Tujuan Pembelajaran:**
Peserta didik mampu merangkai sensor suhu dan kelembapan fisik pada papan mikrokontroler ESP32, memprogram koneksi telemetri nirkabel menggunakan protokol MQTT ke peladen broker publik terenkripsi, serta memantau aliran data telemetri real-time melalui dasbor web.

**Alat dan Bahan:**
1. Papan mikrokontroler ESP32 DevKit V1.
2. Sensor suhu dan kelembapan DHT22 / DHT11.
3. Papan sirkuit percobaan (*Breadboard*) dan kabel jumper.
4. Komputer dengan Arduino IDE atau VS Code PlatformIO.
5. Pustaka perangkat lunak: `PubSubClient` dan `DHT sensor library`.

**Instruksi Kerja Praktikum:**
1. Rangkai sensor DHT22 ke pin ESP32: Pin VCC ke 3.3V, Pin GND ke GND, dan Pin Data ke GPIO 4 (beri resistor pull-up 10k ohm).
2. Tuliskan kode program telemetri MQTT berikut ke dalam IDE:

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// Konfigurasi Kredensial Jaringan WiFi
const char* ssid = "NAMA_WIFI_SEKOLAH";
const char* password = "KATA_SANDI_WIFI";

// Konfigurasi Broker Publik MQTT
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
const char* topik_telemetri = "sekolah/faseF/lingkungan";

#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

void hubungkan_wifi() {
  Serial.print("Menghubungkan ke WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n[SUKSES] WiFi Terhubung!");
}

void hubungkan_mqtt() {
  while (!client.connected()) {
    Serial.print("Mencoba koneksi ke Broker MQTT...");
    String clientId = "ESP32Client-" + String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("[TERHUBUNG]");
    } else {
      Serial.print("[GAGAL], rc=");
      Serial.print(client.state());
      Serial.println(" Mencoba lagi dalam 5 detik...");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  hubungkan_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    hubungkan_mqtt();
  }
  client.loop();

  // Membaca data fisik lingkungan
  float suhu = dht.readTemperature();
  float kelembapan = dht.readHumidity();

  if (isnan(suhu) || isnan(kelembapan)) {
    Serial.println("[PERINGATAN] Gagal membaca data dari sensor DHT!");
    delay(2000);
    return;
  }

  // Menyusun muatan data ringan JSON
  String payload = "{\"suhu\": " + String(suhu, 2) + ", \"kelembapan\": " + String(kelembapan, 2) + "}";
  
  // Menerbitkan pesan ke Broker MQTT (Publish)
  client.publish(topik_telemetri, payload.c_str());
  Serial.println(">> Pesan Terkirim: " + payload);

  // Masuk ke mode jeda hemat daya selama 10 detik
  delay(10000);
}
```

3. Unggah (*flash*) program ke ESP32 dan buka Serial Monitor pada baud rate 115200.
4. Buka peramban di komputer kalian, akses klien web HiveMQ di `http://www.hivemq.com/demos/websocket-client/`.
5. Berlanggananlah (*Subscribe*) pada topik `sekolah/faseF/lingkungan`. Saksikan bagaimana data suhu dan kelembapan dari kebun sekolah muncul seketika di layar peramban kalian secara real-time!

**Pertanyaan Analisis Laboratorium:**
1. Mengapa ukuran paket data nirkabel MQTT jauh lebih kecil dan hemat baterai dibandingkan mengirimkan data menggunakan protokol HTTP POST?
2. Bagaimana mekanisme penamaan hierarkis topik MQTT (menggunakan tanda garis miring) memudahkan pengelolaan ratusan sensor di area sekolah yang luas?
3. Uraikan bagaimana modul sirkuit di atas dapat ditingkatkan menjadi sistem Edge AI yang secara mandiri mampu menyalakan kipas pendingin ruangan jika model memprediksi risiko overheat tanpa perlu instruksi dari server!

---

## F. RANGKUMAN MATERI BAB I

1. **Arsitektur Sistem Siber-Fisik (IoT):** Penyatuan dunia digital dan lingkungan fisik melalui tiga lapisan berjenjang: *Perception Layer* (sensor dan aktuator fisik), *Network Layer* (protokol telemetri nirkabel), dan *Application Layer* (dasbor analitik pengguna).
2. **Komputasi Fisik & Aktuator:** Mikrokontroler modern (ESP32) membaca data fisik melalui sensor analog/digital dan mengendalikan perangkat bertegangan tinggi 220V secara aman menggunakan modul relay berisolasi optocoupler.
3. **Protokol Telemetri Ringan MQTT:** Arsitektur *Publish-Subscribe* yang sangat efisien daya dan pita lebar dengan overhead header hanya 2 Byte. Menggunakan konsep Broker pusat, jalur Topik hierarkis, serta tiga tingkatan keandalan pengiriman paket data (*Quality of Service* QoS 0, QoS 1, QoS 2).
4. **Revolusi Edge AI & TinyML:** Mengeksekusi inferensi model kecerdasan artifisial langsung di perangkat keras mikrokontroler lokal melalui teknik kuantisasi bobot neuron (Float32 ke Int8). Memberikan keunggulan mutlak berupa respons instan nol latensi, privasi data terlindungi sejalan dengan UU PDP, dan keandalan sistem mandiri tanpa ketergantungan jaringan internet.

---

## G. UJI KOMPETENSI BAB I

### I. Pilihan Ganda
Pilihlah salah satu jawaban yang paling tepat (A, B, C, atau D) untuk setiap butir pertanyaan berikut!

1. Lapisan dalam arsitektur Internet of Things (IoT) yang bertugas berinteraksi langsung dengan besaran fisik alam nyata melalui sensor dan aktuator dinamakan...
   A. Application Layer
   B. Perception Layer
   C. Transport Layer
   D. Business Layer

2. Komponen perangkat keras elektromekanik yang berfungsi sebagai sakelar penyambung sirkuit listrik berdaya tinggi (seperti pompa air 220V) yang dikendalikan oleh sinyal digital mikrokontroler 3,3V adalah...
   A. Sensor DHT22
   B. Modul Relay Optocoupler
   C. Resistor Pull-Up
   D. Kapasitor Keramik

3. Alasan utama mengapa protokol komunikasi MQTT jauh lebih disukai dibandingkan protokol HTTP pada perangkat IoT bertenaga baterai di lingkungan nirkabel adalah...
   A. Karena protokol MQTT hanya dapat dijalankan pada komputer super
   B. Karena protokol MQTT memiliki overhead ukuran header yang sangat kecil (mulai 2 Byte) dan berbasis Publish-Subscribe yang hemat daya
   C. Karena protokol HTTP tidak mendukung pengiriman data angka
   D. Karena protokol MQTT tidak membutuhkan alamat IP

4. Dalam arsitektur perpesanan protokol MQTT, entitas peladen pusat yang bertugas menerima pesan telemetri dari pengirim dan meneruskannya kepada penerima yang berlangganan dinamakan...
   A. Client Subscriber
   B. Hardware Publisher
   C. MQTT Broker
   D. Gateway Actuator

5. Tingkat jaminan pengiriman pesan pada protokol MQTT yang memastikan bahwa paket pesan telemetri dijamin sampai ke tujuan tepat satu kali tanpa kemungkinan duplikasi (*Exactly once*) adalah...
   A. QoS 0
   B. QoS 1
   C. QoS 2
   D. QoS 3

6. Paradigma rekayasa di mana model kecerdasan artifisial dilatih dan dieksekusi secara lokal langsung pada perangkat mikrokontroler fisik tanpa mengirim data mentah ke peladen awan internet dinamakan...
   A. Cloud Computing
   B. Edge AI (TinyML)
   C. Centralized Mainframe
   D. Grid Computing

7. Manakah di antara keunggulan berikut yang BUKAN merupakan manfaat langsung dari penerapan teknologi Edge AI pada sistem kendali industri?
   A. Respons kendali tanpa jeda latensi jaringan (*Zero Latency*)
   B. Sistem tetap beroperasi mandiri saat koneksi internet terputus total
   C. Menghilangkan kebutuhan perangkat keras mikrokontroler di lapangan
   D. Melindungi privasi data karena informasi tidak dialirkan ke peladen publik

8. Teknik optimasi model jaringan saraf tiruan dalam kerangka kerja TinyML yang mengonversi bobot numerik desimal Float32 menjadi bilangan bulat Int8 untuk menghemat memori cip dinamakan...
   A. Kuantisasi Model (*Quantization*)
   B. Serialisasi JSON
   C. Interpolasi Spasial
   D. Tokenisasi Teks

9. Pin masukan dan keluaran serbaguna pada papan mikrokontroler ESP32 yang dapat diprogram untuk membaca sinyal sensor atau memicu relay listrik dikenal dengan singkatan...
   A. HDMI
   B. GPIO (General Purpose Input/Output)
   C. SATA
   D. PCIe

10. Format penulisan topik saluran telemetri standar pada protokol MQTT yang mencerminkan struktur hierarki lokasi yang benar di bawah ini adalah...
    A. `sekolah.lab.suhu`
    B. `sekolah/lantai2/ruang_rpl/suhu`
    C. `sekolah-ruang-suhu`
    D. `sekolah::lab::suhu`

### II. Uraian Pemecahan Kasus
Jawablah pertanyaan-pertanyaan berikut dengan uraian analitis, runut, dan tepat!

1. Jelaskan perbedaan mendasar antara arsitektur komunikasi *Request-Response* pada protokol HTTP dan arsitektur *Publish-Subscribe* pada protokol MQTT! Mengapa arsitektur Publish-Subscribe jauh lebih unggul dalam sistem pemantauan telemetri IoT multi-sensor?
2. Uraikan secara rinci peran vital modul relay berisolasi optocoupler dalam menjembatani mikrokontroler bertegangan rendah (3,3V) dengan beban kelistrikan berdaya tinggi (motor pompa 220V)! Apa bahaya fisik yang terjadi jika mikrokontroler dihubungkan langsung ke motor 220V tanpa modul perantara?
3. Analisislah mengapa paradigma *Edge AI* sangat mutlak diwajibkan dalam perancangan sistem pengereman darurat otomatis pada kendaraan listrik cerdas dibandingkan mengandalkan komputasi awan (*Cloud AI*)! Uraikan kaitannya dengan faktor latensi jaringan dan keselamatan jiwa manusia!
4. Jelaskan apa yang dimaksud dengan proses Kuantisasi Model (*Quantization*) dari Float32 menjadi Int8 dalam kerangka kerja TinyML! Mengapa kompresi ini memungkinkan model jaringan saraf tiruan berjalan di dalam cip mikrokontroler yang hanya memiliki memori RAM beberapa ratus Kilobyte?
5. Sebuah kelompok tani di daerah pelosok pegunungan ingin memantau kelembapan tanah perkebunan kopi seluas 5 hektar yang tidak terjangkau jaringan internet kabel. Rancanglah arsitektur sistem IoT cerdas hemat energi terpadu (sebutkan jenis sensor, mikrokontroler, protokol telemetri, dan strategi penghematan daya baterai) yang paling tepat untuk memecahkan masalah tersebut!

---

### KUNCI JAWABAN DAN PEMBAHASAN ANALITIS BAB I

**Kunci Pilihan Ganda:**
1. **B** (Perception Layer berinteraksi fisik dengan alam melalui sensor dan aktuator).
2. **B** (Modul Relay Optocoupler bertindak sebagai sakelar pengaman sirkuit daya tinggi).
3. **B** (MQTT memiliki overhead header sangat kecil mulai 2 Byte dan berbasis Publish-Subscribe hemat daya).
4. **C** (Broker MQTT adalah peladen perantara pengatur lalu lintas pesan telemetri).
5. **C** (QoS 2 menjamin paket pesan diterima tepat satu kali / Exactly Once).
6. **B** (Edge AI / TinyML menjalankan inferensi model langsung di perangkat lokal).
7. **C** (Edge AI justru membutuhkan cip mikrokontroler fisik di lapangan untuk mengeksekusi model).
8. **A** (Kuantisasi mengonversi bobot Float32 menjadi Int8 untuk mereduksi ukuran memori).
9. **B** (GPIO adalah General Purpose Input/Output pada mikrokontroler).
10. **B** (Topik MQTT menggunakan tanda garis miring untuk menyusun hierarki lokasi).

**Pembahasan Soal Uraian:**
1. *Request-Response vs Publish-Subscribe:*
   - Pada Request-Response (HTTP), klien harus selalu menginisiasi permintaan secara berulang (*polling*) dan menunggu jawaban server. Sirkuit radio nirkabel harus menyala terus, memboroskan baterai dan kuota.
   - Pada Publish-Subscribe (MQTT), Publisher hanya mengirim data saat terjadi perubahan nilai atau sesuai jadwal berkala ke Broker. Subscriber menerima data secara pasif hanya saat data baru tersedia (*event-driven*). Ini memungkinkan mikrokontroler tidur hemat daya (*deep sleep*) di sela-sela jadwal pengiriman data, sangat efisien mengelola ratusan sensor sekaligus.
2. *Peranan Modul Relay & Bahaya Korsleting:*
   Pin GPIO ESP32 hanya mengeluarkan daya mikro 3,3V DC. Motor pompa air menggunakan listrik 220V AC berkekuatan ratusan Watt dengan lonjakan arus induktif (*back-EMF*) yang besar saat dihidupkan. Modul relay optocoupler menggunakan sinar cahaya LED internal untuk memicu sakelar mekanik, sehingga tidak ada kontak fisik kabel antara listrik 220V dan cip ESP32. Jika dihubungkan langsung tanpa relay, tegangan 220V AC akan seketika membakar habis sirkuit semikonduktor mikrokontroler dan memicu ledakan korsleting.
3. *Edge AI pada Rem Kendaraan Listrik:*
   Sinyal transmisi ke Cloud AI membutuhkan waktu bolak-balik jaringan (*Round-Trip Time* / RTT) berkisar antara 50 hingga 500 milidetik, bahkan bisa detik jika sinyal seluler terganggu. Pada kecepatan 100 km/jam, mobil melaju sejauh hampir 30 meter dalam waktu 1 detik. Jika pengereman bergantung pada respons server awan yang mengalami jeda atau putus koneksi (*timeout*), mobil akan menabrak rintangan sebelum perintah rem tiba. Edge AI mengeksekusi deteksi rintangan secara lokal dalam hitungan di bawah 5 milidetik tanpa butuh internet, menjamin keselamatan mutlak pejalan kaki dan penumpang.
4. *Mekanisme Kuantisasi TinyML:*
   Float32 menggunakan 32 bit (4 byte) untuk setiap angka bobot neuron, membutuhkan memori sangat besar dan unit kalkulasi floating-point (FPU) khusus. Kuantisasi memetakan rentang nilai kontinu Float32 ke rentang bilangan bulat diskret 8-bit (-128 hingga 127). Dengan hanya membutuhkan 1 byte per bobot (reduksi memori 75%), model deep learning yang awalnya berukuran 20 Megabyte dapat menyusut menjadi kurang dari 5 Megabyte, serta dapat dieksekusi secara instan menggunakan instruksi matematika bilangan bulat pada prosesor berdaya rendah.
5. *Rancangan Sistem IoT Ladang Kopi Pelosok:*
   - Sensor: Sensor kelembapan tanah kapasitif tahan korosi (*Capacitive Soil Moisture*) dan sensor suhu udara DHT22.
   - Mikrokontroler: ESP32 berdaya rendah yang dikombinasikan dengan modul pemancar radio nirkabel LoRa (*Long Range*) frekuensi 915 MHz yang mampu menjangkau radius 5-10 kilometer tanpa pulsa seluler.
   - Protokol: Protokol telemetri MQTT yang dialirkan dari LoRa Gateway menuju server lokal.
   - Strategi Hemat Daya: Memanfaatkan panel surya mini (solar cell 5V) dengan baterai LiFePO4, serta mengaktifkan mode tidur lelap (*ESP32 Deep Sleep*): mikrokontroler tidur selama 30 menit (hanya mengonsumsi arus mikroampere), bangun selama 2 detik untuk membaca sensor dan memancarkan data, lalu kembali tidur lelap. Baterai dapat bertahan tanpa henti selama bertahun-tahun.
"""
