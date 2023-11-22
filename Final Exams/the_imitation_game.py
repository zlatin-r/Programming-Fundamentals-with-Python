message = input()

instructions = input()

while instructions != "Decode":
    instructions = instructions.split("|")
    action = instructions[0]

    if action == "Move":
        index = int(instructions[1])
        message = message[index:] + message[:index]

    elif action == "Insert":
        index, value = int(instructions[1]), instructions[2]
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        message = message.replace(substring, replacement)

    instructions = input()

print(f"The decrypted message is: {message}")
