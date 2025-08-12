from flask import Flask
from backend.routes.book_routes import book_bp
from backend.routes.voice_routes import voice_bp
from backend.routes.health_check import health_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(book_bp, url_prefix="/books")
app.register_blueprint(voice_bp, url_prefix="/voice")
app.register_blueprint(health_bp, url_prefix="/health")

@app.route("/")
def home():
    return {"message": "Welcome to Voice Assistant Book Reader API"}

if __name__ == "__main__":
    app.run(debug=True)
