import time
import socket

HOST = "127.0.0.1"
PORT = 12000

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'test'
    addr = (HOST, PORT)
    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        ex_time = end - start
        print(f'{data} {pings} {ex_time}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
    finally:
        client_socket.close()
