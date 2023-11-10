dragons_data = {}
num_dragons = int(input())
count_dragons = 0

for dragon in range(num_dragons):
    dragon_type, name, damage, health, armor = input().split()

    if dragon_type in dragons_data and name in dragons_data[dragon_type]:
        dragons_data[dragon_type].pop(name)

    dragons_data[dragon_type] = dragons_data.get(dragon_type, {})
    dragons_data[dragon_type][name] = dragons_data[dragon_type].get(name, [])
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    dragons_data[dragon_type][name].append(int(damage))
    dragons_data[dragon_type][name].append(int(health))
    dragons_data[dragon_type][name].append(int(armor))

for type_dragon, data in dragons_data.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for damage in data.values():
        total_damage += damage[0]
        total_health += damage[1]
        total_armor += damage[2]
        count_dragons = len(dragons_data[type_dragon].keys())
    print(f"{type_dragon}::({(total_damage / count_dragons):.2f}/"
          f"{(total_health / count_dragons):.2f}/"
          f"{(total_armor / count_dragons):.2f})")
    for dragon, info in sorted(dragons_data[type_dragon].items()):
        print(f"-{dragon} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")
