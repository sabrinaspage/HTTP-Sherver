import asyncio

HOST = '127.0.0.1'
PORT = '8888'

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connect(HOST, PORT)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    #wait for data 
    data = await reader.read(100)
    print(f'Received: {data.decode()}!r')

    print('Close the connection')
    writer.close() #underling connection is closed
    await writer.wait_closed() # wait until stream is closed