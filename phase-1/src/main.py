import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.services.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.cli.menu import display_menu, get_menu_choice, handle_menu_choice

def main():
    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 6: # Exit option
            break
        
        handle_menu_choice(choice, task_service)

if __name__ == "__main__":
    main()