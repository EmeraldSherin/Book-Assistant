import os
from dotenv import load_dotenv

load_dotenv()

# Basic config
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
ALLOWED_EXTENSIONS = {".pdf", ".epub", ".mp3", ".wav"}
