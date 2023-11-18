import re

bought = []
total_cost = 0
command = input()
pattern = r">>([\w]+)<<([\d\.?]+)!([\d])"

while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
print("\n".join(bought))
print(f"Total money spend: {total_cost}")
