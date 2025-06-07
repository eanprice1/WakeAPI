import os

class Config:
    TOTP_SECRET = os.environ.get("WAKEAPI_TOTP_SECRET", "")
    TARGET_MAC_ADDRESS = os.environ.get("WAKEAPI_TARGET_MAC", "")
    API_KEY = os.environ.get("WAKEAPI_API_KEY", "")
    SSH_USER = os.environ.get("WAKEAPI_SSH_USER", "")
    SSH_HOST = os.environ.get("WAKEAPI_SSH_HOST", "")
    LOG_DIR = os.environ.get("WAKEAPI_LOG_DIR", "logs")
    MAGIC_PACKET_COUNT = int(os.environ.get("MAGIC_PACKET_COUNT", 1))

    @classmethod
    def validate(cls):
        missing = []
        if not cls.TOTP_SECRET:
            missing.append("WAKEAPI_TOTP_SECRET")
        if not cls.TARGET_MAC_ADDRESS:
            missing.append("WAKEAPI_TARGET_MAC")
        if not cls.API_KEY:
            missing.append("WAKEAPI_API_KEY")
        if not cls.SSH_USER:
            missing.append("WAKEAPI_SSH_USER")
        if not cls.SSH_HOST:
            missing.append("WAKEAPI_SSH_HOST")

        if missing:
            raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")