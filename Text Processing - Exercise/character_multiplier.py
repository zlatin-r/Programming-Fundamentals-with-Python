string_1, string_2 = input().split()
total_sum = 0

if len(string_1) > len(string_2):
    for index in range(len(string_2)):
        total_sum += ord(string_1[index]) * ord(string_2[index])

    diff = len(string_1) - len(string_2)

    for index in range(len(string_1[-diff:])):
        total_sum += ord(string_1[-diff:][index])

elif len(string_1) < len(string_2):
    for index in range(len(string_1)):
        total_sum += ord(string_1[index]) * ord(string_2[index])

    diff = len(string_2) - len(string_1)

    for index in range(len(string_2[-diff:])):
        total_sum += ord(string_2[-diff:][index])

elif len(string_1) == len(string_2):
    for index in range(len(string_1)):
        total_sum += ord(string_1[index]) * ord(string_2[index])

print(total_sum)
