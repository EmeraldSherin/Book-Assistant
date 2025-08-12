# backend/routes/__init__.py
from flask import Blueprint

# Create a blueprint for all routes
routes_bp = Blueprint("routes", __name__)

# Import and register route files
from .book_routes import book_bp
from .voice_routes import voice_bp
from .health_check import health_bp

# Register blueprints
routes_bp.register_blueprint(book_bp, url_prefix="/books")
routes_bp.register_blueprint(voice_bp, url_prefix="/voice")
routes_bp.register_blueprint(health_bp, url_prefix="/health")
