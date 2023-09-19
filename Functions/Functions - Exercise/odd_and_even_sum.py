number_string = input()


def odd_even_sum(number_string):
    odd_digits = [int(x) for x in number_string if int(x) % 2 != 0]
    even_digits = [int(x) for x in number_string if int(x) % 2 == 0]

    return f"Odd sum = {sum(odd_digits)}, Even sum = {sum(even_digits)}"


print(odd_even_sum(number_string))
