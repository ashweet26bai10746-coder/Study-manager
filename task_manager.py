tasks = []


def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
            def delete_task():
                view_tasks()

    if len(tasks) > 0:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(removed, "deleted successfully!")
        else:
            print("Invalid task number.")


def task_manager():
    while True:
        print("TASK MANAGER")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
