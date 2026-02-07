from src.services.task_service import TaskService
from src.cli.input_handler import get_task_details, get_task_id_input, get_string_input
from src.cli.output_formatter import display_tasks

def display_menu():
    print("\nTodo App Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Exit")

def get_menu_choice():
    while True:
        choice = input("Enter your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_menu_choice(choice: int, task_service: TaskService):
    if choice == 1:
        print("\n--- Add New Task ---")
        try:
            title, description = get_task_details()
            new_task = task_service.add_task(title, description)
            print(f"Task '{new_task.title}' added with ID: {new_task.id}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == 2:
        print("\n--- Your Tasks ---")
        tasks = task_service.get_all_tasks()
        display_tasks(tasks)
    elif choice == 3:
        print("\n--- Update Task ---")
        task_id = get_task_id_input()
        if not task_id:
            print("Task ID cannot be empty.")
            return

        print("Enter new title (leave blank to keep current):")
        new_title = get_string_input("New Title: ", allow_empty=True)
        print("Enter new description (leave blank to keep current):")
        new_description = get_string_input("New Description: ", allow_empty=True)

        if not new_title and not new_description:
            print("No updates provided.")
            return

        try:
            updated_task = task_service.update_task(task_id, new_title if new_title else None, new_description if new_description else None)
            if updated_task:
                print(f"Task with ID {task_id} updated successfully.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error updating task: {e}")
    elif choice == 4:
        print("\n--- Delete Task ---")
        task_id = get_task_id_input()
        if not task_id:
            print("Task ID cannot be empty.")
            return
        
        if task_service.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    elif choice == 5:
        print("\n--- Mark Task Complete ---")
        task_id = get_task_id_input()
        if not task_id:
            print("Task ID cannot be empty.")
            return
        
        try:
            completed_task = task_service.mark_task_complete(task_id)
            if completed_task:
                if completed_task.status == "Completed":
                    print(f"Task with ID {task_id} marked as 'Completed'.")
                else:
                    print(f"Task with ID {task_id} was already 'Completed'.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error marking task complete: {e}")
    elif choice == 6:
        print("Exiting Todo App.")
    else:
        print(f"Choice {choice} selected (Not yet implemented fully)")