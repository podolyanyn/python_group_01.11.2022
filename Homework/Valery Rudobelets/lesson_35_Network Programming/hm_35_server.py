import socket


def caesar_cipher(datum, key):
    encrypted_datum = ""
    for char in datum:
        if char.isupper():
            encrypted_datum += chr((ord(char) + key - 65) % 26 + 65)
        else:
            encrypted_datum += chr((ord(char) + key - 97) % 26 + 97)
    return encrypted_datum

# task_1


HOST = 'localhost'  # Standard loop-back interface address (localhost)
PORT = 5051        # Port to listen on (non-privileged ports are > 1023)
bufferSize = 1024
ADDR = (HOST, PORT)
#
# msgFromServer = "Hello UDP Client"
# bytesToSend = str.encode(msgFromServer)
#
# UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# UDPServerSocket.bind(ADDR)
# print("UDP server up and listening")
#
# while (True):
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#     message = bytesAddressPair[0]
#     address = bytesAddressPair[1]
#     clientMsg = f"Message from Client:{message}"
#     clientIP = f"Client IP Address:{address}"
#
#     print(clientMsg)
#     print(clientIP)
#
#     UDPServerSocket.sendto(bytesToSend, address)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)[0:-1]
            key = conn.recv(1024)[-1]
            encrypted_data = caesar_cipher(data, int(key))
            if not data:
                break
            conn.sendall(encrypted_data)
