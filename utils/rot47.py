class Rot47():
    def decode(self, message):
        translated = []
        for i in range(len(message)):
            j = ord(message[i])
            if j >= 33 and j <= 126:
                translated.append(chr(33 + ((j + 14) % 94)))
            else:
                translated.append(message[i])
        return ''.join(translated).rstrip('\n')