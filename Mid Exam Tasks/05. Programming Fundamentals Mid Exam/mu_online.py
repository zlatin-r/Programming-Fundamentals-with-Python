rooms = input().split("|")
health = 100
bitcoins = 0
counter = 0
live = True

for room in rooms:
    room = room.split(" ")
    monster = room[0]
    points = int(room[1])
    counter += 1

    if monster != "potion" and monster != "chest":
        health -= points
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {counter}")
            live = False
            break
    elif monster == "potion":
        if health + points <= 100:
            health += points
            print(f"You healed for {points} hp.")
        else:
            healed_amount = 100 - health
            health = 100
            print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif monster == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

if live:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")


