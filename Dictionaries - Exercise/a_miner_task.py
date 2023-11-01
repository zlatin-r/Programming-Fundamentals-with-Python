dictionary = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    if resource not in dictionary:
        dictionary[resource] = 0
    dictionary[resource] += quantity

for key, quantity in dictionary.items():
    print(f"{key} -> {quantity}")


