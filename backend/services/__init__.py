# backend/services/__init__.py

"""
Services package initializer.
This file ensures that the 'services' folder is treated as a Python package.
You can import specific service functions from here if needed.
"""

# Example: if you have modules like text_processing.py, translation.py, etc.
from .text_processing import process_text
from .translation import translate_text
from .voice_assistant import handle_voice_query

__all__ = [
    "process_text",
    "translate_text",
    "handle_voice_query"
]
