to_do_list = [0] * 10

while True:
    command = input().split("-")
    if command[0] == 'End':
        break

    importance = int(command[0]) - 1
    to_do = command[1]

    to_do_list.pop(importance)
    to_do_list.insert(importance, to_do)

result = [el for el in to_do_list if el != 0]
print(result)
