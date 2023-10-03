initial_list = [int(x) for x in input().split(' ')]
command = input().split(' ')

while command[0] != "end":

    if command == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])

        initial_list[index_1], initial_list[index_2] = initial_list[index_2], initial_list[index_1]

    elif command == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])

        product = initial_list[index_1] * initial_list[index_2]
        initial_list.insert(0, product)

    elif
