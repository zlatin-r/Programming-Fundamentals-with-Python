schedule = input().split(", ")

while True:
    command = input().split(":")

    if command[0] == "course start":
        break

    action = command[0]
    lesson_title = command[1]

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
        lesson_title2 = command[2]
        if lesson_title in schedule and lesson_title2 in schedule:
            index1 = schedule.index(lesson_title)
            index2 = schedule.index(lesson_title2)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
            if f"{lesson_title}-Exercise" in schedule and f"{lesson_title2}-Exercise" in schedule:
                index1_exercise = schedule.index(f"{lesson_title}-Exercise")
                index2_exercise = schedule.index(f"{lesson_title2}-Exercise")
                schedule[index1_exercise], schedule[index2_exercise] = schedule[index2_exercise], schedule[
                    index1_exercise]
            elif f"{lesson_title}-Exercise" in schedule:
                index1_exercise = schedule.index(f"{lesson_title}-Exercise")
                schedule.remove(f"{lesson_title}-Exercise")
                schedule.insert(index2 + 1, f"{lesson_title}-Exercise")
            elif f"{lesson_title2}-Exercise" in schedule:
                index2_exercise = schedule.index(f"{lesson_title2}-Exercise")
                schedule.remove(f"{lesson_title2}-Exercise")
                schedule.insert(index1 + 1, f"{lesson_title2}-Exercise")
    elif action == "Exercise":
        if lesson_title in schedule:
            index = schedule.index(lesson_title)
            if index + 1 < len(schedule) and not schedule[index + 1].endswith('-Exercise'):
                schedule.insert(index + 1, f"{lesson_title}-Exercise")
            elif index + 1 == len(schedule):
                schedule.append(f"{lesson_title}-Exercise")
        else:
            schedule.append(lesson_title)
            schedule.append(f"{lesson_title}-Exercise")

for i, lesson in enumerate(schedule, start=1):
    print(f"{i}.{lesson}")
