# -*- coding: utf-8 -*-
import docx
import re

doc = docx.Document(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx')

print(f"Total paragraphs: {len(doc.paragraphs)}")

# Look for all paragraphs with any bullet character
bullets = []
for i, p in enumerate(doc.paragraphs):
    t = p.text
    if '•' in t:
        bullets.append((i, p.text.strip()))

print(f"Total paragraphs with bullet '•': {len(bullets)}")
print("\nFirst 30 bullets:")
for i, t in bullets[:30]:
    print(f"[{i}] {t[:80]}")

print("\nMiddle bullets (around bab content):")
for i, t in bullets[55:85]:
    print(f"[{i}] {t[:80]}")

print("\nLast 30 bullets:")
for i, t in bullets[-30:]:
    print(f"[{i}] {t[:80]}")
