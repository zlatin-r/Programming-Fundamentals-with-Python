integers = [int(x) for x in input().split(" ")]
command = input().split(" ")
action = command[0]

while action != "end":

    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        integers[index_1], integers[index_2] = integers[index_2], integers[index_1]
    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        product = integers[index_1] * integers[index_2]
        integers[index_1] = product
    elif action == "decrease":
        integers = [x - 1 for x in integers]

    command = input().split(" ")
    action = command[0]

print(", ".join(map(str, integers)))
