targets = [int(x) for x in input().split(" ")]
command = input()
shot_targets = 0

while command != "End":
    index = int(command)
    if 0 <= index < len(targets):
        target = targets[index]
        targets[index] = -1
        shot_targets += 1

        for x in range(len(targets)):
            if targets[x] > target and targets[x] != -1:
                targets[x] -= target
            elif targets[x] <= target and targets[x] != -1:
                targets[x] += target

    command = input()

print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")
