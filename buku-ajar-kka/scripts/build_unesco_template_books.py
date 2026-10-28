# -*- coding: utf-8 -*-
"""
Master Builder for Official UNESCO Template Books:
Gold Standard Bab 1 (Rich Visuals, Comic Dialogs, Gamification)
Base: 'TEMPLATE BUKU AJAR UKURAN UNESCO.docx'
"""
import os, sys, re, shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.path.insert(0, r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts")
sys.path.insert(0, r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts")
import guru_data_part1
import guru_bab_1_2_3
import guru_bab_4_5_6
from docx_advanced_parser import add_styled_runs, clean_latex_symbols
from naskah_bab1_gold_standard import BAB_1_GOLD
from naskah_bab2_bab3_gold import BAB_2_GOLD, BAB_3_GOLD
from naskah_bab4_bab5_bab6_gold import BAB_4_GOLD, BAB_5_GOLD, BAB_6_GOLD, BAGIAN_AKHIR_GOLD

template_src = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\template buku\TEMPLATE BUKU AJAR UKURAN UNESCO.docx"
tot_dir = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD"
local_dir = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd"
assets_local = os.path.join(local_dir, "assets")
assets_tot = os.path.join(tot_dir, "assets")

cover_img_path = os.path.join(assets_local, "cover_buku_siswa_sd5.jpg")

DAFTAR_PUSTAKA_RESMI = """### DAFTAR PUSTAKA & RUJUKAN STANDAR RESMI

1. Badan Standar, Kurikulum, dan Asesmen Pendidikan. (2024). *Keputusan Kepala BSKAP Kemendikbudristek Nomor 032/H/KR/2024 tentang Capaian Pembelajaran pada Pendidikan Anak Usia Dini, Jenjang Pendidikan Dasar, dan Jenjang Pendidikan Menengah pada Kurikulum Merdeka*. Jakarta: Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.
2. Bers, M. U. (2020). *Coding as a Playground: Programming and Computational Thinking in the Early Childhood Classroom (2nd ed.)*. New York: Routledge. ISBN: 978-0367366766.
3. Brennan, K., & Resnick, M. (2012). *New frameworks for studying and assessing the development of computational thinking*. In Proceedings of the 2012 Annual Meeting of the American Educational Research Association (AERA), Vancouver, Canada.
4. Direktorat Jenderal Guru dan Tenaga Kependidikan. (2025). *Pedoman Bimbingan Teknis Fasilitator Koding dan Kecerdasan Artifisial Sekolah Dasar*. Jakarta: Kementerian Pendidikan Dasar dan Menengah RI.
5. Grover, S., & Pea, R. (2013). *Computational Thinking in K-12: A Review of the State of the Field*. *Educational Researcher*, 42(1), 38-43. https://doi.org/10.3102/0013189X12463051
6. International Society for Technology in Education (ISTE), & Computer Science Teachers Association (CSTA). (2011). *Computational Thinking Teacher Resources (2nd ed.)*. Washington, DC: ISTE.
7. Kementerian Pendidikan Dasar dan Menengah RI. (2025). *Peraturan Menteri Pendidikan Dasar dan Menengah Nomor 13 Tahun 2025 tentang Perubahan atas Permendikbudristek Nomor 12 Tahun 2024 tentang Kurikulum pada Pendidikan Anak Usia Dini, Jenjang Pendidikan Dasar, dan Jenjang Pendidikan Menengah*. Jakarta: Kemendikdasmen.
8. Papert, S. (1980). *Mindstorms: Children, Computers, and Powerful Ideas*. New York: Basic Books. ISBN: 978-0465046744.
9. Pusat Kurikulum dan Pembelajaran BSKAP. (2024). *Panduan Pembelajaran dan Asesmen Pendidikan Anak Usia Dini, Pendidikan Dasar, dan Menengah*. Jakarta: Kemendikbudristek.
10. Pusat Perbukuan BSKAP. (2022). *Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 22 Tahun 2022 tentang Standar Mutu Buku, Standar Proses dan Kaidah Pemerolehan Naskah, serta Standar Proses dan Kaidah Penerbitan Buku Pendidikan*. Jakarta: Kemendikbudristek.
11. Resnick, M. (2017). *Lifelong Kindergarten: Cultivating Creativity through Projects, Passion, Peers, and Play*. Cambridge, MA: The MIT Press. ISBN: 978-0262037298.
12. Touretzky, D., Gardner-McCune, C., Martin, F., & Seehorn, D. (2019). *Envisioning AI for K-12: What Should Every Child Know about AI?*. *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(01), 9795-9799. https://doi.org/10.1609/aaai.v33i01.33019795
13. UNESCO. (2022). *K-12 AI curricula: A mapping of government-endorsed AI curricula*. Paris: United Nations Educational, Scientific and Cultural Organization. ISBN: 978-92-3-100514-5.
14. Wing, J. M. (2006). *Computational Thinking*. *Communications of the ACM*, 49(3), 33-35. https://doi.org/10.1145/1118178.1118215"""

def replace_biblio(text):
    if "### DAFTAR PUSTAKA" in text:
        parts = text.split("### DAFTAR PUSTAKA")
        before = parts[0]
        after = ""
        if "### INDEKS KATA" in parts[1]:
            after = "### INDEKS KATA" + parts[1].split("### INDEKS KATA")[1]
        elif "### G. Profil Penulis" in parts[1]:
            after = "### G. Profil Penulis" + parts[1].split("### G. Profil Penulis")[1]
        return before + DAFTAR_PUSTAKA_RESMI + "\n\n---\n\n" + after
    return text

FRONT_MATTER_GOLD = """# KODING DAN KECERDASAN ARTIFISIAL
## BUKU TEKS PELAJARAN SISWA SD/MI KELAS V
### Mata Pelajaran Pilihan — Fase C

**Penulis:**  
Gede Erik Aktama, S.Pd., M.Pd.  
*(Fasilitator Nasional Koding dan Kecerdasan Artifisial Kemendikdasmen RI)*  
*(Dosen Lektor & Ketua Program Studi S1 Sistem Komputer, Universitas Parna Raya)*  

**Penelaah & Konsultan Ahli:**  
Tim Pengembang Kurikulum KKA Direktorat Guru Pendidikan Dasar Kemendikdasmen RI  

**Penerbit:**  
Pusat Perbukuan  
Badan Standar, Kurikulum, dan Asesmen Pendidikan  
Kementerian Pendidikan Dasar dan Menengah Republik Indonesia  
Tahun 2025 / 2026  

---

## IDENTITAS PENERBITAN & HAK CIPTA
**Judul Buku:** Koding dan Kecerdasan Artifisial untuk SD/MI Kelas V (Fase C)  
**Penulis:** Gede Erik Aktama, S.Pd., M.Pd.  
**Penyunting / Editor Naskah:** Tim Fasilitator Dikdasmen Kemendikdasmen  
**Tata Letak & Tipografi:** Format Standar Buku Ajar UNESCO (15,5 cm x 23,0 cm)  
**Desain Sampul & Ilustrasi:** Tim Desain Edukatif Digital Aktama  
**Penerbit:** Pusat Perbukuan Kemendikdasmen RI  
**Hak Cipta Dilindungi Undang-Undang:** Berdasarkan Permendikdasmen No. 13 Tahun 2025 tentang Kurikulum pada Pendidikan Dasar dan Menengah.  

---

## KATA PENGANTAR KEMENDIKDASMEN
Puji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa. Perkembangan teknologi digital dan kecerdasan artifisial telah melaju sedemikian pesat, menyentuh hampir setiap segi kehidupan manusia. Menjawab tantangan tersebut, Kementerian Pendidikan Dasar dan Menengah resmi menghadirkan mata pelajaran pilihan **Koding dan Kecerdasan Artifisial (KKA)** mulai jenjang Sekolah Dasar pada Fase C (Kelas V dan VI).

Buku Teks Pelajaran ini disusun dengan pendekatan **Pembelajaran Mendalam (*Deep Learning*)** yang berkesadaran (*mindful*), bermakna (*meaningful*), dan menggembirakan (*joyful*). Melalui buku ini, anak-anak Indonesia diajak bukan sekadar menjadi konsumen pasif teknologi, melainkan menjadi penemu dan pencipta muda yang bernalar kritis, kreatif, serta berakhlak mulia.

Apresiasi tinggi kami sampaikan kepada Saudara **Gede Erik Aktama, S.Pd., M.Pd.** atas dedikasi dan karyanya dalam menyusun buku teks yang kaya ilustrasi visual, aplikatif, dan kontekstual ini. Selamat bertualang menjelajahi dunia koding!

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
4. Mengenal sahabat kecerdasan artifisial dan peran sensor peniru pancaindra manusia.
5. Melatih kecerdasan artifisial mengenali foto benda menggunakan Google Teachable Machine.
6. Merancang game dan animasi penyelamat laut Nusantara buatanmu sendiri di Scratch!

Ingatlah selalu pesan Robot Kibo: *"Jangan pernah takut salah saat mencoba! Kesalahan koding (bug) adalah teman belajar terbaik yang membuat otak kita makin cerdas."* Selamat berkreasi dan jadilah kebanggaan nusa dan bangsa!

Manado, 2025  
**Gede Erik Aktama, S.Pd., M.Pd.**  
*(Fasilitator Nasional KKA Kemendikdasmen RI)*  
*(Dosen Lektor & Kaprodi Sistem Komputer, Universitas Parna Raya)*

---

## DAFTAR ISI
Halaman Judul & Hak Cipta
Kata Pengantar Kemendikdasmen
Prakata Penulis
Daftar Isi, Daftar Gambar, dan Daftar Tabel
Petunjuk Penggunaan Fitur Buku
Mengenal Tokoh Sahabat Belajar
Peta Konsep Pembelajaran Tahunan

SEMESTER 1
  BAB I: Berpikir Komputasional dan Pemecahan Masalah (16 JP)
    Misi 1: Menjadi Detektif Logika Cilik
    A. Pendahuluan: Misteri Sepatu Erik yang Lenyap
    B. Konsep dan Materi Pembelajaran (4 Jurus Utama)
    C. Proses dan Aktivitas Belajar (Ayo Mencoba)
    D. Tugas Proyek Kinerja Siswa (LKPD 1.1 Labirin Kibo)
    E. Rangkuman Materi Bab I
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder
  BAB II: Mengenal Teknologi Digital dan Perangkat Komputer (12 JP)
    Misi 2: Sang Penjelajah Perangkat Komputer
    A. Pendahuluan: Misteri Layar Komputer yang Gelap Gulita
    B. Konsep dan Materi Pembelajaran (3 Pilar, Anatomi Dapur Restoran, Ergonomi & 20-20-20)
    C. Proses dan Aktivitas Belajar (Detektif Kabel & Port)
    D. Tugas Proyek Kinerja Siswa (LKPD 2.1 Klasifikasi Hardware)
    E. Rangkuman Materi Bab II
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder
  BAB III: Menjaga Rahasia dan Keamanan Data Pribadi (8 JP)
    Misi 3: Agen Rahasia Penjaga Kata Sandi
    A. Pendahuluan: Perangkap Permen Game Online
    B. Konsep dan Materi Pembelajaran (Data Sensitif vs Umum, Rumus Sandi Super, Phishing, Anti-Cyberbullying)
    C. Proses dan Aktivitas Belajar (Simulasi Ketangguhan Sandi)
    D. Tugas Proyek Kinerja Siswa (LKPD 3.1 Poster Kampanye Agen Cerdas)
    E. Rangkuman Materi Bab III
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder

SEMESTER 2
  BAB IV: Mengenal Kecerdasan Artifisial (12 JP)
    Misi 4: Sahabat Robot Kecerdasan Artifisial
    A. Pendahuluan: Apakah Robot Kibo Punya Perasaan?
    B. Konsep dan Materi Pembelajaran (Definisi AI, 5 Ide Besar, Sensor vs Pancaindra, AI Nusantara, Etika)
    C. Proses dan Aktivitas Belajar (Unplugged Robot Sensor)
    D. Tugas Proyek Kinerja Siswa (LKPD 4.1 Eksplorasi Sensor Sekitarku)
    E. Rangkuman Materi Bab IV
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder
  BAB V: Eksperimen Klasifikasi Data Bersama AI (12 JP)
    Misi 5: Pelatih Mesin Cerdas Teachable Machine
    A. Pendahuluan: Mengajari Kibo Memilah Sampah Sekolah
    B. Konsep dan Materi Pembelajaran (Siklus Machine Learning, 4 Langkah Teachable Machine, Mitigasi Bias)
    C. Proses dan Aktivitas Belajar (Uji Ketahanan Pencahayaan)
    D. Tugas Proyek Kinerja Siswa (LKPD 5.1 Eksperimen Detektor Sampah)
    E. Rangkuman Materi Bab V
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder
  BAB VI: Berkreasi dengan Koding Blok Visual Scratch (12 JP)
    Misi 6: Sang Pencipta Game Nusantara Scratch & Gelar Karya
    A. Pendahuluan: Kucing Scratch Penyelamat Terumbu Karang
    B. Konsep dan Materi Pembelajaran (Filosofi 4P Resnick, 5 Zona Antarmuka, Kartu Mantra Balok, Tutorial Game Konservasi Laut, Panduan Gelar Karya)
    C. Proses dan Aktivitas Belajar (Praktikum Mini Rintangan Sampah)
    D. Tugas Proyek Kinerja Siswa (LKPD 6.1 Portofolio Game Scratch & Gelar Karya)
    E. Rangkuman Materi Bab VI
    F. Tes Formatif (Uji Pemahaman HOTS)
    G. Kunci Jawaban Tes Formatif
    H. Pojok Diskusi Bersama Ayah dan Bunda di Rumah
    I. Jurnal Refleksiku & Lencana Medali Bintang Koder

BAGIAN AKHIR
  Evaluasi Komprehensif Sumatif Akhir Tahun (25 Soal Kasus HOTS)
  Kunci Jawaban Sumatif Akhir Tahun
  Glosarium Istilah Komputasi & AI A-Z
  Daftar Pustaka & Rujukan Standar Resmi
  Indeks Kata
  Profil Penulis & Fasilitator ToT Nasional

---

## DAFTAR GAMBAR
Gambar 0.1: Empat Sahabat Belajar Koding dan Kecerdasan Artifisial Kelas 5
Gambar 1.1: Komik Sahabat Koder — Misteri Sepatu Erik yang Lenyap di Kamar Berantakan
Gambar 1.2: Jurus 1 — Dekomposisi Memotong Masalah Raksasa Menjadi Potongan Kecil
Gambar 1.3: Jurus 2 — Pengenalan Pola pada Alam, Batik Nusantara, dan Angka Koding
Gambar 1.4: Jurus 3 — Abstraksi Menyaring Hal Penting dan Membuang Rincian Rumit
Gambar 1.5: Contoh Bagan Alir (Flowchart) — Algoritma Membuat Teh Manis Hangat
Gambar 1.6: Detektif Logika — Mengenal Bug dan 4 Langkah Sakti Debugging
Gambar 1.7: Peta Pikiran (Mind Map) Rangkuman 4 Jurus Berpikir Komputasional
Gambar 2.1: Komik Sahabat Koder — Misteri Layar Komputer yang Gelap Gulita di Laboratorium
Gambar 2.2: Arsitektur Lengkap Sistem Komputer — Hardware, Software, dan Brainware
Gambar 2.3: Analogi Alur Kerja Sistem Komputer — Dapur Restoran Kibo
Gambar 2.4: Panduan Posisi Duduk Ergonomis dan Senam Mata Aturan 20-20-20
Gambar 3.1: Komik Sahabat Koder — Perangkap Permen Game Online dan Sirine Bahaya Kibo
Gambar 3.2: Perisai Keamanan Data Pribadi dan Rumus Kata Sandi Kuat
Gambar 3.3: Poster 4 Jurus Sakti — Internet Sehat dan Stop Cyberbullying
Gambar 4.1: Komik Sahabat Koder — Apakah Robot Kibo Punya Hati dan Perasaan?
Gambar 4.2: Perbandingan Sensor Komputer Meniru Fungsi Pancaindra Manusia
Gambar 4.3: Kecerdasan Artifisial Penolong Negeri — Penerapan di Indonesia
Gambar 5.1: Komik Sahabat Koder — Mengajari Kibo Memilah Sampah Sekolah Menggunakan AI
Gambar 5.2: Siklus Kerja Pembelajaran Mesin (Machine Learning) — Data, Latih, Evaluasi
Gambar 5.3: Panduan 4 Langkah Praktikum Melatih Model AI dengan Google Teachable Machine
Gambar 6.1: Komik Sahabat Koder — Kucing Scratch Penyelamat Terumbu Karang Nusantara
Gambar 6.2: Peta Antarmuka Studio Koding Blok Visual Scratch 3.0
Gambar 6.3: Kartu Mantra Koding Blok Visual Scratch 3.0

---

## MENGENAL TOKOH SAHABAT BELAJAR

[[IMAGE: gambar_tokoh_sahabat.png | Gambar 0.1: Empat Sahabat Belajar Koding dan Kecerdasan Artifisial Kelas 5]]

Di sepanjang buku ini, kalian akan ditemani oleh empat sahabat hebat:
1. **Erik:** Teman kita yang berambut ikal pendek, selalu penuh semangat, suka bertanya, dan gemar membongkar-pasang balok mainan untuk mencari tahu cara kerjanya.
2. **Siti:** Teman kita yang berkerudung hijau teduh, sangat teliti, gemar merawat tanaman bunga di taman sekolah, dan senang menggambar lukisan digital.
3. **Made:** Teman kita yang mengenakan udeng khas Bali, lincah bergerak, penari tari daerah yang luwes, serta selalu punya ide-ide unik dan kreatif.
4. **Robot Kibo:** Robot asisten cerdas berwarna biru-oranye dengan wajah layar ramah. Robot Kibo setia memandu kita memecahkan kode rahasia dan melatih model AI.
"""

full_siswa_gold_md = "\n\n".join([
    FRONT_MATTER_GOLD,
    BAB_1_GOLD,
    BAB_2_GOLD,
    BAB_3_GOLD,
    BAB_4_GOLD,
    BAB_5_GOLD,
    BAB_6_GOLD,
    BAGIAN_AKHIR_GOLD
])

# Save Markdown files
for base in [tot_dir, local_dir]:
    try:
        with open(os.path.join(base, "Buku_Siswa_Koding_dan_KA_Kelas_5_SD.md"), "w", encoding="utf-8") as f:
            f.write(full_siswa_gold_md.strip() + "\n")
    except Exception as e:
        print(f"Notice saving MD in {base}: {e}")

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

def prepare_template_doc(template_path, new_footer_text):
    doc = docx.Document(template_path)
    for section in doc.sections:
        footer = section.footer
        if footer.paragraphs:
            p_foot = footer.paragraphs[0]
            p_foot.text = ""
            p_foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r_foot = p_foot.add_run(f"{new_footer_text}  |  ")
            r_foot.font.name = 'Times New Roman'
            r_foot.font.size = Pt(8.5)
            r_foot.font.italic = True
            r_foot.font.color.rgb = RGBColor(100, 116, 139)
            fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
            p_foot._p.append(fldSimple)

    sectPr = doc.sections[-1]._sectPr
    for child in list(doc._body._element):
        if child != sectPr:
            doc._body._element.remove(child)

    return doc

def build_full_book_from_template(md_content, output_docx_name, is_guru=False, cover_path=None):
    footer_title = "Buku Panduan Guru: KKA Kelas 5 SD (Fase C)" if is_guru else "Koding & Kecerdasan Artifisial — Kelas 5 SD"
    doc = prepare_template_doc(template_src, footer_title)
    
    if cover_path and os.path.exists(cover_path) and not is_guru:
        p_cov = doc.add_paragraph()
        p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cov.paragraph_format.space_before = Pt(0)
        p_cov.paragraph_format.space_after = Pt(0)
        r_cov = p_cov.add_run()
        r_cov.add_picture(cover_path, width=Inches(4.9))
        doc.add_page_break()

    if is_guru:
        p_t = doc.add_paragraph()
        p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_t.paragraph_format.space_before = Pt(36)
        p_t.paragraph_format.space_after = Pt(8)
        r_t = p_t.add_run("BUKU PANDUAN GURU")
        r_t.font.name = 'Times New Roman'; r_t.font.bold = True; r_t.font.size = Pt(20)
        r_t.font.color.rgb = RGBColor(146, 64, 14)

        p_sub = doc.add_paragraph()
        p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sub.paragraph_format.space_after = Pt(20)
        r_sub = p_sub.add_run("KODING DAN KECERDASAN ARTIFISIAL\nUNTUK SD/MI KELAS V (FASE C)")
        r_sub.font.name = 'Times New Roman'; r_sub.font.bold = True; r_sub.font.size = Pt(13.5)
        r_sub.font.color.rgb = RGBColor(30, 41, 59)

        p_pill = doc.add_paragraph()
        p_pill.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_pill.paragraph_format.space_after = Pt(40)
        r_pill = p_pill.add_run("PEDOMAN OPERASIONAL PEMBELAJARAN MENDALAM (DEEP LEARNING)\nBERKESADARAN (MINDFUL) • BERMAKNA (MEANINGFUL) • MENGGEMBIRAKAN (JOYFUL)")
        r_pill.font.name = 'Times New Roman'; r_pill.font.italic = True; r_pill.font.size = Pt(9)
        r_pill.font.color.rgb = RGBColor(71, 85, 105)

        p_auth = doc.add_paragraph()
        p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_auth.paragraph_format.space_after = Pt(70)
        r_auth = p_auth.add_run("Penulis:\nGede Erik Aktama, S.Pd., M.Pd.\n(Fasilitator Nasional KKA Kemendikdasmen RI)\n(Dosen Lektor & Kaprodi Sistem Komputer, Universitas Parna Raya)")
        r_auth.font.name = 'Times New Roman'; r_auth.font.bold = True; r_auth.font.size = Pt(11)
        r_auth.font.color.rgb = RGBColor(15, 23, 42)

        p_inst = doc.add_paragraph()
        p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_inst = p_inst.add_run("PUSAT PERBUKUAN\nBADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN\nKEMENTERIAN PENDIDIKAN DASAR DAN MENENGAH RI\n2025 / 2026")
        r_inst.font.name = 'Times New Roman'; r_inst.font.size = Pt(9)
        r_inst.font.color.rgb = RGBColor(100, 116, 139)

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
                        cell.text = ""
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.space_before = Pt(2)
                        if ri == 0:
                            set_cell_background(cell, "FEF3C7" if is_guru else "E0F2FE")
                            add_styled_runs(p, cell_text, base_font_size=8.5,
                                            base_color=RGBColor(146, 64, 14) if is_guru else RGBColor(3, 105, 161),
                                            font_name='Times New Roman')
                            for r in p.runs:
                                r.bold = True
                        else:
                            add_styled_runs(p, cell_text, base_font_size=8.5,
                                            base_color=RGBColor(30, 41, 59), font_name='Times New Roman')
        in_table = False
        table_rows = []

    current_section = "NORMAL"

    for line in lines:
        sline = line.strip()

        if sline.startswith("|") and sline.endswith("|"):
            in_table = True
            table_rows.append(sline)
            continue
        else:
            if in_table:
                flush_table()

        if not sline:
            continue

        # Embedded Images [[IMAGE: filename.png | Caption]]
        if sline.startswith("[[IMAGE:") and "]]" in sline:
            tag_content = sline.replace("[[IMAGE:", "").replace("]]", "").strip()
            parts = [p.strip() for p in tag_content.split("|")]
            img_filename = parts[0]
            caption = parts[1] if len(parts) > 1 else ""
            img_full = os.path.join(assets_local, img_filename)
            if not os.path.exists(img_full):
                img_full = os.path.join(assets_tot, img_filename)
            if os.path.exists(img_full):
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(10)
                p_img.paragraph_format.space_after = Pt(3)
                r_img = p_img.add_run()
                # Author photo (3x4 portrait) uses smaller width
                img_width = Inches(1.5) if "foto_penulis" in img_filename else Inches(4.6)
                r_img.add_picture(img_full, width=img_width)
                if caption:
                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(10)
                    r_cap = p_cap.add_run(caption)
                    r_cap.font.name = 'Times New Roman'
                    r_cap.font.size = Pt(8.5)
                    r_cap.font.italic = True
                    r_cap.font.color.rgb = RGBColor(71, 85, 105)
            continue

        clean_heading = sline.replace("**", "").replace("*", "")
        clean_upper = clean_heading.upper()

        # Section Context Detection
        if clean_heading.startswith("# ") or clean_heading.startswith("## ") or clean_heading.startswith("### ") or clean_heading.startswith("#### "):
            if "DAFTAR ISI" in clean_upper:
                current_section = "DAFTAR_ISI"
            elif "DAFTAR GAMBAR" in clean_upper or "DAFTAR TABEL" in clean_upper:
                current_section = "DAFTAR_GAMBAR"
            elif "IDENTITAS PENERBITAN" in clean_upper:
                current_section = "IDENTITAS"
            elif "INDEKS KATA" in clean_upper:
                current_section = "INDEKS"
            elif any(clean_upper.startswith(x) for x in ["# BAB", "## BAB", "### BAB", "# SEMESTER", "## SEMESTER", "# BAGIAN", "## BAGIAN", "## KATA PENGANTAR", "## PRAKATA", "## PETUNJUK", "## DAFTAR TOKOH", "## MENGENAL TOKOH", "## PETA KONSEP", "### AYO", "### LKPD", "### PROFIL PENULIS", "### DAFTAR PUSTAKA", "## A.", "## B.", "## C.", "## D.", "## E.", "## F.", "## G.", "## H.", "## I."]):
                current_section = "NORMAL"

            # Render Headings
            if clean_heading.startswith("# "):
                if not (clean_heading.startswith("# KODING") or clean_heading.startswith("# PANDUAN GURU:")):
                    doc.add_page_break()
                p = doc.add_paragraph()
                if "BAB " in clean_heading:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(16)
                p.paragraph_format.space_after = Pt(8)
                run = p.add_run(clean_heading[2:])
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(14)
                run.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(15, 23, 42)
            elif clean_heading.startswith("## "):
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(14)
                p.paragraph_format.space_after = Pt(6)
                run = p.add_run(clean_heading[3:])
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(12)
                run.font.color.rgb = RGBColor(180, 83, 9) if is_guru else RGBColor(2, 132, 199)
            elif clean_heading.startswith("### "):
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
                run = p.add_run(clean_heading[4:])
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(30, 41, 59) if is_guru else RGBColor(13, 148, 136)
            elif clean_heading.startswith("#### "):
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(3)
                run = p.add_run(clean_heading[5:])
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(71, 85, 105)
            continue

        # Section 1: DAFTAR ISI (Professional Clean Indented Format, ZERO Bullets)
        if current_section == "DAFTAR_ISI":
            if sline.startswith("---"):
                current_section = "NORMAL"
                continue
            clean_item = re.sub(r'^[\*\-\s]+', '', sline).strip()
            if not clean_item:
                continue
            if clean_item.startswith("SEMESTER") or clean_item.startswith("BAGIAN AKHIR"):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0)
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(2)
                run = p.add_run(clean_item)
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(2, 132, 199)
            elif clean_item.startswith("BAB "):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.18)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(1.5)
                run = p.add_run(clean_item)
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(15, 23, 42)
            elif re.match(r'^[A-I]\.\s', clean_item) or clean_item.startswith("Misi "):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.38)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                run = p.add_run(clean_item)
                run.font.name = 'Times New Roman'; run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(51, 65, 85)
            else:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.18)
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                run = p.add_run(clean_item)
                run.font.name = 'Times New Roman'; run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(51, 65, 85)
            continue

        # Section 2: DAFTAR GAMBAR & TABEL (Clean Hanging Indent, ZERO Bullets)
        if current_section == "DAFTAR_GAMBAR":
            if sline.startswith("---"):
                current_section = "NORMAL"
                continue
            clean_item = re.sub(r'^[\*\-\s]+', '', sline).strip()
            if not clean_item:
                continue
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.28)
            p.paragraph_format.first_line_indent = -Inches(0.28)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            m = re.match(r'^(Gambar\s+[\d\.]+:|Tabel\s+[\d\.]+:)(.*)', clean_item)
            if m:
                r1 = p.add_run(m.group(1))
                r1.font.name = 'Times New Roman'; r1.font.bold = True; r1.font.size = Pt(9.5)
                r1.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(2, 132, 199)
                r2 = p.add_run(m.group(2))
                r2.font.name = 'Times New Roman'; r2.font.size = Pt(9.5)
                r2.font.color.rgb = RGBColor(51, 65, 85)
            else:
                add_styled_runs(p, clean_item, base_font_size=9.5, base_color=RGBColor(51, 65, 85), font_name='Times New Roman')
            continue

        # Section 3: IDENTITAS PENERBITAN (Clean Key-Value, ZERO Bullets)
        if current_section == "IDENTITAS":
            if sline.startswith("---"):
                current_section = "NORMAL"
                continue
            clean_item = re.sub(r'^[\*\-\s]+', '', sline).strip()
            if not clean_item:
                continue
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.15)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2)
            add_styled_runs(p, clean_item, base_font_size=9.5, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')
            continue

        # Section 4: INDEKS KATA (Clean Alphabet Headers, ZERO Bullets)
        if current_section == "INDEKS":
            if sline.startswith("---"):
                current_section = "NORMAL"
                continue
            clean_item = re.sub(r'^[\*\-\s]+', '', sline).strip()
            if not clean_item:
                continue
            letter = clean_item.replace("#", "").replace("*", "").strip()
            if len(letter) == 1 and letter.isalpha():
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.left_indent = Inches(0)
                run = p.add_run(letter)
                run.font.name = 'Times New Roman'; run.font.bold = True; run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(2, 132, 199)
            else:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.25)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                add_styled_runs(p, clean_item, base_font_size=9, base_color=RGBColor(51, 65, 85), font_name='Times New Roman')
            continue

        # Normal Body Processing

        # Callout Boxes (> quote)
        if sline.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.right_indent = Inches(0.15)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            raw_text = sline.lstrip("> ")
            add_styled_runs(p, raw_text, base_font_size=9.5, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')
            for r in p.runs:
                r.italic = True
            if is_guru:
                apply_callout_box(p, bg_hex="FFFBEB", border_hex="F59E0B")
            else:
                apply_callout_box(p, bg_hex="F0F9FF", border_hex="0284C7")
            continue

        # Checkboxes (* [ ] or [ ]) -> Render as Clean Ballot Box (□), NO Bullets
        if sline.startswith("* [ ]") or sline.startswith("- [ ]") or sline.startswith("[ ]"):
            clean_text = re.sub(r'^[\*\-\s]*\[\s*\]\s*', '', sline).strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.first_line_indent = -Inches(0.18)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            r_box = p.add_run("□  ")
            r_box.font.name = 'Times New Roman'; r_box.font.size = Pt(11); r_box.font.bold = True
            r_box.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(2, 132, 199)
            add_styled_runs(p, clean_text, base_font_size=10, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')
            continue

        # Check if line was written with bullet then number/letter (e.g. "* 1." or "* A.")
        m_bnum = re.match(r'^[\*\-]\s+([0-9]+|[A-Za-z])[\.\)]\s+(.*)', sline)
        if m_bnum:
            prefix = m_bnum.group(1)
            rest = m_bnum.group(2)
            sline = f"{prefix}. {rest}"

        # Multiple-choice exam options: A. , B. , C. , D.
        if re.match(r'^[A-D]\.\s', sline):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.first_line_indent = -Inches(0.18)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.line_spacing = 1.15
            opt_letter = sline[:3]
            r_opt = p.add_run(opt_letter)
            r_opt.font.name = 'Times New Roman'; r_opt.font.size = Pt(10); r_opt.font.bold = True
            r_opt.font.color.rgb = RGBColor(15, 23, 42)
            opt_text = sline[3:].strip()
            add_styled_runs(p, opt_text, base_font_size=10, base_color=RGBColor(51, 65, 85), font_name='Times New Roman')

        # Numbered List (1. , 2. , etc.) with Hanging Indent
        elif re.match(r'^\d+\.\s', sline):
            leading_spaces = len(line) - len(line.lstrip())
            level = min(2, leading_spaces // 2)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.24 + level * 0.18)
            p.paragraph_format.first_line_indent = -Inches(0.18)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            match = re.match(r'^(\d+\.\s)(.*)', sline)
            num_prefix = match.group(1)
            rest_text = match.group(2)
            r_num = p.add_run(num_prefix)
            r_num.font.name = 'Times New Roman'; r_num.font.size = Pt(10); r_num.font.bold = True
            r_num.font.color.rgb = RGBColor(15, 23, 42)
            add_styled_runs(p, rest_text, base_font_size=10, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')

        # Bullet List (* or -) with Intelligent Indentation & Hanging Indent
        elif sline.startswith("* ") or sline.startswith("- "):
            leading_spaces = len(line) - len(line.lstrip())
            level = min(2, leading_spaces // 2)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.24 + level * 0.18)
            p.paragraph_format.first_line_indent = -Inches(0.14)
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            bullet_sym = "•  " if level == 0 else ("–  " if level == 1 else "▪  ")
            r_b = p.add_run(bullet_sym)
            r_b.font.name = 'Times New Roman'; r_b.font.size = Pt(9.5); r_b.font.bold = True
            r_b.font.color.rgb = RGBColor(146, 64, 14) if is_guru else RGBColor(2, 132, 199)
            bullet_text = re.sub(r'^[\*\-\+]\s+', '', sline)
            add_styled_runs(p, bullet_text, base_font_size=10, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')

        elif sline.startswith("```"):
            pass
        elif sline.startswith("---"):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run("―" * 38)
            run.font.name = 'Times New Roman'
            run.font.color.rgb = RGBColor(226, 232, 240)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_styled_runs(p, sline, base_font_size=10, base_color=RGBColor(30, 41, 59), font_name='Times New Roman')

    if in_table:
        flush_table()

    # Save to output_docx_name directly and delete redundant files
    for base in [local_dir, tot_dir]:
        out_f = os.path.join(base, output_docx_name)
        redundant_name = output_docx_name.replace(".docx", "_Edisi_Terbaru.docx")
        redundant_f = os.path.join(base, redundant_name)
        if os.path.exists(redundant_f):
            try:
                os.remove(redundant_f)
                print(f"Deleted redundant file: {redundant_f}")
            except Exception as e:
                print(f"Notice deleting {redundant_f}: {e}")

        try:
            doc.save(out_f)
            print(f"Official UNESCO Base DOCX Successfully Saved: {out_f}")
        except PermissionError:
            import time
            time.sleep(1)
            doc.save(out_f)
            print(f"Official UNESCO Base DOCX Successfully Saved (retry): {out_f}")

if __name__ == "__main__":
    print("Compiling Official Buku Siswa (Gold Standard Bab 1)...")
    build_full_book_from_template(full_siswa_gold_md, "Buku_Siswa_Koding_dan_KA_Kelas_5_SD.docx", is_guru=False, cover_path=cover_img_path)
    
    print("Compiling Official Buku Panduan Guru...")
    guru_bab_6_updated = replace_biblio(guru_bab_4_5_6.GURU_BAB_6)
    full_guru_md_clean = "\n\n".join([
        guru_data_part1.GURU_FRONT_MATTER,
        guru_bab_1_2_3.GURU_BAB_1,
        guru_bab_1_2_3.GURU_BAB_2,
        guru_bab_1_2_3.GURU_BAB_3,
        guru_bab_4_5_6.GURU_BAB_4,
        guru_bab_4_5_6.GURU_BAB_5,
        guru_bab_6_updated
    ])
    
    for base in [tot_dir, local_dir]:
        try:
            with open(os.path.join(base, "Buku_Panduan_Guru_Koding_dan_KA_Kelas_5_SD.md"), "w", encoding="utf-8") as f:
                f.write(full_guru_md_clean.strip() + "\n")
        except Exception:
            pass
            
    build_full_book_from_template(full_guru_md_clean, "Buku_Panduan_Guru_Koding_dan_KA_Kelas_5_SD.docx", is_guru=True, cover_path=None)
    print("GOLD STANDARD COMPILATION FINISHED SUCCESSFULLY!")
