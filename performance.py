marks = []


def add_marks():
    marks.clear()

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    print("Marks added successfully!")


def view_marks():
    if len(marks) == 0:
        print("No marks available.")
    else:
        print("\n===== MARKS =====")

        for i in range(len(marks)):
            print("Subject", i + 1, ":", marks[i])


def calculate_average():
    if len(marks) == 0:
        print("No marks available.")
    else:
        total = 0

        for mark in marks:
            total = total + mark

        average = total / len(marks)

        print("Average marks:", average)


def highest_lowest():
    if len(marks) == 0:
        print("No marks available.")
    else:
        print("Highest marks:", max(marks))
        print("Lowest marks:", min(marks))


def performance_category():
    if len(marks) == 0:
        print("No marks available.")
    else:
        total = 0

        for mark in marks:
            total = total + mark

        average = total / len(marks)

        if average >= 90:
            category = "Excellent"
        elif average >= 75:
            category = "Very Good"
        elif average >= 60:
            category = "Good"
        elif average >= 40:
            category = "Pass"
        else:
            category = "Needs Improvement"

        print("Average:", average)
        print("Performance:", category)


def performance_analyzer():
    while True:
        print("\n===== PERFORMANCE ANALYZER =====")
        print("1. Enter Marks")
        print("2. View Marks")
        print("3. Calculate Average")
        print("4. Highest and Lowest Marks")
        print("5. Performance Category")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_marks()
        elif choice == "2":
            view_marks()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            highest_lowest()
        elif choice == "5":
            performance_category()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
