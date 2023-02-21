# Task 1
# Create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

HOST = 'localhost'
PORT = 65432

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((HOST, PORT))
    msg = input('Enter message: ')
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())
