# Task 2
# Extend the echo server, which returns to client the data,
# encrypted using the Caesar cipher algorithm by a specific key obtained from the client.

import socket

HOST = '127.0.0.2'
PORT = 65432


############  Caesar cipher algorithm   ############

def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

################################################################

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addrr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            shift = int(data.decode()[0])
            msg = str(data.decode()[1:])
            msg_encrypted = encrypt(msg, shift)
            print(f'{msg} --> {msg_encrypted}')
            conn.send(msg_encrypted.encode())
