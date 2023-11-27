destinations = input()


def valid(index):
    if 0 <= index < len(destinations):
        return True


command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index, stop = int(command[1]), command[2]
        if valid(index):
            destinations = destinations[:index] + stop + destinations[index:]

    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if valid(start_index) and valid(end_index):
            destinations = destinations[:start_index] + destinations[end_index + 1:]

    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)

    print(destinations)
    command = input()

print(f"Ready for world tour! Planned stops: {destinations}")
