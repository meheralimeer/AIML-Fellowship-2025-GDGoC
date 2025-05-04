def read_student_file(filename):
    """
    Reads student records from a text file and prints them.
    Also returns the total number of students.
    """
    total_students = 0
    try:
        with open(filename, 'r') as file:
            print("Reading student records:\n")
            for line in file:
                print(line.strip())
                total_students += 1
        print(f"\nTotal students found: {total_students}")
        return total_students
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return 0


def write_student_file(filename, students):
    """
    Writes student records to a file.
    Each student should be a string (one line per student).
    """
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(student + '\n')
        print(f"Successfully wrote {len(students)} student records to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# Demonstration
if __name__ == "__main__":
    # Example content for testing write
    sample_students = [
        "Ali,20,S123,Math:3.7;Physics:3.5",
        "Sara,24,G456,AI:3.9;ML:4.0"
    ]

    write_student_file("students.txt", sample_students)

    read_student_file("students.txt")

    total = read_student_file("students.txt")
    if total > 0:
        try:
            with open("students.txt", 'r') as infile:
                contents = infile.readlines()
            write_student_file("student_output.txt", [line.strip() for line in contents])
        except Exception as e:
            print("An error occurred during copying:", e)
