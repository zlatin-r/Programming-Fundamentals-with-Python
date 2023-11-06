inventory = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    items = input().split()

    for i in range(0, len(items), 2):
        quantity = int(items[i])
        item = (items[i + 1]).lower()

        if item not in inventory:
            inventory[item] = 0
        inventory[item] += quantity

        if inventory["shards"] >= 250:
            inventory["shards"] -= 250
            print("Shadowmourne obtained!")
            obtained = True
        elif inventory["fragments"] >= 250:
            inventory["fragments"] -= 250
            print("Valanyr obtained!")
            obtained = True
        elif inventory["motes"] >= 250:
            inventory["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break

for key, val in inventory.items():
    print(f"{key}: {val}")
