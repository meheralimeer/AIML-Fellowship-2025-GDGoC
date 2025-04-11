import file_handler
from termcolor import colored


def view_all_tasks():
    print(colored(" VIEWING ALL TASKS ", "white", "on_light_blue", ["bold"]))
    print()
    try:
        tasks = file_handler.read_tasks()
        if tasks is None:
            print(
                colored("File is empty, try adding some tasks first...", "black", "on_yellow"))
            return None

        for numbr, name_and_disc in tasks.items():
            print(f"{numbr}: {name_and_disc[0]}\n{name_and_disc[1]}")
            print()
        return tasks
    except FileNotFoundError:
        print(colored(
            "File \"tasks.txt\" not found in current directory...", "black", "on_red"))
        print(colored("Add a task to automatically create...", "black", "on_green"))


def add_task():
    print(colored(" ADD TASK ", "white", "on_light_blue", ["bold"]))
    print()
    name = input(colored("Enter Name: ", "light_blue"))
    desc = input(colored("Enter Short Description: ", "light_blue"))
    print()
    if file_handler.write_task(name=name, decs=desc):
        print(colored("Successfully added!", "green"))
        print()
        print("Press enter key to return to main menu...")
        input()

    else:
        print(colored("Error while adding task...", "red"))


def update_task():
    print(colored(" UPDATE TASK ", "white", "on_light_blue", ["bold"]))
    print()
    tasks = view_all_tasks()
    if tasks is None:
        print("Press enter key to return to main menu...")
        input()
        return
    to_update = int(input(colored("Enter task number to update: ", "blue")))

    while True:
        new_name = input(colored("Enter Updated Name: ", "light_blue"))
        new_desc = input(
            colored("Enter Updated Short Description: ", "light_blue"))
        if new_name == tasks[to_update][0] and new_desc == tasks[to_update][1]:
            print(colored(
                "Name or Descriptions must be modified to update...\n Try Again!", "red"))
            print()
            continue
        break

    tasks[to_update] = (new_name, new_desc)
    if file_handler.rewrite_tasks(tasks):
        print(colored("Successfully updated task!", "white", "on_green"))
        print()
        print("Press enter key to return to main menu...")
        input()
        return
    print(colored("Error while updating task!", "red"))


def remove_task():
    print(colored(" REMOVE TASK ", "white", "on_light_blue", ["bold"]))
    print()
    tasks = view_all_tasks()
    if tasks is None:
        print("Press enter key to return to main menu...")
        input()
        return

    while True:
        to_remove = int(
            input(colored("Enter task number to remove: ", "blue")))
        if to_remove not in tasks:
            print(colored("Invalid task number...", "red"))
            continue
        break

    tasks.pop(to_remove)
    if file_handler.rewrite_tasks(tasks):
        print(colored("Successfully removed task!", "white", "on_green"))
        print()
        print("Press enter key to return to main menu...")
        input()
        return
    print(colored("Error while removing task!", "red"))
