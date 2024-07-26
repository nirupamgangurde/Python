class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: {task}')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task deleted: {removed_task}')
        else:
            print("Invalid task number.")

todo_list = TodoList()
todo_list.add_task("Finish Python project")
todo_list.add_task("Read a book")
todo_list.view_tasks()
todo_list.delete_task(1)
todo_list.view_tasks()
