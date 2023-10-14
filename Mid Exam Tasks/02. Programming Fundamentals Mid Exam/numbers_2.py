integers = list(map(int, input().split()))
average = sum(integers) / len(integers)

filtered = sorted([x for x in integers if x > average], key=lambda x: -x)

if len(filtered) > 0:
    print(*filtered[:5])
else:
    print("No")
