import re

data = {}
participants = input().split(", ")
info = input()

while info != "end of race":
    name = "".join(re.findall(r"[A-Za-z]", info))
    distance = sum(int(x) for x in (re.findall(r"\d", info)))

    if name in participants:
        if name not in data:
            data[name] = 0
        data[name] += distance

    info = input()

sorted_dict = sorted(data.items(), key=lambda item: -item[1])

print(f"1st place: {sorted_dict[0][0]}")
print(f"2nd place: {sorted_dict[1][0]}")
print(f"3rd place: {sorted_dict[2][0]}")
