price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()

sum_left = 0
sum_right = 0

entry_point_item = price_ratings[entry_point]

left_items = price_ratings[:entry_point]
right_items = price_ratings[entry_point + 1:]

if item_type == "cheap":
    sum_left = sum([x for x in left_items if x < entry_point_item])
    sum_right = sum([x for x in right_items if x < entry_point_item])
elif item_type == "expensive":
    sum_left = sum([x for x in left_items if x >= entry_point_item])
    sum_right = sum([x for x in right_items if x >= entry_point_item])

if sum_left == sum_right:
    print(f"Left - {sum_left}")
elif sum_left > sum_right:
    print(f"Left - {sum_left}")
else:
    print(f"Right - {sum_right}")
