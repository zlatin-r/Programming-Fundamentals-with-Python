sequence = list(map(int, input().split()))
moves = 0

while True:
    integers = input().split()
    moves += 1

    if integers == "end":
        print(f"Sorry you lose :(")
        print(f"{sequence}")
        break

    index1 = int(integers[0])
    index2 = int(integers[1])
    sequence_mid = len(sequence) // 2

    if index1 == index2 or 0 > index1 > len(sequence) or 0 > index2 > len(sequence):
        sequence[sequence_mid] = f"{sequence_mid}a" * 2
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {index1}!")
    elif sequence[index1] != sequence[index2]:
        print("Try again")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break


