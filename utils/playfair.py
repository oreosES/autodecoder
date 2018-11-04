from pycipher import Playfair

class PlayFair:
    def decode(self, message, key):
        try:
            return Playfair(key).decipher(message)
        except:
            return None