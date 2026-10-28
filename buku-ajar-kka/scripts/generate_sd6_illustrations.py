# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Buku KKA Kelas 6 SD (Fase C)
Resolusi Tinggi 300 DPI, Desain Infografis Edukatif & Komik Ramah Anak,
Harmonis, Penuh Warna, Sesuai Standar Kemendikdasmen & Kurikulum Nasional.
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-6-sd\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 6 SD\assets"

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
# 0. TOKOH SAHABAT BELAJAR KELAS 6
# -------------------------------------------------------------
def make_tokoh_sahabat():
    fig, ax = plt.subplots(figsize=(8.0, 3.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.6); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 2.9), 7.2, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 3.17, "EMPAT SAHABAT BELAJAR KODING & KECERDASAN ARTIFISIAL KELAS VI",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    tokohs = [
        {"nama": "ERIK", "role": "Arsitek Logika", "ciri": "Berambut ikal pendek, ceria, gemar logika percabangan", "color": "#0284C7", "bg": "#E0F2FE", "x": 0.4},
        {"nama": "SITI", "role": "Kreator Media", "ciri": "Berkerudung hijau, teliti, mahir merancang cerita digital", "color": "#059669", "bg": "#ECFDF5", "x": 2.25},
        {"nama": "MADE", "role": "Inovator Gerak", "ciri": "Berudeng khas Bali, lincah, pembuat rute dan animasi", "color": "#D97706", "bg": "#FFFBEB", "x": 4.1},
        {"nama": "ROBOT KIBO", "role": "Asisten AI Cerdas", "ciri": "Robot sahabat biru-oranye, pemandu sensor & kode", "color": "#7C3AED", "bg": "#F5F3FF", "x": 5.95},
    ]

    for t in tokohs:
        card = patches.FancyBboxPatch((t["x"], 0.25), 1.65, 2.5, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=t["bg"], edgecolor=t["color"], linewidth=2)
        ax.add_patch(card)

        # Avatar circle
        circle = patches.Circle((t["x"] + 0.825, 2.05), 0.5, facecolor=t["color"], edgecolor='#FFFFFF', linewidth=2)
        ax.add_patch(circle)
        ax.text(t["x"] + 0.825, 2.05, t["nama"][0], ha='center', va='center', fontsize=16, fontweight='bold', color='#FFFFFF')

        # Nama & Role
        ax.text(t["x"] + 0.825, 1.35, t["nama"], ha='center', va='center', fontsize=10, fontweight='bold', color=t["color"])
        ax.text(t["x"] + 0.825, 1.1, t["role"], ha='center', va='center', fontsize=8, fontweight='bold', color='#334155')

        # Deskripsi
        ax.text(t["x"] + 0.825, 0.65, t["ciri"], ha='center', va='center', fontsize=7.2, color='#475569', wrap=True,
                multialignment='center')

    save_fig(fig, "gambar_tokoh_sahabat_sd6.png")

# -------------------------------------------------------------
# 1. BAB 1: KOMIK PEMBUKA
# -------------------------------------------------------------
def make_bab1_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: TANTANGAN MEMBUAT GAME KUIS CERDAS CERMAT",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Ide Seru Istirahat", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "ERIK & MADE:\n\"Siti, lihat kuis buatan kita!\nSetiap tombol ditekan,\nskornya tidak mau nambah!\nBagaimana cara komputer tahu\njawabannya benar atau salah?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Siti Menganalisis", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "SITI:\n\"Betul, Erik! Komputer kita\nmasih bingung karena belum ada\naturan percabangan!\nKalau benar, harus apa?\nKalau salah, bunyinya bagaimana?\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Kibo Datang Membantu", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Bip-bip!\nGunakan Mantra Sakti:\nJIKA... MAKA... (If-Then-Else)!\nKomputer butuh logika keputusan\nuntuk memilih dua jalan!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Variabel & Perulangan", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "KIBO & TIM:\n\"Lalu siapkan 'Toples Variabel'\nuntuk menyimpan Skor Nilai,\ndan blok 'Repeat' agar kuis\nbisa berulang sampai 5 soal!\nGame kita siap dimainkan!\"", "x": 4.4, "y": 0.35},
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

    save_fig(fig, "bab1_komik_pembuka_sd6.png")

