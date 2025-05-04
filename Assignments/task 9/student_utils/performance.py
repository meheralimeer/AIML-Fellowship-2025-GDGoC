def is_eligible_for_scholarship(gpa, attendance_percentage):
    try:
        return gpa >= 3.5 and attendance_percentage >= 90
    except Exception as e:
        print("Error evaluating scholarship eligibility:", e)
        return False

def performance_remark(gpa):
    try:
        if gpa >= 3.7:
            return "Excellent"
        elif gpa >= 3.0:
            return "Good"
        elif gpa >= 2.0:
            return "Satisfactory"
        else:
            return "Needs Improvement"
    except Exception as e:
        print("Error in evaluating performance:", e)
        return "Error"
