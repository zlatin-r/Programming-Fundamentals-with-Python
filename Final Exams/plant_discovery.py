lines = int(input())
plants_data = {}

for _ in range(lines):
    info = input().split("<->")
    plant, rarity = info[0], int(info[1])
    plants_data[plant] = [rarity]

command = input()
while command != "Exhibition":
    command = command.split(":")
    action, data = command[0].strip(), command[1].strip()

    if action == "Rate":
        data = data.split(" - ")
        plant, rating = data[0], int(data[1])
        plants_data[plant].append(rating)

    elif action == "Update":
        data = data.split(" - ")
        plant, new_rarity = data[0], int(data[1])
        plants_data[plant][0] = new_rarity

    elif action == "Reset":
        plants_data[data] = plants_data[data][:1]

    command = input()

print("Plants for the exhibition:")
for plant, info in plants_data.items():
    sum_rating = sum(plants_data[plant][1:])
    if len(plant) == 0:
        print("error")
    else:
        if sum_rating > 0:
            average_rating = sum_rating / len(plants_data[plant][1:])
        else:
            average_rating = 0
        print(f"- {plant}; Rarity: {plants_data[plant][0]}; Rating: {average_rating:.2f}")