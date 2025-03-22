import file_handler

def view_all_tasks():
    tasks = file_handler.read_tasks()
    print()
    for numbr, name_and_disc in tasks.items():
        name = name_and_disc[0]
        disc = name_and_disc[1]
        print(f"{numbr}: {name}\n{disc}")
        print()