from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.recognize_face import recognize_face
from datetime import datetime
import csv
import os

router = APIRouter()

@router.post("/recognize")
def recognize():
    name = recognize_face()
    if name:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        status = "Present"

        with open("attendance.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if os.stat("attendance.csv").st_size == 0:
                writer.writerow(["name", "user_id", "date", "time", "status"])
            writer.writerow([name, name, date, time, status])

        return {
            "name": name,
            "user_id": name,
            "date": date,
            "time": time,
            "status": status
        }
    return JSONResponse(content={"error": "Face not recognized"}, status_code=404)
