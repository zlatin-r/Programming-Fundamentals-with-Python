string = input()
result = ""

command = input()
while command != "Done":
    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        string = "".join([string[x] for x in range(len(string)) if x % 2 == 1])
        print(string)
    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        string = string[:index] + string[index + length:]
        print(string)
    elif action == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {string}")
