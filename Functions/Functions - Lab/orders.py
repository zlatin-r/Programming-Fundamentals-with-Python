product = input()
quantity = int(input())


def bill(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


print(f"{bill(product, quantity):.2f}")
