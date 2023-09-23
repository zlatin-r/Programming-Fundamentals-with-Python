numbers = list(map(int, input().split(", ")))

if max(numbers) % 10 == 0:
    max_value = max(numbers) // 10
else:
    max_value = max(numbers) // 10 + 1

group_zero = []
group_of_10 = [x for x in numbers if x <= 10]
group_of_20 = [x for x in numbers if 10 < x <= 20]
group_of_30 = [x for x in numbers if 20 < x <= 30]
group_of_40 = [x for x in numbers if 30 < x <= 40]
group_of_50 = [x for x in numbers if 40 < x <= 50]
group_of_60 = [x for x in numbers if 50 < x <= 60]
group_of_70 = [x for x in numbers if 60 < x <= 70]
group_of_80 = [x for x in numbers if 70 < x <= 80]
group_of_90 = [x for x in numbers if 80 < x <= 90]
group_of_100 = [x for x in numbers if 90 < x <= 100]

total_groups = [group_zero, group_of_10, group_of_20, group_of_30, group_of_40, group_of_50, group_of_60, group_of_70,
                group_of_80, group_of_90, group_of_100]

for group in range(1, max_value + 1):
    print(f"Group of {group}0's: {total_groups[group]}")
