import re

n = int(input())
pattern = r"([|])([A-Z]{4,})\1:([#])([A-Za-z\s]+)\3"

for _ in range(n):
    data = input()
    match = re.findall(pattern, data)

    if match and match[0][3].count(" ") == 1:
        name = match[0][1]
        title = match[0][3]

        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
