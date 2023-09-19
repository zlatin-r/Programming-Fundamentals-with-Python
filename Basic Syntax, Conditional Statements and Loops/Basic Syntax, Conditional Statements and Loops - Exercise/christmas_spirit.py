quantity = int(input())
days = int(input())

spirit = 0
total_cost = 0

for i in range(1, days + 1):

    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += 2 * quantity
        spirit += 5
    if i % 3 == 0:
        total_cost += (5 + 3) * quantity
        spirit += 3 + 10
    if i % 5 == 0:
        total_cost += 15 * quantity
        spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        spirit += 30
    if i % 10 == 0:
        spirit -= 20
        total_cost += 5 + 3 + 15

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
