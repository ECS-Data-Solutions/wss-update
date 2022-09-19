import asyncio
import websockets
import os

conn = []

async def echo(websocket):
    conn.append(websocket)
    message = await websocket.recv()
    if message == {"msg": "trigger_update", "key": os.getenv("TRIG_KEY")}:
        for i in conn:
            i.sendMessage(str({"msg": "update"}))


async def main():
    async with websockets.serve(echo, "0.0.0.0", 80):
        await asyncio.Future()  # run forever

asyncio.run(main())
