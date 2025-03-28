def read_tasks():
    try:
        file = open("tasks.txt")
        tasks = {}
        for line in file:
            line = line.strip()  # Remove trailing newline
            if line:  # Skip empty lines
                parts = line.split(", ")
                if len(parts) >= 3:
                    numbr = parts[0]
                    name = parts[1]
                    desc = parts[2]
                    tasks[numbr] = (name, desc)
        file.close()  # Added parentheses
        return tasks
    except FileNotFoundError:
        # Handle file not found by returning empty dictionary
        return {}

def write_task(numbr: str, name: str, decs: str) -> bool:
    file = open("tasks.txt", "a")
    file.write(f"{numbr}, {name}, {decs}\n")  # Removed extra comma
    file.close()  # Added parentheses
    return True


write_task("1", "hehe", "nothing")
print(read_tasks())