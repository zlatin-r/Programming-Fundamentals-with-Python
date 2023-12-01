num_pieces = int(input())
pieces = {}

for _ in range(num_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]

command = input()
while command != "Stop":
    command = command.split("|")
    piece = command[1]

    if command[0] == "Add":
        if piece not in pieces.keys():
            pieces[piece] = [command[2], command[3]]
            print(f"{piece} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        if piece in pieces.keys():
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        if piece in pieces.keys():
            pieces[piece][1] = command[2]
            print(f"Changed the key of {piece} to {command[2]}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")
