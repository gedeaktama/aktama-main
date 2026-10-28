"""
Script Pembuatan Ilustrasi dan Diagram Visual 300 DPI - Kelas XII SMA/SMK (Fase F Akhir)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

import os, shutil
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-12-sma-smk\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 12 SMA-SMK\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

# Copy foto penulis
foto_source = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\Master AI\foto_penulis.jpg"
if os.path.exists(foto_source):
    for target_dir in [local_assets, tot_assets]:
        shutil.copy2(foto_source, os.path.join(target_dir, "foto_penulis.jpg"))
    print("Copied foto_penulis.jpg to Kelas 12 SMA/SMK assets")

def get_fonts():
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 36)
        font_sub = ImageFont.truetype("arialbd.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_small = ImageFont.load_default()
    return font_title, font_sub, font_text, font_small

def save_image(img, filename):
    for base_dir in [local_assets, tot_assets]:
        p = os.path.join(base_dir, filename)
        img.save(p, dpi=(300, 300))
    print(f"Generated illustration: {filename}")

def create_comic_strip(filename, chapter_title, scene1_text, scene2_text, scene3_text):
    w, h = 1800, 750
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    # Header banner
    draw.rectangle([0, 0, w, 80], fill='#0F172A')
    draw.text((w // 2, 40), f"KOMIK PEMBUKA KELAS XII (FASE F AKHIR) - {chapter_title.upper()}", fill='#FFFFFF', font=f_title, anchor='mm')

    panel_w = 540
    panel_h = 600
    y_top = 110

    panels = [
        ("#F8FAFC", "#0284C7", "Panel 1: Titik Masalah Riil", scene1_text),
        ("#F0FDFA", "#0D9488", "Panel 2: Eksplorasi Solusi Sains", scene2_text),
        ("#EFF6FF", "#3B82F6", "Panel 3: Terobosan Terpadu", scene3_text)
    ]

    for idx, (bg_col, border_col, p_title, p_text) in enumerate(panels):
        x_left = 40 + idx * (panel_w + 35)
        draw.rounded_rectangle([x_left, y_top, x_left + panel_w, y_top + panel_h], radius=15, fill=bg_col, outline=border_col, width=3)
        draw.rectangle([x_left, y_top, x_left + panel_w, y_top + 50], fill=border_col)
        draw.text((x_left + panel_w // 2, y_top + 25), p_title, fill='#FFFFFF', font=f_sub, anchor='mm')

        lines = p_text.split('\n')
        curr_y = y_top + 80
        for line in lines:
            if line.startswith("Arya:"):
                draw.text((x_left + 20, curr_y), line, fill='#0369A1', font=f_text)
            elif line.startswith("Dinda:"):
                draw.text((x_left + 20, curr_y), line, fill='#0F766E', font=f_text)
            elif line.startswith("Bagas:"):
                draw.text((x_left + 20, curr_y), line, fill='#1D4ED8', font=f_text)
            else:
                draw.text((x_left + 20, curr_y), line, fill='#334155', font=f_small)
            curr_y += 32

    save_image(img, filename)

def create_diagram_iot_edge_ai():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0D9488')
    draw.text((w // 2, 40), "ARSITEKTUR CYBER-PHYSICAL SYSTEM: IOT & EDGE AI", fill='#FFFFFF', font=f_title, anchor='mm')

    layers = [
        ("1. Perception Layer (Fisik)", "Sensor Kelembapan Tanah, DHT22,\nModul ESP32-CAM, Motor Pompa Air.\nMenjalankan Edge AI TinyML lokal.", "#F0FDFA", "#0D9488"),
        ("2. Network Layer (Protokol)", "Protokol Komunikasi Ringan MQTT\n(Publish/Subscribe) via WiFi/LoRa.\nData telemetri aman terenkripsi.", "#FEF3C7", "#D97706"),
        ("3. Cloud & Application Layer", "Broker MQTT + REST API Backend.\nDashboard analitik Adafruit IO / Web.\nNotifikasi peringatan dini ke petani.", "#EFF6FF", "#2563EB")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(layers):
        x = 60 + idx * 500
        draw.rounded_rectangle([x, 160, x + 460, 680], radius=16, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 160, x + 460, 230], fill=out_c)
        draw.text((x + 230, 195), title, fill='#FFFFFF', font=f_sub, anchor='mm')
        
        dy = 270
        for l in desc.split('\n'):
            draw.text((x + 30, dy), l, fill='#1E293B', font=f_text)
            dy += 40

        if idx < 2:
            ax = x + 465
            draw.line([(ax, 420), (ax + 30, 420)], fill='#0F172A', width=4)
            draw.polygon([(ax + 30, 410), (ax + 40, 420), (ax + 30, 430)], fill='#0F172A')

    # Footer banner
    draw.rounded_rectangle([60, 720, 1540, 810], radius=10, fill='#F8FAFC', outline='#94A3B8', width=2)
    draw.text((w // 2, 765), "Keunggulan Edge AI: Inferensi Instan (Tanpa Latensi), Hemat Bandwidth, Beroperasi Mandiri Tanpa Internet!", fill='#0F172A', font=f_sub, anchor='mm')

    save_image(img, "bab1_diagram_arsitektur_iot_edge_ai.png")

def create_diagram_big_data_5v():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0284C7')
    draw.text((w // 2, 40), "INFOGRAFIS REKAYASA MAHADATA: KARAKTERISTIK 5V BIG DATA", fill='#FFFFFF', font=f_title, anchor='mm')

    v_items = [
        ("VOLUME", "Skala data raksasa:\nTerabyte hingga Petabyte.\nMembutuhkan Data Lake & NoSQL.", "#E0F2FE", "#0284C7"),
        ("VELOCITY", "Laju aliran kilat:\nStreaming sensor real-time,\ntransaksi e-commerce per milidetik.", "#DCFCE7", "#16A34A"),
        ("VARIETY", "Keragaman format:\nData terstruktur (SQL), teks,\naudio spektrogram, & video mentah.", "#FEF3C7", "#D97706"),
        ("VERACITY", "Tingkat keandalan data:\nMenyaring noise, bias data sosial,\ndan disinformasi berita palsu.", "#FEE2E2", "#DC2626"),
        ("VALUE", "Nilai dampak guna:\nWawasan prediktif untuk kebijakan\npublik, kesehatan, & kedaulatan data.", "#F3E8FF", "#9333EA")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(v_items):
        x = 50 + idx * 305
        draw.rounded_rectangle([x, 150, x + 280, 750], radius=14, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 150, x + 280, 220], fill=out_c)
        draw.text((x + 140, 185), title, fill='#FFFFFF', font=f_sub, anchor='mm')
        
        dy = 260
        for l in desc.split('\n'):
            draw.text((x + 20, dy), l, fill='#1E293B', font=f_text)
            dy += 40

    save_image(img, "bab2_infografis_karakteristik_5v_big_data.png")

def create_diagram_deep_learning_cnn():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#4338CA')
    draw.text((w // 2, 40), "ARSITEKTUR DEEP LEARNING: CONVOLUTIONAL NEURAL NETWORK (CNN)", fill='#FFFFFF', font=f_title, anchor='mm')

    stages = [
        ("1. Input Image", "Matriks Piksel RGB\nUkuran: 224 x 224 x 3\nCitra medis / daun padi", "#EEF2FF", "#4F46E5"),
        ("2. Convolution + ReLU", "Filter Kernel menyapu piksel,\nmengekstrak fitur tepi, tekstur.\nAktivasi non-linear ReLU.", "#FEF3C7", "#D97706"),
        ("3. Max Pooling", "Mereduksi dimensi spasial\n(misal ukuran 2x2 stride 2).\nHemat komputasi & anti-geser.", "#F0FDF4", "#16A34A"),
        ("4. Fully Connected (Dense)", "Lapisan neuron terhubung penuh.\nFungsi aktivasi Softmax untuk\nprobabilitas kelas prediksi.", "#FDF2F8", "#DB2777")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(stages):
        x = 60 + idx * 370
        draw.rounded_rectangle([x, 160, x + 340, 660], radius=14, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 160, x + 340, 230], fill=out_c)
        draw.text((x + 170, 195), title, fill='#FFFFFF', font=f_sub, anchor='mm')

        dy = 270
        for l in desc.split('\n'):
            draw.text((x + 20, dy), l, fill='#1E293B', font=f_text)
            dy += 40

        if idx < 3:
            ax = x + 345
            draw.line([(ax, 410), (ax + 20, 410)], fill='#0F172A', width=4)
            draw.polygon([(ax + 20, 400), (ax + 30, 410), (ax + 20, 420)], fill='#0F172A')

    draw.rounded_rectangle([60, 700, 1540, 800], radius=10, fill='#F8FAFC', outline='#94A3B8', width=2)
    draw.text((w // 2, 750), "Transfer Learning: Memanfaatkan bobot model industri (MobileNet / ResNet) untuk efisiensi data & waktu!", fill='#0F172A', font=f_sub, anchor='mm')

    save_image(img, "bab3_diagram_arsitektur_cnn_deep_learning.png")

def create_diagram_capstone_architecture():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#047857')
    draw.text((w // 2, 40), "ARSITEKTUR MULTI-LAPISAN CAPSTONE PROJECT REKAYASA SISTEM TERPADU", fill='#FFFFFF', font=f_title, anchor='mm')

    layers = [
        ("Layer 1: Frontend & User Interface", "Web Dashboard (HTML/JS/Bootstrap) / Mobile App.\nVisualisasi data interaktif & form pemesanan.", "#ECFDF5", "#059669"),
        ("Layer 2: Backend RESTful API Service", "Peladen Python (Flask/FastAPI).\nEndpoint komunikasi JSON, validasi token keamanan.", "#FEF3C7", "#D97706"),
        ("Layer 3: Artificial Intelligence Engine", "Model Deep Learning / Edge AI / NLP Pipeline.\nInferensi cerdas klasifikasi penyakit / sentimen.", "#EFF6FF", "#2563EB"),
        ("Layer 4: Relational & Cloud Database", "Pangkalan data terintegrasi (PostgreSQL / SQLite).\nProteksi Parameterized Query & enkripsi UU PDP.", "#F5F3FF", "#7C3AED")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(layers):
        y = 140 + idx * 165
        draw.rounded_rectangle([80, y, 1520, y + 140], radius=12, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([80, y, 620, y + 140], fill=out_c)
        draw.text((350, y + 70), title, fill='#FFFFFF', font=f_sub, anchor='mm')
        
        dy = y + 45
        for l in desc.split('\n'):
            draw.text((660, dy), l, fill='#1E293B', font=f_text)
            dy += 35

    save_image(img, "bab4_arsitektur_sistem_terintegrasi_capstone.png")

def create_diagram_ai_governance():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0F172A')
    draw.text((w // 2, 40), "PETA TATA KELOLA GLOBAL ETIKA AI & KESIAPAN KARIER DIGITAL", fill='#FFFFFF', font=f_title, anchor='mm')

    # Left: UNESCO & Ethics Pillars
    draw.rounded_rectangle([60, 140, 780, 800], radius=16, fill='#F0FDF4', outline='#059669', width=3)
    draw.rectangle([60, 140, 780, 210], fill='#059669')
    draw.text((420, 175), "STANDAR TATA KELOLA GLOBAL ETIKA AI", fill='#FFFFFF', font=f_sub, anchor='mm')
    
    ethics_lines = [
        "1. Keadilan & Non-Diskriminasi (Fairness):",
        "   Mencegah bias ras, gender, dan status sosial.",
        "",
        "2. Transparansi & Explainable AI (XAI):",
        "   Menolak tirani 'Kotak Hitam' (Black Box).",
        "   Pengguna berhak tahu dasar logika keputusan AI.",
        "",
        "3. Kedaulatan & Perlindungan Data Pribadi:",
        "   Kepatuhan UU PDP No. 27/2022 dan GDPR.",
        "",
        "4. Keberlanjutan Lingkungan (Green AI):",
        "   Efisiensi energi komputasi & jejak karbon peladen.",
        "",
        "5. Pengawasan Manusia (Human-in-the-Loop):",
        "   Keputusan akhir kritis tetap dipegang manusia."
    ]
    ey = 240
    for l in ethics_lines:
        f = f_sub if l.startswith("1.") or l.startswith("2.") or l.startswith("3.") or l.startswith("4.") or l.startswith("5.") else f_small
        col = '#065F46' if l.startswith("1.") or l.startswith("2.") or l.startswith("3.") or l.startswith("4.") or l.startswith("5.") else '#334155'
        draw.text((90, ey), l, fill=col, font=f)
        ey += 35

    # Right: Career Portfolio
    draw.rounded_rectangle([820, 140, 1540, 800], radius=16, fill='#EFF6FF', outline='#2563EB', width=3)
    draw.rectangle([820, 140, 1540, 210], fill='#2563EB')
    draw.text((1180, 175), "PORTOFOLIO PROFESIONAL LULUSAN FASE F", fill='#FFFFFF', font=f_sub, anchor='mm')

    career_lines = [
        "Komponen Portofolio Digital Kelas Dunia:",
        "• Repositori GitHub Terkurasi (Kode Bersih PEP 8)",
        "• Berkas Dokumentasi Teknis README.md Lengkap",
        "• Manifes Dependensi Lingkungan requirements.txt",
        "• Video Demonstrasi Pitching Produk Startup Cerdas",
        "• Poster Ilmiah Capstone Project Terverifikasi Mitra",
        "",
        "Peluang Karier & Pendidikan Tinggi:",
        "- Lanjut Studi S1 Sistem Komputer / Informatika / AI",
        "- Junior Machine Learning & Data Engineer",
        "- Full-Stack Web Service & REST API Developer",
        "- IoT Firmware & Edge AI Specialist",
        "- AI Ethics Auditor & Compliance Officer"
    ]
    cy = 240
    for l in career_lines:
        f = f_sub if l.endswith(":") else f_small
        col = '#1E40AF' if l.endswith(":") or l.startswith("-") else '#334155'
        draw.text((850, cy), l, fill=col, font=f)
        cy += 35

    save_image(img, "bab5_peta_tata_kelola_global_etika_ai.png")

def create_tokoh():
    w, h = 1600, 750
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0F172A')
    draw.text((w // 2, 40), "TRIO TOKOH SAHABAT BELAJAR KKA - FASE F AKHIR (KELAS XII)", fill='#FFFFFF', font=f_title, anchor='mm')

    tokoh = [
        ("Arya", "Arsitek Deep Learning & Sains Data", "#EEF2FF", "#4F46E5", "Keahlian Puncak:\n- Jaringan Saraf Tiruan CNN & Transfer Learning\n- Analisis Mahadata 5V & Klastering K-Means\n- Optimasi Model Green AI Hemat Energi\nKarakter: Visioner, analitis, teliti"),
        ("Dinda", "Pakar Human-Centered AI & Etika", "#ECFDF5", "#059669", "Keahlian Puncak:\n- Audit Etika Algoritma & Explainable AI (XAI)\n- Uji Penerimaan Pengguna Nyata (UAT Mitra)\n- Kepatuhan Hukum UU PDP No. 27/2022\nKarakter: Humanis, berintegritas, kepemimpinan"),
        ("Bagas", "Spesialis IoT Cerdas & Rekayasa Sistem", "#FEF3C7", "#D97706", "Keahlian Puncak:\n- Komputasi Fisik Edge AI & ESP32 Mikrokontroler\n- Protokol Telemetri Nirkabel MQTT & Cloud Broker\n- Integrasi Multi-Lapisan Capstone Project\nKarakter: Tanggap, terampil, solutif")
    ]

    for idx, (name, role, fill_c, out_c, desc) in enumerate(tokoh):
        x = 50 + idx * 520
        draw.rounded_rectangle([x, 130, x + 460, 690], radius=16, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 130, x + 460, 200], fill=out_c)
        draw.text((x + 230, 165), name, fill='#FFFFFF', font=f_sub, anchor='mm')
        draw.text((x + 230, 230), role, fill=out_c, font=f_text, anchor='mm')

        dy = 280
        for l in desc.split('\n'):
            f = f_sub if l.startswith("Keahlian") or l.startswith("Karakter") else f_text
            col = '#0F172A' if l.startswith("Keahlian") or l.startswith("Karakter") else '#334155'
            draw.text((x + 30, dy), l, fill=col, font=f)
            dy += 40

    save_image(img, "gambar_tokoh_sahabat_sma12.png")

def create_cover():
    w, h = 1800, 2600
    img = Image.new('RGB', (w, h), color='#090D16')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    try:
        font_main = ImageFont.truetype("arialbd.ttf", 64)
        font_huge = ImageFont.truetype("arialbd.ttf", 88)
        font_badge = ImageFont.truetype("arialbd.ttf", 40)
        font_author = ImageFont.truetype("arialbd.ttf", 44)
    except:
        font_main = ImageFont.load_default()
        font_huge = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_author = ImageFont.load_default()

    font_sub = f_sub

    # Header tech wave
    draw.rectangle([0, 0, w, 400], fill='#064E3B')
    draw.polygon([(0, 400), (w, 400), (w, 600), (0, 800)], fill='#047857')
    draw.polygon([(0, 800), (w, 600), (w, 750), (0, 950)], fill='#059669', outline=None)

    # Top badges
    draw.rounded_rectangle([100, 80, 750, 160], radius=16, fill='#047857', outline='#FFFFFF', width=3)
    draw.text((425, 120), "KURIKULUM KKA KEMENDIKDASMEN RI", fill='#FFFFFF', font=font_badge, anchor='mm')

    draw.rounded_rectangle([w - 650, 80, w - 100, 160], radius=16, fill='#D97706', outline='#FFFFFF', width=3)
    draw.text((w - 375, 120), "FASE F (KELAS XII)", fill='#FFFFFF', font=font_badge, anchor='mm')

    # Main Titles
    draw.text((w // 2, 450), "KODING DAN", fill='#FFFFFF', font=font_huge, anchor='mm')
    draw.text((w // 2, 570), "KECERDASAN ARTIFISIAL", fill='#34D399', font=font_huge, anchor='mm')

    # Subtitle
    draw.text((w // 2, 700), "UNTUK SMA / MA / SMK KELAS XII", fill='#F1F5F9', font=font_main, anchor='mm')
    draw.text((w // 2, 770), "IOT CERDAS • BIG DATA • DEEP LEARNING • CAPSTONE", fill='#FDE047', font=font_badge, anchor='mm')

    # Center Hero Box
    draw.rounded_rectangle([120, 950, w - 120, 1950], radius=24, fill='#111827', outline='#059669', width=4)
    
    features = [
        "Puncak Eksplorasi Fase F Tingkat Akhir:",
        "• Komputasi Fisik Cerdas: Internet of Things (IoT) & Edge AI Mikrokontroler",
        "• Protokol Telemetri Ringan MQTT Publish-Subscribe & Cloud Broker",
        "• Rekayasa Mahadata (Big Data 5V) & Algoritma Klastering K-Means",
        "• Jaringan Saraf Tiruan Deep Learning & Convolutional Neural Network (CNN)",
        "• Efisiensi Komputasi Melalui Transfer Learning (MobileNet / ResNet)",
        "• Capstone Project Terpadu Multi-Lapisan Bermitra Industri / Masyarakat",
        "• Tata Kelola Global Etika AI (UNESCO) & Portofolio Profesional Lulusan"
    ]
    fy = 1040
    for l in features:
        draw.text((180, fy), l, fill='#FFFFFF' if l.startswith("Puncak") else '#34D399', font=font_sub)
        fy += 105

    # Author banner
    draw.rectangle([0, 2050, w, 2350], fill='#064E3B')
    draw.text((w // 2, 2140), "Gede Erik Aktama, S.Pd., M.Pd.", fill='#FFFFFF', font=font_author, anchor='mm')
    draw.text((w // 2, 2220), "Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", fill='#A7F3D0', font=font_sub, anchor='mm')
    draw.text((w // 2, 2280), "Fasilitator Nasional Pelatihan KKA Kemendikdasmen RI", fill='#FDE047', font=font_sub, anchor='mm')

    # Footer
    draw.text((w // 2, 2480), "EDISI STANDAR INTERNASIONAL UNESCO (15,5 cm x 23,0 cm)", fill='#9CA3AF', font=font_badge, anchor='mm')

    save_image(img, "cover_buku_siswa_sma12.jpg")

print("Starting visual assets generation for Grade 12 SMA/SMK...")

# Comics for 5 Chapters
create_comic_strip("bab1_komik_pembuka_sma12.png", "Bab I: IoT Cerdas & Edge AI",
    "Bagas:\n'Sensor kelembapan tanah di ladang\npetani sering mati karena baterai\nhabis dan sinyal internet lemah!'",
    "Arya:\n'Protokol HTTP terlalu boros data!\nKita butuh MQTT Publish-Subscribe\nyang super hemat daya baterai!'",
    "Dinda:\n'Dan kita tanamkan model AI langsung\ndi mikrokontroler (Edge AI)!\nSistem mandiri tanpa internet!'")

create_comic_strip("bab2_komik_pembuka_sma12.png", "Bab II: Mahadata & Klastering",
    "Arya:\n'Data log sensor lingkungan kita\nsudah mencapai jutaan baris!\nKomputer biasa mulai kewalahan!'",
    "Dinda:\n'Inilah era Big Data 5V!\nVolume raksasa dan laju Velocity\nyang menuntut arsitektur NoSQL!'",
    "Bagas:\n'Dan algoritma K-Means menemukan\nkelompok klaster tersembunyi\nsecara mandiri tanpa label!'")

create_comic_strip("bab3_komik_pembuka_sma12.png", "Bab III: Deep Learning & CNN",
    "Dinda:\n'Bagaimana mobil otonom dan sistem\nmedis mengenali citra secara instan\ntanpa ekstraksi fitur manual?'",
    "Arya:\n'Jawabannya adalah Deep Learning!\nLapisan konvolusi dan pooling CNN\nmengekstrak pola visual mandiri!'",
    "Bagas:\n'Dan dengan Transfer Learning,\nkita bisa pakai bobot model canggih\ndunia untuk memecahkan masalah lokal!'")

create_comic_strip("bab4_komik_pembuka_sma12.png", "Bab IV: Capstone Project Mitra Industri",
    "Bagas:\n'Saatnya menyatukan seluruh ilmu kita:\nhardware IoT, database API, dan AI\nmenjadi produk utuh untuk warga!'",
    "Dinda:\n'Bukan sekadar simulasi kelas,\nkita uji langsung di balai desa (UAT)\nbersama petani dan UMKM nyata!'",
    "Arya:\n'Integritas dan keselamatan pengguna\nadalah hukum tertinggi inovator!\nMari tuntaskan Capstone kita!'")

create_comic_strip("bab5_komik_pembuka_sma12.png", "Bab V: Tata Kelola Global & Karier",
    "Arya:\n'Setelah 3 tahun belajar koding dan AI,\nbagaimana kita bersiap melangkah\nke dunia industri dan universitas?'",
    "Dinda:\n'Kita susun portofolio GitHub rapi\ndan tegakkan rekomendasi etika AI\nUNESCO: adil, transparan, dan humanis!'",
    "Bagas:\n'Kita buktikan talenta muda Indonesia\nsiap memimpin peradaban digital dunia!\nSelamat berjuang, kawan-kawan!'")

# Diagrams
create_diagram_iot_edge_ai()
create_diagram_big_data_5v()
create_diagram_deep_learning_cnn()
create_diagram_capstone_architecture()
create_diagram_ai_governance()
create_tokoh()
create_cover()

print("All visual assets for Grade 12 SMA/SMK successfully generated!")
