# Tasks: Core Todo App Features

**Input**: Design documents from `specs/001-core-todo-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create `src/`, `tests/`, `src/services/`, `src/models/`, `src/cli/` directories
- [x] T002 Initialize Python project (e.g., create `__init__.py` files in `src/`, `src/services/`, `src/models/`, `src/cli/`, `tests/`, `tests/unit/`, `tests/integration/`)
- [x] T003 [P] Configure `pytest` for testing (e.g., `pytest.ini` or basic test setup)
- [x] T004 [P] Create `utils.py` for common utility functions in `src/services/utils.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create `Task` entity class/dictionary structure in `src/models/task.py`
- [x] T006 [P] Implement `Task` validation logic (e.g., `validate_task_title` to ensure non-empty) in `src/models/task.py`
- [x] T007 [P] Create `TaskRepository` class for in-memory storage (list/dict based) in `src/services/task_repository.py`
- [x] T008 [P] Implement `generate_unique_id` function in `src/services/utils.py`
- [x] T009 [P] Write unit tests for `Task` entity validation in `tests/unit/test_task_model.py`
- [x] T010 [P] Write unit tests for `generate_unique_id` in `tests/unit/test_utils.py`
- [x] T011 [P] Write unit tests for `TaskRepository` methods (init, add, get_all) in `tests/unit/test_task_repository.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel ✅

---

## Phase 3: User Story 1 - Add a New Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their todo list.

**Independent Test**: Add a task, then view the task list to confirm its presence.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [P] [US1] Write unit test for `add_task` function (success case) in `tests/unit/test_task_service.py`
- [x] T013 [P] [US1] Write unit test for `add_task` function (empty title error) in `tests/unit/test_task_service.py`
- [x] T014 [P] [US1] Write integration test for CLI "Add Task" flow in `tests/integration/test_cli_add_task.py`

### Implementation for User Story 1

- [x] T015 [US1] Create `TaskService` class with `add_task` method in `src/services/task_service.py`
- [x] T016 [US1] Implement CLI menu option for "Add Task" in `src/cli/menu.py`
- [x] T017 [US1] Implement user input handling for `add_task` (title, description) in `src/cli/input_handler.py`
- [x] T018 [US1] Integrate `TaskService.add_task` with CLI input and output in `src/cli/menu.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently ✅

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to view all their tasks with their status.

**Independent Test**: Add multiple tasks, then view the task list to confirm all tasks are displayed correctly.

### Tests for User Story 2 ⚠️

- [x] T019 [P] [US2] Write unit test for `get_all_tasks` function (with tasks) in `tests/unit/test_task_service.py`
- [x] T020 [P] [US2] Write unit test for `get_all_tasks` function (no tasks) in `tests/unit/test_task_service.py`
- [x] T021 [P] [US2] Write integration test for CLI "View Tasks" flow in `tests/integration/test_cli_view_tasks.py`

### Implementation for User Story 2

