import csv
from datetime import datetime

def mark_attendance(name):
    with open("data/attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        now = datetime.now()
        writer.writerow([name, now.date(), now.strftime("%H:%M:%S")])
    print(f"Attendance marked for {name}")
