total_price = 0
price_with_tax = 0
discount = 0

while True:
    part_price = input()

    if part_price == "special" or part_price == "regular":
        if part_price == "special":
            discount = 0.10
        break
    elif float(part_price) > 0:
        total_price += float(part_price)
    else:
        print("Invalid price!")

tax = total_price * 0.20
price_with_tax += tax + total_price
discount *= price_with_tax
price_with_tax -= discount

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_tax:.2f}$")
