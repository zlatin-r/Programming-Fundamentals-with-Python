letters = input()
text = input()

while letters in text:
    text = text.replace(letters, "")

print(text)
