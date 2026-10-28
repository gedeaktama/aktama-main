# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Buku KKA Kelas 9 SMP (Fase D)
Resolusi Tinggi 300 DPI, Desain Infografis Edukatif & Komik Remaja,
Modern, Penuh Warna, Sesuai Standar Kemendikdasmen & Kurikulum Nasional.
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-9-smp\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 9 SMP\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

# Copy foto_penulis.jpg
src_foto = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-7-smp\assets\foto_penulis.jpg"
if os.path.exists(src_foto):
    shutil.copy2(src_foto, os.path.join(local_assets, "foto_penulis.jpg"))
    shutil.copy2(src_foto, os.path.join(tot_assets, "foto_penulis.jpg"))
    print("Copied foto_penulis.jpg to Kelas 9 assets")

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
# 0. TOKOH SAHABAT BELAJAR KELAS 9 SMP
# -------------------------------------------------------------
def make_tokoh_sahabat():
    fig, ax = plt.subplots(figsize=(8.0, 3.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.6); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 2.9), 7.2, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor='#047857', edgecolor='#065F46')
    ax.add_patch(title_box)
    ax.text(4.0, 3.17, "TIGA SAHABAT INOVATOR SENIOR KODING & KA KELAS IX SMP",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    tokohs = [
        {"nama": "RIAN", "role": "Programmer Python Muda", "ciri": "Siswa analitis, menguasai sintaks teks Python, algoritma efisien & arsitek prototipe", "color": "#059669", "bg": "#ECFDF5", "x": 0.5},
        {"nama": "AYU", "role": "Data Storyteller & Desainer", "ciri": "Siswi kreatif, perancang instrumen survei, visualisasi dashboard & UX Design", "color": "#D97706", "bg": "#FFFBEB", "x": 3.0},
        {"nama": "FAJAR", "role": "Peneliti Regulasi & Etika AI", "ciri": "Siswa kritis, aktivis perlindungan data pribadi (UU PDP), etika hukum & hak cipta", "color": "#4F46E5", "bg": "#EEF2FF", "x": 5.5},
    ]

    for t in tokohs:
        card = patches.FancyBboxPatch((t["x"], 0.25), 2.0, 2.5, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=t["bg"], edgecolor=t["color"], linewidth=2)
        ax.add_patch(card)

        circle = patches.Circle((t["x"] + 1.0, 2.05), 0.5, facecolor=t["color"], edgecolor='#FFFFFF', linewidth=2)
        ax.add_patch(circle)
        ax.text(t["x"] + 1.0, 2.05, t["nama"][0], ha='center', va='center', fontsize=16, fontweight='bold', color='#FFFFFF')

        ax.text(t["x"] + 1.0, 1.35, t["nama"], ha='center', va='center', fontsize=10.5, fontweight='bold', color=t["color"])
        ax.text(t["x"] + 1.0, 1.1, t["role"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#1E293B')

        ax.text(t["x"] + 1.0, 0.65, t["ciri"], ha='center', va='center', fontsize=7.2, color='#475569', wrap=True,
                multialignment='center')

    save_fig(fig, "gambar_tokoh_sahabat_smp9.png")

# -------------------------------------------------------------
# 1. BAB 1: KOMIK PEMBUKA TRANSISI PYTHON
# -------------------------------------------------------------
def make_bab1_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#065F46', edgecolor='#064E3B')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 1: LANGKAH BESAR MENUJU DUNIA TEKS PYTHON",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Rindu Blok Visual", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Ayu:\n'Wah, lihat layar monitor Rian! Tidak ada lagi blok warna-warni yang bisa kita seret! Semuanya baris teks kode hitam-putih! Apakah Python sesulit itu?'",
         "status": "Tantangan Koding Teks"},
        {"x": 3.0, "title": "Panel 2: Sintaks yang Mirip Manusia", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Rian:\n'Awalnya memang terasa asing, Ayu! Tapi begitu kita baca, kata-katanya sangat mirip bahasa Inggris: print(), input(), if-else! Ringkas dan bertenaga!'",
         "status": "Keindahan Sintaks"},
        {"x": 5.6, "title": "Panel 3: Bahasa Para Ilmuwan AI", "bg": "#FFFBEB", "bdr": "#F59E0B",
         "dialog": "Fajar:\n'Benar! Python adalah bahasa resmi pengembang kecerdasan artifisial dan sains data dunia. Dengan menguasai Python di kelas IX, gerbang masa depan terbuka lebar!'",
         "status": "Siap Menjadi Pro!"}
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
        ax.text(p["x"]+1.25, 2.95, "PYTHON\nKODER", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab1_komik_pembuka_smp9.png")

# -------------------------------------------------------------
# 2. BAB 1: JEMBATAN SCRATCH KE PYTHON
# -------------------------------------------------------------
def make_bab1_jembatan():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "JEMBATAN KOMPUTASI: DARI BLOK VISUAL MENUJU SINTAKS PYTHON",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Left: Scratch Blocks
    b_left = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                   facecolor='#FFF7ED', edgecolor='#EA580C', lw=2)
    ax.add_patch(b_left)
    ax.text(2.2, 3.5, "PEMROGRAMAN VISUAL (SCRATCH)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#C2410C')

    # Scratch blocks mockup
    s1 = patches.FancyBboxPatch((0.7, 2.65), 3.0, 0.5, boxstyle="round,pad=0.03,rounding_size=0.08", facecolor='#F59E0B', edgecolor='#D97706')
    ax.add_patch(s1)
    ax.text(2.2, 2.9, "katakan [Halo Nusantara!] selama (2) dtk", ha='center', va='center', fontsize=7.5, color='#FFFFFF')

    s2 = patches.FancyBboxPatch((0.7, 1.7), 3.0, 0.75, boxstyle="round,pad=0.03,rounding_size=0.08", facecolor='#3B82F6', edgecolor='#1D4ED8')
    ax.add_patch(s2)
    ax.text(2.2, 2.15, "jika < (Skor) > [80] > maka", ha='center', va='center', fontsize=7.5, color='#FFFFFF')
    ax.text(2.4, 1.85, "katakan [Lulus Memuaskan!]", ha='center', va='center', fontsize=7.0, color='#FEF08A')

    s3 = patches.FancyBboxPatch((0.7, 0.75), 3.0, 0.75, boxstyle="round,pad=0.03,rounding_size=0.08", facecolor='#EC4899', edgecolor='#DB2777')
    ax.add_patch(s3)
    ax.text(2.2, 1.2, "ulangi (5) kali", ha='center', va='center', fontsize=7.5, color='#FFFFFF')
    ax.text(2.4, 0.9, "ubah [Langkah v] sebesar (10)", ha='center', va='center', fontsize=7.0, color='#FDF2F8')

    # Center Bridge Arrow
    ax.annotate("", xy=(4.4, 2.1), xytext=(4.1, 2.1), arrowprops=dict(arrowstyle="->", color='#10B981', lw=3))

    # Right: Python Code
    b_right = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                    facecolor='#0F172A', edgecolor='#38BDF8', lw=2)
    ax.add_patch(b_right)
    ax.text(6.3, 3.5, "PEMROGRAMAN TEKSTUAL (PYTHON)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#38BDF8')

    py_code = (
        "# 1. Perintah Cetak Teks\n"
        "print('Halo Nusantara!')\n\n"
        "# 2. Percabangan Bersyarat\n"
        "if skor > 80:\n"
        "    print('Lulus Memuaskan!')\n\n"
        "# 3. Perulangan Otomatis\n"
        "for i in range(5):\n"
        "    langkah += 10\n"
        "    print(f'Langkah ke-{i+1}')"
    )
    ax.text(4.7, 1.8, py_code, ha='left', va='center', fontsize=7.8, color='#F8FAFC', linespacing=1.2)

    save_fig(fig, "bab1_jembatan_scratch_ke_python.png")

# -------------------------------------------------------------
# 3. BAB 1: ANATOMI SINTAKS PYTHON DASAR
# -------------------------------------------------------------
def make_bab1_anatomi_python():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "ANATOMI SINTAKS DASAR BAHASA PYTHON: VARIABEL, INPUT & INDENTASI",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Card
    card = patches.FancyBboxPatch((0.5, 0.4), 7.5, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                  facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=2)
    ax.add_patch(card)

    pillars = [
        {"title": "1. FUNGSI print()", "desc": "Mencetak teks ke layar monitor. Gunakan tanda petik (' atau \") untuk teks string.", "code": "print('Halo Sobat!')", "bg": "#EFF6FF", "bdr": "#3B82F6"},
        {"title": "2. VARIABEL & INPUT", "desc": "Menampung nilai dari pengguna. Gunakan int() atau float() untuk angka.", "code": "umur = int(input())\nnilai = 85.5", "bg": "#FEF3C7", "bdr": "#D97706"},
        {"title": "3. ATURAN INDENTASI", "desc": "Spasi menjorok (4 spasi) setelah tanda titik dua (:) menandai blok kode bersarang.", "code": "if nilai >= 75:\n    print('Tuntas')", "bg": "#ECFDF5", "bdr": "#10B981"},
        {"title": "4. KOMENTAR #", "desc": "Catatan penjelasan untuk manusia yang diabaikan oleh mesin penerjemah.", "code": "# Ini baris komentar\n# sangat berguna!", "bg": "#FAF5FF", "bdr": "#8B5CF6"}
    ]

    curr_x = 0.7
    for p in pillars:
        box = patches.FancyBboxPatch((curr_x, 0.65), 1.65, 2.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=p["bg"], edgecolor=p["bdr"], lw=1.5)
        ax.add_patch(box)

        ax.text(curr_x + 0.82, 3.25, p["title"], ha='center', va='center', fontsize=7.8, fontweight='bold', color=p["bdr"])
        ax.text(curr_x + 0.82, 2.4, p["desc"], ha='center', va='center', fontsize=7.0, color='#334155', wrap=True,
                multialignment='center')

        # Code pill
        c_pill = patches.FancyBboxPatch((curr_x + 0.08, 0.85), 1.49, 0.85, boxstyle="square,pad=0.02",
                                        facecolor='#0F172A', edgecolor=p["bdr"])
        ax.add_patch(c_pill)
        ax.text(curr_x + 0.82, 1.25, p["code"], ha='center', va='center', fontsize=6.8, color='#38BDF8', linespacing=1.2)

        curr_x += 1.82

    save_fig(fig, "bab1_anatomi_sintaks_python_dasar.png")

# -------------------------------------------------------------
# 4. BAB 1: STRUKTUR KONDISI IF-ELIF-ELSE
# -------------------------------------------------------------
def make_bab1_if_elif_else():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#4338CA', edgecolor='#3730A3')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "STRUKTUR KEPUTUSAN MULTI-KONDISI: IF - ELIF - ELSE DALAM PYTHON",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Flowchart Left
    ax.text(2.0, 3.6, "Diagram Alur Keputusan Rapor:", fontsize=8.5, fontweight='bold', color='#1E293B')

    d1 = patches.Polygon([[2.0, 3.4], [2.9, 2.9], [2.0, 2.4], [1.1, 2.9]], closed=True, facecolor='#BAE6FD', edgecolor='#0284C7', lw=1.5)
    ax.add_patch(d1)
    ax.text(2.0, 2.9, "Nilai >= 85?", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0369A1')

    ax.annotate("YA", xy=(3.4, 2.9), xytext=(2.9, 2.9), arrowprops=dict(arrowstyle="->", color='#16A34A', lw=1.5))
    ax.text(3.7, 2.9, "Grade A", fontsize=7.5, fontweight='bold', color='#166534')

    ax.annotate("TIDAK", xy=(2.0, 2.0), xytext=(2.0, 2.4), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=1.5))

    d2 = patches.Polygon([[2.0, 2.0], [2.9, 1.5], [2.0, 1.0], [1.1, 1.5]], closed=True, facecolor='#FEF08A', edgecolor='#D97706', lw=1.5)
    ax.add_patch(d2)
    ax.text(2.0, 1.5, "Nilai >= 70?", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#92400E')

    ax.annotate("YA", xy=(3.4, 1.5), xytext=(2.9, 1.5), arrowprops=dict(arrowstyle="->", color='#16A34A', lw=1.5))
    ax.text(3.7, 1.5, "Grade B", fontsize=7.5, fontweight='bold', color='#854D0E')

    ax.annotate("TIDAK", xy=(2.0, 0.6), xytext=(2.0, 1.0), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=1.5))
    ax.text(2.0, 0.45, "Grade C (Else)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#991B1B')

    # Right: Python Script Box
    py_box = patches.FancyBboxPatch((4.7, 0.4), 3.4, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                    facecolor='#0F172A', edgecolor='#6366F1', lw=2)
    ax.add_patch(py_box)
    ax.text(6.4, 3.5, "Implementasi Python Bersih:", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#818CF8')

    code_if = (
        "nilai = int(input('Ketik nilai: '))\n\n"
        "if nilai >= 85:\n"
        "    grade = 'A (Istimewa)'\n"
        "elif nilai >= 70:\n"
        "    grade = 'B (Memuaskan)'\n"
        "elif nilai >= 60:\n"
        "    grade = 'C (Cukup)'\n"
        "else:\n"
        "    grade = 'Perlu Bimbingan'\n\n"
        "print(f'Predikat Rapor: {grade}')"
    )
    ax.text(4.9, 1.8, code_if, ha='left', va='center', fontsize=7.8, color='#F8FAFC', linespacing=1.2)

    save_fig(fig, "bab1_struktur_kondisi_if_elif_else.png")

# -------------------------------------------------------------
# 5. BAB 2: KOMIK PEMBUKA ANALISIS DATA
# -------------------------------------------------------------
def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#B45309', edgecolor='#92400E')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 2: DETEKTIF DATA MENGUNGKAP MISTERI KONSENTRASI BELAJAR",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Banyak Teman Mengantuk", "bg": "#FFFBEB", "bdr": "#D97706",
         "dialog": "Ayu:\n'Guru Bimbingan Konseling bilang, banyak siswa kelas 7-9 yang sering mengantuk saat jam pelajaran ketiga. Mengapa ya? Apakah karena kurang tidur atau melewatkan sarapan?'",
         "status": "Identifikasi Masalah"},
        {"x": 3.0, "title": "Panel 2: Survei Kuesioner Digital", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Rian:\n'Jangan menebak tanpa bukti! Mari kita sebar kuesioner digital anonim ke 100 siswa: tanyakan jam tidur, menu sarapan, dan tingkat fokus mereka di kelas!'",
         "status": "Pengumpulan Data"},
        {"x": 5.6, "title": "Panel 3: Angka yang Bercerita", "bg": "#EFF6FF", "bdr": "#2563EB",
         "dialog": "Fajar:\n'Luar biasa! Setelah diolah di spreadsheet, grafik menunjukkan 85% siswa yang sarapan bergizi memiliki fokus sangat baik! Mari kita buat poster data storytelling untuk kantin!'",
         "status": "Solusi Nyata"}
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
        ax.text(p["x"]+1.25, 2.95, "DATA\nSAINS", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab2_komik_pembuka_smp9.png")

# -------------------------------------------------------------
# 6. BAB 2: SIKLUS ANALISIS DATA SOSIAL
# -------------------------------------------------------------
def make_bab2_siklus_data():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "SIKLUS LENGKAP ANALISIS DATA KUANTITATIF: DARI MASALAH MENUJU AKSI",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "title": "RUMUSKAN MASALAH", "sub": "Pertanyaan Kunci", "desc": "Menentukan hipotesis: Apakah sarapan mempengaruhi fokus?", "bg": "#FEF3C7", "bdr": "#D97706", "x": 0.4},
        {"num": "2", "title": "SURVEI DIGITAL", "sub": "Google / MS Forms", "desc": "Kuesioner etis, opsi tertutup & skala Likert (1-5).", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 1.95},
        {"num": "3", "title": "BERSIHKAN DATA", "sub": "Data Cleaning", "desc": "Hapus jawaban ganda, periksa angka pencilan (*outliers*).", "bg": "#FAF5FF", "bdr": "#8B5CF6", "x": 3.5},
        {"num": "4", "title": "RUMUS STATISTIK", "sub": "Fungsi Spreadsheet", "desc": "Gunakan AVERAGE, COUNTIF, SUM untuk melihat korelasi.", "bg": "#ECFDF5", "bdr": "#10B981", "x": 5.05},
        {"num": "5", "title": "DATA STORYTELLING", "sub": "Grafik Dashboard", "desc": "Sajikan narasi visual untuk usulan menu kantin sehat!", "bg": "#FFF1F2", "bdr": "#F43F5E", "x": 6.6}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 0.6), 1.45, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        cir = patches.Circle((s["x"]+0.725, 3.2), 0.28, facecolor=s["bdr"], edgecolor='#FFFFFF', lw=1.5)
        ax.add_patch(cir)
        ax.text(s["x"]+0.725, 3.2, s["num"], ha='center', va='center', fontsize=12, fontweight='bold', color='#FFFFFF')

        ax.text(s["x"]+0.725, 2.65, s["title"], ha='center', va='center', fontsize=7.2, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.725, 2.4, s["sub"], ha='center', va='center', fontsize=6.8, color='#475569')

        ax.text(s["x"]+0.725, 1.5, s["desc"], ha='center', va='center', fontsize=7.0, color='#1E293B', wrap=True,
                multialignment='center')

    save_fig(fig, "bab2_siklus_analisis_data_sosial.png")

# -------------------------------------------------------------
# 7. BAB 2: PANDUAN PEMILIHAN GRAFIK DATA
# -------------------------------------------------------------
def make_bab2_panduan_grafik():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "PANDUAN PEMILIHAN GRAFIK: MEMILIH VISUAL YANG TEPAT UNTUK AUDIENS",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    charts = [
        {"title": "DIAGRAM BATANG (BAR)", "purpose": "PERBANDINGAN KATEGORI", "when": "Membandingkan jumlah pemilih menu kantin antar kelas 7, 8, dan 9 secara jelas.", "bg": "#EFF6FF", "bdr": "#3B82F6", "x": 0.5},
        {"title": "DIAGRAM GARIS (LINE)", "purpose": "TREN PERUBAHAN WAKTU", "when": "Melihat kenaikan tingkat kehadiran siswa dari hari Senin hingga Jumat.", "bg": "#ECFDF5", "bdr": "#10B981", "x": 3.1},
        {"title": "DIAGRAM LINGKARAN (PIE)", "purpose": "PROPORSI BAGIAN DARI 100%", "when": "Menampilkan persentase jenis transportasi siswa ke sekolah (jalan, sepeda, bus).", "bg": "#FFFBEB", "bdr": "#D97706", "x": 5.7}
    ]

    for c in charts:
        box = patches.FancyBboxPatch((c["x"], 0.4), 2.3, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                     facecolor=c["bg"], edgecolor=c["bdr"], lw=2)
        ax.add_patch(box)

        ax.text(c["x"]+1.15, 3.25, c["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=c["bdr"])
        ax.text(c["x"]+1.15, 2.95, c["purpose"], ha='center', va='center', fontsize=7.2, fontweight='bold', color='#334155')

        ax.text(c["x"]+1.15, 1.8, c["when"], ha='center', va='center', fontsize=7.6, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((c["x"]+0.15, 0.65), 2.0, 0.4, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=c["bdr"], edgecolor=c["bdr"])
        ax.add_patch(pill)
        ax.text(c["x"]+1.15, 0.85, "PILIHAN TEPAT", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab2_panduan_pemilihan_grafik_data.png")

# -------------------------------------------------------------
# 8. BAB 2: INFOGRAFIS DE-IDENTIFIKASI DATA
# -------------------------------------------------------------
def make_bab2_deidentifikasi():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E293B', edgecolor='#0F172A')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "ETIKA PRIVASI RISET: DE-IDENTIFIKASI & ANONIMITAS RESPONDEN",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Before vs After
    b1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFF1F2', edgecolor='#F43F5E', lw=2)
    ax.add_patch(b1)
    ax.text(2.2, 3.4, "DATA MENTAH BERBAHAYA (RAW)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#BE123C')
    txt_raw = (
        "Memuat Identitas Pribadi Terbuka:\n"
        "- Nama Lengkap: Ayu Sekar\n"
        "- Nomor Induk Siswa: 20240981\n"
        "- Nomor HP: 08123456789\n"
        "- Jawaban: 'Sering menangis di kelas'\n\n"
        "BAHAYA BESAR:\n"
        "Jika data bocor, privasi responden hancur\n"
        "dan dapat memicu perundungan siber!"
    )
    ax.text(0.6, 1.8, txt_raw, ha='left', va='center', fontsize=7.6, color='#4C0519', linespacing=1.2)

    b2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#ECFDF5', edgecolor='#10B981', lw=2)
    ax.add_patch(b2)
    ax.text(6.3, 3.4, "DATA SETELAH DE-IDENTIFIKASI", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#065F46')
    txt_clean = (
        "Identitas Dibuat Anonim & Agregat:\n"
        "- Kode Responden: Siswa_#042\n"
        "- Usia / Tingkat: 14 Tahun / Kelas IX\n"
        "- Nomor Kontak: DIHAPUS PERMANEN\n"
        "- Jawaban: 'Kategori C (Perlu Pendampingan)'\n\n"
        "KEUNGGULAN ETIS:\n"
        "v Aman dipublikasikan dalam laporan\n"
        "v Melindungi martabat & kerahasiaan siswa\n"
        "v Sesuai standar hukum UU PDP!"
    )
    ax.text(4.7, 1.8, txt_clean, ha='left', va='center', fontsize=7.6, color='#064E3B', linespacing=1.2)

    save_fig(fig, "bab2_infografis_deidentifikasi_data.png")

# -------------------------------------------------------------
# 9. BAB 3: KOMIK PEMBUKA REGULASI HUKUM AI
# -------------------------------------------------------------
def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#4338CA', edgecolor='#3730A3')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 3: SIMULASI SIDANG SEMU KASUS HAK CIPTA KARYA AI",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Juara Lomba Lukis AI", "bg": "#EEF2FF", "bdr": "#6366F1",
         "dialog": "Fajar:\n'Ada kabar heboh! Sebuah lukisan digital memenangkan juara 1 festival seni, tetapi ternyata seluruh gambarnya dihasilkan oleh generator AI hanya dengan mengetik 2 baris prompt!'",
         "status": "Kontroversi Karya Seni"},
        {"x": 3.0, "title": "Panel 2: Gugatan Seniman Asli", "bg": "#FFF1F2", "bdr": "#F43F5E",
         "dialog": "Ayu:\n'Para seniman pelukis asli protes keras! Model AI tersebut ternyata dilatih menggunakan jutaan karya mereka tanpa izin! Siapakah pemilik hak cipta sebenarnya?'",
         "status": "Dilema Hak Cipta"},
        {"x": 5.6, "title": "Panel 3: Hukum Siber Indonesia", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Rian:\n'Ayo kita gelar simulasi sidang semu di kelas! Kita bedah undang-undang hak cipta dan UU ITE untuk melihat batas legalitas etika teknologi masa kini!'",
         "status": "Sidang Etika Dimulai"}
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
        ax.text(p["x"]+1.25, 2.95, "SIDANG\nETIKA", ha='center', va='center', fontsize=7.5, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab3_komik_pembuka_smp9.png")

# -------------------------------------------------------------
# 10. BAB 3: TIMBANGAN KEADILAN HUKUM SIBER
# -------------------------------------------------------------
def make_bab3_hukum_siber():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E293B', edgecolor='#0F172A')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "PAYUNG HUKUM RUANG SIBER INDONESIA: MEMAHAMI UU ITE DAN UU PDP",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Card Left: UU ITE
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.5, "UU ITE (INFORMASI & TRANSAKSI ELEKTRONIK)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1D4ED8')
    txt_ite = (
        "Fokus Penegakan Hukum:\n"
        "v Larangan menyebarkan berita bohong (hoaks)\n"
        "  yang memicu keonaran di masyarakat.\n"
        "v Larangan pencemaran nama baik & fitnah siber.\n"
        "v Larangan meretas (*hacking*) atau mengakses\n"
        "  sistem komputer orang lain tanpa izin.\n"
        "v Menjamin keabsahan transaksi digital.\n\n"
        "Sanksi: Denda miliaran rupiah & pidana penjara!"
    )
    ax.text(0.6, 1.8, txt_ite, ha='left', va='center', fontsize=7.5, color='#1E293B', linespacing=1.2)

    # Card Right: UU PDP
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#ECFDF5', edgecolor='#059669', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.5, "UU PDP (PERLINDUNGAN DATA PRIBADI)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#065F46')
    txt_pdp = (
        "Fokus Perlindungan Hak Asasi Warga:\n"
        "v Setiap warga negara berhak atas kerahasiaan\n"
        "  data pribadinya (NIK, rekam medis, biometrik).\n"
        "v Perusahaan/pengembang aplikasi WAJIB meminta\n"
        "  persetujuan jelas sebelum mengumpulkan data.\n"
        "v Hak warga untuk menghapus data miliknya.\n"
        "v Kewajiban enkripsi ketat mencegah kebocoran.\n\n"
        "Menjamin kedaulatan & keamanan warga di ruang maya."
    )
    ax.text(4.7, 1.8, txt_pdp, ha='left', va='center', fontsize=7.5, color='#064E3B', linespacing=1.2)

    save_fig(fig, "bab3_timbangan_keadilan_hukum_siber.png")

# -------------------------------------------------------------
# 11. BAB 3: DILEMA TANGGUNG JAWAB MORAL AI
# -------------------------------------------------------------
def make_bab3_dilema_moral():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#991B1B', edgecolor='#7F1D1D')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "SEGITIGA TANGGUNG JAWAB: SIAPA YANG BERSALAH ATAS KEGAGALAN AI?",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Central Triangle
    # Apex: Pengembang
    box_dev = patches.FancyBboxPatch((3.2, 2.7), 2.1, 0.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(box_dev)
    ax.text(4.25, 3.3, "PENGEMBANG (DEVELOPER)", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1D4ED8')
    ax.text(4.25, 2.95, "Bertanggung jawab atas arsitektur\nkode, keamanan & pengujian.", ha='center', va='center', fontsize=6.8, color='#334155')

    # Bottom Left: Penyedia Data
    box_data = patches.FancyBboxPatch((0.5, 0.6), 2.5, 0.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                      facecolor='#FEF3C7', edgecolor='#D97706', lw=2)
    ax.add_patch(box_data)
    ax.text(1.75, 1.2, "PENYEDIA DATA LATIH", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#B45309')
    ax.text(1.75, 0.85, "Bertanggung jawab atas keakuratan,\nkeberagaman & keadilan data.", ha='center', va='center', fontsize=6.8, color='#334155')

    # Bottom Right: Operator Manusia
    box_oper = patches.FancyBboxPatch((5.5, 0.6), 2.5, 0.9, boxstyle="round,pad=0.04,rounding_size=0.08",
                                      facecolor='#ECFDF5', edgecolor='#10B981', lw=2)
    ax.add_patch(box_oper)
    ax.text(6.75, 1.2, "OPERATOR MANUSIA (USER)", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#065F46')
    ax.text(6.75, 0.85, "Bertanggung jawab atas keputusan final\ndan pengawasan etis (Oversight).", ha='center', va='center', fontsize=6.8, color='#334155')

    # Center circle: Sistem AI
    cir_ai = patches.Circle((4.25, 1.6), 0.55, facecolor='#1E293B', edgecolor='#EF4444', lw=2)
    ax.add_patch(cir_ai)
    ax.text(4.25, 1.6, "SISTEM AI\n(Bukan Subjek\nHukum)", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#FFFFFF')

    # Connecting lines
    ax.plot([3.2, 2.0], [2.7, 1.5], color='#94A3B8', lw=1.5, ls='--')
    ax.plot([5.3, 6.5], [2.7, 1.5], color='#94A3B8', lw=1.5, ls='--')
    ax.plot([3.0, 5.5], [1.05, 1.05], color='#94A3B8', lw=1.5, ls='--')

    save_fig(fig, "bab3_dilema_tanggung_jawab_moral_ai.png")

# -------------------------------------------------------------
# 12. BAB 3: PETA KETERAMPILAN MASA DEPAN AI
# -------------------------------------------------------------
def make_bab3_keterampilan_masa_depan():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#0D9488', edgecolor='#0F766E')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "MEMPERSIAPKAN MASA DEPAN: KETERAMPILAN UNIK MANUSIA YANG TAK TERGANTIKAN AI",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    skills = [
        {"title": "1. EMPATI & KASIH", "desc": "Mendengarkan dengan hati, memahami duka sesama, dan merawat hubungan sosial.", "icon": "HATI", "bg": "#FFF1F2", "bdr": "#F43F5E", "x": 0.5},
        {"title": "2. KREATIVITAS ORISINAL", "desc": "Melahirkan gagasan baru di luar pola masa lalu; berani mengambil risiko seni.", "icon": "KARYA", "bg": "#FEF3C7", "bdr": "#D97706", "x": 2.45},
        {"title": "3. PENALARAN ETIS", "desc": "Membedakan benar dan salah; memperjuangkan keadilan sosial di atas keuntungan.", "icon": "MORAL", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 4.4},
        {"title": "4. KEPEMIMPINAN", "desc": "Menginspirasi tim, menggerakkan gotong royong, dan memimpin perubahan peradaban.", "icon": "PEMIMPIN", "bg": "#ECFDF5", "bdr": "#10B981", "x": 6.35}
    ]

    for s in skills:
        box = patches.FancyBboxPatch((s["x"], 0.5), 1.65, 3.1, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        cir = patches.Circle((s["x"]+0.825, 3.1), 0.28, facecolor=s["bdr"], edgecolor='#FFFFFF', lw=1.5)
        ax.add_patch(cir)
        ax.text(s["x"]+0.825, 3.1, s["icon"][0], ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

        ax.text(s["x"]+0.825, 2.55, s["title"], ha='center', va='center', fontsize=7.6, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.825, 1.5, s["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B', wrap=True,
                multialignment='center')

    save_fig(fig, "bab3_peta_keterampilan_masa_depan_ai.png")

# -------------------------------------------------------------
# 13. BAB 4: KOMIK PEMBUKA CAPSTONE PROJECT
# -------------------------------------------------------------
def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#047857', edgecolor='#065F46')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 4: SPRINT CAPSTONE PROJECT MENUJU PAMERAN KELULUSAN",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Empati Masalah Sekolah", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Ayu:\n'Kantin dan bank sampah sekolah kita sering kewalahan mencatat setoran botol plastik secara manual di buku tulis tipis yang mudah sobek!'",
         "status": "Empathize & Define"},
        {"x": 3.0, "title": "Panel 2: Kolaborasi Prototipe", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Rian:\n'Ayo kita bangun Bank Sampah Digital! Aku buat program pencatatan saldo tabungan sampah pakai Python, dan Fajar siapkan poster panduan pilah sampah!'",
         "status": "Ideate & Prototype"},
        {"x": 5.6, "title": "Panel 3: Exhibition Day Kelulusan", "bg": "#FFFBEB", "bdr": "#F59E0B",
         "dialog": "Fajar:\n'Semua murid, guru, dan orang tua memuji karya kita di hari pameran! Ini adalah bukti nyata bahwa anak SMP bisa melahirkan inovasi untuk masyarakat!'",
         "status": "Tuntas Fase D!"}
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
        ax.text(p["x"]+1.25, 2.95, "CAPSTONE\nINOVASI", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab4_komik_pembuka_smp9.png")

# -------------------------------------------------------------
# 14. BAB 4: LIMA TAHAP DESIGN THINKING
# -------------------------------------------------------------
def make_bab4_design_thinking():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#4F46E5', edgecolor='#4338CA')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "METODOLOGI DESIGN THINKING: LIMA TAHAP INOVASI DIGITAL INKLUSIF",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    stages = [
        {"num": "1", "name": "EMPATHIZE", "sub": "Mendengar & Peduli", "desc": "Wawancara pengguna untuk memahami keluh kesah nyata di lapangan.", "bg": "#FFF1F2", "bdr": "#F43F5E", "x": 0.4},
        {"num": "2", "name": "DEFINE", "sub": "Merumuskan Masalah", "desc": "Menetapkan rumusan kebutuhan inti: Bagaimana kita bisa membantu?", "bg": "#FEF3C7", "bdr": "#D97706", "x": 1.95},
        {"num": "3", "name": "IDEATE", "sub": "Curah Pendapat Liar", "desc": "Mengumpulkan puluhan ide solusi koding & media tanpa menghakimi.", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 3.5},
        {"num": "4", "name": "PROTOTYPE", "sub": "Membangun Versi 1.0", "desc": "Membuat aplikasi Python sederhana atau dashboard spreadsheet cepat.", "bg": "#ECFDF5", "bdr": "#10B981", "x": 5.05},
        {"num": "5", "name": "TEST", "sub": "Uji Coba Pengguna", "desc": "Meminta warga sekolah mencoba langsung dan memberi masukan jujur.", "bg": "#FAF5FF", "bdr": "#8B5CF6", "x": 6.6}
    ]

    for s in stages:
        box = patches.FancyBboxPatch((s["x"], 0.6), 1.45, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        cir = patches.Circle((s["x"]+0.725, 3.2), 0.28, facecolor=s["bdr"], edgecolor='#FFFFFF', lw=1.5)
        ax.add_patch(cir)
        ax.text(s["x"]+0.725, 3.2, s["num"], ha='center', va='center', fontsize=12, fontweight='bold', color='#FFFFFF')

        ax.text(s["x"]+0.725, 2.65, s["name"], ha='center', va='center', fontsize=7.8, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.725, 2.4, s["sub"], ha='center', va='center', fontsize=6.8, color='#475569')

        ax.text(s["x"]+0.725, 1.5, s["desc"], ha='center', va='center', fontsize=7.0, color='#1E293B', wrap=True,
                multialignment='center')

    save_fig(fig, "bab4_lima_tahap_design_thinking.png")

# -------------------------------------------------------------
# 15. BAB 4: ALUR SPRINT CAPSTONE PROJECT
# -------------------------------------------------------------
def make_bab4_alur_sprint():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#065F46', edgecolor='#064E3B')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "JADWAL SPRINT 4 MINGGU PROYEK CAPSTONE KELULUSAN FASE D",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    sprints = [
        {"week": "MINGGU 1", "title": "RISET & EMPATI", "items": ["* Memilih tema proyek", "* Wawancara 5 responden", "* Rumusan masalah (Define)"], "bg": "#EFF6FF", "bdr": "#3B82F6", "x": 0.5},
        {"week": "MINGGU 2", "title": "KODING PROTOTIPE", "items": ["* Penulisan skrip Python", "* Desain antarmuka konsol", "* Debugging logika dasar"], "bg": "#ECFDF5", "bdr": "#10B981", "x": 2.45},
        {"week": "MINGGU 3", "title": "UJI PENGGUNA", "items": ["* Uji coba bersama teman", "* Pencatatan saran perbaikan", "* Pembuatan poster media"], "bg": "#FEF3C7", "bdr": "#D97706", "x": 4.4},
        {"week": "MINGGU 4", "title": "EXHIBITION DAY", "items": ["* Pameran karya sekolah", "* Presentasi tim inovator", "* Evaluasi Portofolio D"], "bg": "#FAF5FF", "bdr": "#9333EA", "x": 6.35}
    ]

    for s in sprints:
        box = patches.FancyBboxPatch((s["x"], 0.5), 1.65, 3.1, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        ax.text(s["x"]+0.825, 3.25, s["week"], ha='center', va='center', fontsize=8.2, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.825, 2.95, s["title"], ha='center', va='center', fontsize=7.2, fontweight='bold', color='#334155')

        y_it = 2.4
        for it in s["items"]:
            ax.text(s["x"]+0.15, y_it, it, ha='left', va='center', fontsize=6.8, color='#1E293B')
            y_it -= 0.45

    save_fig(fig, "bab4_alur_sprint_capstone_project.png")

# -------------------------------------------------------------
# 16. COVER BUKU SISWA SMP KELAS 9
# -------------------------------------------------------------
def make_cover_smp9():
    img = Image.new('RGB', (1800, 2700), color='#064E3B')
    draw = ImageDraw.Draw(img)

    for y in range(800):
        ratio = y / 800
        r = int(6 + (4 - 6) * ratio)
        g = int(78 + (120 - 78) * ratio)
        b = int(59 + (87 - 59) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(800, 1900):
        ratio = (y - 800) / 1100
        r = int(4 + (2 - 4) * ratio)
        g = int(120 + (132 - 120) * ratio)
        b = int(87 + (199 - 87) * ratio)
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

    draw.rectangle([100, 90, 820, 160], fill='#059669')
    draw.text((130, 102), "BUKU TEKS PELAJARAN SMP/MTs", font=f_badge, fill='#FFFFFF')

    draw.text((100, 260), "KODING DAN", font=f_title, fill='#FFFFFF')
    draw.text((100, 370), "KECERDASAN", font=f_title, fill='#34D399')
    draw.text((100, 480), "ARTIFISIAL", font=f_title, fill='#FACC15')

    # Grade Pill Badge
    draw.rectangle([100, 620, 950, 720], fill='#D97706')
    draw.text((130, 642), "KELAS IX  •  FASE D (SMP/MTs)", font=f_phase, fill='#FFFFFF')

    # Big Rounded Showcase Card
    draw.rounded_rectangle([150, 820, 1650, 1920], radius=40, fill='#0F172A', outline='#34D399', width=8)

    draw.text((220, 900), "KURIKULUM NASIONAL KKA KEMENDIKDASMEN RI", font=f_badge, fill='#FACC15')
    draw.text((220, 980), "Puncak Penuntasan Kompetensi Menengah Pertama (Fase D):", font=f_sub, fill='#FFFFFF')

    features = [
        "v  Transisi Pemrograman Tekstual: Fondasi Sintaks Bahasa Python",
        "v  Variabel, Input Dinamis & Struktur Logika if-elif-else serta Perulangan",
        "v  Pengolahan Data Lapangan Kuantitatif & Narasi Visual (Data Storytelling)",
        "v  Hukum & Etika Digital: Membedah Regulasi UU ITE & UU Perlindungan Data",
        "v  Dilema Moral Sistem Cerdas & Peta Keterampilan Abadi Manusia di Era AI",
        "v  Capstone Project Akhir Fase D Berbasis Metodologi Design Thinking"
    ]

    curr_y = 1080
    for feat in features:
        draw.text((220, curr_y), feat, font=f_phase, fill='#E2E8F0')
        curr_y += 120

    # Author Box
    draw.rounded_rectangle([100, 2020, 1700, 2300], radius=30, fill='#FFFFFF', outline='#059669', width=5)
    draw.text((150, 2060), "Penulis: Gede Erik Aktama, S.Pd., M.Pd.", font=f_auth, fill='#0F172A')
    draw.text((150, 2130), "Fasilitator Nasional Bimbingan Teknis & ToT KKA Kemendikdasmen RI", font=f_role, fill='#059669')
    draw.text((150, 2185), "Dosen Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", font=f_role, fill='#475569')

    # Publisher Footer
    draw.text((900, 2390), "PUSAT PERBUKUAN", font=f_pub, fill='#FFFFFF', anchor="mm")
    draw.text((900, 2450), "BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2505), "KEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2560), "TAHUN 2025 / 2026", font=f_subpub, fill='#FACC15', anchor="mm")

    local_cov = os.path.join(local_assets, "cover_buku_siswa_smp9.jpg")
    img.save(local_cov, quality=95)
    tot_cov = os.path.join(tot_assets, "cover_buku_siswa_smp9.jpg")
    try:
        shutil.copy2(local_cov, tot_cov)
    except Exception as e:
        print(f"Warning copying cover: {e}")
    print("Generated cover: cover_buku_siswa_smp9.jpg")

if __name__ == "__main__":
    print("Starting visual assets generation for Grade 9 SMP...")
    make_tokoh_sahabat()
    make_bab1_komik()
    make_bab1_jembatan()
    make_bab1_anatomi_python()
    make_bab1_if_elif_else()
    make_bab2_komik()
    make_bab2_siklus_data()
    make_bab2_panduan_grafik()
    make_bab2_deidentifikasi()
    make_bab3_komik()
    make_bab3_hukum_siber()
    make_bab3_dilema_moral()
    make_bab3_keterampilan_masa_depan()
    make_bab4_komik()
    make_bab4_design_thinking()
    make_bab4_alur_sprint()
    make_cover_smp9()
    print("All visual assets for Grade 9 SMP successfully generated!")
