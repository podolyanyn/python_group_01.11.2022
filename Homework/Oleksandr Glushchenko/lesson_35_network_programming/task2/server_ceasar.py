import socket
from ceasar import caesar_encrypt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65437)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            key = connection.recv(1024).decode()
            if key:
                print(f'key received: {key}')
                print('sending ceasar encrypted data to the client')
                data = 'hello world'
                ceasar_data = caesar_encrypt(data, int(key)).encode()
                connection.sendall(ceasar_data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
