total_price = 0
total_price_without_taxes = 0
total_amount_of_taxes = 0
discount = 0
valid_order = True

while True:
    part_price = input()
    if part_price == "special":
        discount = 0.10
        break
    elif part_price == "regular":
        break
    part_price = float(part_price)
    if part_price < 0:
        print("Invalid price!")
        continue

    total_price_without_taxes += part_price
    tax = part_price * 0.20
    total_amount_of_taxes += tax
    part_price += tax
    total_price += part_price

if total_price == 0:
    print("Invalid order!")
    valid_order = False

discount = total_price * discount
total_price -= discount

if valid_order:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")



