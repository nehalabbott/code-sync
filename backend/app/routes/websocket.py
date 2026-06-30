from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.manager import manager

from app.database.database import SessionLocal

from app.services.document_service import (
    save_document,
    get_document
)

router = APIRouter(prefix="/ws")


@router.websocket("/{room_code}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_code: str,
):

    db = SessionLocal()

    await manager.connect(room_code, websocket)

    previous = get_document(db, room_code)

    if previous != "":
        await websocket.send_text(previous)

    try:

        while True:

            data = await websocket.receive_text()

            save_document(
                db,
                room_code,
                data
            )

            await manager.broadcast(
                room_code,
                data
            )

    except WebSocketDisconnect:

        manager.disconnect(
            room_code,
            websocket
        )

    finally:

        db.close()