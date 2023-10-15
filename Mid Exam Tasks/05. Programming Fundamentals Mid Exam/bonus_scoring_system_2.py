from math import ceil

students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
lectures = 0

for student in range(1, students + 1):
    attendance = int(input())
    total_bonus = (attendance / total_lectures) * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lectures} lectures.")
