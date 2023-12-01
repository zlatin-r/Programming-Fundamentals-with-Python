data, total_points = {}, {}
data_input = input()
count = 1

while data_input != "no more time":
    user_name, contest, points = data_input.split(" -> ")

    data[contest] = data.get(contest, {})
    data[contest][user_name] = data[contest].get(user_name, int(points))
    data[contest][user_name] = max(int(points), data[contest][user_name])

    data_input = input()

for contest, user_name in data.items():
    print(f"{contest}: {len(user_name)} participants")
    for pos, (name, points) in enumerate(sorted(user_name.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {name} <::> {points}")
        total_points[name] = total_points.get(name, 0) + points

print("Individual standings:")
for pos, (name, points) in enumerate(sorted(total_points.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {name} -> {points}")
