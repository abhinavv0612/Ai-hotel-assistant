from fastapi import FastAPI
from app.routes import chat, booking
from app.db.database import engine, Base
from app.models.booking import Booking  

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chat.router)
app.include_router(booking.router)

@app.get("/")
def home():
    return {"message": "AI Hotel Assistant Running"}