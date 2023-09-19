numbers = input().split(" ")


def min_max_sum(numbers):
    numbers = list(map(int, numbers))
    min_num = min(numbers)
    max_num = max(numbers)
    sum_num = sum(numbers)
    return (f"The minimum number is {min_num}\n"
            f"The maximum number is {max_num}\n"
            f"The sum number is: {sum_num}")


print(min_max_sum(numbers))
