import re

pattern = r"[@][#]+([A-Z][A-Za-z0-9]{4,}[A-Z])[@][#]+"
n = int(input())
valids = []

for _ in range(n):
    text = input()
    match = re.findall(pattern, text)

    if match:
        product_group = re.findall(r"\d", match[0])
        if product_group:
            num = "".join(product_group)
            print(f"Product group: {num}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
