string = input()

digits = ""
letters = ""
other = ""

for symb in string:
    if symb.isdigit():
        digits += symb
    elif symb.isalpha():
        letters += symb
    else:
        other += symb
print(f"{digits}\n{letters}\n{other}")
