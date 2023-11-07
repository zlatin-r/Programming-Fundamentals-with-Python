part_one_interviews = {}
part_two_submissions = {}
command = input()

while command != "end of contests":
    contest, password = command.split(":")
    if contest not in part_one_interviews.keys():
        part_one_interviews[contest] = ""
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
                if part_two_submissions[user_name][contest] < int(points):
                    part_two_submissions[user_name][contest] = int(points)
            else:
                part_two_submissions[user_name][contest] = int(points)

    command = input()

best_candidate = max(part_two_submissions.keys())
max_points = sum(part_two_submissions[best_candidate].values())

print(f"Best candidate is {best_candidate} with total {max_points}")
print("Ranking:")

for candidate, submissions in sorted(part_two_submissions.items()):
    print(candidate)
    for contest, points in submissions.items():
        print(f"{contest} -> {points}")
