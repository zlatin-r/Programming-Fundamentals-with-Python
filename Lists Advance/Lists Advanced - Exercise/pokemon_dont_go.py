sequence_int = [int(x) for x in input().split(" ")]
sum_removed = 0


def check_index_negative(index_value, sequence):  # problem
    if index_value < 0:
        sequence.pop(0)
        sequence.append(sequence[-1])
    return sequence


def check_index_positive(index_value, sequence):
    sequence.pop(-1)
    sequence.append(sequence[0])
    global index
    index = len(sequence) - 1
    return sequence


def remove_element(sequence, element):  # works good
    sequence.pop(element)
    return sequence


def increase_decrease(sequence):  # works good
    counter = 0
    for number in sequence:
        if number <= element_to_remove:
            number += element_to_remove
            sequence[counter] = number
            counter += 1
        else:
            number -= element_to_remove
            sequence[counter] = number
            counter += 1
    return sequence


while len(sequence_int) > 0:
    index = int(input())

    check_index_negative(index, sequence_int)
    if index >= len(sequence_int):
        check_index_positive(index, sequence_int)
        element_to_remove = int(sequence_int[index])
        sum_removed += element_to_remove
        increase_decrease(sequence_int)
        continue

    element_to_remove = int(sequence_int[index])
    sum_removed += element_to_remove
    remove_element(sequence_int, index)
    increase_decrease(sequence_int)

print(sum_removed)