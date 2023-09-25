input_line = input().split(" ")


def merge(array):
    merged_list = ""
    start_index = int(command[1])
    end_index = int(command[2])

    for word in range(len(array)):
        if start_index >= len(array):
            merged_list = " ".join(array)
            break
        if end_index > len(array):
            end_index = len(array)

        if start_index <= word <= end_index:
            merged_list += "".join(array[word])
        elif word < start_index:
            merged_list += "".join(array[word]) + " "
        else:
            merged_list += " " + "".join(array[word])
    return merged_list.split(" ")


def divide(array):
    index = int(command[1])
    partitions = int(command[2])

    string = input_line[index]
    partition_length = len(string) // partitions
    reminder = len(string) % partitions

    new_parts = [string[i: i + partition_length] for i in
                 range(0, len(string), partition_length)]
    if reminder > 0:
        new_parts[-1] += string[-reminder:]
    input_line[index:index + 1] = new_parts
    return input_line


while True:
    command = input().split(" ")
    if command[0] == "merge":
        input_line = merge(input_line)
        print(input_line)

    elif command[0] == "divide":
        input_line = divide(input_line)
        print(divide(input_line))
    elif command[0] == "3:1":
        print(input_line)
        break
