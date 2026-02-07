# The Evolution of Todo (Phase I) Constitution

<!-- 
Sync Impact Report:
- Version change: none -> 1.0.0
- List of modified principles: none
- Added sections: Core Principles, Technology Stack & Constraints, Core Features, Governance
- Removed sections: none
- Templates requiring updates:
- Follow-up TODOs: none
-->

## Core Principles

### I. Architecture Principles
- **Modularity:** Code must be organized into clean, single-purpose functions (e.g., `add_task`, `view_tasks`).
- **State Management:** Global state (the list of tasks) should be managed cleanly, preferably passed as arguments or contained within a Service class.
- **Error Handling:** The app must not crash on invalid input. It should catch errors (e.g., entering text instead of a Task ID) and show friendly messages.
- **User Experience:** The application must run in a continuous loop (Interactive Menu) until the user explicitly selects "Exit".

### II. Development Workflow (Spec-Driven)
- **Zero-Inference Rule:** AI Agents must strictly follow the requirements defined in `speckit.specify.md` and `speckit.plan.md`. Do not invent features not requested.
- **Task-Based Implementation:** No code is written unless it maps to a specific Task ID in `speckit.tasks.md`.
- **Code Style:** Follow PEP 8 standards. Use Python Type Hints (e.g., `def add_task(title: str) -> dict:`) for clarity.

## Technology Stack & Constraints
- **Language:** Python 3.13+
- **Interface:** Command Line Interface (CLI) / Console App
- **Data Storage:** In-Memory only (Python Lists/Dictionaries).
    - *Constraint:* No external database (SQL/NoSQL) or file persistence (JSON/TXT) is allowed in this phase. Data is lost when the app exits.
- **Package Manager:** UV (if external packages are needed, though standard library is preferred for Phase I).

## Core Features (Non-Negotiable)
1.  **Add Task:** Must capture a Title (required) and Description (optional). Auto-generate a unique ID.
2.  **View Tasks:** Display ID, Title, and Status (Pending/Completed).
3.  **Update Task:** Modify Title or Description by ID.
4.  **Delete Task:** Remove task by ID.
5.  **Mark Complete:** Toggle status to "Completed".

## Governance
This constitution is the single source of truth for project principles and architecture. All development artifacts, including specifications, plans, and code, must adhere to it. Amendments require a documented proposal and review.

**Version**: 1.0.0 | **Ratified**: 2026-01-19 | **Last Amended**: 2026-01-19