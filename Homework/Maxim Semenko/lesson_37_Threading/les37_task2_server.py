import threading
import socket
import _thread

HOST = '127.0.0.1'
PORT = 64532
lock = threading.Lock()


def client_thread(conn):
    print(threading.current_thread())
    while True:
        data = conn.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        conn.send(data)
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print('Server binded to  port', PORT)
    server.listen(5)
    print('Server is listening')

    while True:
        conn, addr = server.accept()
        lock.acquire()
        print(f'Connected to: {addr[0]}:{addr[1]}')

        _thread.start_new_thread(client_thread, (conn, ))