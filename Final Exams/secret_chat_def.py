message = input()


def insert_space(text, index):
    text = text[:index] + " " + text[index:]
    print(text)
    return text


def reverse_string(text, string):
    if string in text:
        text = text.replace(string, "", 1) + string[::-1]
        print(text)
        return text
    else:
        print("error")
        return text


def change_all(text, old_string, new_string):
    text = text.replace(old_string, new_string)
    print(text)
    return text


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

    command = input()
print(f"You have a new text message: {message}")
