pool = {}

command = input()
while command != 'Season end':
    if "->" in command:
        name, skill, points = [int(i) if i.isdigit() else i for i in command.split(" -> ")]
        if name not in pool:
            pool[name] = {skill: points}
        elif name in pool and skill not in pool[name]:
            pool[name][skill] = points
        elif name in pool and skill in pool[name]:
            if pool[name][skill] < points:
                pool[name][skill] = points

    else:
        player1, player2 = command.split(" vs ")
        if player1 in pool and player2 in pool:
            for position, points in pool[player1].items():
                if position in pool[player2].keys():
                    if points < pool[player2][position]:
                        del pool[player1]
                    elif pool[player2][position] < pool[player1][position]:
                        del pool[player2]
                    break

    command = input()

# total points generating and sorting
total_points = {}
for name in pool.keys():
    for v in pool[name].values():
        if name not in total_points:
            total_points[name] = 0
        total_points[name] += v
total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))

# inside points sorting
for name in pool.keys():
    for k, v in pool[name].items():
        pool[name] = dict(sorted(pool[name].items(), key=lambda x: (-x[1], x[0])))

for name, totalpoints in total_points.items():
    print(f"{name}: {totalpoints} skill")
    for k, v in pool[name].items():
        print(f"- {k} <::> {v}")
