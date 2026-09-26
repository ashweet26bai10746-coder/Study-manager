from task_manager import task_manager, tasks 
from performance import performance_analyzer, marks
from search_sort import search_sort_menu

def main():
  
       while True:
        print("STUDENT STUDY AND TASK MANAGER SYSTEM")
        print("1. Task Manager")
        print("2. Performance Analyzer")
        print("3. Search and Sort")
        print("4. Exit")

        choice=input('enter your choice:')

        if choice == "1":
            task_manager()
            print("Task Manager selected")

        elif choice == "2":
            performance_analyzer()
            print("Performance Analyzer selected")

        elif choice == "3":
            search_sort_menu(tasks, marks)
            print("Search and Sort selected")

        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print('invalid choice , please try again')


main()


