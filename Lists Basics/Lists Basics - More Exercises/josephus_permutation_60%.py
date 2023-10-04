circle = input().split(" ")
k = int(input())
index = 0
result = []

while len(circle) != 0:
    for i in circle:
        index += k - 1
        while index >= len(circle):
            index -= len(circle)
        result.append(circle[index])
        circle.remove(circle[index])

print("[" + ",".join(result) + "]")
