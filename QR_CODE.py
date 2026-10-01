# ======QR CODE GENERATOR======

import qrcode
import re

def detect_type(data):
    data = data.strip()

    if data.upper().startswith("WIFI:"):
        return "WIFI"

    if re.match(r"^https?://", data, re.IGNORECASE) or re.match(r"^www\.", data, re.IGNORECASE):
        return "URL"
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", data):
        return "EMAIL"
    if re.match(r"^\+\d{10,15}$", data):
        return "PHONE"

    return "TEXT"
# >>>>>>>>>>>>>>>>>>>>>>>
def format_data(data, dtype):
    data = data.strip()

    if dtype == "URL":
        if data.startswith("http://") or data.startswith("https://"):
            return data
        else:
            return "https://" + data

    if dtype == "EMAIL":
        return "mailto:" + data

    if dtype == "PHONE":
        return "tel:" + data

    return data

# >>>>>>>>>>>>>>>>>>>>>

data = input("ENTER SOMTHING TO GENERATE QRCODE:")
dtype = detect_type(data)
print(f"Detected: {dtype}")
formatted= format_data(data , dtype)

size = int(input("ENTER THE SIZE OF THE QR CODE:"))
border = int(input("ENTER THE BORDER SIZE OF THE QR CODE:"))
qr = qrcode.QRCode(
    version = 4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size  = size,
    border = border,
    
)
qr.add_data(formatted)
qr.make(fit=True)

img =qr.make_image()
img.save("qr_code.png")
img.show()

print("QR CODE GENERATED SUCCESSFULLY AND SAVED AS qr_code.png!")



