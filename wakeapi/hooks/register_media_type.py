from flask import request, jsonify

def register_media_type(app):
    @app.before_request
    def enforce_json_for_post():
        if request.method == "POST" and request.content_type != "application/json":
            return jsonify({"error": "Request must be JSON"}), 415
