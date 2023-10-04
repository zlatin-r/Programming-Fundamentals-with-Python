circle = list(map(int, input().split()))
k = int(input())

result = []
index = 0

while len(circle) > 0:

    prev = index + k - 1
    prev2 = len(circle)
    prev3 = prev % prev2

    index = (index + k - 1) % len(circle)
    executed_person = circle.pop(index)
    result.append(executed_person)

output = "[" + ",".join(map(str, result)) + "]"
print(output)
