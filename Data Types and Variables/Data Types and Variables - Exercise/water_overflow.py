n = int(input())
amount_water = 0
capacity_water = 255

for i in range(n):
    poured_water = int(input())
    if amount_water + poured_water > capacity_water:
        print("Insufficient capacity!")
        continue
    amount_water += poured_water

print(amount_water)
