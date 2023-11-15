lines = int(input())

for person in range(lines):
    data = input()
    name = ""
    age = ""
    for char in range(len(data)):
        if data[char] == "@":
            while data[char] != "|":
                char += 1
                name += data[char]
        if data[char] == "#":
            while data[char] != "*":
                char += 1
                age += data[char]
    print(f"{name.rstrip('|')} is {age.rstrip('*')} years old.")
