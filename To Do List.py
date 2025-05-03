def menu():
    # Displays the menu options for the user
    print("\nTo-Do List Menu")
    print("1. Add Task")  # Option to add a new task
    print("2. Show Tasks")  # Option to show all tasks
    print("3. Complete Task")  # Option to mark a task as completed
    print("4. Remove Task")  # Option to remove a task
    print("5. Quit")  # Option to quit the program

def add_task(tasks):
    # Defines the "add_task" function, which takes the (tasks) dictionary as input
    name = input("Enter task name: ")  # Prompts the user to enter the task name
    tasks[name] = {"completed": False}  # Adds the task to the dictionary
    # The task name (input by the user) is the key
    # The value is a dictionary containing a completion status (False initially)

def show_tasks(tasks):
    # Defines the "show_tasks" function, which displays all tasks in the dictionary
    if not tasks:  # Checks if there are no tasks
        print("No tasks to show.")  # Prints a message if no tasks exist
    for task, details in tasks.items():  # Loops through each task in the dictionary
        status = "Completed" if details["completed"] else "Pending"  # Determines if the task is completed
        print(f"{task}:{status}")  # Prints task details (name, description, status)

def complete_task(tasks):
    # Defines the "complete_task" function, which allows the user to mark a task as completed
    task_name = input("Enter task name to mark as completed: ")  # Prompts the user to enter the task name
    if task_name in tasks:  # Checks if the task exists in the dictionary
        tasks[task_name]["completed"] = True  # Sets the task's completion status to True
        print(f"Task '{task_name}' marked as completed.")  # Prints a confirmation message
    else:
        print(f"Task '{task_name}' not found.")  # Prints an error message if the task isn't found

def remove_task(tasks):
    # Defines the "remove_task" function, which allows the user to remove a task
    task_name = input("Enter task name to remove: ")  # Prompts the user to enter the task name
    if task_name in tasks:  # Checks if the task exists in the dictionary
        del tasks[task_name]  # Deletes the task from the dictionary
        print(f"Task '{task_name}' removed.")  # Prints a confirmation message
    else:
        print(f"Task '{task_name}' not found.")  # Prints an error message if the task isn't found

def main():
    # Defines the "main" function, which controls the flow of the program
    tasks = {}  # Initializes an empty dictionary to store tasks
    while True:  # Starts an infinite loop to keep the program running
        menu()  # Displays the menu options
        choice = input("Choose an option: ")  # Prompts the user to choose an option
        if choice == '1':  # If the user chooses option 1 (Add Task)
            add_task(tasks)  # Calls the "add_task" function
        elif choice == '2':  # If the user chooses option 2 (Show Tasks)
            show_tasks(tasks)  # Calls the "show_tasks" function
        elif choice == '3':  # If the user chooses option 3 (Complete Task)
            complete_task(tasks)  # Calls the "complete_task" function
        elif choice == '4':  # If the user chooses option 4 (Remove Task)
            remove_task(tasks)  # Calls the "remove_task" function
        elif choice == '5':  # If the user chooses option 5 (Quit)
            print("Goodbye!")  # Prints a goodbye message
            break  # Exits the loop and ends the program
        else:
            print("Invalid option. Please try again.")  # Prints an error message for invalid input

# Starts the program by calling the "main" function
main()
