import os

# Base data folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

# Paths for sample books and output audio
SAMPLE_BOOKS_DIR = os.path.join(BASE_DIR, "sample_books")
OUTPUT_AUDIO_DIR = os.path.join(BASE_DIR, "output_audio")

# Example files
PDF_SAMPLE_PATH = os.path.join(SAMPLE_BOOKS_DIR, "example.pdf")
EPUB_SAMPLE_PATH = os.path.join(SAMPLE_BOOKS_DIR, "example.epub")

# Ensure output folder exists
os.makedirs(OUTPUT_AUDIO_DIR, exist_ok=True)

def get_sample_file(file_type="pdf"):
    """Return path to sample file."""
    if file_type.lower() == "pdf":
        return PDF_SAMPLE_PATH
    elif file_type.lower() == "epub":
        return EPUB_SAMPLE_PATH
    else:
        raise ValueError("Unsupported file type")

def get_output_path(filename="output.mp3"):
    """Return path to save generated audio."""
    return os.path.join(OUTPUT_AUDIO_DIR, filename)
