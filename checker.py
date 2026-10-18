
import requests
import sys

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Forces browsers to use HTTPS",
    "Content-Security-Policy": "Blocks malicious scripts from running",
    "X-Frame-Options": "Stops other sites embedding this page (clickjacking)",
    "X-Content-Type-Options": "Stops browsers guessing file types",
    "Referrer-Policy": "Controls what info is shared when users click links",
}

url = sys.argv[1]
response = requests.get(url, timeout=10)

print("Checking:", url)
for header, purpose in SECURITY_HEADERS.items():
    if header in response.headers:
        print("[PASS]", header)
    else:
        print("[MISSING]", header, "-", purpose)

