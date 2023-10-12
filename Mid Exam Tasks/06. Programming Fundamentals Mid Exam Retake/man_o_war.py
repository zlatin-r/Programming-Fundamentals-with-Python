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

        pirate_ship = [num - damage for num in pirate_ship if start_index <= pirate_ship.index(num) <= end_index]
        xax

    print(pirate_ship)
