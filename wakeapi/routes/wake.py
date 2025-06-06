from flask import Blueprint, request, jsonify
from flask_limiter.util import get_remote_address
from wakeapi.config import Config
from wakeapi.core import auth, utils
from wakeapi.core.logger import logger

wake_bp = Blueprint('wake', __name__)

@wake_bp.route('/wake', methods=["POST"])
def wake():
    data = request.get_json()

    if not data or "code" not in data:
        return jsonify({"error": "Missing TOTP code"}), 400

    if not auth.is_valid_totp(data["code"]):
        return jsonify({"error": "Invalid TOTP code"}), 403

    logger.info(f"[{get_remote_address()}] Valid TOTP — attempting to send magic packet")

    if utils.wake_target(Config.TARGET_MAC_ADDRESS):
        logger.info(f"[{get_remote_address()}] Magic packet sent successfully")
        return jsonify({"message": "Magic packet sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send magic packet"}), 500
