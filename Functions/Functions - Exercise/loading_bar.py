number = int(input())


def loading_bar():
    string = ""
    string += "%" * (number // 10)
    string += "." * (10 - (number // 10))
    if number != 100:
        print(f"{number}% [{string}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{string}]")

loading_bar()
