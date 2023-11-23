heroes = int(input())
heroes_data = {}

for _ in range(heroes):
    name, hit_points, mana_points = input().split()
    heroes_data[name] = {"HP": int(hit_points), "MP": int(mana_points)}

commands = input()
while commands != "End":
    commands = commands.split("-")
    action, hero_name = commands[0].strip(), commands[1].strip()

    if action == "CastSpell":
        mp_needed, spell_name = int(commands[2]), commands[3].strip()
        if heroes_data[hero_name]["MP"] >= mp_needed:
            MP_left = heroes_data[hero_name]["MP"] - mp_needed
            heroes_data[hero_name]["MP"] = MP_left
            print(f"{hero_name} has successfully cast {spell_name} and now has {MP_left} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage, attacker = int(commands[2]), commands[3].strip()
        heroes_data[hero_name]["HP"] -= damage
        if heroes_data[hero_name]["HP"] <= 0:
            heroes_data.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            current_damage = heroes_data[hero_name]["HP"]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_damage} HP left!")

    elif action == "Recharge":
        amount = int(commands[2])
        current_MP = heroes_data[hero_name]["MP"]
        heroes_data[hero_name]["MP"] = min(heroes_data[hero_name]["MP"] + amount, 200)
        amount_recovered = heroes_data[hero_name]["MP"] - current_MP
        print(f"{hero_name} recharged for {amount_recovered} MP!")

    elif action == "Heal":
        amount = int(commands[2])
        current_HP = heroes_data[hero_name]["HP"]
        heroes_data[hero_name]["HP"] = min(heroes_data[hero_name]["HP"] + amount, 100)
        amount_recovered = heroes_data[hero_name]["HP"] - current_HP
        print(f"{hero_name} healed for {amount_recovered} HP!")

    commands = input()

for hero, data in heroes_data.items():
    print(hero)
    print(f"  HP: {data['HP']}")
    print(f"  MP: {data['MP']}")
