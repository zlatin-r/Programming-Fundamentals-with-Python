import re

pattern = r"\b\+359 (2)([ |-]?\d{3}){2}\b"
numbers = input()

matches = re.findall(pattern, numbers)

print(" ".join(matches))