- [x] T022 [US2] Implement `get_all_tasks` method in `src/services/task_service.py`
- [x] T023 [US2] Implement CLI menu option for "View Tasks" in `src/cli/menu.py`
- [x] T024 [US2] Implement task display formatting in `src/cli/output_formatter.py`
- [x] T025 [US2] Integrate `TaskService.get_all_tasks` with CLI output in `src/cli/menu.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently ✅

---

## Phase 5: User Story 3 - Update an Existing Task (Priority: P2)

**Goal**: Allow users to update the title or description of an existing task.

**Independent Test**: Create a task, then update its title and/or description, and finally view the task to verify the changes.

### Tests for User Story 3 ⚠️

- [x] T026 [P] [US3] Write unit test for `update_task` (success case) in `tests/unit/test_task_service.py`
- [x] T027 [P] [US3] Write unit test for `update_task` (task not found) in `tests/unit/test_task_service.py`
- [x] T028 [P] [US3] Write unit test for `update_task` (empty title error) in `tests/unit/test_task_service.py`
- [x] T029 [P] [US3] Write integration test for CLI "Update Task" flow in `tests/integration/test_cli_update_task.py`

### Implementation for User Story 3

- [x] T030 [US3] Implement `update_task` method in `src/services/task_service.py`
- [x] T031 [US3] Implement CLI menu option for "Update Task" in `src/cli/menu.py`
- [x] T032 [US3] Implement user input for `update_task` (Task ID, new title/description) in `src/cli/input_handler.py`
- [x] T033 [US3] Integrate `TaskService.update_task` with CLI input/output in `src/cli/menu.py`

**Checkpoint**: All user stories should now be independently functional ✅

---

## Phase 6: User Story 4 - Delete an Existing Task (Priority: P2)

**Goal**: Allow users to delete tasks from their todo list.

**Independent Test**: Create a task, then delete it, and finally view the task list to confirm its removal.

### Tests for User Story 4 ⚠️

- [x] T034 [P] [US4] Write unit test for `delete_task` (success case) in `tests/unit/test_task_service.py`
- [x] T035 [P] [US4] Write unit test for `delete_task` (task not found) in `tests/unit/test_task_service.py`
- [x] T036 [P] [US4] Write integration test for CLI "Delete Task" flow in `tests/integration/test_cli_delete_task.py`

### Implementation for User Story 4

- [x] T037 [US4] Implement `delete_task` method in `src/services/task_service.py`
- [x] T038 [US4] Implement CLI menu option for "Delete Task" in `src/cli/menu.py`
- [x] T039 [US4] Implement user input for `delete_task` (Task ID) in `src/cli/input_handler.py`
**Checkpoint**: All user stories should now be independently functional ✅

---

## Phase 7: User Story 5 - Mark a Task as Complete (Priority: P2)

**Goal**: Allow users to mark a task as complete.

**Independent Test**: Create a task, then mark it complete, and finally view the task to verify its status has changed.

### Tests for User Story 5 ⚠️

- [x] T041 [P] [US5] Write unit test for `mark_task_complete` (success case) in `tests/unit/test_task_service.py`
- [x] T042 [P] [US5] Write unit test for `mark_task_complete` (task not found) in `tests/unit/test_task_service.py`
- [x] T043 [P] [US5] Write unit test for `mark_task_complete` (already complete) in `tests/unit/test_task_service.py`
- [x] T044 [P] [US5] Write integration test for CLI "Mark Complete" flow in `tests/integration/test_cli_mark_complete.py`

### Implementation for User Story 5

- [x] T045 [US5] Implement `mark_task_complete` method in `src/services/task_service.py`
- [x] T046 [US5] Implement CLI menu option for "Mark Complete" in `src/cli/menu.py`
- [x] T047 [US5] Implement user input for `mark_task_complete` (Task ID) in `src/cli/input_handler.py`
**Checkpoint**: All user stories should now be independently functional ✅

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T049 Implement main application loop and menu display in `src/main.py`
- [x] T050 Implement robust error handling for user input (e.g., `ValueError` for non-numeric IDs) in `src/cli/input_handler.py`
- [x] T051 Implement "Exit" option in the main menu loop in `src/cli/menu.py`
- [x] T052 Add overall integration test for continuous menu operation and exit in `tests/integration/test_cli_main_loop.py`
- [x] T053 Refactor and clean up code for PEP 8 compliance and type hinting enforcement

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
-   **User Stories (Phase 3+)**: All depend on Foundational phase completion
    -   User stories can then proceed in parallel (if staffed)
    -   Or sequentially in priority order (P1 → P2 → P3)
-   **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
-   **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
-   **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

-   Tests MUST be written and FAIL before implementation
-   CLI input/output handling should follow service implementation
-   Core implementation before integration

### Parallel Opportunities

-   All Setup tasks marked [P] can run in parallel
-   All Foundational tasks marked [P] can run in parallel (within Phase 2)
-   Once Foundational phase completes, User Stories 1 and 2 can start in parallel (P1 priority)
-   Once Foundational phase completes, User Stories 3, 4, and 5 can start in parallel after P1 stories (P2 priority)
-   All tests for a user story marked [P] can run in parallel
-   Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 & 2 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  Complete Phase 4: User Story 2
5.  **STOP and VALIDATE**: Test User Stories 1 & 2 independently
6.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Add User Story 4 → Test independently → Deploy/Demo
6.  Add User Story 5 → Test independently → Deploy/Demo
7.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
    -   Developer C: User Story 3
    -   Developer D: User Story 4
    -   Developer E: User Story 5
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence