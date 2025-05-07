import os
import sys
from random import Random

ARITHMETIC_SYMBOLS = [
    '+', '-', '×', '÷', 'π', '√', '∆', '=', '%', '∗', '∝', '∞', '∫', '∬',
    '∮', '∴', '∵', '∼', '≅', '≈', '≠', '≡', '≤', '≥', '≪', '≫', '⊕', '⊗',
    '⊥', '⊤', '∂', '∇', '∃', '∀', '∅', '∈', '∉', '∋', '∌', '∎', '∘', '∙',
    '√', '∛', '∜', '∑', '∏', '∐', '⋈', '⋉', '⋊', '⋋', '⋌', '⋍', '⋎', '⋏',
    '⋒', '⋓', '⌈', '⌉', '⌊', '⌋', '⌲', '⌳', '⌴', '⌵', '⌶', '⌷', '⌸', '⌹',
    '⌺', '⌻', '⌼', '⌽', '⌾', '⌿', '⍀', '⍁', '⍂', '⍃', '⍄', '⍅', '⍆', '⍇',
    '⍈', '⍉', '⍊', '⍋', '⍌', '⍍', '⍎', '⍏', '⍐', '⍑', '⍒', '⍓', '⍔', '⍕',
    '⍖', '⍗', '⍘', '⍙', '⍚', '⍛', '⍜', '⍝', '⍞', '⍟', '⍠', '⍡', '⍢', '⍣',
    '⍤', '⍥', '⍦', '⍧', '⍨', '⍩', '⍪', '⍫', '⍬', '⍭', '⍮', '⍯', '⍰', '⍱',
    '⍲', '⍳', '⍴', '⍵', '⍶', '⍷', '⍸', '⍹', '⍺', '﹢', '﹣', '﹤', '﹥', '﹦',
    '﹨', '﹪', '﹫', '﹬', '﹭', '﹮', '﹯', '＋', '－', '／', '＝', '＼', '～',
    '‖', '∧', '∨', '∩', '∪', '∴', '∵', '∶', '∷', '∼', '∽', '∾', '∿', '≀',
    '≁', '≂', '≃', '≄', '≅', '≆', '≇', '≈', '≉', '≊', '≋', '≌', '≍', '≎',
    '≏', '≐', '≑', '≒', '≓', '≔', '≕', '≖', '≗', '≘', '≙', '≚', '≛', '≜',
    '≝', '≞', '≟', '≠', '≡', '≢', '≣', '≤', '≥', '≦', '≧', '≨', '≩', '≪',
    '≫', '≬', '≭', '≮', '≯', '≰', '≱', '≲', '≳', '≴', '≵', '≶', '≷', '≸',
    '≹', '≺', '≻', '≼', '≽', '≾', '≿', '⊀', '⊁', '⊂', '⊃', '⊄', '⊅', '⊆',
    '⊇', '⊈', '⊉', '⊊', '⊋', '⊌', '⊍', '⊎', '⊏', '⊐', '⊑', '⊒', '⊓', '⊔',
    '⊕', '⊖', '⊗', '⊘', '⊙', '⊚', '⊛', '⊜', '⊝', '⊞', '⊟', '⊠', '⊡', '⊢',
    '⊣', '⊤', '⊥', '⊧', '⊨', '⊩', '⊪', '⊫', '⊬', '⊭', '⊮', '⊯', '⊰', '⊱',
    '⊲', '⊳', '⊴', '⊵', '⊶', '⊷', '⊸', '⊹', '⊺', '⊻', '⊼', '⊽', '⊾', '⊿',
    '⋀', '⋁', '⋂', '⋃', '⋄', '⋅', '⋆', '⋇', '⋈', '⋉', '⋊', '⋋', '⋌', '⋍',
    '⋎', '⋏', '⋐', '⋑', '⋒', '⋓', '⋔', '⋕', '⋖', '⋗', '⋘', '⋙', '⋚', '⋛',
    '⋜', '⋝', '⋞', '⋟', '⋠', '⋡', '⋢', '⋣', '⋤', '⋥', '⋦', '⋧', '⋨', '⋩',
    '⋪', '⋫', '⋬', '⋭', '⋮', '⋯', '⋰', '⋱', '⋲', '⋳', '⋴', '⋵', '⋶', '⋷',
    '⋸', '⋹', '⋺', '⋻', '⋼', '⋽', '⋾', '⋿'
]

DEFAULT_MODE = "xslash"
VALID_MODES = ("xslash", "gibbercipher", "mathsense")

def _get_gibberish_chars():
    chars = []
    chars.extend(chr(i) for i in range(32, 127))    
    chars.extend(chr(i) for i in range(161, 256))   
    chars.extend(chr(i) for i in range(0x2200, 0x2200 + 66))  
    return chars[:256]

def mode(new_mode):
    global DEFAULT_MODE
    if new_mode not in VALID_MODES:
        raise ValueError(f"Invalid mode. Choose from {VALID_MODES}.")
    DEFAULT_MODE = new_mode

def genkey(keyfile):""
    if os.path.exists(keyfile):
        raise FileExistsError(f"Key file {keyfile} already exists. ")
    
    key = os.urandom(32)
    with open(keyfile, 'wb') as f:
        f.write(key)
    
    if os.path.getsize(keyfile) != 32:
        os.remove(keyfile)
        raise ValueError("Failed to generate valid 32-byte key.")

def encrypt(text, keyfile, mode=None):
    mode = mode or DEFAULT_MODE
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}.")
    
    with open(keyfile, 'rb') as f:
        key = f.read()
    
    if len(key) != 32:
        raise ValueError("Invalid key length - must be 32 bytes.")
    
    data = text.encode('utf-8')
    encrypted = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
    
    if mode == "xslash":
        return '/x'.join([''] + [f"{b:02x}" for b in encrypted])
    
    seed = int.from_bytes(key, 'big')
    rng = Random(seed)
    
    if mode == "gibbercipher":
        chars = _get_gibberish_chars()
        rng.shuffle(chars)
        return ''.join([chars[b] for b in encrypted])
    
    if mode == "mathsense":
        symbols = ARITHMETIC_SYMBOLS.copy()
        rng.shuffle(symbols)
        return ''.join([symbols[b] for b in encrypted])

def decrypt(cipher, keyfile, mode=None):
    mode = mode or DEFAULT_MODE
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}.")
    
    with open(keyfile, 'rb') as f:
        key = f.read()
    
    if len(key) != 32:
        raise ValueError("Invalid key length - must be 32 bytes.")
    

    if mode == "xslash":
        parts = cipher.split('/x')[1:]
        data = bytes(int(p, 16) for p in parts)
    else:
        seed = int.from_bytes(key, 'big')
        rng = Random(seed)
        
        if mode == "gibbercipher":
            chars = _get_gibberish_chars()
            rng.shuffle(chars)
            char_map = {c:i for i,c in enumerate(chars)}
        elif mode == "mathsense":
            symbols = ARITHMETIC_SYMBOLS.copy()
            rng.shuffle(symbols)
            char_map = {c:i for i,c in enumerate(symbols)}
        
        try:
            data = bytes([char_map[c] for c in cipher])
        except KeyError as e:
            raise ValueError(f"Invalid {mode} character: {e.args[0]}.")

    decrypted = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
    return decrypted.decode('utf-8')

def version():
    print(f"""
XNUM Cipher Module {__version__}
Platform: {os.name}
Python: {sys.version.split()[0]}
Modes: {', '.join(VALID_MODES)}
""")

def credits():
    print("""
Published by: whotfusests

Repository: https://github.com/whotfusests/xnum
""")

__version__ = "3.1.0"