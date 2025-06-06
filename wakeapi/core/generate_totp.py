import pyotp
import qrcode

TOTP_ISSUER = "WakeAPI"
TOTP_NAME = "Eans_PC@raspberrypi"
QR_CODE_FILENAME = "WakeAPI_TOTP_QR.png"

secret = pyotp.random_base32()
print("TOTP Secret:", secret)

uri = pyotp.TOTP(secret).provisioning_uri(name=TOTP_NAME, issuer_name=TOTP_ISSUER)
qr = qrcode.make(uri)
qr.save(QR_CODE_FILENAME)
print(f"QR code saved as {QR_CODE_FILENAME}. Scan it with your authenticator app.")