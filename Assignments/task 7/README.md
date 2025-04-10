# Task Manager CLI Application

## Overview
This is a Command-Line Interface (CLI) Task Manager application written in Python. It allows users to manage their tasks by providing options to add, remove, update, and view tasks. All tasks are stored persistently in a text file (`tasks.txt`) to ensure data retention between program executions.

The project is designed modularly with separate files for handling different functionalities:
- **File Handling**: Reading and writing tasks to/from the `tasks.txt` file.
- **Task Operations**: Adding, removing, updating, and viewing tasks.
- **User Interaction**: A CLI interface that interacts with the user and calls task operations.

---

## Project Structure
```
Task7/
│── task_manager.py         # Main program (User Interface)
│── task_operations.py      # Functions for handling tasks
│── file_handler.py         # Functions for file handling
│── tasks.txt               # Stores tasks (auto-created by the program)
│── README.md               # Project documentation
```

---

## Features
1. **Add a Task**:
   - Users can input a task name and a short description.
   - The task is appended to the `tasks.txt` file.

2. **Remove a Task**:
   - Users can specify a task number to remove.
   - The task is deleted from the `tasks.txt` file.

3. **Update a Task**:
   - Users can modify the name or description of an existing task by specifying its task number.

4. **View All Tasks**:
   - Displays all tasks in a formatted manner, showing their task number, name, and description.

5. **Exit the Program**:
   - Exits the application gracefully.

---

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system.
- Install the required Python library: `termcolor`.
  pip install termcolor

### Steps to Run the Program
1. Clone the repository:
   git clone <repository-url>
2. Navigate to the `Task7` directory:
   cd Task7
3. Run the main program:
   python task_manager.py

---

## Usage Instructions

### Menu Options
Upon running the program, you will see the following menu:

Main Menu:
1. Add a task
2. Remove a task
3. Update a task
4. View tasks
5. Exit

#### 1. Add a Task
- Enter the task name and a short description when prompted.
- The task will be added to the list and saved in `tasks.txt`.

#### 2. Remove a Task
- Enter the task number of the task you want to remove.
- The task will be removed from the list and updated in `tasks.txt`.

#### 3. Update a Task
- View all tasks to identify the task number you want to update.
- Enter the new name and description for the task.
- The updated task will replace the old one in `tasks.txt`.

#### 4. View All Tasks
- Displays all tasks in the following format:
  Task Number: Task Name
  Description

#### 5. Exit
- Exits the program.

---

## File Descriptions

### `task_manager.py`
- The main entry point of the application.
- Handles user interaction and displays the menu.
- Calls functions from `task_operations.py` to perform task-related operations.

### `task_operations.py`
- Contains functions for adding, removing, updating, and viewing tasks.
- Uses `file_handler.py` to read/write tasks to/from the `tasks.txt` file.

### `file_handler.py`
- Handles reading and writing tasks to the `tasks.txt` file.
- Ensures the file is created if it doesn't exist.
- Implements exception handling for file operations.

### `tasks.txt`
- Stores all tasks in the following format:
  TaskNumber, TaskName, TaskDescription

---

## Error Handling
The program includes robust error handling to manage invalid inputs and edge cases:
- Invalid task numbers (e.g., out-of-range or non-integer values).
- Missing or corrupted `tasks.txt` file.
- Empty task lists.

---

## Testing
The program has been tested for the following scenarios:
1. Adding multiple tasks.
2. Removing tasks from an empty list.
3. Updating tasks with valid and invalid inputs.
4. Viewing tasks when the list is empty.
5. Handling invalid menu choices.

---

## Contribution Guidelines
If you wish to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature/fix:
   git checkout -b feature-name
3. Commit your changes:
   git commit -m "Add feature/fix"
4. Push to your branch:
   git push origin feature-name
5. Open a pull request.

---

## Contact
For any questions or feedback, feel free to reach out:
- Email: meherali.meer@gmail.com
- GitHub: [meheralimeer](https://github.com/meheralimeer)

---

## Acknowledgments
- Thanks to the Python community for providing excellent libraries like `termcolor` to enhance CLI applications.