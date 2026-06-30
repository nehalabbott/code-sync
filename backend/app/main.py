from fastapi import FastAPI

from app.database.database import Base, engine

from app.models import user, room, document

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CodeSync")

from app.routes.auth import router as auth_router

app.include_router(auth_router)
