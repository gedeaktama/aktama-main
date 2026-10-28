# -*- coding: utf-8 -*-
import docx
import re

doc = docx.Document(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx')

categories = {
    "identitas_buku": [],       # Judul Buku, Penulis, etc.
    "daftar_isi": [],           # TOC items: BAB, SEMESTER, A., B., Misi
    "index_letters": [],        # Single letters like D, E, H, S
    "checkboxes": [],           # [ ] Checkboxes
    "command_brackets": [],     # [ MAJU ] etc.
    "other_anomalies": [],      # Anything starting with letter/number
    "normal_text_bullets": []   # Valid regular bullet points in text
}

for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    if '•' not in text:
        continue
    
    # Remove bullet prefix for classification
    clean = re.sub(r'^[•\s]+', '', text).strip()
    
    if any(k in clean for k in ["Judul Buku:", "Penulis:", "Penyunting", "Tata Letak", "Desain Sampul", "Penerbit:", "Hak Cipta"]):
        categories["identitas_buku"].append((i, clean))
    elif any(clean.startswith(x) for x in ["Halaman Judul", "Kata Pengantar", "Prakata", "Daftar Isi", "Petunjuk Penggunaan", "Mengenal Tokoh", "Peta Konsep", "SEMESTER", "BAB ", "Misi ", "BAGIAN AKHIR", "Evaluasi Komprehensif", "Glosarium", "Daftar Pustaka", "Indeks Kata", "Profil Penulis"]) or re.match(r'^[A-I]\.\s', clean):
        categories["daftar_isi"].append((i, clean))
    elif re.match(r'^[A-Z]$', clean):
        categories["index_letters"].append((i, clean))
    elif clean.startswith("[ ]"):
        categories["checkboxes"].append((i, clean))
    elif re.match(r'^\[\s*[A-Z_ ]+\s*\]', clean):
        categories["command_brackets"].append((i, clean))
    elif re.match(r'^[0-9A-Za-z]\.', clean) or re.match(r'^[0-9]', clean):
        categories["other_anomalies"].append((i, clean))
    else:
        categories["normal_text_bullets"].append((i, clean))

for cat, items in categories.items():
    print(f"\n==========================================")
    print(f"CATEGORY: {cat} (Count: {len(items)})")
    print(f"==========================================")
    for idx, c in items[:12]:
        print(f"  p[{idx:4d}] {c[:80]}")
