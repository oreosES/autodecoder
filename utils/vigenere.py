import pyperclip

class Vigenere:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def decode(self, message, key):
        try:
            translated = []
            keyIndex = 0
            key = key.upper()
            for symbol in message:
                num = self.alphabet.find(symbol.upper())
                if num != -1:
                    num -= self.alphabet.find(key[keyIndex])
                    num %= len(self.alphabet)
                    if symbol.isupper():
                        translated.append(self.alphabet[num])
                    elif symbol.islower():
                        translated.append(self.alphabet[num].lower())
                    keyIndex += 1
                    if keyIndex == len(key):
                        keyIndex = 0
                else:
                    translated.append(symbol)
            return ''.join(translated).rstrip('\n')
        except:
            return None