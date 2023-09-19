gifts = input().split(" ")

while True:
    command = input().split(" ")

    if command[0] == "No" and command[1] == "Money":
        for k in gifts:
            if k != "None":
                print(k, end=" ")
        break

    elif command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"

    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
