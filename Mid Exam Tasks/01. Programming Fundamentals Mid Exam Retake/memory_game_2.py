sequence = input().split()
moves = 0

while True:
    integers = input().split()

    if integers[0] == "end":
        print(f"Sorry you lose :(")
        print(" ".join(map(str, sequence)))
        break

    moves += 1
    index1 = int(integers[0])
    index2 = int(integers[1])
    sequence_mid = len(sequence) // 2

    if index1 == index2 or 0 > index1 or index1 > len(sequence) - 1 or 0 > index2 or index2 > len(sequence) - 1:
        sequence.insert(sequence_mid, f"-{moves}a")
        sequence.insert(sequence_mid, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        sequence_el = sequence[index1]
        sequence.remove(sequence_el)
        sequence.remove(sequence_el)
    elif sequence[index1] != sequence[index2]:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break




