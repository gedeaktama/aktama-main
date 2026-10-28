# -*- coding: utf-8 -*-
"""
Professional Publishing Compiler for Buku Siswa & Buku Guru SD Kelas 5
Standard: Permendikdasmen No. 13 Tahun 2025, Pusbuk BSKAP, UNESCO B5 Format
Features: High-Res Embedded Illustrations, Callout Boxes, Authentic Rubrics, Dynamic Layout
"""
import os, sys, shutil, docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

import sd5_data
import guru_data_part1
import guru_bab_1_2_3
import guru_bab_4_5_6

tot_dir = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD"
local_dir = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd"
assets_tot = os.path.join(tot_dir, "assets")
assets_local = os.path.join(local_dir, "assets")

os.makedirs(assets_tot, exist_ok=True)
os.makedirs(assets_local, exist_ok=True)

cover_img = os.path.join(assets_local, "cover_buku_siswa_sd5.jpg")

# -------------------------------------------------------------
# 1. Update Front Matter with Daftar Gambar & Daftar Tabel
# -------------------------------------------------------------
FRONT_MATTER_UPDATED = """# KODING DAN KECERDASAN ARTIFISIAL
## BUKU TEKS PELAJARAN SISWA SD/MI KELAS V
### Mata Pelajaran Pilihan — Fase C

**Penulis:**  
Gede Erik Aktama, M.Kom  
*(Fasilitator Nasional Koding dan Kecerdasan Artifisial Kemendikdasmen RI)*  

**Penelaah & Konsultan Ahli:**  
Tim Pengembang Kurikulum KKA Direktorat Guru Pendidikan Dasar Kemendikdasmen RI  

**Penerbit:**  
Pusat Perbukuan  
Badan Standar, Kurikulum, dan Asesmen Pendidikan  
Kementerian Pendidikan Dasar dan Menengah Republik Indonesia  
Tahun 2025 / 2026  

---

## IDENTITAS PENERBITAN & HAK CIPTA
* **Judul Buku:** Koding dan Kecerdasan Artifisial untuk SD/MI Kelas V (Fase C)
* **Penulis:** Gede Erik Aktama, M.Kom
* **Penyunting / Editor Naskah:** Tim Fasilitator Bimtek KKA Kemendikdasmen
* **Tata Letak & Tipografi:** Format Standar Buku Ajar UNESCO (15,5 cm x 23,0 cm)
* **Desain Sampul & Ilustrasi:** Tim Desain Edukatif Digital Aktama
* **Penerbit:** Pusat Perbukuan Kemendikdasmen RI
* **Hak Cipta Dilindungi Undang-Undang:** Diterbitkan dan disesuaikan berdasarkan Permendikdasmen Nomor 13 Tahun 2025 tentang Kurikulum Sekolah Dasar dan Menengah.

---

## KATA PENGANTAR KEMENDIKDASMEN
Puji dan syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa. Perkembangan teknologi digital dan kecerdasan artifisial telah melaju sedemikian pesat, menyentuh hampir setiap segi kehidupan manusia. Menjawab tantangan tersebut, Kementerian Pendidikan Dasar dan Menengah resmi menghadirkan mata pelajaran pilihan **Koding dan Kecerdasan Artifisial (KKA)** mulai jenjang Sekolah Dasar pada Fase C (Kelas V dan VI).

Buku Teks Pelajaran ini disusun dengan pendekatan **Pembelajaran Mendalam (*Deep Learning*)** yang berkesadaran (*mindful*), bermakna (*meaningful*), dan menggembirakan (*joyful*). Melalui buku ini, anak-anak Indonesia diajak bukan sekadar menjadi konsumen pasif teknologi, melainkan menjadi penemu dan pencipta muda yang bernalar kritis, kreatif, serta berakhlak mulia.

Apresiasi tinggi kami sampaikan kepada Saudara **Gede Erik Aktama, M.Kom** atas dedikasi dan karyanya dalam menyusun buku teks yang kaya ilustrasi visual, aplikatif, dan kontekstual ini. Selamat bertualang menjelajahi dunia koding!

Jakarta, 2025  
**Kementerian Pendidikan Dasar dan Menengah Republik Indonesia**

---

## PRAKATA PENULIS
Halo, sahabat koder cilik Indonesia yang hebat!

Selamat datang di kelas 5 SD dan selamat memulai petualangan baru yang sangat seru dalam mata pelajaran **Koding dan Kecerdasan Artifisial (KKA)**! Apakah kalian pernah membayangkan bagaimana sebuah robot bisa membedakan sampah plastik dengan daun kering? Atau bagaimana karakter kartun di komputer bisa melompat saat tombol spasi ditekan?

Di buku ini, kalian tidak perlu takut merasa kesulitan. Belajar koding itu seperti bermain puzzle dan menyusun balok lego warna-warni! Bersama sahabat belajar kita: **Erik**, **Siti**, **Made**, dan **Robot Kibo**, kalian akan diajak:
1. Memecahkan teka-teki logika yang mengasyikkan lewat 4 jurus pahlawan berpikir komputasional.
2. Membongkar rahasia cara kerja komputer dan menjaga kesehatan mata dengan senam 20-20-20.
3. Menjadi detektif siber yang melindungi kata sandi rahasia dari jeratan penipuan online.
4. Melatih kecerdasan artifisial mengenali foto benda menggunakan Google Teachable Machine.
5. Merancang game dan animasi penyelamat bumi buatanmu sendiri di Scratch!

Ingatlah selalu pesan Robot Kibo: *"Jangan pernah takut salah saat mencoba! Kesalahan koding (bug) adalah teman belajar terbaik yang membuat otak kita makin cerdas."* Selamat berkreasi dan jadilah kebanggaan nusa dan bangsa!

Denpasar, 2025  
**Gede Erik Aktama, M.Kom**  
*(Fasilitator Nasional KKA Kemendikdasmen)*

---

## DAFTAR ISI
* **Halaman Judul & Hak Cipta**
* **Kata Pengantar Kemendikdasmen**
* **Prakata Penulis**
* **Daftar Isi, Daftar Gambar, dan Daftar Tabel**
* **Petunjuk Penggunaan Fitur Buku**
* **Mengenal Tokoh Sahabat Belajar**
* **Peta Konsep Pembelajaran Tahunan**
* **SEMESTER 1**
  * **BAB 1: Berpikir Komputasional dan Pemecahan Masalah (16 JP)**
    * 1.1 Mengenal 4 Pilar Berpikir Komputasional
    * 1.2 Menerapkan Dekomposisi dan Pengenalan Pola
    * 1.3 Menyusun Algoritma dan Membaca Bagan Alir (*Flowchart*)
    * 1.4 Melacak dan Memperbaiki Kesalahan Logika (*Debugging*)
    * Rangkuman, Evaluasi HOTS Bab 1, dan Jurnal Refleksiku
  * **BAB 2: Mengenal Teknologi Digital dan Perangkat Komputer (12 JP)**
    * 2.1 Manfaat dan Dampak Teknologi dalam Kehidupan Sehari-hari
    * 2.2 Arsitektur Sistem Komputer: Perangkat Keras, Lunak, dan Manusia
    * 2.3 Praktik Sikap Tubuh Sehat (*Ergonomi*) dan Senam Mata 20-20-20
    * 2.4 Berkreasi Membuat Gambar Digital Sederhana di Komputer
    * Rangkuman, Evaluasi HOTS Bab 2, dan Jurnal Refleksiku
  * **BAB 3: Menjaga Rahasia dan Keamanan Data Pribadi (8 JP)**
    * 3.1 Membedakan Informasi Publik dan Informasi Pribadi Rahasia
    * 3.2 Merancang Kata Sandi (*Password*) yang Kuat dan Unik
    * 3.3 Waspada Penipuan Digital (*Phishing*) dan Rahasia Kode OTP
    * 3.4 Etika Santun Bermedia Sosial dan Gerakan Lawan Perundungan Siber
    * Rangkuman, Evaluasi HOTS Bab 3, dan Proyek Mini Semester 1
* **SEMESTER 2**
  * **BAB 4: Mengenal Kecerdasan Artifisial (12 JP)**
    * 4.1 Apa Itu Kecerdasan Artifisial (AI)?
    * 4.2 Membedakan Mesin Otomatis Biasa dengan Sistem AI Cerdas
    * 4.3 Bagaimana AI Melihat dan Mendengar: Sensor Pintar Gawai
    * 4.4 Pemanfaatan AI untuk Pertanian, Kesehatan, dan Alam Indonesia
    * 4.5 Nilai Mulia Manusia (*Human-Centered AI*): Hati Nurani dan Empati
    * Rangkuman, Evaluasi HOTS Bab 4, dan Jurnal Refleksiku
  * **BAB 5: Eksperimen Klasifikasi Data Bersama AI (12 JP)**
    * 5.1 Mengenal Data, Label Kategori, dan Fitur Pembeda
    * 5.2 Mengenal Laboratorium Digital Google Teachable Machine
    * 5.3 Langkah Eksperimen: Kumpul Data, Latih Model, dan Uji Prediksi
    * 5.4 Membaca Tingkat Keyakinan (*Confidence Score*)
    * 5.5 Memahami Bahaya Bias Data dan Cara Menyeimbangkannya
    * Rangkuman, Evaluasi HOTS Bab 5, dan Jurnal Refleksiku
  * **BAB 6: Berkreasi dengan Koding Blok Visual & Gelar Karya (12 JP)**
    * 6.1 Mengenal Studio Koding Visual Scratch
    * 6.2 Karakter Sprite, Panggung (*Stage*), dan Latar Belakang
    * 6.3 Menyusun Blok Peristiwa (*Events*), Gerakan, dan Perulangan (*Loop*)
    * 6.4 Merancang Storyboard Naskah Game Edukasi Penyelamat Bumi
    * 6.5 Gelar Karya Siswa (*Showcase Day*): Pameran Karya Koding di Kelas
    * Rangkuman, Uji Pemahaman Akhir Tahun, dan Capstone Project
* **BAGIAN AKHIR BUKU**
  * Evaluasi Komprehensif Sumatif Akhir Tahun (Pilihan Ganda & Uraian)
  * Glosarium Istilah Komputasi & Kecerdasan Artifisial
  * Kunci Jawaban Soal Pilihan Ganda Terpilih
  * Daftar Pustaka Standar Rujukan
  * Indeks Kata
  * Profil Penulis dan Fasilitator Nasional ToT

---

## DAFTAR GAMBAR
* **Gambar 0.1:** Tokoh Sahabat Belajar Koding dan Kecerdasan Artifisial Kelas 5
* **Gambar 1.1:** Empat Pilar Berpikir Komputasional (*Computational Thinking*)
* **Gambar 1.2:** Contoh Bagan Alir (*Flowchart*): Algoritma Mencuci Tangan 6 Langkah
* **Gambar 1.3:** Peta Labirin Algoritma Rute Robot Kibo (Grid 5x5)
* **Gambar 2.1:** Arsitektur Lengkap Sistem Komputer: Tritunggal Hardware, Software, Brainware
* **Gambar 2.2:** Panduan Kesehatan Digital: Posisi Duduk Ergonomis dan Senam Mata 20-20-20
* **Gambar 3.1:** Perisai Keamanan Data Pribadi dan Rumus Kata Sandi Kuat
* **Gambar 4.1:** Sensor Perangkat Gawai Meniru Pancaindra Manusia
* **Gambar 5.1:** Alur Kerja Eksperimen AI pada Google Teachable Machine
* **Gambar 6.1:** Peta Antarmuka Studio Koding Blok Visual Scratch

---

## DAFTAR TABEL
* **Tabel 1.1:** Pemetaan Alur Tujuan Pembelajaran (ATP) dan Alokasi JP Kelas 5
* **Tabel 1.2:** Skema Dekomposisi Tugas Pembersihan Kelas
* **Tabel 1.3:** Rubrik Penilaian Kinerja Labirin Algoritma Sampah
* **Tabel 2.1:** Klasifikasi Perangkat Keras Input, Output, dan Penyimpanan
* **Tabel 2.2:** Lembar Observasi Sikap Duduk Ergonomis di Lab Komputer
* **Tabel 3.1:** Lembar Klasifikasi Data: Boleh Dibagikan vs Wajib Dirahasiakan
* **Tabel 5.1:** Tabel Pencatatan Data Uji Akurasi dan Confidence Score AI
* **Tabel 6.1:** Rubrik Penilaian Proyek Capstone Game Penyelamat Lingkungan

---

## PETUNJUK PENGGUNAAN FITUR BUKU
Agar belajar koding semakin terarah dan menyenangkan, kenali ikon-ikon petualangan berikut:

* 💡 **Ayo Menyimak:** Cerita pembuka yang seru dan dekat dengan keseharian anak untuk memantik rasa ingin tahu.
* 🔍 **Tahukah Kamu?:** Kotak wawasan sains dan teknologi terkini untuk memperluas cakrawala berpikir.
* 🛠️ **Ayo Mencoba:** Aktivitas langsung di kelas, baik permainan tanpa komputer (*Unplugged*) maupun praktik laptop (*Plugged*).
* 🛡️ **Pojok Karakter & Etika:** Petuah budi pekerti luhur agar menjadi anak yang santun dan bijak di dunia nyata maupun dunia maya.
* 📝 **Rangkuman Bab:** Ringkasan inti materi yang wajib kalian ingat di setiap akhir pelajaran.
* 🎯 **Uji Pemahaman HOTS:** Latihan soal logika (Pilihan Ganda & Uraian) untuk menguji ketajaman berpikirmu.
* 💖 **Jurnal Refleksiku:** Ruang mencatat perasaan hatimu dan hal-hal baru yang berhasil kamu pelajari.

---

## MENGENAL TOKOH SAHABAT BELAJAR

[[IMAGE: gambar_tokoh_sahabat.png | Gambar 0.1: Empat Sahabat Belajar Koding dan Kecerdasan Artifisial Kelas 5]]

Di sepanjang buku ini, kalian akan ditemani oleh empat sahabat hebat:
1. **Erik:** Teman kita yang berambut ikal pendek, selalu penuh semangat, suka bertanya, dan gemar membongkar-pasang balok mainan untuk mencari tahu cara kerjanya.
2. **Siti:** Teman kita yang berkerudung hijau teduh, sangat teliti, gemar merawat tanaman bunga di taman sekolah, dan senang menggambar lukisan digital.
3. **Made:** Teman kita yang mengenakan udeng khas Bali, lincah bergerak, penari tari daerah yang luwes, serta selalu punya ide-ide unik dan kreatif.
4. **Robot Kibo:** Robot asisten cerdas berwarna biru-oranye dengan wajah layar ramah. Robot Kibo setia memandu kita memecahkan kode rahasia dan melatih model AI.

---

## PETA KONSEP PEMBELAJARAN TAHUNAN KELAS 5 (FASE C)

```
                            PETUALANGAN KODING & KA KELAS V
                                          │
            ┌─────────────────────────────┴─────────────────────────────┐
            ▼                                                           ▼
       SEMESTER 1                                                  SEMESTER 2
┌───────────────────────────────┐           ┌───────────────────────────────┐
│ BAB 1: Berpikir Komputasional │           │ BAB 4: Mengenal Kecerdasan    │
│        dan Pemecahan Masalah  │           │        Artifisial (AI)        │
├───────────────────────────────┤           ├───────────────────────────────┤
│ BAB 2: Mengenal Teknologi     │           │ BAB 5: Eksperimen Klasifikasi │
│        Digital & Komputer     │           │        Data Bersama AI        │
├───────────────────────────────┤           ├───────────────────────────────┤
│ BAB 3: Menjaga Rahasia &      │           │ BAB 6: Berkreasi dengan Koding│
│        Keamanan Data Pribadi  │           │        Blok Visual Scratch    │
└───────────────────────────────┘           │        & Gelar Karya Siswa    │
                                            └───────────────────────────────┘
```
"""

