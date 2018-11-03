import base64

class Base():
    def decode16(self, message):
        try:
            return base64.b16decode(message).decode("utf-8").rstrip('\n')
        except:
            return None

    def decode32(self, message):
        try:
            return base64.b32decode(message).decode("utf-8").rstrip('\n')
        except:
            return None

    def decode64(self, message):
        try:
            return base64.b64decode(message).decode("utf-8").rstrip('\n')
        except:
            return None

    def decode85(self, message):
        try:
            return base64.b85decode(message).decode("utf-8").rstrip('\n')
        except:
            return None