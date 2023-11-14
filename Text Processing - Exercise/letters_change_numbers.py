strings = input().split()
number = ""
final_sum = 0


for string in strings:
    first_letter = ord(string[0].lower()) - 96
    second_letter = ord(string[-1].lower()) - 96

    if string[0].isupper():
        for char in range(len(string)):
            if string[char].isdigit():
                number += string[char]
        number = int(number)
        number /= first_letter
        number /= second_letter

    elif string[0].islower():


