pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input().split()
    action = command[0]

    if action == "Retire":
        break
    elif action == "Fire":
        index = int(command[1])
        damage = int(command[2])

        if 0 <= index <= len(war_ship) - 1:
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if 0 <= start_index <= len(war_ship) - 1 and 0 <= end_index <= len(war_ship) - 1:




print(pirate_ship)