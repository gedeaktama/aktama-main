# -*- coding: utf-8 -*-
import re

for fname in ['Buku_Siswa_Koding_dan_KA_Kelas_5_SD.md', 'Buku_Panduan_Guru_Koding_dan_KA_Kelas_5_SD.md']:
    path = rf'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd\{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"\n==========================================")
    print(f"{fname}: checking indented lines")
    print(f"==========================================")
    indented = []
    for i, line in enumerate(lines):
        if line.startswith("  ") or line.startswith("\t"):
            indented.append((i+1, line.strip()))
    print(f"Total indented lines: {len(indented)}")
    for lno, text in indented[:30]:
        print(f"  Line {lno:4d}: {text[:80]}")
