numbers = input().split(" ")


def round_nums(numbers):
    rounded_nums = [round(float(num)) for num in numbers]
    return rounded_nums


print(round_nums(numbers))
