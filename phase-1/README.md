# To-Do List CLI Application

This is a command-line interface (CLI) application for managing your to-do tasks. It allows you to add, view, update, mark as complete, and delete tasks.

## Project Structure

The project is structured into several key components:

-   `src/main.py`: The entry point of the application, responsible for initializing services and running the main CLI loop.
-   `src/cli/`: Contains modules related to the command-line interface, including menu display, input handling, and choice processing.
-   `src/models/`: Defines the `Task` data model and its associated logic, such as validation and serialization.
-   `src/services/`: Houses the core business logic, including `TaskRepository` for data persistence and `TaskService` for task management operations.
-   `tests/`: Contains unit and integration tests to ensure the application's functionality and reliability.

## Features

-   **Add Task:** Create new tasks with a title and optional description.
-   **View Tasks:** List all existing tasks with their details and status.
-   **Update Task:** Modify the title or description of an existing task.
-   **Mark Task as Complete:** Change the status of a task to "Complete".
-   **Delete Task:** Remove a task from the list.
-   **Exit:** Close the application.

## Getting Started

### Prerequisites

-   Python 3.x installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # On Windows
    source venv/bin/activate # On macOS/Linux
    ```

### Usage

To run the application, navigate to the project's root directory and execute:

```bash
python src/main.py
```

The application will present a menu with options to interact with your to-do list. Follow the on-screen prompts to manage your tasks.

## Running Tests

The project includes a suite of unit and integration tests. To run them, ensure you have `pytest` installed:

```bash
pip install pytest
```

Then, execute the tests from the project root directory:

```bash
pytest
```

## Contributing

(Future section for contribution guidelines)

## License

(Future section for licensing information)