# -------------------------------------------------------------
# 2. Inject Image Tags into Chapter Texts
# -------------------------------------------------------------
BAB_1_PRO = sd5_data.BAB_1.replace(
    "### A. MENGENAL 4 PILAR BERPIKIR KOMPUTASIONAL",
    "### A. MENGENAL 4 PILAR BERPIKIR KOMPUTASIONAL\n\n[[IMAGE: gambar_1_1_pilar_bk.png | Gambar 1.1: Empat Pilar Berpikir Komputasional (Computational Thinking)]]\n"
).replace(
    "### C. MENYUSUN ALGORITMA DAN MEMBUAT BAGAN ALIR (FLOWCHART)",
    "### C. MENYUSUN ALGORITMA DAN MEMBUAT BAGAN ALIR (FLOWCHART)\n\n[[IMAGE: gambar_1_2_flowchart_algoritma.png | Gambar 1.2: Contoh Bagan Alir (Flowchart) Algoritma Mencuci Tangan 6 Langkah]]\n"
).replace(
    "* **Judul Proyek:** \"Merancang Peta Labirin Algoritma Sampah\"",
    "* **Judul Proyek:** \"Merancang Peta Labirin Algoritma Sampah\"\n\n[[IMAGE: gambar_1_3_labirin_unplugged.png | Gambar 1.3: Peta Labirin Algoritma Rute Robot Kibo (Grid 5x5)]]\n"
)

