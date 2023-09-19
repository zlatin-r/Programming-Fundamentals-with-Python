number_string = input().split(" ")


def even_nums(number_string):
    return [int(x) for x in number_string if int(x) % 2 == 0]


print(even_nums(number_string))

