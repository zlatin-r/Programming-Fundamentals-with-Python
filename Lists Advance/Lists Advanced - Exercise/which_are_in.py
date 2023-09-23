first_sequence = input().split(", ")
second_sequence = input().split(", ")
result = []

for string in first_sequence:
    for second_string in second_sequence:
        if string in second_string:
            if string in result:
                continue
            else:
                result.append(string)

print(result)
