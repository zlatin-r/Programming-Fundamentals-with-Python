n = int(input())
cars_data = {}

for i in range(n):
    car, mileage, fuel = input().split("|")
    cars_data[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    command = command.split(" : ")
    action, car = command[0], command[1]

    if action == "Drive":
        distance, needed_fuel = int(command[2]), int(command[3])

        if cars_data[car][1] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_data[car][0] += distance
            cars_data[car][1] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")

        if cars_data[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars_data.pop(car)

    elif action == "Refuel":
        fuel_to_fill = int(command[2])
        fuel_in_tank = cars_data[car][1]
        cars_data[car][1] = min(cars_data[car][1] + fuel_to_fill, 75)
        print(f"{car} refueled with {cars_data[car][1] - fuel_in_tank} liters")

    elif action == "Revert":
        kilometers = int(command[2])
        cars_data[car][0] -= kilometers

        if cars_data[car][0] < 10000:
            cars_data[car][0] = 10000
        print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, data in cars_data.items():
    print(f"{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")
