text = input()
final_text = ""
strength = 0

for i in range(len(text)):
    if strength > 0 and text[i] != ">":
        strength -= 1
    elif text[i] == ">":
        final_text += ">"
        strength += int(text[i + 1])
    else:
        final_text += text[i]

print(final_text)
