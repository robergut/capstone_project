from docx import Document
import os

url = './resources/{0}'

def read_profile(file):
    path = os.path.abspath(url.format(file))
    with open(path, 'r') as f:
        text = f.read()
    return text

def read_docx(file):
    path = os.path.abspath(url.format(file))
    document = Document(path)
    text = ""

    for p in document.paragraphs:
        text += f'{p.text.strip()}\n'

    return text

