elements = input().split()

bakery = {}

for product in range(0, len(elements), 2):
    key = elements[product]
    value = elements[product + 1]
    bakery[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left.")
    else:
        print(f"Sorry, we don't have {product}")

