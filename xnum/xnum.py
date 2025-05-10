import os
import sys
from random import Random

arithmetic_symbols = [
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

number_symbols = [
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

EMPTYSPACE_SYMBOLS = [
    '\u0020', '\u00A0', '\u1680', '\u2000', '\u2001', '\u2002',
    '\u2003', '\u2004', '\u2005', '\u2006', '\u2007', '\u2008',
    '\u2009', '\u200A', '\u202F', '\u205F', '\u3000', '\uFEFF'
]

VALID_MODES = ("xslash", "gibbercipher", "mathsense", "numcrap", "emptyspace")
DEFAULT_MODE = "xslash"
__version__ = "6.0"

def _get_gibberish_chars():
    chars = []
    chars.extend(chr(i) for i in range(32, 127))    
    chars.extend(chr(i) for i in range(161, 256))
    chars.extend(chr(i) for i in range(0x2200, 0x2200 + 66))
    return chars[:256]

def _get_emptyspace_chars():
    return (EMPTYSPACE_SYMBOLS * 15)[:256]

def _parse_key_input(key_input):
    if isinstance(key_input, str) and len(key_input) == 64:
        try:
            return bytes.fromhex(key_input)
        except ValueError:
            pass
    
    try:
        with open(key_input, 'rb') as f:
            key = f.read()
        if len(key) != 32:
            raise ValueError("Invalid key length - must be 32 bytes")
        return key
    except Exception as e:
        raise ValueError(f"Invalid key input: {str(e)}")

def genkey(keyfile):
    if keyfile == "$printable":
        key = os.urandom(32)
        print(f"PRINTABLE KEY (hex): {key.hex()}")
        return
    
    dir_path = os.path.dirname(keyfile)
    if dir_path: 
        os.makedirs(dir_path, exist_ok=True)
    
    if os.path.exists(keyfile):
        raise FileExistsError(f"Key file {keyfile} already exists")
    
    key = os.urandom(32)
    with open(keyfile, 'wb') as f:
        f.write(key)
    
    if os.path.getsize(keyfile) != 32:
        os.remove(keyfile)
        raise ValueError("Failed to generate valid 32-byte key")

def encrypt(text, key_input, mode=DEFAULT_MODE):
    key = _parse_key_input(key_input)
    
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}. Valid: {VALID_MODES}")
    
    data = text.encode('utf-8')
    encrypted = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
    
    if mode == "xslash":
        return '/x'.join([''] + [f"{b:02x}" for b in encrypted])
    

    seed = int.from_bytes(key, 'big')
    rng = Random(seed
    if mode == "gibbercipher":
        symbols = _get_gibberish_chars()
    elif mode == "mathsense":
        symbols = ARITHMETIC_SYMBOLS.copy()
    elif mode == "numcrap":
        symbols = NUMBER_SYMBOLS.copy()
    elif mode == "emptyspace":
        symbols = _get_emptyspace_chars()
    
    rng.shuffle(symbols)
    return ''.join([symbols[b] for b in encrypted])

def decrypt(cipher, key_input, mode=DEFAULT_MODE):
    key = _parse_key_input(key_input)
    
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}. Valid: {VALID_MODES}")
    
    if mode == "xslash":
        parts = cipher.split('/x')[1:]
        data = bytes(int(p, 16) for p in parts)
    else:
        seed = int.from_bytes(key, 'big')
        rng = Random(seed)
        
        if mode == "gibbercipher":
            symbols = _get_gibberish_chars()
        elif mode == "mathsense":
            symbols = ARITHMETIC_SYMBOLS.copy()
        elif mode == "numcrap":
            symbols = NUMBER_SYMBOLS.copy()
        elif mode == "emptyspace":
            symbols = _get_emptyspace_chars()
        
        rng.shuffle(symbols)
        symbol_map = {char: idx for idx, char in enumerate(symbols)}
        
        try:
            data = bytes([symbol_map[c] for c in cipher])
        except KeyError as e:
            raise ValueError(f"Invalid {mode} character: {e.args[0]}")

    decrypted = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
    return decrypted.decode('utf-8')

def version():
    print(f"""
XNUM Cipher Module v{__version__}
Platform: {os.name}
Python: {sys.version.split()[0]}
Key Format: 32-byte hex or key file.
Valid Modes: {', '.join(VALID_MODES)}
""")

def credits():
    print("""
Developer: whotfusests

Repository: https://github.com/whotfusests/xnum
""")

def set_default_mode(mode):
    global DEFAULT_MODE
    if mode not in VALID_MODES:
        raise ValueError(f"Invalid mode: {mode}.")
    DEFAULT_MODE = mode