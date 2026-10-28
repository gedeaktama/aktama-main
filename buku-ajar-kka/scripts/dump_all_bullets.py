# -*- coding: utf-8 -*-
import docx
import re

doc = docx.Document(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx')

print("=== ALL 316 BULLETS CATEGORIZED ===")
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if '•' in t:
        print(f"p[{i:4d}] {t}")
