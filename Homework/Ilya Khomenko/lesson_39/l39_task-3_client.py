import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1',7976))


while 1:
    message = input("Enter a message: ")
    if message != '':
        client.send(message.encode())
        response = client.recv(1024).decode('utf8')
        print(response)
    else:
        break