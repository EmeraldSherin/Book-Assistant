# services/speech_to_text.py
import speech_recognition as sr

def speech_to_text(audio_path):
    """
    Convert speech audio to text.
    :param audio_path: Path to audio file (.wav recommended).
    :return: Transcribed text.
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "Speech recognition service unavailable."
