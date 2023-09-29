rows = int(input())

matrix, moves, starting_row, starting_col = [], [], 0, 0

for row in range(rows):
    matrix.append(list(input()))
    if "k" in matrix[row]:
        starting_row, starting_col = row, matrix[row].index("k")

cols = len(matrix[0])


def find_way_out(row, col, step):
    if not 0 <= row < rows or not 0 <= col < cols or matrix[row][col] in "#*":
        return

    step += 1
    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        moves.append(step)

    matrix[row][col] = "*"
    [find_way_out(row, col, step) for row, col in
     ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col))]
    matrix[row][col] = " "
    step -= 1


find_way_out(starting_row, starting_col, 0)
if moves:
    print(f"Kate got out in {max(moves)} moves")
else:
    print("Kate cannot get out")