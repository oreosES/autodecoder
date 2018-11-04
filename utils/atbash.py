from pycipher import Atbash

class AtBash:
    def decode(self, message):
        try:
            return Atbash().decipher(message)
        except:
            return None