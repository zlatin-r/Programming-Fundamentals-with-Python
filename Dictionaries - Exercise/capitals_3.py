countries = input().split(", ")
capitals = input().split(", ")

result = dict(zip(countries, capitals))

for state, cap in result.items():
    print(f"{state} -> {cap}")
