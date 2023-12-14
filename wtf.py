class Task:
    def init(self, name, priority=0):
        self.name = name
        self.priority = priority

    def str(self):
        return f"{self.name} - Priority: {self.priority}"

class PriorityDecorator:
    def init(self, default_priority=0):
        self.default_priority = default_priority

    def call(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if func.name == "add_task":
                priority = kwargs.get('priority', self.default_priority)
                args[0][-1].priority = priority

            return result
        return wrapper

@PriorityDecorator(default_priority=1)
def add_task(tasks, task):
    tasks.append(task)

def display_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x.priority)
    for task in sorted_tasks:
        print(task)

def execute_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x.priority)
    for task in sorted_tasks:
        print(f"Executing task: {task.name}")
    tasks.clear()


def change_task_priority(tasks, task_name, new_priority):
    task_found = False
    for task in tasks:
        if task.name == task_name:
            task.priority = new_priority
            task_found = True
            break

    if not task_found:
        print(f"Error: Task with name '{task_name}' not found.")

if name == "main":
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Change Task Priority")
        print("3. Display Tasks")
        print("4. Execute Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter task priority: ")
            try:
                priority = int(priority)
            except ValueError:
                print("Error: Priority must be an integer.")
                continue

            task = Task(name, priority)
            add_task(tasks, task=Task(name, priority=priority))
            print("Task added successfully!")

        elif choice == "2":
            task_name = input("Enter task name to change priority: ")
            new_priority = input("Enter new priority: ")
            try:
                new_priority = int(new_priority)
            except ValueError:
                print("Error: New priority must be an integer.")
                continue

            change_task_priority(tasks, task_name, new_priority)

        elif choice == "3":
            print("\nTasks:")
            display_tasks(tasks)

        elif choice == "4":
            print("\nExecuting Tasks:")
            execute_tasks(tasks)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")