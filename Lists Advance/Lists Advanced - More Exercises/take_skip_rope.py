initial_string = [x for x in input().split(" ")]
result = ""

number_list = [int(x) for x in initial_string if x.isdigit()]
non_numbers_list = [x for x in initial_string if x.isalpha()]

take_list = [x for x in number_list if number_list.index(x) % 2 == 0]
skip_list = [x for x in number_list if number_list.index(x) % 2 != 0]



