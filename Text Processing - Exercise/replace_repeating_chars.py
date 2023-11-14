text = input()
filtered_text = ""
last_added = ""

for char in text:
    if char != last_added:
        filtered_text += char
        last_added = char

print(filtered_text)
