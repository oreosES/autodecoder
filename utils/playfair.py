import re

class Playfair:
    def generateTable(self, key=''):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        table = [[0] * 5 for row in range(5)]
        key = re.sub(r'[\WJ]', '', key.upper())
        for row in range(5):
            for col in range(5):
                if len(key):
                    table[row][col] = key[0]
                    alphabet = alphabet.replace(key[0], '')
                    key = key.replace(key[0], '', -1)
                else:
                    table[row][col] = alphabet[0]
                    alphabet = alphabet[1:]
        return table

    def position(self, table, ch):
        for row in range(5):
            for col in range(5):
                if table[row][col] == ch:
                    return [row, col]
        return [row, col]

    def decode(self, message, key):
        try:
            table = self.generateTable(key)
            message = re.sub(r'[\WJ]', '', message.upper())
            translated = ''
            for i in range(0, len(message), 2):
                digraphs = message[i:i+2]
                if len(digraphs) != 2:
                    return None
                a, b = digraphs[0], digraphs[1]
                a = self.position(table, a)
                b = self.position(table, b)
                if (a[0] == b[0]):
                    translated += table[a[0]][(a[1] - 1) % 5] + table[b[0]][(b[1] - 1) % 5]
                elif (a[1] == b[1]):
                    translated += table[(a[0] - 1) % 5][a[1]] + table[(b[0] - 1) % 5][b[1]]
                else:
                    translated += table[a[0]][b[1]] + table[b[0]][a[1]]
            return translated.rstrip('\n')
        except:
            return None