from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)

    room_code = Column(String, unique=True, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))