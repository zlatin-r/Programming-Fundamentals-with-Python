operator = input()
a = int(input())
b = int(input())


def solve(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(solve(a, b, operator))
