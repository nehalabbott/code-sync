from sqlalchemy.orm import Session

from app.models.room import Room
from app.models.document import Document


def save_document(db: Session, room_code: str, content: str):

    room = (
        db.query(Room)
        .filter(Room.room_code == room_code)
        .first()
    )

    if room is None:
        return

    document = (
        db.query(Document)
        .filter(Document.room_id == room.id)
        .first()
    )

    if document:

        document.content = content

    else:

        document = Document(
            room_id=room.id,
            content=content
        )

        db.add(document)

    db.commit()


def get_document(db: Session, room_code: str):

    room = (
        db.query(Room)
        .filter(Room.room_code == room_code)
        .first()
    )

    if room is None:
        return ""

    document = (
        db.query(Document)
        .filter(Document.room_id == room.id)
        .first()
    )

    if document:
        return document.content

    return ""