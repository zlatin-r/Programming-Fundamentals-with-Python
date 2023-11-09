data = {}
data_input = input()

while data_input != "no more time":
    user_name, contest, points = data_input.split(" -> ")

    if user_name not in data:
        data[user_name] = data.get(user_name, {})
        data[user_name][contest] = data[user_name].get()

    data_input = input()
