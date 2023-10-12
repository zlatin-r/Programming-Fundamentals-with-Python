pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
stalemate = True

while True:
    command = input().split()
    action = command[0]

    if action == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(war_ship)}")
        exit()

    elif action == "Fire":
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

        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for x in range(start_index, end_index + 1):
                pirate_ship[x] -= damage
                if pirate_ship[x] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif action == "Status":
        threshold = max_health * 0.20

        sections_for_repair = [section for section in pirate_ship if section < threshold]
        print(f"{len(sections_for_repair)} sections need repair.")
