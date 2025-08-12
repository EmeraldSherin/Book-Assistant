# services/pdf_reader.py
import PyPDF2

def read_pdf(file_path):
    """
    Extract text from a PDF file.
    :param file_path: Path to PDF.
    :return: Extracted text as string.
    """
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text
