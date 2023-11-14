strings = input().split()
final_sum = 0

for string in strings:
    number = ""
    first_letter = ord(string[0].lower()) - 96
    second_letter = ord(string[-1].lower()) - 96

    for char in range(len(string)):
        if string[char].isdigit():
            number += string[char]
    number = int(number)

    if string[0].isupper():
        number /= first_letter
    else:
        number *= first_letter

    if string[-1].isupper():
        number -= second_letter
    else:
        number += second_letter

    final_sum += number

print(f"{final_sum:.2f}")
