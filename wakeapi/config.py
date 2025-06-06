import os

class Config:
    TOTP_SECRET = os.environ.get("WAKEAPI_TOTP_SECRET", "")
    TARGET_MAC_ADDRESS = os.environ.get("WAKEAPI_TARGET_MAC", "")
    API_KEY = os.environ.get("WAKEAPI_API_KEY", "")
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

        if missing:
            raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")