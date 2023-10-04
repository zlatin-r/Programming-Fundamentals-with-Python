targets = [int(x) for x in input().split(" ")]
count = 0

while True:
    command = input()
    if command == "End":
        result = " ".join(str(x) for x in targets)
        print(f"Shot targets: {count} -> {result}")
        break

    index = int(command)
    if index > len(targets) - 1:
        continue
    target_value = targets[index]
    targets[index] = -1
    count += 1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        elif targets[i] > target_value:
            targets[i] -= target_value
        elif targets[i] <= target_value:
            targets[i] += target_value
