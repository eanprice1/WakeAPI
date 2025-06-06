from wakeonlan import send_magic_packet
from wakeapi.core.logger import logger
from wakeapi.config import Config

def wake_target(mac_address: str) -> bool:
    success = False
    for i in range(Config.MAGIC_PACKET_COUNT):
        try:
            send_magic_packet(mac_address)
            success = True
        except Exception as e:
            logger.error(f"Attempt {i + 1} failed to send magic packet: {e}")
    return success
