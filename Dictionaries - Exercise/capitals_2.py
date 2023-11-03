countries = input().split(", ")
capitals = input().split(", ")

result = {countries[index]: capitals[index] for index in range(len(countries))}

for state, cap in result.items():
    print(f"{state} -> {cap}")