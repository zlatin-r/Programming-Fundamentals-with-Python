passwords = {}
rankings = {}

contest = input()

while contest != 'end of contests':
    name, password = contest.split(':')
    passwords[name] = password
    contest = input()

users_input = input()

while users_input != 'end of submissions':
    contest_name, password, user_name, score = users_input.split('=>')

    if contest_name not in passwords or password != passwords[contest_name]:
        users_input = input()
        continue

    rankings[user_name] = rankings.get(user_name, {})
    rankings[user_name][contest_name] = rankings[user_name].get(contest_name, 0)
    rankings[user_name][contest_name] = max(int(score), rankings[user_name][contest_name])

    users_input = input()

max_user, max_total_score = max(rankings.items(), key=lambda user_scores: sum(user_scores[1].values()))

print(f'Best candidate is {max_user} with total {sum(max_total_score.values())} points.\nRanking:')
for name in sorted(rankings):
    print(name)
    for contest, points in sorted(rankings[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")
