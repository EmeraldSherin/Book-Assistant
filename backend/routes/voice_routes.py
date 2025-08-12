from flask import Blueprint, request, jsonify
from backend.services.text_to_speech import text_to_speech_service
from backend.services.speech_to_text import speech_to_text_service

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/tts", methods=["POST"])
def text_to_speech():
    data = request.get_json()
    text = data.get("text", "")
    output_path = data.get("output_path", "data/output_audio/output.mp3")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        text_to_speech_service(text, output_path)
        return jsonify({"message": "Audio file generated", "path": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@voice_bp.route("/stt", methods=["POST"])
def speech_to_text():
    file = request.files.get("audio")
    if not file:
        return jsonify({"error": "No audio file uploaded"}), 400

    try:
        text = speech_to_text_service(file)
        return jsonify({"transcribed_text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
