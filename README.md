# xnum 🔐

Encryption module for Python with 4 different cipher modes.    
![GitHub forks](https://img.shields.io/github/forks/whotfusests/bfthon?style=social)
![GitHub stars](https://img.shields.io/github/stars/whotfusests/bfthon?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/whotfusests/bfthon?style=social)
![Version](https://img.shields.io/badge/Version-6.0-233572A5?&logo=github&logoColor=white)
[![Made with](https://img.shields.io/badge/language-Python-%233572A5?logo=python&logoColor=white)](https://www.python.org/)


## Installation 📥

1.Using PIP
```bash
pip install https://github.com/whotfusests/xnum/tarball/main
```

2.Visual Installer (Requires Administrator)      
![Installer](https://img.shields.io/github/v/release/whotfusests/xnum?&logo=github&logoColor=white)

## Usage 📀

1.genkey (Generate a key)
```py
# Saved in file
import xnum

xnum.genkey("yourkeyfile.key") # Use .key extension.
# Output in keyfile: V@��i4<u�p���^U��Z^Qܢ0g����^N��V8�
# ---------------------------------------
# Printable
import xnum

xnum.genkey("$printable")
# Output: V@��i4<u�p���^U��Z^Qܢ0g����^N��V8�
```

2.encrypt (Encrypt a string)
```py
# XSLASH Mode
import xnum

enc = xnum.encrypt("Hello!", "yourkeyfile.key/keytoken", "xslash")
print(enc)
# Output: /x98/x80/x8b/x27/xf9/x66
# ---------------------------------------
# GibberCipher Mode
import xnum

enc = xnum.encrypt("Hello!", "yourkeyfile.key/keytoken", "gibbercipher")
print(enc)
# Output: w9J∭Ei
# ---------------------------------------
# MathSense Mode
import xnum

enc = xnum.encrypt("Hello!", "yourkeyfile.key/keytoken", "mathsense")
print(enc)
# Output: ⊣⊡⍪⊵⊋≷
# ---------------------------------------
# NumCrap Mode
import xnum

enc = xnum.encrypt("Hello!", "yourkeyfile.key/keytoken", "numcrap")
print(enc)
# Output: ⅊₄ℏ⑿1⁚
```

3.decrypt (Decrypt a string)
```py
# XSLASH Mode
import xnum

dec = xnum.decrypt("/x98/x80/x8b/x27/xf9/x66", "yourkeyfile.key/keytoken", "xslash")
print(dec)
# Output: Hello!
# ---------------------------------------
# GibberCipher Mode
import xnum

dec = xnum.decrypt("w9J∭Ei", "yourkeyfile.key/keytoken", "gibbercipher")
print(dec)
# Output: Hello!
# ---------------------------------------
# MathSense Mode
import xnum

dec = xnum.decrypt("⊣⊡⍪⊵⊋≷", "yourkeyfile.key/keytoken", "mathsense")
print(dec)
# Output: Hello!
# ---------------------------------------
# NumCrap Mode
import xnum

dec = xnum.decrypt("⅊₄ℏ⑿1⁚", "yourkeyfile.key/keytoken", "numcrap")
print(dec)
# Output: Hello!
```

4.version (Show xnum version)
```py
import xnum

xnum.version()
```

5.credits (Show xnum credits)
```py
import xnum

xnum.credits()
```

### Made with <3 by whotfusests
