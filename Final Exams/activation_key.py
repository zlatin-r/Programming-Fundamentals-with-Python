activation_key = input()

commands = input()
while commands != "Generate":
    commands = commands.split(">>>")
    action = commands[0]

    if action == "Contains":
        substring = commands[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == "Flip":
        change, start, end = commands[1], int(commands[2]), int(commands[3])
        if change == "Lower":
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
        elif change == "Upper":
            activation_key = activation_key[:start] + activation_key[start:end].upper() + activation_key[end:]
        print(activation_key)
    elif action == "Slice":
        start, end = int(commands[1]), int(commands[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)

    commands = input()
print(f"Your activation key is: {activation_key}")
