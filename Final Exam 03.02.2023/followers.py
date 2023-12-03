followers_data = {}

command = input()
while command != "Log out":
    command = command.split(":")
    action, username = command[0], command[1].strip()

    if action == "New follower":
        if username not in followers_data:
            followers_data[username] = [0, 0]

    elif action == "Like":
        likes = int(command[2])
        if username in followers_data:
            followers_data[username][0] += likes
        else:
            followers_data[username] = [likes, 0]

    elif action == "Comment":
        if username not in followers_data:
            followers_data[username] = [0, 1]
        else:
            followers_data[username][1] += 1

    elif action == "Blocked":
        if username in followers_data:
            followers_data.pop(username)
        else:
            print(f"{username} doesn't exist.")

    command = input()

print(f"{len(followers_data)} followers")
for user, info in followers_data.items():
    print(f"{user}: {info[0] + info[1]}")
