pool = {}
data_input = input()

while data_input != "Season end":
    if "->" in data_input:
        player, position, skill = data_input.split(" -> ")

        pool[player] = pool.get(player, {})
        pool[player][position] = pool[player].get(position, int(skill))
        pool[player][position] = max(int(skill), pool[player][position])

    elif "vs" in data_input:
        player1, player2 = data_input.split(" vs ")

        if player1 in pool and player2 in pool:
            for position, points in pool[player1].items():
                if position in pool[player2].keys():
                    if points < pool[player2][position]:
                        del pool[player1]
                    elif pool[player2][position] < pool[player1][position]:
                        del pool[player2]
                    break

    data_input = input()

total_points = {}
for player in pool.keys():
    for v in pool[player].values():
        if player not in total_points:
            total_points[player] = 0
        total_points[player] += v
total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))

for player in pool.keys():
    for k, v in pool[player].items():
        pool[player] = dict(sorted(pool[player].items(), key=lambda x: (-x[1], x[0])))

for player, total_points in total_points.items():
    print(f"{player}: {total_points} skill")
    for k, v in pool[player].items():
        print(f"- {k} <::> {v}")
