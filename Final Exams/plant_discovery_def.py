plants_count = int(input())
plants_data = {}


def valid(data, name):
    if name in data:
        return True
    print("error")


def rate(data, name, rating):
    data[name][1].append(int(rating))


def update(data, name, new_rarity):
    data[name][0] = new_rarity


def reset(data, name):
    data[name][1] = []


for _ in range(plants_count):
    plant, rarity = input().split("<->")
    plants_data[plant] = [rarity, []]

command = input()
while command != "Exhibition":
    command = command.split(":")
    action, plant_data = command[0], command[1]
    plant_data = plant_data.split(" - ")
    plant_name = plant_data[0].strip()

    if valid(plants_data, plant_name):
        if action == "Rate":
            rate(plants_data, plant_name, plant_data[1])

        elif action == "Update":
            update(plants_data, plant_name, plant_data[1])

        elif action == "Reset":
            reset(plants_data, plant_name)

    command = input()

print("Plants for the exhibition:")
for plant, info in plants_data.items():
    if len(info[1]) > 0:
        average_rating = sum(info[1]) / len(info[1])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {info[0]}; Rating: {average_rating:.2f}")
