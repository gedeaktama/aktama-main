# -*- coding: utf-8 -*-
import re

def check_file(filepath):
    print(f"\n==========================================")
    print(f"CHECKING: {filepath}")
    print(f"==========================================")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    bullet_letter_or_number = []
    nested_bullets = []
    numbered_with_bullets = []
    
    for i, line in enumerate(lines):
        sline = line.strip()
        # Pattern 1: * 1. or - 1. or * A. or - A.
        if re.match(r'^[\*\-\+]\s+([0-9]+|[A-Za-z])[\.\)]\s+', sline):
            bullet_letter_or_number.append((i+1, sline))
        # Pattern 2: line has bullet character directly
        if '•' in sline:
            nested_bullets.append((i+1, sline))
        # Pattern 3: Number followed by bullet
        if re.match(r'^\d+[\.\)]\s*[\*\-\•]', sline):
            numbered_with_bullets.append((i+1, sline))

    print(f"1. Lines starting with bullet THEN number/letter (e.g. '* A.' or '* 1.'): {len(bullet_letter_or_number)}")
    for lno, text in bullet_letter_or_number[:20]:
        print(f"   Line {lno}: {text}")

    print(f"2. Lines containing raw bullet symbol '•': {len(nested_bullets)}")
    for lno, text in nested_bullets[:10]:
        print(f"   Line {lno}: {text}")

    print(f"3. Lines with number followed by bullet: {len(numbered_with_bullets)}")
    for lno, text in numbered_with_bullets[:10]:
        print(f"   Line {lno}: {text}")

check_file(r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd\Buku_Siswa_Koding_dan_KA_Kelas_5_SD.md')
check_file(r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd\Buku_Panduan_Guru_Koding_dan_KA_Kelas_5_SD.md')
