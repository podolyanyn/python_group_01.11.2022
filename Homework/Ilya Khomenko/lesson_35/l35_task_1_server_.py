import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 8000)
sock.bind(server_address)

while True:
    print('waiting to receive message')
    data, address = sock.recvfrom(4096)
    print('received {} bytes from {}'.format(len(data), address))
    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))