import asyncio
from math import sin
import os

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

PORT = int(os.environ.get("PORT", 8080))

async def main():
    async with serve(handler, "0.0.0.0", PORT):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())