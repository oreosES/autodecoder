class Rot47():
    def decode(self, message):
        try:
            translated = []
            for i in range(len(message)):
                j = ord(message[i])
                if j >= 33 and j <= 126:
                    translated.append(chr(33 + ((j + 14) % 94)))
                else:
                    translated.append(message[i])
            translated = translated if len(translated) > 0 else None
            return ''.join(translated).rstrip('\n')
        except:
            return None