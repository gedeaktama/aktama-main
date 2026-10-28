# -*- coding: utf-8 -*-
import docx
import re

def analyze_paragraphs(doc_path):
    print(f"\n==============================================")
    print(f"ANALYZING: {doc_path}")
    print(f"==============================================")
    doc = docx.Document(doc_path)
    
    # 1. Any bullet followed by letter/number
    bullet_num = []
    # 2. Any bullet followed by non-letter (like punctuation, numbers)
    weird_bullets = []
    # 3. Check Daftar Isi lines
    daftar_isi = []
    in_daftar_isi = False
    
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if 'DAFTAR ISI' in t.upper():
            in_daftar_isi = True
        if in_daftar_isi and ('BAB I' in t or 'BAB 1' in t) and len(daftar_isi) > 20:
            in_daftar_isi = False
            
        if in_daftar_isi:
            daftar_isi.append((i, p.style.name, t))
            
        if '•' in t:
            # Check what follows bullet
            m = re.search(r'•\s*(.*)', t)
            if m:
                after = m.group(1).strip()
                if re.match(r'^[0-9A-Za-z]\.', after):
                    bullet_num.append((i, t))
                elif not re.match(r'^[A-Z]', after):
                    weird_bullets.append((i, t))
                    
    print(f"Total bullets followed by Number/Letter: {len(bullet_num)}")
    for i, t in bullet_num[:15]:
        print(f"  [{i}]: {t[:80]}")
        
    print(f"\nTotal weird bullets (not starting with Capital letter): {len(weird_bullets)}")
    for i, t in weird_bullets[:15]:
        print(f"  [{i}]: {t[:80]}")

analyze_paragraphs(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Siswa_Koding_dan_KA_Kelas_5_SD_Edisi_Terbaru.docx')
analyze_paragraphs(r'D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD\Buku_Panduan_Guru_Koding_dan_KA_Kelas_5_SD.docx')
