def get_string_input(prompt: str, allow_empty: bool = False) -> str:
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        else:
            print("Input cannot be empty. Please try again.")

def get_task_details() -> tuple[str, str]:
    title = get_string_input("Enter task title: ")
    description = get_string_input("Enter task description (optional): ", allow_empty=True)
    return title, description

def get_task_id_input() -> str:
    while True:
        task_id = input("Enter Task ID: ").strip()
        if task_id:
            return task_id
        else:
            print("Task ID cannot be empty.")
            