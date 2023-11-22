import re

pattern = r"([@#])([a-zA-Z]{3,}\1\1[A-Za-z]{3,}\1)"
letters_pattern = r"[a-zA-Z]+"

text = input()
matches_list = []

matches = re.findall(pattern, text)
if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        filtered = re.findall(letters_pattern, match[1])
        if filtered[0] == filtered[1][::-1]:
            matches_list.append(f"{filtered[0]} <=> {filtered[1]}")
    if len(matches_list) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(matches_list))
else:
    print("No word pairs found!")
    print("No mirror words!")
