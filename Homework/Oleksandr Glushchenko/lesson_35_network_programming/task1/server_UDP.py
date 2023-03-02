import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 65432)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

while True:
    # Wait for incoming data
    print('waiting for data')
    data, address = sock.recvfrom(1024)

    # Print the received data
    print(f'Received {len(data)} bytes from {address}:')
    print(data.decode())

    # Send a response back to the client
    message = 'This is a response message'
    sock.sendto(message.encode(), address)
