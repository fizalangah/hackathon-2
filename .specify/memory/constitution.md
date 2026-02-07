<!--
Sync Impact Report:
- Version change: 0.0.0 -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> Spec First, Always
  - [PRINCIPLE_2_NAME] -> No Manual Coding
  - [PRINCIPLE_3_NAME] -> Incremental Evolution
  - [PRINCIPLE_4_NAME] -> Clean Architecture
  - [PRINCIPLE_5_NAME] -> Simplicity First
  - [PRINCIPLE_6_NAME] -> Traceability
- Added sections:
  - Purpose
  - Constraints
  - Success Criteria
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Project Constitution – The Evolution of Todo

## Purpose
This project exists to demonstrate spec-driven, AI-assisted software development.
No manual boilerplate coding is allowed. All code must be generated through AI
using specifications, plans, and task breakdowns.

## Core Principles
### 1. Spec First, Always
   - No implementation without an approved specification.
### 2. No Manual Coding
   - All code must be generated via AI (Claude Code / Gemini).
### 3. Incremental Evolution
   - Each phase builds on the previous one.
### 4. Clean Architecture
   - Separation of concerns (models, services, CLI).
### 5. Simplicity First
   - Prefer clarity over cleverness.
### 6. Traceability
   - Every feature must map back to a spec and task.

## Constraints
- Phase I must remain in-memory only.
- No database, no files, no external services.
- CLI-based interaction only.

## Success Criteria
- Fully working CLI Todo App
- All 5 basic features implemented
- Clear spec → plan → tasks → implementation trail

## Governance
This constitution is the single source of truth for project principles and constraints. All development activities must adhere to it. Amendments require team consensus and must be documented in a new version of this constitution.

**Version**: 1.0.0 | **Ratified**: 2026-02-07 | **Last Amended**: 2026-02-07