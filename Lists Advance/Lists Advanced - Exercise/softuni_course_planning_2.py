lessons = input().split(", ")

while True:
    command = input().split(":")
    action = command[0]

    if action == "course start":
        break

    lesson_title = command[1]

    if action == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)

    elif action == "Swap":
        lesson_title_2 = command[2]

        if lesson_title in lessons and lesson_title_2 in lessons:
            index_one = lessons.index(lesson_title)
            index_two = lessons.index(lesson_title_2)
            lessons[index_one], lessons[index_two] = lessons[index_two], lessons[index_one]

    elif action == "Exercise":
        if lesson_title in lessons:
            index = lessons.index(lesson_title)
            if index + 1 < len(lessons) and not lessons[index + 1].endswith('-Exercise'):
                lessons.insert(index + 1, f"{lesson_title}-Exercise")
            elif index + 1 == len(lessons):
                lessons.append(f"{lesson_title}-Exercise")
        else:
            lessons.append(lesson_title)
            lessons.append(f"{lesson_title}-Exercise")

for i, lesson in enumerate(lessons, start=1):
    print(f"{i}.{lesson}")


