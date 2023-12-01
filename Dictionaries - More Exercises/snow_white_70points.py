dwarfs = {}

dwarf_data = input()
while dwarf_data != "Once upon a time":
    name, hat_color, physics = dwarf_data.split(' <:> ')

    if hat_color not in dwarfs:
        dwarfs[hat_color] = {name: int(physics)}
    elif name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = int(physics)
    else:
        dwarfs[hat_color][name] = max(int(physics), dwarfs[hat_color][name])

    dwarf_data = input()

sorted_data = {k: dict(sorted(v.items(), key=lambda x: x[1], reverse=True)) for k, v in sorted(dwarfs.items(), key=lambda x: sum(x[1].values()), reverse=True)}

for color, data in sorted_data.items():
    for name, physics in data.items():
        print(f"({color}) {name} <-> {physics}")


