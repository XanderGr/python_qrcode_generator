### QR Code Generator for OTP Authentication

#### Code (`qrcode_generator.py`):

import os
import base64
import qrcode

# Step 1: Generate a Secret Key
secret_key = base64.b32encode(os.urandom(10)).decode('utf-8')
print(f"Secret Key: {secret_key}")

# Step 2: Encode the Key
service_name = "YourService"
user_email = "YourEmail"
issuer_name = "YourIssuer"
otpauth_uri = f"otpauth://totp/{service_name}:{user_email}?secret={secret_key}&issuer={issuer_name}"

# Step 3: Create the QR Code
qr = qrcode.make(otpauth_uri)
qr.save("otp_qrcode.png")