# Task Tracker

A simple command-line task tracker built with Python and JSON.

The project allows you to create, list, update, delete, and change the status of tasks. It supports both **interactive CLI mode** and **direct command execution**.

## Features

- Create tasks
- List all tasks
- Filter tasks by status
- Update task descriptions
- Change task status
- Delete tasks
- Persistent data storage using JSON
- Unique task IDs
- Interactive CLI mode
- Direct command-line mode
- No external dependencies

## Requirements

- Python 3.8+

The project only uses Python's standard library, so no additional packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/Vini-23/task-tracker.git
```

Enter the project directory:

```bash
cd task-tracker
```

No installation or dependency setup is required.

## Data Storage

Tasks are stored in the `tasks.json` file.

Example:

```json
{
    "tasks": [
        {
            "id": 1,
            "description": "Study Python",
            "status": "todo",
            "createdAt": "2026-08-11",
            "updatedAt": "2026-08-11"
        }
    ]
}
```

The available task statuses are:

- `todo`
- `in-progress`
- `done`

Task IDs are automatically generated and are not reused after a task is deleted.

## Usage

The application can be used in two different ways.

### Interactive Mode

Start the application without any arguments:

```bash
python3 tasks.py
```

You will enter the interactive CLI:

```text
********************
*** Task Tracker ***
********************

Type 'help' for available commands.

> list
ID    | Description                    | Status
============================================================
1     | Study Python                   | todo

> add Study JSON

Task added successfully!

> change_status 2 done

Task status updated successfully!

> delete 1

Task deleted successfully!

> exit

Goodbye!
```

### Available Commands

#### List Tasks

List all tasks:

```text
> list
```

Filter by status:

```text
> list todo
> list in-progress
> list done
```

#### Add a Task

```text
> add <description>
```

Example:

```text
> add Study Python
```

#### Update a Task

Update the description of an existing task:

```text
> update <task_id> <new_description>
```

Example:

```text
> update 1 Study Python and JSON
```

#### Change Task Status

```text
> change_status <task_id> <status>
```

Example:

```text
> change_status 1 in-progress
```

Available statuses:

```text
todo
in-progress
done
```

#### Delete a Task

```text
> delete <task_id>
```

Example:

```text
> delete 1
```

#### Help

Display the available commands:

```text
> help
```

#### Exit

Close the interactive CLI:

```text
> exit
```

---

## Direct Command Mode

Commands can also be executed directly from the terminal without entering interactive mode.

### List

```bash
python3 tasks.py list
```

Filter by status:

```bash
python3 tasks.py list todo
```

### Add

```bash
python3 tasks.py add "Study Python"
```

### Update

```bash
python3 tasks.py update 1 "Study Python and JSON"
```

### Change Status

```bash
python3 tasks.py change_status 1 done
```

### Delete

```bash
python3 tasks.py delete 1
```

This makes it possible to use the application either interactively or as a traditional command-line utility.

## Project Structure

```text
task-tracker/
├── tasks.py
├── tasks.json
└── README.md
```

### `tasks.py`

Contains the task management logic and command-line interface.

### `tasks.json`

Stores all tasks and their information.

### `README.md`

Project documentation.

## How It Works

The project is divided into two main parts.

### `Tasks`

The `Tasks` class is responsible for managing the task data.

It handles:

- Loading tasks from the JSON file
- Creating tasks
- Finding tasks by ID
- Updating tasks
- Deleting tasks
- Changing task statuses
- Saving changes to the JSON file

### Command Handler

The command handler interprets user commands and calls the appropriate method from the `Tasks` class.

For example:

```text
> add Study Python
```

is interpreted as:

```text
command = add
arguments = ["Study", "Python"]
```

The description is then passed to:

```python
tasks.add_task("Study Python")
```

## Data Persistence

Changes are automatically saved to `tasks.json`.

The application loads the JSON data when it starts and writes the updated data back to the file whenever a task is created, updated, deleted, or has its status changed.

## Future Improvements

Some possible improvements for future versions:

- Add task priorities
- Add due dates
- Add task categories/tags
- Add task search
- Add confirmation before deleting tasks
- Improve command validation
- Add command history
- Add tab completion
- Add automated tests
- Separate the CLI and task-management logic into different modules
- Replace the JSON storage with a database
- Package the project as an installable CLI application
