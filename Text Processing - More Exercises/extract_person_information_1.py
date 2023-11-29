num_names = int(input())
name, age = "", ""

for _ in range(num_names):
    string = input()

    index_1 = string.index("@")
    index_2 = string.index("|")
    index_3 = string.index("#")
    index_4 = string.index("*")

    name = string[index_1 + 1:index_2]
    age = string[index_3 + 1:index_4]

    print(f"{name} is {age} years old.")
