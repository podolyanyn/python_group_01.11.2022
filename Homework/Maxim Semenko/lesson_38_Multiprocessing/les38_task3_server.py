import multiprocessing
import socket

HOST = 'localhost'
PORT = 64533


def handle(conn, addr):
    print(multiprocessing.current_process())
    while True:
        print(f'Connected to: {addr[0]}:{addr[1]}')
        data = conn.recv(1024)
        if not data:
            print('Bye')
            break
        conn.send(data)
    conn.close()


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        print('Server binded to  port', PORT)
        server.listen(3)
        print('Server is listening')
        while True:
            conn, addr = server.accept()
            p = multiprocessing.Process(target=handle, args=(conn, addr))
            p.start()
