lines = int(input())
chars_sum = 0

for i in range(lines):
    char = input()
    chars_sum += ord(char)

print(f"The sum equals: {chars_sum}")
