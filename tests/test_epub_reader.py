import pytest
from backend.services import epub_reader
import os

def test_epub_reader_extract_text():
    sample_path = "data/sample_books/example.epub"
    if not os.path.exists(sample_path):
        pytest.skip("Sample EPUB not found")
    
    text = epub_reader.extract_text_from_epub(sample_path)
    assert isinstance(text, str)
    assert len(text) > 0
