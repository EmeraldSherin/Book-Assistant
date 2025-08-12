# API Documentation

## Endpoints

### 1. `/api/convert/pdf-to-audio`
- **Method:** POST  
- **Description:** Converts a PDF file to speech and returns audio file.  
- **Request Body:**  
    - `file`: PDF file (multipart/form-data)  
- **Response:** MP3 file download URL.

### 2. `/api/convert/epub-to-audio`
- **Method:** POST  
- **Description:** Converts an EPUB file to speech.  
- **Request Body:**  
    - `file`: EPUB file  
- **Response:** MP3 file URL.

### 3. `/api/speech-to-text`
- **Method:** POST  
- **Description:** Converts speech in an audio file to text.  
- **Request Body:**  
    - `file`: Audio file (WAV/MP3)  
- **Response:** JSON text output.
