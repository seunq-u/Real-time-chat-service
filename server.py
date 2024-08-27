from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
import uvicorn

app = FastAPI()

clients = set()

async def connect(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    print("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                await client.send_text(data)
                print(client, data)
    except WebSocketDisconnect:
        clients.remove(websocket)
        print("WebSocket disconnected")
    finally:
        await websocket.close()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connect(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3940)