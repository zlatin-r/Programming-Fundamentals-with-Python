contests = {}
users = {}

command = input()
while command != "end of contests":
    contest, password = command.split(":")
    contests[contest] = password
    command = input()

data = input()
while data != "end of submissions":
    contest, password, user_name, points = data.split("=>")

    if contest in contests and password in contests.values():
        if user_name not in users.keys():
            users[user_name] = {}
            users[user_name][contest] = int(points)
        else:
            if contest not in users[user_name].keys():
                users[user_name][contest] = int(points)
            else:
                users[user_name][contest] = max(int(points), users[user_name][contest])

    data = input()

best_user, max_score = max(users.items(), key=lambda user_scores: sum(user_scores[1].values()))

print(f"Best candidate is {best_user} with total {sum(max_score.values())} points.\nRanking:")
for user, info in sorted(users.items()):
    print(user)
    sorted_info = sorted(info.items(), key=lambda item: item[1], reverse=True)
    for contest, points in sorted_info:
        print(f"#  {contest} -> {points}")
