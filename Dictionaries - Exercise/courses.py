data = {}
info = input()

while info != "end":
    course_name, student_name = info.split(":")

    if course_name not in data:
        data[course_name] = []
    data[course_name].append(student_name)

    info = input()

for course in data:
    print(f"{course.strip()}: {len(data[course])}")
    for student in data[course]:
        print(f"-- {student.strip()}")