# -*- coding: utf-8 -*-
"""
Professional Educational Textbook Illustration Generator (Clean Vector Style, 300 DPI)
Koding & Kecerdasan Artifisial Kelas 5 SD - Standar Pusbuk Kemendikdasmen
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

tot_dir = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\assets"
local_dir = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd\assets"

os.makedirs(tot_dir, exist_ok=True)
os.makedirs(local_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def save_fig(fig, filename):
    local_path = os.path.join(local_dir, filename)
    fig.savefig(local_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    tot_path = os.path.join(tot_dir, filename)
    try:
        shutil.copy2(local_path, tot_path)
    except Exception as e:
        print(f"Warning copying {filename} to OneDrive: {e}")
    print(f"Vector Illustration Ready: {filename}")

# 1. Tokoh Sahabat Belajar
def make_tokoh():
    fig, ax = plt.subplots(figsize=(8, 3.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8); ax.set_ylim(0, 3.2); ax.axis('off')

    bg = patches.FancyBboxPatch((0.2, 0.2), 7.6, 2.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5)
    ax.add_patch(bg)
    ax.text(4, 2.7, "SAHABAT BELAJAR KODING & KECERDASAN ARTIFISIAL KELAS 5",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1E293B')

    chars = [
        {"name": "ERIK", "title": "[ Tokoh Murid ]", "desc": "Penuh semangat,\nsuka merakit logika &\nbereksperimen.", "col": "#0284C7", "bg": "#E0F2FE", "x": 1.2},
        {"name": "SITI", "title": "[ Tokoh Murid ]", "desc": "Teliti dan tekun,\nsuka merawat tanaman\n& gambar digital.", "col": "#0D9488", "bg": "#CCFBF1", "x": 3.0},
        {"name": "MADE", "title": "[ Tokoh Murid ]", "desc": "Lincah & kreatif,\npandai menari daerah\n& ide-ide segar.", "col": "#D97706", "bg": "#FEF3C7", "x": 4.8},
        {"name": "ROBOT KIBO", "title": "[ Maskot Belajar ]", "desc": "Robot asisten cerdas,\nramah, setia memandu\nkoder cilik.", "col": "#7C3AED", "bg": "#EDE9FE", "x": 6.6},
    ]

    for c in chars:
        x = c["x"]
        circle = patches.Circle((x, 1.8), 0.5, facecolor=c["bg"], edgecolor=c["col"], linewidth=2.5)
        ax.add_patch(circle)
        ax.text(x, 1.8, c["name"][:1], ha='center', va='center', fontsize=20, fontweight='bold', color=c["col"])
        ax.text(x, 1.15, c["name"], ha='center', va='center', fontsize=10, fontweight='bold', color=c["col"])
        ax.text(x, 0.92, c["title"], ha='center', va='center', fontsize=7.5, color='#64748B')
        ax.text(x, 0.55, c["desc"], ha='center', va='center', fontsize=7.2, color='#334155')

    save_fig(fig, "gambar_tokoh_sahabat.png")

# 2. Gambar 1.1: 4 Pilar BK
def make_pilar_bk():
    fig, ax = plt.subplots(figsize=(8.2, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.2); ax.axis('off')

    ax.text(4.1, 3.85, "EMPAT PILAR BERPIKIR KOMPUTASIONAL (COMPUTATIONAL THINKING)",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#0F172A')

    pillars = [
        {"title": "DEKOMPOSISI", "sub": "Memecah Masalah", "desc": "Memecah tugas besar\ndan rumit menjadi\nbagian kecil yang\nmudah dikelola.", "col": "#0284C7", "bg": "#F0F9FF", "x": 1.1},
        {"title": "PENGENALAN POLA", "sub": "Mencari Kesamaan", "desc": "Menemukan pola atau\nketeraturan berulang\npada masalah untuk\nmenentukan solusi.", "col": "#0D9488", "bg": "#F0FDFA", "x": 3.1},
        {"title": "ABSTRAKSI", "sub": "Memilah Informasi", "desc": "Fokus pada informasi\nesensial dan penting,\nmengabaikan rincian\nyang tidak perlu.", "col": "#D97706", "bg": "#FFFBEB", "x": 5.1},
        {"title": "ALGORITMA", "sub": "Langkah Terurut", "desc": "Menyusun urutan\ninstruksi logis yang\nruntut dan teratur\nsampai selesai.", "col": "#7C3AED", "bg": "#F5F3FF", "x": 7.1},
    ]

    for p in pillars:
        x = p["x"]
        box = patches.FancyBboxPatch((x - 0.9, 0.4), 1.8, 3.05, boxstyle="round,pad=0.08,rounding_size=0.15",
                                     facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(box)
        hdr = patches.FancyBboxPatch((x - 0.9, 2.85), 1.8, 0.6, boxstyle="round,pad=0.04,rounding_size=0.1",
                                     facecolor=p["col"], edgecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(x, 3.15, p["title"], ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')
        ax.text(x, 2.5, f'"{p["sub"]}"', ha='center', va='center', fontsize=8, fontstyle='italic', color=p["col"])
        ax.text(x, 1.45, p["desc"], ha='center', va='center', fontsize=7.8, color='#1E293B')

    save_fig(fig, "gambar_1_1_pilar_bk.png")

# 3. Gambar 1.2: Flowchart Algoritma
def make_flowchart():
    fig, ax = plt.subplots(figsize=(7, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 7); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(3.5, 4.3, "BAGAN ALIR (FLOWCHART): ALGORITMA MENCUCI TANGAN 6 LANGKAH",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')

    steps = [
        {"text": "MULAI (START)", "shape": "oval", "col": "#059669", "text_col": "#FFFFFF", "y": 3.65},
        {"text": "Basahi Tangan dengan Air Mengalir", "shape": "rect", "col": "#E0F2FE", "text_col": "#0369A1", "y": 2.85},
        {"text": "Tuang Sabun & Gosok Telapak, Punggung, Sela Jari (20 Detik)", "shape": "rect", "col": "#E0F2FE", "text_col": "#0369A1", "y": 2.05},
        {"text": "Bilas dengan Air Bersih & Keringkan", "shape": "rect", "col": "#E0F2FE", "text_col": "#0369A1", "y": 1.25},
        {"text": "SELESAI (FINISH)", "shape": "oval", "col": "#DC2626", "text_col": "#FFFFFF", "y": 0.45},
    ]

    for i, s in enumerate(steps):
        y = s["y"]
        if s["shape"] == "oval":
            p = patches.FancyBboxPatch((2.2, y), 2.6, 0.42, boxstyle="round,pad=0.05,rounding_size=0.2",
                                       facecolor=s["col"], edgecolor=s["col"])
        else:
            p = patches.Rectangle((1.6, y), 3.8, 0.42, facecolor=s["col"], edgecolor='#0284C7', linewidth=1.5)
        ax.add_patch(p)
        ax.text(3.5, y + 0.21, s["text"], ha='center', va='center', fontsize=8, fontweight='bold', color=s["text_col"])

        if i < len(steps) - 1:
            ax.annotate('', xy=(3.5, y - 0.35), xytext=(3.5, y),
                        arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=1.5, headwidth=5))

    ax.text(5.6, 3.65, "<- Simbol Oval:\nAwal & Akhir", fontsize=7, color='#475569')
    ax.text(5.6, 2.05, "<- Simbol Persegi:\nProses / Tindakan", fontsize=7, color='#475569')

    save_fig(fig, "gambar_1_2_flowchart_algoritma.png")

# 4. Gambar 1.3: Labirin Rute Kibo
def make_labirin():
    fig, ax = plt.subplots(figsize=(6.5, 4.8), facecolor='#F8FAFC')
    ax.set_xlim(0, 6.5); ax.set_ylim(0, 4.8); ax.axis('off')

    ax.text(3.25, 4.5, "PETA LABIRIN ALGORITMA ROBOT KIBO (GRID 5x5)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    ox, oy = 0.8, 0.5
    cs = 0.72
    for r in range(5):
        for c in range(5):
            x = ox + c * cs
            y = oy + (4 - r) * cs
            rect = patches.Rectangle((x, y), cs, cs, facecolor='#FFFFFF', edgecolor='#94A3B8', linewidth=1.2)
            ax.add_patch(rect)
            ax.text(x + 0.12, y + cs - 0.15, f"{c+1},{5-r}", fontsize=6, color='#CBD5E1')

    # Obstacles
    for r, c in [(1, 2), (3, 1), (2, 3)]:
        x = ox + c * cs; y = oy + (4 - r) * cs
        ax.add_patch(patches.Rectangle((x+0.05, y+0.05), cs-0.1, cs-0.1, facecolor='#E2E8F0', edgecolor='#64748B'))
        ax.text(x + cs/2, y + cs/2, "BATU", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#475569')

    # Trash
    for r, c in [(0, 3), (3, 4)]:
        x = ox + c * cs; y = oy + (4 - r) * cs
        ax.add_patch(patches.Circle((x + cs/2, y + cs/2), 0.22, facecolor='#FEF08A', edgecolor='#CA8A04'))
        ax.text(x + cs/2, y + cs/2, "SAMPAH", ha='center', va='center', fontsize=6, fontweight='bold', color='#854D0E')

    # Start
    sx = ox + 0 * cs; sy = oy + (4 - 4) * cs
    ax.add_patch(patches.Rectangle((sx+0.05, sy+0.05), cs-0.1, cs-0.1, facecolor='#EDE9FE', edgecolor='#7C3AED', linewidth=2))
    ax.text(sx + cs/2, sy + cs/2, "KIBO\n(START)", ha='center', va='center', fontsize=7, fontweight='bold', color='#7C3AED')

    # Goal
    gx = ox + 4 * cs; gy = oy + (4 - 0) * cs
    ax.add_patch(patches.Rectangle((gx+0.05, gy+0.05), cs-0.1, cs-0.1, facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=2))
    ax.text(gx + cs/2, gy + cs/2, "TONG\n(GOAL)", ha='center', va='center', fontsize=7, fontweight='bold', color='#16A34A')

    # Instructions
    ax.text(4.7, 3.8, "PETUNJUK KODING:", fontsize=8, fontweight='bold', color='#1E293B')
    ax.text(4.7, 3.4, "[ MAJU ] = 1 Kotak\n[ BELOK KIRI ] = Putar 90\n[ BELOK KANAN ] = Putar 90\n[ AMBIL ] = Pungut Sampah", fontsize=7.2, color='#334155')

    save_fig(fig, "gambar_1_3_labirin_unplugged.png")

# 5. Gambar 2.1: Anatomi Komputer
def make_anatomi():
    fig, ax = plt.subplots(figsize=(8.2, 4.3), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.3); ax.axis('off')

    ax.text(4.1, 4.0, "ARSITEKTUR SISTEM KOMPUTER (TRITUNGGAL: HARDWARE, SOFTWARE, BRAINWARE)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    boxes = [
        {"title": "1. PERANGKAT MASUKAN\n(Input Device)", "col": "#0284C7", "bg": "#F0F9FF",
         "items": "• Keyboard (Papan Ketik)\n• Mouse (Tetikus)\n• Mikrofon (Perekam Suara)\n• Kamera / Scanner", "x": 1.1},
        {"title": "2. PERANGKAT PEMROSES\n(CPU / Otak Utama)", "col": "#7C3AED", "bg": "#F5F3FF",
         "items": "• Central Processing Unit\n• Menghitung Logika & Data\n• Mengatur Semua Alat\n• Kecepatan Tinggi", "x": 3.1},
        {"title": "3. PERANGKAT KELUARAN\n(Output Device)", "col": "#059669", "bg": "#F0FDF4",
         "items": "• Monitor (Layar Tampilan)\n• Speaker / Headphone\n• Printer (Cetak Kertas)\n• Proyektor Layar", "x": 5.1},
        {"title": "4. MEDIA PENYIMPANAN\n(Storage Device)", "col": "#D97706", "bg": "#FFFBEB",
         "items": "• Flashdisk Portabel USB\n• Harddisk Internal / SSD\n• Kartu Memori SD\n• Penyimpanan Awan", "x": 7.1},
    ]

    for b in boxes:
        x = b["x"]
        card = patches.FancyBboxPatch((x - 0.9, 0.8), 1.8, 2.9, boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=b["bg"], edgecolor=b["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(x, 3.25, b["title"], ha='center', va='center', fontsize=7.5, fontweight='bold', color=b["col"])
        ax.text(x, 1.8, b["items"], ha='center', va='center', fontsize=7.2, color='#1E293B')

    bot = patches.FancyBboxPatch((0.2, 0.15), 7.8, 0.55, boxstyle="round,pad=0.04,rounding_size=0.1",
                                 facecolor='#1E293B', edgecolor='#0F172A')
    ax.add_patch(bot)
    ax.text(4.1, 0.42, "SOFTWARE (Sistem Windows, Aplikasi Scratch, Paint)  +  BRAINWARE (Manusia Pengguna & Pemrogram)",
            ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "gambar_2_1_anatomi_komputer.png")

# 6. Gambar 2.2: Ergonomi Duduk & Aturan 20-20-20
def make_ergonomi():
    fig, ax = plt.subplots(figsize=(8, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8); ax.set_ylim(0, 4.0); ax.axis('off')

    ax.text(4, 3.7, "PANDUAN KESEHATAN DIGITAL: POSISI DUDUK ERGONOMIS & SENAM MATA",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Left
    b1 = patches.FancyBboxPatch((0.3, 0.4), 3.5, 3.0, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=2)
    ax.add_patch(b1)
    ax.text(2.05, 3.05, "[ POSISI DUDUK BENAR ]", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803D')
    t1 = (
        "1. Punggung tegak menempel sandaran kursi.\n"
        "2. Jarak mata ke monitor 50 - 70 cm.\n"
        "3. Layar sejajar atau sedikit di bawah mata.\n"
        "4. Siku tangan menekuk 90 derajat rileks.\n"
        "5. Telapak kaki menapak rata di lantai."
    )
    ax.text(2.05, 1.65, t1, ha='center', va='center', fontsize=7.8, color='#1E293B')

    # Right
    b2 = patches.FancyBboxPatch((4.2, 0.4), 3.5, 3.0, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2)
    ax.add_patch(b2)
    ax.text(5.95, 3.05, "[ ATURAN MATA 20 - 20 - 20 ]", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1D4ED8')
    t2 = (
        "Setiap menatap layar gawai:\n"
        "->  20 MENIT  <-\n\n"
        "Istirahatkan mata melihat objek jauh:\n"
        "->  20 KAKI (6 METER)  <-\n\n"
        "Kedipkan mata dengan rileks selama:\n"
        "->  20 DETIK  <-"
    )
    ax.text(5.95, 1.65, t2, ha='center', va='center', fontsize=7.8, color='#1E293B')

    save_fig(fig, "gambar_2_2_ergonomi_duduk.png")

# 7. Gambar 3.1: Keamanan Data & Sandi
def make_keamanan():
    fig, ax = plt.subplots(figsize=(8, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8); ax.set_ylim(0, 4.0); ax.axis('off')

    ax.text(4, 3.7, "PERISAI KEAMANAN DATA PRIBADI & RUMUS KATA SANDI KUAT",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Left: Rahasia
    b1 = patches.FancyBboxPatch((0.3, 0.4), 3.5, 3.0, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(b1)
    ax.text(2.05, 3.05, "[ DATA PRIBADI: RAHASIA / PRIVATE ]", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B91C1C')
    t1 = (
        "• Kata Sandi (Password) Akun\n"
        "• Kode OTP SMS dari Aplikasi/Bank\n"
        "• Nomor Induk Kependudukan (NIK)\n"
        "• Nama Lengkap Ibu Kandung\n"
        "• Alamat Lengkap Rumah & Nomor HP\n"
        "• Lokasi Langsung (Live Location)"
    )
    ax.text(2.05, 1.65, t1, ha='center', va='center', fontsize=7.8, color='#1E293B')

    # Right: Formula
    b2 = patches.FancyBboxPatch((4.2, 0.4), 3.5, 3.0, boxstyle="round,pad=0.08,rounding_size=0.15",
                                facecolor='#FFFBEB', edgecolor='#D97706', linewidth=2)
    ax.add_patch(b2)
    ax.text(5.95, 3.05, "[ FORMULA KATA SANDI AMAN ]", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')
    t2 = (
        "1. Ambil kalimat kesukaanmu:\n"
        "   \"Aku Suka Koding di Sekolah\"\n\n"
        "2. Ambil huruf awal + angka + simbol:\n"
        "   ==>  AsKdS#2025!  <==\n\n"
        "Kombinasi Huruf Besar, Kecil, Angka, Simbol.\n"
        "Panjang Minimal 8 - 12 Karakter."
    )
    ax.text(5.95, 1.65, t2, ha='center', va='center', fontsize=7.6, color='#1E293B')

    save_fig(fig, "gambar_3_1_perisai_keamanan_data.png")

# 8. Gambar 4.1: Sensor AI vs Pancaindra
def make_sensor():
    fig, ax = plt.subplots(figsize=(7.8, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 7.8); ax.set_ylim(0, 4.0); ax.axis('off')

    ax.text(3.9, 3.7, "BAGAIMANA CARA KECERDASAN ARTIFISIAL MELIHAT DAN MENDENGAR?",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')

    rows = [
        {"human": "MATA MANUSIA\nMelihat Cahaya & Objek Fisik", "sensor": "SENSOR KAMERA\nMenangkap Piksel Citra Digital", "tech": "Computer Vision", "col": "#0284C7", "y": 2.5},
        {"human": "TELINGA MANUSIA\nMendengar Gelombang Suara", "sensor": "MIKROFON DIGITAL\nMerekam Frekuensi Akustik", "tech": "Voice Recognition", "col": "#059669", "y": 1.5},
        {"human": "KULIT / TANGAN\nMerasakan Sentuhan Fisik", "sensor": "LAYAR SENTUH\nMendeteksi Koordinat Sentuh", "tech": "Touch Sensor", "col": "#D97706", "y": 0.5},
    ]

    for r in rows:
        y = r["y"]
        ax.add_patch(patches.Rectangle((0.4, y), 2.5, 0.75, facecolor='#FFFFFF', edgecolor=r["col"], linewidth=1.5))
        ax.text(1.65, y + 0.38, r["human"], ha='center', va='center', fontsize=7.2, color='#1E293B')
        ax.annotate('', xy=(4.6, y + 0.38), xytext=(3.1, y + 0.38),
                    arrowprops=dict(facecolor=r["col"], edgecolor=r["col"], width=1.5, headwidth=5))
        ax.text(3.85, y + 0.52, "Ditiru AI", ha='center', va='center', fontsize=6.5, color=r["col"])
        ax.add_patch(patches.Rectangle((4.8, y), 2.6, 0.75, facecolor='#FFFFFF', edgecolor=r["col"], linewidth=1.5))
        ax.text(6.1, y + 0.38, r["sensor"], ha='center', va='center', fontsize=7.2, color='#1E293B')

    save_fig(fig, "gambar_4_1_sensor_vs_pancaindra.png")

# 9. Gambar 5.1: Alur Kerja Google Teachable Machine
def make_teachable():
    fig, ax = plt.subplots(figsize=(8.2, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.0); ax.axis('off')

    ax.text(4.1, 3.7, "ALUR KERJA EKSPERIMEN AI: GOOGLE TEACHABLE MACHINE",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    steps = [
        {"num": "1", "title": "KUMPUL DATA", "sub": "(Gather Data)", "desc": "Merekam 30+ foto\nobjek per kelas\n(Botol vs Kardus).", "col": "#0284C7", "x": 1.1},
        {"num": "2", "title": "LATIH MODEL", "sub": "(Train Model)", "desc": "Klik Train Model.\nKomputer mencari pola\ndan fitur pembeda.", "col": "#7C3AED", "x": 3.1},
        {"num": "3", "title": "UJI PREDIKSI", "sub": "(Test / Preview)", "desc": "Tunjukkan benda baru\nke webcam. Perhatikan\nConfidence Score.", "col": "#059669", "x": 5.1},
        {"num": "4", "title": "ATASI BIAS", "sub": "(Retrain)", "desc": "Bila AI salah tebak,\ntambah variasi foto\ndan latih ulang.", "col": "#D97706", "x": 7.1},
    ]

    for s in steps:
        x = s["x"]
        card = patches.FancyBboxPatch((x - 0.85, 0.4), 1.7, 2.9, boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor='#FFFFFF', edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        circle = patches.Circle((x, 2.9), 0.25, facecolor=s["col"])
        ax.add_patch(circle)
        ax.text(x, 2.9, s["num"], ha='center', va='center', fontsize=10, fontweight='bold', color='#FFFFFF')
        ax.text(x, 2.3, s["title"], ha='center', va='center', fontsize=8, fontweight='bold', color=s["col"])
        ax.text(x, 2.0, s["sub"], ha='center', va='center', fontsize=7, fontstyle='italic', color='#64748B')
        ax.text(x, 1.15, s["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B')

    for ax_x in [2.15, 4.15, 6.15]:
        ax.annotate('', xy=(ax_x + 0.1, 1.8), xytext=(ax_x - 0.1, 1.8),
                    arrowprops=dict(facecolor='#64748B', edgecolor='#64748B', width=1.5, headwidth=5))

    save_fig(fig, "gambar_5_1_siklus_machine_learning.png")

# 10. Gambar 6.1: Antarmuka Scratch
def make_scratch():
    fig, ax = plt.subplots(figsize=(8.2, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.4); ax.axis('off')

    ax.text(4.1, 4.15, "ANTARMUKA STUDIO KODING BLOK VISUAL: SCRATCH",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Top Bar
    ax.add_patch(patches.Rectangle((0.3, 3.6), 7.6, 0.32, facecolor='#4D97FE', edgecolor='#2563EB'))
    ax.text(0.5, 3.76, "SCRATCH DESKTOP  |  File   Edit   Tutorial", fontsize=7.5, color='#FFFFFF', fontweight='bold')
    ax.text(7.1, 3.76, "[MULAI HIJAU] [STOP MERAH]", fontsize=6.8, color='#FFFFFF', fontweight='bold')

    # 1. Blocks Palette
    ax.add_patch(patches.Rectangle((0.3, 0.4), 1.7, 3.1, facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5))
    ax.text(1.15, 3.25, "KATEGORI BLOK", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')
    cats = [("Motion (Gerak)", "#4C97FF"), ("Looks (Tampilan)", "#9966FF"),
            ("Sound (Suara)", "#D65CD6"), ("Events (Pemicu)", "#FFBF00"),
            ("Control (Perulangan)", "#FFAB19"), ("Sensing (Sensor)", "#4CBFE6")]
    for i, (cn, col) in enumerate(cats):
        ax.text(0.4, 2.8 - i*0.42, f"[x] {cn}", fontsize=6.8, color=col, fontweight='bold')

    # 2. Scripts Area
    ax.add_patch(patches.Rectangle((2.15, 0.4), 3.1, 3.1, facecolor='#F1F5F9', edgecolor='#94A3B8', linewidth=1.5))
    ax.text(3.7, 3.25, "AREA KERJA SKRIP (KODING)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')

    # Scratch Blocks
    b1 = patches.FancyBboxPatch((2.35, 2.4), 2.4, 0.4, boxstyle="round,pad=0.03,rounding_size=0.1",
                                facecolor='#FFBF00', edgecolor='#D97706')
    ax.add_patch(b1)
    ax.text(3.55, 2.6, "when [Green Flag] clicked", ha='center', va='center', fontsize=7, fontweight='bold', color='#FFFFFF')

    b2 = patches.FancyBboxPatch((2.35, 1.25), 2.7, 1.05, boxstyle="round,pad=0.03,rounding_size=0.1",
                                facecolor='#FFAB19', edgecolor='#B45309')
    ax.add_patch(b2)
    ax.text(3.55, 2.15, "repeat ( 10 )", ha='center', va='center', fontsize=7, fontweight='bold', color='#FFFFFF')

    b3 = patches.FancyBboxPatch((2.55, 1.45), 2.2, 0.38, boxstyle="round,pad=0.03,rounding_size=0.1",
                                facecolor='#4C97FF', edgecolor='#1D4ED8')
    ax.add_patch(b3)
    ax.text(3.65, 1.64, "move ( 10 ) steps", ha='center', va='center', fontsize=7, fontweight='bold', color='#FFFFFF')

    # 3. Stage
    ax.add_patch(patches.Rectangle((5.4, 1.8), 2.5, 1.7, facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=2))
    ax.text(6.65, 3.25, "PANGGUNG (STAGE)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1D4ED8')
    ax.text(6.65, 2.5, "[ KARAKTER KUCING ]\nSprite Beraksi di Sini", ha='center', va='center', fontsize=7.2, color='#475569')

    # 4. Sprites Info
    ax.add_patch(patches.Rectangle((5.4, 0.4), 2.5, 1.25, facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5))
    ax.text(6.65, 1.45, "DAFTAR SPRITE & LATAR", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')
    ax.text(6.0, 0.85, "Sprite 1: Kucing", fontsize=7, color='#1E293B')
    ax.text(6.0, 0.55, "Backdrop: Halaman", fontsize=7, color='#1E293B')

    save_fig(fig, "gambar_6_1_antarmuka_scratch.png")

if __name__ == "__main__":
    make_tokoh()
    make_pilar_bk()
    make_flowchart()
    make_labirin()
    make_anatomi()
    make_ergonomi()
    make_keamanan()
    make_sensor()
    make_teachable()
    make_scratch()
    print("ALL 10 VECTOR ILLUSTRATIONS GENERATED SUCCESSFULLY!")
