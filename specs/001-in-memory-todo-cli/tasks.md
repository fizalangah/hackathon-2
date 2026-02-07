# Tasks: In-Memory Todo CLI App

**Input**: Design documents from `specs/001-in-memory-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Tests**: The feature specification does not explicitly request TDD, so tests are not included as separate tasks in this list. Validation will occur through manual CLI testing as per the plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure `src/todo_app/` with `__init__.py` files.
- [ ] T002 Initialize Python environment (Python 3.13+) and virtual environment.

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 Define `Task` class in `src/todo_app/models/task.py`.
- [ ] T004 Implement in-memory `TaskCollection` (or similar data structure) in `src/todo_app/services/task_repository.py` to manage `Task` objects, including ID generation.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add a new task with a title and optional description.

**Independent Test**: A task can be added and subsequently viewed via the CLI.

### Implementation for User Story 1

- [ ] T005 [P] [US1] Add `add_task` method to `src/todo_app/services/task_service.py` to handle adding new tasks.
- [ ] T006 [P] [US1] Implement CLI function to prompt for task title and description in `src/todo_app/cli/commands.py`.
- [ ] T007 [US1] Integrate `add_task` CLI command with `task_service` in `src/todo_app/cli/app.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Allow users to view all existing tasks with their ID and completion status.

**Independent Test**: All added tasks are displayed correctly via the CLI.

### Implementation for User Story 2

- [ ] T008 [P] [US2] Add `list_tasks` method to `src/todo_app/services/task_service.py` to retrieve all tasks.
- [ ] T009 [P] [US2] Implement CLI function to display tasks in a user-friendly format in `src/todo_app/cli/commands.py`.
- [ ] T010 [US2] Integrate `list_tasks` CLI command with `task_service` in `src/todo_app/cli/app.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

## Phase 5: User Story 5 - Mark Complete / Incomplete (Priority: P1)

**Goal**: Allow users to toggle the completion status of an existing task.

**Independent Test**: A task's completion status can be toggled and verified via the CLI.

### Implementation for User Story 5

- [ ] T011 [P] [US5] Add `toggle_task_status` method to `src/todo_app/services/task_service.py` to change task completion status.
- [ ] T012 [P] [US5] Implement CLI function to prompt for task ID and call `toggle_task_status` in `src/todo_app/cli/commands.py`.
- [ ] T013 [US5] Integrate `toggle_task_status` CLI command with `task_service` in `src/todo_app/cli/app.py`.

**Checkpoint**: All P1 user stories should now be independently functional

## Phase 6: User Story 3 - Update Task (Priority: P2)

**Goal**: Allow users to modify the title and/or description of an existing task.

**Independent Test**: An existing task's details can be updated and verified via the CLI.

### Implementation for User Story 3

- [ ] T014 [P] [US3] Add `update_task` method to `src/todo_app/services/task_service.py` to modify task details.
- [ ] T015 [P] [US3] Implement CLI function to prompt for task ID, new title, and description in `src/todo_app/cli/commands.py`.
- [ ] T016 [US3] Integrate `update_task` CLI command with `task_service` in `src/todo_app/cli/app.py`.

**Checkpoint**: At this point, User Stories 1, 2, 5, AND 3 should all work independently

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to remove a task by its ID.

**Independent Test**: A task can be deleted and no longer appears in the list via the CLI.

### Implementation for User Story 4

- [ ] T017 [P] [US4] Add `delete_task` method to `src/todo_app/services/task_service.py` to remove a task.
- [ ] T018 [P] [US4] Implement CLI function to prompt for task ID and call `delete_task` in `src/todo_app/cli/commands.py`.
- [ ] T019 [US4] Integrate `delete_task` CLI command with `task_service` in `src/todo_app/cli/app.py`.

**Checkpoint**: All user stories should now be independently functional

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T020 Implement main CLI loop and menu rendering in `src/todo_app/cli/app.py`.
- [ ] T021 Implement graceful handling of invalid user input in `src/todo_app/cli/app.py` and `src/todo_app/cli/commands.py`.
- [ ] T022 Ensure clear prompts and feedback in `src/todo_app/cli/commands.py` and `src/todo_app/cli/app.py`.
- [ ] T023 Manual CLI testing to ensure all spec requirements are met.
- [ ] T024 Review code for clean project structure, readability, and maintainability.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1, US2, US5 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1, US2, US5 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI functions
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Within each user story, tasks marked [P] can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1, 2, 5 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. Complete Phase 5: User Story 5
6. **STOP and VALIDATE**: Test User Stories 1, 2, and 5 independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 5 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 5
   - Developer D: User Story 3
   - Developer E: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify features work before moving on
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
