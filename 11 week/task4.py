import unittest
class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = {}
        self._decode = {}
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[encoded] = letter
            self._decode[encoded.upper()] = letter.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


class TestCaesarCipher(unittest.TestCase):
    def encode_lower(self):
        self.assertEqual(self.cipher.encode("абв"), "где")

    def encode_upper(self):
        self.assertEqual(self.cipher.encode("АБВ"), "ГДЕ")

    def encode_with_numbers(self):
        self.assertEqual(self.cipher.encode("абв123"), "где123")

    def decode_lower(self):
        self.assertEqual(self.cipher.decode("где"), "абв")

    def decode_upper(self):
        self.assertEqual(self.cipher.decode("ГДЕ"), "АБВ")

    def decode_with_numbers(self):
        self.assertEqual(self.cipher.decode("где123"), "абв123")

unittest.main()