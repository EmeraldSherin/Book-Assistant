# services/epub_reader.py
from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub(file_path):
    """
    Extract text from an EPUB file.
    :param file_path: Path to EPUB.
    :return: Extracted text as string.
    """
    book = epub.read_epub(file_path)
    text = ""

    for item in book.get_items():
        if item.get_type() == epub.EpubHtml:
            soup = BeautifulSoup(item.content, "html.parser")
            text += soup.get_text()

    return text
