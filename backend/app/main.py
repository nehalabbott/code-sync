from fastapi import FastAPI

from app.database.database import Base, engine

from app.models import user, room, document

from app.routes.auth import router as auth_router
from app.routes.room import router as room_router
from app.routes.websocket import router as websocket_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeSync"
)

app.include_router(auth_router)
app.include_router(room_router)
app.include_router(websocket_router)

@app.get("/")
def root():
    return {
        "message": "CodeSync API Running"
    }

@app.get("/test")
def test():
    return {"status": "ok"}