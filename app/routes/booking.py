from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.booking import Booking

router = APIRouter(prefix="/booking")

@router.post("/")
def create_booking(name: str, room: str):
    db = SessionLocal()

    new_booking = Booking(name=name, room=room)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    db.close()

    return {"message": "Booking saved", "id": new_booking.id}