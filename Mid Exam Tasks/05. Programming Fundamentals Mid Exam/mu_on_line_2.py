dungeon = input().split("|")
health = 100
bitcoins = 0
count = 0

for rooms in dungeon:
    count += 1
    room = rooms.split(" ")
    command = room[0]
    points = int(room[1])

    if command == "potion":
        if health + points > 100:
            healed_points = 100 - health
            health = 100
            print(f"You healed for {healed_points} hp.")
        else:
            health += points
            print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        health -= points
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count}")
            exit()
        else:
            print(f"You slayed {command}.")

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")

