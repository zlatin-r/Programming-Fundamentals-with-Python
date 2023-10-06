<<<<<<< HEAD
from math import ceil

number_of_students = int(input())
total_count_of_lectures = int(input())
additional_bonuses = int(input())

lectures = 0
max_points = 0

for student in range(number_of_students):
    attendance = int(input())

    total_bonus = (attendance / total_count_of_lectures) * (5 + additional_bonuses)

    if total_bonus >= max_points:
        max_points = total_bonus
        lectures = attendance

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {ceil(lectures)} lectures.")
=======
from math import ceil

number_of_students = int(input())
total_count_of_lectures = int(input())
additional_bonuses = int(input())

lectures = 0
max_points = 0

for student in range(number_of_students):
    attendance = int(input())

    total_bonus = (attendance / total_count_of_lectures) * (5 + additional_bonuses)

    if total_bonus >= max_points:
        max_points = total_bonus
        lectures = attendance

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {ceil(lectures)} lectures.")
>>>>>>> origin/main