# -------------------------------------------------------------
# 2. BAB 1: FLOWCHART PERCABANGAN
# -------------------------------------------------------------
def make_bab1_flowchart():
    fig, ax = plt.subplots(figsize=(8.0, 4.5), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.5); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.85), 7.2, 0.5, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 4.1, "DIAGRAM ALUR LOGIKA PERCABANGAN (IF - THEN - ELSE)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    # Start Box
    start_box = patches.FancyBboxPatch((3.0, 3.1), 2.0, 0.45, boxstyle="round,pad=0.05,rounding_size=0.2",
                                       facecolor='#10B981', edgecolor='#059669', linewidth=1.5)
    ax.add_patch(start_box)
    ax.text(4.0, 3.32, "Mulai: Ajukan Soal Kuis", ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF')

    # Arrow Down
    ax.annotate('', xy=(4.0, 2.5), xytext=(4.0, 3.1),
                arrowprops=dict(arrowstyle="->", lw=2, color="#475569"))

    # Decision Diamond
    diamond = patches.Polygon([[4.0, 2.5], [5.6, 1.9], [4.0, 1.3], [2.4, 1.9]],
                              closed=True, facecolor='#FEF08A', edgecolor='#CA8A04', linewidth=2)
    ax.add_patch(diamond)
    ax.text(4.0, 1.9, "Apakah Jawaban\nBenar?", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#854D0E')

    # Branch YA (Kanan)
    ax.annotate('', xy=(6.8, 1.9), xytext=(5.6, 1.9),
                arrowprops=dict(arrowstyle="->", lw=2, color="#059669"))
    ax.text(6.1, 2.05, "YA (Benar)", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#059669')

    box_ya = patches.FancyBboxPatch((6.0, 0.8), 1.7, 0.75, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=1.5)
    ax.add_patch(box_ya)
    ax.text(6.85, 1.17, "Katakan 'Hore, Benar!'\nSkor = Skor + 10", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#15803D')

    # Branch TIDAK (Kiri)
    ax.annotate('', xy=(1.2, 1.9), xytext=(2.4, 1.9),
                arrowprops=dict(arrowstyle="->", lw=2, color="#DC2626"))
    ax.text(1.9, 2.05, "TIDAK (Salah)", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#DC2626')

    box_tidak = patches.FancyBboxPatch((0.3, 0.8), 1.7, 0.75, boxstyle="round,pad=0.04,rounding_size=0.08",
                                       facecolor='#FEE2E2', edgecolor='#DC2626', linewidth=1.5)
    ax.add_patch(box_tidak)
    ax.text(1.15, 1.17, "Katakan 'Coba Lagi!'\nNyawa = Nyawa - 1", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#B91C1C')

    # Rejoin at End
    ax.annotate('', xy=(4.0, 0.3), xytext=(6.85, 0.8),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#475569", connectionstyle="arc3,rad=-0.2"))
    ax.annotate('', xy=(4.0, 0.3), xytext=(1.15, 0.8),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#475569", connectionstyle="arc3,rad=0.2"))

    end_box = patches.FancyBboxPatch((3.0, 0.05), 2.0, 0.4, boxstyle="round,pad=0.05,rounding_size=0.2",
                                     facecolor='#64748B', edgecolor='#475569', linewidth=1.5)
    ax.add_patch(end_box)
    ax.text(4.0, 0.25, "Lanjut ke Soal Berikutnya", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab1_flowchart_percabangan.png")

# -------------------------------------------------------------
# 3. BAB 1: ANALOGI VARIABEL (TOPLES KUE AJAIB)
# -------------------------------------------------------------
def make_bab1_variabel():
    fig, ax = plt.subplots(figsize=(8.0, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.0); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.4), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(title_box)
    ax.text(4.0, 3.62, "KONSEP VARIABEL: KOTAK AJAIB PENYIMPAN NILAI DALAM GAME",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    jars = [
        {"label": "Variabel 'Skor'", "val": "100", "desc": "Mencatat perolehan poin.\nBisa bertambah (+10)\nsaat menjawab benar.", "col": "#0284C7", "bg": "#E0F2FE", "x": 0.5},
        {"label": "Variabel 'Nyawa'", "val": "3", "desc": "Mencatat kesempatan main.\nBerkurang (-1)\nsaat salah menjawab.", "col": "#EF4444", "bg": "#FEE2E2", "x": 3.0},
        {"label": "Variabel 'Waktu'", "val": "30 dtk", "desc": "Mencatat hitungan mundur.\nGame berakhir jika\nwaktu mencapai 0.", "col": "#10B981", "bg": "#D1FAE5", "x": 5.5},
    ]

    for j in jars:
        # Jar body
        jar = patches.FancyBboxPatch((j["x"], 0.4), 2.0, 2.7, boxstyle="round,pad=0.08,rounding_size=0.15",
                                     facecolor=j["bg"], edgecolor=j["col"], linewidth=2.5)
        ax.add_patch(jar)

        # Jar lid
        lid = patches.FancyBboxPatch((j["x"]+0.3, 2.95), 1.4, 0.25, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=j["col"], edgecolor=j["col"])
        ax.add_patch(lid)

        # Label tag
        ax.text(j["x"]+1.0, 2.65, j["label"], ha='center', va='center', fontsize=9.5, fontweight='bold', color=j["col"])

        # Display Value Inside
        val_box = patches.FancyBboxPatch((j["x"]+0.4, 1.7), 1.2, 0.65, boxstyle="round,pad=0.03,rounding_size=0.08",
                                         facecolor='#FFFFFF', edgecolor=j["col"], linewidth=1.5)
        ax.add_patch(val_box)
        ax.text(j["x"]+1.0, 2.02, j["val"], ha='center', va='center', fontsize=16, fontweight='bold', color=j["col"])

        # Explanation
        ax.text(j["x"]+1.0, 1.0, j["desc"], ha='center', va='center', fontsize=7.5, color='#334155', multialignment='center')

    save_fig(fig, "bab1_analogi_variabel.png")

# -------------------------------------------------------------
# 4. BAB 1: KARTU BLOK KODING SCRATCH
# -------------------------------------------------------------
def make_bab1_scratch():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.65), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#F59E0B', edgecolor='#D97706')
    ax.add_patch(title_box)
    ax.text(4.0, 3.87, "KARTU MANTRA BLOK SCRATCH: PERCABANGAN, PERULANGAN & VARIABEL",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    blocks = [
        {"title": "Blok Percabangan", "code": "if <jawaban = 'Monas'> then\n  change [Skor v] by (10)\n  start sound [Cheer v]\nelse\n  change [Nyawa v] by (-1)\n  start sound [Oops v]\nend", "color": "#EAB308", "bg": "#FEFCE8", "x": 0.4},
        {"title": "Blok Perulangan", "code": "repeat (5)\n  ask [Pertanyaan?] and wait\n  check_jawaban\n  wait (1) seconds\nend\n\nforever\n  next costume\n  wait (0.2) secs\nend", "color": "#F97316", "bg": "#FFF7ED", "x": 4.1},
    ]

    for b in blocks:
        card = patches.FancyBboxPatch((b["x"], 0.3), 3.5, 3.1, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=b["bg"], edgecolor=b["color"], linewidth=2)
        ax.add_patch(card)
        ax.text(b["x"]+1.75, 3.1, b["title"], ha='center', va='center', fontsize=10, fontweight='bold', color=b["color"])

        # Code display box
        code_bg = patches.FancyBboxPatch((b["x"]+0.15, 0.5), 3.2, 2.3, boxstyle="round,pad=0.04,rounding_size=0.08",
                                         facecolor='#1E293B', edgecolor='#0F172A')
        ax.add_patch(code_bg)
        ax.text(b["x"]+0.3, 1.65, b["code"], ha='left', va='center', fontsize=8, family='monospace', color='#38BDF8')

    save_fig(fig, "bab1_kartu_blok_scratch.png")

# -------------------------------------------------------------
# 5. BAB 2: KOMIK PEMBUKA KONTEN DIGITAL
# -------------------------------------------------------------
def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#059669', edgecolor='#047857')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: PROYEK DONGENG DIGITAL & HAK CIPTA KARYA",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Merekam Cerita", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "SITI & MADE:\n\"Erik, ayo rekam suaramu!\nKamu jadi Si Kancil cerdik,\ndan aku jadi Buaya!\nKita gabungkan dengan ilustrasi\nhutan Nusantara di laptop!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Asal Mengunduh", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "ERIK:\n\"Biar cepat, aku ambil saja\ngambar harimau keren dari Google!\nLangsung kupasang di cerita kita,\ntak perlu izin siapa-siapa!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Peringatan Hak Cipta", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Bahaya, Erik!\nGambar di internet itu punya\npenciptanya! Kita tidak boleh\nmengambil karya orang tanpa izin!\nItu melanggar HAK CIPTA!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Creative Commons", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "KIBO & SITI:\n\"Gunakan gambar berlisensi\nCREATIVE COMMONS (CC)!\nBoleh digunakan bebas asal kita\nmenuliskan nama pembuatnya\n(Atribusi)! Itu baru jujur & keren!\"", "x": 4.4, "y": 0.35},
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

    save_fig(fig, "bab2_komik_pembuka_sd6.png")

# -------------------------------------------------------------
# 6. BAB 2: INFOGRAFIS CREATIVE COMMONS & ATRIBUSI
# -------------------------------------------------------------
def make_bab2_cc():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title_box)
    ax.text(4.0, 4.04, "PANDUAN LISENSI HAK CIPTA & CREATIVE COMMONS (CC)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    cards = [
        {"simbol": "(C)", "nama": "Hak Cipta Penuh\n(All Rights Reserved)", "arti": "Dilarang menyalin/memakai\ntanpa izin tertulis dari\npemilik karya.", "col": "#DC2626", "bg": "#FEF2F2", "x": 0.4},
        {"simbol": "CC-BY", "nama": "Atribusi Bebas\n(Creative Commons)", "arti": "Boleh dipakai dan dibagikan,\nASAL mencantumkan nama\npembuat aslinya.", "col": "#059669", "bg": "#ECFDF5", "x": 2.25},
        {"simbol": "CC-BY-SA", "nama": "Berbagi Serupa\n(ShareAlike)", "arti": "Boleh dimodifikasi,\ntetapi karya barumu harus\nberlisensi sama.", "col": "#0284C7", "bg": "#F0F9FF", "x": 4.1},
        {"simbol": "CC-NC", "nama": "Non-Komersial\n(Non-Commercial)", "arti": "Boleh dipakai untuk belajar,\ntetapi TIDAK boleh\ndijual untuk uang.", "col": "#D97706", "bg": "#FFFBEB", "x": 5.95},
    ]

    for c in cards:
        card = patches.FancyBboxPatch((c["x"], 1.1), 1.65, 2.5, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=c["bg"], edgecolor=c["col"], linewidth=2)
        ax.add_patch(card)
        badge = patches.Circle((c["x"]+0.825, 3.0), 0.38, facecolor=c["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(badge)
        ax.text(c["x"]+0.825, 3.0, c["simbol"], ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(c["x"]+0.825, 2.35, c["nama"], ha='center', va='center', fontsize=8, fontweight='bold', color=c["col"], multialignment='center')
        ax.text(c["x"]+0.825, 1.6, c["arti"], ha='center', va='center', fontsize=7, color='#334155', multialignment='center')

    # Example of Proper Attribution Box
    ex_box = patches.FancyBboxPatch((0.4, 0.15), 7.2, 0.75, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor='#F1F5F9', edgecolor='#94A3B8', linewidth=1.5)
    ax.add_patch(ex_box)
    ax.text(0.6, 0.65, "Contoh Cara Menuliskan Atribusi yang Benar:", fontsize=8, fontweight='bold', color='#0F172A')
    ax.text(0.6, 0.35, "Foto Candi Borobudur oleh Siti Nurhaliza (Wikimedia Commons), dilisensikan di bawah CC-BY 4.0.", fontsize=7.5, color='#334155', style='italic')

    save_fig(fig, "bab2_infografis_creative_commons.png")

# -------------------------------------------------------------
# 7. BAB 2: POSTER SARING HOAKS
# -------------------------------------------------------------
def make_bab2_hoaks():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.75), 7.2, 0.5, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#DC2626', edgecolor='#B91C1C')
    ax.add_patch(title_box)
    ax.text(4.0, 4.0, "SARING SEBELUM SEBAR: 4 LANGKAH DETEKTIF SIBER ATASI HOAKS",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "title": "Waspada Judul Heboh", "desc": "Judul bombastis, HURUF BESAR SEMUA, atau memicu ketakutan biasanya tanda berita palsu.", "col": "#EF4444", "x": 0.4},
        {"num": "2", "title": "Periksa Sumbernya", "desc": "Apakah ada nama penulis jelas dan diterbitkan oleh situs resmi (seperti .kemdikbud.go.id)?", "col": "#F59E0B", "x": 2.25},
        {"num": "3", "title": "Cek Keaslian Foto", "desc": "Apakah foto tampak editan kasar atau peristiwa lama yang didaur ulang?", "col": "#3B82F6", "x": 4.1},
        {"num": "4", "title": "Tanyakan Orang Dewasa", "desc": "Jika ragu, tanyakan pada Guru atau Orang Tua sebelum membagikannya ke grup teman!", "col": "#10B981", "x": 5.95},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.4), 1.65, 3.1, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor='#FFFFFF', edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        num_circle = patches.Circle((s["x"]+0.825, 2.95), 0.35, facecolor=s["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(num_circle)
        ax.text(s["x"]+0.825, 2.95, s["num"], ha='center', va='center', fontsize=14, fontweight='bold', color='#FFFFFF')
        ax.text(s["x"]+0.825, 2.2, s["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=s["col"], multialignment='center')
        ax.text(s["x"]+0.825, 1.2, s["desc"], ha='center', va='center', fontsize=7.2, color='#334155', multialignment='center')

    save_fig(fig, "bab2_poster_saring_hoaks.png")

# -------------------------------------------------------------
# 8. BAB 2: POSTER STOP CYBERBULLYING
# -------------------------------------------------------------
def make_bab2_cyberbullying():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.55), 7.2, 0.5, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(title_box)
    ax.text(4.0, 3.8, "KEADABAN DIGITAL: JEJAK DIGITALMU ADALAH CERMIN DIRIMU!",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"title": "BERPIKIR SEBELUM MENULIS (T.H.I.N.K)", "bg": "#F5F3FF", "col": "#7C3AED", "x": 0.4,
         "items": "T - True? (Apakah itu benar?)\nH - Helpful? (Apakah itu menolong?)\nI - Inspiring? (Apakah memberi inspirasi?)\nN - Necessary? (Apakah penting dibagikan?)\nK - Kind? (Apakah kalimatnya santun & ramah?)"},
        {"title": "HENTIKAN CYBERBULLYING", "bg": "#FEF2F2", "col": "#DC2626", "x": 4.1,
         "items": "1. Jangan mengejek foto atau karya teman di komentar.\n2. Jangan menyebarkan rahasia atau aib orang lain.\n3. Laporkan dan blokir akun yang menyakiti teman.\n4. Berikan komentar pujian yang membesarkan hati!"},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], 0.3), 3.5, 3.0, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(p["x"]+1.75, 2.95, p["title"], ha='center', va='center', fontsize=9, fontweight='bold', color=p["col"])
        ax.text(p["x"]+0.3, 1.45, p["items"], ha='left', va='center', fontsize=7.8, color='#1E293B', linespacing=1.6)

    save_fig(fig, "bab2_kampanye_stop_cyberbullying.png")

# -------------------------------------------------------------
# 9. BAB 3: KOMIK PEMBUKA SENSOR
# -------------------------------------------------------------
def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: MISTERI PINTU & KERAN AJAIB YANG MENYALA SENDIRI",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Keran Mengalir Sendiri", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "ERIK:\n\"Wah! Keran tempat wudhu sekolah\nmengalirkan air begitu tanganku\nmendekat, tanpa kusentuh sama sekali!\nApakah ini sulap atau sihir?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Pintu Minimarket Terbuka", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "MADE:\n\"Di minimarket juga begitu!\nPintu kaca otomatis bergeser\nsaat Made melangkah di depannya!\nSiapa yang membukakannya ya?\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Kibo Menjelaskan", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Bukan sihir, teman-teman!\nItu adalah kehebatan SENSOR!\nSensor adalah 'indera buatan'\nyang dipasang pada komputer\nuntuk merasakan dunia nyata!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Sensor Cerdas AI", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "KIBO & SITI:\n\"Ada sensor inframerah pendeteksi jarak,\nsensor cahaya saat malam tiba,\ndan kamera AI pembaca pelat mobil!\nTeknologi membantu kita hidup hemat!\"", "x": 4.4, "y": 0.35},
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

    save_fig(fig, "bab3_komik_pembuka_sd6.png")

# -------------------------------------------------------------
# 10. BAB 3: INFOGRAFIS 4 SENSOR PINTAR VS PANCAINDRA
# -------------------------------------------------------------
def make_bab3_sensor():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(title_box)
    ax.text(4.0, 4.04, "4 SENSOR CERDAS DI SEKITAR KITA VS PANCAINDRA MANUSIA",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    sensors = [
        {"nama": "Sensor Cahaya (LDR)", "indera": "Meniru Mata", "contoh": "Menyalakan lampu jalanan\notomatis saat sore hari\nmulai gelap (magrib).", "col": "#EAB308", "bg": "#FEFCE8", "x": 0.4},
        {"nama": "Sensor Jarak (Ultrasonik)", "indera": "Meniru Telinga Kelelawar", "contoh": "Memancarkan gelombang suara\nagar mobil tidak menabrak\ntembok saat mundur.", "col": "#0284C7", "bg": "#F0F9FF", "x": 2.25},
        {"nama": "Sensor Gerak (PIR)", "indera": "Meniru Kulit Perasa Panas", "contoh": "Mendeteksi hawa panas tubuh\nuntuk menyalakan pendingin\natau lampu toilet otomatis.", "col": "#EF4444", "bg": "#FEF2F2", "x": 4.1},
        {"nama": "Kamera Cerdas (AI Vision)", "indera": "Mata + Otak Pengenal", "contoh": "Membaca pelat nomor kendaraan\ndi gerbang tol atau mengenali\nwajah murid untuk presensi.", "col": "#10B981", "bg": "#ECFDF5", "x": 5.95},
    ]

    for s in sensors:
        card = patches.FancyBboxPatch((s["x"], 0.3), 1.65, 3.3, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=s["bg"], edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(s["x"]+0.825, 3.25, s["nama"], ha='center', va='center', fontsize=8, fontweight='bold', color=s["col"], multialignment='center')

        # Indera tag
        tag = patches.FancyBboxPatch((s["x"]+0.1, 2.65), 1.45, 0.3, boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor=s["col"], edgecolor=s["col"])
        ax.add_patch(tag)
        ax.text(s["x"]+0.825, 2.8, s["indera"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')

        # Contoh
        ax.text(s["x"]+0.825, 1.4, s["contoh"], ha='center', va='center', fontsize=7.2, color='#334155', multialignment='center')

    save_fig(fig, "bab3_infografis_4_sensor.png")

# -------------------------------------------------------------
# 11. BAB 3: DIAGRAM SISTEM OTOMATIS
# -------------------------------------------------------------
def make_bab3_diagram():
    fig, ax = plt.subplots(figsize=(8.0, 3.8), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.8); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.2), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#10B981', edgecolor='#059669')
    ax.add_patch(title_box)
    ax.text(4.0, 3.42, "SIKLUS KERJA SISTEM OTOMATIS CERDAS: INPUT -> PROSES -> OUTPUT",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    steps = [
        {"title": "1. MASUKAN (INPUT)", "sub": "Sensor Mendeteksi Fisik", "desc": "Sensor ultrasonik mendeteksi\nmobil mendekat pada jarak 1 meter.", "col": "#0284C7", "bg": "#E0F2FE", "x": 0.4},
        {"title": "2. PROSES (PROCESS)", "sub": "Otak AI Mengambil Keputusan", "desc": "Koding logika membaca data:\nJika jarak <= 1m -> Buka Palang!", "col": "#7C3AED", "bg": "#F5F3FF", "x": 2.95},
        {"title": "3. KELUARAN (OUTPUT)", "sub": "Aktuator Beraksi Nyata", "desc": "Motor listrik berputar mengangkat\npalang pintu dan lampu hijau menyala.", "col": "#059669", "bg": "#ECFDF5", "x": 5.5},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.4), 2.1, 2.5, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=s["bg"], edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(s["x"]+1.05, 2.55, s["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=s["col"])
        ax.text(s["x"]+1.05, 2.15, s["sub"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155', multialignment='center')
        ax.text(s["x"]+1.05, 1.1, s["desc"], ha='center', va='center', fontsize=7.2, color='#475569', multialignment='center')

    # Arrows connecting cards
    ax.annotate('', xy=(2.9, 1.65), xytext=(2.55, 1.65), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))
    ax.annotate('', xy=(5.45, 1.65), xytext=(5.1, 1.65), arrowprops=dict(arrowstyle="->", lw=3, color="#64748B"))

    save_fig(fig, "bab3_diagram_sistem_otomatis.png")

# -------------------------------------------------------------
# 12. BAB 3: AI INKLUSI DISABILITAS
# -------------------------------------------------------------
def make_bab3_inklusi():
    fig, ax = plt.subplots(figsize=(8.0, 4.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.0); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.4), 7.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(title_box)
    ax.text(4.0, 3.62, "KECERDASAN ARTIFISIAL UNTUK INKLUSIVITAS (AI FOR GOOD)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    boxes = [
        {"title": "Kacamata Cerdas Tunanetra", "col": "#0284C7", "bg": "#F0F9FF", "x": 0.4,
         "desc": "Dilengkapi kamera AI mini dan earphone.\nAI membaca rambu lalu lintas, uang kertas,\ndan mendeteksi rintangan di depan jalan,\nlalu membisikkan instruksi suara kepada pengguna."},
        {"title": "Penerjemah Suara-ke-Teks (Live Transcribe)", "col": "#059669", "bg": "#ECFDF5", "x": 4.1,
         "desc": "Membantu sahabat tunarungu di kelas inklusi.\nSuara penjelasan guru secara instan diubah\nmenjadi teks huruf berjalan di layar tablet,\nsehingga teman tunarungu dapat membaca pelajaran."},
    ]

    for b in boxes:
        card = patches.FancyBboxPatch((b["x"], 0.4), 3.5, 2.7, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=b["bg"], edgecolor=b["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(b["x"]+1.75, 2.75, b["title"], ha='center', va='center', fontsize=9.5, fontweight='bold', color=b["col"])
        ax.text(b["x"]+0.3, 1.4, b["desc"], ha='left', va='center', fontsize=8, color='#334155', linespacing=1.6)

    save_fig(fig, "bab3_ai_inklusi_disabilitas.png")

# -------------------------------------------------------------
# 13. BAB 4: KOMIK PEMBUKA CAPSTONE PROJECT
# -------------------------------------------------------------
def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: GELAR KARYA INOVASI DIGITAL KELULUSAN FASE C",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Mencari Masalah Nyata", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "SITI & ERIK:\n\"Lihat teman-teman, banyak sampah\nplastik tercampur dengan daun\ndi halaman belakang sekolah!\nBagaimana kalau kita buat proyek\nTempat Sampah Cerdas AI?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Bagi Tugas Tim", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "MADE:\n\"Setuju! Aku yang merancang\ndesain kardus dan mekanik tutupnya!\nSiti membuat poster dan naskah,\nErik memprogram Scratch dan AI-nya!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Proses Uji & Debugging", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Jangan lupa uji coba!\nSaat diuji, tutup tempat sampah\nterlambat membuka 2 detik.\nErik mempercepat kode Scratch-nya!\nBug berhasil diperbaiki!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Hari Gelar Karya", "col": "#059669", "bg": "#ECFDF5",
         "dialog": "SEMUA TOKOH:\n\"HORE! Bapak Kepala Sekolah dan\nadik kelas kagum melihat karya kita!\nKita resmi lulus Fase C sebagai\nSang Pencipta Teknologi Nusantara!\"", "x": 4.4, "y": 0.35},
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

    save_fig(fig, "bab4_komik_pembuka_sd6.png")

# -------------------------------------------------------------
# 14. BAB 4: TAHAPAN CAPSTONE PROJECT
# -------------------------------------------------------------
def make_bab4_tahapan():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.4); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.8), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#7C3AED', edgecolor='#6D28D9')
    ax.add_patch(title_box)
    ax.text(4.0, 4.04, "5 TAHAP EMAS CAPSTONE PROJECT KODING & KA (FASE C)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    steps = [
        {"num": "1", "nama": "EMPATI & IDE", "desc": "Observasi masalah nyata\ndi sekitar sekolah kita.", "col": "#EF4444", "x": 0.3},
        {"num": "2", "nama": "PERANCANGAN", "desc": "Membuat sketsa prototipe,\nalur flowchart & bagi tugas.", "col": "#F59E0B", "x": 1.8},
        {"num": "3", "nama": "KODING & RAKIT", "desc": "Menyusun blok kode Scratch\ndan melatih model cerdas.", "col": "#0284C7", "x": 3.3},
        {"num": "4", "nama": "UJI & DEBUG", "desc": "Menguji coba bersama calon\npengguna & perbaiki bug.", "col": "#10B981", "x": 4.8},
        {"num": "5", "nama": "GELAR KARYA", "desc": "Presentasi karya di depan\nguru, ortu, & adik kelas.", "col": "#7C3AED", "x": 6.3},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.4), 1.4, 3.1, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor='#FFFFFF', edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        num_circle = patches.Circle((s["x"]+0.7, 2.95), 0.3, facecolor=s["col"], edgecolor='#FFFFFF', linewidth=1.5)
        ax.add_patch(num_circle)
        ax.text(s["x"]+0.7, 2.95, s["num"], ha='center', va='center', fontsize=12, fontweight='bold', color='#FFFFFF')
        ax.text(s["x"]+0.7, 2.25, s["nama"], ha='center', va='center', fontsize=7.5, fontweight='bold', color=s["col"], multialignment='center')
        ax.text(s["x"]+0.7, 1.2, s["desc"], ha='center', va='center', fontsize=6.8, color='#334155', multialignment='center')

    save_fig(fig, "bab4_tahapan_capstone_project.png")

# -------------------------------------------------------------
# 15. BAB 4: PANDUAN STAN PAMERAN GELAR KARYA
# -------------------------------------------------------------
def make_bab4_stan():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 3.55), 7.2, 0.48, boxstyle="round,pad=0.04,rounding_size=0.1",
                                       facecolor='#059669', edgecolor='#047857')
    ax.add_patch(title_box)
    ax.text(4.0, 3.8, "DENAH & PERLENGKAPAN STAN PAMERAN GELAR KARYA DIGITAL",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    items = [
        {"title": "1. Banner Poster Proyek", "col": "#0284C7", "bg": "#F0F9FF", "x": 0.4,
         "desc": "Menjelaskan judul proyek, nama tim,\nlatar belakang masalah, manfaat karya,\ndan diagram alur sistem yang dibuat."},
        {"title": "2. Meja Demo Interaktif", "col": "#D97706", "bg": "#FFFBEB", "x": 4.1,
         "desc": "Laptop dengan game Scratch siap dimainkan\natau prototipe tempat sampah cerdas ber-AI.\nPengunjung boleh mencoba langsung!"},
        {"title": "3. Tim Presenter Sigap", "col": "#7C3AED", "bg": "#F5F3FF", "x": 0.4, "y": 0.3,
         "desc": "Anggota tim bergantian menjelaskan karya\ndengan tutur bahasa sopan dan ramah.\nMenjawab pertanyaan dari pengunjung."},
        {"title": "4. Buku Tamu & Kotak Bintang", "col": "#059669", "bg": "#ECFDF5", "x": 4.1, "y": 0.3,
         "desc": "Pengunjung dapat menuliskan kesan pesan,\nsaran perbaikan, serta menempelkan stiker\nbintang apresiasi atas karya inovatifmu!"},
    ]

    for it in items:
        y_pos = it.get("y", 1.8)
        card = patches.FancyBboxPatch((it["x"], y_pos), 3.5, 1.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=it["bg"], edgecolor=it["col"], linewidth=1.8)
        ax.add_patch(card)
        ax.text(it["x"]+1.75, y_pos+1.18, it["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=it["col"])
        ax.text(it["x"]+0.25, y_pos+0.55, it["desc"], ha='left', va='center', fontsize=7.2, color='#334155', linespacing=1.4)

    save_fig(fig, "bab4_peta_pameran_gelar_karya.png")

# -------------------------------------------------------------
# 16. COVER BUKU SISWA KELAS 6 SD
# -------------------------------------------------------------
def make_cover_sd6():
    img = Image.new('RGB', (1800, 2700), color='#0F172A')
    draw = ImageDraw.Draw(img)

    # Top Gradient Band (Navy to Rich Teal/Cyan)
    for y in range(800):
        r = int(15 + (14 - 15) * (y / 800))
        g = int(23 + (116 - 23) * (y / 800))
        b = int(42 + (144 - 42) * (y / 800))
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    # Middle Band (Vibrant Royal Cyan to Deep Blue)
    for y in range(800, 1900):
        ratio = (y - 800) / 1100
        r = int(14 + (2 - 14) * ratio)
        g = int(116 + (132 - 116) * ratio)
        b = int(144 + (199 - 144) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    # Bottom Band
    for y in range(1900, 2700):
        ratio = (y - 1900) / 800
        r = int(2 + (15 - 2) * ratio)
        g = int(132 + (23 - 132) * ratio)
        b = int(199 + (42 - 199) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    # Header Badges
    draw.rectangle([100, 90, 800, 160], fill='#0284C7')
    # Use default font or truetype
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

    draw.text((130, 102), "BUKU TEKS PELAJARAN SD/MI", font=f_badge, fill='#FFFFFF')

    # Main Titles
    draw.text((100, 260), "KODING DAN", font=f_title, fill='#FFFFFF')
    draw.text((100, 370), "KECERDASAN", font=f_title, fill='#38BDF8')
    draw.text((100, 480), "ARTIFISIAL", font=f_title, fill='#FACC15')

    # Grade Pill Badge
    draw.rectangle([100, 620, 950, 720], fill='#D97706')
    draw.text((130, 642), "KELAS VI  •  FASE C (AKHIR SD)", font=f_phase, fill='#FFFFFF')

    # Center Visual Element: Big Rounded Showcase Card
    draw.rounded_rectangle([150, 820, 1650, 1920], radius=40, fill='#0F172A', outline='#38BDF8', width=8)

    # Decorative Elements inside card
    draw.text((220, 900), "KURIKULUM NASIONAL KKA KEMENDIKDASMEN RI", font=f_badge, fill='#FACC15')
    draw.text((220, 980), "Fokus Capstone Project & Penguasaan Fase C:", font=f_sub, fill='#FFFFFF')

    features = [
        "v  Logika Percabangan Bersarang (If-Then-Else) & Variabel Skor",
        "v  Membuat Game Kuis Interaktif & Animasi Bersuara di Scratch",
        "v  Keadaban Konten Digital, Hak Cipta & Creative Commons",
        "v  Eksplorasi Sensor Otomasi Cerdas & AI Ramah Disabilitas",
        "v  Capstone Project: Karya Nyata Inovasi Lingkungan Sekolah",
        "v  Gelar Karya Teknologi & Kesiapan Melangkah ke Fase D (SMP)"
    ]

    curr_y = 1080
    for feat in features:
        draw.text((220, curr_y), feat, font=f_phase, fill='#E2E8F0')
        curr_y += 120

    # Author Box at Bottom
    draw.rounded_rectangle([100, 2020, 1700, 2300], radius=30, fill='#FFFFFF', outline='#0284C7', width=5)
    draw.text((150, 2060), "Penulis: Gede Erik Aktama, S.Pd., M.Pd.", font=f_auth, fill='#0F172A')
    draw.text((150, 2130), "Fasilitator Nasional Bimbingan Teknis & ToT KKA Kemendikdasmen RI", font=f_role, fill='#0284C7')
    draw.text((150, 2185), "Dosen Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", font=f_role, fill='#475569')

    # Publisher Footer
    draw.text((900, 2390), "PUSAT PERBUKUAN", font=f_pub, fill='#FFFFFF', anchor="mm")
    draw.text((900, 2450), "BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2505), "KEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2560), "TAHUN 2025 / 2026", font=f_subpub, fill='#FACC15', anchor="mm")

    local_cov = os.path.join(local_assets, "cover_buku_siswa_sd6.jpg")
    img.save(local_cov, quality=95)
    tot_cov = os.path.join(tot_assets, "cover_buku_siswa_sd6.jpg")
    try:
        shutil.copy2(local_cov, tot_cov)
    except Exception as e:
        print(f"Warning copying cover: {e}")
    print("Generated cover: cover_buku_siswa_sd6.jpg")

if __name__ == "__main__":
    print("Starting visual assets generation for Grade 6 SD...")
    make_tokoh_sahabat()
    make_bab1_komik()
    make_bab1_flowchart()
    make_bab1_variabel()
    make_bab1_scratch()
    make_bab2_komik()
    make_bab2_cc()
    make_bab2_hoaks()
    make_bab2_cyberbullying()
    make_bab3_komik()
    make_bab3_sensor()
    make_bab3_diagram()
    make_bab3_inklusi()
    make_bab4_komik()
    make_bab4_tahapan()
    make_bab4_stan()
    make_cover_sd6()
    print("All visual assets for Grade 6 SD successfully generated!")
