initial_list = [int(x) for x in input().split(' ')]
command = input().split(' ')
action = command[0]

while action != "end":

    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])

        initial_list[index_1], initial_list[index_2] = initial_list[index_2], initial_list[index_1]

    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])

        product = initial_list[index_1] * initial_list[index_2]
        initial_list[index_1] = product

    elif action == "decrease":
        for i in range(len(initial_list)):
            initial_list[i] -= 1

    command = input().split(" ")
    action = command[0]

print(" ".join(str(x) for x in initial_list))
