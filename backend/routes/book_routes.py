from flask import Blueprint, request, jsonify
from backend.services.pdf_reader import read_pdf
from backend.services.epub_reader import read_epub

book_bp = Blueprint("books", __name__)

@book_bp.route("/pdf", methods=["POST"])
def process_pdf():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No PDF file uploaded"}), 400
    try:
        text = read_pdf(file)
        return jsonify({"content": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@book_bp.route("/epub", methods=["POST"])
def process_epub():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No EPUB file uploaded"}), 400
    try:
        text = read_epub(file)
        return jsonify({"content": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
