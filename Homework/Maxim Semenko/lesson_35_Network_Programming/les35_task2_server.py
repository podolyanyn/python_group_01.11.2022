import socket
from caesar import Caesar


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 12345))

while True:
    data, address = server.recvfrom(1024)
    message = "Enter a key: "
    server.sendto(message.encode("utf-8"), address)

    key, address = server.recvfrom(1024)
    encryption = Caesar().caesar_it(data.decode("utf-8"), int(key))
    server.sendto(encryption.encode("utf-8"), address)
