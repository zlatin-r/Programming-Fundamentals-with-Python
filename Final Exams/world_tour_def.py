def validation(string, index):
    if 0 <= index < len(string):
        return True
    return False


def add_stop(string, index, substring):
    string = string[:index] + substring + string[index:]
    return string


def remove_stop(string, start, end):
    string = string[:start] + string[end + 1:]
    return string


def switch(string, old_string, new_string):
    string = string.replace(old_string, new_string)
    return string


initial_sting = input()

command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        if validation(initial_sting, int(command[1])):
            initial_sting = add_stop(initial_sting, int(command[1]), command[2])

    elif action == "Remove Stop":
        if validation(initial_sting, int(command[1])) and validation(initial_sting, int(command[2])):
            initial_sting = remove_stop(initial_sting, int(command[1]), int(command[2]))

    elif action == "Switch":
        if command[1] in initial_sting:
            initial_sting = switch(initial_sting, command[1], command[2])

    print(initial_sting)
    command = input()

print(f"Ready for world tour! Planned stops: {initial_sting}")
