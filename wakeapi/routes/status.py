from flask import Blueprint, jsonify, request
from flask_limiter.util import get_remote_address
from wakeapi.core.logger import logger

from wakeapi.core.utils import is_port_open

status_bp = Blueprint('status', __name__)

@status_bp.route("/status", methods=["GET"])
def status():
    ip = get_remote_address()
    target_port = 22

    logger.info(f"[{ip}] Checking PC online status via TCP port {target_port}")

    online = is_port_open(target_port)

    return jsonify({
        "pc_online": online
    }), 200
