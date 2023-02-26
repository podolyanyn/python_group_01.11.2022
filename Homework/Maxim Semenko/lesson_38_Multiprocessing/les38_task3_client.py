import socket

HOST = 'localhost'
PORT = 64533

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    msg = 'Hello'
    while True:
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print('Received from the server:', str(data.decode('utf-8')))
        ans = input('\nDo you want to continue(y/n)?\n')
        if ans == 'y':
            continue
        else:
            break