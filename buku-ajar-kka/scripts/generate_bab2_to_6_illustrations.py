# -*- coding: utf-8 -*-
"""
Generator Ilustrasi Visual Edukatif Bab 2 - Bab 6 (Buku Siswa KKA Kelas 5 SD)
Resolusi Tinggi 300 DPI, Gaya Infografis Ramah Anak, Penuh Warna, Edukatif.
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
    print(f"Asset Created: {filename}")

# ==============================================================================
# BAB 2: TEKNOLOGI DIGITAL & PERANGKAT KOMPUTER
# ==============================================================================

def make_bab2_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    # Title Banner
    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0D9488', edgecolor='#0F766E')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: MISTERI LAYAR KOMPUTER YANG GELAP GULITA",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Panik di Lab Komputer", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "MADE:\n\"Gawat, Erik!\nTombol power CPU sudah kupencet,\ntapi layarku tetap hitam pekat!\nApakah komputernya rusak terbakar?!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Siti Memeriksa", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "SITI:\n\"Tunggu Made, jangan ditekan-tekan terus!\nCoba kita cek lampu monitornya...\nLoh, lampunya sama sekali tidak menyala!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Robot Kibo Detektif Kabel", "col": "#2563EB", "bg": "#EFF6FF",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Jangan terburu-buru menangis!\nKomputer butuh aliran listrik dan data.\nMari kita periksa kabel bagian belakang!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Solusi Kabel Longgar", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "ERIK & KIBO:\n\"Aha! Kabel power monitornya copot!\nBegitu dicolokkan... CLING!\nLayar menyala cerah dengan gambar Kibo!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab2_komik_pembuka.png")

def make_bab2_input_output():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(4.25, 4.25, "ANALOGI ALUR SISTEM KOMPUTER: DAPUR RESTORAN KIBO",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A')

    boxes = [
        {"title": "1. PERANGKAT INPUT (MASUKAN)", "subtitle": "Bahan Mentah Masuk", "col": "#0284C7", "bg": "#F0F9FF",
         "items": ["Keyboard (Ketik huruf)", "Mouse (Klik & Arahkan)", "Microphone (Suara)", "Webcam (Kamera)"], "x": 0.3},
        {"title": "2. PEMROSESAN (CPU / OTAK)", "subtitle": "Koki Memasak di Dapur", "col": "#D97706", "bg": "#FFFBEB",
         "items": ["Processor (Otak Cepat)", "RAM (Meja Kerja Dapur)", "Motherboard (Papan Utama)", "Menghitung data biner"], "x": 3.0},
        {"title": "3. PERANGKAT OUTPUT (KELUARAN)", "subtitle": "Makanan Siap Disajikan", "col": "#059669", "bg": "#F0FDF4",
         "items": ["Monitor (Tampilkan visual)", "Speaker (Keluarkan bunyi)", "Printer (Cetak di kertas)", "Proyektor layar lebar"], "x": 5.7},
    ]

    for b in boxes:
        card = patches.FancyBboxPatch((b["x"], 0.6), 2.5, 3.2, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=b["bg"], edgecolor=b["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((b["x"], 3.3), 2.5, 0.5, facecolor=b["col"])
        ax.add_patch(hdr)
        ax.text(b["x"] + 1.25, 3.55, b["title"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(b["x"] + 1.25, 3.05, f"({b['subtitle']})", ha='center', va='center', fontsize=7.5, fontstyle='italic', color=b["col"])
        
        y_txt = 2.6
        for item in b["items"]:
            ax.text(b["x"] + 0.2, y_txt, f"• {item}", ha='left', va='center', fontsize=7.5, color='#1E293B')
            y_txt -= 0.5

    # Arrows connecting boxes
    ax.annotate('', xy=(2.9, 2.2), xytext=(2.6, 2.2),
                arrowprops=dict(facecolor='#64748B', edgecolor='#64748B', width=2, headwidth=6))
    ax.annotate('', xy=(5.6, 2.2), xytext=(5.3, 2.2),
                arrowprops=dict(facecolor='#64748B', edgecolor='#64748B', width=2, headwidth=6))

    # Bottom Storage Box
    stor = patches.FancyBboxPatch((2.2, 0.05), 4.1, 0.45, boxstyle="round,pad=0.04,rounding_size=0.08",
                                  facecolor='#F3E8FF', edgecolor='#9333EA', linewidth=1.5)
    ax.add_patch(stor)
    ax.text(4.25, 0.27, "4. STORAGE (PENYIMPANAN): Harddisk / SSD / Flashdisk (Gudang Lemari Simpan)",
            ha='center', va='center', fontsize=7.5, fontweight='bold', color='#6B21A8')

    save_fig(fig, "bab2_perangkat_input_output.png")

# ==============================================================================
# BAB 3: KEAMANAN DATA PRIBADI & ETIKA DIGITAL
# ==============================================================================

def make_bab3_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#DC2626', edgecolor='#991B1B')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: PERANGKAP PERMEN GAME ONLINE",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Pesan Misterius", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "ERIK:\n\"Hore! Aku dapat pesan WhatsApp!\n'Selamat! Kamu menang 1000 Diamond\ngratis! Klik tautan ini dan masukkan\nnama ibu kandung serta nomor HP!'\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Erik Mau Mengisi", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "ERIK & SITI:\nErik: \"Wah, lumayan buat beli skin robot!\"\nSiti: \"Erik, tunggu! Jangan diklik!\nNama ibu kandung dan nomor HP itu\nrahasia data pribadi berbahaya!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Sirine Bahaya Kibo", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "ROBOT KIBO:\n\"NINO-NINO! SIRINE BAHAYA!\nItu namanya PHISHING alias PANCINGAN!\nPenipu pura-pura memberi hadiah gratis\nuntuk mencuri akun dan uang orang tua!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Pahlawan Siber Bijak", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "ERIK, SITI, MADE:\n\"Segera LAPORKAN dan BLOKIR!\nJangan pernah berikan sandi dan data diri\nkepada orang tak dikenal di internet!\nKita adalah Agen Rahasia Cerdas!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab3_komik_pembuka.png")

def make_bab3_poster():
    fig, ax = plt.subplots(figsize=(8.2, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.2); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(4.1, 4.25, "POSTER 4 JURUS SAKTI: INTERNET SEHAT & STOP CYBERBULLYING",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1E293B')

    rules = [
        {"no": "1", "title": "SARING SEBELUM SHARING", "col": "#0284C7", "bg": "#F0F9FF",
         "desc": "Jangan langsung percaya berita heboh.\nTanyakan pada guru atau orang tua:\nApakah berita ini benar dan bermanfaat?"},
        {"no": "2", "title": "JAGA KATA SANDI KUAT", "col": "#059669", "bg": "#F0FDF4",
         "desc": "Kombinasikan Huruf Besar, Angka & Simbol.\nContoh: Kibo#Hebat2025!\nJangan pakai tanggal lahir atau 123456!"},
        {"no": "3", "title": "SANTUN BERKOMUNIKASI", "col": "#D97706", "bg": "#FFFBEB",
         "desc": "Gunakan kata-kata yang baik di kolom komentar.\nJangan mengejek, menghina, atau menyebarkan\nfoto teman tanpa izin mereka (Stop Bullying!)."},
        {"no": "4", "title": "BERANI LAPOR & BLOKIR", "col": "#DC2626", "bg": "#FEF2F2",
         "desc": "Jika ada pesan kasar, foto aneh, atau ancaman,\nJANGAN TAKUT! Ambil tangkapan layar (screenshot),\nblokir akunnya, dan laporkan ke Guru atau Ortu!"},
    ]

    coords = [(0.4, 2.3), (4.3, 2.3), (0.4, 0.4), (4.3, 0.4)]
    for idx, r in enumerate(rules):
        x, y = coords[idx]
        card = patches.FancyBboxPatch((x, y), 3.5, 1.7, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=r["bg"], edgecolor=r["col"], linewidth=2)
        ax.add_patch(card)
        badge = patches.Circle((x + 0.35, y + 1.35), 0.22, facecolor=r["col"], edgecolor=r["col"])
        ax.add_patch(badge)
        ax.text(x + 0.35, y + 1.35, r["no"], ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF')
        ax.text(x + 1.8, y + 1.35, r["title"], ha='center', va='center', fontsize=8, fontweight='bold', color=r["col"])
        ax.text(x + 1.75, y + 0.65, r["desc"], ha='center', va='center', fontsize=7.2, color='#1E293B', multialignment='center')

    save_fig(fig, "bab3_poster_anti_cyberbullying.png")

# ==============================================================================
# BAB 4: MENGENAL KECERDASAN ARTIFISIAL (AI)
# ==============================================================================

def make_bab4_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#4F46E5', edgecolor='#3730A3')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: APAKAH ROBOT KIBO PUNYA PERASAAN?",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Erik Penasaran", "col": "#4F46E5", "bg": "#EEF2FF",
         "dialog": "ERIK:\n\"Kibo, kamu bisa menjawab semua teka-teki,\nbahkan tahu nama ibukota seluruh dunia.\nApakah kamu juga bisa merasa lapar, sedih,\natau sayang kepada kami?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Jawaban Jujur Kibo", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "ROBOT KIBO:\n\"Tii-tut! Aku adalah KECERDASAN ARTIFISIAL!\nArtifisial artinya BUATAN MANUSIA.\nAku tidak punya hati, darah, atau perasaan.\nAku hanya membaca jutaan baris data!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Made Menimpali", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "MADE:\n\"Berarti kalau Kibo dibilang jelek,\nKibo tidak akan menangis tersedu-sedu?\"\nKibo: \"Tentu tidak, Made! Hatiku adalah sirkuit kabel,\nbukan sel saraf rasa seperti manusia!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Sahabat Penolong Manusia", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "SITI & KIBO:\nSiti: \"Manusia punya hati nurani, kasih sayang,\ndan empati. AI bertugas sebagai asisten pembantu!\"\nKibo: \"Benar! Manusia tetaplah kapten kemudi,\ndan AI adalah teleskop hebatnya!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab4_komik_pembuka.png")

def make_bab4_ai_indonesia():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(4.25, 4.25, "KECERDASAN ARTIFISIAL PENOLONG NEGERI: PENERAPAN DI INDONESIA",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#0F172A')

    cards = [
        {"title": "1. PERTANIAN PADI PINTAR", "col": "#059669", "bg": "#F0FDF4", "x": 0.3,
         "desc": "Petani memotret daun padi dengan HP.\nAI menganalisis warna bintik daun dan\nmemberitahu: 'Padi ini diserang hama wereng!\nGunakan pupuk organik ramah lingkungan!'"},
        {"title": "2. PENERJEMAH BAHASA DAERAH", "col": "#0284C7", "bg": "#F0F9FF", "x": 3.0,
         "desc": "Indonesia punya lebih dari 700 bahasa daerah!\nAI membantu menerjemahkan Bahasa Jawa, Sunda,\nBali, hingga Papua ke Bahasa Indonesia\nagar warisan budaya bangsa tetap lestari."},
        {"title": "3. PENGAWAS KELAUTAN NUSANTARA", "col": "#7C3AED", "bg": "#F5F3FF", "x": 5.7,
         "desc": "Kamera drone dan satelit maritim membaca pola\npergerakan kapal asing tanpa izin.\nAI membantu nelayan menemukan zona ikan melimpah\ntanpa merusak terumbu karang laut kita!"},
    ]

    for c in cards:
        card = patches.FancyBboxPatch((c["x"], 0.6), 2.5, 3.2, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=c["bg"], edgecolor=c["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((c["x"], 3.3), 2.5, 0.5, facecolor=c["col"])
        ax.add_patch(hdr)
        ax.text(c["x"] + 1.25, 3.55, c["title"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(c["x"] + 1.25, 2.0, c["desc"], ha='center', va='center', fontsize=7.5, color='#1E293B', multialignment='center')

    save_fig(fig, "bab4_ai_di_indonesia.png")

# ==============================================================================
# BAB 5: EKSPERIMEN KLASIFIKASI DATA & TEACHABLE MACHINE
# ==============================================================================

def make_bab5_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#0284C7', edgecolor='#0369A1')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: MENGAJARI KIBO MEMILAH SAMPAH SEKOLAH",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Tong Sampah Tercampur", "col": "#EF4444", "bg": "#FEF2F2",
         "dialog": "SITI:\n\"Teman-teman, lihat tong sampah daur ulang ini!\nBotol plastik bercampur dengan kulit pisang!\nPadahal sudah ada tulisan Organik & Anorganik!\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Ide Brilian Made", "col": "#D97706", "bg": "#FFFBEB",
         "dialog": "MADE:\n\"Bagaimana kalau kita pasang webcam dan sensor?\nSetiap ada yang mau buang sampah,\nkamera akan melihat sampahnya dan membuka\ntong yang benar secara otomatis!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Melatih Otak AI", "col": "#2563EB", "bg": "#EFF6FF",
         "dialog": "ROBOT KIBO:\n\"Ide jenius! Tapi komputer belum tahu\nbagaimana bentuk botol plastik dan daun kering!\nKita harus 'menyuapi' komputer dengan banyak contoh foto!\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Teachable Machine Berhasil!", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "ERIK & TIM:\n\"Kita rekam 30 foto botol plastik dan 30 foto daun!\nKlik tombol 'Train Model' di Teachable Machine...\nKeren! Skor akurasinya 100%! Tong sampah otomatis siap!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab5_komik_pembuka.png")

def make_bab5_tutorial():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(4.25, 4.25, "4 LANGKAH PRAKTIKUM: MELATIH MODEL AI GOOGLE TEACHABLE MACHINE",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')

    steps = [
        {"step": "LANGKAH 1", "title": "BUAT KELAS LABEL", "col": "#0284C7", "bg": "#F0F9FF", "x": 0.3,
         "desc": "Buka teachablemachine.withgoogle.com\nPilih 'Image Project' -> 'Standard Model'.\nBeri nama label: 'Kelas 1: Botol Plastik'\ndan 'Kelas 2: Daun Kering'."},
        {"step": "LANGKAH 2", "title": "REKAM DATA FOTO", "col": "#D97706", "bg": "#FFFBEB", "x": 2.35,
         "desc": "Nyalakan Webcam.\nPencet tombol tahan 'Hold to Record'.\nAmbil 30-50 foto dari berbagai sudut:\ndekat, jauh, miring, tegak."},
        {"step": "LANGKAH 3", "title": "TRAIN MODEL", "col": "#7C3AED", "bg": "#F5F3FF", "x": 4.4,
         "desc": "Klik tombol 'Train Model'.\nJANGAN tutup tab browser saat melatih!\nKomputer sedang menghitung pola piksel dan\nmembangun jaringan saraf buatan."},
        {"step": "LANGKAH 4", "title": "PREVIEW & UJI", "col": "#059669", "bg": "#F0FDF4", "x": 6.45,
         "desc": "Sorot benda baru di depan webcam!\nLihat grafik batang persentase (Confidence Score):\n'Botol Plastik: 98%!'\nModel AI kamu berhasil cerdas!"},
    ]

    for s in steps:
        card = patches.FancyBboxPatch((s["x"], 0.6), 1.75, 3.2, boxstyle="round,pad=0.04,rounding_size=0.1",
                                      facecolor=s["bg"], edgecolor=s["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((s["x"], 3.3), 1.75, 0.5, facecolor=s["col"])
        ax.add_patch(hdr)
        ax.text(s["x"] + 0.875, 3.55, s["step"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
        ax.text(s["x"] + 0.875, 3.05, s["title"], ha='center', va='center', fontsize=7, fontweight='bold', color=s["col"])
        ax.text(s["x"] + 0.875, 1.8, s["desc"], ha='center', va='center', fontsize=6.8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab5_panduan_teachable_machine.png")

# ==============================================================================
# BAB 6: BERKREASI DENGAN KODING BLOK VISUAL SCRATCH
# ==============================================================================

def make_bab6_komik():
    fig, ax = plt.subplots(figsize=(8.5, 5.0), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 5.0); ax.axis('off')

    banner = patches.FancyBboxPatch((0.3, 4.45), 7.9, 0.45, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    facecolor='#EA580C', edgecolor='#C2410C')
    ax.add_patch(banner)
    ax.text(4.25, 4.67, "KOMIK SAHABAT KODER: KUCING SCRATCH PENYELAMAT TERUMBU KARANG",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#FFFFFF')

    panels = [
        {"num": "PANEL 1", "title": "Ide Game Nusantara", "col": "#EA580C", "bg": "#FFF7ED",
         "dialog": "MADE:\n\"Erik, Siti! Aku punya ide hebat untuk\npameran karya akhir semester kita!\nBagaimana kalau kita membuat game bertema\n'Petualangan Menyelamatkan Laut Raja Ampat'?\"", "x": 0.3, "y": 2.45},
        {"num": "PANEL 2", "title": "Merancang Tokoh Sprite", "col": "#0284C7", "bg": "#F0F9FF",
         "dialog": "SITI:\n\"Aku akan menggambar Sprite Ikan Badut yang lincah,\nSprite Penyu Laut, dan rintangan botol plastik!\nKita gunakan panggung latar bawah air yang indah!\"", "x": 4.4, "y": 2.45},
        {"num": "PANEL 3", "title": "Merakit Blok Mantra", "col": "#7C3AED", "bg": "#F5F3FF",
         "dialog": "ERIK & KIBO:\n\"Erik: 'Bagaimana membuat ikannya berenang ke kanan?'\nKibo: 'Pasang blok [when key right arrow pressed],\nlalu sambungkan balok [change x by 10]! Klik-klik!'\"", "x": 0.3, "y": 0.35},
        {"num": "PANEL 4", "title": "Showcase Day Meriah", "col": "#059669", "bg": "#F0FDF4",
         "dialog": "SEMUA SAHABAT KODER:\n\"BENDERAH HIJAU DIKLIK! GAME BERJALAN!\nTeman-teman sekelas dan orang tua kita tersenyum kagum!\nKita bukan cuma bermain game, kita PENCIPTA GAME!\"", "x": 4.4, "y": 0.35},
    ]

    for p in panels:
        card = patches.FancyBboxPatch((p["x"], p["y"]), 3.8, 1.9, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=p["bg"], edgecolor=p["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((p["x"], p["y"] + 1.5), 3.8, 0.4, facecolor=p["col"])
        ax.add_patch(hdr)
        ax.text(p["x"] + 1.9, p["y"] + 1.7, f"{p['num']}: {p['title']}", ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#FFFFFF')
        ax.text(p["x"] + 1.9, p["y"] + 0.75, p["dialog"], ha='center', va='center',
                fontsize=8, color='#1E293B', multialignment='center')

    save_fig(fig, "bab6_komik_pembuka.png")

def make_bab6_kartu_blok():
    fig, ax = plt.subplots(figsize=(8.5, 4.6), facecolor='#F8FAFC')
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 4.6); ax.axis('off')

    ax.text(4.25, 4.25, "KARTU MANTRA KODING BLOK VISUAL SCRATCH 3.0",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#0F172A')

    blocks = [
        {"cat": "GERAKAN (MOTION)", "col": "#2563EB", "bg": "#EFF6FF", "x": 0.3,
         "blocks": ["[move 10 steps]", "[turn right 15 degrees]", "[go to x: 0 y: 0]", "[point in direction 90]"],
         "fungsi": "Menggerakkan tokoh sprite maju, mundur, memutar, atau meluncur ke koordinat layar."},
        {"cat": "TAMPILAN (LOOKS)", "col": "#9333EA", "bg": "#FAF5FF", "x": 3.0,
         "blocks": ["[say 'Halo!' for 2 secs]", "[switch costume to kostum2]", "[next costume]", "[change size by 10]"],
         "fungsi": "Mengubah ekspresi, kostum animasi langkah kaki, ukuran tokoh, dan gelembung ucapan."},
        {"cat": "KONTROL & KEJADIAN", "col": "#D97706", "bg": "#FFFBEB", "x": 5.7,
         "blocks": ["[when green flag clicked]", "[forever ...]", "[repeat 10 ...]", "[if <touching plastic?> then]"],
         "fungsi": "Pemicu bendera hijau mulainya game, jurus pengulangan (loop), dan pengambilan keputusan logika."},
    ]

    for b in blocks:
        card = patches.FancyBboxPatch((b["x"], 0.6), 2.5, 3.2, boxstyle="round,pad=0.06,rounding_size=0.12",
                                      facecolor=b["bg"], edgecolor=b["col"], linewidth=2)
        ax.add_patch(card)
        hdr = patches.Rectangle((b["x"], 3.3), 2.5, 0.5, facecolor=b["col"])
        ax.add_patch(hdr)
        ax.text(b["x"] + 1.25, 3.55, b["cat"], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
        
        y_pos = 2.9
        for blk in b["blocks"]:
            b_box = patches.FancyBboxPatch((b["x"] + 0.15, y_pos - 0.15), 2.2, 0.35, boxstyle="round,pad=0.02,rounding_size=0.06",
                                           facecolor='#FFFFFF', edgecolor=b["col"], linewidth=1.2)
            ax.add_patch(b_box)
            ax.text(b["x"] + 1.25, y_pos, blk, ha='center', va='center', fontsize=6.8, fontweight='bold', color=b["col"])
            y_pos -= 0.45

        ax.text(b["x"] + 1.25, 0.95, b["fungsi"], ha='center', va='center', fontsize=7, color='#334155', multialignment='center')

    save_fig(fig, "bab6_kartu_koding_scratch.png")

if __name__ == '__main__':
    print("Generating High-Resolution Vibrant Assets for Bab 2 to Bab 6...")
    make_bab2_komik()
    make_bab2_input_output()
    make_bab3_komik()
    make_bab3_poster()
    make_bab4_komik()
    make_bab4_ai_indonesia()
    make_bab5_komik()
    make_bab5_tutorial()
    make_bab6_komik()
    make_bab6_kartu_blok()
    print("All 10 Assets Generated Successfully!")
