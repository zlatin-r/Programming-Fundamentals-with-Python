sequence = input().split(" ")
string = input()
index = 0
result = ""

for number in sequence:

    for char in number:
        index += int(char)
    while index >= len(string):
        index -= len(string)

    result += string[index]
    string = string[:index] + string[index + 1:]
    index = 0
    
print(result)
