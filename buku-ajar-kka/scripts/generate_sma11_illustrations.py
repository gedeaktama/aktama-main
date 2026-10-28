"""
Script Pembuatan Ilustrasi dan Diagram Visual 300 DPI - Kelas XI SMA/SMK (Fase F)
Buku Koding dan Kecerdasan Artifisial (KKA)
Penulis: Gede Erik Aktama, S.Pd., M.Pd.
"""

import os, shutil
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-11-sma-smk\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 11 SMA-SMK\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

# Copy foto penulis
foto_source = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\Master AI\foto_penulis.jpg"
if os.path.exists(foto_source):
    for target_dir in [local_assets, tot_assets]:
        shutil.copy2(foto_source, os.path.join(target_dir, "foto_penulis.jpg"))
    print("Copied foto_penulis.jpg to Kelas 11 SMA/SMK assets")

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
    draw.rectangle([0, 0, w, 80], fill='#0284C7')
    draw.text((w // 2, 40), f"KOMIK PEMBUKA KELAS XI (FASE F) - {chapter_title.upper()}", fill='#FFFFFF', font=f_title, anchor='mm')

    # 3 Panels
    panel_w = 540
    panel_h = 600
    y_top = 110

    panels = [
        ("#F0F9FF", "#0284C7", "Panel 1: Eksplorasi Masalah", scene1_text),
        ("#F8FAFC", "#0D9488", "Panel 2: Investigasi & Diskusi", scene2_text),
        ("#EFF6FF", "#3B82F6", "Panel 3: Solusi Komputasional", scene3_text)
    ]

    for idx, (bg_col, border_col, p_title, p_text) in enumerate(panels):
        x_left = 40 + idx * (panel_w + 35)
        draw.rounded_rectangle([x_left, y_top, x_left + panel_w, y_top + panel_h], radius=15, fill=bg_col, outline=border_col, width=3)
        # Panel header
        draw.rectangle([x_left, y_top, x_left + panel_w, y_top + 50], fill=border_col)
        draw.text((x_left + panel_w // 2, y_top + 25), p_title, fill='#FFFFFF', font=f_sub, anchor='mm')

        # Bubble content
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

def create_diagram_oop_blueprint():
    w, h = 1600, 900
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    # Header
    draw.rectangle([0, 0, w, 80], fill='#0369A1')
    draw.text((w // 2, 40), "PARADIGMA PEMROGRAMAN BERORIENTASI OBJEK (OOP)", fill='#FFFFFF', font=f_title, anchor='mm')

    # Left: Blueprint Class
    draw.rounded_rectangle([60, 130, 680, 830], radius=16, fill='#F0F9FF', outline='#0284C7', width=3)
    draw.rectangle([60, 130, 680, 200], fill='#0284C7')
    draw.text((370, 165), "CETAK BIRU: CLASS 'Karyawan'", fill='#FFFFFF', font=f_sub, anchor='mm')
    
    class_details = [
        "ATRIBUT INSTANS (State):",
        "- nama: String",
        "- gaji_pokok: Integer",
        "- __saldo_rahasia: Integer (Private - Enkapsulasi)",
        "",
        "METODE (Behavior):",
        "+ __init__(nama, gaji_pokok) : Konstruktor",
        "+ hitung_tunjangan() : Integer (Polimorfisme)",
        "+ get_saldo() / set_saldo() : Getter & Setter",
        "",
        "KONSEPSI TIGA PILAR:",
        "1. Enkapsulasi: Proteksi data __saldo",
        "2. Pewarisan (Inheritance): Induk class Manajer",
        "3. Polimorfisme: Override hitung_tunjangan()"
    ]
    cy = 230
    for l in class_details:
        f = f_sub if l.startswith("KONSEPSI") or l.endswith(":") else f_text
        col = '#0369A1' if l.startswith("1.") or l.startswith("2.") or l.startswith("3.") else '#1E293B'
        draw.text((90, cy), l, fill=col, font=f)
        cy += 40

    # Arrow in Middle
    draw.polygon([(720, 480), (840, 480), (840, 450), (900, 500), (840, 550), (840, 520), (720, 520)], fill='#0D9488')
    draw.text((810, 410), "Instansiasi Objek\n(Obj = Class())", fill='#0D9488', font=f_sub, anchor='mm')

    # Right: Objects in Memory
    draw.rounded_rectangle([940, 130, 1540, 830], radius=16, fill='#F8FAFC', outline='#0D9488', width=3)
    draw.rectangle([940, 130, 1540, 200], fill='#0D9488')
    draw.text((1240, 165), "INSTANS OBJEK NYATA DI MEMORI", fill='#FFFFFF', font=f_sub, anchor='mm')

    objects = [
        ("Objek 1: karyawan_1 (Manajer)", "#E0F2FE", "#0284C7", "nama = 'Arya'\ngaji_pokok = Rp15.000.000\ntunjangan = Rp5.000.000 (Overridden)"),
        ("Objek 2: karyawan_2 (Staff)", "#CCFBF1", "#0D9488", "nama = 'Dinda'\ngaji_pokok = Rp8.000.000\ntunjangan = Rp2.000.000 (Standar)"),
        ("Objek 3: karyawan_3 (Teknisi)", "#FEF3C7", "#D97706", "nama = 'Bagas'\ngaji_pokok = Rp8.500.000\ntunjangan = Rp2.500.000 (Standar)")
    ]
    oy = 230
    for name, fill_c, out_c, desc in objects:
        draw.rounded_rectangle([970, oy, 1510, oy + 170], radius=10, fill=fill_c, outline=out_c, width=2)
        draw.text((990, oy + 25), name, fill=out_c, font=f_sub)
        dy = oy + 65
        for dl in desc.split('\n'):
            draw.text((1000, dy), dl, fill='#1E293B', font=f_text)
            dy += 30
        oy += 190

    save_image(img, "bab1_diagram_arsitektur_oop_python.png")

def create_diagram_git_workflow():
    w, h = 1600, 750
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#1E293B')
    draw.text((w // 2, 40), "ALUR KERJA MANAJEMEN VERSI KODE DENGAN GIT & GITHUB", fill='#FFFFFF', font=f_title, anchor='mm')

    stages = [
        ("1. Working Directory", "Berkas aktif lokal yang diedit\noleh programmer di VS Code", "#F1F5F9", "#475569"),
        ("2. Staging Area", "Penyaringan berkas siap commit\n(git add file.py)", "#FEF3C7", "#D97706"),
        ("3. Local Repository", "Riwayat versi tersimpan lokal\n(git commit -m 'Pesan')", "#E0F2FE", "#0284C7"),
        ("4. Remote GitHub", "Repositori awan kolaboratif\n(git push origin main)", "#DCFCE7", "#16A34A")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(stages):
        x = 50 + idx * 380
        draw.rounded_rectangle([x, 180, x + 340, 580], radius=14, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 180, x + 340, 240], fill=out_c)
        draw.text((x + 170, 210), title, fill='#FFFFFF', font=f_sub, anchor='mm')
        
        dy = 280
        for l in desc.split('\n'):
            draw.text((x + 170, dy), l, fill='#1E293B', font=f_text, anchor='mm')
            dy += 40

        # Draw connecting arrows between boxes
        if idx < 3:
            ax = x + 345
            draw.line([(ax, 380), (ax + 30, 380)], fill='#0F172A', width=4)
            draw.polygon([(ax + 30, 370), (ax + 40, 380), (ax + 30, 390)], fill='#0F172A')

    # Bottom notes
    draw.rounded_rectangle([100, 620, 1500, 710], radius=10, fill='#F8FAFC', outline='#94A3B8', width=2)
    draw.text((w // 2, 665), "Kolaborasi Tim: Cabang Branch terpisah -> Pull Request (PR) -> Code Review -> Merge to Main", fill='#0F172A', font=f_sub, anchor='mm')

    save_image(img, "bab1_alur_kerja_git_github_flow.png")

def create_diagram_rest_api():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0F766E')
    draw.text((w // 2, 40), "ARSITEKTUR PERTUKARAN DATA MODERN: REST API & JSON", fill='#FFFFFF', font=f_title, anchor='mm')

    # Left: Client (Mobile/Web)
    draw.rounded_rectangle([60, 150, 480, 750], radius=16, fill='#F0FDFA', outline='#0D9488', width=3)
    draw.rectangle([60, 150, 480, 220], fill='#0D9488')
    draw.text((270, 185), "CLIENT APPLICATION", fill='#FFFFFF', font=f_sub, anchor='mm')
    client_lines = [
        "Perangkat Klien:",
        "- Smartphone App (Flutter/React Native)",
        "- Web Browser (Single Page App)",
        "- Perangkat Cerdas IoT",
        "",
        "Tugas Utama:",
        "1. Mengirim HTTP Request (GET, POST)",
        "2. Menampilkan antarmuka UI/UX",
        "3. Mem-parsing respons JSON"
    ]
    cy = 250
    for l in client_lines:
        draw.text((90, cy), l, fill='#134E4A', font=f_text)
        cy += 40

    # Middle: REST API Bridge & Cloud
    draw.rounded_rectangle([560, 150, 1040, 750], radius=16, fill='#FEF3C7', outline='#D97706', width=3)
    draw.rectangle([560, 150, 1040, 220], fill='#D97706')
    draw.text((800, 185), "REST API SERVICE (Python)", fill='#FFFFFF', font=f_sub, anchor='mm')
    api_lines = [
        "Protokol HTTP / HTTPS:",
        "- GET /api/v1/siswa (Baca data)",
        "- POST /api/v1/siswa (Tambah data)",
        "- PUT /api/v1/siswa/10 (Ubah data)",
        "- DELETE /api/v1/siswa/10 (Hapus)",
        "",
        "Status HTTP Respon:",
        "- 200 OK (Berhasil)",
        "- 201 Created (Data Baru Terbuat)",
        "- 404 Not Found (Data Hilang)",
        "- 500 Server Error (Galat Internal)"
    ]
    cy = 250
    for l in api_lines:
        draw.text((590, cy), l, fill='#78350F', font=f_text)
        cy += 40

    # Right: Database Server
    draw.rounded_rectangle([1120, 150, 1540, 750], radius=16, fill='#EFF6FF', outline='#2563EB', width=3)
    draw.rectangle([1120, 150, 1540, 220], fill='#2563EB')
    draw.text((1330, 185), "DATABASE RELASIONAL", fill='#FFFFFF', font=f_sub, anchor='mm')
    db_lines = [
        "Sistem Penyimpanan:",
        "- MySQL / PostgreSQL / SQLite",
        "",
        "Mekanisme Keamanan:",
        "1. Parameterized Query",
        "   (Tangkal SQL Injection)",
        "2. Password Hashing (Bcrypt)",
        "3. Token Autentikasi (JWT)",
        "",
        "Integritas Referensial:",
        "- Primary Key & Foreign Key"
    ]
    cy = 250
    for l in db_lines:
        draw.text((1150, cy), l, fill='#1E3A8A', font=f_text)
        cy += 40

    save_image(img, "bab2_arsitektur_rest_api_json_pipeline.png")

def create_diagram_ml_pipeline():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#4338CA')
    draw.text((w // 2, 40), "SIKLUS KERJA PIPELINE MACHINE LEARNING TERAPAN", fill='#FFFFFF', font=f_title, anchor='mm')

    steps = [
        ("1. Data Gathering", "Koleksi dataset mentah dari CSV / SQL database", "#EEF2FF", "#4F46E5"),
        ("2. Preprocessing", "Handling missing values, scaling, & encoding", "#F0FDF4", "#16A34A"),
        ("3. Train-Test Split", "Pemisahan data: 80% Latih & 20% Uji Mandiri", "#FEF3C7", "#D97706"),
        ("4. Model Training", "Pelatihan KNN / Decision Tree / Naive Bayes", "#FDF2F8", "#DB2777"),
        ("5. Evaluasi Objektif", "Confusion Matrix (Akurasi, Presisi, Recall)", "#F5F3FF", "#7C3AED"),
        ("6. Deployment Model", "Integrasi model ke aplikasi web / API sistem", "#F0F9FF", "#0284C7")
    ]

    for idx, (title, desc, fill_c, out_c) in enumerate(steps):
        row = idx // 3
        col = idx % 3
        x = 60 + col * 500
        y = 150 + row * 340
        draw.rounded_rectangle([x, y, x + 460, y + 260], radius=14, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, y, x + 460, y + 55], fill=out_c)
        draw.text((x + 230, y + 27), title, fill='#FFFFFF', font=f_sub, anchor='mm')
        
        dy = y + 85
        for l in desc.split('\n'):
            draw.text((x + 30, dy), l, fill='#1E293B', font=f_text)
            dy += 35

    save_image(img, "bab4_alur_kerja_pipeline_machine_learning.png")

def create_diagram_confusion_matrix():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#9333EA')
    draw.text((w // 2, 40), "MATRIKS KONFUSI (CONFUSION MATRIX) & METRIK EVALUASI AI", fill='#FFFFFF', font=f_title, anchor='mm')

    # Grid 2x2
    grid_x, grid_y = 100, 160
    cell_w, cell_h = 320, 240

    # Headers
    draw.text((grid_x + cell_w + cell_w // 2, grid_y - 30), "PREDIKSI: POSITIF", fill='#0F172A', font=f_sub, anchor='mm')
    draw.text((grid_x + cell_w * 2 + cell_w // 2, grid_y - 30), "PREDIKSI: NEGATIF", fill='#0F172A', font=f_sub, anchor='mm')
    draw.text((grid_x + 50, grid_y + cell_h // 2), "AKTUAL:\nPOSITIF", fill='#0F172A', font=f_sub, anchor='mm')
    draw.text((grid_x + 50, grid_y + cell_h + cell_h // 2), "AKTUAL:\nNEGATIF", fill='#0F172A', font=f_sub, anchor='mm')

    # Cells
    # TP (True Positive)
    draw.rectangle([grid_x + 180, grid_y, grid_x + 180 + cell_w, grid_y + cell_h], fill='#DCFCE7', outline='#16A34A', width=3)
    draw.text((grid_x + 180 + cell_w // 2, grid_y + 60), "TRUE POSITIVE (TP)", fill='#166534', font=f_sub, anchor='mm')
    draw.text((grid_x + 180 + cell_w // 2, grid_y + 120), "Aktual Positif\nDiprediksi Positif (Tepat)", fill='#15803D', font=f_text, anchor='mm')

    # FN (False Negative)
    draw.rectangle([grid_x + 180 + cell_w, grid_y, grid_x + 180 + cell_w * 2, grid_y + cell_h], fill='#FEE2E2', outline='#DC2626', width=3)
    draw.text((grid_x + 180 + cell_w + cell_w // 2, grid_y + 60), "FALSE NEGATIVE (FN)", fill='#991B1B', font=f_sub, anchor='mm')
    draw.text((grid_x + 180 + cell_w + cell_w // 2, grid_y + 120), "Aktual Positif\nDiprediksi Negatif (Fatal!)", fill='#B91C1C', font=f_text, anchor='mm')

    # FP (False Positive)
    draw.rectangle([grid_x + 180, grid_y + cell_h, grid_x + 180 + cell_w, grid_y + cell_h * 2], fill='#FEF3C7', outline='#D97706', width=3)
    draw.text((grid_x + 180 + cell_w // 2, grid_y + cell_h + 60), "FALSE POSITIVE (FP)", fill='#92400E', font=f_sub, anchor='mm')
    draw.text((grid_x + 180 + cell_w // 2, grid_y + cell_h + 120), "Aktual Negatif\nDiprediksi Positif (Alarm Palsu)", fill='#B45309', font=f_text, anchor='mm')

    # TN (True Negative)
    draw.rectangle([grid_x + 180 + cell_w, grid_y + cell_h, grid_x + 180 + cell_w * 2, grid_y + cell_h * 2], fill='#E0F2FE', outline='#0284C7', width=3)
    draw.text((grid_x + 180 + cell_w + cell_w // 2, grid_y + cell_h + 60), "TRUE NEGATIVE (TN)", fill='#075985', font=f_sub, anchor='mm')
    draw.text((grid_x + 180 + cell_w + cell_w // 2, grid_y + cell_h + 120), "Aktual Negatif\nDiprediksi Negatif (Tepat)", fill='#0369A1', font=f_text, anchor='mm')

    # Right: Formula Boxes
    draw.rounded_rectangle([920, 160, 1540, 640], radius=14, fill='#F8FAFC', outline='#9333EA', width=2)
    draw.rectangle([920, 160, 1540, 220], fill='#9333EA')
    draw.text((1230, 190), "RUMUS EVALUASI MODEL KLASIFIKASI", fill='#FFFFFF', font=f_sub, anchor='mm')

    formulas = [
        "Akurasi = (TP + TN) / (TP + TN + FP + FN)",
        "-> Mengukur ketepatan total prediksi benar",
        "",
        "Presisi = TP / (TP + FP)",
        "-> Dari semua yang diprediksi Positif, berapa yang benar?",
        "",
        "Recall (Sensitivitas) = TP / (TP + FN)",
        "-> Dari semua kasus Aktual Positif, berapa yang terdeteksi?",
        "",
        "F1-Score = 2 * (Presisi * Recall) / (Presisi + Recall)",
        "-> Rata-rata harmonik penyeimbang Presisi dan Recall"
    ]
    fy = 250
    for l in formulas:
        f = f_sub if l.startswith("Akurasi") or l.startswith("Presisi") or l.startswith("Recall") or l.startswith("F1-Score") else f_small
        col = '#9333EA' if l.startswith("Akurasi") or l.startswith("Presisi") or l.startswith("Recall") or l.startswith("F1-Score") else '#334155'
        draw.text((950, fy), l, fill=col, font=f)
        fy += 36

    save_image(img, "bab4_diagram_matriks_konfusi_evaluasi.png")

def create_diagram_nlp_pipeline():
    w, h = 1600, 850
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0284C7')
    draw.text((w // 2, 40), "PIPELINE PRA-PEMROSESAN TEKS & VEKTORISASI NLP", fill='#FFFFFF', font=f_title, anchor='mm')

    steps = [
        ("Kalimat Asli (Raw Text)", "'Siswa-siswa SANGAT menyukai koding Python di sekolah!'", "#F1F5F9", "#475569"),
        ("1. Case Folding", "'siswa-siswa sangat menyukai koding python di sekolah!'", "#FEF3C7", "#D97706"),
        ("2. Tokenizing", "['siswa-siswa', 'sangat', 'menyukai', 'koding', 'python', 'di', 'sekolah']", "#E0F2FE", "#0284C7"),
        ("3. Stopwords Removal", "['siswa-siswa', 'koding', 'python', 'sekolah'] (hapus 'sangat', 'di')", "#DCFCE7", "#16A34A"),
        ("4. Stemming (Sastrawi)", "['siswa', 'koding', 'python', 'sekolah'] (kembali ke kata dasar)", "#FDF2F8", "#DB2777"),
        ("5. Vektorisasi (TF-IDF)", "Vektor Numerik: [0.45, 0.62, 0.58, 0.31] Siap Diproses Model AI", "#EDE9FE", "#7C3AED")
    ]

    for idx, (title, sample, fill_c, out_c) in enumerate(steps):
        y = 130 + idx * 115
        draw.rounded_rectangle([80, y, 1520, y + 95], radius=10, fill=fill_c, outline=out_c, width=2)
        draw.text((120, y + 25), title, fill=out_c, font=f_sub)
        draw.text((120, y + 60), sample, fill='#1E293B', font=f_text)

    save_image(img, "bab5_diagram_pipeline_nlp_text_processing.png")

def create_cover():
    w, h = 1800, 2600
    img = Image.new('RGB', (w, h), color='#0F172A')
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

    # Decorative shapes (Modern Tech Gradient Style)
    draw.rectangle([0, 0, w, 400], fill='#0369A1')
    draw.polygon([(0, 400), (w, 400), (w, 550), (0, 750)], fill='#0284C7')
    draw.polygon([(0, 750), (w, 550), (w, 700), (0, 900)], fill='#0284C7', outline=None)

    # Top badges
    draw.rounded_rectangle([100, 80, 750, 160], radius=16, fill='#0284C7', outline='#FFFFFF', width=3)
    draw.text((425, 120), "KURIKULUM KKA KEMENDIKDASMEN RI", fill='#FFFFFF', font=font_badge, anchor='mm')

    draw.rounded_rectangle([w - 650, 80, w - 100, 160], radius=16, fill='#10B981', outline='#FFFFFF', width=3)
    draw.text((w - 375, 120), "FASE F (KELAS XI)", fill='#FFFFFF', font=font_badge, anchor='mm')

    # Main Titles
    draw.text((w // 2, 450), "KODING DAN", fill='#FFFFFF', font=font_huge, anchor='mm')
    draw.text((w // 2, 570), "KECERDASAN ARTIFISIAL", fill='#38BDF8', font=font_huge, anchor='mm')

    # Subtitle
    draw.text((w // 2, 700), "UNTUK SMA / MA / SMK KELAS XI", fill='#F1F5F9', font=font_main, anchor='mm')
    draw.text((w // 2, 770), "PEMROGRAMAN OOP • REST API • MACHINE LEARNING • NLP", fill='#FDE047', font=font_badge, anchor='mm')

    # Center Hero Box
    draw.rounded_rectangle([120, 950, w - 120, 1950], radius=24, fill='#1E293B', outline='#0284C7', width=4)
    
    font_sub = f_sub

    # Feature list in Hero Box
    features = [
        "Eksplorasi Pembelajaran Mendalam (Deep Learning):",
        "• Pemrograman Berorientasi Objek (OOP Python: Class, Inheritance, Polymorphism)",
        "• Manajemen Rekayasa Perangkat Lunak Terintegrasi Git & GitHub Kolaboratif",
        "• Basis Data Relasional Tingkat Lanjut, Data Encoding JSON, & REST API",
        "• Pipeline Machine Learning Terapan: Klasifikasi KNN & Decision Tree",
        "• Evaluasi Objektif Model AI: Matriks Konfusi (Akurasi, Presisi, Recall, F1)",
        "• Pemrosesan Bahasa Alami (NLP): Preprocessing, TF-IDF, & Transformer",
        "• Disrupsi Sosio-Teknologi & Standar Etika Pengembang Human-Centered AI"
    ]
    fy = 1040
    for l in features:
        draw.text((180, fy), l, fill='#FFFFFF' if l.startswith("Eksplorasi") else '#38BDF8', font=font_sub)
        fy += 105

    # Author banner
    draw.rectangle([0, 2050, w, 2350], fill='#0F766E')
    draw.text((w // 2, 2140), "Gede Erik Aktama, S.Pd., M.Pd.", fill='#FFFFFF', font=font_author, anchor='mm')
    draw.text((w // 2, 2220), "Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", fill='#CCFBF1', font=font_sub, anchor='mm')
    draw.text((w // 2, 2280), "Fasilitator Nasional Pelatihan KKA Kemendikdasmen RI", fill='#FDE047', font=font_sub, anchor='mm')

    # Footer
    draw.text((w // 2, 2480), "EDISI STANDAR INTERNASIONAL UNESCO (15,5 cm x 23,0 cm)", fill='#94A3B8', font=font_badge, anchor='mm')

    save_image(img, "cover_buku_siswa_sma11.jpg")

def create_tokoh():
    w, h = 1600, 750
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title, f_sub, f_text, f_small = get_fonts()

    draw.rectangle([0, 0, w, 80], fill='#0284C7')
    draw.text((w // 2, 40), "TRIO TOKOH SAHABAT BELAJAR KKA - FASE F (KELAS XI)", fill='#FFFFFF', font=f_title, anchor='mm')

    tokoh = [
        ("Arya", "Peminat Sains Komputasi & AI", "#E0F2FE", "#0284C7", "Fokus Keahlian:\n- Pemrograman OOP Python Lanjut\n- Algoritma Machine Learning (KNN)\n- Perancangan Arsitektur Sistem\nKarakter: Kritis, teliti, matematis"),
        ("Dinda", "Peminat Analisis Sosial & NLP", "#CCFBF1", "#0D9488", "Fokus Keahlian:\n- Pemrosesan Bahasa Alami (NLP)\n- Evaluasi Model Confusion Matrix\n- Etika Human-Centered AI & UU PDP\nKarakter: Humanis, reflektif, etis"),
        ("Bagas", "Peminat RPL & Integrasi Sistem", "#FEF3C7", "#D97706", "Fokus Keahlian:\n- Rekayasa Perangkat Lunak (SDLC)\n- Manajemen Versi Git & GitHub\n- Arsitektur Database & REST API\nKarakter: Praktis, solutif, kolaboratif")
    ]

    for idx, (name, role, fill_c, out_c, desc) in enumerate(tokoh):
        x = 50 + idx * 520
        draw.rounded_rectangle([x, 130, x + 460, 690], radius=16, fill=fill_c, outline=out_c, width=3)
        draw.rectangle([x, 130, x + 460, 200], fill=out_c)
        draw.text((x + 230, 165), name, fill='#FFFFFF', font=f_sub, anchor='mm')
        draw.text((x + 230, 230), role, fill=out_c, font=f_text, anchor='mm')

        dy = 280
        for l in desc.split('\n'):
            f = f_sub if l.startswith("Fokus") or l.startswith("Karakter") else f_text
            col = '#0F172A' if l.startswith("Fokus") or l.startswith("Karakter") else '#334155'
            draw.text((x + 30, dy), l, fill=col, font=f)
            dy += 40

    save_image(img, "gambar_tokoh_sahabat_sma11.png")

print("Starting visual assets generation for Grade 11 SMA/SMK...")

# Comics for 6 Chapters
create_comic_strip("bab1_komik_pembuka_sma11.png", "Bab I: Paradigma OOP & Git",
    "Arya:\n'Program kasir kita mulai kacau\nkarena variabelnya saling tindih!'\nDinda:\n'Kode prosedural kita sudah ribuan\nbaris dan sulit dipelihara!'",
    "Bagas:\n'Kita butuh Class sebagai cetak\nbiru objek nyata di memori!'\nArya:\n'Dan kita wajib pakai Git agar\nkoding bersama tidak bentrok!'",
    "Dinda:\n'Enkapsulasi menjaga data privat,\ndan GitHub menyatukan cabang\nkoding kita secara rapi!'\nBagas:\n'Mari bangun sistem OOP modern!'")

create_comic_strip("bab2_komik_pembuka_sma11.png", "Bab II: Basis Data & REST API",
    "Bagas:\n'Bagaimana aplikasi Android\nkita bisa membaca basis data\ndi server sekolah?'\nArya:\n'Kita butuh jembatan data!'",
    "Dinda:\n'Bukan mengirim file langsung,\nmelainkan melalui format teks\nringan terstandar JSON!'\nBagas:\n'Dan arsitektur REST API!'",
    "Arya:\n'Endpoint GET dan POST dengan\nkeamanan Parameterized Query\nmenangkal serangan siber!'\nDinda:\n'Data aman dan terintegrasi!'")

create_comic_strip("bab3_komik_pembuka_sma11.png", "Bab III: Multimedia & Technical Writing",
    "Dinda:\n'Kode aplikasi kita sangat hebat,\ntetapi teman-teman bingung\ncara memasang dan memakainya!'",
    "Arya:\n'Sebuah proyek belum tuntas\ntanpa dokumentasi teknis rapi\nseperti berkas README.md!'",
    "Bagas:\n'Dan kita butuh slide pitching\nproduk startup untuk demo!\nMari kemas karya kita memukau!'")

create_comic_strip("bab4_komik_pembuka_sma11.png", "Bab IV: Pipeline Machine Learning",
    "Arya:\n'Model AI pendeteksi penyakit\nkita mengklaim akurasi 98%,\ntetapi pasien kanker terlewat!'",
    "Dinda:\n'Hati-hati, Arya! Pada dataset\nyang timpang, metrik Akurasi\nbisa sangat menipu!'",
    "Bagas:\n'Kita wajib pakai Confusion Matrix!\nRecall dan Presisi jauh lebih krusial\ndaripada akurasi semu!'")

create_comic_strip("bab5_komik_pembuka_sma11.png", "Bab V: NLP & Teks Komputasi",
    "Bagas:\n'Mengapa komputer gagal paham\nkalimat ulasan sarkasme di web?'\nDinda:\n'Bahasa manusia kaya makna!'",
    "Arya:\n'Teks harus disaring: buang kata\nsambung, cari kata dasar, lalu diubah\nmenjadi bobot angka TF-IDF!'",
    "Dinda:\n'Dan arsitektur Transformer\nmembaca konteks utuh kalimat!\nMari bedah rahasia NLP!'")

create_comic_strip("bab6_komik_pembuka_sma11.png", "Bab VI: Etika & Dampak Sosio-Teknologi AI",
    "Arya:\n'Apakah AI akan menggantikan\nseluruh profesi manusia kelak?'\nBagas:\n'Pekerjaan repetitif terancam!'",
    "Dinda:\n'AI bukan pengganti, melainkan\npenguat (Augmented Intelligence).\nKunci utamanya ada pada etika!'",
    "Arya:\n'Pengembang wajib transparan\ndan berpihak pada kemanusiaan!\nMari jadi inovator berintegritas!'")

# Diagrams
create_diagram_oop_blueprint()
create_diagram_git_workflow()
create_diagram_rest_api()
create_diagram_ml_pipeline()
create_diagram_confusion_matrix()
create_diagram_nlp_pipeline()
create_tokoh()
create_cover()

print("All visual assets for Grade 11 SMA/SMK successfully generated!")
