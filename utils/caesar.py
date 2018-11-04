class Caesar:
    a, z = ord('a'), ord('z')
    A, Z = ord('A'), ord('Z')
    def getShiftCh(self, ch, shift):
        result = dif = ord(ch) + shift
        if dif > self.Z:
            result = (dif - self.Z) % 26 - 1 + self.A
        elif dif < self.A:
            result = self.Z - ((self.A - dif) % 26 - 1)
        return chr(result)

    def decode(self, message, shift):
        try:
            translated = ""
            for ch in message:
                if ch.islower():
                    translated += self.getShiftCh(ch, shift)
                elif ch.isupper():
                    translated += self.getShiftCh(ch, shift)
                else:
                    translated += ch
            return translated.rstrip('\n')
        except:
            return None