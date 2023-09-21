first_input = input()
second_input = input()


def data_type():
    if first_input == "int":
        print(int(second_input) * 2)
    elif first_input == "real":
        print(f"{float(second_input) * 1.5:.2f}")
    elif first_input == "string":
        print(f"${second_input}$")


data_type()
