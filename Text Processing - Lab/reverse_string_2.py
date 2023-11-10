text = input()

while text != "end":
    reversed_text = ""

    for char in reversed(text):
        reversed_text += char
    print(f"{text} = {reversed_text}")

    text = input()