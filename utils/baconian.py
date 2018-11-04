from unicodedata import normalize
import re

class Baconian:
    def generate_dict(self):
        bacon_dict = {}
        for i in range(0, 26):
            tmp = bin(i)[2:].zfill(5)
            tmp = tmp.replace('0', 'a')
            tmp = tmp.replace('1', 'b')
            bacon_dict[tmp] = chr(65 + i)
        return bacon_dict

    def decode(self, message):
        try:
            translated = ''
            bacon_dict = self.generate_dict()
            message = message.lower()
            message = re.sub(r'[^ab]+', '', message)
            for i in range(0, int(len(message) / 5)):
                translated += bacon_dict.get(message[i * 5:i * 5 + 5], ' ')
            translated = translated if len(translated) > 0 else None
            return translated.rstrip('\n')
        except:
            return None
