input_line = input().split(" ")
command = input().split(" ")
result = ""

if command[0] == "merge":
    start_index = int(command[1])
    end_index = int(command[2])

    for word in range(len(input_line)):
        if word == start_index or word <= end_index:
            result += input_line[word]
        else:
            result += ", " + input_line[word]
