from termcolor import colored
import os
import operation_handler

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_console()
    print(colored("Welcome to Task Manager:-", "yellow", None, ["bold"]))
    print()
    choise = 0
    while(True):
        print(colored("Main Menu:", "blue", None, ["underline", "bold"]))
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Update a task")
        print("4. View tasks")
        print(colored("5. Exit", "red"))
        print()
        choise = int(input(colored("choise: ", "green")))
        
        match choise:
            case 1:
                clear_console()
                operation_handler.add_task()
                clear_console()
            case 2:
                clear_console()
                operation_handler.remove_task()
                clear_console()
            case 3:
                clear_console()
                operation_handler.update_task()
                clear_console()
            case 4:
                clear_console()
                operation_handler.view_all_tasks()
            case 5:
                print(colored("Exiting... Good Bye...", "black", "on_light_yellow"))
                break

            case _:
                clear_console()
                print(colored("Invalid input!!\nTry again!", "light_magenta"))
                print()
                continue


main()