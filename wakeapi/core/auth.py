import pyotp
from wakeapi.config import Config

def is_valid_totp(code: str) -> bool:
    totp = pyotp.TOTP(Config.TOTP_SECRET)
    return totp.verify(code, valid_window=1)
