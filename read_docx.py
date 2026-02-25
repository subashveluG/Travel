import zipfile
import xml.etree.ElementTree as ET
import sys

def read_docx(path):
    with zipfile.ZipFile(path) as docx:
        tree = ET.fromstring(docx.read('word/document.xml'))
    
    text = []
    for node in tree.iter():
        if node.tag.endswith('}t'):
            if node.text:
                text.append(node.text)
    return '\n'.join(text)

try:
    print(read_docx(sys.argv[1]))
except Exception as e:
    print(e)
