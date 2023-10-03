from math import ceil

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())

total_students = int(input())

total_employees_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

total_time_needed = ceil(total_students / total_employees_efficiency)

if total_time_needed >= 3:
    extra_time = total_time_needed // 3
    total_time_needed += extra_time

print(f"Time needed: {total_time_needed}h.")
