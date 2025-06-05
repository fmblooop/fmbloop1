import os
import re
from typing import Dict

try:
    from PyPDF2 import PdfReader
except ImportError:  # pragma: no cover
    PdfReader = None

def extract_text(file_path: str) -> str:
    """Extract text from a PDF or text file."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        if PdfReader is None:
            raise ImportError('PyPDF2 is required to read PDF files.')
        reader = PdfReader(file_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text() or '')
        return '\n'.join(text)
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

def parse_sections(text: str) -> Dict[str, str]:
    """Parse the text for sections: Exceptions, Requirements, Mortgage Schedule."""
    sections = {'exceptions': '', 'requirements': '', 'mortgage_schedule': ''}
    patterns = {
        'exceptions': re.compile(r'\bexceptions?\b', re.IGNORECASE),
        'requirements': re.compile(r'\brequirements?\b', re.IGNORECASE),
        'mortgage_schedule': re.compile(r'\bmortgage schedule\b', re.IGNORECASE),
    }
    # Sort keys by position of first occurrence
    positions = {}
    for key, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            positions[key] = match.start()
    if not positions:
        return sections
    # Sort keys by position and append end position as next start or end of text
    keys_sorted = sorted(positions.items(), key=lambda x: x[1])
    keys_sorted.append(('end', len(text)))
    for (key, start), (next_key, next_start) in zip(keys_sorted, keys_sorted[1:]):
        if key == 'end':
            continue
        sections[key] = text[start:next_start].strip()
    return sections

def extract_sections(file_path: str) -> Dict[str, str]:
    text = extract_text(file_path)
    return parse_sections(text)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Parse title insurance document.')
    parser.add_argument('file', help='Path to PDF or text file')
    args = parser.parse_args()

    sections = extract_sections(args.file)
    for name, content in sections.items():
        print(f'--- {name.upper()} ---')
        print(content)
        print()
