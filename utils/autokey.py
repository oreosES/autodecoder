from pycipher import Autokey

class AutoKey:
    def decode(self, message, key):
        try:
            return Autokey(key).decipher(message)
        except:
            return None