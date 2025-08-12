import pytest
from backend.services import speech_to_text
import os

def test_speech_to_text_transcription():
    sample_path = "data/output_audio/example.mp3"
    if not os.path.exists(sample_path):
        pytest.skip("Sample audio not found")
    
    transcript = speech_to_text.transcribe_audio(sample_path)
    assert isinstance(transcript, str)
