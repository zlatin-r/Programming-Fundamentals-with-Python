import re

full_names_input = input()
pattern = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"

matches = re.findall(pattern, full_names_input)

print(" ".join(matches))

