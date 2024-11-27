import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List CLI")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            todo.list_tasks()
        elif choice == '2':
            task = input("Enter a new task: ")
            todo.add_task(task)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
