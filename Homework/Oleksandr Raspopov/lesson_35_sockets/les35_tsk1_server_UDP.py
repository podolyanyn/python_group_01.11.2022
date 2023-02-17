# Task 1
# Create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

HOST = 'localhost'
PORT = 65432

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    data = s.recvfrom(1024)
    print(f'Incoming data: {data}')
    message = b'echo: ' + data[0]
    client = data[1]
    s.sendto(message, client)
