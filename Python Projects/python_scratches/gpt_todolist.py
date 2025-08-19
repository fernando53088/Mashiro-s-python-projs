# Start with an empty to-do list
todo_list = []

# Add some tasks
todo_list.append("Finish homework")
todo_list.append("Practice Python")
todo_list.append("Clean room")

# Print all tasks
print("My To-Do List:")
for task in todo_list:
    print("- " + task)

# Remove a task (e.g., "Clean room" done)
todo_list.remove("Clean room")

print("\nUpdated To-Do List:")
for task in todo_list:
    print("- " + task)
