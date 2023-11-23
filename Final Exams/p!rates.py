cities_data = {}

command = input()
while command != "Sail":
    city, population, gold = command.split("||")

    if city in cities_data:
        cities_data[city]["population"] += int(population)
        cities_data[city]["gold"] += int(gold)
    else:
        cities_data[city] = {"population": int(population), "gold": int(gold)}

    command = input()

events = input()
while events != "End":
    events = events.split("=>")
    action, town = events[0], events[1]

    if action == "Plunder":
        people, gold = int(events[2]), int(events[3])
        cities_data[town]["population"] -= people
        cities_data[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_data[town]["population"] <= 0 or cities_data[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            cities_data.pop(town)
    elif action == "Prosper":
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_data[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_data[town]['gold']} gold.")

    events = input()

if len(cities_data) > 0:
    print(f"Ahoy, Captain! There are {len(cities_data)} wealthy settlements to go to:")
    for city, data in cities_data.items():
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
