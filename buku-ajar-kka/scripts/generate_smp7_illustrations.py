# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Buku KKA Kelas 7 SMP (Fase D)
Resolusi Tinggi 300 DPI, Desain Infografis Edukatif & Komik Remaja,
Modern, Penuh Warna, Sesuai Standar Kemendikdasmen & Kurikulum Nasional.
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-7-smp\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 7 SMP\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

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
# 0. TOKOH SAHABAT BELAJAR KELAS 7 SMP
# -------------------------------------------------------------
def make_tokoh_sahabat():
    fig, ax = plt.subplots(figsize=(8.0, 3.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.6); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 2.9), 7.2, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor='#0D9488', edgecolor='#0F766E')
    ax.add_patch(title_box)
    ax.text(4.0, 3.17, "TIGA SAHABAT INOVATOR REMAJA KODING & KA KELAS VII SMP",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    tokohs = [
        {"nama": "RIAN", "role": "Analis Data Sosial", "ciri": "Siswa aktif, gemar survei lapangan, fotografi & matematika", "color": "#0284C7", "bg": "#E0F2FE", "x": 0.5},
        {"nama": "AYU", "role": "Desainer Visual", "ciri": "Siswi kreatif, hobi ilustrasi digital, infografis & tipografi", "color": "#D97706", "bg": "#FFFBEB", "x": 3.0},
        {"nama": "FAJAR", "role": "Penyelidik AI & Etika", "ciri": "Siswa kritis, penasaran sistem cerdas, deepfake & keadilan", "color": "#7C3AED", "bg": "#F5F3FF", "x": 5.5},
    ]

    for t in tokohs:
        card = patches.FancyBboxPatch((t["x"], 0.25), 2.0, 2.5, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=t["bg"], edgecolor=t["color"], linewidth=2)
        ax.add_patch(card)

        # Avatar circle
        circle = patches.Circle((t["x"] + 1.0, 2.05), 0.5, facecolor=t["color"], edgecolor='#FFFFFF', linewidth=2)
        ax.add_patch(circle)
        ax.text(t["x"] + 1.0, 2.05, t["nama"][0], ha='center', va='center', fontsize=16, fontweight='bold', color='#FFFFFF')

        # Nama & Role
        ax.text(t["x"] + 1.0, 1.35, t["nama"], ha='center', va='center', fontsize=10.5, fontweight='bold', color=t["color"])
        ax.text(t["x"] + 1.0, 1.1, t["role"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#334155')

        # Deskripsi
        ax.text(t["x"] + 1.0, 0.65, t["ciri"], ha='center', va='center', fontsize=7.5, color='#475569', wrap=True,
                multialignment='center')

    save_fig(fig, "gambar_tokoh_sahabat_smp7.png")

# -------------------------------------------------------------
# 1. BAB 1: KOMIK PEMBUKA DATA SOSIAL
# -------------------------------------------------------------
def make_bab1_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0D9488', edgecolor='#0F766E')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK INOVATOR REMAJA: MISTERI ANTREAN PANJANG KANTIN SEKOLAH",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Kekacauan Istirahat", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "RIAN:\n\"Aduh! Waktu istirahat tinggal 10 menit,\ntapi antrean beli makanan masih\nmengular panjang sampai ke lorong!\nBanyak teman belum sempat makan!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Bukan Sekadar Mengeluh", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "AYU:\n\"Mengeluh tidak akan menyelesaikan masalah!\nBagaimana kalau kita catat datanya?\nBerapa menit waktu rata-rata\npelayanan tiap kasir kantin?\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Fajar Beraksi", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "FAJAR:\n\"Bagus sekali idemu, Ayu!\nData adalah fakta nyata!\nKita kumpulkan data transaksi,\nbuat tabel frekuensi dan grafik,\nlalu uraikan akar masalahnya!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Algoritma Solusi", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "TIM INOVATOR:\n\"Dengan Diagram Alur Flowchart,\nkita rancang sistem pre-order digital!\nAntrean terurai dari 15 menit\nmenjadi hanya 2 menit!\nData mengubah segalanya!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        tag = patches.FancyBboxPatch((p["x"]+0.1, p["y"]+1.55), 1.6, 0.28, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=p["col"], edgecolor=p["col"])
        ax.add_patch(tag)
        ax.text(p["x"]+0.9, p["y"]+1.69, p["num"] + ": " + p["title"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"]+1.9, p["y"]+0.75, p["dialog"], ha='center', va='center',
                fontsize=8.5, color='#1E293B', multialignment='center')

    save_fig(fig, "bab1_komik_pembuka_smp7.png")

# -------------------------------------------------------------
# 2. BAB 1: INFOGRAFIS SIKLUS PENGELOLAAN DATA
# -------------------------------------------------------------
def make_bab1_siklus_data():
    fig, ax = plt.subplots(figsize=(8.0, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.0); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.4), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 3.62, "SIKLUS PENGELOLAAN DATA SOSIAL: DARI FAKTA MENTAH MENJADI KEBIJAKAN",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "title": "PENGUMPULAN", "sub": "Survei & Observasi", "desc": "Mencatat angka antrean,\nwawancara petugas kantin,\nmengumpulkan kuisioner.", "col": "#0284C7", "bg": "#E0F2FE", "x": 0.4},
        {"num": "2", "title": "ORGANISASI", "sub": "Tabel & Grafik", "desc": "Menyusun tabel frekuensi,\ndiagram batang antrean,\ndan grafik waktu layanan.", "col": "#D97706", "bg": "#FFFBEB", "x": 2.25},
        {"num": "3", "title": "ANALISIS", "sub": "Pola & Dekomposisi", "desc": "Menemukan titik kemacetan\n(bottleneck) saat transaksi\npembayaran uang tunai.", "col": "#7C3AED", "bg": "#F5F3FF", "x": 4.1},
        {"num": "4", "title": "KEPUTUSAN", "sub": "Aksi Berbasis Data", "desc": "Merumuskan solusi digital:\nsistem kupon / kartu pintar\nuntuk percepat antrean.", "col": "#059669", "bg": "#ECFDF5", "x": 5.95},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.35), 1.65, 2.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=s["bg"], edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        circle = patches.Circle((s["x"]+0.825, 2.75), 0.28, facecolor=s["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(s["x"]+0.825, 2.75, s["num"], ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')
        ax.text(s["x"]+0.825, 2.2, s["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=s["col"])
        ax.text(s["x"]+0.825, 1.85, s["sub"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')
        ax.text(s["x"]+0.825, 1.0, s["desc"], ha='center', va='center', fontsize=7, color='#475569', multialignment='center')

    # Connecting arrows
    for ax_x in [2.1, 3.95, 5.8]:
        ax.annotate('', xy=(ax_x+0.1, 1.75), xytext=(ax_x-0.05, 1.75), arrowprops=dict(arrowstyle="->", lw=2, color="#64748B"))

    save_fig(fig, "bab1_infografis_siklus_data.png")

# -------------------------------------------------------------
# 3. BAB 1: FLOWCHART STANDAR ISO
# -------------------------------------------------------------
def make_bab1_flowchart():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title_box)
    ax.text(4.0, 4.02, "STANDAR SIMBOL FLOWCHART ISO: SISTEM PEMBAYARAN KANTIN",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Terminator Start
    start = patches.FancyBboxPatch((3.0, 3.1), 2.0, 0.4, boxstyle="round,pad=0.04,rounding_size=0.2",
                                   facecolor='#10B981', edgecolor='#059669', linewidth=1.5)
    ax.add_patch(start)
    ax.text(4.0, 3.3, "Mulai (Terminator)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

    ax.annotate('', xy=(4.0, 2.5), xytext=(4.0, 3.1), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))

    # Input Parallelogram
    input_box = patches.Polygon([[3.0, 2.1], [5.2, 2.1], [4.8, 2.5], [2.6, 2.5]],
                                closed=True, facecolor='#E0F2FE', edgecolor='#0284C7', linewidth=1.5)
    ax.add_patch(input_box)
    ax.text(3.9, 2.3, "Input: Pindai Kartu Siswa", ha='center', va='center', fontsize=8, fontweight='bold', color='#0369A1')

    ax.annotate('', xy=(4.0, 1.7), xytext=(4.0, 2.1), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))

    # Decision Diamond
    diamond = patches.Polygon([[4.0, 1.7], [5.5, 1.2], [4.0, 0.7], [2.5, 1.2]],
                              closed=True, facecolor='#FEF08A', edgecolor='#CA8A04', linewidth=1.5)
    ax.add_patch(diamond)
    ax.text(4.0, 1.2, "Apakah Saldo\nCukup?", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#854D0E')

    # YA -> Output Kanan
    ax.annotate('', xy=(6.8, 1.2), xytext=(5.5, 1.2), arrowprops=dict(arrowstyle="->", lw=1.8, color="#059669"))
    ax.text(6.15, 1.35, "YA", fontsize=8, fontweight='bold', color='#059669')

    proc_ya = patches.FancyBboxPatch((6.0, 0.2), 1.7, 0.65, boxstyle="round,pad=0.03,rounding_size=0.08",
                                     facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=1.5)
    ax.add_patch(proc_ya)
    ax.text(6.85, 0.52, "Kurangi Saldo &\nCetak Struk Makanan", ha='center', va='center', fontsize=7, fontweight='bold', color='#15803D')

    # TIDAK -> Output Kiri
    ax.annotate('', xy=(1.2, 1.2), xytext=(2.5, 1.2), arrowprops=dict(arrowstyle="->", lw=1.8, color="#DC2626"))
    ax.text(1.85, 1.35, "TIDAK", fontsize=8, fontweight='bold', color='#DC2626')

    proc_tidak = patches.FancyBboxPatch((0.3, 0.2), 1.7, 0.65, boxstyle="round,pad=0.03,rounding_size=0.08",
                                        facecolor='#FEE2E2', edgecolor='#DC2626', linewidth=1.5)
    ax.add_patch(proc_tidak)
    ax.text(1.15, 0.52, "Tampilkan Pesan:\n'Saldo Tidak Cukup'", ha='center', va='center', fontsize=7, fontweight='bold', color='#B91C1C')

    save_fig(fig, "bab1_flowchart_standar_iso.png")

# -------------------------------------------------------------
# 4. BAB 1: DIAGRAM FISHBONE (TULANG IKAN)
# -------------------------------------------------------------
def make_bab1_fishbone():
    fig, ax = plt.subplots(figsize=(8.0, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.0); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.4), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(title_box)
    ax.text(4.0, 3.62, "DEKOMPOSISI MASALAH: DIAGRAM TULANG IKAN (FISHBONE DIAGRAM)",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Central Backbone Arrow
    ax.annotate('', xy=(6.2, 1.7), xytext=(0.8, 1.7), arrowprops=dict(arrowstyle="->", lw=4, color="#334155"))

    # Fish Head (Problem Statement)
    head_box = patches.FancyBboxPatch((6.3, 1.15), 1.4, 1.1, boxstyle="round,pad=0.05,rounding_size=0.15",
                                      facecolor='#EF4444', edgecolor='#B91C1C', linewidth=2)
    ax.add_patch(head_box)
    ax.text(7.0, 1.7, "MASALAH:\nAntrean Kantin\nMenumpuk di\nJam Istirahat", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color='#FFFFFF')

    # 4 Ribs (Bones)
    ribs = [
        {"cat": "MANUSIA", "desc": "• Pembeli lama memilih menu\n• Petugas repot cari kembalian", "x": 2.0, "y_top": 2.9, "col": "#0284C7"},
        {"cat": "METODE", "desc": "• Pesan & bayar di satu titik\n• Tidak ada antrean khusus", "x": 4.5, "y_top": 2.9, "col": "#D97706"},
        {"cat": "ALAT / TEKNOLOGI", "desc": "• Masih pakai uang tunai fisik\n• Belum ada sistem pre-order", "x": 2.0, "y_top": 0.5, "col": "#059669"},
        {"cat": "LINGKUNGAN", "desc": "• Lorong kantin sempit\n• Jam istirahat serentak", "x": 4.5, "y_top": 0.5, "col": "#7C3AED"},
    ]

    for r in ribs:
        if r["y_top"] > 2.0:
            ax.annotate('', xy=(r["x"]+0.8, 1.7), xytext=(r["x"], r["y_top"]-0.3),
                        arrowprops=dict(arrowstyle="->", lw=2, color=r["col"]))
            ax.text(r["x"]-0.1, r["y_top"], r["cat"], fontsize=8, fontweight='bold', color=r["col"])
            ax.text(r["x"]-0.1, r["y_top"]-0.45, r["desc"], fontsize=6.8, color='#334155')
        else:
            ax.annotate('', xy=(r["x"]+0.8, 1.7), xytext=(r["x"], r["y_top"]+0.5),
                        arrowprops=dict(arrowstyle="->", lw=2, color=r["col"]))
            ax.text(r["x"]-0.1, r["y_top"]+0.4, r["cat"], fontsize=8, fontweight='bold', color=r["col"])
            ax.text(r["x"]-0.1, r["y_top"]-0.05, r["desc"], fontsize=6.8, color='#334155')

    save_fig(fig, "bab1_diagram_fishbone_masalah.png")

# -------------------------------------------------------------
# 5. BAB 2: KOMIK PEMBUKA DESAIN SLIDE
# -------------------------------------------------------------
def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK INOVATOR REMAJA: SENI MENYAMPAIKAN GAGASAN LEWAT DESAIN VISUAL",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Slide Teks Rapat", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "AYU:\n\"Teman-teman, lihat slide presentasiku!\nSeluruh isi buku kurangkum\nke dalam satu slide penuh!\nKenapa malah membuat pusing ya?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Fajar Mengamati", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "FAJAR:\n\"Wah, Ayu! Itu bukan slide presentasi,\ntapi memindahkan koran ke layar!\nHurufnya rapat dan warnanya tabrakan,\naudiens pasti bosan membacanya!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Rian Mengenalkan CRAP", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "RIAN:\n\"Kita butuh Prinsip Desain C.R.A.P!\nContrast, Repetition, Alignment, Proximity!\nBuat judul tegas, ruang kosong lega,\ndan gunakan ikon vektor yang memikat!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Infografis Memukau", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "TIM INOVATOR:\n\"Luar biasa! Setelah ditata ulang,\npesan peduli lingkungan kita\nlangsung dipahami audiens!\nDesain yang baik menyelamatkan ide!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        tag = patches.FancyBboxPatch((p["x"]+0.1, p["y"]+1.55), 1.6, 0.28, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=p["col"], edgecolor=p["col"])
        ax.add_patch(tag)
        ax.text(p["x"]+0.9, p["y"]+1.69, p["num"] + ": " + p["title"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"]+1.9, p["y"]+0.75, p["dialog"], ha='center', va='center',
                fontsize=8.5, color='#1E293B', multialignment='center')

    save_fig(fig, "bab2_komik_pembuka_smp7.png")

# -------------------------------------------------------------
# 6. BAB 2: PRINSIP DESAIN CRAP
# -------------------------------------------------------------
def make_bab2_crap():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(title_box)
    ax.text(4.0, 4.04, "4 PRINSIP DESAIN KOMUNIKASI VISUAL EFEKTIF (C.R.A.P)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    cards = [
        {"letter": "C", "nama": "CONTRAST\n(Kontras)", "desc": "Bedakan judul dan isi teks\nsecara tegas menggunakan\nukuran & warna berbeda.", "col": "#DC2626", "bg": "#FEF2F2", "x": 0.4},
        {"letter": "R", "nama": "REPETITION\n(Pengulangan)", "desc": "Gunakan gaya visual, palet\nwarna, & jenis font yang sama\ndi seluruh halaman slide.", "col": "#0284C7", "bg": "#F0F9FF", "x": 2.25},
        {"letter": "A", "nama": "ALIGNMENT\n(Perataan)", "desc": "Susun elemen secara sejajar\n(rata kiri / tengah) agar\ntata letak tampak rapi & tertib.", "col": "#059669", "bg": "#ECFDF5", "x": 4.1},
        {"letter": "P", "nama": "PROXIMITY\n(Kedekatan)", "desc": "Dekatkan elemen yang saling\nberhubungan dan beri ruang\nkosong untuk elemen berbeda.", "col": "#7C3AED", "bg": "#F5F3FF", "x": 5.95},
    ]

    for c in cards:
        card = patches.FancyBboxPatch((c["x"], 0.4), 1.65, 3.2, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=c["bg"], edgecolor=c["col"], linewidth=2)
        ax.add_patch(card)
        circle = patches.Circle((c["x"]+0.825, 2.95), 0.35, facecolor=c["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(c["x"]+0.825, 2.95, c["letter"], ha='center', va='center', fontsize=16, fontweight='bold', color='#FFFFFF')
        ax.text(c["x"]+0.825, 2.2, c["nama"], ha='center', va='center', fontsize=8, fontweight='bold', color=c["col"], multialignment='center')
        ax.text(c["x"]+0.825, 1.1, c["desc"], ha='center', va='center', fontsize=7.2, color='#334155', multialignment='center')

    save_fig(fig, "bab2_prinsip_desain_crap.png")

# -------------------------------------------------------------
# 7. BAB 2: STRUKTUR 3 BABAK PRESENTASI
# -------------------------------------------------------------
def make_bab2_storyline():
    fig, ax = plt.subplots(figsize=(8.0, 3.8), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.8); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.2), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 3.42, "STRUKTUR STORYLINE PRESENTASI MEMIKAT (3 BABAK)",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    acts = [
        {"num": "BABAK 1", "title": "MASALAH YANG MENGGUGAH", "desc": "Paparkan data fakta nyata:\n'500 kg sampah plastik menumpuk\ndi sekolah setiap bulan!'\nBangkitkan empati audiens.", "col": "#EF4444", "bg": "#FEF2F2", "x": 0.4},
        {"num": "BABAK 2", "title": "SOLUSI BERBASIS DATA", "desc": "Tunjukkan solusi inovatif:\nGrafik perbandingan volume sampah\nsebelum vs sesudah program pilah\nbank sampah sekolah.", "col": "#0284C7", "bg": "#F0F9FF", "x": 2.95},
        {"num": "BABAK 3", "title": "AJAKAN NYATA (CALL TO ACTION)", "desc": "Berikan langkah konkret:\n'Mulai hari ini, bawa botol minum\nsendiri dan pisahkan sampahmu!'\nAkhiri dengan penuh optimisme.", "col": "#059669", "bg": "#ECFDF5", "x": 5.5},
    ]

    for a in acts:
        card = patches.FancyBboxPatch((a["x"], 0.35), 2.1, 2.6, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=a["bg"], edgecolor=a["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(a["x"]+1.05, 2.65, a["num"], ha='center', va='center', fontsize=9.5, fontweight='bold', color=a["col"])
        ax.text(a["x"]+1.05, 2.25, a["title"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1E293B', multialignment='center')
        ax.text(a["x"]+1.05, 1.15, a["desc"], ha='center', va='center', fontsize=7.2, color='#475569', multialignment='center')

    # Arrows
    ax.annotate('', xy=(2.9, 1.65), xytext=(2.55, 1.65), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))
    ax.annotate('', xy=(5.45, 1.65), xytext=(5.1, 1.65), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))

    save_fig(fig, "bab2_struktur_3_babak_presentasi.png")

# -------------------------------------------------------------
# 8. BAB 2: INFOGRAFIS LISENSI CREATIVE COMMONS SMP
# -------------------------------------------------------------
def make_bab2_cc_smp():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.6), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title_box)
    ax.text(4.0, 3.84, "RAGAM LISENSI KARYA DIGITAL & ATRIBUSI RESMI",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    items = [
        {"code": "CC-BY", "nama": "Atribusi Bebas", "desc": "Boleh disalin, diubah, dan dibagikan asalkan mencantumkan nama pembuat aslinya.", "col": "#059669", "x": 0.4},
        {"code": "CC-BY-SA", "nama": "Berbagi Serupa", "desc": "Karya turunan wajib dibagikan dengan lisensi terbuka yang sama persis.", "col": "#0284C7", "x": 2.25},
        {"code": "CC-BY-NC", "nama": "Non-Komersial", "desc": "Hanya untuk tujuan edukasi & sosial, dilarang diperjualbelikan untuk profit.", "col": "#D97706", "x": 4.1},
        {"code": "CC-BY-ND", "nama": "Tanpa Turunan", "desc": "Boleh disebarkan secara utuh, dilarang mengubah/mengedit karya asli.", "col": "#DC2626", "x": 5.95},
    ]

    for it in items:
        card = patches.FancyBboxPatch((it["x"], 1.1), 1.65, 2.3, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor='#FFFFFF', edgecolor=it["col"], linewidth=2)
        ax.add_patch(card)
        badge = patches.FancyBboxPatch((it["x"]+0.15, 2.75), 1.35, 0.4, boxstyle="round,pad=0.02,rounding_size=0.08",
                                       facecolor=it["col"], edgecolor=it["col"])
        ax.add_patch(badge)
        ax.text(it["x"]+0.825, 2.95, it["code"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(it["x"]+0.825, 2.35, it["nama"], ha='center', va='center', fontsize=8, fontweight='bold', color=it["col"])
        ax.text(it["x"]+0.825, 1.65, it["desc"], ha='center', va='center', fontsize=6.8, color='#334155', multialignment='center')

    # Example of TASL Box
    box_tasl = patches.FancyBboxPatch((0.4, 0.15), 7.2, 0.75, boxstyle="round,pad=0.04,rounding_size=0.08",
                                      facecolor='#F1F5F9', edgecolor='#94A3B8', linewidth=1.5)
    ax.add_patch(box_tasl)
    ax.text(0.6, 0.65, "Formula Penulisan Kredit TASL (Title + Author + Source + License):", fontsize=8, fontweight='bold', color='#0F172A')
    ax.text(0.6, 0.35, "Grafik 'Statistik Timbulan Sampah' oleh KLHK RI (menlhk.go.id), dilisensikan di bawah CC-BY-SA 4.0.", fontsize=7.2, color='#334155', style='italic')

    save_fig(fig, "bab2_infografis_lisensi_cc_smp.png")

# -------------------------------------------------------------
# 9. BAB 3: KOMIK PEMBUKA AI GENERATIF
# -------------------------------------------------------------
def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK INOVATOR REMAJA: JEBAKAN HALUSINASI & DEEPFAKE KECERDASAN ARTIFISIAL",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Jawaban Menakjubkan", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "FAJAR:\n\"Wah! Aku meminta AI merangkum\nsejarah Kerajaan Majapahit,\nkeluarannya panjang dan bahasanya\nsangat meyakinkan dalam 3 detik!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Rian Menemukan Kejanggalan", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "RIAN:\n\"Tunggu dulu, Fajar! Coba baca baris ini:\n'Hayam Wuruk menggunakan telepon seluler\nuntuk memanggil Gajah Mada?!'\nItu fakta palsu yang mustahil!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Ayu Menganalisis", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "AYU:\n\"Itulah fenomena HALUSINASI AI!\nAI tidak memahami makna sejarah,\nmelainkan hanya merangkai kata\nberdasarkan probabilitas statistik!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Kritis & Skeptis", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "TIM INOVATOR:\n\"Jangan telan mentah-mentah!\nVerifikasi fakta lewat sumber resmi,\nwaspadai rekayasa video Deepfake,\ndan jadilah pengguna AI yang kritis!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        tag = patches.FancyBboxPatch((p["x"]+0.1, p["y"]+1.55), 1.6, 0.28, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=p["col"], edgecolor=p["col"])
        ax.add_patch(tag)
        ax.text(p["x"]+0.9, p["y"]+1.69, p["num"] + ": " + p["title"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"]+1.9, p["y"]+0.75, p["dialog"], ha='center', va='center',
                fontsize=8.5, color='#1E293B', multialignment='center')

    save_fig(fig, "bab3_komik_pembuka_smp7.png")

# -------------------------------------------------------------
# 10. BAB 3: ARSITEKTUR CARA KERJA LLM
# -------------------------------------------------------------
def make_bab3_llm():
    fig, ax = plt.subplots(figsize=(8.0, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.0); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.4), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(title_box)
    ax.text(4.0, 3.62, "DI BALIK DAPUR MODEL BAHASA BESAR (LLM): PENEBAK KATA BERIKUTNYA",
            ha='center', va='center', fontsize=10, fontweight='bold', color='#FFFFFF')

    # Prompt Input Box
    in_box = patches.FancyBboxPatch((0.4, 1.2), 2.2, 1.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                                    facecolor='#E0F2FE', edgecolor='#0284C7', linewidth=2)
    ax.add_patch(in_box)
    ax.text(1.5, 2.65, "Teks Masukan (Input):", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0369A1')
    ax.text(1.5, 1.8, "\"Ibu kota negara\nIndonesia saat ini\nadalah...\"", ha='center', va='center', fontsize=8, color='#1E293B', style='italic')

    # Arrow to Model
    ax.annotate('', xy=(2.95, 2.1), xytext=(2.65, 2.1), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))

    # LLM Core Box
    core_box = patches.FancyBboxPatch((3.0, 0.6), 2.2, 2.4, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor='#F5F3FF', edgecolor='#7C3AED', linewidth=2)
    ax.add_patch(core_box)
    ax.text(4.1, 2.7, "Mesin Probabilitas LLM", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#7C3AED')
    ax.text(4.1, 1.7, "Menghitung Skor Kata:\n• 'Jakarta': 78%\n• 'Nusantara': 18%\n• 'Bandung': 3%\n• 'Bulan': 1%",
            ha='center', va='center', fontsize=7.5, color='#334155')

    # Arrow to Output
    ax.annotate('', xy=(5.55, 2.1), xytext=(5.25, 2.1), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))

    # Output Box
    out_box = patches.FancyBboxPatch((5.6, 1.2), 2.0, 1.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                                     facecolor='#ECFDF5', edgecolor='#059669', linewidth=2)
    ax.add_patch(out_box)
    ax.text(6.6, 2.65, "Kata Terpilih (Output):", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#059669')
    ax.text(6.6, 1.8, "\"...Jakarta.\"\n(Dipilih probabilitas\ntertinggi)", ha='center', va='center', fontsize=8, color='#15803D', fontweight='bold')

    # Footnote
    ax.text(4.0, 0.25, "Catatan Kritis: AI tidak memiliki pemahaman kebenaran sejati, ia hanya merangkai kata berdasarkan statistik pola!",
            ha='center', va='center', fontsize=7, color='#64748B', style='italic')

    save_fig(fig, "bab3_arsitektur_llm_probabilistik.png")

# -------------------------------------------------------------
# 11. BAB 3: INFOGRAFIS KETERBATASAN AI
# -------------------------------------------------------------
def make_bab3_keterbatasan():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.6), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#DC2626', edgecolor='#B91C1C')
    ax.add_patch(title_box)
    ax.text(4.0, 3.82, "3 TANTANGAN & KETERBATASAN UTAMA KECERDASAN ARTIFISIAL GENERATIF",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    challenges = [
        {"title": "1. HALUSINASI DATA", "col": "#EF4444", "bg": "#FEF2F2", "x": 0.4,
         "desc": "AI mengarang fakta, tanggal, kutipan tokoh, atau jurnal fiktif dengan gaya bahasa yang sangat percaya diri dan meyakinkan."},
        {"title": "2. BIAS ALGORITMA", "col": "#D97706", "bg": "#FFFBEB", "x": 2.95,
         "desc": "Jika data latih di internet tidak adil, AI akan meniru prasangka manusia (misalnya stereotip gender atau ketimpangan budaya)."},
        {"title": "3. REKAYASA DEEPFAKE", "col": "#7C3AED", "bg": "#F5F3FF", "x": 5.5,
         "desc": "Kloning suara dan peniruan wajah video palsu yang disalahgunakan untuk penipuan finansial dan pencemaran nama baik."},
    ]

    for c in challenges:
        card = patches.FancyBboxPatch((c["x"], 0.4), 2.1, 2.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=c["bg"], edgecolor=c["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(c["x"]+1.05, 2.9, c["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=c["col"])
        ax.text(c["x"]+1.05, 1.5, c["desc"], ha='center', va='center', fontsize=7.5, color='#334155', linespacing=1.6, multialignment='center')

    save_fig(fig, "bab3_infografis_keterbatasan_ai.png")

# -------------------------------------------------------------
# 12. BAB 3: POSTER DETEKSI DEEPFAKE
# -------------------------------------------------------------
def make_bab3_deepfake():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.55), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#1E293B', edgecolor='#0F172A')
    ax.add_patch(title_box)
    ax.text(4.0, 3.79, "PANDUAN DETEKTIF DIGITAL: 4 CIRI REKAYASA VIDEO DEEPFAKE",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#38BDF8')

    clues = [
        {"num": "1", "title": "Gerakan Mata & Kedipan", "desc": "Wajah deepfake sering tidak berkedip wajar atau arah sorot mata tidak fokus.", "col": "#38BDF8", "x": 0.4},
        {"num": "2", "title": "Sinkronisasi Bibir", "desc": "Gerakan bibir terlambat sepersekian detik dibandingkan gelombang suara audio.", "col": "#F59E0B", "x": 2.25},
        {"num": "3", "title": "Tepi Wajah & Tekstur Kulit", "desc": "Terdapat bayangan buram (blur) atau garis aneh di perbatasan dagu dan leher.", "col": "#EC4899", "x": 4.1},
        {"num": "4", "title": "Anomali Jari & Telinga", "desc": "AI sering kesulitan melukis telinga simetris atau jumlah jari tangan yang wajar.", "col": "#10B981", "x": 5.95},
    ]

    for cl in clues:
        card = patches.FancyBboxPatch((cl["x"], 0.4), 1.65, 2.9, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor='#FFFFFF', edgecolor=cl["col"], linewidth=2)
        ax.add_patch(card)
        num_c = patches.Circle((cl["x"]+0.825, 2.8), 0.3, facecolor=cl["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(num_c)
        ax.text(cl["x"]+0.825, 2.8, cl["num"], ha='center', va='center', fontsize=12, fontweight='bold', color='#FFFFFF')
        ax.text(cl["x"]+0.825, 2.15, cl["title"], ha='center', va='center', fontsize=7.8, fontweight='bold', color=cl["col"], multialignment='center')
        ax.text(cl["x"]+0.825, 1.15, cl["desc"], ha='center', va='center', fontsize=7, color='#334155', multialignment='center')

    save_fig(fig, "bab3_poster_deteksi_deepfake.png")

# -------------------------------------------------------------
# 13. BAB 4: KOMIK PEMBUKA SENI INPUT BERMAKNA
# -------------------------------------------------------------
def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK INOVATOR REMAJA: SENI MENYUSUN INPUT BERMAKNA (PROMPTING)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Prompt Asal-Asalan", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "FAJAR:\n\"Aneh sekali! Aku meminta AI:\n'Buatkan ide acara sekolah', dan\njawabannya sangat umum dan membosankan!\nAI katanya pintar, kok begini ya?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Ayu Menganalisis", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "AYU:\n\"Tentu saja, Fajar! Rumusnya adalah:\nGARBAGE IN, GARBAGE OUT!\nKalau input perintahmu asal-asalan,\nmaka output AI juga akan menjadi sampah!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Formula 4 Pilar Rian", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "RIAN:\n\"Gunakan FORMULA PROMPT 4 PILAR:\nRole (Peran Ahli), Task (Tugas Spesifik),\nContext (Latar Belakang SMP), dan\nFormat (Tabel / Butir Solusi)!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Hasil Berkualitas", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "TIM INOVATOR:\n\"Luar biasa! Dalam sekejap AI menyajikan\nrancangan kampanye anti-bullying lengkap\ndengan jadwal, anggaran, dan tema visual!\nManusia adalah pengemudi cerdasnya!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        tag = patches.FancyBboxPatch((p["x"]+0.1, p["y"]+1.55), 1.6, 0.28, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=p["col"], edgecolor=p["col"])
        ax.add_patch(tag)
        ax.text(p["x"]+0.9, p["y"]+1.69, p["num"] + ": " + p["title"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"]+1.9, p["y"]+0.75, p["dialog"], ha='center', va='center',
                fontsize=8.5, color='#1E293B', multialignment='center')

    save_fig(fig, "bab4_komik_pembuka_smp7.png")

# -------------------------------------------------------------
# 14. BAB 4: FORMULA PROMPT 4 PILAR
# -------------------------------------------------------------
def make_bab4_prompt_formula():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 4.04, "FORMULA PROMPT STANDAR 4 PILAR: ROLE + TASK + CONTEXT + FORMAT",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    pillars = [
        {"tag": "1. ROLE (Peran)", "desc": "\"Bertindaklah sebagai\nFasilitator OSIS SMP\nyang berpengalaman...\"", "col": "#0284C7", "bg": "#E0F2FE", "x": 0.4},
        {"tag": "2. TASK (Tugas)", "desc": "\"Rancanglah 3 ide program\nkampanye ramah lingkungan\ndi sekolah kami...\"", "col": "#D97706", "bg": "#FFFBEB", "x": 2.25},
        {"tag": "3. CONTEXT (Konteks)", "desc": "\"Untuk siswa kelas 7 SMP\ndengan anggaran hemat\ndan bahan daur ulang...\"", "col": "#7C3AED", "bg": "#F5F3FF", "x": 4.1},
        {"tag": "4. FORMAT (Penyajian)", "desc": "\"Sajikan dalam bentuk\ntabel 4 kolom: Nama Acara,\nTujuan, Langkah, dan Biaya.\"", "col": "#059669", "bg": "#ECFDF5", "x": 5.95},
    ]

    for p in pillars:
        card = patches.FancyBboxPatch((p["x"], 0.4), 1.65, 3.2, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(p["x"]+0.825, 3.2, p["tag"], ha='center', va='center', fontsize=8, fontweight='bold', color=p["col"])
        ax.text(p["x"]+0.825, 1.8, p["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B', style='italic', multialignment='center')

    save_fig(fig, "bab4_formula_prompt_4_pilar.png")

# -------------------------------------------------------------
# 15. BAB 4: ALUR CAPSTONE MINI PROYEK SMP KELAS 7
# -------------------------------------------------------------
def make_bab4_capstone_smp():
    fig, ax = plt.subplots(figsize=(8.0, 3.8), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.8); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.2), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title_box)
    ax.text(4.0, 3.42, "ALUR CAPSTONE MINI PROYEK KELAS VII: KAMPANYE DIGITAL SEKOLAH",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "title": "RISET IDE AI", "desc": "Brainstorming gagasan\npositif dengan formula\nprompting terstruktur.", "col": "#0284C7", "bg": "#E0F2FE", "x": 0.4},
        {"num": "2", "title": "VERIFIKASI FAKTA", "desc": "Periksa keakuratan data\nhasil AI dengan jurnal &\nsumber resmi pemerintah.", "col": "#DC2626", "bg": "#FEF2F2", "x": 2.25},
        {"num": "3", "title": "DESAIN INFOGRAFIS", "desc": "Menerapkan prinsip CRAP\npada aplikasi cloud design\ndan beri atribusi karya.", "col": "#D97706", "bg": "#FFFBEB", "x": 4.1},
        {"num": "4", "title": "PAMERAN KARYA", "desc": "Mempublikasikan poster di\nmading sekolah & presentasi\ndi depan teman dan guru.", "col": "#059669", "bg": "#ECFDF5", "x": 5.95},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.35), 1.65, 2.6, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=s["bg"], edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        circle = patches.Circle((s["x"]+0.825, 2.55), 0.25, facecolor=s["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(circle)
        ax.text(s["x"]+0.825, 2.55, s["num"], ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')
        ax.text(s["x"]+0.825, 2.05, s["title"], ha='center', va='center', fontsize=7.5, fontweight='bold', color=s["col"])
        ax.text(s["x"]+0.825, 1.0, s["desc"], ha='center', va='center', fontsize=6.8, color='#334155', multialignment='center')

    for ax_x in [2.1, 3.95, 5.8]:
        ax.annotate('', xy=(ax_x+0.1, 1.65), xytext=(ax_x-0.05, 1.65), arrowprops=dict(arrowstyle="->", lw=2, color="#64748B"))

    save_fig(fig, "bab4_alur_capstone_kampanye_smp.png")

# -------------------------------------------------------------
# 16. COVER BUKU SISWA KELAS 7 SMP
# -------------------------------------------------------------
def make_cover_smp7():
    img = Image.new('RGB', (1800, 2700), color='#042F2E') # Dark Teal
    draw = ImageDraw.Draw(img)

    for y in range(800):
        ratio = y / 800
        r = int(4 + (13 - 4) * ratio)
        g = int(47 + (148 - 47) * ratio)
        b = int(46 + (136 - 46) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(800, 1900):
        ratio = (y - 800) / 1100
        r = int(13 + (2 - 13) * ratio)
        g = int(148 + (132 - 148) * ratio)
        b = int(136 + (199 - 136) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(1900, 2700):
        ratio = (y - 1900) / 800
        r = int(2 + (4 - 2) * ratio)
        g = int(132 + (47 - 132) * ratio)
        b = int(199 + (46 - 199) * ratio)
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

    draw.rectangle([100, 90, 820, 160], fill='#0D9488')
    draw.text((130, 102), "BUKU TEKS PELAJARAN SMP/MTs", font=f_badge, fill='#FFFFFF')

    draw.text((100, 260), "KODING DAN", font=f_title, fill='#FFFFFF')
    draw.text((100, 370), "KECERDASAN", font=f_title, fill='#2DD4BF')
    draw.text((100, 480), "ARTIFISIAL", font=f_title, fill='#FACC15')

    # Grade Pill Badge
    draw.rectangle([100, 620, 950, 720], fill='#D97706')
    draw.text((130, 642), "KELAS VII  •  FASE D (SMP/MTs)", font=f_phase, fill='#FFFFFF')

    # Big Rounded Showcase Card
    draw.rounded_rectangle([150, 820, 1650, 1920], radius=40, fill='#042F2E', outline='#2DD4BF', width=8)

    draw.text((220, 900), "KURIKULUM NASIONAL KKA KEMENDIKDASMEN RI", font=f_badge, fill='#FACC15')
    draw.text((220, 980), "Fokus Penguasaan Fondasi SMP (Fase D):", font=f_sub, fill='#FFFFFF')

    features = [
        "v  Berpikir Komputasional & Analisis Data Sosial Masyarakat",
        "v  Diagram Alur Standar ISO & Dekomposisi Fishbone Diagram",
        "v  Desain Komunikasi Digital (Prinsip CRAP & Storyline 3 Babak)",
        "v  Lisensi Terbuka Creative Commons & Format Atribusi TASL",
        "v  Menyelami AI Generatif (LLM, Fenomena Halusinasi & Deepfake)",
        "v  Seni Input Bermakna: Formula Prompting Terstruktur 4 Pilar"
    ]

    curr_y = 1080
    for feat in features:
        draw.text((220, curr_y), feat, font=f_phase, fill='#E2E8F0')
        curr_y += 120

    # Author Box
    draw.rounded_rectangle([100, 2020, 1700, 2300], radius=30, fill='#FFFFFF', outline='#0D9488', width=5)
    draw.text((150, 2060), "Penulis: Gede Erik Aktama, S.Pd., M.Pd.", font=f_auth, fill='#0F172A')
    draw.text((150, 2130), "Fasilitator Nasional Bimbingan Teknis & ToT KKA Kemendikdasmen RI", font=f_role, fill='#0D9488')
    draw.text((150, 2185), "Dosen Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", font=f_role, fill='#475569')

    # Publisher Footer
    draw.text((900, 2390), "PUSAT PERBUKUAN", font=f_pub, fill='#FFFFFF', anchor="mm")
    draw.text((900, 2450), "BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2505), "KEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2560), "TAHUN 2025 / 2026", font=f_subpub, fill='#FACC15', anchor="mm")

    local_cov = os.path.join(local_assets, "cover_buku_siswa_smp7.jpg")
    img.save(local_cov, quality=95)
    tot_cov = os.path.join(tot_assets, "cover_buku_siswa_smp7.jpg")
    try:
        shutil.copy2(local_cov, tot_cov)
    except Exception as e:
        print(f"Warning copying cover: {e}")
    print("Generated cover: cover_buku_siswa_smp7.jpg")

if __name__ == "__main__":
    print("Starting visual assets generation for Grade 7 SMP...")
    make_tokoh_sahabat()
    make_bab1_komik()
    make_bab1_siklus_data()
    make_bab1_flowchart()
    make_bab1_fishbone()
    make_bab2_komik()
    make_bab2_crap()
    make_bab2_storyline()
    make_bab2_cc_smp()
    make_bab3_komik()
    make_bab3_llm()
    make_bab3_keterbatasan()
    make_bab3_deepfake()
    make_bab4_komik()
    make_bab4_prompt_formula()
    make_bab4_capstone_smp()
    make_cover_smp7()
    print("All visual assets for Grade 7 SMP successfully generated!")
