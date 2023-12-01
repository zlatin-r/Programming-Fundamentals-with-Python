message = input()


def insert_space(text, index):
    return text[:index] + " " + text[index:]


def reverse_string(text, string):
    if string in text:
        text = text.replace(string, "", 1) + string[::-1]
        return text
    else:
        print("error")


def change_all(text, old_string, new_string):
    return text.replace(old_string, new_string)


command = input()
while command != "Reveal":
    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        message = insert_space(message, int(command[1]))

    elif action == "Reverse":
        message = reverse_string(message, command[1])

    elif action == "ChangeAll":
        message = change_all(message, command[1], command[2])

    print(message)
    command = input()
print(f"You have a new text message: {message}")
