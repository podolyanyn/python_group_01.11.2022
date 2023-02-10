import string
"""CLASS FOR CAESAR ENCRYPTION"""


class Caesar:

    default_alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.punctuation)

    def __init__(self):
        pass

    def shift_alphabet(self, shift, alphabet="".join(default_alphabets)):
        return alphabet[shift:] + alphabet[:shift]

    def translation_table(self, alphabet, shifted_alphabet):
        return str.maketrans(alphabet, shifted_alphabet)

    def caesar_it(self, text, shift, alphabet="".join(default_alphabets)):
        shifted_alphabet = self.shift_alphabet(shift, alphabet)

        return text.translate(self.translation_table(alphabet, shifted_alphabet))
