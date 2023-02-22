# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread

import socket
import threading

# Set HOST and PORT
HOST = '127.0.0.1'
PORT = 65432


def connect(connection, address):
    with connection:
        print(f'Successfully connected by {address}')
        while True:
            data = connection.recv(1024)
            print(f'received from {address} via {threading.current_thread().name}: {data}')
            if not data:
                break
            connection.send(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print(f'Server started\n{HOST}:{PORT}')
s.listen(5)

while True:
    conn, addrr = s.accept()
    t = threading.Thread(target=connect, args=(conn, addrr))
    t.start()
