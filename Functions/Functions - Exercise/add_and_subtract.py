a = int(input())
b = int(input())
c = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_subtract(a, b, c):
    result = sum_numbers(a, b)
    subtract_result = subtract(result, c)
    return subtract_result


print(add_subtract(a, b, c))
