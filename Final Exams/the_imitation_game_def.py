def move(message, num_letters):
    output = message[num_letters:] + message[:num_letters]
    return output


def insert(message, index, value):
    first_part = message[:index]
    second_part = message[index:]
    output = first_part + value + second_part
    return output


def change_all(message, sub_string, replacement):
    output = message.replace(sub_string, replacement)
    return output


encrypted_message = input()

instructions = input()
while instructions != "Decode":
    data = instructions.split("|")

    if "Move" in data:
        encrypted_message = move(encrypted_message, int(data[1]))
    elif "Insert" in data:
        encrypted_message = insert(encrypted_message, int(data[1]), data[2])
    elif "ChangeAll" in data:
        encrypted_message = change_all(encrypted_message, data[1], data[2])

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
