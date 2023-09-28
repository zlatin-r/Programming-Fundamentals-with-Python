schedule = input().split(", ")

while True:
    command = input().split(":")
    action = command[0]
    lesson_title = command[1]
    result = []

    if action == "Add" and lesson_title not in schedule:
        schedule.append(lesson_title)
    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in schedule:
            schedule.insert(index, lesson_title)
    elif action == "Remove":
        if lesson_title in schedule:
            schedule.remove(lesson_title)

    elif action == "Swap":
        lesson_title_2 = command[2]
        if lesson_title in schedule and lesson_title_2 in schedule:
            index_1 = schedule.index(lesson_title)
            index_2 = schedule.index(lesson_title_2)
            schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

    elif action == "Exercise":
        if lesson_title not in schedule:
            schedule.append(lesson_title)
            schedule.append(lesson_title + "-Exercise")
        else:
            index = schedule.index(lesson_title)
            schedule[index] = lesson_title + "-Exercise"
    print(schedule)
