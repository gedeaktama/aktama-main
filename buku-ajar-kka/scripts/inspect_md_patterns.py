# -*- coding: utf-8 -*-
with open(r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd\Buku_Siswa_Koding_dan_KA_Kelas_5_SD.md', 'r', encoding='utf-8') as f:
    md_lines = f.readlines()

print(f"Total lines in Buku Siswa md: {len(md_lines)}")

# Let's inspect all lines starting with bullets or numbers or containing bullet
import re

print("\n--- SAMPLE LIST & NUMBERING LINES IN MD ---")
sample_count = 0
for i, line in enumerate(md_lines):
    sline = line.strip()
    # Check for bullet or number patterns
    if re.match(r'^[\*\-\+]\s', sline) or re.match(r'^\d+[\.\)]', sline):
        # Let's look for interesting patterns:
        # e.g., bullet followed by number, or number inside a bullet list, or sub-bullets
        if re.match(r'^[\*\-\+]\s*\d+', sline) or '•' in sline or re.match(r'^\s*[\*\-]\s+[A-D]\.', sline):
            print(f"Line {i+1}: {sline}")
            sample_count += 1
            if sample_count > 30:
                break

print(f"Finished checking special patterns.")
