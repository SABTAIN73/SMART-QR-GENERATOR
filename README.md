# Smart QR Generator

A Python QR code generator that detects your input type automatically. One input, right QR.

## How it works

Type anything, the program figures out what it is:

| Input | Detected as |
|-------|-------------|
| `https://google.com` | URL |
| `www.google.com` | URL |
| `someone@example.com` | Email |
| `+923001234567` | Phone |
| `WIFI:T:WPA;S:Home;P:1234;;` | WiFi |
| `Hello there` | Text |

URLs get `https://` added if missing. Emails get `mailto:`, phones get `tel:`.

## Setup

Install:

    pip install qrcode[pil]

Run:

    python QR_CODE.py

It asks for your data, size, and border. QR saves as `qr_code.png` and opens automatically.

## WiFi format

WiFi needs the password and security type, so it uses this format:

    WIFI:T:WPA;S:NetworkName;P:Password;;

- **T** — security type (`WPA`, `WEP`, `nopass`)
- **S** — network name
- **P** — password

Example:

    WIFI:T:WPA;S:MyHomeWiFi;P:mypassword123;;

## Tech stack

- Python 3
- `qrcode` — QR generation
- `re` — input detection
- `Pillow` — image handling

## What's next

- Custom filename
- Batch generation
- GUI version
- Colored QR codes

## Author

SABTAIN
