import re

text = input()
total_calories = 0

pattern = r"([|#])([A-Za-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1(\d+)\1"
matches = re.findall(pattern, text)

for match in matches:
    total_calories += int(match[3])
print(f"You have food to last you for: {total_calories // 2000} days!")

for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
