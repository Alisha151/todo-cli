import sys

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")

    def list(self):
        if not self.tasks:
            print("No tasks yet!")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            print(f"Removed: {removed}")
        except IndexError:
            print("Invalid task number.")

def main():
    todo = TodoList()
    while True:
        command = input("\nEnter command (add/list/remove/quit): ").strip().lower()
        if command == "add":
            task = input("Task: ")
            todo.add(task)
        elif command == "list":
            todo.list()
        elif command == "remove":
            try:
                index = int(input("Task number to remove: "))
                todo.remove(index)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "quit":
            print("Goodbye!")
            sys.exit()
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

