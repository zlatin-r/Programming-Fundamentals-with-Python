numbers = input().split(", ")

positive_numbers = [x for x in numbers if int(x) >= 0]
positive = ", ".join(positive_numbers)
negative_numbers = [x for x in numbers if int(x) < 0]
negative = ", ".join(negative_numbers)
even_numbers = [x for x in numbers if int(x) % 2 == 0]
even = ", ".join(even_numbers)
odd_numbers = [x for x in numbers if int(x) % 2 != 0]
odd = ", ".join(odd_numbers)

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")