initial_string = input()


def take_odd(string):
    return "".join([string[x] for x in range(len(string)) if x % 2 == 1])


def cut(string, index, length):
    return string[:index] + string[index + length:]


command = input()
while command != "Done":
    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        initial_string = take_odd(initial_string)
        print(initial_string)
    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        initial_string = cut(initial_string, index, length)
        print(initial_string)
    elif action == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, substitute)
            print(initial_string)
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {initial_string}")
