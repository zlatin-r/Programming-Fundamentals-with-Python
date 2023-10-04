key = int(input())
lines = int(input())
result = ""

for i in range(lines):
    letter = input()
    result += chr(ord(letter) + key)

print(result)
