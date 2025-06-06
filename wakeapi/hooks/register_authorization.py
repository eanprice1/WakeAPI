from flask import request, jsonify
from wakeapi.config import Config

def register_authorization(app):
    @app.before_request
    def authenticate():
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401

        provided_key = auth_header.split("Bearer ")[1].strip()
        if provided_key != Config.API_KEY:
            return jsonify({"error": "Invalid API key"}), 401
