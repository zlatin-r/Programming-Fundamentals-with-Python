integers = [int(x) for x in input().split(" ")]
sum_of_removed = 0


def increase_decrease(sequence):
    counter = 0

    for num in sequence:
        if num <= element_to_remove:
            sequence[counter] = num + element_to_remove
            counter += 1
        else:
            sequence[counter] = num - element_to_remove
            counter += 1
    return sequence


while len(integers) > 0:
    index = int(input())

    if index < 0:
        integers[0] = integers[-1]
        index = 0
        element_to_remove = integers[index]
        increase_decrease(integers)
    elif index >= len(integers):
        integers[-1] = integers[0]
        index = len(integers) - 1
        element_to_remove = integers[index]
        increase_decrease(integers)
    else:
        element_to_remove = integers[index]
        increase_decrease(integers)
        integers.pop(index)

    sum_of_removed += element_to_remove

print(sum_of_removed)
