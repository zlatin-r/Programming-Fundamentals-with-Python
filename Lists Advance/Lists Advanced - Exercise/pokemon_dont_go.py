line_input = input().split(" ")
sequence = [int(x) for x in line_input]
removed_elements = 0

while len(sequence) > 0:
    index = int(input())
    count = 0

    if index < 0:
        sequence.pop(0)
        sequence.insert(0, sequence[-1])
        removed_elements += sequence[index - 1]
        continue
    if index >= len(sequence):
        sequence.pop(-1)
        sequence.append(sequence[0])
        removed_elements += sequence[index-1]
        index -= 1

    removed_elements += sequence[index]
    element = sequence[index]

    for num in sequence:
        if num <= element:
            num += element
            sequence[count] = num
            count += 1
        elif num >= element:
            num -= element
            sequence[count] = num
            count += 1

    sequence.pop(index)

print(sequence)
