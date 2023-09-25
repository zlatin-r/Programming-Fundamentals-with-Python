input_line = input().split(" ")
command = input().split(" ")


def merge(array):
    merged_list = ""
    start_index = int(command[1])
    end_index = int(command[2])

    for word in range(len(array)):
        if end_index > len(array):
            end_index = len(array)
        else:
            if word == start_index or word <= end_index:
                merged_list += "".join(array[word])
            else:
                merged_list += " " + "".join(array[word])
    array = merged_list
    return array


print(merge(input_line))
print(input_line)


if command[0] == "divide":
    index = int(command[1])
    partitions = int(command[2])

    word = input_line[index]
    list_of_letters = [x for x in word]

    if len(list_of_letters) % 2 == 0:
        for i in range(0, len(list_of_letters), partitions):
            result += ", ".join(list_of_letters[i:partitions])

print(result)
