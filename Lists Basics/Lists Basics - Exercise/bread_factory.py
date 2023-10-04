import sys
events = input().split("|")
energy = 100
coins = 100

for event in events:
    event_data = event.split("-")
    event_name = event_data[0]
    points = int(event_data[1])

    if event_name == "rest":
        if energy + points >= 100:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.")
        else:
            energy += points
            print(f"You gained {points} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        earn = points
        if energy >= 30:
            coins += earn
            energy -= 30
            print(f"You earned {earn} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - points >= 0:
            coins -= points
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            sys.exit()
print(f"Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
