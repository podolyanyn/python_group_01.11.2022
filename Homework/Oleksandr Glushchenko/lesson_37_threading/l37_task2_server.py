"""
Task 2. Echo server with threading
Create a socket echo server which handles each connection in a separate Thread
"""
import socket
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65436)
print(f'starting up on {server_address[0]}:{server_address[1]}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)


def client_conn(conn):
    print(f'Connected by {conn.getpeername()}')
    while True:
        data = conn.recv(1024).decode()
        if data:
            print(f'Now running: {threading.current_thread().getName()}')
            print(f'received from {conn.getpeername()}: {data}')
        else:
            break
        conn.sendall(data.encode())
    print(f'Connection from {conn.getpeername()} closed')


while True:
    # Wait for a connection
    print('waiting for a connection')
    # Accept a new connection and start a new thread to handle it
    connection, client_address = sock.accept()
    conn_thread = threading.Thread(target=client_conn, args=(connection, ))
    conn_thread.start()
