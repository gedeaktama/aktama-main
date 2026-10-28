# -*- coding: utf-8 -*-
import re

def parse_inline_markdown(text):
    """
    Parses a string with inline markdown:
    ***bold italic***, **bold**, *italic*, `code`, and plain text.
    Returns a list of tuples: (text_content, is_bold, is_italic, is_code)
    """
    pattern = re.compile(r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`.*?`|[^*`]+)')
    tokens = pattern.findall(text)
    runs = []
    for token in tokens:
        if token.startswith('***') and token.endswith('***') and len(token) >= 6:
            runs.append((token[3:-3], True, True, False))
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            runs.append((token[2:-2], True, False, False))
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            runs.append((token[1:-1], False, True, False))
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            runs.append((token[1:-1], False, False, True))
        else:
            runs.append((token, False, False, False))
    return runs

# Test cases
sample = "**Erik:** Teman kita yang *penuh semangat*, menggunakan `[move 10 steps]` dan ***berpikir kritis***!"
parsed = parse_inline_markdown(sample)
for r in parsed:
    print(r)
