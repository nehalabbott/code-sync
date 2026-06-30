import random
import string

from fastapi import APIRouter

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.post("/")
def create_room():

    code = "".join(

        random.choices(

            string.ascii_uppercase +
            string.digits,

            k=6

        )

    )

    return {

        "room_code": code

    }