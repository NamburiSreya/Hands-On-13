class Task:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

def sort_by_finish_time(taskA, taskB):
    # Sort tasks by their finish time in descending order
    return taskB.finish - taskA.finish

# List of tasks with their start and finish times
tasks = [
    Task("watch", 9, 10),
    Task("shirt", 1, 8),
    Task("tie", 2, 5),
    Task("jacket", 3, 4),
    Task("belt", 6, 7),
    Task("pants", 12, 15),
    Task("undershorts", 11, 16),
    Task("socks", 17, 18),
    Task("shoes", 13, 14)
]

# Sort tasks by finish time in descending order
tasks.sort(key=lambda x: x.finish, reverse=True)

# Print the sorted tasks
print("Sorted tasks by finish time:")
for task in tasks:
    print(task.name)



# output Sorted tasks by finish time:
#socks
#undershorts
#pants
#shoes
#watch
#shirt
#tie
#jacket
