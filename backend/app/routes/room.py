import random
import string

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.room import Room
from app.models.document import Document

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


def generate_room_code():

    return "".join(

        random.choices(

            string.ascii_uppercase +
            string.digits,

            k=6

        )

    )


@router.post("/")
def create_room(
    db: Session = Depends(get_db)
):

    room = Room(

        room_code=generate_room_code(),

        owner_id=None

    )

    db.add(room)

    db.commit()

    db.refresh(room)

    document = Document(

        room_id=room.id,

        content=""

    )

    db.add(document)

    db.commit()

    return {

        "room_code": room.room_code

    }


@router.get("/{room_code}")
def get_room(

    room_code: str,

    db: Session = Depends(get_db)

):

    room = (

        db.query(Room)

        .filter(Room.room_code == room_code)

        .first()

    )

    if room is None:

        return {

            "exists": False

        }

    return {

        "exists": True,

        "room_code": room.room_code

    }