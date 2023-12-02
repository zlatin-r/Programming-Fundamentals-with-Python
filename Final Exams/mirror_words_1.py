import re

initial_string = input()
mirror_words = []

pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(pattern, initial_string)

if matches:
    print(f"{len(matches)} word pairs found!")

    for match in matches:
        if match[1] == match[2][::-1]:
            pair = f"{match[1]} <=> {match[2]}"
            mirror_words.append(pair)
    if len(mirror_words) > 0:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")

