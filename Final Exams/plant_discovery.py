number_of_plants = int(input())

plants_info = {}

for plant in range(number_of_plants):
    plant_name, rarity = input().split("<->")
    plants_info[plant_name] = [rarity, []]