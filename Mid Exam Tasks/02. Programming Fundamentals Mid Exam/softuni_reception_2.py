first_employee, second_employee, third_employee = int(input()), int(input()), int(input())
students_count = int(input())
total_students_per_hour = first_employee + second_employee + third_employee
hour_count = 0

while students_count > 0:

    if hour_count == 3:
        continue
    else:
        students_count -= total_students_per_hour
