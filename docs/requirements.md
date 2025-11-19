# Requirements Specification – TaskFlow

## Functional Requirements
1. Users can create tasks with title + description.
2. Users can edit existing tasks.
3. Users can delete tasks.
4. Users can mark a task as completed.
5. Tasks are stored persistently.

## Non-Functional Requirements
- Simple and intuitive UI
- Fast response time (<200ms per request)
- Code readability & maintainability
- Cross-platform (Windows/Linux/Mac)

## Constraints
- Python Flask for fast prototyping
- SQLite as simple local persistence layer
