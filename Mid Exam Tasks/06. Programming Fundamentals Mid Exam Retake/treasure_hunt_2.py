chest = input().split("|")
command = input().split()
stolen_items = []

while command[0] != "Yohoho!":

    if command[0] == "Loot":
        for i in command[1:]:
            if i not in chest:
                chest.insert(0, i)
    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(chest):
            chest.append(chest[index])
            chest.pop(index)
    elif command[0] == "Steal":
        count = int(command[1])
        if count < len(chest):
            stolen_items = chest[-count:]
            print(", ".join(stolen_items))
            chest = chest[:-count]
        else:
            stolen_items = chest
            chest = []
    command = input().split()

if len(chest) > 0:
    average_gain = sum([len(x) for x in chest]) / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print(", ".join(stolen_items))
    print("Failed treasure hunt.")
