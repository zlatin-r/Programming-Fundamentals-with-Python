countries = input().split(", ")
capitals = input().split(", ")

result = {k: v for (k, v) in zip(countries, capitals)}

for state, cap in result.items():
    print(f"{state} -> {cap}")
