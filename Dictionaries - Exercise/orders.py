products = {}
command = input()

while command != "buy":

    product, price, quantity = command.split(" ")
    quantity = int(quantity)
    price = float(price)

    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][1] += quantity
        products[product][0] = price

    command = input()

for k, v in products.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")
