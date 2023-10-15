journal = input().split(", ")

while True:
    command = input().split(" - ")

    if command[0] == "Collect":
        if command[1] not in journal:
            journal.append(command[1])

    elif command[0] == "Drop":
        if command[1] in journal:
            journal.remove(command[1])

    elif command[0] == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)

    elif command[0] == "Renew":
        if command[1] in journal:
            index = journal.index(command[1])
            journal.append(command[1])
            journal.pop(index)

    elif command[0] == "Craft!":
        print(", ".join(journal))
        break
