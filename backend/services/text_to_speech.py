# services/text_to_speech.py
from gtts import gTTS
import os
import uuid

def text_to_speech(text, lang="en", output_dir="output_audio"):
    """
    Convert text to speech and save as MP3.
    :param text: String of text to convert.
    :param lang: Language code (default 'en').
    :param output_dir: Directory to save audio.
    :return: Path to saved MP3 file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(output_dir, file_name)

    tts = gTTS(text=text, lang=lang)
    tts.save(file_path)

    return file_path
