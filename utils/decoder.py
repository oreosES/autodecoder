from utils.base import Base
from utils.autokey import AutoKey
from utils.atbash import AtBash
from utils.beaufort import BeauFort
from utils.baconian import Baconian
from utils.caesar import Caesar
from utils.morsecode import MorseCode
from utils.rot13 import Rot13
from utils.rot47 import Rot47
from utils.playfair import PlayFair
from utils.vigenere import Vigenere

class Decoder():
    def decode(self, decoder, message, shift, key=None):
        base = Base()
        autokey = AutoKey()
        atbash = AtBash()
        baconian = Baconian()
        beaufort = BeauFort()
        caesar = Caesar()
        morsecode = MorseCode()
        rot13 = Rot13()
        rot47 = Rot47()
        playfair = PlayFair()
        vigenere = Vigenere()

        if decoder == "base16":
            translated = base.decode16(message)
        elif decoder == "base32":
            translated = base.decode32(message)
        elif decoder == "base64":
            translated = base.decode64(message)
        elif decoder == "base85":
            translated = base.decode85(message)
        elif decoder == "autokey":
            translated = autokey.decode(message, key)
        elif decoder == "atbash":
            translated = atbash.decode(message)
        elif decoder == "baconian":
            translated = baconian.decode(message)
        elif decoder == "beaufort":
            translated = beaufort.decode(message, key)
        elif decoder == "caesar":
            translated = caesar.decode(message, shift)
        elif decoder == "morse":
            translated = morsecode.decode(message)
        elif decoder == "rot13":
            translated = rot13.decode(message)
        elif decoder == "rot47":
            translated = rot47.decode(message)
        elif decoder == "playfair":
            translated = playfair.decode(message, key)
        elif decoder == "vigenere":
            translated = vigenere.decode(message, key)
        else:
            translated = None
        return translated