import os
import base64
from random import Random

_default_mode = "xslash"

os = os.name() 
py = os.system("python3 --version")

def _get_gibberish_chars():
    chars = []
    chars.extend(chr(i) for i in range(32, 127))
    chars.extend(chr(i) for i in range(161, 256))
    chars.extend(chr(i) for i in range(0x2200, 0x2200 + 66))
    return chars[:256]  

def mode(new_mode):
    global _default_mode
    if new_mode not in ("xslash", "gibbercipher"):
        raise ValueError("Invalid mode. Choose 'xslash' or 'gibbercipher'.")
    _default_mode = new_mode

def genkey(keyfile):
    key = os.urandom(32)
    with open(keyfile, 'wb') as f:
        f.write(key)

def encrypt(code, keyfile, mode=None):
    if mode is None:
        mode = _default_mode
    
    with open(keyfile, 'rb') as f:
        key = f.read()
    
    code_bytes = code.encode('utf-8')
    encrypted_bytes = bytes([code_byte ^ key[i % len(key)] for i, code_byte in enumerate(code_bytes)])

    if mode == "xslash":
        cipher = ''.join(f'/x{byte:02x}' for byte in encrypted_bytes)
    elif mode == "gibbercipher":
        chars = _get_gibberish_chars()
        rng = Random(key)
        shuffled = chars.copy()
        rng.shuffle(shuffled)
        cipher = ''.join(shuffled[byte] for byte in encrypted_bytes)
    else:
        raise ValueError(f"Invalid mode: {mode}")
    
    return cipher

def decrypt(cipher, keyfile, mode=None):
    if mode is None:
        mode = _default_mode
    
    with open(keyfile, 'rb') as f:
        key = f.read()

    if mode == "xslash":
        parts = cipher.split('/x')[1:]
        encrypted_bytes = bytes(int(part, 16) for part in parts)
    elif mode == "gibbercipher":
        chars = _get_gibberish_chars()
        rng = Random(key)
        shuffled = chars.copy()
        rng.shuffle(shuffled)
        char_map = {char: idx for idx, char in enumerate(shuffled)}
        encrypted_bytes = bytes(char_map[c] for c in cipher)
    else:
        raise ValueError(f"Invalid mode: {mode}")
    
    decrypted_bytes = bytes([encrypted_byte ^ key[i % len(key)] for i, encrypted_byte in enumerate(encrypted_bytes)])
    return decrypted_bytes.decode('utf-8')

def version():
    print(f"""
XNUM Version: 2.0 - https://whotfusests.github.io/xnum/
OS: {os}
""")

def credits():
    print("Credits: whotfusests on GitHub")
