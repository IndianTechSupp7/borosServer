import asyncio
from math import sin

from websockets.asyncio.server import serve

from container import ContainerManager


containerManager = ContainerManager()
clients = set()
containerManager.verify("test1:SET:3")
containerManager.verify("test2:SET:10")
containerManager.verify("test3:SET:15")
containerManager.verify("test4:SET:0")  
async def handler(websocket):
    #clients.append(websocket)
    while True:
        msg = f""
        for container in containerManager:
            msg += f"{container.name}:SET:{container.temp};"
        print(msg)
        await websocket.send(msg[:-1])
        await asyncio.sleep(0.5)

async def main():
    async with serve(handler, "192.168.1.74", 8001):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())