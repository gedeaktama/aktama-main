# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Bab 1: Petualangan Berpikir Komputasional
Resolusi Tinggi 300 DPI, Bergaya Infografis Edukatif Ramah Anak, Penuh Warna,
Menarik dan Memikat untuk Buku Siswa SD Kelas 5.
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
        print(f"Warning copying {filename}: {e}")
    print(f"Bab 1 Illustration Ready: {filename}")

# -------------------------------------------------------------
# 1. Komik Strip Pembuka 4 Panel (Kamar Erik yang Berantakan)
# -------------------------------------------------------------
def make_komik_pembuka():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    # Title Banner
    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: MISTERI SEPATU ERIK YANG LENYAP",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Kamar Berantakan", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "ERIK:\n\"Aduh! Jam 7 kurang 15!\nDi mana sepatu kiriku?\nKamarku berantakan sekali,\nsemua barang bertumpuk!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Teman Datang", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "SITI & MADE:\n\"Erik, ayo cepat!\nNanti kita terlambat upacara!\nKenapa kamu belum pakai\nsepatu hitammu?\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Robot Kibo Datang", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Jangan panik, Erik!\nPikiranmu pusing karena\nmelihat kamar sebagai\nsatu masalah raksasa!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Jurus Komputasi", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "KIBO & ERIK:\n\"Gunakan Jurus DEKOMPOSISI!\nBagi kamar jadi 3 kotak kecil:\nKasur, Meja, Rak Sepatu!\nSepatunya ketemu di rak!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        # Box panel
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        # Header panel
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        # Dialog
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab1_komik_pembuka.png")

