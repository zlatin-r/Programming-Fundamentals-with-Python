inventory = {"shards": 0, "fragments": 0, "motes": 0}

while True:
    items = input().split()

    for i in range(0, len(items), 2):
        quantity = int(items[i])
        item = (items[i + 1]).lower()

        if item not in inventory:
            inventory[item] = 0
        inventory[item] += quantity
        if inventory[item] >= 250:
            break

    if inventory["shards"] >= 250:
        inventory["shards"] -= 250
        print("Shadowmourne obtained!")
        break
    elif inventory["fragments"] >= 250:
        inventory["fragments"] -= 250
        print("Valanyr obtained!")
        break
    elif inventory["motes"] >= 250:
        inventory["motes"] -= 250
        print("Dragonwrath obtained!")
        break

for key, value in inventory.items():
    print(f"{key}: {value}")
