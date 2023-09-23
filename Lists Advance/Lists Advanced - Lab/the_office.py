employees_happiness = [int(x) for x in input().split(" ")]
improvement_factor = int(input())

multiplied_happiness = list(map(lambda x: x * improvement_factor, employees_happiness))
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employees = [x for x in multiplied_happiness if x >= average_happiness]

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
