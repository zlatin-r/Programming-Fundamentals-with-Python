message = input()
final_message, symbols, number = "", "", ""

for index in range(len(message)):
    if not message[index].isdigit():
        symbols += message[index].upper()
    else:
        number += message[index]
        if index + 1 < len(message):
            if message[index + 1].isdigit():
                continue
        final_message += symbols.upper() * int(number)
        symbols, number = "", ""

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)
