bakery = {}

while True:
    command = input()

    if command == "statistics":
        print("Products in stock:")
        for product in bakery:
            print(f"- {product} {bakery[product]}")
        # or [print(f"- {product}: {bakery[product]}") for product in bakery]

        print(f"Total Products: {len(bakery)}")
        print(f"Total Quantity: {sum(bakery.values())}")
        break

    product, (quantity) = command.split()

    if product in bakery:
        bakery[product] += int(quantity)
    else:
        bakery[product] = int(quantity)
