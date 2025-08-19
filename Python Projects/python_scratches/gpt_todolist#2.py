# your tasks
todolist = ["Python proj (gui)", "Workout", "Bible", "Don't do it"]

# simulate completed task index (for example: task 1 and 2 are done)
completed_tasks = [0, 2]  # indices of completed tasks

# function to apply strikethrough
def strikethrough(text):
    return ''.join(char + '\u0336' for char in text)

# print the todo list
for index, task in enumerate(todolist):
    if index in completed_tasks:
        print("-", strikethrough(task))
    else:
        print("-", task)
