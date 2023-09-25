sequence_int = [int(x) for x in input().split(" ")]


def check_index(index_value, sequence):                     # problem
    if index_value < 0:
        sequence.pop(0)
        sequence.append(sequence[-1])
    elif index_value >= len(sequence):
        sequence.pop(-1)
        sequence.append(sequence[0])
    return index_value, sequence


def remove_element(sequence, element):                     # works good
    sequence.pop(element)
    return sequence


def increase_decrease(sequence):                            # works good
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


def sum_removed(element):                             # works good
    removed_sum = 0
    removed_sum += element
    return removed_sum


while len(sequence_int) != 0:
    index = int(input())

    check_index(index, sequence_int)

    element_to_remove = int(sequence_int[index])    # problem

    sum_removed(element_to_remove)
    remove_element(sequence_int, index)
    increase_decrease(sequence_int)
