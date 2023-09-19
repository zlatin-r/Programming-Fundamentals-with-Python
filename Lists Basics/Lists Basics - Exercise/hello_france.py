items = input().split("|")
budget = float(input())
profit = 0
spending = 0

for i in items:
    index = i.index(">")
    item = i[:index - 1]
    price = float(i[index + 1:])

    if item == "Clothes" and price > 50:
        pass
    elif item == "Shoes" and price > 35:
        pass
    elif item == "Accessories" and price > 20.50:
        pass
    elif price > budget:
        pass
    else:
        budget -= price
        spending += price
        new_price = price * 1.40
        profit += new_price
        print(f"{new_price:.2f}", end=" ")
print()
print(f"Profit: {profit - spending:.2f}")

if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