BAB_2_PRO = sd5_data.BAB_2.replace(
    "### B. MENGENAL PERANGKAT KERAS KOMPUTER (HARDWARE)",
    "### B. MENGENAL PERANGKAT KERAS KOMPUTER (HARDWARE)\n\n[[IMAGE: gambar_2_1_anatomi_komputer.png | Gambar 2.1: Arsitektur Lengkap Sistem Komputer: Hardware, Software, Brainware]]\n"
).replace(
    "### D. MENJAGA KESEHATAN TUBUH SAAT MENGGUNAKAN KOMPUTER (ERGONOMI)",
    "### D. MENJAGA KESEHATAN TUBUH SAAT MENGGUNAKAN KOMPUTER (ERGONOMI)\n\n[[IMAGE: gambar_2_2_ergonomi_duduk.png | Gambar 2.2: Panduan Posisi Duduk Ergonomis dan Senam Mata Aturan 20-20-20]]\n"
)

BAB_3_PRO = sd5_data.BAB_3.replace(
    "### A. INFORMASI PRIBADI VS INFORMASI PUBLIK",
    "### A. INFORMASI PRIBADI VS INFORMASI PUBLIK\n\n[[IMAGE: gambar_3_1_perisai_keamanan_data.png | Gambar 3.1: Perisai Keamanan Data Pribadi dan Rumus Kata Sandi Kuat]]\n"
)

