energy = int(input())
won_battles = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy}" )
        break
    if energy >= int(distance):
        energy -= int(distance)
        won_battles += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    if won_battles % 3 == 0:
        energy += won_battles