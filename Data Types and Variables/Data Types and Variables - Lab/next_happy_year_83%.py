year = int(input())

while True:
    year += 1

    digit_1 = year // 1000
    digit_2 = year % 1000 // 100
    digit_3 = year % 100 // 10
    digit_4 = year % 10

    if digit_1 == digit_2 or digit_1 == digit_3 or digit_1 == digit_4:
        continue
    if digit_2 == digit_1 or digit_2 == digit_3 or digit_2 == digit_4:
        continue
    if digit_3 == digit_1 or digit_3 == digit_2 or digit_3 == digit_4:
        continue
    if digit_4 == digit_1 or digit_4 == digit_2 or digit_4 == digit_3:
        continue

    else:
        print(year)
        break
