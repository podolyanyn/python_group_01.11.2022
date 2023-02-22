import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(('localhost', 8888))
    while True:
        msg = input('>>> ')
        if msg:
            client.send(msg.encode('utf8'))
            response = client.recv(1024).decode('utf8')
            print(response)
        else:
            break