BAB_4_PRO = sd5_data.BAB_4.replace(
    "### B. BAGAIMANA CARA AI MELIHAT DAN MENDENGAR? (SENSOR PINTAR)",
    "### B. BAGAIMANA CARA AI MELIHAT DAN MENDENGAR? (SENSOR PINTAR)\n\n[[IMAGE: gambar_4_1_sensor_vs_pancaindra.png | Gambar 4.1: Sensor Perangkat Gawai Meniru Pancaindra Manusia]]\n"
)

BAB_5_PRO = sd5_data.BAB_5.replace(
    "### B. MENGENAL LABORATORIUM DIGITAL: GOOGLE TEACHABLE MACHINE",
    "### B. MENGENAL LABORATORIUM DIGITAL: GOOGLE TEACHABLE MACHINE\n\n[[IMAGE: gambar_5_1_siklus_machine_learning.png | Gambar 5.1: Alur Kerja Eksperimen AI pada Google Teachable Machine]]\n"
)

BAB_6_PRO = sd5_data.BAB_6.replace(
    "### A. MENGENAL RUMAH KREATIF: STUDIO SCRATCH",
    "### A. MENGENAL RUMAH KREATIF: STUDIO SCRATCH\n\n[[IMAGE: gambar_6_1_antarmuka_scratch.png | Gambar 6.1: Peta Antarmuka Studio Koding Blok Visual Scratch]]\n"
)

