from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.manager import manager

router = APIRouter(prefix="/ws", tags=["WebSocket"])


@router.websocket("/{room_code}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_code: str,
):
    await manager.connect(room_code, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(room_code, data)

    except WebSocketDisconnect:
        manager.disconnect(room_code, websocket)