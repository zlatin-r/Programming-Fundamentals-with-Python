import re

raw_string = input()

pattern_emojis = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"


def valid_emojis(pattern, string):
    matches = re.findall(pattern, string)
    return len(matches)


def emojis(pattern, string):
    matches = re.findall(pattern, string)
    return matches


def cool_threshold(pattern, string):
    digits = re.findall(pattern, string)
    result = 1
    for x in digits:
        result *= int(x)
    return result


def coolness(match):
    filtered = re.findall(r"[A-Za-z]", match)
    result = sum(ord(char) for char in filtered)
    return result


threshold = cool_threshold(r"\d", raw_string)

print(f"Cool threshold: {threshold}")
print(f"{valid_emojis(pattern_emojis, raw_string)} emojis found in the text. The cool ones are:")

for emoji in emojis(pattern_emojis, raw_string):
    if coolness(emoji) >= threshold:
        print(emoji)
