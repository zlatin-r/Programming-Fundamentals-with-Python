raw_key = input()


def contains(key, string):
    if string in key:
        return f"{key} contains {string}"
    else:
        return "Substring not found!"


def flip(key, up_low, start, end):
    if up_low == "Upper":
        result = key[:start] + key[start:end].upper() + key[end:]
    elif up_low == "Lower":
        result = key[:start] + key[start:end].lower() + key[end:]
    return result


def slice(key, start, end):
    key = key[:start] + key[end:]
    return key


command = input()
while command != "Generate":
    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        print(contains(raw_key, substring))

    elif action == "Flip":
        upper_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        raw_key = flip(raw_key, upper_lower, start_index, end_index)
        print(raw_key)

    elif action == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        raw_key = slice(raw_key, start_index, end_index)
        print(raw_key)

    command = input()
print(f"Your activation key is: {raw_key}")
