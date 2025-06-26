from fastapi import APIRouter
from services.auto_absent import mark_auto_absent

router = APIRouter()

@router.get("/mark-absent")
def mark_absent():
    mark_auto_absent()
    return {"message": "Absent users marked"}
