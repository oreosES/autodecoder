from pycipher import Beaufort

class BeauFort:
    def decode(self, message, key):
        try:
            return Beaufort(key).decipher(message)
        except:
            return None