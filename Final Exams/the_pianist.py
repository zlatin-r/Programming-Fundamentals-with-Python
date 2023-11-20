pieces = int(input())
data = {}

for _ in range(pieces):
    info = input().split("|")
    piece, composer, key = info[0], info[1], info[2]
    data[piece] = [composer, key]

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]

    if action == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece not in data:
            data[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        piece = command[1]
        if piece in data:
            data.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in data:
            data[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, data in data.items():
    print(f"{piece} -> Composer: {data[0]}, Key: {data[1]}")
