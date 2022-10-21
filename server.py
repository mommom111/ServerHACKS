import asyncio
import websockets
from IPython import embed
import nest_asyncio

nest_asyncio.apply()
 
clients = set()
device_count = "0"

async def broadcast():
    while True:
        for ws in clients:
            global device_count
            device_count
            await ws.send(device_count)
        await asyncio.sleep(1)

asyncio.get_event_loop().create_task(broadcast())

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for msg in websocket:
            global device_count
            device_count = msg
    finally:
        clients.remove(websocket)
 
async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever
 
if __name__ == "__main__":
    asyncio.run(main())