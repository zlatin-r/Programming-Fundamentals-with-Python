import re

pattern = r"\b_([A-Za-z0-9]+)\b"

line = input()

matches = re.findall(pattern, line)

print(",".join(matches))
