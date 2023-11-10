text = input().split()
repeated_text = ""

for word in text:
    repeated_text += word * len(word)

print(repeated_text)
