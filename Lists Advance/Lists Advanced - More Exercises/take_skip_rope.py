initial_string = list(input())
result = ""

number_list = [int(x) for x in initial_string if x.isdigit()]
non_numbers_list = [x for x in initial_string if not x.isdigit()]

take_list = [number for index, number in enumerate(number_list) if index % 2 == 0]
skip_list = [number for index, number in enumerate(number_list) if index % 2 != 0]





