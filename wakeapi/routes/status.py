from flask import Blueprint, jsonify, request
from flask_limiter.util import get_remote_address
from wakeapi.core.logger import logger

from wakeapi.core.utils import is_port_open

status_bp = Blueprint('status', __name__)

@status_bp.route("/status", methods=["GET"])
def status():
    ip = get_remote_address()
    target_port = 22

    #temporary
    ip_remote = request.remote_addr
    ip_forwarded = request.headers.get("X-Forwarded-For", "N/A")
    ip_limiter = get_remote_address()

    # Log all headers
    logger.info("Request headers:\n" + "\n".join(f"{k}: {v}" for k, v in request.headers.items()))

    logger.info(
        f"[status] IP check: remote_addr={ip_remote}, "
        f"X-Forwarded-For={ip_forwarded}, limiter_addr={ip_limiter}"
    )

    logger.info(f"[{ip}] Checking PC online status via TCP port {target_port}")

    online = is_port_open(target_port)

    return jsonify({
        "pc_online": online
    }), 200
