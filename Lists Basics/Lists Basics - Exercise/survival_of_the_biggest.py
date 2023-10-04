input_numbers = list(map(int, input().split()))
n = int(input())
new_list = []
result = []

for i in input_numbers:
    new_list.append(i)
    new_list.sort()
to_remove = new_list[:n]

for j in range(len(input_numbers)):
    if input_numbers[j] not in to_remove:
        result.append(input_numbers[j])

string_nums = [str(num) for num in result]

print(", ".join(string_nums))
