import socket
server_data = ("127.0.0.1", 12345)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Enter string: ")
    client.sendto(msg.encode("utf-8"), server_data)
    data, address = client.recvfrom(1024)
    print(f"Server: {data.decode('utf-8')}")
    if not msg:
        break
    key = str(input(""))
    client.sendto(key.encode("utf-8"), server_data)
    data, addr = client.recvfrom(1024)
    print(f"Server: {data.decode('utf-8')}")
    if not key:
        break
client.close()
