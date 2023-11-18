import re

name = r"%([A-Z][a-z]+)%"
product = r"<(\w+)>"
count = r"\|(\d+)\|"
price = r"(\d+\.?\d*)\$"

line = input()
total_income = 0
bill = 0

while line != "end of shift":
    name_match = re.findall(name, line)
    product_match = re.findall(product, line)
    count_match = re.findall(count, line)
    price_match = re.findall(price, line)

    if name_match and product_match and count_match and price_match:

        bill = float(price_match[0]) * int(count_match[0])
        print(f"{name_match[0]}: {product_match[0]} - {bill:.2f}")
        total_income += bill
        bill = 0

    line = input()

print(f"Total income: {total_income:.2f}")
