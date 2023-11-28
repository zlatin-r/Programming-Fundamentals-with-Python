import re

pattern = r"%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)\|[^\|\$\%\.]*([1-9]+[.0-9]*)\$"
total_income = 0

order = input()
while order != "end of shift":
    matches = re.search(pattern, order)

    if matches:
        client, product, quantity, price = matches.groups()
        bill = float(price) * int(quantity)
        print(f"{client}: {product} - {bill:.2f}")
        total_income += bill

    order = input()
print(f"Total income: {total_income:.2f}")
