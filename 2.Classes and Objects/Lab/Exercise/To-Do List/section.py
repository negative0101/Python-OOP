from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {Task.details(new_task)} is added to the section'

    def complete_task(self, task_name):
        task_complete = [i for i in self.tasks if i.name == task_name]
        if task_complete:
            check = task_complete[0]
            check.complete = True
            return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        trued = [tru for tru in self.tasks if tru.completed]
        cleared = len(trued)
        for el in trued:
            self.tasks.remove(el)
            return f"Cleared {cleared} tasks."
        return f"Cleared 0 tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for tsk in self.tasks:
            result += f"{tsk.details()}\n"
        return result

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())