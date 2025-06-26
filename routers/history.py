from fastapi import APIRouter
import csv
import os

router = APIRouter()

@router.get("/history")
def get_history():
    data = []
    if not os.path.exists("attendance.csv"):
        return []
    with open("attendance.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
