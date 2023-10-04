first_row = input().split(" ")
second_row = input().split(" ")
third_row = input().split(" ")

first_col = [first_row[0], second_row[0], third_row[0]]
second_col = [first_row[1], second_row[1], third_row[1]]
third_col = [first_row[2], second_row[2], third_row[2]]

diagonal_one = [first_col[0], second_col[1], third_col[2]]
diagonal_two = [first_col[2], second_col[1], third_col[0]]

total_combos = [first_row, second_row, third_row, first_col, second_col, third_col, diagonal_one, diagonal_two]

player_one_win = ["1", "1", "1"]
player_two_win = ["2", "2", "2"]
winner = ""

if player_one_win in total_combos:
    winner = "First player won"
elif player_two_win in total_combos:
    winner = "Second player won"
else:
    winner = "Draw!"
print(winner)
