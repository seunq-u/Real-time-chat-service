from fastapi import FastAPI, WebSocket, Request
from starlette.websockets import WebSocketDisconnect
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from MessageManager import MessageManager

global messageManager
messageManager = MessageManager()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

clients = set()

@app.get("/")
async def read_index():
    with open("static/index.html") as file:
        return HTMLResponse(content=file.read())


async def connect(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    print("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            
            await messageManager.post(data) # 메시지관리자에게 메시지 전달

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