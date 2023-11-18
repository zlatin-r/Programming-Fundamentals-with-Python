import re

line = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"    # or: pattern = fr"(?i)\b{searched_word}\b"

matches = re.findall(pattern, line, re.IGNORECASE)

print(len(matches))
