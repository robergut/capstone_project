from docx import Document

def read_profile(path):
    with open(path, 'r') as f:
        text = f.read()
    return text

def read_docx(path):
    document = Document(path)
    text = ""

    for p in document.paragraphs:
        text += f'{p.text.strip()}\n'

    return text

