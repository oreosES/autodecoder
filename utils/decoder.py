from utils.vigenere import Vigenere
from utils.morsecode import MorseCode
from utils.rot13 import Rot13
from utils.rot47 import Rot47
from utils.base import Base

class Decoder():
    def decode(self, decoder, message, key=None):
        base = Base()
        morsecode = MorseCode()
        rot13 = Rot13()
        rot47 = Rot47()
        vigenere = Vigenere()

        if decoder == "base16":
            translated = base.decode16(message)
        elif decoder == "base32":
            translated = base.decode32(message)
        elif decoder == "base64":
            translated = base.decode64(message)
        elif decoder == "base85":
            translated = base.decode85(message)
        elif decoder == "morse":
            translated = morsecode.decode(message)
        elif decoder == "rot13":
            translated = rot13.decode(message)
        elif decoder == "rot47":
            translated = rot47.decode(message)
        elif decoder == "vigenere":
            translated = vigenere.decode(message, key)
        else:
            translated = None
        return translated