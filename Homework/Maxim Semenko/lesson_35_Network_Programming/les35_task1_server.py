import random
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))
server_socket.listen(1)
conn, addr = server_socket.accept()

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)
    if not message:
        break
    message = message.upper()
    server_socket.sendto(message, address)

conn.close()