# -------------------------------------------------------------
# 2. Gambar 1.1: Konsep Dekomposisi (Analogi Irisan Pizza Tugas)
# -------------------------------------------------------------
def make_dekomposisi_pizza():
    fig, ax = plt.subplots(figsize=(8.2, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.4); ax.axis('off')

    ax.text(4.1, 4.15, "JURUS 1: DEKOMPOSISI (MEMOTONG MASALAH SEPERTI MEMOTONG PIZZA)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Left: Masalah Raksasa (Pizza Utuh Besar)
    b_left = patches.FancyBboxPatch((0.4, 0.5), 3.4, 3.3, boxstyle="round,pad=0.06,rounding_size=0.15",
                                    facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(b_left)
    ax.text(2.1, 3.45, "MASALAH RAKSASA (RUMIT)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B91C1C')
    # Big circle pizza
    c_big = patches.Circle((2.1, 2.2), 0.9, facecolor='#FCA5A5', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(c_big)
    ax.text(2.1, 2.2, "TUGAS BESAR:\n\"Membersihkan Seluruh\nRuang Kelas 5\"\n(Bingung mulai dari mana)",
            ha='center', va='center', fontsize=7.2, fontweight='bold', color='#7F1D1D')
    ax.text(2.1, 0.9, "Jangan ditelan bulat-bulat!\nPikiranmu akan kelelahan!",
            ha='center', va='center', fontsize=7.5, fontstyle='italic', color='#991B1B')

    # Arrow Transformation
    ax.annotate('', xy=(4.4, 2.2), xytext=(3.9, 2.2),
                arrowprops=dict(facecolor='#0284C7', edgecolor='#0284C7', width=2.5, headwidth=8))
    ax.text(4.15, 2.5, "DIPOTONG\n(Dekomposisi)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0284C7')

    # Right: Potongan Kecil yang Mudah
    b_right = patches.FancyBboxPatch((4.5, 0.5), 3.4, 3.3, boxstyle="round,pad=0.06,rounding_size=0.15",
                                     facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=2)
    ax.add_patch(b_right)
    ax.text(6.2, 3.45, "SUB-TUGAS KECIL (MUDAH)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803D')

    slices = [
        ("Potongan 1: Siti menyapu lantai ruang kelas", 2.8),
        ("Potongan 2: Erik merapikan meja & kursi guru", 2.2),
        ("Potongan 3: Made menghapus papan tulis putih", 1.6),
        ("Potongan 4: Kibo membuang kantong sampah", 1.0),
    ]
    for text, y in slices:
        box_s = patches.Rectangle((4.7, y - 0.2), 3.0, 0.38, facecolor='#DCFCE7', edgecolor='#22C55E')
        ax.add_patch(box_s)
        ax.text(6.2, y, text, ha='center', va='center', fontsize=7.2, color='#14532D')

    save_fig(fig, "bab1_dekomposisi_pizza.png")

# -------------------------------------------------------------
# 3. Gambar 1.2: Pengenalan Pola (Batik Nusantara, Alam, Deret)
# -------------------------------------------------------------
def make_pola_batik():
    fig, ax = plt.subplots(figsize=(8.2, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.4); ax.axis('off')

    ax.text(4.1, 4.15, "JURUS 2: PENGENALAN POLA (MENEMUKAN KETERATURAN DI SEKITAR KITA)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    cards = [
        {"title": "1. POLA ALAM\n(Simetri Kupu-Kupu)", "col": "#0D9488", "bg": "#F0FDFA",
         "desc": "Sayap kiri dan sayap kanan\nkupu-kupu selalu memiliki\nbentuk dan warna yang sama\n(pola cermin / simetri).", "x": 1.1},
        {"title": "2. POLA BATIK\n(Motif Kawung Jawa)", "col": "#D97706", "bg": "#FFFBEB",
         "desc": "Motif lingkaran lonjong 4 sisi\ndiulang ratusan kali dengan\njarak teratur menghasilkan\nkain batik yang sangat indah.", "x": 3.1},
        {"title": "3. POLA IRAMA\n(Gamelan / Musik)", "col": "#7C3AED", "bg": "#F5F3FF",
         "desc": "Dentang gong berbunyi:\n[Tung - Tang - Ting - GONG!]\nIrama berulang membuat penari\ntahu kapan harus berputar.", "x": 5.1},
        {"title": "4. POLA ANGKA\n(Koding Komputer)", "col": "#0284C7", "bg": "#F0F9FF",
         "desc": "Deret langkah Kibo:\n2,  4,  6,  8,  [ ...? ]\nPola: Selalu ditambah 2!\nAngka berikutnya adalah 10!", "x": 7.1},
    ]

    for c in cards:
        x = c["x"]
        card = patches.FancyBboxPatch((x - 0.85, 0.4), 1.7, 3.3, boxstyle="round,pad=0.06,rounding_size=0.15",
                                      facecolor=c["bg"], edgecolor=c["col"], linewidth=2)
        ax.add_patch(card)
        ax.text(x, 3.3, c["title"], ha='center', va='center', fontsize=7.8, fontweight='bold', color=c["col"])
        # Inner decorative circle
        circ = patches.Circle((x, 2.3), 0.45, facecolor='#FFFFFF', edgecolor=c["col"], linewidth=1.5)
        ax.add_patch(circ)
        ax.text(x, 2.3, "POLA", ha='center', va='center', fontsize=8, fontweight='bold', color=c["col"])
        ax.text(x, 1.25, c["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B')

    save_fig(fig, "bab1_pola_batik_alam.png")

# -------------------------------------------------------------
# 4. Gambar 1.3: Konsep Abstraksi (Peta Nyata vs Peta Garis Jalur)
# -------------------------------------------------------------
def make_abstraksi_peta():
    fig, ax = plt.subplots(figsize=(8.2, 4.4), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.4); ax.axis('off')

    ax.text(4.1, 4.15, "JURUS 3: ABSTRAKSI (MEMILAH INFORMASI PENTING SEPERTI MEMBACA PETA)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Left: Peta Terlalu Rinci (Bikin Bingung)
    b_left = patches.FancyBboxPatch((0.4, 0.5), 3.4, 3.3, boxstyle="round,pad=0.06,rounding_size=0.15",
                                    facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(b_left)
    ax.text(2.1, 3.45, "DUNIA NYATA: TERLALU BANYAK DETAIL", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B91C1C')
    details = (
        "• Warna genteng rumah tetangga (merah/biru)\n"
        "• Jumlah daun di pohon mangga pinggir jalan\n"
        "• Kucing hitam yang sedang tidur di trotoar\n"
        "• Merek ban mobil yang parkir\n\n"
        "-> Semua detail ini TIDAK PENTING\n"
        "   untuk mencari jalan ke sekolah!"
    )
    ax.text(2.1, 1.9, details, ha='center', va='center', fontsize=7.5, color='#7F1D1D')

    # Right: Peta Hasil Abstraksi (Jelas & Cepat Dipahami)
    b_right = patches.FancyBboxPatch((4.4, 0.5), 3.4, 3.3, boxstyle="round,pad=0.06,rounding_size=0.15",
                                     facecolor='#F0FDFA', edgecolor='#0D9488', linewidth=2)
    ax.add_patch(b_right)
    ax.text(6.1, 3.45, "HASIL ABSTRAKSI: FOKUS PADA INTI", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0F766E')
    # Simple line route
    ax.plot([4.8, 5.8, 7.0], [2.6, 2.6, 1.3], color='#0D9488', linewidth=3)
    ax.scatter([4.8, 5.8, 7.0], [2.6, 2.6, 1.3], color='#042F2E', s=80, zorder=5)
    ax.text(4.8, 2.85, "Rumah Erik", ha='center', fontsize=7.5, fontweight='bold', color='#0D9488')
    ax.text(5.8, 2.85, "Perempatan", ha='center', fontsize=7.5, fontweight='bold', color='#0D9488')
    ax.text(7.0, 1.05, "SEKOLAH (TIBA)", ha='center', fontsize=7.5, fontweight='bold', color='#059669')
    ax.text(6.1, 0.8, "Hanya menampilkan: Titik Belokan & Nama Jalan!\nInilah yang dinamakan ABSTRAKSI!",
            ha='center', va='center', fontsize=7.2, fontstyle='italic', color='#134E4A')

    save_fig(fig, "bab1_abstraksi_peta.png")

# -------------------------------------------------------------
# 5. Gambar 1.4: Bagan Alir Flowchart dengan Percabangan Keputusan
# -------------------------------------------------------------
def make_flowchart_teh():
    fig, ax = plt.subplots(figsize=(7.5, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 7.5); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(3.75, 4.3, "BAGAN ALIR (FLOWCHART): ALGORITMA MEMBUAT TEH MANIS HANGAT",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')

    # 1. Start (Oval)
    p_start = patches.FancyBboxPatch((2.7, 3.7), 2.1, 0.4, boxstyle="round,pad=0.05,rounding_size=0.2",
                                     facecolor='#10B981', edgecolor='#059669')
    ax.add_patch(p_start)
    ax.text(3.75, 3.9, "MULAI (START)", ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')

    # Arrow 1
    ax.annotate('', xy=(3.75, 3.25), xytext=(3.75, 3.7),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=1.5, headwidth=5))

    # 2. Seduh Teh (Rect)
    ax.add_patch(patches.Rectangle((2.0, 2.8), 3.5, 0.42, facecolor='#E0F2FE', edgecolor='#0284C7', linewidth=1.5))
    ax.text(3.75, 3.01, "Seduh Kantong Teh dengan Air Panas", ha='center', va='center', fontsize=7.5, color='#0369A1')

    # Arrow 2
    ax.annotate('', xy=(3.75, 2.35), xytext=(3.75, 2.8),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', width=1.5, headwidth=5))

    # 3. Decision (Belah Ketupat)
    diamond = patches.Polygon([[3.75, 2.3], [5.2, 1.7], [3.75, 1.1], [2.3, 1.7]],
                              facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.8)
    ax.add_patch(diamond)
    ax.text(3.75, 1.7, "Apakah Teh\nSudah Manis?", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#92400E')

    # Loop "TIDAK" (Kembali tambah gula)
    ax.annotate('', xy=(2.0, 3.01), xytext=(2.3, 1.7),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', width=1.2, headwidth=5))
    ax.text(1.3, 2.2, "[TIDAK]\nTambah 1 Sendok\nGula & Aduk", fontsize=6.8, fontweight='bold', color='#DC2626')

    # Yes Arrow down to Finish
    ax.annotate('', xy=(3.75, 0.65), xytext=(3.75, 1.1),
                arrowprops=dict(facecolor='#059669', edgecolor='#059669', width=1.5, headwidth=5))
    ax.text(4.2, 0.88, "[YA, PAS!]", fontsize=7, fontweight='bold', color='#059669')

    # 4. Finish (Oval)
    p_end = patches.FancyBboxPatch((2.7, 0.25), 2.1, 0.38, boxstyle="round,pad=0.05,rounding_size=0.2",
                                   facecolor='#EF4444', edgecolor='#DC2626')
    ax.add_patch(p_end)
    ax.text(3.75, 0.44, "SELESAI DIMINUM", ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')

    # Legend
    ax.text(5.5, 3.7, "Oval = Mulai / Akhir", fontsize=7, color='#475569')
    ax.text(5.5, 3.01, "Persegi = Aksi Langkah", fontsize=7, color='#475569')
    ax.text(5.5, 1.7, "Belah Ketupat =\nKeputusan / Percabangan", fontsize=7, color='#D97706')

    save_fig(fig, "bab1_flowchart_teh_manis.png")

# -------------------------------------------------------------
# 6. Gambar 1.5: Robot Kibo Melacak Bug & Debugging
# -------------------------------------------------------------
def make_kibo_debugging():
    fig, ax = plt.subplots(figsize=(8.0, 4.2), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 4.2); ax.axis('off')

    ax.text(4.0, 3.9, "DETEKTIF LOGIKA: APA ITU BUG DAN BAGAIMANA CARA DEBUGGING?",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    # Left: Apa itu Bug?
    b1 = patches.FancyBboxPatch((0.4, 0.4), 3.4, 3.1, boxstyle="round,pad=0.06,rounding_size=0.15",
                                facecolor='#FEF2F2', edgecolor='#DC2626', linewidth=2)
    ax.add_patch(b1)
    ax.text(2.1, 3.15, "APA ITU \"BUG\"?", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#B91C1C')
    t_bug = (
        "• Bug adalah KESALAHAN pada urutan\n"
        "  perintah program komputer.\n\n"
        "• Akibat ada Bug:\n"
        "  - Robot Kibo menabrak tembok\n"
        "  - Karakter kucing berjalan mundur\n"
        "  - Game tiba-tiba berhenti macet\n\n"
        "• Bug BUKAN karena komputernya rusak,\n"
        "  tapi ada langkah instruksi yang terbalik!"
    )
    ax.text(2.1, 1.7, t_bug, ha='center', va='center', fontsize=7.5, color='#7F1D1D')

    # Right: Cara Debugging Koder Hebat
    b2 = patches.FancyBboxPatch((4.2, 0.4), 3.4, 3.1, boxstyle="round,pad=0.06,rounding_size=0.15",
                                facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=2)
    ax.add_patch(b2)
    ax.text(5.9, 3.15, "CARA \"DEBUGGING\" KODER JUARA", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803D')
    t_deb = (
        "1. TETAP TENANG & TERSENYUM\n"
        "   Jangan marah atau menyalahkan laptop.\n\n"
        "2. TELITI LANGKAH DEMI LANGKAH\n"
        "   Periksa baris perintah satu per satu.\n\n"
        "3. TEMUKAN KARTU YANG SALAH\n"
        "   Apakah ada balok yang terbalik posisinya?\n\n"
        "4. UJI COBA KEMBALI HINGGA BERHASIL!\n"
        "   \"Kesalahan adalah cara otak kita belajar!\""
    )
    ax.text(5.9, 1.7, t_deb, ha='center', va='center', fontsize=7.3, color='#14532D')

    save_fig(fig, "bab1_kibo_debugging.png")

# -------------------------------------------------------------
# 7. Gambar 1.6: Mind Map Rangkuman 4 Pilar Komputasi
# -------------------------------------------------------------
def make_mindmap_rangkuman():
    fig, ax = plt.subplots(figsize=(8.2, 4.5), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.5); ax.axis('off')

    # Center Hub
    hub = patches.FancyBboxPatch((3.1, 1.8), 2.0, 0.9, boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor='#1E293B', edgecolor='#0F172A', linewidth=2)
    ax.add_patch(hub)
    ax.text(4.1, 2.25, "BERPIKIR\nKOMPUTASIONAL", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

    nodes = [
        {"title": "DEKOMPOSISI", "sub": "Memecah tugas besar\njadi bagian kecil", "col": "#0284C7", "bg": "#E0F2FE", "x": 1.4, "y": 3.4},
        {"title": "PENGENALAN POLA", "sub": "Melihat kesamaan\ndan keteraturan berulang", "col": "#0D9488", "bg": "#CCFBF1", "x": 6.8, "y": 3.4},
        {"title": "ABSTRAKSI", "sub": "Menyaring hal penting,\nmengabaikan rincian", "col": "#D97706", "bg": "#FEF3C7", "x": 1.4, "y": 1.0},
        {"title": "ALGORITMA", "sub": "Menyusun langkah urut\nlogis tanpa ambigu", "col": "#7C3AED", "bg": "#EDE9FE", "x": 6.8, "y": 1.0},
    ]

    for n in nodes:
        box = patches.FancyBboxPatch((n["x"] - 1.1, n["y"] - 0.45), 2.2, 0.9, boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor=n["bg"], edgecolor=n["col"], linewidth=2)
        ax.add_patch(box)
        ax.text(n["x"], n["y"] + 0.15, n["title"], ha='center', va='center', fontsize=8.5, fontweight='bold', color=n["col"])
        ax.text(n["x"], n["y"] - 0.18, n["sub"], ha='center', va='center', fontsize=6.8, color='#334155')

        # Line to center
        ax.plot([n["x"], 4.1], [n["y"], 2.25], color=n["col"], linewidth=1.8, linestyle='--', zorder=1)

    save_fig(fig, "bab1_mindmap_rangkuman.png")

if __name__ == "__main__":
    make_komik_pembuka()
    make_dekomposisi_pizza()
    make_pola_batik()
    make_abstraksi_peta()
    make_flowchart_teh()
    make_kibo_debugging()
    make_mindmap_rangkuman()
    print("ALL BAB 1 VIBRANT ILLUSTRATIONS GENERATED SUCCESSFULLY!")
