import asyncio


async def handle_client(reader, writer):
    while True:
        request = (await reader.read(255)).decode()
        if not request:
            writer.close()
            break
        writer.write(request.encode())
        await writer.drain()


async def run_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 7976)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())