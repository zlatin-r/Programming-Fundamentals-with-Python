fire_level = input().split("#")
water = int(input())
effort = 0
total_fire = 0
flag = False
print("Cells:")

while water > 0:
    for i in fire_level:
        index = i.index("=")
        fire_type = i[:index].strip(" ")
        cell_value = int(i[index + 1:].strip(" "))

        if fire_type == "High" and 81 <= cell_value <= 125 and water >= cell_value:
            flag = True
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
        elif fire_type == "Medium" and 51 <= cell_value <= 80 and water >= cell_value:
            flag = True
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
        elif fire_type == "Low" and 1 <= cell_value <= 50 and water >= cell_value:
            flag = True
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
        else:
            flag = False

        if flag:
            print(" -", cell_value)

    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {total_fire}")
    break
