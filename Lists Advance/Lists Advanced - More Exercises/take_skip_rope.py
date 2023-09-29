initial_string = list(input())
result = ""

number_list = [int(x) for x in initial_string if x.isdigit()]
non_numbers_list = [x for x in initial_string if not x.isdigit()]

take_list = [number for index, number in enumerate(number_list) if index % 2 == 0]
skip_list = [number for index, number in enumerate(number_list) if index % 2 != 0]

count = len(take_list)

while count > 0:
    for m in take_list:
        taken_string = non_numbers_list[0:m]
        result += "".join(taken_string)
        non_numbers_list = non_numbers_list[m:]
        take_list.remove(m)
        break

    for n in skip_list:
        non_numbers_list = non_numbers_list[n:]
        skip_list.remove(n)
        break
    count -= 1

print(result)
