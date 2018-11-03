from codecs import encode

class Rot13():
    def decode(self, message):
        return encode(message, 'rot13').rstrip('\n')