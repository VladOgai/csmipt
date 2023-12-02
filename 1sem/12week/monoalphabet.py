import random


class Monoalphabet:
    # alphabet = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {x: y for y, x in self._encode.items()}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


def find_keytable(text):
    chastot = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
    keys = list(chastot)
    keys.sort(key=text.lower().count, reverse=True)
    return ''.join(keys)


# key = Monoalphabet.alphabet[:]
# random.shuffle(key)
# cipher = Monoalphabet(key)
# line = input()
# while line != '.':
#     print(cipher.encode(line))
#     line = input()

text = ''
line = input()
while line != '.':
    text += ' ' + line
    line = input()
# key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = 'эьормщднйгычясюцажшбтпвёле__зхкфи'
cipher = Monoalphabet(key)
print(cipher.decode(text))
