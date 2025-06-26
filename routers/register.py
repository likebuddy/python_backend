from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from services.register_face import register_face
from services.train_model import train_model

router = APIRouter()

@router.post("/register")
async def register(user_id: str = Form(...)):
    if register_face(user_id):
        train_model()
        return {"message": "Face registered successfully"}
    return JSONResponse(content={"error": "Failed to register face"}, status_code=500)
