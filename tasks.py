import sys
import json
from datetime import datetime

DATA_FILE = "tasks.json"
TASKS_STATUS = {"todo", "in-progress", "done"}

class Tasks:
    def __init__(self):
        with open(DATA_FILE, "r") as file:
            self.data = json.load(file)


    def _find_task(self, task_id):
        return next(
            (task for task in self.data["tasks"] if task["id"] == task_id),
            None
        )

    def _save(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)


    def list_tasks(self, status=None):
        if status and status not in TASKS_STATUS:
            print("Invalid status. Please use 'todo', 'in-progress', 'done', or leave it empty.")
            return

        print(f"{'ID':<5} | {'Description':<30} | {'Status':<10}")
        print("=" * 60)
        for task in self.data["tasks"]:
            if status is None or task["status"] == status:
                print(
                    f"{task['id']:<5} | "
                    f"{task['description']:<30} | "
                    f"{task['status']:<10}"
                )


    def add_task(self, task):
        new_id = max(
            (task["id"] for task in self.data["tasks"]), default=0
        ) + 1

        new_task = {
            "id": new_id,
            "description": task,
            "status": "todo",
            "createdAt": datetime.today().strftime("%Y-%m-%d"),
            "updatedAt": datetime.today().strftime("%Y-%m-%d")
        }

        self.data["tasks"].append(new_task)
        self._save()

        print("\nTask added successfully!\n")


    def update_task(self, task_id, new_description):
        task = self._find_task(task_id)
        if task is None:
            print("Invalid task ID.")
            return

        task["description"] = new_description
        task["updatedAt"] = datetime.today().strftime("%Y-%m-%d")
        self._save()

        print("\nTask updated successfully!\n")


    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            print("Invalid task ID.")
            return

        self.data["tasks"].remove(task)
        self._save()

        print("\nTask deleted successfully!\n")


    def change_task_status(self, task_id, new_status):
        task = self._find_task(task_id)
        if task is None:
            print("Invalid task ID.")
            return

        if new_status not in TASKS_STATUS:
            print("Invalid status. Please use 'todo', 'in-progress' or 'done'.")
            return

        task["status"] = new_status
        task["updatedAt"] = datetime.today().strftime("%Y-%m-%d")
        self._save()

        print("\nTask status updated successfully!\n")


def handler_command(tasks, command):
    parts = command.split()

    if not parts:
        return

    command = parts[0]
    args = parts[1:]

    if command == "list":
        status = args[0] if args else None
        tasks.list_tasks(status)

    elif command == "add":
        if not args:
            print("Usage: python tasks.py add <task_description>\n")
            return

        task_description = " ".join(args)
        tasks.add_task(task_description)

    elif command == "update":
        if len(args) < 2:
            print("Usage: python tasks.py update <task_id> <new_description>\n")
            return

        task_id = int(args[0])
        task_description = " ".join(args[1:])
        tasks.update_task(task_id, task_description)

    elif command == "delete":
        if not args:
            print("Usage: python tasks.py delete <task_id>\n")
            return

        task_id = int(args[0])
        tasks.delete_task(task_id)

    elif command == "change_status":
        if len(args) < 2:
            print("Usage: python tasks.py change_status <task_id> <new_status>\n")
            return

        task_id = int(args[0])
        task_status = args[1]
        tasks.change_task_status(task_id, task_status)

    elif command == "help":
        print("""
Avalible commands:
    list [status]
    add <description>
    update <task_id> <description>
    change_status <task_id> <status>
    delete <task_id>
    help
    exit
""")

    elif command == "exit":
        print("Exiting the program.")
        return  False

    else:
        print("Invalid command. Type 'help' for a list of available commands.\n")

    return True


def main():
    tasks = Tasks()

    # CLI direta
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        handler_command(tasks, command)
        return

    # CLI interativa
    print("\n" + "*" * 20)
    print("*** Task Tracker ***")
    print("*" * 20 + "\n")
    print("Type 'help' for available commands.\n")

    while True:
        command = input("> ")

        if handler_command(tasks, command) is False:
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    main()
