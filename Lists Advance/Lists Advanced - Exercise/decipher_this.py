text = input().split(" ")

decoded_message = ""

for word in text:
    decipher = []
    symbols = [x for x in word]
    first_letter = [x for x in symbols if x.isdigit()]
    first_letter = chr(int("".join(first_letter)))
    letters = [x for x in symbols if not x.isdigit()]

    decipher.append(first_letter)
    decipher.append(letters[-1])
    if len(letters) > 1:
        letters.pop(-1)
        decipher.extend(letters[1:])
        decipher.append(letters[0])
    decoded_message += "".join(decipher)
    decoded_message += " "

print(decoded_message.strip(" "))
