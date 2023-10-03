initial_list = [int(x) for x in input().split(" ")]
greater_list = []

average_number = sum(initial_list) / len(initial_list)

for num in initial_list:
    if num > average_number:
        greater_list.append(num)

greater_list.sort(reverse=True)

if len(greater_list) > 0:
    print(" ".join(str(x) for x in greater_list[:5]))
else:
    print("No")
