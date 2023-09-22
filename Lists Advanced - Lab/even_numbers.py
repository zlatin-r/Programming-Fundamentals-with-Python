numbers = input().split(", ")
even_indices = []

for number in numbers:
    if int(number) % 2 == 0:
        even_indices.append(numbers.index(number))

print(even_indices)
