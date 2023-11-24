import re

pattern = r"([|#])([A-Za-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1"

text = input()
food_data = list()
total_calories = 0

matches = re.findall(pattern, text)

for match in matches:
    total_calories += int(match[3])
    food_data.append({"food": match[1], "date": match[2], "calories": match[3]})
print(f"You have food to last you for: {total_calories // 2000} days!")

for item in food_data:
    print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['calories']}")
