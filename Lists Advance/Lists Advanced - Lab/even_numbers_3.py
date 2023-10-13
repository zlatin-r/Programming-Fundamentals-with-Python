numbers = list(map(int, input().split(", ")))

even_nums = [numbers.index(x) for x in numbers if x % 2 == 0]

print(even_nums)