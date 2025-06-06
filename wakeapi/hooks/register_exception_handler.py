from flask import request, jsonify
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException
from wakeapi.core.logger import logger

def register_exception_handler(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({"error": e.name}), e.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        ip = get_remote_address()
        logger.exception(f"[{ip}] Unhandled exception during {request.method} {request.path}")
        return jsonify({"error": "Internal server error"}), 500
