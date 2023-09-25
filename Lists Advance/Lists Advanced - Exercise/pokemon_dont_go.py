line_input = input().split(" ")
sequence = [int(x) for x in line_input]
removed_elements = 0

while len(sequence) > 0:
    index = int(input())
    count = 0

    prev = len(sequence)
    prev2 = sequence[index]

    if index < 0:
        sequence.pop(0)
        sequence.insert(0, sequence[-1])
    if index > len(sequence):
        sequence.pop(-1)
        sequence.insert(0, sequence[-1])

    removed_elements += sequence[index]
    element = sequence[index]
    sequence.pop(index)

    for num in sequence:
        if num <= element:
            num += element
            sequence[count] = num
            count += 1
        elif num >= element:
            num -= element
            sequence[count] = num
            count += 1

print(sequence)
