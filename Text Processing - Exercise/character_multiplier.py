string_1, string_2 = input().split()
i = 0
n = 0
total_sum = 0

while i < max(len(string_1), len(string_2)):
    total_sum += ord(string_1[i]) * ord(string_2[n])
    if i == min(len(string_1), len(string_2)):
        i = 1
    elif n == min(len(string_1), len(string_2)):
        n = 1
    else:
        i += 1
        n += 1

print(total_sum)