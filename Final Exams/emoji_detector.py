import re

emoji_pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
digits_pattern = r"\d"

text = input()
cool_threshold = 1
cool_emojis = []

emojis = re.findall(emoji_pattern, text)
digits = re.findall(digits_pattern, text)

for x in digits:
    cool_threshold *= int(x)
print(f"Cool threshold: {cool_threshold}")

for emoji in emojis:
    filtered = re.findall(r"[A-Za-z]+", emoji)
    ascii_sum = sum(ord(char) for char in filtered[0])
    if ascii_sum > cool_threshold:
        cool_emojis.append(emoji)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))
