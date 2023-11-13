names = input().split(", ")
valids = []

for name in names:
    is_valid = False
    if 3 <= len(name) <= 16:
        for letter in name:
            if letter.isalpha() or letter in "-_" or letter.isdigit():
                is_valid = True
            else:
                is_valid = False
                break
    if is_valid:
        valids.append(name)

print("\n".join(valids))
