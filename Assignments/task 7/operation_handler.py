import file_handler
from termcolor import colored

def view_all_tasks():
    tasks = file_handler.read_tasks()
    print()
    for numbr, name_and_disc in tasks.items():
        print(f"{numbr}: {name_and_disc[0]}\n{name_and_disc[1]}")
        print()

def add_task():
    name = input(colored("Enter Name: ", "light_blue"))
    desc = input(colored("Enter short description: ", "light_blue"))
    if file_handler.write_task(name=name, decs=desc):
        print(colored("Successfully added!", "green"))