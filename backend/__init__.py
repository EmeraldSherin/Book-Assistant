from flask import Flask
from routes import routes_bp
from utils.file_utils import ensure_upload_folder

def create_app():
    app = Flask(__name__)
    ensure_upload_folder()

    # Register routes
    app.register_blueprint(routes_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
