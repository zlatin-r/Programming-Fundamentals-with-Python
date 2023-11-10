dragons_data = {}
num_dragons = int(input())

for dragon in range(num_dragons):
    dragon_type, name, damage, health, armor = input().split()

    dragons_data[dragon_type] = dragons_data.get(dragon_type, {})
    dragons_data[dragon_type][name] = dragons_data[dragon_type].get(name, [])
    dragons_data[dragon_type][name].append(damage)
    dragons_data[dragon_type][name].append(health)
    dragons_data[dragon_type][name].append(armor)

    if damage == "null":
        dragons_data[dragon_type][name][0] = 250
    if health == "null":
        dragons_data[dragon_type][name][1] = 45
    if armor == "null":
        dragons_data[dragon_type][name][2] = 10


