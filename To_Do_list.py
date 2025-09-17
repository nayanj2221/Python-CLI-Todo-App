import json

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            print("Tasks loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing task file found. Starting with an empty list.")
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        print("Tasks saved.")

# The rest of the functions (show_tasks, add_task, complete_task, delete_task, save_report_to_file)
# remain the same as in your original code. The changes are primarily in the main function.
# Please copy your original functions here.
# ... (your original functions) ...
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print(f"Task '{title}' added.")
    else:
        print("Task title cannot be empty.")

def complete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['title']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def save_report_to_file():
    if not tasks:
        print("No tasks to save.")
        return

    completed_count = sum(task['completed'] for task in tasks)
    remaining_count = len(tasks) - completed_count

    try:
        with open("task_report.txt", "w", encoding="utf-8") as file:
            file.write("Task Report\n")
            file.write("===========\n\n")
            for i, task in enumerate(tasks, 1):
                status = "Completed" if task['completed'] else "Pending"
                file.write(f"{i}. [{status}] {task['title']}\n")

            file.write("\n")
            file.write(f"Total tasks: {len(tasks)}\n")
            file.write(f"Completed tasks: {completed_count}\n")
            file.write(f"Remaining tasks: {remaining_count}\n")

        print("Task report saved to 'task_report.txt'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    load_tasks() # Load tasks at the start

    while True:
        print("\nTask Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save Task Report to File")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
            save_tasks() # Save after adding
        elif choice == '3':
            complete_task()
            save_tasks() # Save after completing
        elif choice == '4':
            delete_task()
            save_tasks() # Save after deleting
        elif choice == '5':
            save_report_to_file()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()