pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
command = input().split()

while command[0] != "Retire":
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health > max_health:
                pirate_ship[index] = max_health
            else:
                pirate_ship[index] += health

    elif action == "Status":
        need_repair = [x for x in pirate_ship if x < max_health * 0.20]
        print(f"{len(need_repair)} sections need repair.")

    command = input().split()

if command[0] == "Retire":
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
