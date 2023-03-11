import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 8000)
message = b'This is the message. It will be repeated'

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()