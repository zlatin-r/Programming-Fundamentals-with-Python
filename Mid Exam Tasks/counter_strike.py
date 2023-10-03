energy = int(input())
command = input()

battles_won = 0
win = True

while command != "End of battle":
    energy -= int(command)

    if energy <= 0:
        win = False
        break

    battles_won += 1
    if battles_won % 3 == 0:
        energy += battles_won

if win:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
