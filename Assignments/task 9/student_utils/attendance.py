def calculate_attendance(total_classes, attended_classes):
    try:
        if total_classes <= 0:
            raise ValueError("Total classes must be greater than 0.")
        percentage = (attended_classes / total_classes) * 100
        return round(percentage, 2)
    except Exception as e:
        print("Error in calculating attendance:", e)
        return 0.0
