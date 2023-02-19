import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = 'This is a test message from client to the server'
server_address = (HOST, PORT)
sent = sock.sendto(message.encode(), server_address)

# Receive a response from the server
print('Waiting for a response ...')
data, server = sock.recvfrom(1024)
print(f'Received {len(data)} bytes from {server}:')
print(data.decode())
