sequence_of_elements = input().split(" ")
command = input().split(" ")
counter = 0

while True:
    counter += 1
    index1 = int(command[0])
    index2 = int(command[1])

    if (index1 == index2) or (index1 > len(sequence_of_elements) - 1) or (index1 < 0) or (
            index2 > len(sequence_of_elements) - 1) or (index2 < 0):
        mid_index = len(sequence_of_elements) // 2
        add_nums = f"-{counter}a"
        sequence_of_elements.insert(mid_index, add_nums)
        sequence_of_elements.insert(mid_index, add_nums)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[index1] == sequence_of_elements[index2]:
            element = sequence_of_elements[index1]
            sequence_of_elements.remove(element)
            sequence_of_elements.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {counter} turns!")
        break

    command = input().split(" ")
    if command[0] == "end":
        result = " ".join(sequence_of_elements)
        print(f"Sorry you lose :(\n{result}")
        break



