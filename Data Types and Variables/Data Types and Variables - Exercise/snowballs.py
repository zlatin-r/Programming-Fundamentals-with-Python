total_snowballs = int(input())
max_value = -9999999
best_ball = ""

for i in range(total_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_value:
        max_value = value
        best_ball = f"{weight} : {time} = {int(value)} ({quality})"

print(best_ball)

