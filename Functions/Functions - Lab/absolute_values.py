nums_data = input().split(" ")


def solve(nums):
    abs_nums = list(map(float, nums_data))
    abs_nums = [abs(x) for x in abs_nums]
    return abs_nums


print(solve(nums_data))
