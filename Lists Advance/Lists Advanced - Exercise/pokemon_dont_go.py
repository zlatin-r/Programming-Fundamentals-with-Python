sequence_int = [int(x) for x in input().split(" ")]
sum_removed = 0


while len(sequence_int) > 0:
    index = int(input())

    if index < 0:
        sequence_int[0] = sequence_int[-1]
    elif index > len(sequence_int):
        sequence_int[-1] = sequence_int[0]
        index = len(sequence_int) - 1
        element = sequence_int[index]
        sum_removed += sequence_int[index]
        counter = 0
        for num in sequence_int:
            if num <= element:
                num += element
                sequence_int[counter] = num
                counter += 1
            else:
                num -= element
                sequence_int[counter] = num
                counter += 1

    else:
        element = sequence_int[index]
        sum_removed += sequence_int[index]
        counter = 0
        for num in sequence_int:
            if num <= element:
                num += element
                sequence_int[counter] = num
                counter += 1
            else:
                num -= element
                sequence_int[counter] = num
                counter += 1
        sequence_int.pop(index)

print(sum_removed)
