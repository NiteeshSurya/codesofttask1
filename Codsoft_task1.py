import sys

# A simple in-memory storage for to-do items
to_do_list = []

def add_task():
    print("\nAdd New Task")
    task = input("Enter task description: ")
    to_do_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not to_do_list:
        print("\nNo tasks available.")
        return
    
    print("\nTo-Do List:")
    for idx, item in enumerate(to_do_list, start=1):
        status = "Completed" if item["completed"] else "Pending"
        print(f"{idx}. {item['task']} - {status}")

def update_task():
    view_tasks()
    if not to_do_list:
        return
    
    try:
        task_number = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_number < len(to_do_list):
            new_description = input("Enter new task description (leave blank to keep current): ")
            if new_description:
                to_do_list[task_number]["task"] = new_description
            
            status = input("Is the task completed? (yes/no): ").lower()
            to_do_list[task_number]["completed"] = True if status == "yes" else False
            
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not to_do_list:
        return
    
    try:
        task_number = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_number < len(to_do_list):
            del to_do_list[task_number]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
