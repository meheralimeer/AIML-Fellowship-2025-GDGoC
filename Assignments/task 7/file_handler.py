filename = "Assignments/task 7/tasks.txt"

def read_tasks():
    try:
        with open(filename) as file:
            if not file.read():
                return None
        with open(filename) as file:
            tasks = {}
            for line in file.readlines():
                line = line.strip()
                numbr, name, desc = line.split(", ")
                tasks[int(numbr)] = (name, desc)
            return tasks
    except FileNotFoundError:
        pass

def write_task(name: str, decs: str) -> bool:
    tasks = read_tasks()
    if tasks is None: numbr = 0;
    else: numbr = len(tasks)
    try:
        with open(filename, "+a") as file:
            file.write(f"{numbr + 1}, {name}, {decs}\n")
            return True
    except FileNotFoundError:
        return False
    
def update_task(id: int) -> bool:
    tasks = read_tasks()

def rewrite_tasks(tasks: dict) -> bool:
    try:
        with open(filename, "w") as file:
            for numbr, name_and_desc in tasks.items():
                file.write(f"{numbr}, {name_and_desc[0]}, {name_and_desc[1]}\n")
            return True
    except FileNotFoundError:
        return False