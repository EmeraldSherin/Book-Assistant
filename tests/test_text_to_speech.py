import pytest
from backend.services import text_to_speech

def test_text_to_speech_generation(tmp_path):
    text = "Hello world, this is a test."
    output_file = tmp_path / "output.mp3"
    
    text_to_speech.generate_tts(text, str(output_file))
    
    assert output_file.exists()
    assert output_file.stat().st_size > 0
