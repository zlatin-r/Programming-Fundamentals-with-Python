rows = int(input())
matrix = []
destroyed_ships = 0

for _ in range(rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

attack_data = input().split(" ")

for i in attack_data:
    attack = [int(x) for x in i.split("-")]
    row = attack[0]
    col = attack[1]

    if matrix[row][col] > 0:
        matrix[row][col] -= 1
        if matrix[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)