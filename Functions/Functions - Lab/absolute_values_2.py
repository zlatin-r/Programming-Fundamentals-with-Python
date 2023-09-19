numbers = input().split(" ")
abs_nums = list(map(float, numbers))
abs_nums = [abs(x) for x in abs_nums]
print(abs_nums)
