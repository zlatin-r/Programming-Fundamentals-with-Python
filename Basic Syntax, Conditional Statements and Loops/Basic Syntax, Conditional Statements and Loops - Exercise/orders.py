n = int(input())
total_price = 0

for i in range(n):
    price_per_caps = float(input())
    days = int(input())
    caps_needed = int(input())

    if 2000 >= caps_needed >= 1 and 31 >= days >= 1 and 100 >= price_per_caps >= 0.01:
        price_coffe = (price_per_caps * caps_needed) * days
        total_price += price_coffe
        print(f"The price for the coffee is: ${price_coffe:.2f}")
    price_coffe = 0

print(f"Total: ${total_price:.2f}")
