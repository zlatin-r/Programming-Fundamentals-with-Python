students = []

while True:
    info = input()

    if ":" not in info:
        course_to_search = info
        break

    name, ID, course = info.split(":")
    students.append({"name": name, "ID": ID, "course": course})

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
