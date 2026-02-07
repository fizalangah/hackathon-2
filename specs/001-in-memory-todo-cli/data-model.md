# Data Model: In-Memory Todo CLI App

## Entity: Task

Represents a single todo item managed by the CLI application.

### Attributes:

*   **`id`**:
    *   **Type**: Integer
    *   **Constraints**: Unique, auto-incrementing.
    *   **Description**: A unique identifier for the task.
*   **`title`**:
    *   **Type**: String
    *   **Constraints**: Required, non-empty.
    *   **Description**: A brief, descriptive title for the task.
*   **`description`**:
    *   **Type**: String
    *   **Constraints**: Optional.
    *   **Description**: A detailed description of the task.
*   **`completed`**:
    *   **Type**: Boolean
    *   **Default**: `false`
    *   **Description**: Indicates whether the task has been completed.

### Relationships:

*   None (stand-alone entity for an in-memory application).