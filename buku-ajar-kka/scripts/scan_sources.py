# -*- coding: utf-8 -*-
import re

files = [
    r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts\sd5_data.py',
    r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts\naskah_bab1_gold_standard.py',
    r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts\naskah_bab2_bab3_gold.py',
    r'd:\Xampp2\htdocs\aktama-main\buku-ajar-kka\scripts\naskah_bab4_bab5_bab6_gold.py',
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"\nFile: {fp}")
    # Find all occurrences of * [A-Z]. or * [0-9].
    m1 = re.findall(r'^\s*[\*\-]\s+[0-9A-Z]\..*', content, re.M)
    print(f"  Bullet followed by Number/Letter: {len(m1)}")
    if m1:
        for x in m1[:5]:
            print(f"    {x}")
    # Find all occurrences of * [ ] or - [ ]
    m2 = re.findall(r'^\s*[\*\-]\s+\[\s*\].*', content, re.M)
    print(f"  Bullet with checkbox [ ]: {len(m2)}")
    if m2:
        for x in m2[:5]:
            print(f"    {x}")
    # Find all occurrences of * [A-Z0-9_ ]+ : (e.g. * [ MAJU ] :)
    m3 = re.findall(r'^\s*[\*\-]\s+\[\s*[A-Za-z0-9_ ]+\s*\].*', content, re.M)
    print(f"  Bullet with bracket commands: {len(m3)}")
    if m3:
        for x in m3[:5]:
            print(f"    {x}")
