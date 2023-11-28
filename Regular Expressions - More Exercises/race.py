import re

names = input().split(", ")
data = input()
results = {}

while data != "end of race":
    match_name = re.findall(r"[A-Za-z]", data)
    match_time = re.findall(r"\d", data)
    name = "".join(match_name)
    time = sum([int(x) for x in match_time])

    if name in names:
        if name not in results:
            results[name] = 0
        results[name] += time
    data = input()

sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)

print(f"1st place: {sorted_results[0][0]}")
print(f"2nd place: {sorted_results[1][0]}")
print(f"3rd place: {sorted_results[2][0]}")
