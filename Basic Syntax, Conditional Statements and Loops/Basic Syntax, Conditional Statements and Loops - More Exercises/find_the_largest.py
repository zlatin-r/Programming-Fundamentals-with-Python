num = input()
digits = []

for i in range(len(num)):
    digits.append(int(num[i]))
    digits.sort()
    digits.reverse()

print("".join(map(str, digits)))
