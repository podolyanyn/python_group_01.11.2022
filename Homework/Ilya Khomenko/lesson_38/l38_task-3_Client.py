import socket

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 7976))
    data = "some data"
    sock.sendall(data)
    result = sock.recv(1024)
    print(result)
    sock.close()