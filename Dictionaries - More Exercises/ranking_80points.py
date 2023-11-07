part_one_interviews = {}
part_two_submissions = {}
command = input()

while command != "end of contests":
    contest, password = command.split(":")
    part_one_interviews[contest] = password
    command = input()

command = input()

while command != "end of submissions":
    contest, password, user_name, points = command.split("=>")

    if contest in part_one_interviews and password in part_one_interviews.values():
        if user_name not in part_two_submissions.keys():
            part_two_submissions[user_name] = {}
            part_two_submissions[user_name][contest] = int(points)
        else:
            if contest in part_two_submissions[user_name].keys():
                part_two_submissions[user_name][contest] = max(int(points), part_two_submissions[user_name][contest])
            else:
                part_two_submissions[user_name][contest] = int(points)

    command = input()

best_candidate = max(part_two_submissions.keys())
max_points = sum(part_two_submissions[best_candidate].values())

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

for candidate, submissions in sorted(part_two_submissions.items()):
    print(candidate)
    sorted_dict = sorted(submissions.items(), key=lambda item: item[1], reverse=True)

    for contest, points in sorted_dict:
        print(f"#  {contest} -> {points}")
