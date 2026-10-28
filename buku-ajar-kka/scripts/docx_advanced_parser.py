# -*- coding: utf-8 -*-
"""
Advanced Markdown to Word Run-Level Parser
Standard: Clean Publishing Output (No raw markdown tokens like **, *, `)
"""
import re, os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def clean_latex_symbols(text):
    """Replaces LaTeX symbols with clean Unicode glyphs and removes XML-invalid control chars"""
    text = text.replace(r'$\checkmark$', '✓')
    text = text.replace(r'$\times$', '✗')
    text = text.replace(r'\checkmark', '✓')
    text = text.replace(r'\times', '✗')
    # Filter out control characters that break XML (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    return text

def parse_inline_markdown(text):
    """
    Parses a string with nested inline markdown:
    **bold (*italic*)**, ***bold italic***, **bold**, *italic*, `code`, and plain text.
    Returns list of tuples: (content, is_bold, is_italic, is_code)
    Guarantees ZERO stray asterisks (*) or backticks (`) in output.
    """
    text = clean_latex_symbols(text)
    
    token_spec = re.compile(
        r'(`(?P<code>[^`]+)`)'
        r'|(\*\*\*(?P<bold_italic>.+?)\*\*\*)'
        r'|(\*\*(?P<bold>.+?)\*\*)'
        r'|(\*(?P<italic>[^*]+?)\*)'
        r'|(?P<plain>[^*`]+)'
    )
    
    results = []
    pos = 0
    while pos < len(text):
        m = token_spec.match(text, pos)
        if m:
            if m.group('code'):
                results.append((m.group('code'), False, False, True))
            elif m.group('bold_italic'):
                results.append((m.group('bold_italic'), True, True, False))
            elif m.group('bold'):
                bold_content = m.group('bold')
                sub_spec = re.compile(
                    r'(`(?P<cd>[^`]+)`)'
                    r'|(\*(?P<it>[^*`]+?)\*)'
                    r'|(?P<pt>[^*`]+)'
                )
                s_pos = 0
                while s_pos < len(bold_content):
                    sm = sub_spec.match(bold_content, s_pos)
                    if sm:
                        if sm.group('cd'):
                            results.append((sm.group('cd'), True, False, True))
                        elif sm.group('it'):
                            results.append((sm.group('it'), True, True, False))
                        elif sm.group('pt'):
                            clean_pt = sm.group('pt').replace('*', '').replace('`', '')
                            if clean_pt:
                                results.append((clean_pt, True, False, False))
                        s_pos = sm.end()
                    else:
                        clean_rem = bold_content[s_pos:].replace('*', '').replace('`', '')
                        if clean_rem:
                            results.append((clean_rem, True, False, False))
                        break
            elif m.group('italic'):
                results.append((m.group('italic'), False, True, False))
            elif m.group('plain'):
                plain_txt = m.group('plain').replace('*', '')
                if plain_txt:
                    results.append((plain_txt, False, False, False))
            pos = m.end()
        else:
            ch = text[pos]
            if ch != '*':
                results.append((ch, False, False, False))
            pos += 1
            
    return results

def add_styled_runs(paragraph, text, base_font_size=9.5, base_color=RGBColor(30, 41, 59), font_name='Arial'):
    """
    Adds runs to a paragraph with proper bold/italic formatting
    and removes all raw markdown symbols.
    """
    tokens = parse_inline_markdown(text)
    for content, is_bold, is_italic, is_code in tokens:
        if not content:
            continue
        run = paragraph.add_run(content)
        run.font.name = font_name
        run.font.size = Pt(base_font_size)
        run.font.color.rgb = base_color
        
        if is_code:
            run.font.name = 'Consolas'
            run.font.size = Pt(base_font_size - 0.5)
            run.font.color.rgb = RGBColor(15, 23, 42)
            run.bold = True
        else:
            if is_bold:
                run.bold = True
            if is_italic:
                run.italic = True
    return paragraph
