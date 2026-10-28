# -*- coding: utf-8 -*-
import docx
import re

doc = docx.Document(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx')

print("=== CHECKING ALL PARAGRAPHS IN DOCX FOR WEIRD BULLETS / NUMBERS ===")
for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    # Check for:
    # 1. • followed by letter or number: e.g. • A. or • 1.
    if re.search(r'•\s*([0-9]+|[A-Za-z])[\.\)]', text):
        print(f"[Line {i}] Bullet with Number/Letter: {text[:100]}")
    # 2. multiple bullets or weird characters:
    if text.count('•') > 1:
        print(f"[Line {i}] Multiple bullets: {text[:100]}")
    # 3. questions with weird bullets:
    if re.search(r'^\d+\..*•', text):
        print(f"[Line {i}] Number followed by bullet in text: {text[:100]}")
    # 4. lines that have * or - literally left over:
    if re.search(r'^\s*[\*\-]\s+', text):
        print(f"[Line {i}] Raw markdown list marker left: {text[:100]}")
    # 5. lines with ** left over:
    if '**' in text:
        print(f"[Line {i}] Raw asterisks ** left: {text[:100]}")
