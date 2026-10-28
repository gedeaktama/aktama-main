import os, docx, re

def audit_doc(path, label):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    doc = docx.Document(path)
    paras = doc.paragraphs
    tables = doc.tables
    print(f"\nAUDIT {label}: {os.path.basename(path)}")
    print(f"Total Paragraphs: {len(paras)}")
    print(f"Total Tables: {len(tables)}")

    stray_asterisks = 0
    stray_backticks = 0
    stray_bullets = 0

    for i, p in enumerate(paras):
        t = p.text
        # check for raw ** (stray bold markers)
        if "**" in t:
            stray_asterisks += 1
            print(f"  [STRAY **] Para {i+1}: {t[:70]}...")
        if "```" in t or ("`" in t and not "Consolas" in [r.font.name for r in p.runs if r.font.name]):
            stray_backticks += 1
            print(f"  [STRAY `] Para {i+1}: {t[:70]}...")
        if re.match(r'^[•\*\-]\s+[0-9]+[\.\)]', t):
            stray_bullets += 1
            print(f"  [STRAY BULLET] Para {i+1}: {t[:70]}...")

    print(f"Summary for {label}: Stray **: {stray_asterisks}, Stray `: {stray_backticks}, Stray Bullets: {stray_bullets}")

local_dir = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-12-sma-smk"
audit_doc(os.path.join(local_dir, "Buku_Siswa_Koding_dan_KA_Kelas_12_SMA-SMK.docx"), "Siswa SMA 12")
audit_doc(os.path.join(local_dir, "Buku_Panduan_Guru_Koding_dan_KA_Kelas_12_SMA-SMK.docx"), "Guru SMA 12")
