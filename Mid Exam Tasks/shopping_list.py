initial_list = input().split("!")
command = input().split(" ")

while True:
    action = command[0]

    if action == "Go":
        break
    elif action == "Urgent":
        item = command[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif action == "Unnecessary":
        item = command[1]
        if item in initial_list:
            index = initial_list.index(item)
            initial_list.pop(index)
    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item
    elif action == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input().split(" ")

print(", ".join(initial_list))


