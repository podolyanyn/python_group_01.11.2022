import socket
import multiprocessing
import threading
import os
# import concurrent.futures


def handle_connection(conn):
    print(f'Connected by {conn.getpeername()}')
    while True:
        data = conn.recv(1024).decode()
        if data:
            print(f'Now running: thread: {threading.current_thread().name}, process: {os.getpid()}, '
                  f'parent process: {os.getppid()}')
            print(f'received from {conn.getpeername()}: {data}')
            print('waiting for a connection')
        else:
            break
        conn.sendall(data.encode())
    print(f'Connection from {conn.getpeername()} closed')


if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Bind the socket to the port
        server_address = ('localhost', 65437)
        print(f'starting up on {server_address[0]}:{server_address[1]}')
        server.bind(server_address)
        # Listen for incoming connections
        server.listen(5)
        print('waiting for a connection')
        while True:
            # Wait for a connection
            # Accept a new connection and start a new process to handle it
            connection, client_address = server.accept()
            conn_process = multiprocessing.Process(target=handle_connection, args=(connection,))
            conn_process.start()

    # alternative using concurrent.futures.ThreadPoolExecutor
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     while True:
    #         # Wait for a connection
    #         print('waiting for a connection')
    #         # Accept a new connection and start a new thread to handle it
    #         connection, client_address = server.accept()
    #         executor.submit(handle_connection, connection)