# -------------------------------------------------------------
# 3. Assemble Full Professional Markdown
# -------------------------------------------------------------
full_pro_md = "\n\n".join([
    FRONT_MATTER_UPDATED,
    BAB_1_PRO,
    BAB_2_PRO,
    BAB_3_PRO,
    BAB_4_PRO,
    BAB_5_PRO,
    BAB_6_PRO
])

for base in [tot_dir, local_dir]:
    with open(os.path.join(base, "Buku_Siswa_Koding_dan_KA_Kelas_5_SD.md"), "w", encoding="utf-8") as f:
        f.write(full_pro_md.strip() + "\n")
print("Professional Markdown Buku Siswa written.")

# -------------------------------------------------------------
# 4. Professional DOCX Builder with Styles, Boxes & Embedded Images
# -------------------------------------------------------------
def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def apply_callout_box(paragraph, bg_hex, border_hex):
    pPr = paragraph._element.get_or_add_pPr()
    pBdr = parse_xml(f'''
        <w:pBdr {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="14" w:color="{border_hex}"/>
        </w:pBdr>
    ''')
    pPr.append(pBdr)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hex}"/>')
    pPr.append(shd)

def build_pro_docx(md_content, output_name, cover_path):
    doc = docx.Document()
    
    # 1. Page Dimension: UNESCO B5 (15.5 cm x 23.0 cm)
    for s in doc.sections:
        s.page_width = Pt(439.45)
        s.page_height = Pt(652.05)
        s.top_margin = Pt(56.7)
        s.bottom_margin = Pt(56.7)
        s.left_margin = Pt(56.7)
        s.right_margin = Pt(56.7)
        
        # Footer
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("Koding & Kecerdasan Artifisial — Kelas 5 SD (Fase C)")
        frun.font.size = Pt(8.5)
        frun.font.name = 'Arial'
        frun.font.color.rgb = RGBColor(100, 116, 139)

    # 2. Add Cover Page
    if cover_path and os.path.exists(cover_path):
        p_cov = doc.add_paragraph()
        p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cov.paragraph_format.space_before = Pt(0)
        p_cov.paragraph_format.space_after = Pt(0)
        run = p_cov.add_run()
        run.add_picture(cover_path, width=Inches(4.9))
        doc.add_page_break()

    lines = md_content.split("\n")
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        rows_data = []
        for r in table_rows:
            parts = [c.strip() for c in r.split("|")[1:-1]]
            if parts and not all(set(c).issubset({'-', ':', ' '}) for c in parts):
                rows_data.append(parts)
        if rows_data:
            num_cols = max(len(r) for r in rows_data)
            tbl = doc.add_table(rows=len(rows_data), cols=num_cols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.style = 'Table Grid'
            for ri, row in enumerate(rows_data):
                for ci, cell_text in enumerate(row):
                    if ci < num_cols:
                        cell = tbl.cell(ri, ci)
                        cell.text = cell_text
                        for p in cell.paragraphs:
                            p.paragraph_format.space_after = Pt(2)
                            p.paragraph_format.space_before = Pt(2)
                            for r in p.runs:
                                r.font.name = 'Arial'
                                r.font.size = Pt(8.5)
                        if ri == 0:
                            set_cell_background(cell, "E0F2FE")
                            for p in cell.paragraphs:
                                for r in p.runs:
                                    r.font.bold = True
                                    r.font.color.rgb = RGBColor(3, 105, 161)
        in_table = False
        table_rows = []

    for line in lines:
        sline = line.strip()
        
        # Handle Table
        if sline.startswith("|") and sline.endswith("|"):
            in_table = True
            table_rows.append(sline)
            continue
        else:
            if in_table:
                flush_table()

        if not sline:
            continue

        # Handle Embedded Image Tag: [[IMAGE: filename.png | Caption text]]
        if sline.startswith("[[IMAGE:") and "]]" in sline:
            tag_content = sline.replace("[[IMAGE:", "").replace("]]", "").strip()
            parts = [p.strip() for p in tag_content.split("|")]
            img_filename = parts[0]
            caption = parts[1] if len(parts) > 1 else ""
            
            # Find image path
            img_full = os.path.join(assets_local, img_filename)
            if not os.path.exists(img_full):
                img_full = os.path.join(assets_tot, img_filename)
                
            if os.path.exists(img_full):
                # Add image paragraph
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(10)
                p_img.paragraph_format.space_after = Pt(4)
                r_img = p_img.add_run()
                r_img.add_picture(img_full, width=Inches(4.6))
                
                # Add caption paragraph
                if caption:
                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(10)
                    r_cap = p_cap.add_run(caption)
                    r_cap.font.name = 'Arial'
                    r_cap.font.size = Pt(8.5)
                    r_cap.font.italic = True
                    r_cap.font.color.rgb = RGBColor(71, 85, 105)
            continue

        # Headings
        if sline.startswith("# "):
            if not sline.startswith("# KODING"):
                doc.add_page_break()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(8)
            run = p.add_run(sline[2:])
            run.font.name = 'Arial'
            run.font.bold = True
            run.font.size = Pt(15)
            run.font.color.rgb = RGBColor(15, 23, 42)
        elif sline.startswith("## "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run(sline[3:])
            run.font.name = 'Arial'
            run.font.bold = True
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(2, 132, 199)
        elif sline.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(sline[4:])
            run.font.name = 'Arial'
            run.font.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(13, 148, 136)
        elif sline.startswith("#### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(sline[5:])
            run.font.name = 'Arial'
            run.font.bold = True
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(71, 85, 105)
        elif sline.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.right_indent = Inches(0.15)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(sline.lstrip("> "))
            run.font.name = 'Arial'
            run.font.size = Pt(9)
            run.font.italic = True
            run.font.color.rgb = RGBColor(30, 41, 59)
            apply_callout_box(p, bg_hex="F0F9FF", border_hex="0284C7")
        elif sline.startswith("* ") or sline.startswith("- "):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(sline[2:])
            run.font.name = 'Arial'
            run.font.size = Pt(9.5)
        elif any(sline.startswith(f"{i}. ") for i in range(1, 40)):
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(sline.split(". ", 1)[1] if ". " in sline else sline)
            run.font.name = 'Arial'
            run.font.size = Pt(9.5)
        elif sline.startswith("```"):
            pass
        elif sline.startswith("---"):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run("―" * 38)
            run.font.name = 'Arial'
            run.font.color.rgb = RGBColor(226, 232, 240)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            run = p.add_run(sline)
            run.font.name = 'Arial'
            run.font.size = Pt(9.5)

    if in_table:
        flush_table()

    for base in [tot_dir, local_dir]:
        out_f = os.path.join(base, output_name)
        doc.save(out_f)
    print(f"Professional DOCX Saved: {output_name}")

build_pro_docx(full_pro_md, "Buku_Siswa_Koding_dan_KA_Kelas_5_SD.docx", cover_img)
print("PROFESSIONAL PUBLISHING BUILD COMPLETED SUCCESSFULLY!")
