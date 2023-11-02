commands = input()
data = {}

while True:

    if "|" in commands:
        force, user = commands.split(" | ")
    elif " -> " in commands:
        user, force = commands.split(" -> ")
    else:
        break

print(data)


