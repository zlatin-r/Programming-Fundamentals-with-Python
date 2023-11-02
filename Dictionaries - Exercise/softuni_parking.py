n = int(input())
database = {}

for user in range(n):
    data = input().split()
    command = data[0]
    name = data[1]

    if command == "register":
        plate = data[2]
        if name in database:
            print(f"ERROR: already registered with plate number {database[name]}")
        else:
            database[name] = plate
            print(f"{name} registered {database[name]} successfully")
    else:
        if name not in database:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            database.pop(name)

for name, plate in database.items():
    print(f"{name} => {plate}")