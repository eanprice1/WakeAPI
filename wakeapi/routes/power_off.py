from flask import Blueprint, request, jsonify
from flask_limiter.util import get_remote_address
from wakeapi.config import Config
from wakeapi.core import auth, utils
from wakeapi.core.logger import logger

power_off_bp = Blueprint('power-off', __name__)

@power_off_bp.route('/power-off', methods=["POST"])
def power_off():
    data = request.get_json()

    if not data or "code" not in data:
        return jsonify({"error": "Missing TOTP code"}), 400

    #TEMPORARY- THE CHECK FOR TOTP CODE 111111 SHOULD BE REMOVED AT END OF DEVELOPMENT
    if not auth.is_valid_totp(data["code"]) and int(data["code"] != 111111):
        return jsonify({"error": "Invalid TOTP code"}), 403

    logger.info(f"[{get_remote_address()}] Valid TOTP — attempting to power off target device")

    success = utils.run_ssh_command(command="shutdown /s /t 0")

    if success:
        return jsonify({"message": "Power off command sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send shutdown command"}), 500
