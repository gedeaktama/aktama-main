# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Buku KKA Kelas 8 SMP (Fase D)
Resolusi Tinggi 300 DPI, Desain Infografis Edukatif & Komik Remaja,
Modern, Penuh Warna, Sesuai Standar Kemendikdasmen & Kurikulum Nasional.
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-8-smp\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 8 SMP\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

# Copy foto_penulis.jpg from smp7
src_foto = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-7-smp\assets\foto_penulis.jpg"
if os.path.exists(src_foto):
    shutil.copy2(src_foto, os.path.join(local_assets, "foto_penulis.jpg"))
    shutil.copy2(src_foto, os.path.join(tot_assets, "foto_penulis.jpg"))
    print("Copied foto_penulis.jpg to Kelas 8 assets")

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def save_fig(fig, filename):
    local_path = os.path.join(local_assets, filename)
    fig.savefig(local_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    tot_path = os.path.join(tot_assets, filename)
    try:
        shutil.copy2(local_path, tot_path)
    except Exception as e:
        print(f"Warning copying {filename}: {e}")
    print(f"Generated illustration: {filename}")

# -------------------------------------------------------------
# 0. TOKOH SAHABAT BELAJAR KELAS 8 SMP
# -------------------------------------------------------------
def make_tokoh_sahabat():
    fig, ax = plt.subplots(figsize=(8.0, 3.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.6); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 2.9), 7.2, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor='#2563EB', edgecolor='#1D4ED8')
    ax.add_patch(title_box)
    ax.text(4.0, 3.17, "TIGA SAHABAT INOVATOR REMAJA KODING & KA KELAS VIII SMP",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    tokohs = [
        {"nama": "RIAN", "role": "Arsitek Logika Modular", "ciri": "Siswa kritis, gemar merancang fungsi mandiri, game simulasi & clean code", "color": "#2563EB", "bg": "#EFF6FF", "x": 0.5},
        {"nama": "AYU", "role": "Produser Media Digital", "ciri": "Siswi kreatif, produser podcast & editor video edukatif bersuara jernih", "color": "#EA580C", "bg": "#FFF7ED", "x": 3.0},
        {"nama": "FAJAR", "role": "Penyelidik Fusi Sensor & Siber", "ciri": "Siswa analitis, gemar riset sensor drone, data latih & keamanan digital", "color": "#9333EA", "bg": "#FAF5FF", "x": 5.5},
    ]

    for t in tokohs:
        card = patches.FancyBboxPatch((t["x"], 0.25), 2.0, 2.5, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=t["bg"], edgecolor=t["color"], linewidth=2)
        ax.add_patch(card)

        circle = patches.Circle((t["x"] + 1.0, 2.05), 0.5, facecolor=t["color"], edgecolor='#FFFFFF', linewidth=2)
        ax.add_patch(circle)
        ax.text(t["x"] + 1.0, 2.05, t["nama"][0], ha='center', va='center', fontsize=16, fontweight='bold', color='#FFFFFF')

        ax.text(t["x"] + 1.0, 1.35, t["nama"], ha='center', va='center', fontsize=10.5, fontweight='bold', color=t["color"])
        ax.text(t["x"] + 1.0, 1.1, t["role"], ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1E293B')

        ax.text(t["x"] + 1.0, 0.65, t["ciri"], ha='center', va='center', fontsize=7.2, color='#475569', wrap=True,
                multialignment='center')

    save_fig(fig, "gambar_tokoh_sahabat_smp8.png")

# -------------------------------------------------------------
# 1. BAB 1: KOMIK PEMBUKA LOGIKA BERSARANG
# -------------------------------------------------------------
def make_bab1_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#1E40AF', edgecolor='#1E3A8A')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 1: TANTANGAN SIMULASI PEMADAM KEBAKARAN HUTAN",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Kode yang Bertumpuk", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Rian:\n'Aduh! Game simulasi kebakaran ini rumit sekali! Jika ada angin kencang DAN kelembapan rendah, api melonjak. Tapi jika tangki air kosong, helikopter tidak boleh terbang!'",
         "status": "Logika Bertingkat Rumit"},
        {"x": 3.0, "title": "Panel 2: Ide Pemecahan Modular", "bg": "#FFFBEB", "bdr": "#F59E0B",
         "dialog": "Fajar:\n'Jangan tumpuk semua blok dalam satu loop raksasa, Rian! Gunakan Custom Blocks! Buat fungsi khusus [CekStatusBencana] dan [SemprotAir(Volume)]!'",
         "status": "Dekomposisi Fungsi"},
        {"x": 5.6, "title": "Panel 3: Bersih, Rapi & Bekerja", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Ayu:\n'Hebat! Dengan operator AND dan fungsi modular, kodenya mudah dibaca dan game berjalan mulus tanpa lag. Inilah rahasia clean code para programmer profesional!'",
         "status": "Clean Code Berhasil!"}
    ]

    for p in panels:
        box = patches.FancyBboxPatch((p["x"], 0.35), 2.5, 3.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                     facecolor=p["bg"], edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(box)

        lbl = patches.FancyBboxPatch((p["x"]+0.1, 3.85), 2.3, 0.3, boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(lbl)
        ax.text(p["x"]+1.25, 4.0, p["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

        cir = patches.Circle((p["x"]+1.25, 2.95), 0.55, facecolor='#FFFFFF', edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(cir)
        ax.text(p["x"]+1.25, 2.95, "SIMULASI\nKODER", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab1_komik_pembuka_smp8.png")

# -------------------------------------------------------------
# 2. BAB 1: DIAGRAM LOGIKA SAKLAR AND, OR, NOT
# -------------------------------------------------------------
def make_bab1_saklar_and_or():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.85), 7.5, 0.5, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.1, "OPERATOR LOGIKA MAJEMUK DALAM KOMPUTASI: AND, OR, DAN NOT",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    # Card 1: AND (Seri)
    c1 = patches.FancyBboxPatch((0.4, 0.4), 2.4, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=2)
    ax.add_patch(c1)
    ax.text(1.6, 3.3, "LOGIKA 'AND' (SERI)", ha='center', va='center', fontsize=10, fontweight='bold', color='#1E40AF')
    ax.text(1.6, 2.85, "KEDUA kondisi harus BENAR\n(Saklar A = ON dan B = ON)\nagar lampu menyala.", ha='center', va='center', fontsize=7.8, color='#334155')
    # Circuit drawing
    ax.plot([0.7, 1.1, 1.4, 1.8, 2.1, 2.5], [2.1, 2.1, 2.4, 2.1, 2.4, 2.1], color='#2563EB', lw=2)
    ax.text(1.25, 2.55, "A", fontsize=8, fontweight='bold', color='#1E40AF')
    ax.text(1.95, 2.55, "B", fontsize=8, fontweight='bold', color='#1E40AF')
    ax.plot([0.7, 0.7, 2.5, 2.5], [2.1, 1.3, 1.3, 2.1], color='#2563EB', lw=2)
    cir1 = patches.Circle((1.6, 1.3), 0.22, facecolor='#FEF08A', edgecolor='#CA8A04', lw=2)
    ax.add_patch(cir1)
    ax.text(1.6, 1.3, "Lampu", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#854D0E')
    ax.text(1.6, 0.75, "Rumus Scratch / Python:\n(Kondisi A) and (Kondisi B)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1D4ED8')

    # Card 2: OR (Paralel)
    c2 = patches.FancyBboxPatch((3.05, 0.4), 2.4, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFFBEB', edgecolor='#D97706', linewidth=2)
    ax.add_patch(c2)
    ax.text(4.25, 3.3, "LOGIKA 'OR' (PARALEL)", ha='center', va='center', fontsize=10, fontweight='bold', color='#92400E')
    ax.text(4.25, 2.85, "SALAH SATU kondisi BENAR\n(Saklar A atau B ON)\nlampu sudah menyala.", ha='center', va='center', fontsize=7.8, color='#334155')
    # Circuit parallel
    ax.plot([3.35, 3.7, 3.7, 4.0, 4.5, 4.8, 4.8, 5.15], [2.1, 2.1, 2.4, 2.4, 2.4, 2.4, 2.1, 2.1], color='#D97706', lw=2)
    ax.plot([3.7, 4.0, 4.5, 4.8], [1.8, 1.8, 1.8, 1.8], color='#D97706', lw=2)
    ax.text(4.25, 2.55, "A (Atas)", fontsize=7.5, fontweight='bold', color='#B45309')
    ax.text(4.25, 1.6, "B (Bawah)", fontsize=7.5, fontweight='bold', color='#B45309')
    ax.plot([3.35, 3.35, 5.15, 5.15], [2.1, 1.1, 1.1, 2.1], color='#D97706', lw=2)
    cir2 = patches.Circle((4.25, 1.1), 0.22, facecolor='#FEF08A', edgecolor='#CA8A04', lw=2)
    ax.add_patch(cir2)
    ax.text(4.25, 1.1, "Lampu", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#854D0E')
    ax.text(4.25, 0.75, "Rumus Scratch / Python:\n(Kondisi A) or (Kondisi B)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#B45309')

    # Card 3: NOT (Inverter)
    c3 = patches.FancyBboxPatch((5.7, 0.4), 2.4, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#F5F3FF', edgecolor='#7C3AED', linewidth=2)
    ax.add_patch(c3)
    ax.text(6.9, 3.3, "LOGIKA 'NOT' (PEMBALIK)", ha='center', va='center', fontsize=10, fontweight='bold', color='#5B21B6')
    ax.text(6.9, 2.85, "MEMBALIK nilai kebenaran.\nJika Asli = BENAR, hasil SALAH.\nJika Asli = SALAH, hasil BENAR.", ha='center', va='center', fontsize=7.8, color='#334155')
    
    # Inverter symbol
    inv_box = patches.FancyBboxPatch((6.3, 1.7), 1.2, 0.6, boxstyle="square,pad=0.02", facecolor='#DDD6FE', edgecolor='#7C3AED', lw=2)
    ax.add_patch(inv_box)
    ax.text(6.9, 2.0, "NOT (Input)", ha='center', va='center', fontsize=8, fontweight='bold', color='#4C1D95')
    ax.annotate("", xy=(7.7, 2.0), xytext=(7.5, 2.0), arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=2))
    ax.text(6.9, 1.35, "Contoh: not (Tombol Ditekan)\nSangat berguna untuk jeda sensor.", ha='center', va='center', fontsize=7.5, color='#334155')
    ax.text(6.9, 0.75, "Rumus Scratch / Python:\nnot (Kondisi)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#6D28D9')

    save_fig(fig, "bab1_diagram_logika_saklar_and_or.png")

# -------------------------------------------------------------
# 3. BAB 1: STRUKTUR PERCABANGAN NESTED IF
# -------------------------------------------------------------
def make_bab1_nested_if():
    fig, ax = plt.subplots(figsize=(8.5, 4.8), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.8); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.2), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#0369A1', edgecolor='#0284C7')
    ax.add_patch(title)
    ax.text(4.25, 4.42, "DIAGRAM ALUR KEPUTUSAN BERLAPIS: STRUKTUR NESTED IF-ELSE",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    # Start
    start = patches.FancyBboxPatch((3.5, 3.6), 1.5, 0.4, boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor='#10B981', edgecolor='#059669')
    ax.add_patch(start)
    ax.text(4.25, 3.8, "Mulai Evaluasi", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

    ax.annotate("", xy=(4.25, 3.3), xytext=(4.25, 3.6), arrowprops=dict(arrowstyle="->", color='#0369A1', lw=2))

    # Condition 1: Diamond
    dia1 = patches.Polygon([[4.25, 3.3], [5.6, 2.7], [4.25, 2.1], [2.9, 2.7]], closed=True,
                           facecolor='#BAE6FD', edgecolor='#0284C7', lw=2)
    ax.add_patch(dia1)
    ax.text(4.25, 2.7, "Apakah Hari = Libur?", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0369A1')

    # False branch to Right -> Masuk Sekolah
    ax.annotate("TIDAK", xy=(6.8, 2.7), xytext=(5.6, 2.7), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2))
    act_school = patches.FancyBboxPatch((6.8, 2.45), 1.4, 0.5, boxstyle="round,pad=0.05,rounding_size=0.08",
                                        facecolor='#FEE2E2', edgecolor='#EF4444', lw=1.5)
    ax.add_patch(act_school)
    ax.text(7.5, 2.7, "Masuk Sekolah\n& Belajar Rutin", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#991B1B')

    # True branch to Down -> Nested Condition 2
    ax.annotate("YA", xy=(4.25, 1.8), xytext=(4.25, 2.1), arrowprops=dict(arrowstyle="->", color='#16A34A', lw=2))

    dia2 = patches.Polygon([[4.25, 1.8], [5.5, 1.25], [4.25, 0.7], [3.0, 1.25]], closed=True,
                           facecolor='#FEF08A', edgecolor='#D97706', lw=2)
    ax.add_patch(dia2)
    ax.text(4.25, 1.25, "Apakah Cuaca = Hujan?", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#92400E')

    # Nested branch True: Main Game di Rumah
    ax.annotate("YA", xy=(1.8, 1.25), xytext=(3.0, 1.25), arrowprops=dict(arrowstyle="->", color='#16A34A', lw=2))
    act_indoor = patches.FancyBboxPatch((0.4, 1.0), 1.4, 0.5, boxstyle="round,pad=0.05,rounding_size=0.08",
                                        facecolor='#DCFCE7', edgecolor='#22C55E', lw=1.5)
    ax.add_patch(act_indoor)
    ax.text(1.1, 1.25, "Bermain Game Koding\ndi Dalam Rumah", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#166534')

    # Nested branch False: Bersepeda di Luar
    ax.annotate("TIDAK", xy=(6.5, 1.25), xytext=(5.5, 1.25), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2))
    act_outdoor = patches.FancyBboxPatch((6.5, 1.0), 1.5, 0.5, boxstyle="round,pad=0.05,rounding_size=0.08",
                                         facecolor='#E0E7FF', edgecolor='#6366F1', lw=1.5)
    ax.add_patch(act_outdoor)
    ax.text(7.25, 1.25, "Bersepeda Bersama\nSahabat di Luar", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#3730A3')

    # Bottom note
    lbl_note = patches.FancyBboxPatch((1.5, 0.15), 5.5, 0.35, boxstyle="round,pad=0.03,rounding_size=0.06",
                                      facecolor='#F1F5F9', edgecolor='#94A3B8')
    ax.add_patch(lbl_note)
    ax.text(4.25, 0.32, "Kunci: Kondisi berlapis memungkinkan algoritma menangani situasi dunia nyata yang kompleks!",
            ha='center', va='center', fontsize=7.8, color='#334155')

    save_fig(fig, "bab1_struktur_percabangan_nested_if.png")

# -------------------------------------------------------------
# 4. BAB 1: ARSITEKTUR MODULAR CUSTOM BLOCK
# -------------------------------------------------------------
def make_bab1_custom_block():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#4F46E5', edgecolor='#4338CA')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "MODULARISASI KODE: MEMBUAT CUSTOM BLOCKS DENGAN PARAMETER DINAMIS",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Left: Spaghetti Code
    c_left = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                    facecolor='#FFF1F2', edgecolor='#F43F5E', linewidth=2)
    ax.add_patch(c_left)
    ax.text(2.2, 3.4, "KODE TANPA FUNGSI (SPAGHETTI)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#BE123C')
    ax.text(2.2, 3.1, "Blok kode diulang-ulang berkali-kali:", ha='center', va='center', fontsize=8, color='#881337')

    code_bad = (
        "- Blok Gerak 10 Langkah\n"
        "- Blok Mainkan Bunyi 'Laser'\n"
        "- Ubah Kostum ke 2\n"
        "- Tunggu 0.2 Detik\n"
        "(Ditulis ulang 15 kali untuk 15 musuh!)\n\n"
        "AKIBAT:\n"
        "* Kode sangat panjang & melelahkan\n"
        "* Sulit mencari bug jika ada kesalahan\n"
        "* Memori program cepat penuh"
    )
    ax.text(0.6, 1.8, code_bad, ha='left', va='center', fontsize=7.8, color='#4C0519', linespacing=1.3)

    # Right: Clean Modular Code
    c_right = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                     facecolor='#ECFDF5', edgecolor='#10B981', linewidth=2)
    ax.add_patch(c_right)
    ax.text(6.3, 3.4, "KODE BERSIH MODULAR (CUSTOM BLOCK)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#065F46')
    ax.text(6.3, 3.1, "Definisikan 1 kali, panggil berkali-kali:", ha='center', va='center', fontsize=8, color='#064E3B')

    # Define Block Box
    def_box = patches.FancyBboxPatch((4.7, 2.1), 3.2, 0.65, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor='#8B5CF6', edgecolor='#6D28D9', lw=1.5)
    ax.add_patch(def_box)
    ax.text(6.3, 2.42, "define TembakLaser (Kecepatan, Warna)", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#FFFFFF')

    # Call Block Box
    call_box = patches.FancyBboxPatch((4.7, 1.25), 3.2, 0.65, boxstyle="round,pad=0.04,rounding_size=0.08",
                                      facecolor='#06B6D4', edgecolor='#0891B2', lw=1.5)
    ax.add_patch(call_box)
    ax.text(6.3, 1.57, "TembakLaser (50, 'Merah')\nTembakLaser (80, 'Biru')", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    benefit = (
        "KEUNTUNGAN:\n"
        "v Sangat rapi, hemat ruang & efisien\n"
        "v Parameter masukan bisa diubah dinamis\n"
        "v Mudah diperbaiki hanya di satu tempat!"
    )
    ax.text(4.7, 0.75, benefit, ha='left', va='center', fontsize=7.6, color='#064E3B', linespacing=1.2)

    save_fig(fig, "bab1_arsitektur_modular_custom_block.png")

# -------------------------------------------------------------
# 5. BAB 2: KOMIK PEMBUKA MULTIMEDIA & PODCAST
# -------------------------------------------------------------
def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#C2410C', edgecolor='#9A3412')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 2: LAHIRNYA 'SUARA REMAJA SMP NUSANTARA'",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Gagasan Podcast Remaja", "bg": "#FFF7ED", "bdr": "#EA580C",
         "dialog": "Ayu:\n'Teman-teman, ayo kita bikin podcast edukasi tentang tips belajar koding tanpa stres! Banyak kawan kita yang ingin tahu cara bikin game sederhana!'",
         "status": "Riset Ide Kreatif"},
        {"x": 3.0, "title": "Panel 2: Naskah & Perekaman", "bg": "#EFF6FF", "bdr": "#2563EB",
         "dialog": "Rian:\n'Sepakat! Aku siapkan naskah terstruktur 5 babak: Jingle pembuka, obrolan santai, tips inti, sesi tanya-jawab, dan penutup motivasi. Mikrofon sudah siap!'",
         "status": "Naskah & Produksi Audio"},
        {"x": 5.6, "title": "Panel 3: Harmoni Video & Takarir", "bg": "#FAF5FF", "bdr": "#9333EA",
         "dialog": "Fajar:\n'Aku bantu potong klip di timeline video dan pasang takarir teks otomatis dengan bantuan AI. Teman tuli kita juga bisa ikut menikmati tayangan ini!'",
         "status": "Editing Inklusif"}
    ]

    for p in panels:
        box = patches.FancyBboxPatch((p["x"], 0.35), 2.5, 3.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                     facecolor=p["bg"], edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(box)

        lbl = patches.FancyBboxPatch((p["x"]+0.1, 3.85), 2.3, 0.3, boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(lbl)
        ax.text(p["x"]+1.25, 4.0, p["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

        cir = patches.Circle((p["x"]+1.25, 2.95), 0.55, facecolor='#FFFFFF', edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(cir)
        ax.text(p["x"]+1.25, 2.95, "STUDIO\nDIGITAL", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab2_komik_pembuka_smp8.png")

# -------------------------------------------------------------
# 6. BAB 2: ALUR PRODUKSI PODCAST & VIDEO
# -------------------------------------------------------------
def make_bab2_alur_produksi():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#EA580C', edgecolor='#C2410C')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "TIGA FASE UTAMA PRODUKSI MEDIA AUDIO-VISUAL EDUKATIF",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "title": "PRA-PRODUKSI", "sub": "Perencanaan & Naskah", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 0.5,
         "items": ["* Riset topik & audiens", "* Penulisan script naskah", "* Storyboard alur visual", "* Informed consent narasumber"]},
        {"num": "2", "title": "PRODUKSI", "sub": "Perekaman & Pengambilan", "bg": "#FFF7ED", "bdr": "#EA580C", "x": 3.1,
         "items": ["* Uji mikrofon & desis", "* Perekaman vokal vokal jernih", "* Pengambilan video multi-angle", "* Pengaturan pencahayaan alami"]},
        {"num": "3", "title": "PASCAPRODUKSI", "sub": "Penyuntingan & Publikasi", "bg": "#ECFDF5", "bdr": "#10B981", "x": 5.7,
         "items": ["* Timeline editing video", "* Noise reduction & EQ audio", "* Penambahan subtitle (AI)", "* Ekspor format MP4/MP3 ramah"]}
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.4), 2.3, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                      facecolor=s["bg"], edgecolor=s["bdr"], linewidth=2)
        ax.add_patch(card)

        cir = patches.Circle((s["x"]+1.15, 3.15), 0.35, facecolor=s["bdr"], edgecolor='#FFFFFF', lw=2)
        ax.add_patch(cir)
        ax.text(s["x"]+1.15, 3.15, s["num"], ha='center', va='center', fontsize=14, fontweight='bold', color='#FFFFFF')

        ax.text(s["x"]+1.15, 2.55, s["title"], ha='center', va='center', fontsize=9.5, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+1.15, 2.3, s["sub"], ha='center', va='center', fontsize=8, color='#475569')

        y_item = 1.95
        for item in s["items"]:
            ax.text(s["x"]+0.2, y_item, item, ha='left', va='center', fontsize=7.8, color='#1E293B')
            y_item -= 0.36

    # Arrows between cards
    ax.annotate("", xy=(3.05, 2.0), xytext=(2.85, 2.0), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=3))
    ax.annotate("", xy=(5.65, 2.0), xytext=(5.45, 2.0), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=3))

    save_fig(fig, "bab2_alur_produksi_podcast_dan_video.png")

# -------------------------------------------------------------
# 7. BAB 2: ANATOMI TIMELINE EDITING VIDEO
# -------------------------------------------------------------
def make_bab2_timeline():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "ANATOMI MULTI-TRACK TIMELINE DALAM PENYUNTINGAN VIDEO DIGITAL",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Main Canvas Frame
    frame = patches.FancyBboxPatch((0.5, 0.4), 7.5, 3.4, boxstyle="round,pad=0.05,rounding_size=0.08",
                                  facecolor='#0F172A', edgecolor='#334155', lw=2)
    ax.add_patch(frame)

    tracks = [
        {"name": "TRACK TEKS / TAKARIR (Subtitle Track)", "color": "#F59E0B", "bg": "#78350F", "y": 2.9, "clips": ["Takarir Pembuka", "Subtitle Sesi 1 (AI)", "Subtitle Sesi 2 (AI)", "Kredit Penutup"]},
        {"name": "TRACK B-ROLL (Cuplikan Tambahan)", "color": "#06B6D4", "bg": "#164E63", "y": 2.25, "clips": ["Foto Robot", "Cuplikan Koding", "Diagram Layar"]},
        {"name": "TRACK VIDEO UTAMA (Main Video Track)", "color": "#3B82F6", "bg": "#1E3A8A", "y": 1.6, "clips": ["Klip Intro Wajah", "Wawancara Pembicara 1", "Wawancara Pembicara 2", "Closing Host"]},
        {"name": "TRACK AUDIO UTAMA (Vokal Suara)", "color": "#10B981", "bg": "#064E3B", "y": 0.95, "clips": ["Vokal Host (Dibersihkan)", "Vokal Tamu (Audio Leveling)"]},
        {"name": "TRACK MUSIK & SFX (Background Music)", "color": "#EC4899", "bg": "#831843", "y": 0.5, "clips": ["Jingle Intro", "Musik Latar Pelan (Volume 15%)", "Sound FX Sukses", "Jingle Outro"]}
    ]

    for t in tracks:
        ax.text(0.7, t["y"]+0.15, t["name"], fontsize=7.2, fontweight='bold', color=t["color"])
        # Track line
        ax.plot([0.7, 7.8], [t["y"], t["y"]], color='#334155', lw=1, ls='--')

        # Draw clips
        curr_x = 0.8
        for c in t["clips"]:
            w = 1.3 if len(c) < 16 else 1.8
            if curr_x + w > 7.7:
                w = 7.7 - curr_x
            if w <= 0.4:
                break
            clip_box = patches.FancyBboxPatch((curr_x, t["y"]-0.16), w, 0.28, boxstyle="round,pad=0.02,rounding_size=0.04",
                                              facecolor=t["bg"], edgecolor=t["color"], lw=1.2)
            ax.add_patch(clip_box)
            ax.text(curr_x + w/2, t["y"]-0.02, c, ha='center', va='center', fontsize=6.5, color='#F8FAFC')
            curr_x += w + 0.15

    # Playhead
    ax.plot([3.2, 3.2], [0.4, 3.7], color='#EF4444', lw=2)
    ax.text(3.2, 3.6, "v Playhead (Waktu Saat Ini)", ha='center', va='bottom', fontsize=7.5, fontweight='bold', color='#EF4444')

    save_fig(fig, "bab2_anatomi_timeline_editing_video.png")

# -------------------------------------------------------------
# 8. BAB 2: INFOGRAFIS INFORMED CONSENT MEDIA
# -------------------------------------------------------------
def make_bab2_consent():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "ETIKA PENYIARAN: PERSETUJUAN ATAS INFORMASI (INFORMED CONSENT)",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Card
    card = patches.FancyBboxPatch((0.5, 0.4), 7.5, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                  facecolor='#ECFDF5', edgecolor='#10B981', linewidth=2)
    ax.add_patch(card)

    pillars = [
        {"title": "1. JELASKAN TUJUAN", "desc": "Sampaikan secara jujur untuk apa video/rekaman dibuat (tugas sekolah, edukasi umum, atau lomba).", "icon": "TUJUAN"},
        {"title": "2. RUANG LINGKUP TAYANG", "desc": "Beri tahu di mana karya akan diunggah (YouTube sekolah, podcast Spotify, atau presentasi kelas).", "icon": "MEDIA"},
        {"title": "3. HAK MENOLAK / MENGEDIT", "desc": "Narasumber berhak meminta bagian tertentu dipotong jika merasa kurang nyaman dengan ucapannya.", "icon": "HAK"},
        {"title": "4. IZIN ORANG TUA (ANAK)", "desc": "Jika narasumber di bawah umur, mintakan izin tertulis dari orang tua atau wali murid terkait.", "icon": "WALI"}
    ]

    curr_x = 0.8
    for p in pillars:
        p_box = patches.FancyBboxPatch((curr_x, 0.7), 1.6, 2.7, boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor='#FFFFFF', edgecolor='#059669', lw=1.5)
        ax.add_patch(p_box)

        cir = patches.Circle((curr_x + 0.8, 3.0), 0.3, facecolor='#059669', edgecolor='#FFFFFF', lw=1.5)
        ax.add_patch(cir)
        ax.text(curr_x + 0.8, 3.0, p["icon"][0], ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

        ax.text(curr_x + 0.8, 2.45, p["title"], ha='center', va='center', fontsize=8.2, fontweight='bold', color='#065F46')
        ax.text(curr_x + 0.8, 1.55, p["desc"], ha='center', va='center', fontsize=7.4, color='#334155', wrap=True,
                multialignment='center')
        curr_x += 1.8

    save_fig(fig, "bab2_infografis_informed_consent_media.png")

# -------------------------------------------------------------
# 9. BAB 3: KOMIK PEMBUKA MULTI-SENSOR
# -------------------------------------------------------------
def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 3: MISI PENYELAMATAN DRONE DI KABUT TEBAL",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Kamera Optik Buntu", "bg": "#F0F9FF", "bdr": "#0284C7",
         "dialog": "Fajar:\n'Gawat! Kabut di lereng gunung sangat pekat! Kamera optik drone kita hanya menangkap layar putih buram! Pendaki yang tersesat tidak terlihat sama sekali!'",
         "status": "Sensor Optik Terhalang"},
        {"x": 3.0, "title": "Panel 2: Fusi Sensor Inframerah", "bg": "#FFFBEB", "bdr": "#D97706",
         "dialog": "Rian:\n'Aktifkan sensor inframerah thermal dan pemindai LiDAR! Panas tubuh manusia akan memancarkan gelombang yang menembus kabut tebal!'",
         "status": "Multi-Sensor Diaktifkan"},
        {"x": 5.6, "title": "Panel 3: Titik Koordinat Akurat", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Ayu:\n'Berhasil! Komputer drone menggabungkan data thermal dan sinyal GPS (Sensor Fusion). Titik lokasi tenda pendaki ditemukan dengan akurat!'",
         "status": "Penyelamatan Sukses"}
    ]

    for p in panels:
        box = patches.FancyBboxPatch((p["x"], 0.35), 2.5, 3.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                     facecolor=p["bg"], edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(box)

        lbl = patches.FancyBboxPatch((p["x"]+0.1, 3.85), 2.3, 0.3, boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(lbl)
        ax.text(p["x"]+1.25, 4.0, p["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

        cir = patches.Circle((p["x"]+1.25, 2.95), 0.55, facecolor='#FFFFFF', edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(cir)
        ax.text(p["x"]+1.25, 2.95, "DRONE\nCERDAS", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab3_komik_pembuka_smp8.png")

# -------------------------------------------------------------
# 10. BAB 3: ARSITEKTUR SENSOR FUSION DRONE
# -------------------------------------------------------------
def make_bab3_sensor_fusion():
    fig, ax = plt.subplots(figsize=(8.5, 4.8), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.8); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.2), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.42, "ARSITEKTUR FUSI SENSOR (SENSOR FUSION): MATA & TELINGA SISTEM CERDAS",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    sensors = [
        {"name": "KAMERA OPTIK RGB", "role": "Melihat warna & bentuk visual", "icon": "OPTIK", "bg": "#EFF6FF", "bdr": "#3B82F6", "y": 3.2},
        {"name": "SENSOR THERMAL INFRAMERAH", "role": "Mendeteksi radiasi panas tubuh", "icon": "PANAS", "bg": "#FFF1F2", "bdr": "#F43F5E", "y": 2.15},
        {"name": "MODUL GPS & IMU (GYRO)", "role": "Menentukan koordinat & kestabilan", "icon": "POSISI", "bg": "#FAF5FF", "bdr": "#A855F7", "y": 1.1}
    ]

    for s in sensors:
        box = patches.FancyBboxPatch((0.5, s["y"]-0.35), 2.8, 0.8, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=2)
        ax.add_patch(box)
        ax.text(1.9, s["y"]+0.12, s["name"], ha='center', va='center', fontsize=8.2, fontweight='bold', color=s["bdr"])
        ax.text(1.9, s["y"]-0.15, s["role"], ha='center', va='center', fontsize=7.4, color='#475569')

        ax.annotate("", xy=(3.8, 2.15), xytext=(3.3, s["y"]), arrowprops=dict(arrowstyle="->", color=s["bdr"], lw=2))

    # Center: Fusion Unit
    unit = patches.FancyBboxPatch((3.8, 1.4), 2.2, 1.5, boxstyle="round,pad=0.05,rounding_size=0.12",
                                  facecolor='#1E293B', edgecolor='#38BDF8', lw=2.5)
    ax.add_patch(unit)
    ax.text(4.9, 2.45, "UNIT FUSI SENSOR", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#38BDF8')
    ax.text(4.9, 2.05, "(Microcontroller /\nAI Processor)", ha='center', va='center', fontsize=8, color='#94A3B8')
    ax.text(4.9, 1.6, "* Menggabungkan data\n* Mengurangi noise\n* Menghilangkan blind spot", ha='center', va='center', fontsize=6.8, color='#E2E8F0')

    # Arrow to Decision
    ax.annotate("", xy=(6.5, 2.15), xytext=(6.0, 2.15), arrowprops=dict(arrowstyle="->", color='#10B981', lw=3))

    # Output Decision Box
    dec_box = patches.FancyBboxPatch((6.5, 1.3), 1.6, 1.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                     facecolor='#ECFDF5', edgecolor='#10B981', lw=2)
    ax.add_patch(dec_box)
    ax.text(7.3, 2.55, "KEPUTUSAN AI", ha='center', va='center', fontsize=9, fontweight='bold', color='#065F46')
    ax.text(7.3, 1.95, "Lokasi Korban:\nLat: -7.2514\nLong: 110.428\nStatus: Selamat\nTindakan:\nJatuhkan Bantuan!",
            ha='center', va='center', fontsize=7.2, color='#064E3B')

    # Bottom summary pill
    bot = patches.FancyBboxPatch((1.0, 0.2), 6.5, 0.4, boxstyle="round,pad=0.03,rounding_size=0.08",
                                 facecolor='#F1F5F9', edgecolor='#CBD5E1')
    ax.add_patch(bot)
    ax.text(4.25, 0.4, "Prinsip: 'Satu sensor bisa salah, namun gabungan multi-sensor saling melengkapi kebenaran.'",
            ha='center', va='center', fontsize=8, color='#334155')

    save_fig(fig, "bab3_arsitektur_sensor_fusion_drone.png")

# -------------------------------------------------------------
# 11. BAB 3: SIKLUS SINYAL FISIK KE BINER
# -------------------------------------------------------------
def make_bab3_sinyal_biner():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#475569', edgecolor='#334155')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "BAGAIMANA KOMPUTER MEMBACA ALAM: DARI SINYAL FISIK MENJADI BINER",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    steps = [
        {"title": "1. FENOMENA FISIK", "sub": "Suhu, Suara, Gelombang Cahaya", "bg": "#FEF3C7", "bdr": "#D97706", "x": 0.4,
         "desc": "Kenyataan di alam bersifat kontinu (analog), berfluktuasi naik-turun tanpa henti."},
        {"title": "2. SENSOR & TEGANGAN", "sub": "Mengubah ke Voltase Listrik", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 2.35,
         "desc": "Resistansi berubah saat panas/cahaya masuk, menghasilkan gelombang voltase analog."},
        {"title": "3. SAMPLING & ADC", "sub": "Analog-to-Digital Converter", "bg": "#FAF5FF", "bdr": "#9333EA", "x": 4.3,
         "desc": "Gelombang listrik diukur nilainya ribuan kali per detik (sampling rate) menjadi angka."},
        {"title": "4. DERETAN BINER", "sub": "Bit Digital: 0 dan 1", "bg": "#ECFDF5", "bdr": "#10B981", "x": 6.25,
         "desc": "Angka diubah ke biner: 10110011. Siap diproses oleh algoritma AI komputer!"}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 0.7), 1.8, 2.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        ax.text(s["x"]+0.9, 3.25, s["title"], ha='center', va='center', fontsize=8, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.9, 2.95, s["sub"], ha='center', va='center', fontsize=7.2, color='#475569')

        ax.text(s["x"]+0.9, 1.7, s["desc"], ha='center', va='center', fontsize=7.4, color='#1E293B', wrap=True,
                multialignment='center')

    # Arrows
    ax.annotate("", xy=(2.3, 2.1), xytext=(2.2, 2.1), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2))
    ax.annotate("", xy=(4.25, 2.1), xytext=(4.15, 2.1), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2))
    ax.annotate("", xy=(6.2, 2.1), xytext=(6.1, 2.1), arrowprops=dict(arrowstyle="->", color='#94A3B8', lw=2))

    save_fig(fig, "bab3_siklus_sinyal_fisik_ke_biner.png")

# -------------------------------------------------------------
# 12. BAB 3: INFOGRAFIS KUALITAS DATA & BIAS
# -------------------------------------------------------------
def make_bab3_kualitas_data():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#DC2626', edgecolor='#B91C1C')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "KUALITAS DATA LATIH AI: DATA BERSIH VS DATA BISING & TIMPANG",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Good Data
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#ECFDF5', edgecolor='#10B981', linewidth=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.4, "DATASET BERKUALITAS (BALANCED)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#065F46')

    good_txt = (
        "Ciri-ciri:\n"
        "v Gambar jernih, variasi sudut cukup\n"
        "v Jumlah sampel merata (50 foto apel,\n"
        "  50 foto jeruk, 50 foto pisang)\n"
        "v Tidak ada bias pencahayaan / warna\n\n"
        "HASIL PREDIKSI AI:\n"
        "Akurasi Tinggi (98%), adil mengenali\n"
        "semua jenis buah dalam segala kondisi!"
    )
    ax.text(0.6, 1.8, good_txt, ha='left', va='center', fontsize=7.8, color='#064E3B', linespacing=1.2)

    # Bad Data
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFF1F2', edgecolor='#F43F5E', linewidth=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.4, "DATASET TIMPANG & BISING (BIASED)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#9F1239')

    bad_txt = (
        "Ciri-ciri:\n"
        "x 100 foto apel, tapi hanya 2 foto pisang\n"
        "x Gambar buram, tertutup bayangan (noise)\n"
        "x Hanya memotret di siang hari terik\n\n"
        "BAHAYA BIAS AI:\n"
        "AI akan mengira semua buah lonjong\n"
        "adalah apel busuk! Akurasi jeblok saat\n"
        "diuji malam hari atau kondisi baru."
    )
    ax.text(4.7, 1.8, bad_txt, ha='left', va='center', fontsize=7.8, color='#881337', linespacing=1.2)

    save_fig(fig, "bab3_infografis_kualitas_data_bias.png")

# -------------------------------------------------------------
# 13. BAB 4: KOMIK PEMBUKA REKAYASA SOSIAL
# -------------------------------------------------------------
def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#7C2D12', edgecolor='#9A3412')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 4: DETEKTIF SIBER & JEBAKAN PHISHING REKAYASA SOSIAL",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Pesan Menggiurkan", "bg": "#FFF7ED", "bdr": "#EA580C",
         "dialog": "Fajar:\n'Lihat ponselku! Ada pesan WhatsApp dari nomor asing: Selamat! Kamu menang voucher game 1 Juta! Klik link ini sekarang atau hadiah hangus dalam 5 menit!'",
         "status": "Umpan Keserakahan & Panik"},
        {"x": 3.0, "title": "Panel 2: Investigasi Tautan Palsu", "bg": "#FEF2F2", "bdr": "#EF4444",
         "dialog": "Ayu:\n'Tunggu, Fajar! Jangan diklik! Lihat alamat web-nya: bukandomainresmi.xyz/login-akun. Ini teknik Phishing! Tampilan web tiruan dibuat persis untuk mencuri sandi!'",
         "status": "Deteksi Tautan Phishing"},
        {"x": 5.6, "title": "Panel 3: Blokir & Edukasi Keluarga", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Rian:\n'Benar! Penipu memanipulasi emosi kita (Social Engineering). Ayo kita blokir nomornya dan buat booklet edukasi agar orang tua kita tidak jadi korban penipuan!'",
         "status": "Benteng Pertahanan Siber"}
    ]

    for p in panels:
        box = patches.FancyBboxPatch((p["x"], 0.35), 2.5, 3.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                     facecolor=p["bg"], edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(box)

        lbl = patches.FancyBboxPatch((p["x"]+0.1, 3.85), 2.3, 0.3, boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(lbl)
        ax.text(p["x"]+1.25, 4.0, p["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

        cir = patches.Circle((p["x"]+1.25, 2.95), 0.55, facecolor='#FFFFFF', edgecolor=p["bdr"], linewidth=2)
        ax.add_patch(cir)
        ax.text(p["x"]+1.25, 2.95, "SIBER\nALERT", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab4_komik_pembuka_smp8.png")

# -------------------------------------------------------------
# 14. BAB 4: ALUR CHAIN OF THOUGHT PROMPTING
# -------------------------------------------------------------
def make_bab4_cot_prompting():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "TEKNIK CHAIN-OF-THOUGHT (CoT): MENGAJAK AI BERNALAR SELANGKAH DEMI SELANGKAH",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Standard vs CoT
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFF1F2', edgecolor='#F43F5E', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.5, "PROMPT STANDAR (LANGSUNG)", ha='center', va='center', fontsize=9, fontweight='bold', color='#BE123C')
    txt_std = (
        "User Prompt:\n"
        "'Berapa kecepatan rata-rata mobil jika\n"
        "menempuh 120 km dalam 2 jam 30 menit?'\n\n"
        "Respon AI Langsung:\n"
        "'Jawabannya 50 km/jam.'\n"
        "(Sering salah hitung karena tebak langsung)\n\n"
        "Kelemahan:\n"
        "- AI rawan halusinasi angka\n"
        "- Kita tidak tahu letak kesalahan logikanya\n"
        "- Tidak melatih nalar kritis murid"
    )
    ax.text(0.6, 1.8, txt_std, ha='left', va='center', fontsize=7.5, color='#4C0519', linespacing=1.2)

    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#3B82F6', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.5, "CHAIN-OF-THOUGHT (BERTAHAP)", ha='center', va='center', fontsize=9, fontweight='bold', color='#1E40AF')
    txt_cot = (
        "User Prompt:\n"
        "'Selesaikan soal ini selangkah demi selangkah:\n"
        "1. Ubah 2 jam 30 menit ke satuan jam desimal.\n"
        "2. Tulis rumus kecepatan v = s / t.\n"
        "3. Hitung hasilnya dan simpulkan.'\n\n"
        "Respon AI Terstruktur:\n"
        "Langkah 1: 30 menit = 0.5 jam -> t = 2.5 jam.\n"
        "Langkah 2: v = 120 / 2.5.\n"
        "Langkah 3: v = 48 km/jam. Tepat 100%!\n\n"
        "Keunggulan: Akurat, logis & mendidik!"
    )
    ax.text(4.7, 1.8, txt_cot, ha='left', va='center', fontsize=7.5, color='#1E293B', linespacing=1.2)

    save_fig(fig, "bab4_alur_chain_of_thought_prompting.png")

# -------------------------------------------------------------
# 15. BAB 4: INFOGRAFIS SOCIAL ENGINEERING & PHISHING
# -------------------------------------------------------------
def make_bab4_social_engineering():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#991B1B', edgecolor='#7F1D1D')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "ANATOMI SERANGAN REKAYASA SOSIAL (SOCIAL ENGINEERING) & MITIGASINYA",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Card
    card = patches.FancyBboxPatch((0.5, 0.4), 7.5, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                  facecolor='#FEF2F2', edgecolor='#EF4444', lw=2)
    ax.add_patch(card)

    tactics = [
        {"title": "1. MENCIPTAKAN KEPANIKAN", "desc": "'Akun bank Anda dibobol! Verifikasi dalam 2 menit atau saldo disita!'", "reaksi": "TENANG & JANGAN PANIK"},
        {"title": "2. MEMICU KESERAKAHAN", "desc": "'Selamat, Anda menang undian 500 juta! Bayar biaya admin 100 ribu.'", "reaksi": "TAK ADA HADIAH GRATIS"},
        {"title": "3. MENIRU FIGUR RESMI", "desc": "'Halo, saya dari kurir paket / kepolisian, mohon kirimkan kode OTP.'", "reaksi": "JANGAN PERNAH BAGI OTP"},
        {"title": "4. TAUTAN PALSU (TYPOS)", "desc": "www.faceb00k-login.cc (perhatikan ejaan domain yang janggal).", "reaksi": "CEK DOMAIN RESMI"}
    ]

    curr_x = 0.8
    for t in tactics:
        t_box = patches.FancyBboxPatch((curr_x, 0.65), 1.6, 2.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor='#FFFFFF', edgecolor='#DC2626', lw=1.5)
        ax.add_patch(t_box)

        ax.text(curr_x + 0.8, 3.25, t["title"], ha='center', va='center', fontsize=7.8, fontweight='bold', color='#991B1B')
        ax.text(curr_x + 0.8, 2.2, t["desc"], ha='center', va='center', fontsize=7.2, color='#334155', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((curr_x + 0.08, 0.85), 1.44, 0.4, boxstyle="round,pad=0.03,rounding_size=0.06",
                                      facecolor='#DC2626', edgecolor='#991B1B')
        ax.add_patch(pill)
        ax.text(curr_x + 0.8, 1.05, t["reaksi"], ha='center', va='center', fontsize=6.8, fontweight='bold', color='#FFFFFF')

        curr_x += 1.8

    save_fig(fig, "bab4_infografis_social_engineering_phishing.png")

# -------------------------------------------------------------
# 16. BAB 4: DIAGRAM JEJAK DIGITAL REMAJA
# -------------------------------------------------------------
def make_bab4_jejak_digital():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#0F172A', edgecolor='#334155')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "JEJAK DIGITAL (DIGITAL FOOTPRINT): ABADI DI RUANG SIBER",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    # Passive
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#F1F5F9', edgecolor='#64748B', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.4, "JEJAK DIGITAL PASIF", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#334155')
    txt_pas = (
        "Tertinggal tanpa kita sadari:\n"
        "- Alamat IP perangkat & lokasi kota\n"
        "- Riwayat pencarian Google / YouTube\n"
        "- Durasi menonton video tertentu\n"
        "- Cookies preferensi belanja online\n\n"
        "Digunakan perusahaan untuk menampilkan\n"
        "iklan bertarget dan rekomendasi algoritma."
    )
    ax.text(0.6, 1.8, txt_pas, ha='left', va='center', fontsize=7.8, color='#1E293B', linespacing=1.2)

    # Active
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFFBEB', edgecolor='#F59E0B', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.4, "JEJAK DIGITAL AKTIF", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B45309')
    txt_akt = (
        "Sengaja kita bagikan ke publik:\n"
        "- Unggahan foto, reels & video TikTok\n"
        "- Komentar dan pesan di forum publik\n"
        "- Status media sosial & ulasan toko\n\n"
        "INGAT:\n"
        "Sekali diunggah, data sulit dihapus 100%!\n"
        "Dapat memengaruhi seleksi beasiswa kuliah\n"
        "dan karir profesional kalian 10 tahun lagi!"
    )
    ax.text(4.7, 1.8, txt_akt, ha='left', va='center', fontsize=7.8, color='#78350F', linespacing=1.2)

    save_fig(fig, "bab4_diagram_jejak_digital_remaja.png")

# -------------------------------------------------------------
# 17. COVER BUKU SISWA SMP KELAS 8
# -------------------------------------------------------------
def make_cover_smp8():
    img = Image.new('RGB', (1800, 2700), color='#1E3A8A')
    draw = ImageDraw.Draw(img)

    for y in range(800):
        ratio = y / 800
        r = int(30 + (29 - 30) * ratio)
        g = int(58 + (78 - 58) * ratio)
        b = int(138 + (216 - 138) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(800, 1900):
        ratio = (y - 800) / 1100
        r = int(29 + (2 - 29) * ratio)
        g = int(78 + (132 - 78) * ratio)
        b = int(216 + (199 - 216) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(1900, 2700):
        ratio = (y - 1900) / 800
        r = int(2 + (15 - 2) * ratio)
        g = int(132 + (23 - 132) * ratio)
        b = int(199 + (42 - 199) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    try:
        f_badge = ImageFont.truetype("arial.ttf", 40)
        f_title = ImageFont.truetype("arialbd.ttf", 92)
        f_sub = ImageFont.truetype("arialbd.ttf", 52)
        f_phase = ImageFont.truetype("arialbd.ttf", 46)
        f_auth = ImageFont.truetype("arialbd.ttf", 48)
        f_role = ImageFont.truetype("arial.ttf", 36)
        f_pub = ImageFont.truetype("arialbd.ttf", 40)
        f_subpub = ImageFont.truetype("arial.ttf", 34)
    except:
        f_badge = f_title = f_sub = f_phase = f_auth = f_role = f_pub = f_subpub = ImageFont.load_default()

    draw.rectangle([100, 90, 820, 160], fill='#2563EB')
    draw.text((130, 102), "BUKU TEKS PELAJARAN SMP/MTs", font=f_badge, fill='#FFFFFF')

    draw.text((100, 260), "KODING DAN", font=f_title, fill='#FFFFFF')
    draw.text((100, 370), "KECERDASAN", font=f_title, fill='#60A5FA')
    draw.text((100, 480), "ARTIFISIAL", font=f_title, fill='#FACC15')

    # Grade Pill Badge
    draw.rectangle([100, 620, 950, 720], fill='#EA580C')
    draw.text((130, 642), "KELAS VIII  •  FASE D (SMP/MTs)", font=f_phase, fill='#FFFFFF')

    # Big Rounded Showcase Card
    draw.rounded_rectangle([150, 820, 1650, 1920], radius=40, fill='#0F172A', outline='#38BDF8', width=8)

    draw.text((220, 900), "KURIKULUM NASIONAL KKA KEMENDIKDASMEN RI", font=f_badge, fill='#FACC15')
    draw.text((220, 980), "Fokus Penguasaan Tingkat Menengah SMP (Fase D):", font=f_sub, fill='#FFFFFF')

    features = [
        "v  Logika Percabangan Bersarang (Nested If-Else) & Operator Majemuk",
        "v  Modularisasi Program: Fungsi Mandiri (Custom Blocks) & Clean Code",
        "v  Produksi Media Digital: Podcast Audio, Timeline Editing Video & AI",
        "v  Etika Penyiaran Digital & Persetujuan Informasi (Informed Consent)",
        "v  Persepsi Mesin, Fusi Sensor (Sensor Fusion) & Kualitas Data Latih",
        "v  Teknik Chain-of-Thought (CoT) Prompting & Mitigasi Phishing Siber"
    ]

    curr_y = 1080
    for feat in features:
        draw.text((220, curr_y), feat, font=f_phase, fill='#E2E8F0')
        curr_y += 120

    # Author Box
    draw.rounded_rectangle([100, 2020, 1700, 2300], radius=30, fill='#FFFFFF', outline='#2563EB', width=5)
    draw.text((150, 2060), "Penulis: Gede Erik Aktama, S.Pd., M.Pd.", font=f_auth, fill='#0F172A')
    draw.text((150, 2130), "Fasilitator Nasional Bimbingan Teknis & ToT KKA Kemendikdasmen RI", font=f_role, fill='#2563EB')
    draw.text((150, 2185), "Dosen Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", font=f_role, fill='#475569')

    # Publisher Footer
    draw.text((900, 2390), "PUSAT PERBUKUAN", font=f_pub, fill='#FFFFFF', anchor="mm")
    draw.text((900, 2450), "BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2505), "KEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2560), "TAHUN 2025 / 2026", font=f_subpub, fill='#FACC15', anchor="mm")

    local_cov = os.path.join(local_assets, "cover_buku_siswa_smp8.jpg")
    img.save(local_cov, quality=95)
    tot_cov = os.path.join(tot_assets, "cover_buku_siswa_smp8.jpg")
    try:
        shutil.copy2(local_cov, tot_cov)
    except Exception as e:
        print(f"Warning copying cover: {e}")
    print("Generated cover: cover_buku_siswa_smp8.jpg")

if __name__ == "__main__":
    print("Starting visual assets generation for Grade 8 SMP...")
    make_tokoh_sahabat()
    make_bab1_komik()
    make_bab1_saklar_and_or()
    make_bab1_nested_if()
    make_bab1_custom_block()
    make_bab2_komik()
    make_bab2_alur_produksi()
    make_bab2_timeline()
    make_bab2_consent()
    make_bab3_komik()
    make_bab3_sensor_fusion()
    make_bab3_sinyal_biner()
    make_bab3_kualitas_data()
    make_bab4_komik()
    make_bab4_cot_prompting()
    make_bab4_social_engineering()
    make_bab4_jejak_digital()
    make_cover_smp8()
    print("All visual assets for Grade 8 SMP successfully generated!")
