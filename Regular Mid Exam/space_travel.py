route = input().split("||")
fuel = int(input())
ammunition = int(input())

for commands in route:
    command = commands.split()

    if command[0] == "Travel":
        distance = int(command[1])
        if fuel - distance >= 0:
            print(f"The spaceship travelled {distance} light-years.")
            fuel -= distance
        else:
            print("Mission failed.")
            exit()

    elif command[0] == "Enemy":
        armour = int(command[1])
        if ammunition >= armour:
            ammunition -= armour
            print(f"An enemy with {armour} armour is defeated.")
        elif ammunition < armour:
            if armour * 2 <= fuel:
                fuel -= armour * 2
                print(f"An enemy with {armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                exit()

    elif command[0] == "Repair":
        add = int(command[1])
        add_ammo = add * 2
        add_fuel = add

        ammunition += add_ammo
        fuel += add_fuel

        print(f"Ammunitions added: {add_ammo}.")
        print(f"Fuel added: {add_fuel}.")

    elif command[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        exit()



