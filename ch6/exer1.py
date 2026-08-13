# **To-Do List (console-based)** — Let the user add, remove, and view tasks in a loop until they type "quit." Store tasks in a list.

task_choice = ["Add task", "Remove task", "View tasks", "Quit"]
to_do = []
user_str = ""

while True:
    for i, choice in enumerate(task_choice):
        print(f"{i}: {choice}")
    print("---------------------------------------")
    user_input = int(input("Enter user input (number): "))

    match user_input:
        case 0:
            user_str = str(input("Enter task to add: "))
            to_do.append(user_str)
            print("Task added")
        case 1:
            user_str = str(input("Enter task to remove: "))
            to_do.remove(user_str)
            print("Task removed")
        case 2:
            print(to_do)
            print("Task viewed")
        case 3:
            print("Quit")
            break
        case _:
            print("Invalid input. Try again")
            continue