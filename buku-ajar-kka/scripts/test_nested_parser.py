# -*- coding: utf-8 -*-
import re

def clean_latex_symbols(text):
    text = text.replace(r'$\checkmark$', '✓')
    text = text.replace(r'$\times$', '✗')
    text = text.replace(r'\checkmark', '✓')
    text = text.replace(r'\times', '✗')
    return text

def parse_inline_markdown(text):
    text = clean_latex_symbols(text)
    
    # Split by code blocks `...`
    pattern = re.compile(r'(`[^`]+`|[#~]+|[^`]+)')
    
    # We can use a tokenizer approach:
    # 1. Match code: `...`
    # 2. Match bold-italic: ***...***
    # 3. Match bold: **...** (which might contain inner *italic*)
    # 4. Match italic: *...*
    
    # Regex that matches tokens
    # Group 1: code `...`
    # Group 2: bold-italic ***...***
    # Group 3: bold **...**
    # Group 4: italic *...*
    # Group 5: plain text
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
                if '*' in bold_content:
                    # Parse inner italic inside bold
                    sub_spec = re.compile(r'(\*(?P<it>[^*]+?)\*)|(?P<pt>[^*]+)')
                    s_pos = 0
                    while s_pos < len(bold_content):
                        sm = sub_spec.match(bold_content, s_pos)
                        if sm:
                            if sm.group('it'):
                                results.append((sm.group('it'), True, True, False))
                            else:
                                results.append((sm.group('pt'), True, False, False))
                            s_pos = sm.end()
                        else:
                            results.append((bold_content[s_pos:].replace('*', ''), True, False, False))
                            break
                else:
                    results.append((bold_content, True, False, False))
            elif m.group('italic'):
                results.append((m.group('italic'), False, True, False))
            elif m.group('plain'):
                plain_txt = m.group('plain').replace('*', '')
                if plain_txt:
                    results.append((plain_txt, False, False, False))
            pos = m.end()
        else:
            # Fallback single char
            ch = text[pos]
            if ch != '*':
                results.append((ch, False, False, False))
            pos += 1
            
    return results

sample = "Buku Teks Pelajaran ini disusun dengan pendekatan **Pembelajaran Mendalam (*Deep Learning*)** yang berkesadaran."
tokens = parse_inline_markdown(sample)
for t in tokens:
    print(t)
