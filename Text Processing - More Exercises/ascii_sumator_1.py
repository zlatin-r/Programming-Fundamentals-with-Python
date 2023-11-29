ord_value_1 = ord(input())
ord_value_2 = ord(input())
string = input()

sum_values = 0

for i in string:
    if ord_value_1 < ord(i) < ord_value_2:
        sum_values += ord(i)

print(sum_values)
