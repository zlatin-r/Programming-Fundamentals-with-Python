encrypted_message = input()

instructions = input()

while instructions != "Decode":
    instructions = instructions.split("|")
    action = instructions[0]

    if action == "Move":
        number_of_letters = int(instructions[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif action == "Insert":
        index, value = int(instructions[1]), instructions[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
