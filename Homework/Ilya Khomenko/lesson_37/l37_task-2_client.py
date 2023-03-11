import socket

HOST = '127.0.0.1'
PORT = 7976

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while True:
        msg = input('Enter a message: ')
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print('Received from the server:', str(data.decode('utf-8')))

