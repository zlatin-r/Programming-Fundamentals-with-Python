data = {}
total_points = {}
data_input = input()


while data_input != "no more time":
    user_name, contest, points = data_input.split(" -> ")

    if contest not in data:
        data[contest] = data.get(contest, {})
    data[contest][user_name] = data[contest].get(user_name, int(points))
    data[contest][user_name] = max(int(points), data[contest][user_name])

    data_input = input()

for contest, user_name in data.items():
    count = 1
    print(f"{contest}: {len(user_name)} participants")
    for name, points in sorted(user_name.items(), key=lambda item: -item[1]):
        if name not in total_points:
            total_points[name] = 0
        total_points[name] += int(points)
        print(f"{count}. {name} <::> {points}")
        count += 1

print("Individual standings:")
for name, points in sorted(total_points.items(), key=lambda item: -item[1]):
    print(f"{name} -> {points}")
