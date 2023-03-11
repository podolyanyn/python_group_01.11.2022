import threading
import socket


HOST = '127.0.0.1'
PORT = 7976
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


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print('Server binded to  port', PORT)
server.listen()
print('Server is listening')

while True:
    conn, addr = server.accept()
    lock.acquire()
    print(f'Connected to: {addr[0]}:{addr[1]}')

    threading.Thread.start_new_thread(client_thread, (conn, ))