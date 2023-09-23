input_line = input().split(" ")
command = input().split(" ")
result = ""

if command[0] == "merge":
    start_index = int(command[1])
    end_index = int(command[2])

    for word in range(len(input_line)):
        if end_index > len(input_line):
            end_index = len(input_line)
        else:
            if word == start_index or word <= end_index:
                result += input_line[word]
            else:
                result += ", " + input_line[word]

if command[0] == "divide":
    index = int(command[1])
    partitions = int(command[2])

    word = input_line[index]
    list_of_letters = [x for x in word]

    if len(list_of_letters) % 2 == 0:
        for i in range(0, len(list_of_letters), partitions):
            result += ", ".join(list_of_letters[i:partitions])

print(result)
