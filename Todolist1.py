tasks = []
def load_tasks():
    """Loads tasks from a file when the programe starts."""

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

    except FileNotFoundError:
        pass

def save_tasks():
    """Saves tasks to a file before the programe exits."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")  


def show_tasks():
    if not tasks:
        print("No tasks available.")

    else:
        print("\nYour To-Do Lists:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {tasks}")

def add_tasks():
    task = input("Enter a new task:")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_tasks():
    show_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(index)
        print(f"Removed task: {removed_task}")

    except(ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    """Main menu loop."""
    load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print(" 1. View Tasks")
        print(" 2. Add Task")
        print(" 3. Remove Task")
        print(" 4. Exit" )

        choice = input("Choose an option:")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            remove_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        
if __name__ == "__main__":
    main()