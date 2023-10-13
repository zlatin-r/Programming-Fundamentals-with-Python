tasks = []

while True:
    task = input()

    sorted_tasks = sorted(tasks, key=lambda x: int(x.split("-")[0]))

    if task == "End":
        sorted_tasks = [x.split("-")[1] for x in sorted_tasks]
        print(sorted_tasks)
        break
    tasks.append(task)
