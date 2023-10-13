employees = input().split()
improvement_factor = int(input())

improved_happiness = [int(x) * improvement_factor for x in employees]
average_happiness = sum(improved_happiness) / len(employees)
happy_employees = len([x for x in improved_happiness if x >= average_happiness])

if happy_employees >= len(employees) // 2:
    print(f"Score: {happy_employees}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees)}. Employees are not happy!")
