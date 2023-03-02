"""
Task 3. Echo server with asyncio
Create a socket echo server which handles each connection using asyncio Tasks.
"""


import asyncio
import threading
import os


async def handle_connection(reader, writer):
    print(f'Connected by {writer.get_extra_info("peername")}')
    while True:
        data_in = await reader.read(1024)
        if data_in:
            print(f'Now running: thread: {threading.current_thread().name}, process: {os.getpid()}, '
                  f'parent process: {os.getppid()}')
            print(f'received from {writer.get_extra_info("peername")}: {data_in.decode()}')
            data_out = data_in.decode().upper()
        else:
            break
        writer.write(data_out.encode())  # writes the response back to the client
        await writer.drain()  # flushes the write buffer to the network
        print(f'sent to {writer.get_extra_info("peername")}: {data_out}')
        print('waiting for a connection')

    writer.close()
    print(f'Connection from {writer.get_extra_info("peername")} closed')


async def main():
    server_address = ('localhost', 65438)
    server = await asyncio.start_server(handle_connection, *server_address)
    print(f'starting up on {server_address[0]}:{server_address[1]}')
    print('waiting for a connection')
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
