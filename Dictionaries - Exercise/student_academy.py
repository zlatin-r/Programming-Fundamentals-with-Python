rows = int(input())
data = {}
counter = 1

for student in range(rows):
    student_name = input()
    grade = float(input())

    if student_name not in data:
        data[student_name] = [grade, counter]
    else:
        data[student_name][0] += grade
        data[student_name][1] += 1

for s, g, in data.items():
    average_grade = g[0] / g[1]
    if average_grade >= 4.50:
        print(f"{s} -> {average_grade:.2f}")
