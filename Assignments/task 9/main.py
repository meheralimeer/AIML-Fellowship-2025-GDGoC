from student_utils.arithmetic import calculate_percentage, classify_grade
from student_utils.attendance import calculate_attendance
from student_utils.performance import is_eligible_for_scholarship, performance_remark

if __name__ == "__main__":
    try:
        # Arithmetic functions
        percent = calculate_percentage(85, 100)
        grade = classify_grade(percent)
        print(f"Percentage: {percent}% | Grade: {grade}")

        # Attendance
        attendance = calculate_attendance(50, 45)
        print(f"Attendance: {attendance}%")

        # Performance
        gpa = 3.6
        eligible = is_eligible_for_scholarship(gpa, attendance)
        remark = performance_remark(gpa)
        print(f"GPA: {gpa} | Eligible for Scholarship: {'Yes' if eligible else 'No'}")
        print(f"Performance Remark: {remark}")

    except Exception as e:
        print("An error occurred in main execution:", e)
