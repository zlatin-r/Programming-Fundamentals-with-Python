import re

pattern = r"[@][#]+([A-Z][A-Za-z0-9]{4,}[A-Z])[@][#]+"
digits_pattern = r"\d"

n = int(input())
for _ in range(n):
    text = input()
    match = re.findall(pattern, text)

    if match:
        group = re.findall(digits_pattern, match[0])
        if group:
            print(f"Product group: {''.join(group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
