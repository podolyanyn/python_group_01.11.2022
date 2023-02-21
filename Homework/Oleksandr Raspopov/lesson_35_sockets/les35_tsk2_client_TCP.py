# Task 2
# Extend the echo server, which returns to client the data,
# encrypted using the Caesar cipher algorithm by a specific key obtained from the client.

import socket

HOST = '127.0.0.2'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        shift = input('Enter integer between 0-25: ')
        msg = str(shift+input('Enter text: '))
        s.send(msg.encode())
        data = s.recv(1024)
        print(data.decode())
