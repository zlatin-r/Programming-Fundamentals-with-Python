encrypted_message = input()

instructions = input()

while instructions != "Decode":
    instructions = instructions.split("|")
    action = instructions[0]

    if action == "Move":
        index = int(instructions[1])
        encrypted_message = encrypted_message[index:] + encrypted_message[:index]

    elif action == "Insert":
        index, value = int(instructions[1]), instructions[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    instructions = input()

print(f"The decrypted message is: {encrypted_message}")
