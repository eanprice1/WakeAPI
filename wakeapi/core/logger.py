import os
import logging
from logging.handlers import RotatingFileHandler
from wakeapi.config import Config

os.makedirs(Config.LOG_DIR, exist_ok=True)

handler = RotatingFileHandler(
    f"{Config.LOG_DIR}/server.log",
    maxBytes=1_000_000,
    backupCount=5
)

handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))

logger = logging.getLogger("wakeonlan")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers if re-imported
if not logger.hasHandlers():
    logger.addHandler(handler)
