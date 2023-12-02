import unittest


class Caesar:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, key):
        self._encode = dict()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


class TestEncode1(unittest.TestCase):
    def test_caesar(self):
        text = 'БибаБоба'
        key = 8
        c = Caesar(key)
        self.assertEqual(c.encode(text), 'ИризИциз')


class TestEncode2(unittest.TestCase):
    def test_caesar(self):
        text = 'фэфм вперёд'
        key = 3
        c = Caesar(key)
        self.assertEqual(c.encode(text), 'чачп етзуиж')


class TestDecode1(unittest.TestCase):
    def test_caesar(self):
        text = 'ИризИциз'
        key = 8
        c = Caesar(key)
        self.assertEqual(c.decode(text), 'БибаБоба')


class TestDecode2(unittest.TestCase):
    def test_caesar(self):
        text = 'чачп етзуиж'
        key = 3
        c = Caesar(key)
        self.assertEqual(c.decode(text), 'фэфм вперёд')