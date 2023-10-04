sequence = input().split(" ")
mid = len(sequence) // 2
left_racer = list(map(int, sequence[:mid]))
right_racer = list(map(int, sequence[mid + 1:]))
time_left = 0
time_right = 0

for i in left_racer:
    if i == 0:
        time_left *= 0.80
    time_left += i
for i in reversed(right_racer):
    if i == 0:
        time_right *= 0.80
    time_right += i

if time_left < time_right:
    winner = "left"
else:
    winner = "right"

print(f"The winner is {winner} with total time: {min(time_left, time_right):.1f}")
