to_do_list = []

# Tasks
to_do_list.append("Workout")
to_do_list.append("Python proj")
to_do_list.append("Bible")
to_do_list.append("Don't do it")

# What shows on screen 
print("My Productive To-do list for exp points in life (Religious and Productive Route):")	
for _ in to_do_list:
    print("- "+ _)

#Completed tasks here
to_do_list.remove("Don't do it")

print("\nUnfinished tasks:")
for _ in to_do_list:
   print("- "+ _)
