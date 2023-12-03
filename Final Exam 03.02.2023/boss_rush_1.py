import re

n = int(input())
pattern = r"([|])([A-Z]{4,})\1:([#])([A-Za-z]+\s[A-Za-z]+)\3"

for _ in range(n):
    data = input()
    matches = re.findall(pattern, data)

    if matches:
        name = matches[0][1]
        title = matches[0][3]

        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
