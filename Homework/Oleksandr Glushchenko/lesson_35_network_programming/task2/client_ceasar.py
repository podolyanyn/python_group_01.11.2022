import socket
import random
from ceasar import caesar_decrypt

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65437        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    key = random.randint(1, 100)
    s.sendall(str(key).encode())
    data = s.recv(1024).decode()

print(f'Received encoded data: {data}')
print(f'Decoded data: {caesar_decrypt(data, key)}')
