items_journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(items_journal))
        break

    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect":
        if item not in items_journal:
            items_journal.append(item)
    elif action == "Drop":
        if item in items_journal:
            items_journal.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in items_journal:
            index_old_item = items_journal.index(old_item)
            items_journal.insert(index_old_item + 1, new_item)
    elif action == "Renew":
        if item in items_journal:
            items_journal.remove(item)
            items_journal.append(item)




