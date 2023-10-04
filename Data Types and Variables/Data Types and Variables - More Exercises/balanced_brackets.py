n = int(input())
stack = []
open_brackets = 0
closed_brackets = 0
balance = True

for _ in range(n):
    line = input()

    if line == "(":
        stack.append(line)
        open_brackets += 1

    elif line == ")":
        stack.append(line)
        closed_brackets += 1

        if stack[0] == ")":
            balance = False
            continue

string = "".join(stack)

if "((" in string or "))" in string:
    balance = False

if open_brackets == closed_brackets and balance:
    print("BALANCED")
else:
    print("UNBALANCED")
