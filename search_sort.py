def search_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    search = input("Enter task to search: ")
    found = False

    for task in tasks:
        if task.lower() == search.lower():
            print("Task found:", task)
            found = True

    if found == False:
        print("Task not found.")


def sort_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        sorted_tasks = sorted(tasks)

        print("\n===== SORTED TASKS =====")

        for task in sorted_tasks:
            print(task)


def sort_marks(marks):
    if len(marks) == 0:
        print("No marks available.")
    else:
        sorted_marks = sorted(marks)

        print("\n===== SORTED MARKS =====")

        for mark in sorted_marks:
            print(mark)


def search_sort_menu(tasks, marks):
    while True:
        print("\n===== SEARCH & SORT =====")
        print("1. Search Task")
        print("2. Sort Tasks")
        print("3. Sort Marks")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_task(tasks)
        elif choice == "2":
            sort_tasks(tasks)
        elif choice == "3":
            sort_marks(marks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")  

