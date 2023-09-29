main_string = input()

numbers, letters, output = [], [], []
[numbers.append(int(x)) if x.isdigit() else letters.append(x) for x in main_string]
while numbers:
    take, skip = numbers.pop(0), numbers.pop(0)

    # for x in range(0, len(numbers), 2): - no while loop / this is faster method
    #     take, skip = numbers[x], numbers[x + 1]

    output += letters[:take]
    letters = letters[take + skip:]

print(*output, sep="")
