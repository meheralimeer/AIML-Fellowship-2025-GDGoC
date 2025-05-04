class Student:
    def __init__(self, name, age, student_id, courses=None):
        if courses is None:
            courses = []
        self._name = name
        self._age = age
        self._student_id = student_id
        self._courses = courses  # List of tuples: (course_name, grade)

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_student_id(self):
        return self._student_id

    def get_courses(self):
        return self._courses

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age

    def set_student_id(self, student_id):
        self._student_id = student_id

    def set_courses(self, courses):
        if not isinstance(courses, list):
            raise TypeError("Courses should be provided as a list.")
        self._courses = courses

    # Class method to calculate GPA (assuming grades are out of 4.0)
    def calculate_gpa(self):
        try:
            if not self._courses:
                return 0.0
            total = sum(grade for _, grade in self._courses)
            return round(total / len(self._courses), 2)
        except Exception as e:
            print("Error calculating GPA:", e)
            return 0.0


# Subclass GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses=None, thesis_title=""):
        super().__init__(name, age, student_id, courses)
        self._thesis_title = thesis_title

    def get_thesis_title(self):
        return self._thesis_title

    def set_thesis_title(self, title):
        self._thesis_title = title

    # Override __str__ to display all attributes
    def __str__(self):
        course_list = ", ".join(f"{course} ({grade})" for course, grade in self.get_courses())
        return (f"Name: {self.get_name()}\n"
                f"Age: {self.get_age()}\n"
                f"Student ID: {self.get_student_id()}\n"
                f"Courses: {course_list if course_list else 'None'}\n"
                f"GPA: {self.calculate_gpa()}\n"
                f"Thesis Title: {self._thesis_title}")


# Demonstration
if __name__ == "__main__":
    try:
        # Creating an instance of Student
        student = Student("Ali", 20, "S123", [("Math", 3.7), ("Physics", 3.5)])
        
        print("Initial Student Info:")
        print(f"Name: {student.get_name()}")
        print(f"Age: {student.get_age()}")
        print(f"ID: {student.get_student_id()}")
        print(f"Courses: {student.get_courses()}")
        print(f"GPA: {student.calculate_gpa()}")

        # Using setter to update age
        student.set_age(21)
        print("\nAfter Updating Age:")
        print(f"Updated Age: {student.get_age()}")

        # Creating an instance of GraduateStudent
        grad_student = GraduateStudent("Sara", 24, "G456", [("AI", 3.9), ("ML", 4.0)], "AI in Healthcare")
        print("\nGraduate Student Info:\n")
        print(grad_student)

    except Exception as e:
        print("An error occurred:", e)
