phone_book = {}

while True:
    info = input().split("-")

    if len(info) == 1:
        for i in range(int(info[0])):
            searched_name = input()
            if searched_name in phone_book.keys():
                print(f"{searched_name} -> {phone_book.get(searched_name)}")
            else:
                print(f"Contact {searched_name} does not exist.")
        break

    name, number = info
    if name not in phone_book:
        phone_book[name] = number
    phone_book[name] = number
