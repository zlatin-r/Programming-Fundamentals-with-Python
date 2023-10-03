first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
total_students = int(input())
total_time_needed = 0

total_employees_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while total_students > 0:
    total_time_needed += 1
    if total_time_needed % 4 != 0:
        total_students -= total_employees_efficiency

print(f"Time needed: {total_time_needed}h.")
