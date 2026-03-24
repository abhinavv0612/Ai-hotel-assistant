from fastapi import APIRouter
from app.services.ai_service import get_response

router = APIRouter(prefix="/chat")

@router.post("/")
def chat(query: str):
    return {"response": get_response(query)}