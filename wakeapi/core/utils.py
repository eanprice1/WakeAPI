import subprocess
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

def run_ssh_command(command: str, timeout: int = 10) -> bool:
    ssh_target = f"{Config.SSH_USER}@{Config.SSH_HOST}"
    try:
        logger.debug(f"Running SSH command: ssh {ssh_target} {command}")
        result = subprocess.run(
            ["ssh", ssh_target, command],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            logger.info(f"SSH command succeeded: {command}")
            return True
        else:
            logger.error(f"SSH command failed: {result.stderr.strip()}")
            return False
    except Exception as e:
        logger.exception(f"Exception running SSH command to {ssh_target}")
        return False
