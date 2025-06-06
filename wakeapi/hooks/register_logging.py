import json
from flask import request
from flask_limiter.util import get_remote_address
from wakeapi.core.logger import logger

def register_logging(app):
    @app.after_request
    def log_errors(response):
        ip = get_remote_address()
        if response.status_code >= 400:
            try:
                data = response.get_data(as_text=True)
                parsed = json.loads(data)
                error_msg = parsed.get("error", "<no 'error' field>")
            except Exception:
                error_msg = "<unable to parse error message>"

            logger.warning(f"[{ip}] {request.method} {request.path} -> {response.status_code} | Error: {error_msg}")
        return response
