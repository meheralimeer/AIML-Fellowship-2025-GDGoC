def calculate_percentage(marks_obtained, total_marks):
    try:
        if total_marks <= 0:
            raise ValueError("Total marks must be greater than 0.")
        percentage = (marks_obtained / total_marks) * 100
        return round(percentage, 2)
    except Exception as e:
        print("Error in calculating percentage:", e)
        return 0.0

def classify_grade(percentage):
    try:
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"
    except Exception as e:
        print("Error in classifying grade:", e)
        return "Invalid"
