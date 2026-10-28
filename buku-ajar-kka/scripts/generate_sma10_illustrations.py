# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Buku KKA Kelas X SMA/SMK (Fase E)
Resolusi Tinggi 300 DPI, Desain Infografis Edukatif & Komik Remaja,
Modern, Penuh Warna, Sesuai Standar Kemendikdasmen & Kurikulum Nasional.
"""
import os, sys, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

local_assets = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-10-sma-smk\assets"
tot_assets = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 10 SMA-SMK\assets"

os.makedirs(local_assets, exist_ok=True)
os.makedirs(tot_assets, exist_ok=True)

# Copy foto_penulis.jpg
src_foto = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-7-smp\assets\foto_penulis.jpg"
if os.path.exists(src_foto):
    shutil.copy2(src_foto, os.path.join(local_assets, "foto_penulis.jpg"))
    shutil.copy2(src_foto, os.path.join(tot_assets, "foto_penulis.jpg"))
    print("Copied foto_penulis.jpg to Kelas 10 SMA/SMK assets")

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
# 0. TOKOH PEMBELAJAR KELAS X SMA/SMK (FASE E)
# -------------------------------------------------------------
def make_tokoh_sahabat():
    fig, ax = plt.subplots(figsize=(8.0, 3.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.6); ax.axis('off')

    title_box = patches.FancyBboxPatch((0.4, 2.9), 7.2, 0.55, boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor='#1E3A8A', edgecolor='#172554')
    ax.add_patch(title_box)
    ax.text(4.0, 3.17, "TIGA SAHABAT INOVATOR KODING & KA KELAS X SMA/MA/SMK (FASE E)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    tokohs = [
        {"nama": "ARYA", "role": "Sains Komputasi (SMA)", "ciri": "Siswa analitis, gemar riset efisiensi algoritma Big-O, Python & basis data", "color": "#1E40AF", "bg": "#EFF6FF", "x": 0.5},
        {"nama": "DINDA", "role": "Data & UI/UX (SMA)", "ciri": "Siswi kreatif, perancang multimedia interaktif, etika siber & user experience", "color": "#B45309", "bg": "#FFFBEB", "x": 3.0},
        {"nama": "BAGAS", "role": "Teknik & AI Terapan (SMK)", "ciri": "Siswa vokasi praktis, pengembang Computer Vision, sensorik & sistem terapan", "color": "#047857", "bg": "#ECFDF5", "x": 5.5},
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

    save_fig(fig, "gambar_tokoh_sahabat_sma10.png")

# -------------------------------------------------------------
# 1. BAB 1: KOMIK PEMBUKA EFISIENSI ALGORITMA
# -------------------------------------------------------------
def make_bab1_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#1E3A8A', edgecolor='#172554')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 1: TANTANGAN SISTEM LOGISTIK & PERANG EFISIENSI ALGORITMA",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Jutaan Paket Menumpuk", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Bagas:\n'Lihat gudang kurir ekspedisi ini! Ada 1.000.000 paket! Jika kita mencari paket dengan memeriksa satu per satu secara linear, butuh waktu seminggu penuh!'",
         "status": "Masalah Skala Masif"},
        {"x": 3.0, "title": "Panel 2: Keajaiban Bagi Dua", "bg": "#FFFBEB", "bdr": "#F59E0B",
         "dialog": "Arya:\n'Urutkan dulu nomor resinya! Dengan Binary Search, kita membelah data menjadi dua setiap langkah. Satu juta paket bisa ditemukan hanya dalam 20 langkah pemotongan!'",
         "status": "Binary Search O(log n)"},
        {"x": 5.6, "title": "Panel 3: Notasi Big-O", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Dinda:\n'Luar biasa! Inilah yang membedakan programmer amatir dan insinyur komputasi sejati: kita tidak hanya mencari kode yang jalan, tapi kode yang paling efisien!'",
         "status": "Efisiensi Terbukti"}
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
        ax.text(p["x"]+1.25, 2.95, "ALGO\nEKSPRES", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab1_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 2. BAB 1: LINEAR VS BINARY SEARCH
# -------------------------------------------------------------
def make_bab1_search_comparison():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "PERBANDINGAN PENCARIAN DATA: LINEAR SEARCH O(n) VS BINARY SEARCH O(log n)",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Card 1: Linear Search
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFF1F2', edgecolor='#F43F5E', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.5, "LINEAR SEARCH (SEKUENSIAL)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#BE123C')
    txt_lin = (
        "Cara Kerja:\n"
        "- Memeriksa elemen satu per satu dari awal\n"
        "  sampai elemen target ditemukan.\n"
        "- Tidak memerlukan data terurut.\n\n"
        "Kompleksitas: O(n)\n"
        "* Jika ada 1.000 data -> Maksimal 1.000 langkah\n"
        "* Jika ada 1.000.000 data -> Maksimal 1.000.000 langkah!\n\n"
        "Kelemahan: Sangat lambat untuk data raksasa."
    )
    ax.text(0.6, 1.8, txt_lin, ha='left', va='center', fontsize=7.5, color='#4C0519', linespacing=1.2)

    # Card 2: Binary Search
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.5, "BINARY SEARCH (BAGI-DUA)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#1D4ED8')
    txt_bin = (
        "Cara Kerja:\n"
        "- Data WAJIB sudah diurutkan terlebih dahulu.\n"
        "- Bandingkan elemen tengah: jika target lebih\n"
        "  besar, buang separuh kiri; jika kecil, buang kanan.\n\n"
        "Kompleksitas: O(log n)\n"
        "* Jika ada 1.000 data -> Maksimal CUMA 10 langkah!\n"
        "* Jika ada 1.000.000 data -> CUMA butuh 20 langkah!\n\n"
        "Keunggulan: Luar biasa cepat & hemat prosesor!"
    )
    ax.text(4.7, 1.8, txt_bin, ha='left', va='center', fontsize=7.5, color='#1E293B', linespacing=1.2)

    save_fig(fig, "bab1_diagram_linear_vs_binary_search.png")

# -------------------------------------------------------------
# 3. BAB 1: VISUALISASI SORTING
# -------------------------------------------------------------
def make_bab1_sorting():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#D97706', edgecolor='#B45309')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "TIGA ALGORITMA PENGURUTAN KLASIK: BUBBLE, SELECTION, DAN INSERTION SORT",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    algos = [
        {"name": "BUBBLE SORT", "mechanism": "Pertukaran Tetangga", "desc": "Membandingkan dua elemen bersebelahan, lalu menukarnya jika urutannya salah. Elemen terbesar menggelembung ke ujung.", "bg": "#EFF6FF", "bdr": "#3B82F6", "x": 0.5},
        {"name": "SELECTION SORT", "mechanism": "Pencarian Nilai Minimum", "desc": "Mencari elemen terkecil di seluruh deret yang belum terurut, lalu menukarnya langsung ke posisi depan yang tepat.", "bg": "#FEF3C7", "bdr": "#D97706", "x": 3.1},
        {"name": "INSERTION SORT", "mechanism": "Penyisipan Seperti Kartu", "desc": "Mengambil satu elemen dan menyisipkannya ke posisi yang tepat di antara elemen-elemen yang sudah terurut di sebelah kiri.", "bg": "#ECFDF5", "bdr": "#10B981", "x": 5.7}
    ]

    for a in algos:
        box = patches.FancyBboxPatch((a["x"], 0.4), 2.3, 3.2, boxstyle="round,pad=0.06,rounding_size=0.1",
                                     facecolor=a["bg"], edgecolor=a["bdr"], lw=2)
        ax.add_patch(box)

        ax.text(a["x"]+1.15, 3.25, a["name"], ha='center', va='center', fontsize=8.8, fontweight='bold', color=a["bdr"])
        ax.text(a["x"]+1.15, 2.95, a["mechanism"], ha='center', va='center', fontsize=7.2, fontweight='bold', color='#334155')

        ax.text(a["x"]+1.15, 1.8, a["desc"], ha='center', va='center', fontsize=7.5, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((a["x"]+0.15, 0.65), 2.0, 0.4, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=a["bdr"], edgecolor=a["bdr"])
        ax.add_patch(pill)
        ax.text(a["x"]+1.15, 0.85, "O(n^2) Rata-rata", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab1_visualisasi_sorting_swapping.png")

# -------------------------------------------------------------
# 4. BAB 1: KURVA KOMPLEKSITAS BIG-O
# -------------------------------------------------------------
def make_bab1_big_o():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#0F172A', edgecolor='#334155')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "GRAFIK PERTUMBUHAN KOMPLEKSITAS KOMPUTASI NOTASI BIG-O",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF')

    # Draw Chart Axes
    ax.plot([1.2, 7.8], [0.8, 0.8], color='#334155', lw=2)  # X axis: Jumlah Data (n)
    ax.plot([1.2, 1.2], [0.8, 3.7], color='#334155', lw=2)  # Y axis: Waktu Operasi (t)
    ax.text(7.8, 0.6, "Ukuran Data (n) ->", ha='right', va='center', fontsize=8, fontweight='bold', color='#334155')
    ax.text(1.0, 3.7, "^ Waktu Operasi", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#334155')

    # O(1) Constant (Green)
    ax.plot([1.2, 7.5], [1.1, 1.1], color='#10B981', lw=2.5)
    ax.text(7.6, 1.1, "O(1) Konstan", fontsize=7.5, fontweight='bold', color='#059669')

    # O(log n) Binary (Blue)
    ax.plot([1.2, 2.5, 4.5, 7.5], [0.8, 1.4, 1.7, 1.9], color='#2563EB', lw=2.5)
    ax.text(7.6, 1.9, "O(log n) Bagi-dua", fontsize=7.5, fontweight='bold', color='#1D4ED8')

    # O(n) Linear (Amber)
    ax.plot([1.2, 7.5], [0.8, 2.6], color='#F59E0B', lw=2.5)
    ax.text(7.6, 2.6, "O(n) Linear", fontsize=7.5, fontweight='bold', color='#D97706')

    # O(n^2) Quadratic (Red)
    ax.plot([1.2, 2.5, 3.8, 5.0], [0.8, 1.3, 2.2, 3.6], color='#EF4444', lw=2.5)
    ax.text(5.1, 3.6, "O(n^2) Kuadratik", fontsize=7.5, fontweight='bold', color='#DC2626')

    save_fig(fig, "bab1_kurva_kompleksitas_big_o.png")

# -------------------------------------------------------------
# 5. BAB 2: KOMIK PEMBUKA DEBUGGING
# -------------------------------------------------------------
def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 2: MISTERI SISTEM KASIR KANTIN & KUTU KODE (BUG)",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Kasir Mendadak Macet", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Dinda:\n'Gawat! Saat pembeli mengetik huruf di kolom jumlah barang, program kasir buatan Arya langsung mogok dan mengeluarkan teks merah mengerikan: ValueError!'",
         "status": "Runtime Crash"},
        {"x": 3.0, "title": "Panel 2: Benteng Try-Except", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Bagas:\n'Tenang! Kita gunakan Exception Handling! Kita pasang blok try-except. Jika pembeli salah ketik, program tidak akan mati, melainkan memberi pesan ramah!'",
         "status": "Penanganan Eksepsi"},
        {"x": 5.6, "title": "Panel 3: Struktur Dictionary Rapi", "bg": "#FFFBEB", "bdr": "#F59E0B",
         "dialog": "Arya:\n'Bagus! Dan seluruh daftar menu kita simpan di Dictionary Python agar pencarian harga instan. Program kasir kita kini tangguh dan siap pakai di sekolah!'",
         "status": "Robust Program Berhasil"}
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
        ax.text(p["x"]+1.25, 2.95, "DEBUG\nMASTER", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab2_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 6. BAB 2: STRUKTUR DATA PYTHON LANJUTAN
# -------------------------------------------------------------
def make_bab2_struktur_data():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#4F46E5', edgecolor='#4338CA')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "EMPAT STRUKTUR DATA UTAMA BAHASA PYTHON: LIST, TUPLE, SET, & DICTIONARY",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    structures = [
        {"name": "1. LIST [ ]", "type": "Berurutan & Dapat Diubah", "desc": "Deretan elemen berindeks angka 0, 1, 2. Bisa ditambah (.append) dan dihapus (.pop).", "code": "buah = ['Apel', 'Jeruk']", "bg": "#EFF6FF", "bdr": "#3B82F6", "x": 0.4},
        {"name": "2. TUPLE ( )", "type": "Berurutan & Konstan (Tetap)", "desc": "Elemen tidak dapat diubah setelah dibuat. Sangat aman untuk koordinat GPS dan konstanta.", "code": "posisi = (-7.25, 110.4)", "bg": "#FEF3C7", "bdr": "#D97706", "x": 2.35},
        {"name": "3. SET { }", "type": "Himpunan Unik Tanpa Urutan", "desc": "Secara otomatis membuang duplikasi data. Sangat cepat untuk operasi irisan & gabungan himpunan.", "code": "id_siswa = {101, 102, 105}", "bg": "#FAF5FF", "bdr": "#8B5CF6", "x": 4.3},
        {"name": "4. DICT {k:v}", "type": "Pasangan Kunci-Nilai", "desc": "Mencari nilai berdasarkan nama kunci string unik. Struktur terpopuler dalam sains data.", "code": "harga = {'Buku': 5000}", "bg": "#ECFDF5", "bdr": "#10B981", "x": 6.25}
    ]

    for s in structures:
        box = patches.FancyBboxPatch((s["x"], 0.6), 1.8, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=s["bg"], edgecolor=s["bdr"], lw=1.8)
        ax.add_patch(box)

        ax.text(s["x"]+0.9, 3.3, s["name"], ha='center', va='center', fontsize=7.8, fontweight='bold', color=s["bdr"])
        ax.text(s["x"]+0.9, 3.05, s["type"], ha='center', va='center', fontsize=6.8, color='#475569')

        ax.text(s["x"]+0.9, 2.05, s["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B', wrap=True,
                multialignment='center')

        # Code pill
        c_pill = patches.FancyBboxPatch((s["x"]+0.08, 0.75), 1.64, 0.5, boxstyle="square,pad=0.02",
                                        facecolor='#0F172A', edgecolor=s["bdr"])
        ax.add_patch(c_pill)
        ax.text(s["x"]+0.9, 1.0, s["code"], ha='center', va='center', fontsize=6.8, color='#38BDF8')

    save_fig(fig, "bab2_arsitektur_struktur_data_python.png")

# -------------------------------------------------------------
# 7. BAB 2: ALUR EXCEPTION HANDLING
# -------------------------------------------------------------
def make_bab2_exception_handling():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#B91C1C', edgecolor='#991B1B')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "BENTENG KODE TANGGUH: BLOK PENANGANAN EKSEPSI TRY - EXCEPT - FINALLY",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    # Left: Code Flow
    ax.text(2.0, 3.6, "Alur Eksekusi Tangguh:", fontsize=8.5, fontweight='bold', color='#1E293B')

    b_try = patches.FancyBboxPatch((0.8, 2.7), 2.4, 0.6, boxstyle="round,pad=0.04,rounding_size=0.08",
                                   facecolor='#EFF6FF', edgecolor='#2563EB', lw=1.5)
    ax.add_patch(b_try)
    ax.text(2.0, 3.0, "try:\n# Jalankan kode berisiko error", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1D4ED8')

    # Arrow Down Error occurs
    ax.annotate("Terjadi Galat!", xy=(2.0, 1.8), xytext=(2.0, 2.7), arrowprops=dict(arrowstyle="->", color='#EF4444', lw=2))

    b_exc = patches.FancyBboxPatch((0.8, 1.2), 2.4, 0.6, boxstyle="round,pad=0.04,rounding_size=0.08",
                                   facecolor='#FEF2F2', edgecolor='#EF4444', lw=1.5)
    ax.add_patch(b_exc)
    ax.text(2.0, 1.5, "except ValueError:\n# Tangani dengan pesan ramah", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#B91C1C')

    # Arrow Down to Finally
    ax.annotate("", xy=(2.0, 0.6), xytext=(2.0, 1.2), arrowprops=dict(arrowstyle="->", color='#10B981', lw=2))

    b_fin = patches.FancyBboxPatch((0.8, 0.2), 2.4, 0.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                   facecolor='#ECFDF5', edgecolor='#10B981', lw=1.5)
    ax.add_patch(b_fin)
    ax.text(2.0, 0.4, "finally: # Selalu dieksekusi", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#065F46')

    # Right: Code Box
    c_box = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.4, boxstyle="round,pad=0.06,rounding_size=0.1",
                                   facecolor='#0F172A', edgecolor='#38BDF8', lw=2)
    ax.add_patch(c_box)
    ax.text(6.3, 3.5, "Skrip Python Kasir Andal:", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#38BDF8')

    code_exc = (
        "try:\n"
        "    beli = int(input('Jumlah: '))\n"
        "    total = 5000 * beli\n"
        "    print(f'Total: Rp{total}')\n"
        "except ValueError:\n"
        "    print('Error: Ketikkan angka valid!')\n"
        "    print('Program tetap aman berjalan.')\n"
        "finally:\n"
        "    print('Transaksi kasir selesai.')"
    )
    ax.text(4.7, 1.8, code_exc, ha='left', va='center', fontsize=7.8, color='#F8FAFC', linespacing=1.2)

    save_fig(fig, "bab2_alur_exception_handling_try_except.png")

# -------------------------------------------------------------
# 8. BAB 3: KOMIK PEMBUKA BASIS DATA
# -------------------------------------------------------------
def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#065F46', edgecolor='#064E3B')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 3: DARI BERKAS CSV LAMBAT MENUJU KEDAULATAN BASIS DATA SQL",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Berkas Teks Rusak", "bg": "#FEF2F2", "bdr": "#EF4444",
         "dialog": "Arya:\n'Aduh! Berkas CSV inventaris perpustakaan kita rusak (*corrupted*) karena dua siswa menyimpan data buku pada detik yang sama secara bersamaan!'",
         "status": "Redundansi & Tabrakan Data"},
        {"x": 3.0, "title": "Panel 2: Solusi Basis Data Relasional", "bg": "#EFF6FF", "bdr": "#2563EB",
         "dialog": "Dinda:\n'Sudah saatnya kita beralih ke Basis Data Relasional! Kita pisahkan tabel Buku, Anggota, dan Peminjaman dengan relasi Primary Key yang unik!'",
         "status": "Desain Relasi ERD"},
        {"x": 5.6, "title": "Panel 3: Keajaiban Query SQLite", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Bagas:\n'Hebat! Cukup sebaris perintah SELECT ... WHERE, data 10.000 buku terpanggil seketika dalam 0.001 detik! Python dan SQLite adalah perpaduan sempurna!'",
         "status": "SQL Terintegrasi"}
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
        ax.text(p["x"]+1.25, 2.95, "SQL\nMASTER", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab3_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 9. BAB 3: DIAGRAM ERD RELASIONAL
# -------------------------------------------------------------
def make_bab3_erd():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#065F46', edgecolor='#064E3B')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "DIAGRAM HUBUNGAN ENTITAS (ERD) SISTEM AKADEMIK SEKOLAH (NOTASI CROW'S FOOT)",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    # Table 1: JURUSAN
    t1 = patches.FancyBboxPatch((0.5, 1.2), 2.4, 2.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(t1)
    ax.text(1.7, 3.3, "TABEL JURUSAN", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1D4ED8')
    ax.plot([0.5, 2.9], [3.1, 3.1], color='#2563EB', lw=1.5)
    txt_t1 = (
        "[PK] id_jurusan (INT)\n"
        "     nama_jurusan (TEXT)\n"
        "     kuota_kelas (INT)"
    )
    ax.text(0.7, 2.4, txt_t1, ha='left', va='center', fontsize=7.5, color='#1E293B', linespacing=1.4)

    # Table 2: SISWA
    t2 = patches.FancyBboxPatch((5.6, 1.2), 2.4, 2.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor='#ECFDF5', edgecolor='#10B981', lw=2)
    ax.add_patch(t2)
    ax.text(6.8, 3.3, "TABEL SISWA", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#065F46')
    ax.plot([5.6, 8.0], [3.1, 3.1], color='#10B981', lw=1.5)
    txt_t2 = (
        "[PK] nis (TEXT)\n"
        "     nama_lengkap (TEXT)\n"
        "     tanggal_lahir (DATE)\n"
        "[FK] id_jurusan (INT)"
    )
    ax.text(5.8, 2.2, txt_t2, ha='left', va='center', fontsize=7.5, color='#1E293B', linespacing=1.4)

    # Connecting Crow's foot line (1-to-Many)
    ax.plot([2.9, 5.6], [2.4, 2.4], color='#334155', lw=2)
    ax.text(3.1, 2.6, "| (Satu)", fontsize=7.5, fontweight='bold', color='#334155')
    ax.text(5.3, 2.6, "< (Banyak)", fontsize=7.5, fontweight='bold', color='#334155')
    ax.text(4.25, 2.1, "Relasi 1-to-Many:\n'Satu Jurusan menaungi\nBanyak Siswa'",
            ha='center', va='center', fontsize=7.2, color='#475569')

    save_fig(fig, "bab3_diagram_erd_crows_foot_sekolah.png")

# -------------------------------------------------------------
# 10. BAB 3: ARSITEKTUR PERINTAH SQL
# -------------------------------------------------------------
def make_bab3_sql_commands():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "ARSITEKTUR PERINTAH SQL: DATA DEFINITION (DDL) VS DATA MANIPULATION (DML)",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    # DDL
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.4, "DATA DEFINITION LANGUAGE (DDL)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1D4ED8')
    txt_ddl = (
        "Membangun Struktur Kerangka Tabel:\n\n"
        "* CREATE TABLE: Membuat tabel baru\n"
        "  CREATE TABLE Siswa (\n"
        "      nis TEXT PRIMARY KEY,\n"
        "      nama TEXT NOT NULL,\n"
        "      nilai REAL\n"
        "  );\n\n"
        "* DROP TABLE: Menghapus tabel permanen\n"
        "* ALTER TABLE: Mengubah struktur kolom"
    )
    ax.text(0.6, 1.8, txt_ddl, ha='left', va='center', fontsize=7.4, color='#1E293B', linespacing=1.15)

    # DML
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#ECFDF5', edgecolor='#10B981', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.4, "DATA MANIPULATION LANGUAGE (DML)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065F46')
    txt_dml = (
        "Mengelola Isi Data di Dalam Tabel:\n\n"
        "* INSERT INTO: Menambah baris data baru\n"
        "* SELECT: Membaca & menyaring data\n"
        "  SELECT * FROM Siswa\n"
        "  WHERE nilai >= 85\n"
        "  ORDER BY nama ASC;\n\n"
        "* UPDATE: Mengubah data yang sudah ada\n"
        "* DELETE: Menghapus baris rekaman tertentu"
    )
    ax.text(4.7, 1.8, txt_dml, ha='left', va='center', fontsize=7.4, color='#064E3B', linespacing=1.15)

    save_fig(fig, "bab3_tabel_arsitektur_perintah_sql.png")

# -------------------------------------------------------------
# 11. BAB 4: KOMIK PEMBUKA MULTIMEDIA SMA
# -------------------------------------------------------------
def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#C2410C', edgecolor='#9A3412')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 4: KAMPANYE MULTIMEDIA EDUKASI PELESTARIAN MANGROVE",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Krisis Abrasi Pantai", "bg": "#FFF7ED", "bdr": "#EA580C",
         "dialog": "Dinda:\n'Hutan mangrove di pesisir desa kita rusak parah, memicu abrasi pantai! Kita harus membuat video edukasi publik yang menggugah masyarakat luas!'",
         "status": "Riset Pesan Publik"},
        {"x": 3.0, "title": "Panel 2: Rekayasa Bitrate & Rasio", "bg": "#EFF6FF", "bdr": "#2563EB",
         "dialog": "Arya:\n'Gunakan aspek rasio 9:16 untuk video seluler vertikal dan 16:9 untuk presentasi! Atur bitrate video secara cermat agar jernih namun hemat kuota!'",
         "status": "Optimasi Teknis Media"},
        {"x": 5.6, "title": "Panel 3: Diseminasi Beretika", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Bagas:\n'Jangan lupa cantumkan label jika ada ilustrasi bantuan AI, patuhi hak cipta musik latar, dan sebarkan dengan narasi yang menyejukkan!'",
         "status": "Kampanye Beradab"}
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
        ax.text(p["x"]+1.25, 2.95, "MEDIA\nSTUDIO", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab4_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 12. BAB 4: ASPEK RASIO & BITRATE
# -------------------------------------------------------------
def make_bab4_rasio_bitrate():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#EA580C', edgecolor='#C2410C')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "ARSITEKTUR MULTIMEDIA: ASPEK RASIO 16:9 VS 9:16 & MANAJEMEN BITRATE",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    # Card 1: 16:9
    c1 = patches.FancyBboxPatch((0.4, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#EFF6FF', edgecolor='#2563EB', lw=2)
    ax.add_patch(c1)
    ax.text(2.2, 3.4, "RASIO HORIZONTAL 16:9 (LANDSCAPE)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1D4ED8')
    txt_16 = (
        "Karakteristik & Penggunaan:\n"
        "- Layar Laptop, TV, dan Proyektor Bioskop\n"
        "- Resolusi Baku: 1920 x 1080 piksel (Full HD)\n"
        "- Memberikan bidang pandang sinematik luas\n\n"
        "Bitrate Rekomendasi:\n"
        "8 - 12 Mbps (Menghasilkan warna kaya tanpa\n"
        "gangguan artefak piksel buram)."
    )
    ax.text(0.6, 1.8, txt_16, ha='left', va='center', fontsize=7.4, color='#1E293B', linespacing=1.2)

    # Card 2: 9:16
    c2 = patches.FancyBboxPatch((4.5, 0.4), 3.6, 3.3, boxstyle="round,pad=0.06,rounding_size=0.1",
                                facecolor='#FFF7ED', edgecolor='#EA580C', lw=2)
    ax.add_patch(c2)
    ax.text(6.3, 3.4, "RASIO VERTIKAL 9:16 (PORTRAIT)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#C2410C')
    txt_9 = (
        "Karakteristik & Penggunaan:\n"
        "- Layar Ponsel Pintar Seluler (Reels, TikTok, Shorts)\n"
        "- Resolusi Baku: 1080 x 1920 piksel\n"
        "- Sangat ergonomis dipegang satu tangan\n\n"
        "Manajemen Kompresi:\n"
        "Gunakan codec H.264/AAC dengan bitrate 4-6 Mbps\n"
        "agar video langsung berputar instan (*no buffering*)."
    )
    ax.text(4.7, 1.8, txt_9, ha='left', va='center', fontsize=7.4, color='#7C2D12', linespacing=1.2)

    save_fig(fig, "bab4_diagram_aspek_rasio_bitrate.png")

# -------------------------------------------------------------
# 13. BAB 5: KOMIK PEMBUKA COMPUTER VISION
# -------------------------------------------------------------
def make_bab5_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#047857', edgecolor='#065F46')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 5: MEMBONGKAR MATA CERDAS COMPUTER VISION & SPEKTROGRAM",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Kamera Mengabstraksi", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Bagas:\n'Bagi manusia, ini adalah foto kucing anggora yang lucu. Tapi di dalam prosesor komputer, foto ini hanyalah deretan jutaan angka matriks piksel 0 sampai 255!'",
         "status": "Representasi Matriks"},
        {"x": 3.0, "title": "Panel 2: Filter Konvolusi", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Arya:\n'Betul! Dan AI menggunakan matriks filter kecil (Convolutional Filter) yang menggeser dan mengalikan piksel untuk menemukan tepi telinga dan kumis kucing!'",
         "status": "Ekstraksi Fitur Tepi"},
        {"x": 5.6, "title": "Panel 3: Spektrogram Suara", "bg": "#FAF5FF", "bdr": "#9333EA",
         "dialog": "Dinda:\n'Begitu juga suara miaw kucing: gelombang getarannya diubah menjadi gambar frekuensi warna-warni (Spektrogram) sebelum dikenali model AI!'",
         "status": "Audio Recognition"}
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
        ax.text(p["x"]+1.25, 2.95, "VISION\nAI", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab5_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 14. BAB 5: MATRIKS KONVOLUSI PIKSEL
# -------------------------------------------------------------
def make_bab5_konvolusi():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#065F46', edgecolor='#064E3B')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "OPERASI MATRIKS KONVOLUSI DALAM COMPUTER VISION (DETEKSI TEPI GAMBAR)",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    # Matrix 1: Input Pixels (5x5)
    ax.text(1.8, 3.6, "Matriks Piksel Asli (5x5):", fontsize=8.2, fontweight='bold', color='#1E293B')
    m_box1 = patches.FancyBboxPatch((0.6, 1.0), 2.4, 2.4, boxstyle="square,pad=0.02",
                                    facecolor='#EFF6FF', edgecolor='#2563EB', lw=1.5)
    ax.add_patch(m_box1)
    grid_txt1 = (
        "100  100  100    0    0\n"
        "100  100  100    0    0\n"
        "100  100  100    0    0\n"
        "100  100  100    0    0\n"
        "100  100  100    0    0"
    )
    ax.text(1.8, 2.2, grid_txt1, ha='center', va='center', fontsize=7.5, color='#1E293B', family='monospace')

    # Multiplication operator
    ax.text(3.4, 2.2, "*", fontsize=16, fontweight='bold', color='#334155')

    # Matrix 2: Kernel Filter (3x3 Sobel Vertical)
    ax.text(4.25, 3.6, "Filter Kernel (3x3):", fontsize=8.2, fontweight='bold', color='#1E293B')
    m_box2 = patches.FancyBboxPatch((3.5, 1.4), 1.5, 1.6, boxstyle="square,pad=0.02",
                                    facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5)
    ax.add_patch(m_box2)
    grid_txt2 = (
        "-1   0   1\n"
        "-2   0   2\n"
        "-1   0   1"
    )
    ax.text(4.25, 2.2, grid_txt2, ha='center', va='center', fontsize=7.5, color='#92400E', family='monospace')

    # Arrow to Output
    ax.annotate("", xy=(5.5, 2.2), xytext=(5.1, 2.2), arrowprops=dict(arrowstyle="->", color='#10B981', lw=3))

    # Matrix 3: Feature Map Result
    ax.text(6.8, 3.6, "Feature Map (Deteksi Garis):", fontsize=8.2, fontweight='bold', color='#065F46')
    m_box3 = patches.FancyBboxPatch((5.6, 1.2), 2.4, 2.0, boxstyle="square,pad=0.02",
                                    facecolor='#ECFDF5', edgecolor='#10B981', lw=1.5)
    ax.add_patch(m_box3)
    grid_txt3 = (
        "  0  400    0\n"
        "  0  400    0\n"
        "  0  400    0"
    )
    ax.text(6.8, 2.2, grid_txt3, ha='center', va='center', fontsize=8.2, color='#065F46', family='monospace', fontweight='bold')
    ax.text(6.8, 0.7, "Nilai 400 = Garis Tepi Vertikal!", ha='center', va='center', fontsize=7.2, color='#065F46')

    save_fig(fig, "bab5_diagram_matriks_konvolusi_piksel.png")

# -------------------------------------------------------------
# 15. BAB 5: PETA KARIER AI
# -------------------------------------------------------------
def make_bab5_peta_karier():
    fig, ax = plt.subplots(figsize=(8.5, 4.5), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.5); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 3.9), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E293B', edgecolor='#0F172A')
    ax.add_patch(title)
    ax.text(4.25, 4.12, "LANSKAP PROFESI MASA DEPAN DI ERA KECERDASAN ARTIFISIAL & SAINS DATA",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    careers = [
        {"name": "AI ENGINEER", "role": "Arsitek Model", "desc": "Merancang dan melatih arsitektur jaringan saraf tiruan (neural networks).", "bg": "#EFF6FF", "bdr": "#2563EB", "x": 0.5},
        {"name": "DATA SCIENTIST", "role": "Penyelidik Pola", "desc": "Mengekstraksi wawasan berharga dari miliaran data besar untuk strategi bisnis.", "bg": "#ECFDF5", "bdr": "#10B981", "x": 2.45},
        {"name": "PROMPT ENGINEER", "role": "Spesialis Input", "desc": "Menyusun struktur prompt industri tingkat lanjut (ROCCF) agar hasil AI presisi.", "bg": "#FEF3C7", "bdr": "#D97706", "x": 4.4},
        {"name": "AI ETHICS OFFICER", "role": "Penjaga Keadilan", "desc": "Mengaudit sistem AI agar bebas bias, mematuhi UU privasi, dan beretika.", "bg": "#FAF5FF", "bdr": "#8B5CF6", "x": 6.35}
    ]

    for c in careers:
        box = patches.FancyBboxPatch((c["x"], 0.5), 1.65, 3.1, boxstyle="round,pad=0.04,rounding_size=0.08",
                                     facecolor=c["bg"], edgecolor=c["bdr"], lw=1.8)
        ax.add_patch(box)

        ax.text(c["x"]+0.825, 3.25, c["name"], ha='center', va='center', fontsize=7.6, fontweight='bold', color=c["bdr"])
        ax.text(c["x"]+0.825, 2.95, c["role"], ha='center', va='center', fontsize=6.8, color='#475569')

        ax.text(c["x"]+0.825, 1.8, c["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B', wrap=True,
                multialignment='center')

    save_fig(fig, "bab5_peta_ekosistem_karier_ai_masa_depan.png")

# -------------------------------------------------------------
# 16. BAB 6: KOMIK PEMBUKA AI SYSTEM DESIGN
# -------------------------------------------------------------
def make_bab6_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#4338CA', edgecolor='#3730A3')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK PEMBUKA BAB 6: MERANCANG PROPOSAL SISTEM AI BERPUSAT PADA MANUSIA",
            ha='center', va='center', fontsize=10.0, fontweight='bold', color='#FFFFFF')

    panels = [
        {"x": 0.4, "title": "Panel 1: Menguji Mutu Konten", "bg": "#EEF2FF", "bdr": "#6366F1",
         "dialog": "Dinda:\n'Prompt amatir menghasilkan jawaban umum yang membosankan! Tapi dengan framework ROCCF (Role, Objective, Context, Constraint, Format), respon AI menjadi sangat presisi!'",
         "status": "Model ROCCF Teruji"},
        {"x": 3.0, "title": "Panel 2: Rancang Bangun Sistem", "bg": "#EFF6FF", "bdr": "#3B82F6",
         "dialog": "Arya:\n'Mari kita susun dokumen AI System Design untuk presensi cerdas sekolah: kita tentukan kamera sensor masukan, database SQLite, dan tombol verifikasi manual!'",
         "status": "Arsitektur Sistem"},
        {"x": 5.6, "title": "Panel 3: Kemanusiaan Sebagai Raja", "bg": "#ECFDF5", "bdr": "#10B981",
         "dialog": "Bagas:\n'Ingat prinsip Human-Centered AI: mesin hanya membantu merekomendasikan, keputusan final tetap berada di tangan guru manusia! Inilah penuntasan Fase E yang membanggakan!'",
         "status": "Tuntas Paripurna Fase E"}
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
        ax.text(p["x"]+1.25, 2.95, "SYSTEM\nDESIGN", ha='center', va='center', fontsize=7.2, fontweight='bold', color=p["bdr"])

        ax.text(p["x"]+1.25, 1.8, p["dialog"], ha='center', va='center', fontsize=8.2, color='#1E293B', wrap=True,
                multialignment='center')

        pill = patches.FancyBboxPatch((p["x"]+0.2, 0.55), 2.1, 0.32, boxstyle="round,pad=0.03,rounding_size=0.08",
                                      facecolor=p["bdr"], edgecolor=p["bdr"])
        ax.add_patch(pill)
        ax.text(p["x"]+1.25, 0.71, p["status"], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#FFFFFF')

    save_fig(fig, "bab6_komik_pembuka_sma10.png")

# -------------------------------------------------------------
# 17. BAB 6: PIRAMIDA ROCCF
# -------------------------------------------------------------
def make_bab6_roccf():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#FFFFFF')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    title = patches.FancyBboxPatch((0.5, 4.0), 7.5, 0.45, boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='#1E40AF', edgecolor='#1D4ED8')
    ax.add_patch(title)
    ax.text(4.25, 4.22, "FRAMEWORK PROMPT ENGINEERING INDUSTRI: FORMULA MODEL ROCCF",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color='#FFFFFF')

    layers = [
        {"letter": "R", "title": "ROLE (PERAN SPESIFIK)", "desc": "Bertindaklah sebagai Senior Software Engineer & Pakar Keamanan Siber...", "color": "#1E3A8A", "y": 3.3},
        {"letter": "O", "title": "OBJECTIVE (TUJUAN JELAS)", "desc": "Tujuan utama: Buatlah skrip fungsi Python untuk validasi kata sandi...", "color": "#2563EB", "y": 2.65},
        {"letter": "C", "title": "CONTEXT (KONTEKS DATA)", "desc": "Konteks: Aplikasi ini akan digunakan oleh 1.500 siswa di sistem perpustakaan...", "color": "#0284C7", "y": 2.0},
        {"letter": "C", "title": "CONSTRAINT (BATASAN KETAT)", "desc": "Batasan: Panjang minimal 12 karakter, wajib ada simbol, tanpa library pihak ketiga...", "color": "#0D9488", "y": 1.35},
        {"letter": "F", "title": "FORMAT (BENTUK LUARAN)", "desc": "Keluaran: Sajikan dalam format blok kode Python beranotasi komentar rapi...", "color": "#059669", "y": 0.7}
    ]

    for l in layers:
        pill_l = patches.FancyBboxPatch((0.7, l["y"]-0.22), 0.5, 0.45, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        facecolor=l["color"], edgecolor=l["color"])
        ax.add_patch(pill_l)
        ax.text(0.95, l["y"], l["letter"], ha='center', va='center', fontsize=12, fontweight='bold', color='#FFFFFF')

        bar = patches.FancyBboxPatch((1.3, l["y"]-0.22), 6.5, 0.45, boxstyle="round,pad=0.03,rounding_size=0.06",
                                     facecolor='#F8FAFC', edgecolor=l["color"], lw=1.5)
        ax.add_patch(bar)
        ax.text(1.5, l["y"]+0.06, l["title"], ha='left', va='center', fontsize=7.8, fontweight='bold', color=l["color"])
        ax.text(3.4, l["y"]-0.04, l["desc"], ha='left', va='center', fontsize=7.0, color='#334155')

    save_fig(fig, "bab6_piramida_framework_roccf_prompt.png")

# -------------------------------------------------------------
# 18. COVER BUKU SISWA SMA/SMK KELAS 10
# -------------------------------------------------------------
def make_cover_sma10():
    img = Image.new('RGB', (1800, 2700), color='#1E293B')
    draw = ImageDraw.Draw(img)

    for y in range(800):
        ratio = y / 800
        r = int(15 + (30 - 15) * ratio)
        g = int(23 + (58 - 23) * ratio)
        b = int(42 + (138 - 42) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(800, 1900):
        ratio = (y - 800) / 1100
        r = int(30 + (4 - 30) * ratio)
        g = int(58 + (120 - 58) * ratio)
        b = int(138 + (87 - 138) * ratio)
        draw.line([(0, y), (1800, y)], fill=(r, g, b))

    for y in range(1900, 2700):
        ratio = (y - 1900) / 800
        r = int(4 + (15 - 4) * ratio)
        g = int(120 + (23 - 120) * ratio)
        b = int(87 + (42 - 87) * ratio)
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

    draw.rectangle([100, 90, 880, 160], fill='#1E40AF')
    draw.text((130, 102), "BUKU TEKS SMA / MA / SMK", font=f_badge, fill='#FFFFFF')

    draw.text((100, 260), "KODING DAN", font=f_title, fill='#FFFFFF')
    draw.text((100, 370), "KECERDASAN", font=f_title, fill='#38BDF8')
    draw.text((100, 480), "ARTIFISIAL", font=f_title, fill='#FACC15')

    # Grade Pill Badge
    draw.rectangle([100, 620, 1050, 720], fill='#B45309')
    draw.text((130, 642), "KELAS X  •  FASE E (SMA/SMK)", font=f_phase, fill='#FFFFFF')

    # Big Rounded Showcase Card
    draw.rounded_rectangle([150, 820, 1650, 1920], radius=40, fill='#0B1329', outline='#38BDF8', width=8)

    draw.text((220, 900), "KURIKULUM NASIONAL KKA KEMENDIKDASMEN RI", font=f_badge, fill='#FACC15')
    draw.text((220, 980), "Pondasi Sains Komputasi & AI Terapan Menengah (Fase E):", font=f_sub, fill='#FFFFFF')

    features = [
        "v  Analisis Efisiensi Algoritma: Linear vs Binary Search & Notasi Big-O",
        "v  Python Terapan: List, Dictionary, Exception Handling & Debugging PEP 8",
        "v  Arsitektur Basis Data Relasional, Diagram ERD & Kueri SQL Terintegrasi",
        "v  Produksi Konten Multimedia Interaktif, Rasio 16:9 & Diseminasi Digital",
        "v  Computer Vision (Matriks Konvolusi 3x3) & Spektrogram Audio AI",
        "v  Framework Prompt Engineering ROCCF & Human-Centered AI System Design"
    ]

    curr_y = 1080
    for feat in features:
        draw.text((220, curr_y), feat, font=f_phase, fill='#E2E8F0')
        curr_y += 120

    # Author Box
    draw.rounded_rectangle([100, 2020, 1700, 2300], radius=30, fill='#FFFFFF', outline='#1E40AF', width=5)
    draw.text((150, 2060), "Penulis: Gede Erik Aktama, S.Pd., M.Pd.", font=f_auth, fill='#0F172A')
    draw.text((150, 2130), "Fasilitator Nasional Bimbingan Teknis & ToT KKA Kemendikdasmen RI", font=f_role, fill='#1E40AF')
    draw.text((150, 2185), "Dosen Lektor & Kaprodi S1 Sistem Komputer, Universitas Parna Raya", font=f_role, fill='#475569')

    # Publisher Footer
    draw.text((900, 2390), "PUSAT PERBUKUAN", font=f_pub, fill='#FFFFFF', anchor="mm")
    draw.text((900, 2450), "BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2505), "KEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI", font=f_subpub, fill='#E2E8F0', anchor="mm")
    draw.text((900, 2560), "TAHUN 2025 / 2026", font=f_subpub, fill='#FACC15', anchor="mm")

    local_cov = os.path.join(local_assets, "cover_buku_siswa_sma10.jpg")
    img.save(local_cov, quality=95)
    tot_cov = os.path.join(tot_assets, "cover_buku_siswa_sma10.jpg")
    try:
        shutil.copy2(local_cov, tot_cov)
    except Exception as e:
        print(f"Warning copying cover: {e}")
    print("Generated cover: cover_buku_siswa_sma10.jpg")

if __name__ == "__main__":
    print("Starting visual assets generation for Grade 10 SMA/SMK...")
    make_tokoh_sahabat()
    make_bab1_komik()
    make_bab1_search_comparison()
    make_bab1_sorting()
    make_bab1_big_o()
    make_bab2_komik()
    make_bab2_struktur_data()
    make_bab2_exception_handling()
    make_bab3_komik()
    make_bab3_erd()
    make_bab3_sql_commands()
    make_bab4_komik()
    make_bab4_rasio_bitrate()
    make_bab5_komik()
    make_bab5_konvolusi()
    make_bab5_peta_karier()
    make_bab6_komik()
    make_bab6_roccf()
    make_cover_sma10()
    print("All visual assets for Grade 10 SMA/SMK successfully generated!")
