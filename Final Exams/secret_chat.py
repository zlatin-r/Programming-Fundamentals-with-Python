text = input()

command = input()
while command != "Reveal":
    data = command.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        index = int(data[1])
        text = text[:index] + " " + text[index:]
        print(text)

    elif action == "Reverse":
        substring = data[1]
        if substring in text:
            reversed_string = substring[::-1]
            text = text.replace(substring, "", 1)
            text += reversed_string
            print(text)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        text = text.replace(substring, replacement)
        print(text)

    command = input()
print(f"You have a new text message: {text}")
