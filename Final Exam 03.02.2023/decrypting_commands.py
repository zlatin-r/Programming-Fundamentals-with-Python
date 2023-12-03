initial_string = input()

command = input()
while command != "Finish":
    command = command.split()
    action = command[0]

    if action == "Replace":
        current_char, new_char = command[1], command[2]
        initial_string = initial_string.replace(current_char, new_char)
        print(initial_string)

    elif action == "Cut":
        start, end = int(command[1]), int(command[2])
        if 0 <= start < len(initial_string) and 0 <= end < len(initial_string):
            initial_string = initial_string[:start] + initial_string[end+1:]
            print(initial_string)
        else:
            print("Invalid indices!")

    elif action == "Make":
        option = command[1]
        if option == "Upper":
            initial_string = initial_string.upper()
            print(initial_string)
        elif option == "Lower":
            initial_string = initial_string.lower()
            print(initial_string)

    elif action == "Check":
        string = command[1]
        if string in initial_string:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif action == "Sum":
        start, end = int(command[1]), int(command[2])
        if 0 <= start < len(initial_string) and 0 <= end < len(initial_string):
            substring = initial_string[start:end+1]
            ascii_sum = sum(ord(c) for c in substring)
            print(ascii_sum)
        else:
            print("Invalid indices!")

    command = input()
