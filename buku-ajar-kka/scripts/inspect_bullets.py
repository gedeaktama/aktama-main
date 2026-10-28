# -*- coding: utf-8 -*-
import docx
import re
import os

doc_path = r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx'
if not os.path.exists(doc_path):
    doc_path = r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD.docx'

doc = docx.Document(doc_path)
print(f"Checking {doc_path} (Paragraphs: {len(doc.paragraphs)})")

patterns = [
    ("Bullet with number (e.g. • 1. or •1)", r'•\s*\d+[\.\)]'),
    ("Double bullet or bullet dash", r'[•\-\*]\s*[•\-\*]'),
    ("Number with bullet (e.g. 1. •)", r'^\s*\d+[\.\)]\s*[•\-\*]'),
    ("Any bullet symbol", r'•'),
    ("Numbering pattern", r'^\s*\d+[\.\)]\s+'),
]

for name, pat in patterns:
    matches = []
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if re.search(pat, t):
            matches.append((i, p.style.name, t))
    print(f"\n=== Pattern: {name} (Total: {len(matches)}) ===")
    for idx, s, t in matches[:15]:
        print(f"  Line {idx} [{s}]: {t[:90]}")
