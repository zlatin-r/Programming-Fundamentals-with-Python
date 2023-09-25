input_line = input().split(" ")


def merge(array):
    merged_list = ""
    start_index = int(command[1])
    end_index = int(command[2])

    for string in range(len(array)):
        if start_index >= len(array):
            merged_list = " ".join(array)
            break
        if end_index > len(array):
            end_index = len(array)

        if start_index <= string <= end_index:
            merged_list += "".join(array[string])
        elif string < start_index:
            merged_list += "".join(array[string]) + " "
        else:
            merged_list += " " + "".join(array[string])
    return merged_list.split(" ")


def divide(array):
    index = int(command[1])
    partitions = int(command[2])

    string = array[index]
    partition_length = len(string) // partitions
    reminder = len(string) % partitions

    new_parts = [string[i: i + partition_length] for i in
                 range(0, len(string), partition_length)]
    if reminder > 0:
        new_parts[-1] += string[-reminder:]
    array[index:index + 1] = new_parts
    return array


while True:
    command = input().split(" ")
    if command[0] == "merge":
        input_line = merge(input_line)
    elif command[0] == "divide":
        input_line = divide(input_line)
    elif command[0] == "3:1":
        print(" ".join(input_line))
        break
