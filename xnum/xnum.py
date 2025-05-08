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

NUMBER_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '²', '³', '¹', '⁰', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹',
    '½', '⅓', '⅔', '¼', '¾', '⅛', '⅜', '⅝', '⅞', '⅕',
    '⅖', '⅗', '⅘', '⅙', '⅚', '‰', '‱', '⁐', '⁒', '₀',
    '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '⓪',
    '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩',
    '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳',
    '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⑽',
    '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒇',
    '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⒑',
    '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛',
    '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾',
    '❿', '⁖', '⁗', '⁘', '⁙', '⁚', '⁛', '⁜', '⁝', '⁞',
    '₠', '₡', '₢', '₣', '₤', '₥', '₦', '₧', '₨', '₩',
    '₪', '₫', '€', '₭', '₮', '₯', '₰', '₱', '₲', '₳',
    '₴', '₵', '₶', '₷', '₸', '₹', '₺', '₻', '₼', '₽',
    '₾', '₿', '℀', '℁', 'ℂ', '℃', '℄', '℅', '℆', 'ℇ',
    '℈', '℉', 'ℊ', 'ℋ', 'ℌ', 'ℍ', 'ℎ', 'ℏ', 'ℐ', 'ℑ',
    'ℒ', 'ℓ', '℔', 'ℕ', '№', '℗', '℘', 'ℙ', 'ℚ', 'ℛ',
    'ℜ', 'ℝ', '℞', '℟', '℠', '℡', '™', '℣', 'ℤ', '℥',
    'Ω', '℧', 'ℨ', '℩', 'K', 'Å', 'ℬ', 'ℭ', '℮', 'ℯ',
    'ℰ', 'ℱ', 'ℳ', 'ℴ', 'ℵ', 'ℶ', 'ℷ', 'ℸ', 'ℹ', '℺',
    '℻', 'ℼ', 'ℽ', 'ℾ', 'ℿ', '⅀', '⅁', '⅂', '⅃', '⅄',
    'ⅅ', 'ⅆ', 'ⅇ', 'ⅈ', 'ⅉ', '⅊', '⅋', '⅌', '⅍', 'ⅎ',
    '⅏', '⅐', '⅑', '⅒', '⅓', '⅔', '⅕', '⅖', '⅗', '⅘',
    '⅙', '⅚', '⅛', '⅜', '⅝', '⅞', '⅟', 'ↀ', 'ↁ', 'ↂ',
    'Ↄ', 'ↄ', 'ↅ', 'ↆ', 'ↇ', 'ↈ', '↉'
]

DEFAULT_MODE = "xslash"
VALID_MODES = ("xslash", "gibbercipher", "mathsense","numcrap")

def _get_gibberish_chars():
    chars = []
    chars.extend(chr(i) for i in range(32, 127))    
    chars.extend(chr(i) for i in range(161, 256))   
    chars.extend(chr(i) for i in range(0x2200, 0x2200 + 66))  
    return chars[:256]

def mode(new_mode):
    global DEFAULT_MODE
    if new_mode not in VALID_MODES:
        raise ValueError(f"Invalid mode. Choose from {VALID_MODES}")
    DEFAULT_MODE = new_mode

def genkey(keyfile):
    if os.path.exists(keyfile):
        raise FileExistsError(f"Key file {keyfile} already exists")
    
    key = os.urandom(32)
    with open(keyfile, 'wb') as f:
        f.write(key)
    
    if os.path.getsize(keyfile) != 32:
        os.remove(keyfile)
        raise ValueError("Failed to generate valid 32-byte key")

def encrypt(text, keyfile, mode=None):
    mode = mode or DEFAULT_MODE
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}")
    
    with open(keyfile, 'rb') as f:
        key = f.read()
    
    if len(key) != 32:
        raise ValueError("Invalid key length - must be 32 bytes")
    
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

    if mode == "numcrap":
        symbols = NUMBER_SYMBOLS.copy()
        rng.shuffle(symbols)
        return ''.join([symbols[b] for b in encrypted])
        
def decrypt(cipher, keyfile, mode=None):
    mode = mode or DEFAULT_MODE
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}")
    
    with open(keyfile, 'rb') as f:
        key = f.read()
    
    if len(key) != 32:
        raise ValueError("Invalid key length - must be 32 bytes")
    
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
            raise ValueError(f"Invalid {mode} character: {e.args[0]}")
        elif mode == "numcrap":
        symbols = NUMBER_SYMBOLS.copy()
        rng.shuffle(symbols)
        char_map = {c:i for i,c in enumerate(symbols)}
        try:
            data = bytes([char_map[c] for c in cipher])
        except KeyError as e:
            raise ValueError(f"Invalid numcipher symbol: {e.args[0]}")

    decrypted = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
    return decrypted.decode('utf-8')

def version():
    print(f"""
XNUM Cipher v{__version__}
OS: {os.name}
Python: {sys.version.split()[0]}
Key Size: 32 bytes
Modes: {', '.join(VALID_MODES)}
""")

def credits():
    print("""
Published by: whotfusests

Repository: https://github.com/whotfusests/xnum
""")

__version__ = "4.0"