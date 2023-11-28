import re

demons = input().split(",")
demons = [demon.strip() for demon in demons]

for demon in sorted(demons):
    health = sum(ord(char) for char in re.findall(r"[^\d\+\-\*\/\.]", demon))
    damage = sum(float(number[0]) for number in re.findall(r"([-+]?\d+(\.\d+)?)", demon))

    for symbol in demon:
        if symbol == "*":
            damage *= 2
        elif symbol == "/":
            damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")
