lines = int(input())
lst = []
filtered = []

for _ in range(lines):
    num = int(input())
    lst.append(num)

command = input()

if command == "even":
    for i in lst:
        if i % 2 == 0:
            filtered.append(i)
elif command == "odd":
    for i in lst:
        if i % 2 != 0:
            filtered.append(i)
elif command == "negative":
    for i in lst:
        if i < 0:
            filtered.append(i)
elif command == "positive":
    for i in lst:
        if i >= 0:
            filtered.append(i)

print(filtered)
