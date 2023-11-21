import re

pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"

string = input()
destinations = []
total_len = 0

matches = re.findall(pattern, string)

for place in matches:
    destinations.append(place[1])
    total_len += len(place[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_len}")
