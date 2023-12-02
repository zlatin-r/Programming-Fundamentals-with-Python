heroes = {}

n = int(input())
for _ in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = [int(hp), int(mp)]

command = input()
while command != "End":
    command = command.split(" - ")
    action, name = command[0], command[1]

    if action == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3]
        if heroes[name][1] >= mp_needed:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        heroes[name][0] -= damage
        if heroes[name][0] <= 0:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")

    elif action == "Recharge":
        amount_mp = int(command[2])
        current_hp = heroes[name][1]
        heroes[name][1] = min(heroes[name][1] + amount_mp, 200)
        recharged_hp = heroes[name][1] - current_hp
        print(f"{name} recharged for {recharged_hp} MP!")

    elif action == "Heal":
        amount_hp = int(command[2])
        current_mp = heroes[name][0]
        heroes[name][0] = min(heroes[name][0] + amount_hp, 100)
        healed_mp = heroes[name][0] - current_mp
        print(f"{name} healed for {healed_mp} HP!")

    command = input()

for hero, data in heroes.items():
    print(hero)
    print(f"  HP: {data[0]}")
    print(f"  MP: {data[1]}")
