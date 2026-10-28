# -*- coding: utf-8 -*-
import os, sys, docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

tot_dir = r"D:\OneDrive - Universitas Parnaraya\GEDE ERIK AKTAMA\TOT\Outline Buku Ajar KKA\Buku Kelas 5 SD"
workspace_dir = r"d:\Xampp2\htdocs\aktama-main\buku-ajar-kka\buku-kelas-5-sd"
cover_img_path = os.path.join(tot_dir, "assets", "cover_buku_siswa_sd5.jpg")

os.makedirs(os.path.join(tot_dir, "assets"), exist_ok=True)
os.makedirs(os.path.join(workspace_dir, "assets"), exist_ok=True)

def save_text(filename, content):
    for base in [tot_dir, workspace_dir]:
        full_path = os.path.join(base, filename)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
    print(f"Text Saved: {filename}")

def build_docx(md_text, docx_filename, cover_image=None):
    doc = docx.Document()
    for s in doc.sections:
        s.page_width = Pt(439.45)   # UNESCO B5 Width: 15.5 cm
        s.page_height = Pt(652.05)  # UNESCO B5 Height: 23.0 cm
        s.top_margin = Pt(56.7)
        s.bottom_margin = Pt(56.7)
        s.left_margin = Pt(56.7)
        s.right_margin = Pt(56.7)

    if cover_image and os.path.exists(cover_image):
        p_cov = doc.add_paragraph()
        p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p_cov.add_run()
        run.add_picture(cover_image, width=Inches(4.8))
        doc.add_page_break()

    lines = md_text.split("\n")
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        rows_data = []
        for r in table_rows:
            parts = [c.strip() for c in r.split("|")[1:-1]]
            if parts and not all(set(c).issubset({'-', ':', ' '}) for c in parts):
                rows_data.append(parts)
        if rows_data:
            num_cols = max(len(r) for r in rows_data)
            tbl = doc.add_table(rows=len(rows_data), cols=num_cols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.style = 'Table Grid'
            for ri, row in enumerate(rows_data):
                for ci, cell_text in enumerate(row):
                    if ci < num_cols:
                        cell = tbl.cell(ri, ci)
                        cell.text = cell_text
                        for p in cell.paragraphs:
                            p.paragraph_format.space_after = Pt(2)
                            p.paragraph_format.space_before = Pt(2)
        in_table = False
        table_rows = []

    for line in lines:
        sline = line.strip()
        if sline.startswith("|") and sline.endswith("|"):
            in_table = True
            table_rows.append(sline)
            continue
        else:
            if in_table:
                flush_table()

        if not sline:
            continue

        if sline.startswith("# "):
            p = doc.add_paragraph(sline[2:], style='Heading 1')
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif sline.startswith("## "):
            doc.add_paragraph(sline[3:], style='Heading 1')
        elif sline.startswith("### "):
            doc.add_paragraph(sline[4:], style='Heading 2')
        elif sline.startswith("#### "):
            doc.add_paragraph(sline[5:], style='Heading 3')
        elif sline.startswith("* ") or sline.startswith("- "):
            doc.add_paragraph(sline[2:], style='List Paragraph')
        elif any(sline.startswith(f"{i}. ") for i in range(1, 35)):
            doc.add_paragraph(sline, style='List Paragraph')
        elif sline.startswith(">"):
            p = doc.add_paragraph(sline.lstrip("> "), style='Normal')
            p.paragraph_format.left_indent = Inches(0.25)
        elif sline.startswith("---"):
            pass
        else:
            doc.add_paragraph(sline, style='Normal')

    if in_table:
        flush_table()

    for base in [tot_dir, workspace_dir]:
        full_docx = os.path.join(base, docx_filename)
        doc.save(full_docx)
    print(f"DOCX Saved: {docx_filename}")

with open("d:\\Xampp2\\htdocs\\aktama-main\\build_sd5_siswa_book.py", "w", encoding="utf-8") as f:
    f.write("# Generator ready\n")
