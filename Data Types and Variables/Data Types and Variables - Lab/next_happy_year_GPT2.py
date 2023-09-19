year = int(input())

while True:
    year += 1
    year_str = str(year)
    is_happy_year = True
    for i in range(len(year_str)):
        for j in range(i + 1, len(year_str)):
            if year_str[i] == year_str[j]:
                is_happy_year = False
                break
        if not is_happy_year:
            break
    if is_happy_year:
        print(year)
        break
