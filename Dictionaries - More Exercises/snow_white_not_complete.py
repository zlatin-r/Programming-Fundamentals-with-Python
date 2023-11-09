data = {}
result_list = []

dwarf_info = input()

while dwarf_info != "Once upon a time":
    name, color, physics = dwarf_info.split(" <:> ")

    if color not in data.keys():
        data[name] = data.get(name, {})
    data[name][color] = data[name].get(physics, 0)
    data[name][color] = max(int(physics), data[name][color])

    dwarf_info = input()


sorted_dwarfs = sorted(data.items(), key=lambda x: (-x[1], -sum(y[1] == x[0][1] for y in data.items()), x[0]))

for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
