data = {}
command = input()
user_points = 0

while command != "exam finished":
    command = command.split("-")

    if "banned" in command:
        user_name, banned = command
        for dicts in data.values():
            for value in dicts.keys():
                if value == user_name:
                    value = "banned"
    else:
        user_name, language, points = command
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
