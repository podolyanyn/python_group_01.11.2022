import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65436        # The port used by the server


def listen_server():
    while True:
        message = sock.recv(1024).decode()
        if message:
            print(f'received message back from server: {message}')
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print(f'trying to connect to the server {HOST}:{PORT}')
    try:
        sock.connect((HOST, PORT))
        print(f'successfully connected to the server {HOST}:{PORT}')
        data = 'Hello world!'

        while True:
            sock.sendall(data.encode())
            print('message sent to the server')
            listen_server()
            cond = input('enter "q" to exit or anything else to continue: ')
            if cond == 'q':
                print('Connection closed')
                break

    except Exception as e:
        print(f'Error connecting to the server due to {e}')
