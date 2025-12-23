import pandas as pd

def analyze_performance():
    try:
        data = pd.read_csv("data/attendance.csv", header=None)
        data.columns = ["Name", "Date", "Time"]
        summary = data["Name"].value_counts()
        print("\nStudent Engagement Summary:")
        print(summary)
    except FileNotFoundError:
        print("No attendance data found.")
