initial_loot = input().split("|")
data_info = input()

while data_info != "Yohoho!":

    command, *data = [x for x in data_info.split()]

    if command == "Loot":
        for item in data:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command == "Drop":
        index = int(data[0])
        if len(initial_loot) > index >= 0:
            initial_loot.append(initial_loot.pop(index))

    elif command == "Steal":
        count = int(data[0])
        stolen_items = initial_loot[-count:]
        initial_loot = initial_loot[:-count]
        print(*stolen_items, sep=", ")

    data_info = input()

if initial_loot:
    average_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
