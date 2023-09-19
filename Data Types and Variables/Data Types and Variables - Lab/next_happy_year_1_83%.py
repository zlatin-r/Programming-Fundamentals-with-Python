year = int(input())

while True:
    year += 1

    digit_1 = year // 1000
    digit_2 = year % 1000 // 100
    digit_3 = year % 100 // 10
    digit_4 = year % 10

    set_year = {digit_1, digit_2, digit_3, digit_4}

    prev = len(set_year)
    prev2 = len(str(year))

    if len(set_year) == len(str(year)):
        print(year)
        break




