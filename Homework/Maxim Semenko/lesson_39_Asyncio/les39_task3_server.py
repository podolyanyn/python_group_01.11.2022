import asyncio


async def handle_client(reader, writer):
    while True:
        request = (await reader.read(255)).decode('utf-8')
        if not request:
            writer.close()
            break
        writer.write(request.encode('utf-8'))
        await writer.drain()


async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())