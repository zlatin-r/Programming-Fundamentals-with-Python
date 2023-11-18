import re

line = input()

regex = r"\d+"

while line:
    match = re.findall(regex, line)
    if match:
        print(" ".join(match), end=" ")
    line = input()
