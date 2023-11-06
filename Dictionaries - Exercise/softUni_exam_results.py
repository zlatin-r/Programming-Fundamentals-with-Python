data = {}
submissions = {}
command = input()
user_points = 0
ban = ""

while command != "exam finished":
    command = command.split("-")

    if "banned" in command:
        user_name, banned = command
        ban = user_name
    else:
        user_name, language, points = command

        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

        if language not in data.keys():
            data[language] = {}
            data[language][user_name] = int(points)

        else:
            if user_name in data[language]:
                user_points = data[language][user_name]
                if int(points) > user_points:
                    user_points = int(points)
            else:
                data[language][user_name] = int(points)

    command = input()

print("Results:")
for k, v in data.items():
    for user, points in v.items():
        if user != ban:
            print(f"{user} | {points}")

print("Submissions:")
for k, v in submissions.items():
    print(f"{k} - {v}")
