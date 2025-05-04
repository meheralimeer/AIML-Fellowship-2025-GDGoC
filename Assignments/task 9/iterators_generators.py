import random

class StudentList:
    """
    An iterator to iterate through a list of enrolled students.
    """
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

def attendance_generator(students):
    """
    Yields attendance (Present/Absent) for each student in the list.
    """
    try:
        for student in students:
            status = random.choice(['Present', 'Absent'])
            yield (student, status)
    except Exception as e:
        print("Error in attendance generator:", e)

def random_marks_generator(students, total_marks=100):
    """
    Yields random marks (0 to total_marks) for each student.
    """
    try:
        for student in students:
            marks = random.randint(0, total_marks)
            yield (student, marks)
    except Exception as e:
        print("Error in marks generator:", e)

if __name__ == "__main__":
    try:
        enrolled_students = ["Ali", "Sara", "John", "Amina", "Zara"]

        print("=== Iterating through StudentList ===")
        student_iter = StudentList(enrolled_students)
        for student in student_iter:
            print("Student:", student)

        print("\n=== Simulated Daily Attendance ===")
        for name, status in attendance_generator(enrolled_students):
            print(f"{name}: {status}")

        print("\n=== Random Marks Generation ===")
        for name, marks in random_marks_generator(enrolled_students, total_marks=100):
            print(f"{name}: {marks} marks")

    except Exception as e:
        print("An error occurred in main execution:", e)
