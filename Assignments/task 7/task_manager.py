from termcolor import colored
import os
import operation_handler

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_console()
    print(colored("Welcome to Task Manager:-", "yellow"))
    print()
    choise = 0
    while(True):
        print(colored("Main Menu:", "blue"))
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Update a task")
        print("4. View tasks")
        print(colored("5. Exit", "red"))
        print()
        choise = int(input(colored("choise: ", "green")))
        
        match choise:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                operation_handler.view_all_tasks()
            case 5:
                print(colored("Exiting... Good Bye...", "yellow"))
                break

            case _:
                clear_console()
                print(colored("Invalid input!!\nTry again!", "light_magenta"))
                print()
                continue


main()