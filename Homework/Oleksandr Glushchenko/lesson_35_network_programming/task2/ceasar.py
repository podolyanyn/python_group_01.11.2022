def caesar_encrypt(data, key):
    """Encrypts the given data using the Caesar cipher algorithm with the given key"""
    encrypted = []
    for char in data:
        if char.isalpha():
            # Shift the character by the key value, wrapping around the alphabet
            temp = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted.append(temp)
        else:
            encrypted.append(char)
    return "".join(encrypted)


def caesar_decrypt(data, key):
    decrypted = []
    for char in data:
        if char.isalpha():
            # Shift the character by the key value, wrapping around the alphabet
            temp = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            decrypted.append(temp)
        else:
            decrypted.append(char)
    return "".join(decrypted)


