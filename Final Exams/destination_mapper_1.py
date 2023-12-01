import re

initial_string = input()
travel_points = 0
destinations = []

pattern = r"([=/])([A-Z][a-z]{2,})\1"

matches = re.findall(pattern, initial_string)

for match in matches:
    travel_points += len(match[1])
    destinations.append(match[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
