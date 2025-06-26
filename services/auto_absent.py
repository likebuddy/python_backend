import os
import csv
from datetime import datetime

def mark_auto_absent():
    today = datetime.now().strftime("%Y-%m-%d")
    marked_ids = set()
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["date"] == today:
                    marked_ids.add(row["user_id"])
    all_ids = os.listdir("dataset")
    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if os.stat("attendance.csv").st_size == 0:
            writer.writerow(["name", "user_id", "date", "time", "status"])
        for user_id in all_ids:
            if user_id not in marked_ids:
                writer.writerow([user_id, user_id, today, "--:--", "Absent"])
