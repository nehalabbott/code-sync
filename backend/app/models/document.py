from sqlalchemy import Column, Integer, Text, ForeignKey
from app.database.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    room_id = Column(
        Integer,
        ForeignKey("rooms.id"),
        unique=True
    )

    content = Column(
        Text,
        default=""
    )