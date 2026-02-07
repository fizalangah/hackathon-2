# Feature Specification: In-Memory Todo CLI App

**Feature Branch**: `001-in-memory-todo-cli`
**Created**: 2026-02-07
**Status**: Draft
**Input**: User description: "# Specification: Phase I – In-Memory Todo CLI App ## Overview A command-line Todo application that allows users to manage tasks in memory. The application runs entirely in the console and exits without persistence. ## Functional Requirements ### Task Entity Each task must contain: - id (integer, auto-increment) - title (string, required) - description (string, optional) - completed (boolean) ### Features 1. Add Task - User can add a task with title and description. 2. View Tasks - Display all tasks with ID and completion status. 3. Update Task - Modify title and/or description of an existing task. 4. Delete Task - Remove a task by ID. 5. Mark Complete / Incomplete - Toggle task completion state. ## CLI Behavior - Menu-driven interface - Clear prompts and feedback - Graceful handling of invalid input ## Non-Functional Requirements - Python 3.13+ - Clean project structure - No external dependencies - Readable and maintainable code ## Out of Scope - File storage - Database - Authentication - Networking"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

As a user, I want to add a new task with a title and optional description so that I can keep track of my pending items.

**Why this priority**: Core functionality, essential for any todo app.

**Independent Test**: A task can be added and subsequently viewed.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I choose to add a task and provide a title "Buy groceries" and description "Milk, Eggs, Bread", **Then** the task "Buy groceries" is added to my todo list and is marked as incomplete.

---

### User Story 2 - View Tasks (Priority: P1)

As a user, I want to view all my tasks with their IDs and completion status so that I can see what I need to do.

**Why this priority**: Core functionality, essential for any todo app.

**Independent Test**: All added tasks are displayed correctly.

**Acceptance Scenarios**:

1. **Given** tasks "Buy groceries" (incomplete) and "Call mom" (complete) exist, **When** I choose to view tasks, **Then** both tasks are displayed with their respective IDs and completion status.

---

### User Story 3 - Update Task (Priority: P2)

As a user, I want to modify the title or description of an existing task so that I can correct or refine my task details.

**Why this priority**: Important for task management, but can come after basic add/view.

**Independent Test**: An existing task's details can be updated and verified.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists with title "Buy groceries", **When** I choose to update task 1 and change the title to "Buy organic groceries", **Then** task 1's title is updated to "Buy organic groceries".

---

### User Story 4 - Delete Task (Priority: P2)

As a user, I want to remove a task by its ID so that I can declutter my list of completed or irrelevant items.

**Why this priority**: Important for task management, but can come after basic add/view.

**Independent Test**: A task can be deleted and no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** I choose to delete task 1, **Then** task 1 is removed from the todo list.

---

### User Story 5 - Mark Complete / Incomplete (Priority: P1)

As a user, I want to mark a task as complete or incomplete so that I can track my progress.

**Why this priority**: Essential for task tracking.

**Independent Test**: A task's completion status can be toggled and verified.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 is incomplete, **When** I choose to mark task 1 as complete, **Then** task 1's status changes to complete.

### Edge Cases

- When a user tries to update/delete a non-existent task ID, the system MUST display a generic "Task not found" message.
- When a user provides invalid input (e.g., non-numeric ID, empty title), the system MUST simply re-display the prompt without explanation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with a title (required) and an optional description.
- **FR-002**: System MUST automatically assign a unique, auto-incrementing integer ID to each new task.
- **FR-003**: System MUST allow users to view all existing tasks, displaying their ID, title, and completion status.
- **FR-004**: System MUST allow users to update the title and/or description of an existing task by its ID.
- **FR-005**: System MUST allow users to delete a task by its ID.
- **FR-006**: System MUST allow users to toggle the completion status of a task by its ID.
- **FR-007**: System MUST provide a menu-driven command-line interface, presenting a numbered list of operations (e.g., 1. Add Task, 2. View Tasks, 3. Update Task, etc.), including an option to exit.
- **FR-008**: System MUST provide clear prompts and feedback to the user.
- **FR-009**: System MUST gracefully handle invalid user input (e.g., non-numeric input for ID, invalid menu choices).

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single todo item.
    *   `id`: Unique identifier (integer, auto-increment).
    *   `title`: Brief description of the task (string, required).
    *   `description`: Detailed description of the task (string, optional).
    *   `completed`: Status of the task (boolean, default to false).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully perform all five core task management operations (add, view, update, delete, mark complete/incomplete) through the CLI.
- **SC-002**: The application responds to all user commands within 1 second.
- **SC-003**: 100% of invalid user inputs are handled gracefully without crashing the application.

## Clarifications
### Session 2026-02-07
- Q: What are the main menu options for the CLI application? → A: A numbered list of operations (e.g., 1. Add Task, 2. View Tasks, 3. Update Task, etc.), with an option to exit.
- Q: How should the application respond when a user attempts to update or delete a non-existent task ID? → A: Display a generic "Task not found" message.
- Q: What specific feedback should be provided for invalid user input (e.g., non-numeric ID where an integer is expected, empty title)? → A: Simply re-display the prompt without explanation.