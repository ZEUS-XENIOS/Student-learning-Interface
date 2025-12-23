from src.face_recognition import recognize_face
from src.attendance import mark_attendance
from src.performance_analysis import analyze_performance

def main():
    print("Student Learning Interface Started")
    student_name = "Kapil"
    mark_attendance(student_name)
    recognize_face()
    analyze_performance()

if __name__ == "__main__":
    main()

