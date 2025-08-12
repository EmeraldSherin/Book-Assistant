import pytest
from backend.services import pdf_reader
import os

def test_pdf_reader_extract_text():
    sample_path = "data/sample_books/example.pdf"
    if not os.path.exists(sample_path):
        pytest.skip("Sample PDF not found")
    
    text = pdf_reader.extract_text_from_pdf(sample_path)
    assert isinstance(text, str)
    assert len(text) > 0
