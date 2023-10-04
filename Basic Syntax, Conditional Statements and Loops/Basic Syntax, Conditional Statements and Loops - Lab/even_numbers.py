n = int(input())
result = "All numbers are even."

for i in range(n):
    num = int(input())

    if num % 2 == 1:
        result = f"{num} is odd!"
        break

print(result)
