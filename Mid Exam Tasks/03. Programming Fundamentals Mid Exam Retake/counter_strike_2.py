energy = int(input())
command = input()
count = 0

while True:
    if energy < int(command):
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break

    energy -= int(command)
    count += 1
    if count % 3 == 0:
        energy += count

    command = input()
    if command == "End of battle":
        print(f"Won battles: {count}. Energy left: {energy}")
        break
