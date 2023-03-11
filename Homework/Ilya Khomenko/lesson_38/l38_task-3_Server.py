import multiprocessing
import socket


HOST = '127.0.0.1'
PORT = 7976



def hand(conn,address):
    while True:
        data = conn.recv(1024)
        if data == "":
            break
        conn.send(data)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()
    print(f'Server ready up on: {PORT}')
    conn,address =server.accept()
    m = multiprocessing.Process(target=hand,args =(conn,address))
    m.start()