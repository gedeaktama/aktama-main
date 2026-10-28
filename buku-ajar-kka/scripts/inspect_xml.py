# -*- coding: utf-8 -*-
import docx

doc_path = r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx'
doc = docx.Document(doc_path)

# Let's inspect paragraphs with numbers, bullets, list paragraphs, and their XML
print("=== Inspecting paragraph styles and numbering XML ===")
num_with_numPr = 0
for i, p in enumerate(doc.paragraphs):
    xml = p._p.xml
    if '<w:numPr>' in xml:
        num_with_numPr += 1
        print(f"p[{i}] has w:numPr! Style: {p.style.name}, Text: {p.text[:60]}")

print(f"Total paragraphs with w:numPr: {num_with_numPr}")

# Check styles in the template
for s in doc.styles:
    if 'List' in s.name or 'Bullet' in s.name or 'Number' in s.name:
        print(f"Style in doc: {s.name}")
